---
name: "rar-cowork-cookbook-configure-analyze-revenue"
description: "Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_revenue", "rar_sha256": "44363dc84157ead4f9dbe743e471f7047d7fdc65e347d762a2fae2fa799ce18a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_revenue`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_revenue_agent.py` and in the RCI capsule.

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

Analyze revenue Configuration Bulk Setup — Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_revenue_agent.py` and embedded as the fenced Python below (sha256 44363dc84157ead4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_revenue_agent.py` first:

```bash
python3 configure_analyze_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_revenue_agent.py   # or on stdin
python3 configure_analyze_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze revenue Configuration Bulk Setup — Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_revenue',
    "version": '2.0.0',
    "display_name": 'Analyze revenue Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze revenue from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-analyze-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a96a08469286bf6d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-revenue'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-analyze-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeRevenue'
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
    print(ConfigureAnalyzeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
