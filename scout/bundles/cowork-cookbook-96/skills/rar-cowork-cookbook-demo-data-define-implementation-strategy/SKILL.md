---
name: "rar-cowork-cookbook-demo-data-define-implementation-strategy"
description: "Generates and creates realistic demo records for define implementation strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_implementation_strategy", "rar_sha256": "46ef9de474dc802855c745080bdcc0b4627b1479a754ed348c7c1bec541502db", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_implementation_strategy_agent.py` and embedded as the fenced Python below (sha256 46ef9de474dc8028…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_implementation_strategy_agent.py` first:

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
    "version": '2.0.1',
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
