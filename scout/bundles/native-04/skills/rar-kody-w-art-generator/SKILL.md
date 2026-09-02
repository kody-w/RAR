---
name: "rar-kody-w-art-generator"
description: "Generates original PNG artwork with Azure GPT Image 2, falls back to GPT Image 1.5 on failure, saves it locally, and optionally opens it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/art_generator_agent", "rar_sha256": "abf32aa1c916a7c4b1606e434d3468e2f75c4bd725eafc304f022aeaae489712", "source_kind": "rar-agent", "source_commit": "9338f55e48447eed9c37c29f99f03a30fdc4bb92", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "art_generator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/art-generator:eb37ea0b483c4dbd52cd93433ac199ebbcca417d13126088378d7fd980c06bfc", "kind": "skill"}, "author": "RAPP Community", "tags": ["art", "image-generation", "azure-openai", "creative"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/art_generator_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `art_generator_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
