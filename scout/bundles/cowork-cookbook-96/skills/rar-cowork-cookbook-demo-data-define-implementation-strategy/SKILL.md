---
name: "rar-cowork-cookbook-demo-data-define-implementation-strategy"
description: "Generates and creates realistic demo records for define implementation strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_implementation_strategy", "rar_sha256": "20ce55314d5721defb8696416fb0b93d1360be3829d54c126277b194245508e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_implementation_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_implementation_strategy_agent.py` and in the RCI capsule.

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

Define implementation strategy Demo Data Generator — Generates and creates realistic demo records for define implementation strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-implementation-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_implementation_strategy_agent.py` and embedded as the fenced Python below (sha256 20ce55314d5721de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_implementation_strategy_agent.py` first:

```bash
python3 demo_data_define_implementation_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_implementation_strategy_agent.py   # or on stdin
python3 demo_data_define_implementation_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define implementation strategy Demo Data Generator — Generates and creates realistic demo records for define implementation strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-implementation-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_implementation_strategy',
    "version": '2.0.0',
    "display_name": 'Define implementation strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define implementation strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-implementation-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-implementation-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd236be18b667108a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-implementation-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-define-implementation-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDefineImplementationStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineImplementationStrategy'
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
    print(DemoDataDefineImplementationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
