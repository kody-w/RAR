---
name: "rar-cowork-cookbook-ppt-exec-budget-workforce"
description: "Generates an executive-ready PowerPoint deck on budget workforce status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_budget_workforce", "rar_sha256": "8222d9998c5d081c12ed9a5635ffd2fdf7aac55d602c96a7f39bb98eb8205638", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_budget_workforce`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_budget_workforce_agent.py` and in the RCI capsule.

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

Budget workforce Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on budget workforce status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-budget-workforce
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_budget_workforce_agent.py` and embedded as the fenced Python below (sha256 8222d9998c5d081c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_budget_workforce_agent.py` first:

```bash
python3 ppt_exec_budget_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_budget_workforce_agent.py   # or on stdin
python3 ppt_exec_budget_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget workforce Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on budget workforce status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-budget-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_budget_workforce',
    "version": '2.0.1',
    "display_name": 'Budget workforce Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on budget workforce status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-budget-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-budget-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '52c1c739f2d12917',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/budget-workforce'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-budget-workforce', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecBudgetWorkforce(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecBudgetWorkforce'
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
    print(PptExecBudgetWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
