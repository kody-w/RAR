"""
MatrixArena — a multi-tab "Matrix Arena" test harness for the live RAPP Commons.

It launches multiple real (headless) browser tabs into the SAME walkable PeerJS
world — one HOST (the leader / recorder / room opener) and N FOLLOWERS (replicas
that join the host's room) — and AUTONOMOUSLY drives + sync-tests them. The point:
let a developer "play as the leader" and verify host-led sync, navigation, signed
actions, and host succession against the actual published world.

What it does (action 'scenario'): opens the host tab (it opens a PeerJS room and
prints its room id to the console), opens N follower tabs joined to that room,
waits for presence/WebRTC to connect, then drives the HOST as the leader
(teleport, walk, a signed say() hello, enter the voxel game + place a block, enter
poker), then PROBES each follower to assert it MIRRORS the host — a remote presence
avatar is visible AND the host's signed say() shows up in the follower's signed
feed (the sync check) — then runs a SUCCESSION test by closing the host tab and
checking the senior follower survives and can open its own room. It screenshots
every tab and returns a JSON report. Drop-in BasicAgent; shells out to a Playwright
harness at ~/.brainstem/matrix_tabs.py using the brainstem venv python. No PII —
public world URL, ~ home expansion only.

Actions:
  scenario  (default) run the full host + N followers sync + succession test
  host      open a single host tab and report its room id + a probe
  join      join an existing room id and report a probe
  drive     drive one tab: an action (where/teleport/walk/say/enter/voxelPlace/...) with text/x/y/z
  probe     open a tab and report where/presence/feed/fractal
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/matrix_arena_agent",
    "version": "1.0.1",
    "display_name": "Matrix Arena",
    "description": "Drives multiple headless RAPP Commons browser tabs via a local Playwright harness to sync-test host-led presence, signed actions, and succession.",
    "author": "kody-w",
    "tags": [
        "commons",
        "multiplayer",
        "testing",
        "playwright",
        "webrtc"
    ],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}

import os
import json
import subprocess

try:
    from agents.basic_agent import BasicAgent  # RAR layout
except Exception:
    try:
        from basic_agent import BasicAgent
    except Exception:
        class BasicAgent:  # tiny stub so this file loads anywhere
            def __init__(self, name=None, metadata=None):
                if name is not None:
                    self.name = name
                if metadata is not None:
                    self.metadata = metadata

            def perform(self, **kwargs):
                return "Not implemented."


PY = os.path.expanduser("~/.brainstem/venv/bin/python")
HARNESS = os.path.expanduser("~/.brainstem/matrix_tabs.py")
LIVE = "https://kody-w.github.io/rapp-commons/commons.html"


def _py():
    return PY if os.path.exists(PY) else "python3"


def _run(args, timeout):
    """Run the harness, return (parsed_json_or_none, raw_stdout, stderr, code)."""
    try:
        r = subprocess.run(
            [_py(), HARNESS] + [str(a) for a in args],
            capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired as e:
        return None, (e.stdout or ""), "timeout after %ss" % timeout, 124
    except Exception as e:
        return None, "", "subprocess error: %s" % e, 1
    out = r.stdout or ""
    parsed = None
    # the harness prints a single JSON document; parse it (find first '{').
    brace = out.find("{")
    if brace >= 0:
        try:
            parsed = json.loads(out[brace:])
        except Exception:
            parsed = None
    return parsed, out, (r.stderr or ""), r.returncode


class MatrixArenaAgent(BasicAgent):
    def __init__(self):
        self.name = "MatrixArena"
        self.metadata = {
            "name": self.name,
            "description": (
                "Launch a multi-tab 'Matrix Arena' against the LIVE RAPP Commons world and autonomously "
                "sync-test it. It opens real headless browser tabs into one shared walkable PeerJS world: a "
                "HOST (the leader that opens the room and records) and N FOLLOWERS (replicas that join the "
                "host's room), then drives them on their own. Use this when the user wants to test the live "
                "commons, host-led sync, multiplayer presence, signed actions/feed relay, navigation, or host "
                "succession — i.e. to 'play as the leader' and prove followers mirror the host. ACTION 'scenario' "
                "(default) runs the full test: open the host (it mints a PeerJS room), open 'n_followers' "
                "followers joined to it, wait for presence to connect, DRIVE THE HOST as leader (teleport, walk, "
                "a SIGNED say() hello, enter the voxel game + place a block, enter poker), then PROBE each follower "
                "and assert it mirrors the host (a remote presence avatar is visible AND the host's signed say() "
                "appears in the follower's feed = the sync check), then a SUCCESSION test (close the host tab and "
                "verify the senior follower survives and can open its own room). It screenshots every tab to "
                "/tmp/matrix and returns a JSON report {host_room, players[], sync_ok, succession_ok, screenshots}. "
                "'seconds' tunes how long it lets things settle/relay. ACTION 'host' opens one host tab and reports "
                "its room id + a probe. ACTION 'join' joins an existing 'room' id and reports a probe. ACTION 'drive' "
                "drives one tab with an 'action' (where/teleport/walk/face/say/enter/voxelPlace/feed/minimap/residents/"
                "fractal/...) plus optional 'text' (for say/enter/goto) or numeric 'x','y','z' (for teleport/voxelPlace). "
                "ACTION 'probe' opens a tab and reports where/presence/feed/fractal. Headless, public world URL, no PII."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["scenario", "host", "join", "drive", "probe"],
                        "description": "scenario = full host + N followers sync + succession test (default); host = open one host tab + report room id; join = join an existing room id; drive = drive one tab with an action; probe = open a tab and report its state.",
                    },
                    "n_followers": {
                        "type": "integer",
                        "description": "scenario: how many FOLLOWER tabs to join to the host's room. Default 1.",
                    },
                    "seconds": {
                        "type": "integer",
                        "description": "scenario: settle/relay window in seconds (how long to let presence connect and signed events relay before asserting). Default 20.",
                    },
                    "room": {
                        "type": "string",
                        "description": "join: the PeerJS room id (the <ID> from a host's '?host=<ID>' line) to join.",
                    },
                    "name": {
                        "type": "string",
                        "description": "drive/probe: a label for the tab being driven/probed (e.g. 'host' or 'follower'). Cosmetic.",
                    },
                    "drive_action": {
                        "type": "string",
                        "description": "drive: the commonsAgent method to call on the tab, e.g. 'where','teleport','walk','face','goto','enter','interact','say','voxelPlace','feed','minimap','residents','fractal','timeOfDay'.",
                    },
                    "text": {
                        "type": "string",
                        "description": "drive: a string argument for the action (the message for say(); the name for enter()/goto(), e.g. 'voxel','poker'; the direction for walk(), e.g. 'forward').",
                    },
                    "steps": {
                        "type": "integer",
                        "description": "drive: number of steps for walk() (paired with text='forward'|'back'|'left'|'right').",
                    },
                    "x": {"type": "number", "description": "drive: x coordinate for teleport()/voxelPlace()."},
                    "y": {"type": "number", "description": "drive: y coordinate for teleport()/voxelPlace()."},
                    "z": {"type": "number", "description": "drive: z coordinate for teleport()/voxelPlace()."},
                    "block": {"type": "string", "description": "drive: block type for voxelPlace() (e.g. 'stone'). Default 'stone'."},
                    "url": {"type": "string", "description": "Optional commons URL override. Default the live Pages site."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ---- argument assembly for `drive` ----
    def _drive_args(self, kwargs):
        act = (kwargs.get("drive_action") or "where").strip()
        args = [act]
        if act in ("teleport",):
            args += [kwargs.get("x", 0), kwargs.get("y", 0), kwargs.get("z", 0)]
        elif act in ("voxelPlace",):
            args += [kwargs.get("x", 0), kwargs.get("y", 1), kwargs.get("z", 0), kwargs.get("block", "stone")]
        elif act in ("walk",):
            args += [kwargs.get("text", "forward"), kwargs.get("steps", 2)]
        elif act in ("say", "enter", "goto", "face", "setTimeOfDay"):
            if kwargs.get("text") is not None:
                args += [kwargs.get("text")]
        return args

    def perform(self, **kwargs):
        if not os.path.exists(HARNESS):
            return json.dumps({
                "schema": "rapp-result/1.0", "agent": self.name, "status": "error",
                "error": "harness missing at %s" % HARNESS,
            }, indent=2)

        action = (kwargs.get("action") or "scenario").strip().lower()
        url = (kwargs.get("url") or LIVE).strip()

        if action == "scenario":
            n = int(kwargs.get("n_followers") or 1)
            secs = int(kwargs.get("seconds") or 20)
            # budget: nav + joins + several settle windows + per-tab work, generous.
            timeout = 120 + (n * 30) + (secs * 4)
            report, raw, err, code = _run(["scenario", n, secs, url], timeout)
            if report is None:
                return json.dumps({
                    "schema": "rapp-result/1.0", "agent": self.name, "action": "scenario",
                    "status": "error", "error": (err or raw or "no report")[:600], "exit_code": code,
                }, indent=2)
            return json.dumps({
                "schema": "rapp-result/1.0", "agent": self.name, "action": "scenario",
                "status": "success",
                "host_room": report.get("host_room"),
                "sync_ok": report.get("sync_ok"),
                "succession_ok": report.get("succession_ok"),
                "players": report.get("players", []),
                "screenshots": report.get("screenshots", []),
                "errors": report.get("errors", []),
                "exit_code": code,
                "persona_directive": (
                    "Report the Matrix Arena run as the leader: state whether followers MIRRORED the host "
                    "(sync_ok — a remote presence avatar was visible and the host's signed say() relayed into "
                    "their feed) and whether the frontier SURVIVED the host leaving (succession_ok — the senior "
                    "follower stayed alive and could open its own room). Give the host room id, the per-player "
                    "summary, and the screenshot paths under /tmp/matrix to open."
                ),
            }, indent=2)

        elif action == "host":
            res, raw, err, code = _run(["host", url], 120)
            return json.dumps({
                "schema": "rapp-result/1.0", "agent": self.name, "action": "host",
                "status": "success" if res is not None else "error",
                "result": res, "error": (None if res is not None else (err or raw)[:400]),
            }, indent=2)

        elif action == "join":
            room = (kwargs.get("room") or "").strip()
            if not room:
                return json.dumps({"schema": "rapp-result/1.0", "agent": self.name,
                                   "status": "error", "error": "join requires 'room' (a host room id)"}, indent=2)
            res, raw, err, code = _run(["join", room, url], 120)
            return json.dumps({
                "schema": "rapp-result/1.0", "agent": self.name, "action": "join",
                "status": "success" if res is not None else "error",
                "result": res, "error": (None if res is not None else (err or raw)[:400]),
            }, indent=2)

        elif action == "drive":
            name = (kwargs.get("name") or "host").strip()
            d_args = self._drive_args(kwargs)
            res, raw, err, code = _run(["drive", name] + d_args + [url], 120)
            return json.dumps({
                "schema": "rapp-result/1.0", "agent": self.name, "action": "drive",
                "status": "success" if res is not None else "error",
                "result": res, "error": (None if res is not None else (err or raw)[:400]),
            }, indent=2)

        elif action == "probe":
            name = (kwargs.get("name") or "host").strip()
            res, raw, err, code = _run(["probe", name, url], 120)
            return json.dumps({
                "schema": "rapp-result/1.0", "agent": self.name, "action": "probe",
                "status": "success" if res is not None else "error",
                "result": res, "error": (None if res is not None else (err or raw)[:400]),
            }, indent=2)

        return json.dumps({
            "schema": "rapp-result/1.0", "agent": self.name,
            "status": "error", "error": "unknown action: %s" % action,
        }, indent=2)
