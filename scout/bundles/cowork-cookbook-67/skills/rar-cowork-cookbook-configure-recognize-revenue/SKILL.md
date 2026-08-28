---
name: "rar-cowork-cookbook-configure-recognize-revenue"
description: "Applies a bulk configuration change to recognize revenue from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_recognize_revenue", "rar_sha256": "aa48c8bec88ce7d7c889667e7b41e930347743047700078e55f1019c5eca818e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_recognize_revenue`. The original RAPP
agent is preserved byte-for-byte in `configure_recognize_revenue_agent.py` and in the RCI capsule.

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

Recognize revenue Configuration Bulk Setup — Applies a bulk configuration change to recognize revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_recognize_revenue_agent.py` and embedded as the fenced Python below (sha256 aa48c8bec88ce7d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_recognize_revenue_agent.py` first:

```bash
python3 configure_recognize_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_recognize_revenue_agent.py   # or on stdin
python3 configure_recognize_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize revenue Configuration Bulk Setup — Applies a bulk configuration change to recognize revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_recognize_revenue',
    "version": '2.0.1',
    "display_name": 'Recognize revenue Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to recognize revenue from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-recognize-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-recognize-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1d9e500aa7ba0505',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/recognize-revenue'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-recognize-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureRecognizeRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRecognizeRevenue'
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
    print(ConfigureRecognizeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
