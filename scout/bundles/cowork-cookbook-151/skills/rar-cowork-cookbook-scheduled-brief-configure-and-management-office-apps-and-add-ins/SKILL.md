---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-management-office-apps-and-add-ins"
description: "Schedulable morning-brief email summarizing configure and management office apps and add-ins for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins", "rar_sha256": "4380c261fbbf6556e6d164f6c962e7fc966b5006e5f19b1bdd66c9f8539fa578", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py` and in the RCI capsule.

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

Configure and management office apps and add-ins Scheduled Email Brief — Schedulable morning-brief email summarizing configure and management office apps and add-ins for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-management-office-apps-and-add-ins
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py` and embedded as the fenced Python below (sha256 4380c261fbbf6556…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py` first:

```bash
python3 scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py   # or on stdin
python3 scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and management office apps and add-ins Scheduled Email Brief — Schedulable morning-brief email summarizing configure and management office apps and add-ins for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-management-office-apps-and-add-ins
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins',
    "version": '2.0.0',
    "display_name": 'Configure and management office apps and add-ins Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing configure and management office apps and add-ins for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-configure-and-management-office-apps-and-add-ins',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-configure-and-management-office-apps-and-add-ins',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7edbc27f1186d39a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-management-office-apps-and-add-ins'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-configure-and-management-office-apps-and-add-ins', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefConfigureAndManagementOfficeAppsAndAddIns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConfigureAndManagementOfficeAppsAndAddIns'
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
    print(ScheduledBriefConfigureAndManagementOfficeAppsAndAddIns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
