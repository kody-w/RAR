---
name: "rar-cowork-cookbook-bulk-update-analyze-rebates-and-incentives"
description: "Applies a bulk field update across analyze rebates and incentives records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_rebates_and_incentives", "rar_sha256": "907ca88088594b302904a0dd7664cc2514c2a83fd5c450209aa08fc7c66059fd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 907ca88088594b30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_rebates_and_incentives_agent.py` first:

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
    "version": '2.0.1',
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
