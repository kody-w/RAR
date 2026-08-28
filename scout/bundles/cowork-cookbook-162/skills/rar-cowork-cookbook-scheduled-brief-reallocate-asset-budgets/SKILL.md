---
name: "rar-cowork-cookbook-scheduled-brief-reallocate-asset-budgets"
description: "Schedulable morning-brief email summarizing reallocate asset budgets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_reallocate_asset_budgets", "rar_sha256": "3bd5d524128c860963604b3369341df1bfeca9b6435e8ff49d86fc8f86ef0472", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_reallocate_asset_budgets_agent.py` and embedded as the fenced Python below (sha256 3bd5d524128c8609…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_reallocate_asset_budgets_agent.py` first:

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
    "version": '2.0.0',
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
