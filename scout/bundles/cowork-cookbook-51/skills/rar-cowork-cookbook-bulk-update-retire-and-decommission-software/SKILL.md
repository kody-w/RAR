---
name: "rar-cowork-cookbook-bulk-update-retire-and-decommission-software"
description: "Applies a bulk field update across retire and decommission software records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retire_and_decommission_software", "rar_sha256": "de49bdfb459e72456f1a3a146bc9b82ed1235d4b616529fee04eeb8b7fa18689", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_retire_and_decommission_software`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_retire_and_decommission_software_agent.py` and in the RCI capsule.

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
