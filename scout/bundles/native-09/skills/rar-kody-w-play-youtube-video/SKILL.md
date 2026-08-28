---
name: "rar-kody-w-play-youtube-video"
description: "Open YouTube in the local user's default browser when the user asks to play, watch, find, or open a YouTube video. A message beginning with 'youtube:' is an explicit trigger. Pass a video title or an official YouTube URL. Do not use this tool to download, copy, extract, or bypass access controls for media."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/play_youtube_video_agent", "rar_sha256": "fa592979b08d6ddeddcc1c6ebd54318f5fd3e37a528d2d22958078a5a514dafb", "source_kind": "rar-agent", "source_commit": "ed86f3685a8d6f3199cb12a61ee1143d619692f7", "author": "RAPP Community", "tags": ["youtube", "video", "browser", "media"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `play_youtube_video_agent.py` and embedded as the fenced Python below (sha256 fa592979b08d6dde…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `play_youtube_video_agent.py` first:

```bash
python3 play_youtube_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 play_youtube_video_agent.py   # or on stdin
python3 play_youtube_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
