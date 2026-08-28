---
name: "rar-cowork-cookbook-teams-update-identify-common-issues"
description: "Drafts a Teams channel post on identify common issues status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_common_issues", "rar_sha256": "d10a9f5b708513d0a8a46cd8bbed4f718231169e196a0db6ec882ca6dbc7032f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_identify_common_issues`. The original RAPP
agent is preserved byte-for-byte in `teams_update_identify_common_issues_agent.py` and in the RCI capsule.

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
