---
name: "rar-kody-w-play-youtube-video"
description: "Open YouTube in the local user's default browser when the user asks to play, watch, find, or open a YouTube video. A message beginning with 'youtube:' is an explicit trigger. Pass a video title or an official YouTube URL. Do not use this tool to download, copy, extract, or bypass access controls for media."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/play_youtube_video_agent", "rar_sha256": "ba4da935eacacd05f6e4f7c8fb3acfcce6277922ff3ac78b0bef7fb4fb3cc8b6", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "RAPP Community", "tags": ["youtube", "video", "browser", "media"]}
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
