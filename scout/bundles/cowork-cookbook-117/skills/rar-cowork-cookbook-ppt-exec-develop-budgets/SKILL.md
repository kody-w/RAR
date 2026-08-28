---
name: "rar-cowork-cookbook-ppt-exec-develop-budgets"
description: "Generates an executive-ready PowerPoint deck on develop budgets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_budgets", "rar_sha256": "6908d1b13b7fa16f2a96d1a556f837eafe6d4a3eaa716f21495035f07bbcfe7c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_budgets_agent.py` and embedded as the fenced Python below (sha256 6908d1b13b7fa16f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_budgets_agent.py` first:

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
    "version": '2.0.0',
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
