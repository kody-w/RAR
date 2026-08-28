---
name: "rar-cowork-cookbook-scheduled-brief-retire-assets"
description: "Schedulable morning-brief email summarizing retire assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_assets", "rar_sha256": "bf20824920ad2fd7d4c6aeebd6921759c7380a9d6da648d374e73b03d2988a68", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_retire_assets_agent.py` and embedded as the fenced Python below (sha256 bf20824920ad2fd7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_retire_assets_agent.py` first:

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
    "version": '2.0.1',
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
