---
name: "rar-cowork-cookbook-configure-analyze-revenue"
description: "Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_revenue", "rar_sha256": "b87f81ce2cde2f033e370cf1c5a4aedffc005dae482b8e125635ce5dd95f0ecd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_revenue`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_revenue_agent.py` and in the RCI capsule.

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

Analyze revenue Configuration Bulk Setup — Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_revenue_agent.py` and embedded as the fenced Python below (sha256 b87f81ce2cde2f03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_revenue_agent.py` first:

```bash
python3 configure_analyze_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_revenue_agent.py   # or on stdin
python3 configure_analyze_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze revenue Configuration Bulk Setup — Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_revenue',
    "version": '2.0.1',
    "display_name": 'Analyze revenue Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-analyze-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a96a08469286bf6d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-revenue'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-analyze-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeRevenue'
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
    print(ConfigureAnalyzeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
