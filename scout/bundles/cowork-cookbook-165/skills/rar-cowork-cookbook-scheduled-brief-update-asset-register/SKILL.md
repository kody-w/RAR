---
name: "rar-cowork-cookbook-scheduled-brief-update-asset-register"
description: "Schedulable morning-brief email summarizing update asset register for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_asset_register", "rar_sha256": "ec86f65c1c1db6ec03c51021a47a996e80a5039920eefbc86382a0a410e0a99a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_update_asset_register`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_update_asset_register_agent.py` and in the RCI capsule.

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

Update asset register Scheduled Email Brief — Schedulable morning-brief email summarizing update asset register for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-asset-register
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_asset_register_agent.py` and embedded as the fenced Python below (sha256 ec86f65c1c1db6ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_asset_register_agent.py` first:

```bash
python3 scheduled_brief_update_asset_register_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_update_asset_register_agent.py   # or on stdin
python3 scheduled_brief_update_asset_register_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update asset register Scheduled Email Brief — Schedulable morning-brief email summarizing update asset register for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-asset-register
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_update_asset_register',
    "version": '2.0.1',
    "display_name": 'Update asset register Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing update asset register for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-update-asset-register',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-update-asset-register',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd92b74ffba01193f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-asset-register'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-update-asset-register', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefUpdateAssetRegister(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefUpdateAssetRegister'
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
    print(ScheduledBriefUpdateAssetRegister().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
