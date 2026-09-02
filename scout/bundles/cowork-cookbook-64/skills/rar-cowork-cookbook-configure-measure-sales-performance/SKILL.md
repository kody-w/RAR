---
name: "rar-cowork-cookbook-configure-measure-sales-performance"
description: "Applies a bulk configuration change to measure sales performance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_measure_sales_performance", "rar_sha256": "10fb1e419366d3c58e97a23e8b94d72a7e4e4dfa27f6bc3df8203f035f3c2def", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_measure_sales_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-measure-sales-performance:dd1c83493687436d53e8be93eb075303b59b67ac0917a3909ea4f294cfa7c15f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_measure_sales_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_measure_sales_performance_agent.py` is
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

Measure sales performance Configuration Bulk Setup — Applies a bulk configuration change to measure sales performance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-sales-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_measure_sales_performance_agent.py` and embedded as the fenced Python below (sha256 10fb1e419366d3c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_measure_sales_performance_agent.py` first:

```bash
python3 configure_measure_sales_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_measure_sales_performance_agent.py   # or on stdin
python3 configure_measure_sales_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure sales performance Configuration Bulk Setup — Applies a bulk configuration change to measure sales performance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-sales-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_measure_sales_performance',
    "version": '2.0.0',
    "display_name": 'Measure sales performance Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to measure sales performance from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-measure-sales-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-measure-sales-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c76fa1457d07794c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/measure-sales-performance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-measure-sales-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureMeasureSalesPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMeasureSalesPerformance'
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
    print(ConfigureMeasureSalesPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
