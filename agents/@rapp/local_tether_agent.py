"""local_tether_agent.py — serve the RAPP tether locally + auto-open browser.

Why this exists
───────────────
The live tether at https://kody-w.github.io/RAPP/pages/tether.html can't
fetch http://localhost:7071/chat — browsers block "mixed content"
(HTTPS→HTTP) regardless of CORS. The work-around without tunnels or
self-signed certs is to serve the tether itself over plain HTTP on
localhost. Then:

  • Desktop runs http://localhost:8000/pages/tether.html
    → can freely fetch http://localhost:7071/chat (same scheme).
    → can also fetch https://kody-w.github.io/rapp-commons/neighborhood.json
      (HTTP page reading HTTPS resources is always allowed).
  • Phone scans the desktop's "📱 Invite a device" QR — that QR encodes
    the LIVE HTTPS tether (kody-w.github.io/RAPP/pages/tether.html) with
    the neighborhood pre-loaded, so the phone never touches localhost.
  • Both meet in the same lobby via the PeerJS broker (both compute the
    same rapp-<rappid-hash>-host peer ID from the same neighborhood).
  • Operator taps "🌐 Ground tether to local brainstem" on the DESKTOP
    (which is now on HTTP, no mixed-content) → phone-tethered guests'
    messages route through the host's local brainstem.

Architecture: agent runs a stdlib http.server in a daemon thread inside
the brainstem process, serving the RAPP repo root that the installer
unpacked at ~/.brainstem/src/. Pure stdlib — no Flask, no extra deps.

Actions: start (default) · stop · status.
"""

from __future__ import annotations

import functools
import http.server
import os
import socketserver
import threading
import urllib.parse
import webbrowser

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:
        class BasicAgent:  # type: ignore
            def __init__(self, name, metadata):
                self.name = name
                self.metadata = metadata


__manifest__ = {
    "schema":       "rapp-agent/1.0",
    "name":         "@rapp/local_tether",
    "version":      "1.0.0",
    "display_name": "LocalTether",
    "description": (
        "Serves the RAPP tether locally on http://localhost:8000 so it "
        "can freely talk to the brainstem at localhost:7071 (no "
        "mixed-content blocking). Auto-opens the browser pre-tethered "
        "to the requested neighborhood (commons by default). Phone "
        "guests join via the live HTTPS tether — both meet in the "
        "same lobby through the PeerJS broker."
    ),
    "author":      "Kody",
    "tags":        ["tether", "lobby", "local-server", "mixed-content-fix"],
    "category":    "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {"args": {"action": "start"}},
}


# Module-level singleton so subsequent calls can stop / status the server
# without re-binding the port. Lives for the lifetime of the brainstem
# process (which is exactly the right scope — when brainstem exits the
# daemon thread is killed too).
_state: dict = {
    "server": None,
    "thread": None,
    "port":   None,
    "served_from": None,
    "neighborhood": None,
    "url": None,
}

DEFAULT_PORT = 8000
DEFAULT_NEIGHBORHOOD = "https://kody-w.github.io/rapp-commons/neighborhood.json"

# Probe a handful of conventional install paths (in order) so the agent
# works regardless of how the operator landed on this code.
_CANDIDATE_ROOTS = [
    os.path.expanduser("~/.brainstem/src"),                 # one-liner install
    os.path.expanduser("~/Documents/GitHub/RAPP"),          # dev clone
    os.path.expanduser("~/RAPP"),                           # short dev clone
    os.environ.get("RAPP_ROOT", ""),                        # explicit override
]


def _find_repo_root() -> str | None:
    for r in _CANDIDATE_ROOTS:
        if not r:
            continue
        if os.path.isfile(os.path.join(r, "pages", "tether.html")):
            return r
    return None


class LocalTetherAgent(BasicAgent):
    def __init__(self):
        self.name = "LocalTether"
        self.metadata = {
            "name": self.name,
            "description": (
                "Serve the RAPP tether on http://localhost:<port> so it can "
                "talk to your local brainstem freely (no mixed-content). "
                "Auto-opens the browser. Phone-tethered guests join via "
                "the live HTTPS tether + the PeerJS lobby broker. "
                "Actions: start / stop / status."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["start", "stop", "status"],
                        "description": "start = begin serving + open browser; stop = shut down server; status = report current state.",
                    },
                    "neighborhood": {
                        "type": "string",
                        "description": "Neighborhood URL to pre-tether the browser to. Default: RAPP Commons. Pass empty string to land in scan-mode (no auto-tether).",
                    },
                    "port": {
                        "type": "integer",
                        "description": f"Local HTTP port to bind (default {DEFAULT_PORT}).",
                    },
                    "open_browser": {
                        "type": "boolean",
                        "description": "Open the browser automatically after start (default true).",
                    },
                    "served_from": {
                        "type": "string",
                        "description": "Override the directory served (default: auto-detect ~/.brainstem/src or your RAPP clone).",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── action dispatch ───────────────────────────────────────────────

    def perform(self, **kwargs) -> str:
        action = (kwargs.get("action") or "start").strip().lower()
        if action == "start":
            return self._start(
                port=int(kwargs.get("port") or DEFAULT_PORT),
                neighborhood=kwargs.get("neighborhood", DEFAULT_NEIGHBORHOOD),
                open_browser=bool(kwargs.get("open_browser", True)),
                served_from=kwargs.get("served_from") or None,
            )
        if action == "stop":
            return self._stop()
        if action == "status":
            return self._status()
        return f"unknown action: '{action}'. Valid: start, stop, status."

    # ── start ─────────────────────────────────────────────────────────

    def _start(self, port: int, neighborhood: str | None,
               open_browser: bool, served_from: str | None) -> str:
        if _state["thread"] and _state["thread"].is_alive():
            return (
                f"Local tether already running on http://localhost:{_state['port']} "
                f"(serving {_state['served_from']}). Use action='stop' first, "
                f"or action='status' for details."
            )

        root = served_from or _find_repo_root()
        if not root:
            return (
                "Could not find the RAPP repo root (looked in ~/.brainstem/src, "
                "~/Documents/GitHub/RAPP, ~/RAPP, $RAPP_ROOT). Pass served_from="
                "<absolute path to RAPP clone> explicitly."
            )
        tether_path = os.path.join(root, "pages", "tether.html")
        if not os.path.isfile(tether_path):
            return f"served_from={root} does not contain pages/tether.html — wrong directory?"

        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=root)

        try:
            server = ThreadingHTTPServer(("", port), handler)
        except OSError as e:
            return (
                f"Could not bind port {port}: {e}. Pass a different port "
                f"(e.g. port=8001) or stop whatever's holding it."
            )

        thread = threading.Thread(
            target=server.serve_forever,
            name=f"local-tether-{port}",
            daemon=True,
        )
        thread.start()

        _state["server"] = server
        _state["thread"] = thread
        _state["port"] = port
        _state["served_from"] = root
        _state["neighborhood"] = neighborhood or ""

        url = f"http://localhost:{port}/pages/tether.html"
        if neighborhood:
            url += "?neighborhood=" + urllib.parse.quote(neighborhood, safe="")
        _state["url"] = url

        if open_browser:
            try:
                webbrowser.open(url, new=2)
            except Exception:
                pass

        return (
            f"🟢 Local tether running on http://localhost:{port}\n"
            f"   serving:      {root}\n"
            f"   browser URL:  {url}\n"
            f"\n"
            f"This URL is HTTP — talks to brainstem at localhost:7071 freely "
            f"(no mixed-content). Phone guests scan the in-page 📱 invite QR "
            f"to join via the live HTTPS tether; lobby is broker-mediated "
            f"so both meet in the same room. Tap 🌐 Ground tether to local "
            f"brainstem on the desktop and the prompt accepts plain "
            f"http://localhost:7071/chat with no certificate dance."
        )

    # ── stop ──────────────────────────────────────────────────────────

    def _stop(self) -> str:
        if not _state["server"]:
            return "Local tether is not running."
        port = _state["port"]
        try:
            _state["server"].shutdown()
            _state["server"].server_close()
        except Exception as e:
            return f"Stop failed: {e}"
        _state.update(server=None, thread=None, port=None,
                      served_from=None, neighborhood=None, url=None)
        return f"🛑 Local tether on port {port} stopped."

    # ── status ────────────────────────────────────────────────────────

    def _status(self) -> str:
        if _state["thread"] and _state["thread"].is_alive():
            return (
                f"🟢 Running\n"
                f"   port:         {_state['port']}\n"
                f"   serving:      {_state['served_from']}\n"
                f"   neighborhood: {_state['neighborhood'] or '(scan mode)'}\n"
                f"   url:          {_state['url']}\n"
            )
        return "⚪ Not running. Call with action='start' to begin."


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    """A ThreadingMixIn HTTPServer so multiple requests (parallel agent/cart
    fetches from the same browser session) don't serialize."""
    daemon_threads = True
    allow_reuse_address = True
