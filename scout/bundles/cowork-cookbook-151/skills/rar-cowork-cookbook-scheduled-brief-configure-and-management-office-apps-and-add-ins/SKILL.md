---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-management-office-apps-and-add-ins"
description: "Schedulable morning-brief email summarizing configure and management office apps and add-ins for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins", "rar_sha256": "4380c261fbbf6556e6d164f6c962e7fc966b5006e5f19b1bdd66c9f8539fa578", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-configure-and-management-office-apps-and-add-ins:27cb12eeabbd88cbde51f0918816912627a4e4ba5aac69022bc39949fe574d53", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py` is
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
