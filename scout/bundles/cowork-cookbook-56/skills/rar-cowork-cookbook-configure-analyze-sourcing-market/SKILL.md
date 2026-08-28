---
name: "rar-cowork-cookbook-configure-analyze-sourcing-market"
description: "Applies a bulk configuration change to analyze sourcing market from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_sourcing_market", "rar_sha256": "32bbfe754ea556fc96b4db1b3e5c887018d5dcdaef77c62bfc84c975db3d1a10", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_sourcing_market`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_sourcing_market_agent.py` and in the RCI capsule.

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

Analyze sourcing market Configuration Bulk Setup — Applies a bulk configuration change to analyze sourcing market from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-sourcing-market
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_sourcing_market_agent.py` and embedded as the fenced Python below (sha256 32bbfe754ea556fc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_sourcing_market_agent.py` first:

```bash
python3 configure_analyze_sourcing_market_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_sourcing_market_agent.py   # or on stdin
python3 configure_analyze_sourcing_market_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing market Configuration Bulk Setup — Applies a bulk configuration change to analyze sourcing market from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-sourcing-market
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_sourcing_market',
    "version": '2.0.1',
    "display_name": 'Analyze sourcing market Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze sourcing market from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-analyze-sourcing-market',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-sourcing-market',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9cda691b2232747e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/analyze-sourcing-market'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-sourcing-market', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeSourcingMarket(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeSourcingMarket'
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
    print(ConfigureAnalyzeSourcingMarket().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
