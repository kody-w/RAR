---
name: "rar-cowork-cookbook-configure-develop-service-pricing-strategy"
description: "Applies a bulk configuration change to develop service pricing strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_service_pricing_strategy", "rar_sha256": "7f1b7e50a0e1d3b01323f5a6dc111a9211b09f7e19425cd0a20d6af570d4c8d8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_develop_service_pricing_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-develop-service-pricing-strategy:8ee008d57478d2172cf684bbde58e0fdbccc0fbbb989af900619de97fe766277", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_develop_service_pricing_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_develop_service_pricing_strategy_agent.py` is
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

Develop service pricing strategy Configuration Bulk Setup — Applies a bulk configuration change to develop service pricing strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-service-pricing-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_service_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 7f1b7e50a0e1d3b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_service_pricing_strategy_agent.py` first:

```bash
python3 configure_develop_service_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_service_pricing_strategy_agent.py   # or on stdin
python3 configure_develop_service_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service pricing strategy Configuration Bulk Setup — Applies a bulk configuration change to develop service pricing strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-service-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_service_pricing_strategy',
    "version": '2.0.0',
    "display_name": 'Develop service pricing strategy Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop service pricing strategy from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-service-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-service-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd4570be27fcd7514',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-pricing-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-develop-service-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDevelopServicePricingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopServicePricingStrategy'
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
    print(ConfigureDevelopServicePricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
