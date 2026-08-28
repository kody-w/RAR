---
name: "rar-cowork-cookbook-scheduled-brief-manage-service-assets"
description: "Schedulable morning-brief email summarizing manage service assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_service_assets", "rar_sha256": "aafe6f3b7760b143e1068c72d92c0d0df8bca4f5a4653b9bd556503eef405cce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_service_assets_agent.py` and embedded as the fenced Python below (sha256 aafe6f3b7760b143…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_service_assets_agent.py` first:

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
    "version": '2.0.0',
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
