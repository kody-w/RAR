---
name: "rar-kody-w-play-youtube-video"
description: "Open YouTube in the local user's default browser when the user asks to play, watch, find, or open a YouTube video. A message beginning with 'youtube:' is an explicit trigger. Pass a video title or an official YouTube URL. Do not use this tool to download, copy, extract, or bypass access controls for media."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/play_youtube_video_agent", "rar_sha256": "fa592979b08d6ddeddcc1c6ebd54318f5fd3e37a528d2d22958078a5a514dafb", "source_kind": "rar-agent", "source_commit": "ed86f3685a8d6f3199cb12a61ee1143d619692f7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "play_youtube_video_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/play-youtube-video:57d7c8b458360cfcdbd2ceaf3b6a20cd013155f34e6c1de1ae0322ab1ec5a280", "kind": "skill"}, "author": "RAPP Community", "tags": ["youtube", "video", "browser", "media"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/play_youtube_video_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `play_youtube_video_agent.py` is
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
