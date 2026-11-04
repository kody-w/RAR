---
name: "rar-kody-w-matrix-arena"
description: "Launch a multi-tab 'Matrix Arena' against the LIVE RAPP Commons world and autonomously sync-test it. It opens real headless browser tabs into one shared walkable PeerJS world: a HOST (the leader that opens the room and records) and N FOLLOWERS (replicas that join the host's room), then drives them on their own. Use this when the user wants to test the live commons, host-led sync, multiplayer presence, signed actions/feed relay, navigation, or host succession \u2014 i.e. to 'play as the leader' and prove followers mirror the host. ACTION 'scenario' (default) runs the full test: open the host (it mints a PeerJS room), open 'n_followers' followers joined to it, wait for presence to connect, DRIVE THE HOST as leader (teleport, walk, a SIGNED say() hello, enter the voxel game + place a block, enter poker), then PROBE each follower and assert it mirrors the host (a remote presence avatar is visible AND the host's signed say() appears in the follower's feed = the sync check), then a SUCCESSION test (close the host tab and verify the senior follower survives and can open its own room). It screenshots every tab to /tmp/matrix and returns a JSON report {host_room, players[], sync_ok, succession_ok, screenshots}. 'seconds' tunes how long it lets things settle/relay. ACTION 'host' opens one host tab and reports its room id + a probe. ACTION 'join' joins an existing 'room' id and reports a probe. ACTION 'drive' drives one tab with an 'action' (where/teleport/walk/face/say/enter/voxelPlace/feed/minimap/residents/fractal/...) plus optional 'text' (for say/enter/goto) or numeric 'x','y','z' (for teleport/voxelPlace). ACTION 'probe' opens a tab and reports where/presence/feed/fractal. Headless, public world URL, no PII."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/matrix_arena_agent", "rar_sha256": "1d1c4fe075943ca79f7873608a2a683448a0bd8d3c97e89b640b4d8690cee7f1", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "multiplayer", "testing", "playwright", "webrtc"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `matrix_arena_agent.py` and embedded as the fenced Python below (sha256 1d1c4fe075943ca7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `matrix_arena_agent.py` first:

```bash
python3 matrix_arena_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 matrix_arena_agent.py   # or on stdin
python3 matrix_arena_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/matrix_arena_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/matrix_arena_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/matrix_arena_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
