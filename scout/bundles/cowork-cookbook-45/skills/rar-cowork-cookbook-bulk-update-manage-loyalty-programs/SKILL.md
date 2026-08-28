---
name: "rar-cowork-cookbook-bulk-update-manage-loyalty-programs"
description: "Applies a bulk field update across manage loyalty programs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_loyalty_programs", "rar_sha256": "2398a051f4815b7189bc37663e3745e02086d9b8bc44e7bddae47012aa908155", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_loyalty_programs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_loyalty_programs_agent.py` and in the RCI capsule.

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

Manage loyalty programs Bulk Field Update — Applies a bulk field update across manage loyalty programs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 2398a051f4815b71…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_loyalty_programs_agent.py` first:

```bash
python3 bulk_update_manage_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_loyalty_programs_agent.py   # or on stdin
python3 bulk_update_manage_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage loyalty programs Bulk Field Update — Applies a bulk field update across manage loyalty programs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_loyalty_programs',
    "version": '2.0.1',
    "display_name": 'Manage loyalty programs Bulk Field Update',
    "description": 'Applies a bulk field update across manage loyalty programs records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-manage-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd89a9d0f3e987374',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/manage-loyalty-programs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-manage-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageLoyaltyPrograms(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageLoyaltyPrograms'
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
    print(BulkUpdateManageLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
