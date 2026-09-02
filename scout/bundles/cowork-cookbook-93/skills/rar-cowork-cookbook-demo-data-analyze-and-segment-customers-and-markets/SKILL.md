---
name: "rar-cowork-cookbook-demo-data-analyze-and-segment-customers-and-markets"
description: "Generates and creates realistic demo records for analyze and segment customers and markets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_and_segment_customers_and_markets", "rar_sha256": "19fdd6e2e6305233b7ed5b93f036ae2f51781d157a3c94c7ae3914b6f0070e9b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_analyze_and_segment_customers_and_markets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-analyze-and-segment-customers-and-markets:3a9180584237877ee96c1a428f1da2756c0d5f580e8d52fbd59161900874a473", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_analyze_and_segment_customers_and_markets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_analyze_and_segment_customers_and_markets_agent.py` is
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
