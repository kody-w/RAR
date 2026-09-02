---
name: "rar-cowork-cookbook-scheduled-brief-update-asset-register"
description: "Schedulable morning-brief email summarizing update asset register for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_asset_register", "rar_sha256": "36e32a4768766df3fce9ac22a4a5fa0a2085a52016b1a7414e89a0f7fcd90e5e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_update_asset_register_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-update-asset-register:c30bf5caf5a41066b9bed8a5e96be033a197cfd488d7704d7c0cf39b8d553645", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_update_asset_register`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_update_asset_register_agent.py` is
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
