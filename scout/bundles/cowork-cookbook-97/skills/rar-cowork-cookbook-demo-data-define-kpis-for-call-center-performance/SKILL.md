---
name: "rar-cowork-cookbook-demo-data-define-kpis-for-call-center-performance"
description: "Generates and creates realistic demo records for define KPIs for call center performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_kpis_for_call_center_performance", "rar_sha256": "4307fb6e55b95ba19af12e1d46a135cafb8659fd138b34532afbcce0cf266ef7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_kpis_for_call_center_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-kpis-for-call-center-performance:80b30e08450927779687b863f28c7ceac2ddf6422f32756ad962ad67319de080", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_kpis_for_call_center_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_kpis_for_call_center_performance_agent.py` is
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
