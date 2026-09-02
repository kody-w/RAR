---
name: "rar-cowork-cookbook-teams-update-develop-company-structure"
description: "Drafts a Teams channel post on develop company structure status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_company_structure", "rar_sha256": "07ab9e29eed9362250b662d287de0a51b60bc65876f260cc23050042626ab6cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_develop_company_structure_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-develop-company-structure:6b71897fdfa65ba2728fe6be8d434a186e1baabbe46420bdfa50434162f5c338", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_develop_company_structure`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_develop_company_structure_agent.py` is
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
