---
name: "rar-kody-w-matrix-arena"
description: "Launch a multi-tab 'Matrix Arena' against the LIVE RAPP Commons world and autonomously sync-test it. It opens real headless browser tabs into one shared walkable PeerJS world: a HOST (the leader that opens the room and records) and N FOLLOWERS (replicas that join the host's room), then drives them on their own. Use this when the user wants to test the live commons, host-led sync, multiplayer presence, signed actions/feed relay, navigation, or host succession \u2014 i.e. to 'play as the leader' and prove followers mirror the host. ACTION 'scenario' (default) runs the full test: open the host (it mints a PeerJS room), open 'n_followers' followers joined to it, wait for presence to connect, DRIVE THE HOST as leader (teleport, walk, a SIGNED say() hello, enter the voxel game + place a block, enter poker), then PROBE each follower and assert it mirrors the host (a remote presence avatar is visible AND the host's signed say() appears in the follower's feed = the sync check), then a SUCCESSION test (close the host tab and verify the senior follower survives and can open its own room). It screenshots every tab to /tmp/matrix and returns a JSON report {host_room, players[], sync_ok, succession_ok, screenshots}. 'seconds' tunes how long it lets things settle/relay. ACTION 'host' opens one host tab and reports its room id + a probe. ACTION 'join' joins an existing 'room' id and reports a probe. ACTION 'drive' drives one tab with an 'action' (where/teleport/walk/face/say/enter/voxelPlace/feed/minimap/residents/fractal/...) plus optional 'text' (for say/enter/goto) or numeric 'x','y','z' (for teleport/voxelPlace). ACTION 'probe' opens a tab and reports where/presence/feed/fractal. Headless, public world URL, no PII."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/matrix_arena_agent", "rar_sha256": "1d1c4fe075943ca79f7873608a2a683448a0bd8d3c97e89b640b4d8690cee7f1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "multiplayer", "testing", "playwright", "webrtc"]}
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
