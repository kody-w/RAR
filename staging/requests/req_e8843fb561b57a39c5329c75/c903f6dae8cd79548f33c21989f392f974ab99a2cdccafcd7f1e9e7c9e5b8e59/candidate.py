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
