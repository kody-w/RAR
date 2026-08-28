---
name: "rar-cowork-cookbook-configure-analyze-service-profitability"
description: "Applies a bulk configuration change to analyze service profitability from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_service_profitability", "rar_sha256": "9df6273d070064b8be372d5f12eec85d23175ca34b6b88f4e8d7a719eb001b37", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_service_profitability`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_service_profitability_agent.py` and in the RCI capsule.

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

Analyze service profitability Configuration Bulk Setup — Applies a bulk configuration change to analyze service profitability from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-service-profitability
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_service_profitability_agent.py` and embedded as the fenced Python below (sha256 9df6273d070064b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_service_profitability_agent.py` first:

```bash
python3 configure_analyze_service_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_service_profitability_agent.py   # or on stdin
python3 configure_analyze_service_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze service profitability Configuration Bulk Setup — Applies a bulk configuration change to analyze service profitability from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-service-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_service_profitability',
    "version": '2.0.1',
    "display_name": 'Analyze service profitability Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze service profitability from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-service-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-service-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a87566e086587ccd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/analyze-service-profitability'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-analyze-service-profitability', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeServiceProfitability(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeServiceProfitability'
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
    print(ConfigureAnalyzeServiceProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
