"""Generate Azure GPT Image artwork, save it locally, and open it."""

import base64
import json
import os
import webbrowser
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlencode, urlparse

import requests

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/art_generator_agent",
    "version": "1.0.0",
    "display_name": "Art Generator",
    "description": (
        "Generates original PNG artwork with Azure GPT Image 2, falls back "
        "to GPT Image 1.5 on failure, saves it locally, and optionally opens it."
    ),
    "author": "RAPP Community",
    "tags": ["art", "image-generation", "azure-openai", "creative"],
    "category": "creative",
    "quality_tier": "community",
    "requires_env": ["AZURE_OPENAI_ENDPOINT"],
    "dependencies": ["@rapp/basic_agent"],
    "external_prereqs": [
        "Azure CLI login or managed identity",
        "Azure OpenAI GPT Image deployments",
    ],
    "example_call": {
        "args": {
            "description": "A detailed original illustration",
            "quality": "medium",
        }
    },
}


_TOKEN_SCOPE = "https://cognitiveservices.azure.com/.default"
_DEFAULT_API_VERSION = "2025-04-01-preview"
_DEFAULT_DEPLOYMENT = "gpt-image-2"
_DEFAULT_FALLBACK_DEPLOYMENT = "gpt-image"
_ART_DIR = (
    Path(__file__).resolve().parents[1]
    / ".brainstem_data"
    / "art"
)
_PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
_SUPPORTED_SIZES = frozenset({
    "1024x1024",
    "1024x1536",
    "1536x1024",
})
_SUPPORTED_QUALITIES = frozenset({"low", "medium", "high"})


def _get_access_token():
    try:
        from azure.identity import AzureCliCredential, ManagedIdentityCredential
    except ImportError as exc:
        raise RuntimeError(
            "Azure authentication requires the azure-identity package."
        ) from exc

    if os.getenv("WEBSITE_INSTANCE_ID"):
        credential = ManagedIdentityCredential()
    else:
        credential = AzureCliCredential()
    return credential.get_token(_TOKEN_SCOPE).token


def _get_api_config():
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "").strip().rstrip("/")
    if not endpoint:
        raise RuntimeError(
            "Set AZURE_OPENAI_ENDPOINT before using ArtGenerator."
        )

    parsed = urlparse(endpoint)
    if parsed.scheme != "https" or not parsed.netloc:
        raise RuntimeError(
            "AZURE_OPENAI_ENDPOINT must be a valid HTTPS endpoint."
        )

    primary_deployment = os.getenv(
        "AZURE_OPENAI_IMAGE_DEPLOYMENT",
        _DEFAULT_DEPLOYMENT,
    ).strip()
    if not primary_deployment:
        raise RuntimeError(
            "AZURE_OPENAI_IMAGE_DEPLOYMENT cannot be empty."
        )

    fallback_deployment = os.getenv(
        "AZURE_OPENAI_IMAGE_FALLBACK_DEPLOYMENT",
        _DEFAULT_FALLBACK_DEPLOYMENT,
    ).strip()
    if not fallback_deployment:
        raise RuntimeError(
            "AZURE_OPENAI_IMAGE_FALLBACK_DEPLOYMENT cannot be empty."
        )

    deployments = tuple(dict.fromkeys((
        primary_deployment,
        fallback_deployment,
    )))

    api_version = (
        os.getenv("AZURE_OPENAI_IMAGE_API_VERSION")
        or os.getenv("AZURE_OPENAI_API_VERSION")
        or _DEFAULT_API_VERSION
    ).strip()
    if not api_version:
        raise RuntimeError(
            "AZURE_OPENAI_IMAGE_API_VERSION cannot be empty."
        )

    return endpoint, deployments, api_version


def _azure_error_message(response):
    try:
        payload = response.json()
    except requests.exceptions.JSONDecodeError:
        return response.text[:500].strip() or response.reason

    error = payload.get("error") if isinstance(payload, dict) else None
    if isinstance(error, dict):
        return str(error.get("message") or error.get("code") or error)
    return str(error or payload)[:500]


def _request_image_from_deployment(
    endpoint,
    deployment,
    api_version,
    access_token,
    prompt,
    size,
    quality,
):
    url = (
        f"{endpoint}/openai/deployments/{quote(deployment, safe='')}"
        f"/images/generations?{urlencode({'api-version': api_version})}"
    )
    try:
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            },
            json={
                "prompt": prompt,
                "n": 1,
                "size": size,
                "quality": quality,
                "output_format": "png",
            },
            timeout=180,
        )
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(
            f"Azure image generation request failed on {deployment}: {exc}"
        ) from exc

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as exc:
        message = _azure_error_message(response)
        raise RuntimeError(
            f"Azure image generation failed on {deployment} "
            f"({response.status_code}): {message}"
        ) from exc

    try:
        payload = response.json()
    except requests.exceptions.JSONDecodeError as exc:
        raise RuntimeError(
            f"Azure image generation on {deployment} returned invalid JSON."
        ) from exc

    data = payload.get("data") if isinstance(payload, dict) else None
    encoded_image = (
        data[0].get("b64_json")
        if isinstance(data, list)
        and data
        and isinstance(data[0], dict)
        else None
    )
    if not encoded_image:
        raise RuntimeError(
            f"Azure image generation on {deployment} returned no image data."
        )

    try:
        image_bytes = base64.b64decode(encoded_image, validate=True)
    except (ValueError, TypeError) as exc:
        raise RuntimeError(
            f"Azure image generation on {deployment} returned invalid "
            "base64 image data."
        ) from exc
    if not image_bytes.startswith(_PNG_SIGNATURE):
        raise RuntimeError(
            f"Azure image generation on {deployment} returned an "
            "unexpected image format."
        )

    return image_bytes


def _request_image(prompt, size, quality):
    endpoint, deployments, api_version = _get_api_config()
    access_token = _get_access_token()
    failures = []
    last_error = None

    for deployment in deployments:
        try:
            image_bytes = _request_image_from_deployment(
                endpoint,
                deployment,
                api_version,
                access_token,
                prompt,
                size,
                quality,
            )
        except RuntimeError as exc:
            failures.append(str(exc))
            last_error = exc
            continue
        return image_bytes, deployment

    raise RuntimeError(
        "Azure image generation failed for all configured deployments: "
        + " | ".join(failures)
    ) from last_error


def _save_image(image_bytes):
    _ART_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")
    image_path = _ART_DIR / f"generated_art_{timestamp}.png"
    temp_path = image_path.with_name(
        f".{image_path.name}.{os.getpid()}.tmp"
    )

    try:
        with temp_path.open("wb") as output:
            output.write(image_bytes)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temp_path, image_path)
    finally:
        if temp_path.exists():
            temp_path.unlink()

    return image_path


class ArtGeneratorAgent(BasicAgent):
    def __init__(self):
        self.name = "ArtGenerator"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generate original art with Azure GPT Image 2, falling back "
                "to GPT Image 1.5 only if generation fails, and save it "
                "locally. Use this tool when the user asks to create, draw, "
                "illustrate, or generate an image. A message beginning with "
                "'art:' is an explicit trigger."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string",
                        "maxLength": 4000,
                        "description": (
                            "A detailed text prompt describing the original "
                            "image to generate."
                        ),
                    },
                    "size": {
                        "type": "string",
                        "enum": sorted(_SUPPORTED_SIZES),
                        "default": "1024x1024",
                        "description": "Dimensions of the generated image.",
                    },
                    "quality": {
                        "type": "string",
                        "enum": sorted(_SUPPORTED_QUALITIES),
                        "default": "medium",
                        "description": "Generation quality and cost level.",
                    },
                    "open_in_browser": {
                        "type": "boolean",
                        "default": True,
                        "description": (
                            "Open the saved image in the local default browser."
                        ),
                    },
                },
                "required": ["description"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(
        self,
        description="",
        size="1024x1024",
        quality="medium",
        open_in_browser=True,
        **kwargs,
    ):
        if not isinstance(description, str) or not description.strip():
            return json.dumps({
                "status": "error",
                "message": "A non-empty art description is required.",
            })
        prompt = description.strip()
        if len(prompt) > 4000:
            raise ValueError(
                "The art description must be 4000 characters or fewer."
            )
        if size not in _SUPPORTED_SIZES:
            raise ValueError(f"Unsupported image size: {size}")
        if quality not in _SUPPORTED_QUALITIES:
            raise ValueError(f"Unsupported image quality: {quality}")
        if not isinstance(open_in_browser, bool):
            raise ValueError("open_in_browser must be a boolean.")

        try:
            image_bytes, deployment = _request_image(prompt, size, quality)
        except RuntimeError as exc:
            return json.dumps({
                "status": "error",
                "message": str(exc),
            })
        image_path = _save_image(image_bytes)
        browser_opened = (
            webbrowser.open_new_tab(image_path.as_uri())
            if open_in_browser
            else False
        )

        return json.dumps({
            "status": "saved",
            "file_path": str(image_path),
            "deployment": deployment,
            "browser_opened": browser_opened,
            "message": "Generated art was saved locally.",
        })


if __name__ == "__main__":
    print(ArtGeneratorAgent().perform())
