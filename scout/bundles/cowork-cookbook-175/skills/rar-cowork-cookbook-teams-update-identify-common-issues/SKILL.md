---
name: "rar-cowork-cookbook-teams-update-identify-common-issues"
description: "Drafts a Teams channel post on identify common issues status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_common_issues", "rar_sha256": "d10a9f5b708513d0a8a46cd8bbed4f718231169e196a0db6ec882ca6dbc7032f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_identify_common_issues_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-identify-common-issues:be039358df26d56d486d485bb326180ad4354fbd267a92d29fcc40cb4fdaf5b2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_identify_common_issues`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_identify_common_issues_agent.py` is
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

Identify common issues Teams Channel Update — Drafts a Teams channel post on identify common issues status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-common-issues
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_identify_common_issues_agent.py` and embedded as the fenced Python below (sha256 d10a9f5b708513d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_identify_common_issues_agent.py` first:

```bash
python3 teams_update_identify_common_issues_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_identify_common_issues_agent.py   # or on stdin
python3 teams_update_identify_common_issues_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify common issues Teams Channel Update — Drafts a Teams channel post on identify common issues status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-common-issues
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_identify_common_issues',
    "version": '2.0.0',
    "display_name": 'Identify common issues Teams Channel Update',
    "description": 'Drafts a Teams channel post on identify common issues status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-identify-common-issues',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-identify-common-issues',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '96e509eb4a1ede2a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/identify-common-issues'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-identify-common-issues', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateIdentifyCommonIssues(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIdentifyCommonIssues'
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
    print(TeamsUpdateIdentifyCommonIssues().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
