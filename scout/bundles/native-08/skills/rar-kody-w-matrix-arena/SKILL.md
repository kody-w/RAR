---
name: "rar-kody-w-matrix-arena"
description: "Launch a multi-tab 'Matrix Arena' against the LIVE RAPP Commons world and autonomously sync-test it. It opens real headless browser tabs into one shared walkable PeerJS world: a HOST (the leader that opens the room and records) and N FOLLOWERS (replicas that join the host's room), then drives them on their own. Use this when the user wants to test the live commons, host-led sync, multiplayer presence, signed actions/feed relay, navigation, or host succession \u2014 i.e. to 'play as the leader' and prove followers mirror the host. ACTION 'scenario' (default) runs the full test: open the host (it mints a PeerJS room), open 'n_followers' followers joined to it, wait for presence to connect, DRIVE THE HOST as leader (teleport, walk, a SIGNED say() hello, enter the voxel game + place a block, enter poker), then PROBE each follower and assert it mirrors the host (a remote presence avatar is visible AND the host's signed say() appears in the follower's feed = the sync check), then a SUCCESSION test (close the host tab and verify the senior follower survives and can open its own room). It screenshots every tab to /tmp/matrix and returns a JSON report {host_room, players[], sync_ok, succession_ok, screenshots}. 'seconds' tunes how long it lets things settle/relay. ACTION 'host' opens one host tab and reports its room id + a probe. ACTION 'join' joins an existing 'room' id and reports a probe. ACTION 'drive' drives one tab with an 'action' (where/teleport/walk/face/say/enter/voxelPlace/feed/minimap/residents/fractal/...) plus optional 'text' (for say/enter/goto) or numeric 'x','y','z' (for teleport/voxelPlace). ACTION 'probe' opens a tab and reports where/presence/feed/fractal. Headless, public world URL, no PII."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/matrix_arena_agent", "rar_sha256": "313121fc5f72c6664069d2b016bf5f3a4566bad3f7bbebe29b411b26cf02425a", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "matrix_arena_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/matrix-arena:ca1891ff4c5d31207dc2cca79ba59e7e1724a805f7b580923fca425436f051f4", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["commons", "multiplayer", "testing", "playwright", "webrtc"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/matrix_arena_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `matrix_arena_agent.py` is
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
