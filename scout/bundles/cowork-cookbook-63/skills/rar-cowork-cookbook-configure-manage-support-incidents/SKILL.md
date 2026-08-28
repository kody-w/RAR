---
name: "rar-cowork-cookbook-configure-manage-support-incidents"
description: "Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_support_incidents", "rar_sha256": "7bba4b977d2b457c1b75a698b551aa1b122788ecff82509809259a9d0889a9a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_support_incidents`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_support_incidents_agent.py` and in the RCI capsule.

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

Manage support incidents Configuration Bulk Setup — Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-support-incidents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_support_incidents_agent.py` and embedded as the fenced Python below (sha256 7bba4b977d2b457c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_support_incidents_agent.py` first:

```bash
python3 configure_manage_support_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_support_incidents_agent.py   # or on stdin
python3 configure_manage_support_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage support incidents Configuration Bulk Setup — Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-support-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_support_incidents',
    "version": '2.0.0',
    "display_name": 'Manage support incidents Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-manage-support-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-support-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '654bffc250c9f16d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/manage-support-incidents'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-support-incidents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageSupportIncidents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSupportIncidents'
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
    print(ConfigureManageSupportIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
