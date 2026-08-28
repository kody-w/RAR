---
name: "rar-cowork-cookbook-configure-retry-background-jobs"
description: "Applies a bulk configuration change to retry background jobs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_retry_background_jobs", "rar_sha256": "ea2ca4482b0e4342856419aea1d64cd4dcd996e8bcc025878a69d5aecdfae6be", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
