---
name: "rar-cowork-cookbook-scheduled-brief-retire-assets"
description: "Schedulable morning-brief email summarizing retire assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_assets", "rar_sha256": "d296c6069831e230682319d338d77f7fd980667b39080fd9e3e48f75276633f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_retire_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_retire_assets_agent.py` and in the RCI capsule.

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

Retire assets Scheduled Email Brief — Schedulable morning-brief email summarizing retire assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_retire_assets_agent.py` and embedded as the fenced Python below (sha256 d296c6069831e230…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_retire_assets_agent.py` first:

```bash
python3 scheduled_brief_retire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_retire_assets_agent.py   # or on stdin
python3 scheduled_brief_retire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire assets Scheduled Email Brief — Schedulable morning-brief email summarizing retire assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_retire_assets',
    "version": '2.0.0',
    "display_name": 'Retire assets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing retire assets for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-retire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-retire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '66b914eec8041dc6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/retire-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-retire-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefRetireAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRetireAssets'
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
    print(ScheduledBriefRetireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
