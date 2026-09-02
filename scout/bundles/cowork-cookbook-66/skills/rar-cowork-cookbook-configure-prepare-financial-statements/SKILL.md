---
name: "rar-cowork-cookbook-configure-prepare-financial-statements"
description: "Applies a bulk configuration change to prepare financial statements from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_prepare_financial_statements", "rar_sha256": "17667df8f9b92a968d6cbb65f2d3ab69bbd00ee14cf33c50aa5cbe516b9c3fcb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_prepare_financial_statements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-prepare-financial-statements:31f40b665aaf0f4e897b5fa977b428a9206a5c0a188e89c610ccb4f786603b93", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_prepare_financial_statements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_prepare_financial_statements_agent.py` is
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

Prepare financial statements Configuration Bulk Setup — Applies a bulk configuration change to prepare financial statements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-prepare-financial-statements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_prepare_financial_statements_agent.py` and embedded as the fenced Python below (sha256 17667df8f9b92a96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_prepare_financial_statements_agent.py` first:

```bash
python3 configure_prepare_financial_statements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_prepare_financial_statements_agent.py   # or on stdin
python3 configure_prepare_financial_statements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare financial statements Configuration Bulk Setup — Applies a bulk configuration change to prepare financial statements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-prepare-financial-statements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_prepare_financial_statements',
    "version": '2.0.0',
    "display_name": 'Prepare financial statements Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to prepare financial statements from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-prepare-financial-statements',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-prepare-financial-statements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7dc8afc1f7a92fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/prepare-financial-statements'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-prepare-financial-statements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePrepareFinancialStatements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePrepareFinancialStatements'
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
    print(ConfigurePrepareFinancialStatements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
