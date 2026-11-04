---
name: "rar-kody-w-art-generator"
description: "Generates original PNG artwork with Azure GPT Image 2, falls back to GPT Image 1.5 on failure, saves it locally, and optionally opens it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/art_generator_agent", "rar_sha256": "bc54973a21c902f273d1340391840ab8b1025232dadcd17175d0c1a2a77fd34c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "RAPP Community", "tags": ["art", "image-generation", "azure-openai", "creative"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `art_generator_agent.py` and embedded as the fenced Python below (sha256 bc54973a21c902f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `art_generator_agent.py` first:

```bash
python3 art_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 art_generator_agent.py   # or on stdin
python3 art_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/art_generator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/art_generator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/art_generator_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
