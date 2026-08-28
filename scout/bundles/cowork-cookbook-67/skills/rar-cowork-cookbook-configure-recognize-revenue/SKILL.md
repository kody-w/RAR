---
name: "rar-cowork-cookbook-configure-recognize-revenue"
description: "Applies a bulk configuration change to recognize revenue from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_recognize_revenue", "rar_sha256": "b04cb7c51491f2e3c8ac4b01a79a18066f9381395f8d61596a7306d41573cf5b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_recognize_revenue_agent.py` and embedded as the fenced Python below (sha256 b04cb7c51491f2e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_recognize_revenue_agent.py` first:

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
    "version": '2.0.0',
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
