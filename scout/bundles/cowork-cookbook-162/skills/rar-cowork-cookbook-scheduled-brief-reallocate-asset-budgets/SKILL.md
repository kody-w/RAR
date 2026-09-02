---
name: "rar-cowork-cookbook-scheduled-brief-reallocate-asset-budgets"
description: "Schedulable morning-brief email summarizing reallocate asset budgets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_reallocate_asset_budgets", "rar_sha256": "3bd5d524128c860963604b3369341df1bfeca9b6435e8ff49d86fc8f86ef0472", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_reallocate_asset_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-reallocate-asset-budgets:89aef692dd2bd723fbdc5dd54b1bd0d3bef1938438335e870de096ef90f8820a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_reallocate_asset_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_reallocate_asset_budgets_agent.py` is
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
