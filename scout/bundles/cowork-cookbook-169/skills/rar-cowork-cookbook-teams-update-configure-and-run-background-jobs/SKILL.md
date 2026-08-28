---
name: "rar-cowork-cookbook-teams-update-configure-and-run-background-jobs"
description: "Drafts a Teams channel post on configure and run background jobs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_run_background_jobs", "rar_sha256": "a7f97d8c66d1c9ee6d4c9833cd46d529602a95249e03447035a7beb7a3cdc3f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_run_background_jobs_agent.py` and embedded as the fenced Python below (sha256 a7f97d8c66d1c9ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_run_background_jobs_agent.py` first:

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
    "version": '2.0.0',
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
