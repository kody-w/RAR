---
name: "rar-cowork-cookbook-configure-identify-background-jobs"
description: "Applies a bulk configuration change to identify background jobs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_background_jobs", "rar_sha256": "085f0fcd8303f08675705a855ef9f164bd945ae1dab1b670536c5f238e5f14a8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_identify_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `configure_identify_background_jobs_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_identify_background_jobs_agent.py` and embedded as the fenced Python below (sha256 085f0fcd8303f086…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_identify_background_jobs_agent.py` first:

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
    "version": '2.0.1',
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
