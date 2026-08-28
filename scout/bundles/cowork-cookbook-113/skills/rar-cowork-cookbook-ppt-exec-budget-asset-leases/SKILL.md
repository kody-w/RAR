---
name: "rar-cowork-cookbook-ppt-exec-budget-asset-leases"
description: "Generates an executive-ready PowerPoint deck on budget asset leases status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_budget_asset_leases", "rar_sha256": "f51374578f80be988c9daca1b5e57571dcabad3bbcbc9bd306fa8b92f631c37d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_budget_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_budget_asset_leases_agent.py` and in the RCI capsule.

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
