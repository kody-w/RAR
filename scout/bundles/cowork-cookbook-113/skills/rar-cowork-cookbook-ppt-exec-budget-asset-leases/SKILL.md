---
name: "rar-cowork-cookbook-ppt-exec-budget-asset-leases"
description: "Generates an executive-ready PowerPoint deck on budget asset leases status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_budget_asset_leases", "rar_sha256": "f51374578f80be988c9daca1b5e57571dcabad3bbcbc9bd306fa8b92f631c37d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_budget_asset_leases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-budget-asset-leases:8a0a50a521fa2e627acff91648da6d094bd7437d7286140dcaba5ff8bddfe1e2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_budget_asset_leases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_budget_asset_leases_agent.py` is
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

Budget asset leases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on budget asset leases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-budget-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_budget_asset_leases_agent.py` and embedded as the fenced Python below (sha256 f51374578f80be98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_budget_asset_leases_agent.py` first:

```bash
python3 ppt_exec_budget_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_budget_asset_leases_agent.py   # or on stdin
python3 ppt_exec_budget_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget asset leases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on budget asset leases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-budget-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_budget_asset_leases',
    "version": '2.0.0',
    "display_name": 'Budget asset leases Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on budget asset leases status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-budget-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-budget-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5f97eea90bd4d9e9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/budget-asset-leases'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-budget-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecBudgetAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecBudgetAssetLeases'
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
    print(PptExecBudgetAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
