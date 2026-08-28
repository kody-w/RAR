---
name: "rar-cowork-cookbook-teams-update-configure-and-run-background-jobs"
description: "Drafts a Teams channel post on configure and run background jobs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_run_background_jobs", "rar_sha256": "5534f91f6548cdb19f9a906ebb11ba7547d816c6c575fb96850754f8998736a0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_configure_and_run_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_configure_and_run_background_jobs_agent.py` and in the RCI capsule.

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

Configure and run background jobs Teams Channel Update — Drafts a Teams channel post on configure and run background jobs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-run-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_run_background_jobs_agent.py` and embedded as the fenced Python below (sha256 5534f91f6548cdb1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_run_background_jobs_agent.py` first:

```bash
python3 teams_update_configure_and_run_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_configure_and_run_background_jobs_agent.py   # or on stdin
python3 teams_update_configure_and_run_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and run background jobs Teams Channel Update — Drafts a Teams channel post on configure and run background jobs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-run-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_configure_and_run_background_jobs',
    "version": '2.0.1',
    "display_name": 'Configure and run background jobs Teams Channel Update',
    "description": 'Drafts a Teams channel post on configure and run background jobs status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-configure-and-run-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-configure-and-run-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '53f598e1bfac3a35',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/configure-and-run-background-jobs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-configure-and-run-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateConfigureAndRunBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConfigureAndRunBackgroundJobs'
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
    print(TeamsUpdateConfigureAndRunBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
