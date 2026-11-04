---
name: "rar-kody-w-matrix-arena"
description: "Launch a multi-tab 'Matrix Arena' against the LIVE RAPP Commons world and autonomously sync-test it. It opens real headless browser tabs into one shared walkable PeerJS world: a HOST (the leader that opens the room and records) and N FOLLOWERS (replicas that join the host's room), then drives them on their own. Use this when the user wants to test the live commons, host-led sync, multiplayer presence, signed actions/feed relay, navigation, or host succession \u2014 i.e. to 'play as the leader' and prove followers mirror the host. ACTION 'scenario' (default) runs the full test: open the host (it mints a PeerJS room), open 'n_followers' followers joined to it, wait for presence to connect, DRIVE THE HOST as leader (teleport, walk, a SIGNED say() hello, enter the voxel game + place a block, enter poker), then PROBE each follower and assert it mirrors the host (a remote presence avatar is visible AND the host's signed say() appears in the follower's feed = the sync check), then a SUCCESSION test (close the host tab and verify the senior follower survives and can open its own room). It screenshots every tab to /tmp/matrix and returns a JSON report {host_room, players[], sync_ok, succession_ok, screenshots}. 'seconds' tunes how long it lets things settle/relay. ACTION 'host' opens one host tab and reports its room id + a probe. ACTION 'join' joins an existing 'room' id and reports a probe. ACTION 'drive' drives one tab with an 'action' (where/teleport/walk/face/say/enter/voxelPlace/feed/minimap/residents/fractal/...) plus optional 'text' (for say/enter/goto) or numeric 'x','y','z' (for teleport/voxelPlace). ACTION 'probe' opens a tab and reports where/presence/feed/fractal. Headless, public world URL, no PII."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/matrix_arena_agent", "rar_sha256": "313121fc5f72c6664069d2b016bf5f3a4566bad3f7bbebe29b411b26cf02425a", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "multiplayer", "testing", "playwright", "webrtc"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/matrix_arena_agent`. The original RAPP
agent is preserved byte-for-byte in `matrix_arena_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "scenario = full host + N followers sync + succession test (default); host = open one host tab + report room id; join = join an existing room id; drive = drive one tab with an action; probe = open a tab and report its state.",
      "enum": [
        "scenario",
        "host",
        "join",
        "drive",
        "probe"
      ],
      "type": "string"
    },
    "block": {
      "description": "drive: block type for voxelPlace() (e.g. 'stone'). Default 'stone'.",
      "type": "string"
    },
    "drive_action": {
      "description": "drive: the commonsAgent method to call on the tab, e.g. 'where','teleport','walk','face','goto','enter','interact','say','voxelPlace','feed','minimap','residents','fractal','timeOfDay'.",
      "type": "string"
    },
    "n_followers": {
      "description": "scenario: how many FOLLOWER tabs to join to the host's room. Default 1.",
      "type": "integer"
    },
    "name": {
      "description": "drive/probe: a label for the tab being driven/probed (e.g. 'host' or 'follower'). Cosmetic.",
      "type": "string"
    },
    "room": {
      "description": "join: the PeerJS room id (the <ID> from a host's '?host=<ID>' line) to join.",
      "type": "string"
    },
    "seconds": {
      "description": "scenario: settle/relay window in seconds (how long to let presence connect and signed events relay before asserting). Default 20.",
      "type": "integer"
    },
    "steps": {
      "description": "drive: number of steps for walk() (paired with text='forward'|'back'|'left'|'right').",
      "type": "integer"
    },
    "text": {
      "description": "drive: a string argument for the action (the message for say(); the name for enter()/goto(), e.g. 'voxel','poker'; the direction for walk(), e.g. 'forward').",
      "type": "string"
    },
    "url": {
      "description": "Optional commons URL override. Default the live Pages site.",
      "type": "string"
    },
    "x": {
      "description": "drive: x coordinate for teleport()/voxelPlace().",
      "type": "number"
    },
    "y": {
      "description": "drive: y coordinate for teleport()/voxelPlace().",
      "type": "number"
    },
    "z": {
      "description": "drive: z coordinate for teleport()/voxelPlace().",
      "type": "number"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `matrix_arena_agent.py` and embedded as the fenced Python below (sha256 313121fc5f72c666…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `matrix_arena_agent.py` first:

```bash
python3 matrix_arena_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 matrix_arena_agent.py   # or on stdin
python3 matrix_arena_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
