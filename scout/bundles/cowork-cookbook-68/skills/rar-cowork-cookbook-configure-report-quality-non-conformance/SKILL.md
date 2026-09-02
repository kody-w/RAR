---
name: "rar-cowork-cookbook-configure-report-quality-non-conformance"
description: "Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_report_quality_non_conformance", "rar_sha256": "826f8bb290cc75da099919a06b1000d433178e54582a84e8af8c37334108935c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_report_quality_non_conformance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-report-quality-non-conformance:563f68c4935954b2104cdd85787d5d89b35fa16635801558dea308dcaeb7585d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_report_quality_non_conformance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_report_quality_non_conformance_agent.py` is
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

Report quality non-conformance Configuration Bulk Setup — Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-report-quality-non-conformance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_report_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 826f8bb290cc75da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_report_quality_non_conformance_agent.py` first:

```bash
python3 configure_report_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_report_quality_non_conformance_agent.py   # or on stdin
python3 configure_report_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality non-conformance Configuration Bulk Setup — Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-report-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_report_quality_non_conformance',
    "version": '2.0.0',
    "display_name": 'Report quality non-conformance Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-report-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-report-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '184d2447414bdcf0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/report-quality-non-conformance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-report-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReportQualityNonConformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReportQualityNonConformance'
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
    print(ConfigureReportQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
