---
name: "rar-cowork-cookbook-bulk-update-configure-and-management-office-apps-and-add-ins"
description: "Applies a bulk field update across configure and management office apps and add-ins records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins", "rar_sha256": "1b72b14120ca2245b9f91336f197066e09a4823d69c8f9cfaa7d735bbac258c0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_configure_and_management_office_apps_and_add_ins_agent.py` and in the RCI capsule.

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
