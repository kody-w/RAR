---
name: "rar-cowork-cookbook-configure-manage-procurement-spend"
description: "Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_procurement_spend", "rar_sha256": "c19dd090588ccc350054cf6d794ee1ba633e9d646d0e18a39b5106619da0b2f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_procurement_spend_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-procurement-spend:3d41b87b4039846fd9644c60c135a606c023208353d12ef868038ddbcc9e15e2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_procurement_spend`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_procurement_spend_agent.py` is
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

Manage procurement spend Configuration Bulk Setup — Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-procurement-spend
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 c19dd090588ccc35…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_procurement_spend_agent.py` first:

```bash
python3 configure_manage_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_procurement_spend_agent.py   # or on stdin
python3 configure_manage_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement spend Configuration Bulk Setup — Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_procurement_spend',
    "version": '2.0.0',
    "display_name": 'Manage procurement spend Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '526c93515deb5e55',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/manage-procurement-spend'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageProcurementSpend(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageProcurementSpend'
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
    print(ConfigureManageProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
