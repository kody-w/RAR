---
name: "rar-cowork-cookbook-bulk-update-analyze-rebates-and-incentives"
description: "Applies a bulk field update across analyze rebates and incentives records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_rebates_and_incentives", "rar_sha256": "e86090b3d7a95d535bee06304055d4420ecd7b8b0a3d89686d79f81032d1f5d5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_rebates_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_rebates_and_incentives_agent.py` and in the RCI capsule.

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

Analyze rebates and incentives Bulk Field Update — Applies a bulk field update across analyze rebates and incentives records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-rebates-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 e86090b3d7a95d53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_rebates_and_incentives_agent.py` first:

```bash
python3 bulk_update_analyze_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_rebates_and_incentives_agent.py   # or on stdin
python3 bulk_update_analyze_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze rebates and incentives Bulk Field Update — Applies a bulk field update across analyze rebates and incentives records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_rebates_and_incentives',
    "version": '2.0.0',
    "display_name": 'Analyze rebates and incentives Bulk Field Update',
    "description": 'Applies a bulk field update across analyze rebates and incentives records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3567aeccdf74d2eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-rebates-and-incentives'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-analyze-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeRebatesAndIncentives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeRebatesAndIncentives'
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
    print(BulkUpdateAnalyzeRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
