---
name: "rar-cowork-cookbook-demo-data-analyze-customer-risk"
description: "Generates and creates realistic demo records for analyze customer risk in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_customer_risk", "rar_sha256": "e68bf6680e8441d49cfb91b0828aef43652b26f79f66962be9c8a612e300e2c3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_customer_risk_agent.py` and embedded as the fenced Python below (sha256 e68bf6680e8441d4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_customer_risk_agent.py` first:

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
    "version": '2.0.1',
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
