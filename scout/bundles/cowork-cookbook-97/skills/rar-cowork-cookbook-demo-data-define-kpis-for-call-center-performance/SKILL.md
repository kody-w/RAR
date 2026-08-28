---
name: "rar-cowork-cookbook-demo-data-define-kpis-for-call-center-performance"
description: "Generates and creates realistic demo records for define KPIs for call center performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_kpis_for_call_center_performance", "rar_sha256": "4307fb6e55b95ba19af12e1d46a135cafb8659fd138b34532afbcce0cf266ef7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_kpis_for_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_kpis_for_call_center_performance_agent.py` and in the RCI capsule.

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

Define KPIs for call center performance Demo Data Generator — Generates and creates realistic demo records for define KPIs for call center performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-kpis-for-call-center-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_kpis_for_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 4307fb6e55b95ba1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_kpis_for_call_center_performance_agent.py` first:

```bash
python3 demo_data_define_kpis_for_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_kpis_for_call_center_performance_agent.py   # or on stdin
python3 demo_data_define_kpis_for_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define KPIs for call center performance Demo Data Generator — Generates and creates realistic demo records for define KPIs for call center performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-kpis-for-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_kpis_for_call_center_performance',
    "version": '2.0.0',
    "display_name": 'Define KPIs for call center performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define KPIs for call center performance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-kpis-for-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-kpis-for-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '074e81abce60d73c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-kpis-for-call-center-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-define-kpis-for-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDefineKpisForCallCenterPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineKpisForCallCenterPerformance'
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
    print(DemoDataDefineKpisForCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
