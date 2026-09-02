---
name: "rar-cowork-cookbook-configure-define-sales-channels"
description: "Applies a bulk configuration change to define sales channels from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_sales_channels", "rar_sha256": "ab9ae7fef52139ab77555e6588378d6cfd13f42a7e948081d669d88e5706dba5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_define_sales_channels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-define-sales-channels:aa5d91d8e2e16fc536f82f4f601cc430ba33957ef1c755553de9f7348adec656", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_define_sales_channels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_define_sales_channels_agent.py` is
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
