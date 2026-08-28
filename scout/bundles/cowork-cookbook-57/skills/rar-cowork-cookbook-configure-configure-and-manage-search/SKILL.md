---
name: "rar-cowork-cookbook-configure-configure-and-manage-search"
description: "Applies a bulk configuration change to configure and manage search from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_manage_search", "rar_sha256": "cce9ec18b9a96930954709d444ae58aea389ddb76d7f3e612f37b792f1f4846f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_configure_and_manage_search`. The original RAPP
agent is preserved byte-for-byte in `configure_configure_and_manage_search_agent.py` and in the RCI capsule.

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

Configure and manage search Configuration Bulk Setup — Applies a bulk configuration change to configure and manage search from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-manage-search
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_and_manage_search_agent.py` and embedded as the fenced Python below (sha256 cce9ec18b9a96930…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_and_manage_search_agent.py` first:

```bash
python3 configure_configure_and_manage_search_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_configure_and_manage_search_agent.py   # or on stdin
python3 configure_configure_and_manage_search_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage search Configuration Bulk Setup — Applies a bulk configuration change to configure and manage search from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-manage-search
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_configure_and_manage_search',
    "version": '2.0.1',
    "display_name": 'Configure and manage search Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to configure and manage search from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-configure-and-manage-search',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-configure-and-manage-search',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a527140413121df5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-search'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-configure-and-manage-search', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureConfigureAndManageSearch(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConfigureAndManageSearch'
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
    print(ConfigureConfigureAndManageSearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
