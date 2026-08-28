---
name: "rar-cowork-cookbook-teams-update-develop-company-structure"
description: "Drafts a Teams channel post on develop company structure status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_company_structure", "rar_sha256": "07ab9e29eed9362250b662d287de0a51b60bc65876f260cc23050042626ab6cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_company_structure_agent.py` and embedded as the fenced Python below (sha256 07ab9e29eed93622…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_company_structure_agent.py` first:

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
    "version": '2.0.0',
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
