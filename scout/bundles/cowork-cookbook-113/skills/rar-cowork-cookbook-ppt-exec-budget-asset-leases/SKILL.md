---
name: "rar-cowork-cookbook-ppt-exec-budget-asset-leases"
description: "Generates an executive-ready PowerPoint deck on budget asset leases status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_budget_asset_leases", "rar_sha256": "2ee2503a465b67757e1bfd6d73296e2386f9d2fdca9423dae194a8d71d4599db", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_budget_asset_leases_agent.py` and embedded as the fenced Python below (sha256 2ee2503a465b6775…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_budget_asset_leases_agent.py` first:

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
    "version": '2.0.1',
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
