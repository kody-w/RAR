---
name: "rar-cowork-cookbook-adaptive-card-set-employee-growth-goals"
description: "Produces a reusable Adaptive Card JSON snapshot of set employee growth goals status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_set_employee_growth_goals", "rar_sha256": "cfeb97aeb8c2f662aa1d948229c93c77ce3e004306c1735ba92896c75ad2898c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_set_employee_growth_goals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-set-employee-growth-goals:e36d2674db7bd2c011657d61458aa7a431b576e96332b3b6f7e0244c96ee0c64", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_set_employee_growth_goals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_set_employee_growth_goals_agent.py` is
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
