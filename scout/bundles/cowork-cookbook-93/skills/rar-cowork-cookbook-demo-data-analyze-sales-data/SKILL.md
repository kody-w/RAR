---
name: "rar-cowork-cookbook-demo-data-analyze-sales-data"
description: "Generates and creates realistic demo records for analyze sales data in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_sales_data", "rar_sha256": "a7e3d8bb2ba4b06c75a111a98403d035d3173391f64507fe2b939e1e20955e3c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_sales_data`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_sales_data_agent.py` and in the RCI capsule.

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

Analyze sales data Demo Data Generator — Generates and creates realistic demo records for analyze sales data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sales-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_sales_data_agent.py` and embedded as the fenced Python below (sha256 a7e3d8bb2ba4b06c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_sales_data_agent.py` first:

```bash
python3 demo_data_analyze_sales_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_sales_data_agent.py   # or on stdin
python3 demo_data_analyze_sales_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sales data Demo Data Generator — Generates and creates realistic demo records for analyze sales data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sales-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_sales_data',
    "version": '2.0.1',
    "display_name": 'Analyze sales data Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze sales data in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-sales-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-sales-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3c593819c483bcb7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-analyze-sales-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataAnalyzeSalesData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeSalesData'
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
    print(DemoDataAnalyzeSalesData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
