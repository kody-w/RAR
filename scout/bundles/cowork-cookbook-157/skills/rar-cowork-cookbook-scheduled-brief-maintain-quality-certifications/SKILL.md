---
name: "rar-cowork-cookbook-scheduled-brief-maintain-quality-certifications"
description: "Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_maintain_quality_certifications", "rar_sha256": "5accab39611ece471f2fda2f747076c8455bce0a6d00588caadc40fe9b52716f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_maintain_quality_certifications_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-maintain-quality-certifications:ae5210891902b69655c89d46d73d7f937a8898e56b224ac11d7470df2448a9b6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_maintain_quality_certifications`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_maintain_quality_certifications_agent.py` is
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

Maintain quality certifications Scheduled Email Brief — Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_maintain_quality_certifications_agent.py` and embedded as the fenced Python below (sha256 5accab39611ece47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_maintain_quality_certifications_agent.py` first:

```bash
python3 scheduled_brief_maintain_quality_certifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_maintain_quality_certifications_agent.py   # or on stdin
python3 scheduled_brief_maintain_quality_certifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain quality certifications Scheduled Email Brief — Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_maintain_quality_certifications',
    "version": '2.0.0',
    "display_name": 'Maintain quality certifications Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-maintain-quality-certifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c2ec1d0cea81b1a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/maintain-quality-certifications'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-maintain-quality-certifications', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefMaintainQualityCertifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMaintainQualityCertifications'
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
    print(ScheduledBriefMaintainQualityCertifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
