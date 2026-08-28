---
name: "rar-cowork-cookbook-configure-analyze-product-quality-data"
description: "Applies a bulk configuration change to analyze product quality data from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_product_quality_data", "rar_sha256": "334553a61d8cd5d1f767d11f6b47986eec494e0fb7c5cda027db3275820aa29e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_product_quality_data`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_product_quality_data_agent.py` and in the RCI capsule.

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

Analyze product quality data Configuration Bulk Setup — Applies a bulk configuration change to analyze product quality data from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-product-quality-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_product_quality_data_agent.py` and embedded as the fenced Python below (sha256 334553a61d8cd5d1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_product_quality_data_agent.py` first:

```bash
python3 configure_analyze_product_quality_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_product_quality_data_agent.py   # or on stdin
python3 configure_analyze_product_quality_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product quality data Configuration Bulk Setup — Applies a bulk configuration change to analyze product quality data from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-product-quality-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_product_quality_data',
    "version": '2.0.0',
    "display_name": 'Analyze product quality data Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze product quality data from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-product-quality-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-product-quality-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2470117fb16a38e1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-quality-data'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-analyze-product-quality-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeProductQualityData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeProductQualityData'
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
    print(ConfigureAnalyzeProductQualityData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
