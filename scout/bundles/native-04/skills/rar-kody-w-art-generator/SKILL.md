---
name: "rar-kody-w-art-generator"
description: "Generates original PNG artwork with Azure GPT Image 2, falls back to GPT Image 1.5 on failure, saves it locally, and optionally opens it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/art_generator_agent", "rar_sha256": "bc54973a21c902f273d1340391840ab8b1025232dadcd17175d0c1a2a77fd34c", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "RAPP Community", "tags": ["art", "image-generation", "azure-openai", "creative"]}
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
