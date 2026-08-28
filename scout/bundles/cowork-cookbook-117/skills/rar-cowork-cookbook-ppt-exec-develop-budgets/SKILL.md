---
name: "rar-cowork-cookbook-ppt-exec-develop-budgets"
description: "Generates an executive-ready PowerPoint deck on develop budgets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_budgets", "rar_sha256": "50c8e25a03b1c5ba0bb24fbcedfaf12ea0d63fbd7aa78b9957d1ab7038e0e795", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_budgets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_budgets_agent.py` and in the RCI capsule.

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

Develop budgets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop budgets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_budgets_agent.py` and embedded as the fenced Python below (sha256 50c8e25a03b1c5ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_budgets_agent.py` first:

```bash
python3 ppt_exec_develop_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_budgets_agent.py   # or on stdin
python3 ppt_exec_develop_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop budgets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop budgets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_budgets',
    "version": '2.0.1',
    "display_name": 'Develop budgets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop budgets status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '28284d3021c43063',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/develop-budgets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-develop-budgets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDevelopBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopBudgets'
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
    print(PptExecDevelopBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
