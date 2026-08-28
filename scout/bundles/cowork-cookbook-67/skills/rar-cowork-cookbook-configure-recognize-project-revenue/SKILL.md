---
name: "rar-cowork-cookbook-configure-recognize-project-revenue"
description: "Applies a bulk configuration change to recognize project revenue from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_recognize_project_revenue", "rar_sha256": "e2b25f751f78b0322e0db4fd479277eee2d285c35d24668f07da8a144f8974b5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_recognize_project_revenue_agent.py` and embedded as the fenced Python below (sha256 e2b25f751f78b032…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_recognize_project_revenue_agent.py` first:

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
    "version": '2.0.1',
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
