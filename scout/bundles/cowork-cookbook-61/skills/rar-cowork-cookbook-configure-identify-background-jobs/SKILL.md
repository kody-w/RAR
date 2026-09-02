---
name: "rar-cowork-cookbook-configure-identify-background-jobs"
description: "Applies a bulk configuration change to identify background jobs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_background_jobs", "rar_sha256": "e166b6139f0793fb5662220dd3c954721d5ace5d556e7d4a38c54fe8604de596", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_identify_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-identify-background-jobs:de5fd8d63462ea725e37dd52c6d16b201a794d706099c92697d0c861f650316d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_identify_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_identify_background_jobs_agent.py` is
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

Identify background jobs Configuration Bulk Setup — Applies a bulk configuration change to identify background jobs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_identify_background_jobs_agent.py` and embedded as the fenced Python below (sha256 e166b6139f0793fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_identify_background_jobs_agent.py` first:

```bash
python3 configure_identify_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_identify_background_jobs_agent.py   # or on stdin
python3 configure_identify_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify background jobs Configuration Bulk Setup — Applies a bulk configuration change to identify background jobs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_identify_background_jobs',
    "version": '2.0.0',
    "display_name": 'Identify background jobs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to identify background jobs from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-identify-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-identify-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7ecb3e8a80b33384',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/identify-background-jobs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-identify-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureIdentifyBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureIdentifyBackgroundJobs'
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
    print(ConfigureIdentifyBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
