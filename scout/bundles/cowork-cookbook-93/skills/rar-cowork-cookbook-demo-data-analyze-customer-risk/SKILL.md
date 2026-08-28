---
name: "rar-cowork-cookbook-demo-data-analyze-customer-risk"
description: "Generates and creates realistic demo records for analyze customer risk in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_customer_risk", "rar_sha256": "ed241a2b6f8f2d4423be0bcadb9da876060a1f7150e558f716349f8f63bdc30a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_customer_risk`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_customer_risk_agent.py` and in the RCI capsule.

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

Analyze customer risk Demo Data Generator — Generates and creates realistic demo records for analyze customer risk in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-customer-risk
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_customer_risk_agent.py` and embedded as the fenced Python below (sha256 ed241a2b6f8f2d44…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_customer_risk_agent.py` first:

```bash
python3 demo_data_analyze_customer_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_customer_risk_agent.py   # or on stdin
python3 demo_data_analyze_customer_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze customer risk Demo Data Generator — Generates and creates realistic demo records for analyze customer risk in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-customer-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_customer_risk',
    "version": '2.0.0',
    "display_name": 'Analyze customer risk Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze customer risk in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-customer-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-customer-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb312d5f58e85713',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-customer-risk'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-analyze-customer-risk', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAnalyzeCustomerRisk(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeCustomerRisk'
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
    print(DemoDataAnalyzeCustomerRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
