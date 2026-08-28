---
name: "rar-cowork-cookbook-demo-data-analyze-sales-data"
description: "Generates and creates realistic demo records for analyze sales data in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_sales_data", "rar_sha256": "9a96e1894351c860ebefaa9baaa12214bc8320bf256f35baaf40b63010ec613c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_sales_data_agent.py` and embedded as the fenced Python below (sha256 9a96e1894351c860…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_sales_data_agent.py` first:

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
    "version": '2.0.0',
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
