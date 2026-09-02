---
name: "rar-cowork-cookbook-demo-data-define-preliminary-budgets"
description: "Generates and creates realistic demo records for define preliminary budgets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_preliminary_budgets", "rar_sha256": "80b9d6331558bac909c5956fdc67ef5533791371d8d2e5c38f3c2a42cfb76278", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_preliminary_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-preliminary-budgets:6704b4c7fa581e0c4281116bd60a78f834db2f140ccd70594f20be9be7023014", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_preliminary_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_preliminary_budgets_agent.py` is
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

Define preliminary budgets Demo Data Generator — Generates and creates realistic demo records for define preliminary budgets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-preliminary-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_preliminary_budgets_agent.py` and embedded as the fenced Python below (sha256 80b9d6331558bac9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_preliminary_budgets_agent.py` first:

```bash
python3 demo_data_define_preliminary_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_preliminary_budgets_agent.py   # or on stdin
python3 demo_data_define_preliminary_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define preliminary budgets Demo Data Generator — Generates and creates realistic demo records for define preliminary budgets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-preliminary-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_preliminary_budgets',
    "version": '2.0.0',
    "display_name": 'Define preliminary budgets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define preliminary budgets in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-define-preliminary-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-preliminary-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b8c6ac49e54667b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/define-preliminary-budgets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-define-preliminary-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDefinePreliminaryBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefinePreliminaryBudgets'
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
    print(DemoDataDefinePreliminaryBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
