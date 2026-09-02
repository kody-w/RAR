---
name: "rar-cowork-cookbook-scheduled-brief-respond-to-non-compliance"
description: "Schedulable morning-brief email summarizing respond to non-compliance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_respond_to_non_compliance", "rar_sha256": "12bd4be5cc9fba4d2b4a9868fd210927e23accc607d0373d0c7ee4cfbae1d689", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_respond_to_non_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-respond-to-non-compliance:00351a15e627c1c020d0c6ab67912cece99565860ba0fe2eb3c9da687e395e8f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_respond_to_non_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_respond_to_non_compliance_agent.py` is
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

Respond to non-compliance Scheduled Email Brief — Schedulable morning-brief email summarizing respond to non-compliance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-respond-to-non-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_respond_to_non_compliance_agent.py` and embedded as the fenced Python below (sha256 12bd4be5cc9fba4d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_respond_to_non_compliance_agent.py` first:

```bash
python3 scheduled_brief_respond_to_non_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_respond_to_non_compliance_agent.py   # or on stdin
python3 scheduled_brief_respond_to_non_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Respond to non-compliance Scheduled Email Brief — Schedulable morning-brief email summarizing respond to non-compliance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-respond-to-non-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_respond_to_non_compliance',
    "version": '2.0.0',
    "display_name": 'Respond to non-compliance Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing respond to non-compliance for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-respond-to-non-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-respond-to-non-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f4e47da48fdf961c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/respond-to-non-compliance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-respond-to-non-compliance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefRespondToNonCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRespondToNonCompliance'
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
    print(ScheduledBriefRespondToNonCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
