---
name: "rar-cowork-cookbook-configure-recognize-project-revenue"
description: "Applies a bulk configuration change to recognize project revenue from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_recognize_project_revenue", "rar_sha256": "8ef9e3dc9d3ed5d17591a06de013272527471aeeb6c357fa0301400521851189", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_recognize_project_revenue`. The original RAPP
agent is preserved byte-for-byte in `configure_recognize_project_revenue_agent.py` and in the RCI capsule.

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

Recognize project revenue Configuration Bulk Setup — Applies a bulk configuration change to recognize project revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-project-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_recognize_project_revenue_agent.py` and embedded as the fenced Python below (sha256 8ef9e3dc9d3ed5d1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_recognize_project_revenue_agent.py` first:

```bash
python3 configure_recognize_project_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_recognize_project_revenue_agent.py   # or on stdin
python3 configure_recognize_project_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize project revenue Configuration Bulk Setup — Applies a bulk configuration change to recognize project revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-project-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_recognize_project_revenue',
    "version": '2.0.0',
    "display_name": 'Recognize project revenue Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to recognize project revenue from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-recognize-project-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-recognize-project-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0a6a8adeb311d11f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/recognize-project-revenue'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-recognize-project-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureRecognizeProjectRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRecognizeProjectRevenue'
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
    print(ConfigureRecognizeProjectRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
