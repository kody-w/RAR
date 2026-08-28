---
name: "rar-cowork-cookbook-demo-data-analyze-and-segment-customers-and-markets"
description: "Generates and creates realistic demo records for analyze and segment customers and markets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_and_segment_customers_and_markets", "rar_sha256": "44fbf86397258b47d0d863cde68f50c3c4952a9b94aa99166d9a03e59d69ea01", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_and_segment_customers_and_markets_agent.py` and embedded as the fenced Python below (sha256 44fbf86397258b47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_and_segment_customers_and_markets_agent.py` first:

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
    "version": '2.0.1',
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
