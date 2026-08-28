---
name: "rar-cowork-cookbook-configure-analyze-service-profitability"
description: "Applies a bulk configuration change to analyze service profitability from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_service_profitability", "rar_sha256": "941f62698fa88e7d393f87ac8a217b4a55b58f6681c1cbdb46bc06a7684dcc19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_service_profitability_agent.py` and embedded as the fenced Python below (sha256 941f62698fa88e7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_service_profitability_agent.py` first:

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
    "version": '2.0.0',
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
