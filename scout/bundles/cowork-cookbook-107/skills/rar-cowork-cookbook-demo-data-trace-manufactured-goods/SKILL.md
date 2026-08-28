---
name: "rar-cowork-cookbook-demo-data-trace-manufactured-goods"
description: "Generates and creates realistic demo records for trace manufactured goods in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_trace_manufactured_goods", "rar_sha256": "41a0ba6e2502a552bcb7b1e213491874af4793b4a8dd615d3e7d342744545f51", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_trace_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `demo_data_trace_manufactured_goods_agent.py` and in the RCI capsule.

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

Trace manufactured goods Demo Data Generator — Generates and creates realistic demo records for trace manufactured goods in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-trace-manufactured-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_trace_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 41a0ba6e2502a552…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_trace_manufactured_goods_agent.py` first:

```bash
python3 demo_data_trace_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_trace_manufactured_goods_agent.py   # or on stdin
python3 demo_data_trace_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Trace manufactured goods Demo Data Generator — Generates and creates realistic demo records for trace manufactured goods in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-trace-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_trace_manufactured_goods',
    "version": '2.0.0',
    "display_name": 'Trace manufactured goods Demo Data Generator',
    "description": 'Generates and creates realistic demo records for trace manufactured goods in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-trace-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-trace-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c7d132d579b4aff1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/trace-manufactured-goods'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-trace-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataTraceManufacturedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTraceManufacturedGoods'
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
    print(DemoDataTraceManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
