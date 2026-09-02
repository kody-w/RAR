---
name: "rar-cowork-cookbook-demo-data-define-costing-policies"
description: "Generates and creates realistic demo records for define costing policies in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_costing_policies", "rar_sha256": "466bd212fc2b5258699e0c2b8e2bec62de71ded47c2c3db03adcd33edfee5161", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_costing_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-costing-policies:73dea48fa864edcd66c7744757ae6f68a5754ea18ed4b9ebd03e27619f77379a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_costing_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_costing_policies_agent.py` is
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

Define costing policies Demo Data Generator — Generates and creates realistic demo records for define costing policies in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-costing-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_costing_policies_agent.py` and embedded as the fenced Python below (sha256 466bd212fc2b5258…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_costing_policies_agent.py` first:

```bash
python3 demo_data_define_costing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_costing_policies_agent.py   # or on stdin
python3 demo_data_define_costing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define costing policies Demo Data Generator — Generates and creates realistic demo records for define costing policies in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-costing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_costing_policies',
    "version": '2.0.0',
    "display_name": 'Define costing policies Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define costing policies in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-costing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-costing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c2dd57fb11e2aee6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-costing-policies'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-define-costing-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDefineCostingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineCostingPolicies'
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
    print(DemoDataDefineCostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
