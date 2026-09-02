---
name: "rar-cowork-cookbook-demo-data-manage-deferrals"
description: "Generates and creates realistic demo records for manage deferrals in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_deferrals", "rar_sha256": "24d564a8819a7274d42995a53504221781a1f65e1ceca2e744bda825dcea1be0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_deferrals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-deferrals:af3006e523c0222eea5a0c0b857ede897f8b209cb499d60a3aa1f4eee239b9e5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_deferrals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_deferrals_agent.py` is
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

Manage deferrals Demo Data Generator — Generates and creates realistic demo records for manage deferrals in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-deferrals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_deferrals_agent.py` and embedded as the fenced Python below (sha256 24d564a8819a7274…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_deferrals_agent.py` first:

```bash
python3 demo_data_manage_deferrals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_deferrals_agent.py   # or on stdin
python3 demo_data_manage_deferrals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage deferrals Demo Data Generator — Generates and creates realistic demo records for manage deferrals in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-deferrals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_deferrals',
    "version": '2.0.0',
    "display_name": 'Manage deferrals Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage deferrals in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-deferrals',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-deferrals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50cb6ea4a6e5c0d7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-deferrals'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-manage-deferrals', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageDeferrals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageDeferrals'
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
    print(DemoDataManageDeferrals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
