---
name: "rar-cowork-cookbook-demo-data-analyze-and-segment-customers-and-markets"
description: "Generates and creates realistic demo records for analyze and segment customers and markets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_and_segment_customers_and_markets", "rar_sha256": "19fdd6e2e6305233b7ed5b93f036ae2f51781d157a3c94c7ae3914b6f0070e9b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_and_segment_customers_and_markets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_and_segment_customers_and_markets_agent.py` and in the RCI capsule.

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

Analyze and segment customers and markets Demo Data Generator — Generates and creates realistic demo records for analyze and segment customers and markets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-and-segment-customers-and-markets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_and_segment_customers_and_markets_agent.py` and embedded as the fenced Python below (sha256 19fdd6e2e6305233…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_and_segment_customers_and_markets_agent.py` first:

```bash
python3 demo_data_analyze_and_segment_customers_and_markets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_and_segment_customers_and_markets_agent.py   # or on stdin
python3 demo_data_analyze_and_segment_customers_and_markets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and segment customers and markets Demo Data Generator — Generates and creates realistic demo records for analyze and segment customers and markets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-and-segment-customers-and-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_and_segment_customers_and_markets',
    "version": '2.0.0',
    "display_name": 'Analyze and segment customers and markets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze and segment customers and markets in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-and-segment-customers-and-markets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-and-segment-customers-and-markets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e27c82efdb9c8e7a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/analyze-and-segment-customers-and-markets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-analyze-and-segment-customers-and-markets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAnalyzeAndSegmentCustomersAndMarkets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeAndSegmentCustomersAndMarkets'
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
    print(DemoDataAnalyzeAndSegmentCustomersAndMarkets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
