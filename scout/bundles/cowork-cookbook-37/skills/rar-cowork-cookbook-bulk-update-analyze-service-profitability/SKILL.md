---
name: "rar-cowork-cookbook-bulk-update-analyze-service-profitability"
description: "Applies a bulk field update across analyze service profitability records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_service_profitability", "rar_sha256": "9a6d94d019938f1efcf149fbae536c6b8dad543941d5439602c625d71e799f6a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_service_profitability`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_service_profitability_agent.py` and in the RCI capsule.

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

Analyze service profitability Bulk Field Update — Applies a bulk field update across analyze service profitability records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-service-profitability
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_service_profitability_agent.py` and embedded as the fenced Python below (sha256 9a6d94d019938f1e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_service_profitability_agent.py` first:

```bash
python3 bulk_update_analyze_service_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_service_profitability_agent.py   # or on stdin
python3 bulk_update_analyze_service_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze service profitability Bulk Field Update — Applies a bulk field update across analyze service profitability records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-service-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_service_profitability',
    "version": '2.0.1',
    "display_name": 'Analyze service profitability Bulk Field Update',
    "description": 'Applies a bulk field update across analyze service profitability records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-service-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-service-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ee3dd1b7e3ce0ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/analyze-service-profitability'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-analyze-service-profitability', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeServiceProfitability(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeServiceProfitability'
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
    print(BulkUpdateAnalyzeServiceProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
