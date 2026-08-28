---
name: "rar-cowork-cookbook-demo-data-manage-deferrals"
description: "Generates and creates realistic demo records for manage deferrals in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_deferrals", "rar_sha256": "1acc605f17dd33c55114c744db983a4444acc2edf369e47b57f5a0b9573c2344", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_deferrals`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_deferrals_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_deferrals_agent.py` and embedded as the fenced Python below (sha256 1acc605f17dd33c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_deferrals_agent.py` first:

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
    "version": '2.0.1',
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
