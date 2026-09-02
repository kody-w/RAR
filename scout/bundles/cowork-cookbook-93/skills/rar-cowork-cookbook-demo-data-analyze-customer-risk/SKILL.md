---
name: "rar-cowork-cookbook-demo-data-analyze-customer-risk"
description: "Generates and creates realistic demo records for analyze customer risk in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_customer_risk", "rar_sha256": "ed241a2b6f8f2d4423be0bcadb9da876060a1f7150e558f716349f8f63bdc30a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_analyze_customer_risk_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-analyze-customer-risk:ab63002d2ddf9b29c384bf8bd6390d5a92ba78f029b03e16457ab01a755a6505", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_analyze_customer_risk`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_analyze_customer_risk_agent.py` is
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
