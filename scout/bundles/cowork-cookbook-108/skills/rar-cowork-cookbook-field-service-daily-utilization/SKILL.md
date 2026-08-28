---
name: "rar-cowork-cookbook-field-service-daily-utilization"
description: "Drafts a morning email to service operations summarizing technician utilization for today and the coming week, including overbooked and underbooked resources."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/field_service_daily_utilization", "rar_sha256": "3769455d269bc64b76d817d4447a0388f55806024987b3485b8cf23db9120383", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/field_service_daily_utilization`. The original RAPP
agent is preserved byte-for-byte in `field_service_daily_utilization_agent.py` and in the RCI capsule.

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
