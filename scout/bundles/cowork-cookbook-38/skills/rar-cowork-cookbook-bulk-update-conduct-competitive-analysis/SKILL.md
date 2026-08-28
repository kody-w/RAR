---
name: "rar-cowork-cookbook-bulk-update-conduct-competitive-analysis"
description: "Applies a bulk field update across conduct competitive analysis records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_competitive_analysis", "rar_sha256": "60c02df43aa71d0bb748869f8b1674500df0181ea43818f1704665baf386838b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_conduct_competitive_analysis`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_conduct_competitive_analysis_agent.py` and in the RCI capsule.

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

Conduct competitive analysis Bulk Field Update — Applies a bulk field update across conduct competitive analysis records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-competitive-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_competitive_analysis_agent.py` and embedded as the fenced Python below (sha256 60c02df43aa71d0b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_competitive_analysis_agent.py` first:

```bash
python3 bulk_update_conduct_competitive_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_conduct_competitive_analysis_agent.py   # or on stdin
python3 bulk_update_conduct_competitive_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct competitive analysis Bulk Field Update — Applies a bulk field update across conduct competitive analysis records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-competitive-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_conduct_competitive_analysis',
    "version": '2.0.1',
    "display_name": 'Conduct competitive analysis Bulk Field Update',
    "description": 'Applies a bulk field update across conduct competitive analysis records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-conduct-competitive-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-conduct-competitive-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d154891813cf7c6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/conduct-competitive-analysis'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-conduct-competitive-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateConductCompetitiveAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConductCompetitiveAnalysis'
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
    print(BulkUpdateConductCompetitiveAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
