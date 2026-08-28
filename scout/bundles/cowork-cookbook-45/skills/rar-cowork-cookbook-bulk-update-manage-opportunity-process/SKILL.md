---
name: "rar-cowork-cookbook-bulk-update-manage-opportunity-process"
description: "Applies a bulk field update across manage opportunity process records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_opportunity_process", "rar_sha256": "11c530647d46e95ddce250ee2ad825c123af4e438f5809c087a3b0d0635c37f5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_opportunity_process_agent.py` and embedded as the fenced Python below (sha256 11c530647d46e95d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_opportunity_process_agent.py` first:

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
    "version": '2.0.0',
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
