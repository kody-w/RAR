---
name: "rar-cowork-cookbook-configure-retry-background-jobs"
description: "Applies a bulk configuration change to retry background jobs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_retry_background_jobs", "rar_sha256": "ea2ca4482b0e4342856419aea1d64cd4dcd996e8bcc025878a69d5aecdfae6be", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_retry_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-retry-background-jobs:03f1c905d4983e6a31316bfd690f4c891bf23a3439c0669d0ff1202f278a352c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_retry_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_retry_background_jobs_agent.py` is
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

Retry background jobs Configuration Bulk Setup — Applies a bulk configuration change to retry background jobs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-retry-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_retry_background_jobs_agent.py` and embedded as the fenced Python below (sha256 ea2ca4482b0e4342…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_retry_background_jobs_agent.py` first:

```bash
python3 configure_retry_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_retry_background_jobs_agent.py   # or on stdin
python3 configure_retry_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retry background jobs Configuration Bulk Setup — Applies a bulk configuration change to retry background jobs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-retry-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_retry_background_jobs',
    "version": '2.0.0',
    "display_name": 'Retry background jobs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to retry background jobs from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-retry-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-retry-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '375923820ea8f062',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/retry-background-jobs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-retry-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureRetryBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRetryBackgroundJobs'
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
    print(ConfigureRetryBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
