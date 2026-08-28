---
name: "rar-cowork-cookbook-configure-analyze-and-segment-goods-and-services"
description: "Applies a bulk configuration change to analyze and segment goods and services from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_and_segment_goods_and_services", "rar_sha256": "52b85d1af95a4fff44fe2b7276691645a139fc9a1123dff49a26016cb17af88b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_and_segment_goods_and_services_agent.py` and embedded as the fenced Python below (sha256 52b85d1af95a4fff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_and_segment_goods_and_services_agent.py` first:

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
    "version": '2.0.0',
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
