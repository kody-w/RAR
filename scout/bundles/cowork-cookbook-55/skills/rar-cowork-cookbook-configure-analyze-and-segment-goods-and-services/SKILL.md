---
name: "rar-cowork-cookbook-configure-analyze-and-segment-goods-and-services"
description: "Applies a bulk configuration change to analyze and segment goods and services from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_and_segment_goods_and_services", "rar_sha256": "2db35405ad63adc4afd288c06d9968b835d17405efbd4d6db589489379044435", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_and_segment_goods_and_services`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_and_segment_goods_and_services_agent.py` and in the RCI capsule.

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

Analyze and segment goods and services Configuration Bulk Setup — Applies a bulk configuration change to analyze and segment goods and services from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-and-segment-goods-and-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_and_segment_goods_and_services_agent.py` and embedded as the fenced Python below (sha256 2db35405ad63adc4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_and_segment_goods_and_services_agent.py` first:

```bash
python3 configure_analyze_and_segment_goods_and_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_and_segment_goods_and_services_agent.py   # or on stdin
python3 configure_analyze_and_segment_goods_and_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and segment goods and services Configuration Bulk Setup — Applies a bulk configuration change to analyze and segment goods and services from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-and-segment-goods-and-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_and_segment_goods_and_services',
    "version": '2.0.1',
    "display_name": 'Analyze and segment goods and services Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze and segment goods and services from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-and-segment-goods-and-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-and-segment-goods-and-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e433b724985b2148',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/analyze-and-segment-goods-and-services'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-analyze-and-segment-goods-and-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeAndSegmentGoodsAndServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeAndSegmentGoodsAndServices'
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
    print(ConfigureAnalyzeAndSegmentGoodsAndServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
