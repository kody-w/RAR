---
name: "rar-cowork-cookbook-bulk-update-conduct-competitive-analysis"
description: "Applies a bulk field update across conduct competitive analysis records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_competitive_analysis", "rar_sha256": "c03f6a8982f3a230dc41b89d3bd4054a305d4d9dc2f45959931e195c975da446", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_competitive_analysis_agent.py` and embedded as the fenced Python below (sha256 c03f6a8982f3a230…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_competitive_analysis_agent.py` first:

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
    "version": '2.0.0',
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
