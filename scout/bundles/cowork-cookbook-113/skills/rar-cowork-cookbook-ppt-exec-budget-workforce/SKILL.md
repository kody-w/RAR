---
name: "rar-cowork-cookbook-ppt-exec-budget-workforce"
description: "Generates an executive-ready PowerPoint deck on budget workforce status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_budget_workforce", "rar_sha256": "efa17d37497212fe517ad6ea474638c705e7927668891cccff100c90f40455be", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_budget_workforce_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-budget-workforce:32041a1afdb2eda3d1300a229011b2ad6c09b3fc634a6b29b15a80f613740650", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_budget_workforce`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_budget_workforce_agent.py` is
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
