---
name: "rar-cowork-cookbook-scheduled-brief-plan-fixed-assets"
description: "Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_fixed_assets", "rar_sha256": "6ebafb10e1e9c98668296c8bcfcc643161a9e3df293d10ce4c01da6b3570dedb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_fixed_assets_agent.py` and in the RCI capsule.

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

Plan fixed assets Scheduled Email Brief — Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 6ebafb10e1e9c986…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_fixed_assets_agent.py` first:

```bash
python3 scheduled_brief_plan_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_fixed_assets_agent.py   # or on stdin
python3 scheduled_brief_plan_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan fixed assets Scheduled Email Brief — Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_fixed_assets',
    "version": '2.0.0',
    "display_name": 'Plan fixed assets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-plan-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07817134cfef3a41',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-fixed-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-plan-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefPlanFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanFixedAssets'
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
    print(ScheduledBriefPlanFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
