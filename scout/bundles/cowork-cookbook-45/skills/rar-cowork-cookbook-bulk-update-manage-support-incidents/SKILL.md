---
name: "rar-cowork-cookbook-bulk-update-manage-support-incidents"
description: "Applies a bulk field update across manage support incidents records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_support_incidents", "rar_sha256": "eb3782889fd5137ed4143f75c6c0086f43e44be0d0f07875d59b3553c2b819ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_support_incidents`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_support_incidents_agent.py` and in the RCI capsule.

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
