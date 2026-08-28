---
name: "rar-cowork-cookbook-demo-data-trace-manufactured-goods"
description: "Generates and creates realistic demo records for trace manufactured goods in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_trace_manufactured_goods", "rar_sha256": "f1b2e93425bd609a8ea96aa9f2048a2f5247398c7ab780258f67ed9d2f60cbd9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_trace_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 f1b2e93425bd609a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_trace_manufactured_goods_agent.py` first:

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
    "version": '2.0.1',
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
