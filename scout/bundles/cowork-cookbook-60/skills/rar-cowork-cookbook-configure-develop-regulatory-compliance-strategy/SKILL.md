---
name: "rar-cowork-cookbook-configure-develop-regulatory-compliance-strategy"
description: "Applies a bulk configuration change to develop regulatory compliance strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_regulatory_compliance_strategy", "rar_sha256": "7412edc3616bb8dfca6a9129a0bc35eb50e9b4a233099a95ba5955c382173c19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_develop_regulatory_compliance_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-develop-regulatory-compliance-strategy:9ae7b6e49f7eca1bbdeedd3f9052d4d68dd1c46573944877ece51c8571049957", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_develop_regulatory_compliance_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_develop_regulatory_compliance_strategy_agent.py` is
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

Develop regulatory compliance strategy Configuration Bulk Setup — Applies a bulk configuration change to develop regulatory compliance strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-regulatory-compliance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_regulatory_compliance_strategy_agent.py` and embedded as the fenced Python below (sha256 7412edc3616bb8df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_regulatory_compliance_strategy_agent.py` first:

```bash
python3 configure_develop_regulatory_compliance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_regulatory_compliance_strategy_agent.py   # or on stdin
python3 configure_develop_regulatory_compliance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop regulatory compliance strategy Configuration Bulk Setup — Applies a bulk configuration change to develop regulatory compliance strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-regulatory-compliance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_regulatory_compliance_strategy',
    "version": '2.0.0',
    "display_name": 'Develop regulatory compliance strategy Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop regulatory compliance strategy from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-develop-regulatory-compliance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-regulatory-compliance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'effff201bcc252a4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-regulatory-compliance-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-develop-regulatory-compliance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDevelopRegulatoryComplianceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopRegulatoryComplianceStrategy'
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
    print(ConfigureDevelopRegulatoryComplianceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
