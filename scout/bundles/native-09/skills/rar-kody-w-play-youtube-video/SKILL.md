---
name: "rar-kody-w-play-youtube-video"
description: "Open YouTube in the local user's default browser when the user asks to play, watch, find, or open a YouTube video. A message beginning with 'youtube:' is an explicit trigger. Pass a video title or an official YouTube URL. Do not use this tool to download, copy, extract, or bypass access controls for media."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/play_youtube_video_agent", "rar_sha256": "ba4da935eacacd05f6e4f7c8fb3acfcce6277922ff3ac78b0bef7fb4fb3cc8b6", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "RAPP Community", "tags": ["youtube", "video", "browser", "media"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/play_youtube_video_agent`. The original RAPP
agent is preserved byte-for-byte in `play_youtube_video_agent.py` and in the RCI capsule.

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

Open an official YouTube URL or title search in the default browser.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "video_title": {
      "description": "The requested video title, optional 'youtube:' trigger followed by a title, or official YouTube URL.",
      "maxLength": 500,
      "type": "string"
    }
  },
  "required": [
    "video_title"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `play_youtube_video_agent.py` and embedded as the fenced Python below (sha256 ba4da935eacacd05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `play_youtube_video_agent.py` first:

```bash
python3 play_youtube_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 play_youtube_video_agent.py   # or on stdin
python3 play_youtube_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/play_youtube_video_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/play_youtube_video_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/play_youtube_video_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Open an official YouTube URL or title search in the default browser."""

import json
import webbrowser
from urllib.parse import urlencode, urlparse, urlunparse

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/play_youtube_video_agent",
    "version": "1.0.0",
    "display_name": "Play YouTube Video",
    "description": (
        "Opens official YouTube URLs or title searches in the local default "
        "browser without downloading or extracting media."
    ),
    "author": "RAPP Community",
    "tags": ["youtube", "video", "browser", "media"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "external_prereqs": ["A local graphical default browser"],
    "example_call": {"args": {"video_title": "lo-fi beats"}},
}


_TRIGGER_PREFIX = "youtube:"
_ALLOWED_YOUTUBE_HOSTS = frozenset({
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "music.youtube.com",
    "youtu.be",
    "www.youtu.be",
    "youtube-nocookie.com",
    "www.youtube-nocookie.com",
})
_SCHEMELESS_YOUTUBE_PREFIXES = tuple(
    f"{host}/" for host in _ALLOWED_YOUTUBE_HOSTS
)
_REDIRECT_PATHS = frozenset({"/attribution_link", "/redirect"})


def _build_youtube_url(video_title):
    if not isinstance(video_title, str):
        raise ValueError("video_title must be a string.")

    request = video_title.strip()
    if request.lower().startswith(_TRIGGER_PREFIX):
        request = request[len(_TRIGGER_PREFIX):].strip()

    if not request:
        raise ValueError("A YouTube video title or URL is required.")
    if len(request) > 500:
        raise ValueError("The YouTube request must be 500 characters or fewer.")

    candidate = request
    if candidate.lower().startswith(_SCHEMELESS_YOUTUBE_PREFIXES):
        candidate = f"https://{candidate}"

    parsed = urlparse(candidate)
    if parsed.scheme or parsed.netloc:
        if parsed.scheme.lower() not in {"http", "https"}:
            raise ValueError("Only HTTP(S) YouTube URLs are supported.")

        try:
            port = parsed.port
        except ValueError as exc:
            raise ValueError("The YouTube URL contains an invalid port.") from exc

        hostname = (parsed.hostname or "").lower()
        if (
            hostname not in _ALLOWED_YOUTUBE_HOSTS
            or parsed.username is not None
            or parsed.password is not None
            or port is not None
        ):
            raise ValueError("Only official YouTube URLs are supported.")
        if parsed.path.rstrip("/").lower() in _REDIRECT_PATHS:
            raise ValueError("YouTube redirect URLs are not supported.")

        return urlunparse((
            "https",
            hostname,
            parsed.path or "/",
            parsed.params,
            parsed.query,
            parsed.fragment,
        ))

    return "https://www.youtube.com/results?" + urlencode({
        "search_query": request,
    })


class PlayYoutubeVideoAgent(BasicAgent):
    def __init__(self):
        self.name = "PlayYoutubeVideo"
        self.metadata = {
            "name": self.name,
            "description": (
                "Open YouTube in the local user's default browser when the user "
                "asks to play, watch, find, or open a YouTube video. A message "
                "beginning with 'youtube:' is an explicit trigger. Pass a video "
                "title or an official YouTube URL. Do not use this tool to "
                "download, copy, extract, or bypass access controls for media."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "video_title": {
                        "type": "string",
                        "maxLength": 500,
                        "description": (
                            "The requested video title, optional 'youtube:' "
                            "trigger followed by a title, or official YouTube URL."
                        ),
                    },
                },
                "required": ["video_title"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, video_title="", **kwargs):
        if video_title == "":
            return json.dumps({
                "status": "error",
                "message": "A YouTube video title or URL is required.",
            })
        url = _build_youtube_url(video_title)
        if not webbrowser.open_new_tab(url):
            raise RuntimeError(
                "The local default browser could not open the YouTube URL."
            )

        return json.dumps({
            "status": "opened",
            "url": url,
            "message": "YouTube opened in the local default browser.",
        })


if __name__ == "__main__":
    print(PlayYoutubeVideoAgent().perform())
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
