---
name: "rar-cowork-cookbook-ppt-exec-budget-workforce"
description: "Generates an executive-ready PowerPoint deck on budget workforce status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_budget_workforce", "rar_sha256": "efa17d37497212fe517ad6ea474638c705e7927668891cccff100c90f40455be", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_budget_workforce_agent.py` and embedded as the fenced Python below (sha256 efa17d37497212fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_budget_workforce_agent.py` first:

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
    "version": '2.0.0',
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
