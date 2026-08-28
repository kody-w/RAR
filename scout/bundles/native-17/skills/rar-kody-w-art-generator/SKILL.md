---
name: "rar-kody-w-art-generator"
description: "Generates original PNG artwork with Azure GPT Image 2, falls back to GPT Image 1.5 on failure, saves it locally, and optionally opens it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/art_generator_agent", "rar_sha256": "abf32aa1c916a7c4b1606e434d3468e2f75c4bd725eafc304f022aeaae489712", "source_kind": "rar-agent", "source_commit": "9338f55e48447eed9c37c29f99f03a30fdc4bb92", "author": "RAPP Community", "tags": ["art", "image-generation", "azure-openai", "creative"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/art_generator_agent`. The original RAPP
agent is preserved byte-for-byte in `art_generator_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Generate Azure GPT Image artwork, save it locally, and open it.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `art_generator_agent.py` and embedded as the fenced Python below (sha256 abf32aa1c916a7c4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `art_generator_agent.py` first:

```bash
python3 art_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 art_generator_agent.py   # or on stdin
python3 art_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
