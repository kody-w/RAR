---
name: "rar-cowork-cookbook-configure-detect-synchronous-integrations-failures"
description: "Applies a bulk configuration change to detect synchronous integrations failures from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_detect_synchronous_integrations_failures", "rar_sha256": "e0e545c5d4dfba790f0725624f154e5c3b33ef8a38ed8782b93c94fc78c9d668", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_detect_synchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 e0e545c5d4dfba79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_detect_synchronous_integrations_failures_agent.py` first:

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
    "version": '2.0.0',
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
