---
name: "rar-cowork-cookbook-field-service-daily-utilization"
description: "Drafts a morning email to service operations summarizing technician utilization for today and the coming week, including overbooked and underbooked resources."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/field_service_daily_utilization", "rar_sha256": "2f8174d2cf4c60a95c981dfbb882e3d48d06d8bdadd194f35fadce21d32e7728", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `field_service_daily_utilization_agent.py` and embedded as the fenced Python below (sha256 2f8174d2cf4c60a9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `field_service_daily_utilization_agent.py` first:

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
    "version": '2.0.1',
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
