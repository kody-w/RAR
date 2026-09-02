---
name: "rar-cowork-cookbook-demo-data-trace-manufactured-goods"
description: "Generates and creates realistic demo records for trace manufactured goods in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_trace_manufactured_goods", "rar_sha256": "41a0ba6e2502a552bcb7b1e213491874af4793b4a8dd615d3e7d342744545f51", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_trace_manufactured_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-trace-manufactured-goods:33d58dad8788c73b56aa1fffc4a5e6d36e8ca4c7531d62a853c4db8e3e2369a1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_trace_manufactured_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_trace_manufactured_goods_agent.py` is
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
