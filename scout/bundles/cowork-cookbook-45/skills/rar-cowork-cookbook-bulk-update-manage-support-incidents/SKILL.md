---
name: "rar-cowork-cookbook-bulk-update-manage-support-incidents"
description: "Applies a bulk field update across manage support incidents records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_support_incidents", "rar_sha256": "0eb06c1d500144b88aa17e6c0254ab7243a71d41de2f492b9b997112267a0bc9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_support_incidents_agent.py` and embedded as the fenced Python below (sha256 0eb06c1d500144b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_support_incidents_agent.py` first:

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
    "version": '2.0.1',
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
