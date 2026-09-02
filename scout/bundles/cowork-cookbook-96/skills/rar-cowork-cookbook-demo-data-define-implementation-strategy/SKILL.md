---
name: "rar-cowork-cookbook-demo-data-define-implementation-strategy"
description: "Generates and creates realistic demo records for define implementation strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_implementation_strategy", "rar_sha256": "20ce55314d5721defb8696416fb0b93d1360be3829d54c126277b194245508e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_implementation_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-implementation-strategy:5096f2e51990f50ee0dded0a26304974e9696038c1ff3634544bf1b77289abdd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_implementation_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_implementation_strategy_agent.py` is
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
