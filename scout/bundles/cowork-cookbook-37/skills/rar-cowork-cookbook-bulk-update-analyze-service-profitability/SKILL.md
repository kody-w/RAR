---
name: "rar-cowork-cookbook-bulk-update-analyze-service-profitability"
description: "Applies a bulk field update across analyze service profitability records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_service_profitability", "rar_sha256": "ec6f9b012356b7e6de1f9a2f65e3b562926219de397f9b74e308bc613f3f0b06", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_service_profitability_agent.py` and embedded as the fenced Python below (sha256 ec6f9b012356b7e6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_service_profitability_agent.py` first:

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
    "version": '2.0.0',
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
