---
name: "rar-cowork-cookbook-bulk-update-analyze-sourcing-market"
description: "Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_sourcing_market", "rar_sha256": "f7439d08500f26f0709b76b01bf42c060f6cbd305fc580ab62383fa3938d8f18", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_sourcing_market`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_sourcing_market_agent.py` and in the RCI capsule.

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

Analyze sourcing market Bulk Field Update — Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_sourcing_market_agent.py` and embedded as the fenced Python below (sha256 f7439d08500f26f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_sourcing_market_agent.py` first:

```bash
python3 bulk_update_analyze_sourcing_market_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_sourcing_market_agent.py   # or on stdin
python3 bulk_update_analyze_sourcing_market_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing market Bulk Field Update — Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_sourcing_market',
    "version": '2.0.1',
    "display_name": 'Analyze sourcing market Bulk Field Update',
    "description": 'Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-analyze-sourcing-market',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5555bf89a931efa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/analyze-sourcing-market'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-analyze-sourcing-market', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeSourcingMarket(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeSourcingMarket'
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
    print(BulkUpdateAnalyzeSourcingMarket().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
