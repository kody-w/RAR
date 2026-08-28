---
name: "rar-cowork-cookbook-teams-update-develop-company-structure"
description: "Drafts a Teams channel post on develop company structure status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_company_structure", "rar_sha256": "358b26563d5d9284a0a4de521030975ac9beb41b71d0396398b68016b3588dd8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_company_structure`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_company_structure_agent.py` and in the RCI capsule.

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

Develop company structure Teams Channel Update — Drafts a Teams channel post on develop company structure status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-company-structure
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_company_structure_agent.py` and embedded as the fenced Python below (sha256 358b26563d5d9284…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_company_structure_agent.py` first:

```bash
python3 teams_update_develop_company_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_company_structure_agent.py   # or on stdin
python3 teams_update_develop_company_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop company structure Teams Channel Update — Drafts a Teams channel post on develop company structure status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-company-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_company_structure',
    "version": '2.0.1',
    "display_name": 'Develop company structure Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop company structure status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-develop-company-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-company-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ed6d3bdda40015ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-company-structure'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-develop-company-structure', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDevelopCompanyStructure(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopCompanyStructure'
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
    print(TeamsUpdateDevelopCompanyStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
