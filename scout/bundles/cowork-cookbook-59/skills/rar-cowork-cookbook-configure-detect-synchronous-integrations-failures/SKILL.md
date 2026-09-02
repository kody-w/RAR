---
name: "rar-cowork-cookbook-configure-detect-synchronous-integrations-failures"
description: "Applies a bulk configuration change to detect synchronous integrations failures from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_detect_synchronous_integrations_failures", "rar_sha256": "e0e545c5d4dfba790f0725624f154e5c3b33ef8a38ed8782b93c94fc78c9d668", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_detect_synchronous_integrations_failures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-detect-synchronous-integrations-failures:a13b25e4f5bbaff0180313f4adc607cd21eb5428eecd68dea89bc50928506ab1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_detect_synchronous_integrations_failures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_detect_synchronous_integrations_failures_agent.py` is
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
