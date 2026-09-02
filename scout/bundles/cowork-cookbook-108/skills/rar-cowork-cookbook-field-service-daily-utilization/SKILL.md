---
name: "rar-cowork-cookbook-field-service-daily-utilization"
description: "Drafts a morning email to service operations summarizing technician utilization for today and the coming week, including overbooked and underbooked resources."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/field_service_daily_utilization", "rar_sha256": "3769455d269bc64b76d817d4447a0388f55806024987b3485b8cf23db9120383", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "field_service_daily_utilization_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/field-service-daily-utilization:4bc60032a8bc4ec49637f70ba32839e75a0ef315681d133a0f68d1349099fd35", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/field_service_daily_utilization`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `field_service_daily_utilization_agent.py` is
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

Field Service Resource Utilization Daily Email — Drafts a morning email to service operations summarizing technician utilization for today and the coming week, including overbooked and underbooked resources.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/field-service-daily-utilization
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `field_service_daily_utilization_agent.py` and embedded as the fenced Python below (sha256 3769455d269bc64b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `field_service_daily_utilization_agent.py` first:

```bash
python3 field_service_daily_utilization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 field_service_daily_utilization_agent.py   # or on stdin
python3 field_service_daily_utilization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Field Service Resource Utilization Daily Email — Drafts a morning email to service operations summarizing technician utilization for today and the coming week, including overbooked and underbooked resources.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/field-service-daily-utilization
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/field_service_daily_utilization',
    "version": '2.0.0',
    "display_name": 'Field Service Resource Utilization Daily Email',
    "description": 'Drafts a morning email to service operations summarizing technician utilization for today and the coming week, including overbooked and underbooked resources.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'field-service-daily-utilization',
        "upstream_url": 'https://coworkcookbook.com/recipes/field-service-daily-utilization',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1cb7801b033ea7ff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/field-service-daily-utilization', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class FieldServiceDailyUtilization(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FieldServiceDailyUtilization'
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
    print(FieldServiceDailyUtilization().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
