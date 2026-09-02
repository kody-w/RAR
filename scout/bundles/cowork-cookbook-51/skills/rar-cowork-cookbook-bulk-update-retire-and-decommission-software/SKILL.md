---
name: "rar-cowork-cookbook-bulk-update-retire-and-decommission-software"
description: "Applies a bulk field update across retire and decommission software records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retire_and_decommission_software", "rar_sha256": "de49bdfb459e72456f1a3a146bc9b82ed1235d4b616529fee04eeb8b7fa18689", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_retire_and_decommission_software_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-retire-and-decommission-software:7ff849cb0d8e9ad3def893fec8fd7a5492f176753496abc0ef8de38671ebba09", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_retire_and_decommission_software`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_retire_and_decommission_software_agent.py` is
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

Retire and decommission software Bulk Field Update — Applies a bulk field update across retire and decommission software records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-and-decommission-software
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_retire_and_decommission_software_agent.py` and embedded as the fenced Python below (sha256 de49bdfb459e7245…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_retire_and_decommission_software_agent.py` first:

```bash
python3 bulk_update_retire_and_decommission_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_retire_and_decommission_software_agent.py   # or on stdin
python3 bulk_update_retire_and_decommission_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire and decommission software Bulk Field Update — Applies a bulk field update across retire and decommission software records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-and-decommission-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_retire_and_decommission_software',
    "version": '2.0.0',
    "display_name": 'Retire and decommission software Bulk Field Update',
    "description": 'Applies a bulk field update across retire and decommission software records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-retire-and-decommission-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-retire-and-decommission-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ca606ba475434478',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/retire-and-decommission-software'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-retire-and-decommission-software', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRetireAndDecommissionSoftware(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRetireAndDecommissionSoftware'
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
    print(BulkUpdateRetireAndDecommissionSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
