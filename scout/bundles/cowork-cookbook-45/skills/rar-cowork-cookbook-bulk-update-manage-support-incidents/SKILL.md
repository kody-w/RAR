---
name: "rar-cowork-cookbook-bulk-update-manage-support-incidents"
description: "Applies a bulk field update across manage support incidents records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_support_incidents", "rar_sha256": "eb3782889fd5137ed4143f75c6c0086f43e44be0d0f07875d59b3553c2b819ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_manage_support_incidents_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-manage-support-incidents:7b2fe7ee7342bba7f903ed65491a67b58c3463bb66e741260dc7b4ebe2973897", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_manage_support_incidents`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_manage_support_incidents_agent.py` is
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

Manage support incidents Bulk Field Update — Applies a bulk field update across manage support incidents records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-support-incidents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_support_incidents_agent.py` and embedded as the fenced Python below (sha256 eb3782889fd5137e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_support_incidents_agent.py` first:

```bash
python3 bulk_update_manage_support_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_support_incidents_agent.py   # or on stdin
python3 bulk_update_manage_support_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage support incidents Bulk Field Update — Applies a bulk field update across manage support incidents records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-support-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_support_incidents',
    "version": '2.0.0',
    "display_name": 'Manage support incidents Bulk Field Update',
    "description": 'Applies a bulk field update across manage support incidents records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-manage-support-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-support-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd361dfd887ef80c3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/manage-support-incidents'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-manage-support-incidents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageSupportIncidents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageSupportIncidents'
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
    print(BulkUpdateManageSupportIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
