---
name: "rar-cowork-cookbook-bulk-update-manage-loyalty-programs"
description: "Applies a bulk field update across manage loyalty programs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_loyalty_programs", "rar_sha256": "a26d10f0895633c69c1b34e46bdf637b89ed42537411529b5534efa7d3e7a079", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 a26d10f0895633c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_loyalty_programs_agent.py` first:

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
    "version": '2.0.0',
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
