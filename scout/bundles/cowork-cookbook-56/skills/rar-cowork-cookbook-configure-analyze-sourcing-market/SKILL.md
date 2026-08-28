---
name: "rar-cowork-cookbook-configure-analyze-sourcing-market"
description: "Applies a bulk configuration change to analyze sourcing market from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_sourcing_market", "rar_sha256": "acf25fd6c825035dd577f572fce9f0b1511fdc62cf739e2495b2da31e7515e7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_sourcing_market_agent.py` and embedded as the fenced Python below (sha256 acf25fd6c825035d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_sourcing_market_agent.py` first:

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
    "version": '2.0.0',
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
