---
name: "rar-cowork-cookbook-demo-data-define-kpis-for-call-center-performance"
description: "Generates and creates realistic demo records for define KPIs for call center performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_kpis_for_call_center_performance", "rar_sha256": "61f4528323c9d6a01a5768dddfac6d4b7b883e7fe8b54d4e97cf8e1e1b9e325c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_kpis_for_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 61f4528323c9d6a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_kpis_for_call_center_performance_agent.py` first:

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
    "version": '2.0.1',
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
