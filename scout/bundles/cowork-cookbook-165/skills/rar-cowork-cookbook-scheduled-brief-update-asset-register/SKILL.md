---
name: "rar-cowork-cookbook-scheduled-brief-update-asset-register"
description: "Schedulable morning-brief email summarizing update asset register for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_asset_register", "rar_sha256": "36e32a4768766df3fce9ac22a4a5fa0a2085a52016b1a7414e89a0f7fcd90e5e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_asset_register_agent.py` and embedded as the fenced Python below (sha256 36e32a4768766df3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_asset_register_agent.py` first:

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
    "version": '2.0.0',
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
