---
name: "rar-cowork-cookbook-bulk-update-hire-for-open-positions"
description: "Applies a bulk field update across hire for open positions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_hire_for_open_positions", "rar_sha256": "2df159badddbc45433daec8cd17a5df8b9a5774ebf7bb4b74e37d54b3315362e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_hire_for_open_positions_agent.py` and embedded as the fenced Python below (sha256 2df159badddbc454…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_hire_for_open_positions_agent.py` first:

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
    "version": '2.0.0',
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
