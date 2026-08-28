---
name: "rar-cowork-cookbook-configure-define-sales-channels"
description: "Applies a bulk configuration change to define sales channels from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_sales_channels", "rar_sha256": "ab9ae7fef52139ab77555e6588378d6cfd13f42a7e948081d669d88e5706dba5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_sales_channels`. The original RAPP
agent is preserved byte-for-byte in `configure_define_sales_channels_agent.py` and in the RCI capsule.

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

Define sales channels Configuration Bulk Setup — Applies a bulk configuration change to define sales channels from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-sales-channels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_sales_channels_agent.py` and embedded as the fenced Python below (sha256 ab9ae7fef52139ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_sales_channels_agent.py` first:

```bash
python3 configure_define_sales_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_sales_channels_agent.py   # or on stdin
python3 configure_define_sales_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales channels Configuration Bulk Setup — Applies a bulk configuration change to define sales channels from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-sales-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_sales_channels',
    "version": '2.0.0',
    "display_name": 'Define sales channels Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define sales channels from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-sales-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-sales-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2017acd42138dab5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-channels'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-define-sales-channels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDefineSalesChannels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineSalesChannels'
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
    print(ConfigureDefineSalesChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
