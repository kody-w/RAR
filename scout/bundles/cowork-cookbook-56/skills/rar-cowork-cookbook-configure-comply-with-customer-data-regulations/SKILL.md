---
name: "rar-cowork-cookbook-configure-comply-with-customer-data-regulations"
description: "Applies a bulk configuration change to comply with customer data regulations from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_comply_with_customer_data_regulations", "rar_sha256": "cf9e34d3926a81c890196bfed34cf267c2938088c0b536b674993b1339d73bf8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_comply_with_customer_data_regulations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-comply-with-customer-data-regulations:5e033b467c709245b6c736e01418a1b4b9bd98eac3e0f74c6cbe6fba64dbad89", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_comply_with_customer_data_regulations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_comply_with_customer_data_regulations_agent.py` is
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

Comply with customer data regulations Configuration Bulk Setup — Applies a bulk configuration change to comply with customer data regulations from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-comply-with-customer-data-regulations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_comply_with_customer_data_regulations_agent.py` and embedded as the fenced Python below (sha256 cf9e34d3926a81c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_comply_with_customer_data_regulations_agent.py` first:

```bash
python3 configure_comply_with_customer_data_regulations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_comply_with_customer_data_regulations_agent.py   # or on stdin
python3 configure_comply_with_customer_data_regulations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Comply with customer data regulations Configuration Bulk Setup — Applies a bulk configuration change to comply with customer data regulations from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-comply-with-customer-data-regulations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_comply_with_customer_data_regulations',
    "version": '2.0.0',
    "display_name": 'Comply with customer data regulations Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to comply with customer data regulations from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-comply-with-customer-data-regulations',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-comply-with-customer-data-regulations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8e808a3e8db0f3d0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/comply-with-customer-data-regulations'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-comply-with-customer-data-regulations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureComplyWithCustomerDataRegulations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureComplyWithCustomerDataRegulations'
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
    print(ConfigureComplyWithCustomerDataRegulations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
