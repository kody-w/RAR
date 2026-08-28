---
name: "rar-cowork-cookbook-configure-retry-background-jobs"
description: "Applies a bulk configuration change to retry background jobs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_retry_background_jobs", "rar_sha256": "d4a57e5e0750525251ebe12a3d209da4555895d4a0435da33b013ab040356d43", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_retry_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `configure_retry_background_jobs_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_retry_background_jobs_agent.py` and embedded as the fenced Python below (sha256 d4a57e5e07505252…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_retry_background_jobs_agent.py` first:

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
    "version": '2.0.1',
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
