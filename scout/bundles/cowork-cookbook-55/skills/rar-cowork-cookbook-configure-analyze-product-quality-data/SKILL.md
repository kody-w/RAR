---
name: "rar-cowork-cookbook-configure-analyze-product-quality-data"
description: "Applies a bulk configuration change to analyze product quality data from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_product_quality_data", "rar_sha256": "334553a61d8cd5d1f767d11f6b47986eec494e0fb7c5cda027db3275820aa29e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_analyze_product_quality_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-analyze-product-quality-data:75438d0c4da7ff65a61ec00c9c10368abe93a1baf3daf39751ffc0cfad03286d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_analyze_product_quality_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_analyze_product_quality_data_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
