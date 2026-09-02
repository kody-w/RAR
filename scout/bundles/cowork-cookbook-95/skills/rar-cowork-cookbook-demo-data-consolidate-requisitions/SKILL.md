---
name: "rar-cowork-cookbook-demo-data-consolidate-requisitions"
description: "Generates and creates realistic demo records for consolidate requisitions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_consolidate_requisitions", "rar_sha256": "3d7a46202e6d2983b0931b54651e15e073ab7dacc43aca5a17d6609ed041ff83", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_consolidate_requisitions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-consolidate-requisitions:5faa1d9de9f97b5bb7ef1d08975808ff7c804160e9ec28774f86965c142b9817", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_consolidate_requisitions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_consolidate_requisitions_agent.py` is
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

Consolidate requisitions Demo Data Generator — Generates and creates realistic demo records for consolidate requisitions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-requisitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_consolidate_requisitions_agent.py` and embedded as the fenced Python below (sha256 3d7a46202e6d2983…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_consolidate_requisitions_agent.py` first:

```bash
python3 demo_data_consolidate_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_consolidate_requisitions_agent.py   # or on stdin
python3 demo_data_consolidate_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate requisitions Demo Data Generator — Generates and creates realistic demo records for consolidate requisitions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_consolidate_requisitions',
    "version": '2.0.0',
    "display_name": 'Consolidate requisitions Demo Data Generator',
    "description": 'Generates and creates realistic demo records for consolidate requisitions in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-consolidate-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-consolidate-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50c2b806e5bfba6b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/consolidate-requisitions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-consolidate-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataConsolidateRequisitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConsolidateRequisitions'
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
    print(DemoDataConsolidateRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
