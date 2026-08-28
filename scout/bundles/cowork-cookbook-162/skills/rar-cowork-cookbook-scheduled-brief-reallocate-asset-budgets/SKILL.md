---
name: "rar-cowork-cookbook-scheduled-brief-reallocate-asset-budgets"
description: "Schedulable morning-brief email summarizing reallocate asset budgets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_reallocate_asset_budgets", "rar_sha256": "e8733d9ef46e1e287c9b46fc2aca35d7041c991fd658dd4578baa6c94e15cc72", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_reallocate_asset_budgets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_reallocate_asset_budgets_agent.py` and in the RCI capsule.

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

Reallocate asset budgets Scheduled Email Brief — Schedulable morning-brief email summarizing reallocate asset budgets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-reallocate-asset-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_reallocate_asset_budgets_agent.py` and embedded as the fenced Python below (sha256 e8733d9ef46e1e28…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_reallocate_asset_budgets_agent.py` first:

```bash
python3 scheduled_brief_reallocate_asset_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_reallocate_asset_budgets_agent.py   # or on stdin
python3 scheduled_brief_reallocate_asset_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reallocate asset budgets Scheduled Email Brief — Schedulable morning-brief email summarizing reallocate asset budgets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-reallocate-asset-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_reallocate_asset_budgets',
    "version": '2.0.1',
    "display_name": 'Reallocate asset budgets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing reallocate asset budgets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-reallocate-asset-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-reallocate-asset-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dab899844477d051',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/reallocate-asset-budgets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-reallocate-asset-budgets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefReallocateAssetBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReallocateAssetBudgets'
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
    print(ScheduledBriefReallocateAssetBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
