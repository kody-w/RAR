---
name: "rar-cowork-cookbook-configure-manage-open-purchases"
description: "Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_open_purchases", "rar_sha256": "6513ccf1fe74b5ca8284badd9ca3798f4d9ba8405dcfabe748106d918b557221", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_open_purchases`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_open_purchases_agent.py` and in the RCI capsule.

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

Manage open purchases Configuration Bulk Setup — Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-open-purchases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_open_purchases_agent.py` and embedded as the fenced Python below (sha256 6513ccf1fe74b5ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_open_purchases_agent.py` first:

```bash
python3 configure_manage_open_purchases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_open_purchases_agent.py   # or on stdin
python3 configure_manage_open_purchases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage open purchases Configuration Bulk Setup — Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-open-purchases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_open_purchases',
    "version": '2.0.0',
    "display_name": 'Manage open purchases Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-open-purchases',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-open-purchases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e07eb8ed54ccbdff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/manage-open-purchases'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-open-purchases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageOpenPurchases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageOpenPurchases'
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
    print(ConfigureManageOpenPurchases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
