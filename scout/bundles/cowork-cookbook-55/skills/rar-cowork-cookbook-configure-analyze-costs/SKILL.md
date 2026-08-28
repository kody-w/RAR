---
name: "rar-cowork-cookbook-configure-analyze-costs"
description: "Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_costs", "rar_sha256": "c7d46803ac34a9c80906ceb14822aba99474994680bdf32016a99a75fb76bed7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_costs`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_costs_agent.py` and in the RCI capsule.

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

Analyze costs Configuration Bulk Setup — Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_costs_agent.py` and embedded as the fenced Python below (sha256 c7d46803ac34a9c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_costs_agent.py` first:

```bash
python3 configure_analyze_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_costs_agent.py   # or on stdin
python3 configure_analyze_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze costs Configuration Bulk Setup — Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_costs',
    "version": '2.0.1',
    "display_name": 'Analyze costs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-analyze-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b14bd69f16ad29d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-costs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-analyze-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeCosts'
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
    print(ConfigureAnalyzeCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
