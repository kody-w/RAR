---
name: "rar-cowork-cookbook-bulk-update-manage-opportunity-process"
description: "Applies a bulk field update across manage opportunity process records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_opportunity_process", "rar_sha256": "a5eb6d462e68b785eb651158a1516ee766ce53b260c1613d6e74177568d4a5f6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_opportunity_process`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_opportunity_process_agent.py` and in the RCI capsule.

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

Manage opportunity process Bulk Field Update — Applies a bulk field update across manage opportunity process records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_opportunity_process_agent.py` and embedded as the fenced Python below (sha256 a5eb6d462e68b785…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_opportunity_process_agent.py` first:

```bash
python3 bulk_update_manage_opportunity_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_opportunity_process_agent.py   # or on stdin
python3 bulk_update_manage_opportunity_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage opportunity process Bulk Field Update — Applies a bulk field update across manage opportunity process records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_opportunity_process',
    "version": '2.0.1',
    "display_name": 'Manage opportunity process Bulk Field Update',
    "description": 'Applies a bulk field update across manage opportunity process records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-opportunity-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34c83edfbdd942b2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-manage-opportunity-process', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageOpportunityProcess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageOpportunityProcess'
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
    print(BulkUpdateManageOpportunityProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
