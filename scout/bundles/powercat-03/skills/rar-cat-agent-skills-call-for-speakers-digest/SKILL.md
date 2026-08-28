---
name: "rar-cat-agent-skills-call-for-speakers-digest"
description: "Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/call_for_speakers_digest", "rar_sha256": "a3e15016b7641d3e6b947d84b323b4343bdb427effe8afb6d280f09d53a39511", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Michael Heath", "tags": ["productivity", "speaking", "conference", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/call_for_speakers_digest`. The original RAPP
agent is preserved byte-for-byte in `call_for_speakers_digest_agent.py` and in the RCI capsule.

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

Call for Speakers Digest — Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#call-for-speakers-digest
  Upstream author: Michael Heath
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `call_for_speakers_digest_agent.py` and embedded as the fenced Python below (sha256 a3e15016b7641d3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `call_for_speakers_digest_agent.py` first:

```bash
python3 call_for_speakers_digest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 call_for_speakers_digest_agent.py   # or on stdin
python3 call_for_speakers_digest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Call for Speakers Digest — Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#call-for-speakers-digest
  Upstream author: Michael Heath
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/call_for_speakers_digest',
    "version": '2.0.0',
    "display_name": 'Call for Speakers Digest',
    "description": "Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc…",
    "author": 'Michael Heath',
    "tags": ['productivity', 'speaking', 'conference', 'automation'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'call-for-speakers-digest',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#call-for-speakers-digest',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd964e313b2ca6981',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Scout', 'Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class CallForSpeakersDigest(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CallForSpeakersDigest'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(CallForSpeakersDigest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
