---
name: "rar-cowork-cookbook-configure-define-sales-channels"
description: "Applies a bulk configuration change to define sales channels from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_sales_channels", "rar_sha256": "3e087ddd721a03015d92e5e3fb6e71004d78238e6c4406bada01f812c489d549", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_sales_channels_agent.py` and embedded as the fenced Python below (sha256 3e087ddd721a0301…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_sales_channels_agent.py` first:

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
    "version": '2.0.1',
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
