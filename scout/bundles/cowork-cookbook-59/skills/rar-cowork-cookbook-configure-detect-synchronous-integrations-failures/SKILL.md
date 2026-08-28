---
name: "rar-cowork-cookbook-configure-detect-synchronous-integrations-failures"
description: "Applies a bulk configuration change to detect synchronous integrations failures from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_detect_synchronous_integrations_failures", "rar_sha256": "95c9414a8261e7746214d31745b9b391641c869d076e6238332dd28a83534ff4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_detect_synchronous_integrations_failures`. The original RAPP
agent is preserved byte-for-byte in `configure_detect_synchronous_integrations_failures_agent.py` and in the RCI capsule.

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

Detect synchronous integrations failures Configuration Bulk Setup — Applies a bulk configuration change to detect synchronous integrations failures from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-detect-synchronous-integrations-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_detect_synchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 95c9414a8261e774…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_detect_synchronous_integrations_failures_agent.py` first:

```bash
python3 configure_detect_synchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_detect_synchronous_integrations_failures_agent.py   # or on stdin
python3 configure_detect_synchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect synchronous integrations failures Configuration Bulk Setup — Applies a bulk configuration change to detect synchronous integrations failures from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-detect-synchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_detect_synchronous_integrations_failures',
    "version": '2.0.1',
    "display_name": 'Detect synchronous integrations failures Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to detect synchronous integrations failures from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-detect-synchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-detect-synchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16c3ccd0995bafee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-synchronous-integrations-failures'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-detect-synchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDetectSynchronousIntegrationsFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDetectSynchronousIntegrationsFailures'
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
    print(ConfigureDetectSynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
