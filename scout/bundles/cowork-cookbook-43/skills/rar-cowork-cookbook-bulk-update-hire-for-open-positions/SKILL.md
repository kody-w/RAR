---
name: "rar-cowork-cookbook-bulk-update-hire-for-open-positions"
description: "Applies a bulk field update across hire for open positions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_hire_for_open_positions", "rar_sha256": "c14f587760c99e03b4afd0c73aafe398af8a698467cabe6cb85839755146e837", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_hire_for_open_positions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_hire_for_open_positions_agent.py` and in the RCI capsule.

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

Hire for open positions Bulk Field Update — Applies a bulk field update across hire for open positions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-hire-for-open-positions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_hire_for_open_positions_agent.py` and embedded as the fenced Python below (sha256 c14f587760c99e03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_hire_for_open_positions_agent.py` first:

```bash
python3 bulk_update_hire_for_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_hire_for_open_positions_agent.py   # or on stdin
python3 bulk_update_hire_for_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Hire for open positions Bulk Field Update — Applies a bulk field update across hire for open positions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-hire-for-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_hire_for_open_positions',
    "version": '2.0.1',
    "display_name": 'Hire for open positions Bulk Field Update',
    "description": 'Applies a bulk field update across hire for open positions records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-hire-for-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-hire-for-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0567190f689d13f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/hire-for-open-positions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-hire-for-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateHireForOpenPositions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateHireForOpenPositions'
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
    print(BulkUpdateHireForOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
