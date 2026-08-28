---
name: "rar-cowork-cookbook-bulk-update-conduct-research"
description: "Applies a bulk field update across conduct research records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_research", "rar_sha256": "8b111e9c911b768bf5b09c22e393f05bad2e3bf570e879114c1e64df15ff3f9d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_conduct_research`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_conduct_research_agent.py` and in the RCI capsule.

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

Conduct research Bulk Field Update — Applies a bulk field update across conduct research records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-research
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_research_agent.py` and embedded as the fenced Python below (sha256 8b111e9c911b768b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_research_agent.py` first:

```bash
python3 bulk_update_conduct_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_conduct_research_agent.py   # or on stdin
python3 bulk_update_conduct_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct research Bulk Field Update — Applies a bulk field update across conduct research records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_conduct_research',
    "version": '2.0.1',
    "display_name": 'Conduct research Bulk Field Update',
    "description": 'Applies a bulk field update across conduct research records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-conduct-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-conduct-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd251af21f42fcb53',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/conduct-research'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-conduct-research', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateConductResearch(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConductResearch'
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
    print(BulkUpdateConductResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
