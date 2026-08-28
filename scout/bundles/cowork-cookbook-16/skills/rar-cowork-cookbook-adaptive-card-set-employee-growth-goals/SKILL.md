---
name: "rar-cowork-cookbook-adaptive-card-set-employee-growth-goals"
description: "Produces a reusable Adaptive Card JSON snapshot of set employee growth goals status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_set_employee_growth_goals", "rar_sha256": "cfeb97aeb8c2f662aa1d948229c93c77ce3e004306c1735ba92896c75ad2898c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_set_employee_growth_goals`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_set_employee_growth_goals_agent.py` and in the RCI capsule.

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

Set employee growth goals Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of set employee growth goals status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-set-employee-growth-goals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_set_employee_growth_goals_agent.py` and embedded as the fenced Python below (sha256 cfeb97aeb8c2f662…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_set_employee_growth_goals_agent.py` first:

```bash
python3 adaptive_card_set_employee_growth_goals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_set_employee_growth_goals_agent.py   # or on stdin
python3 adaptive_card_set_employee_growth_goals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set employee growth goals Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of set employee growth goals status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-set-employee-growth-goals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_set_employee_growth_goals',
    "version": '2.0.0',
    "display_name": 'Set employee growth goals Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of set employee growth goals status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-set-employee-growth-goals',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-set-employee-growth-goals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a00454dbfeb1bd84',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/set-employee-growth-goals'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-set-employee-growth-goals', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardSetEmployeeGrowthGoals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardSetEmployeeGrowthGoals'
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
    print(AdaptiveCardSetEmployeeGrowthGoals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
