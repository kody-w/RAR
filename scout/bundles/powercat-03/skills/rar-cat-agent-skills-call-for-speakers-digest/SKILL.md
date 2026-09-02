---
name: "rar-cat-agent-skills-call-for-speakers-digest"
description: "Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/call_for_speakers_digest", "rar_sha256": "a3e15016b7641d3e6b947d84b323b4343bdb427effe8afb6d280f09d53a39511", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "call_for_speakers_digest_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/call-for-speakers-digest:5f9a8465fab4f9f7fe9fef630ae182cb595c9ddea5e8e7047c3774eecf2c0367", "kind": "skill"}, "version": "2.0.0", "author": "Michael Heath", "tags": ["productivity", "speaking", "conference", "automation"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/call_for_speakers_digest`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `call_for_speakers_digest_agent.py` is
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
