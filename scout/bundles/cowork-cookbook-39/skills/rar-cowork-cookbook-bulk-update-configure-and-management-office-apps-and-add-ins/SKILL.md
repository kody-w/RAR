---
name: "rar-cowork-cookbook-bulk-update-configure-and-management-office-apps-and-add-ins"
description: "Applies a bulk field update across configure and management office apps and add-ins records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins", "rar_sha256": "1b72b14120ca2245b9f91336f197066e09a4823d69c8f9cfaa7d735bbac258c0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_configure_and_management_office_apps_and_add_ins_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-configure-and-management-office-apps-and-add-ins:e8679313b8f737b0054d3111b0e2a1ba63d65b25cc463518802501332339fe33", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_configure_and_management_office_apps_and_add_ins_agent.py` is
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

Configure and management office apps and add-ins Bulk Field Update — Applies a bulk field update across configure and management office apps and add-ins records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-management-office-apps-and-add-ins
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_management_office_apps_and_add_ins_agent.py` and embedded as the fenced Python below (sha256 1b72b14120ca2245…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_management_office_apps_and_add_ins_agent.py` first:

```bash
python3 bulk_update_configure_and_management_office_apps_and_add_ins_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_configure_and_management_office_apps_and_add_ins_agent.py   # or on stdin
python3 bulk_update_configure_and_management_office_apps_and_add_ins_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and management office apps and add-ins Bulk Field Update — Applies a bulk field update across configure and management office apps and add-ins records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-management-office-apps-and-add-ins
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins',
    "version": '2.0.0',
    "display_name": 'Configure and management office apps and add-ins Bulk Field Update',
    "description": 'Applies a bulk field update across configure and management office apps and add-ins records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-configure-and-management-office-apps-and-add-ins',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-configure-and-management-office-apps-and-add-ins',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81e0a820150ffb5d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-management-office-apps-and-add-ins'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-configure-and-management-office-apps-and-add-ins', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateConfigureAndManagementOfficeAppsAndAddIns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConfigureAndManagementOfficeAppsAndAddIns'
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
    print(BulkUpdateConfigureAndManagementOfficeAppsAndAddIns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
