---
name: "rar-cowork-cookbook-bulk-update-conduct-competitive-analysis"
description: "Applies a bulk field update across conduct competitive analysis records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_competitive_analysis", "rar_sha256": "c03f6a8982f3a230dc41b89d3bd4054a305d4d9dc2f45959931e195c975da446", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_conduct_competitive_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-conduct-competitive-analysis:2bc5405e0e9873c0a8c024540c95d98f1c179f811df3e2404f17cfe08f2f51eb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_conduct_competitive_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_conduct_competitive_analysis_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
