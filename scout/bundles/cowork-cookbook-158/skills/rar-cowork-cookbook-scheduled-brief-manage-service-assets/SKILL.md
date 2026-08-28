---
name: "rar-cowork-cookbook-scheduled-brief-manage-service-assets"
description: "Schedulable morning-brief email summarizing manage service assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_service_assets", "rar_sha256": "c34c05d82fa38c3eaa3b41401b1c13695fe21e6b9828c2458b07ab0ca09b5df3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_service_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_service_assets_agent.py` and in the RCI capsule.

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

Manage service assets Scheduled Email Brief — Schedulable morning-brief email summarizing manage service assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-service-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_service_assets_agent.py` and embedded as the fenced Python below (sha256 c34c05d82fa38c3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_service_assets_agent.py` first:

```bash
python3 scheduled_brief_manage_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_service_assets_agent.py   # or on stdin
python3 scheduled_brief_manage_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service assets Scheduled Email Brief — Schedulable morning-brief email summarizing manage service assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_service_assets',
    "version": '2.0.1',
    "display_name": 'Manage service assets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage service assets for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-manage-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '23c11e3b9485f363',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/manage-service-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-manage-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageServiceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageServiceAssets'
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
    print(ScheduledBriefManageServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
