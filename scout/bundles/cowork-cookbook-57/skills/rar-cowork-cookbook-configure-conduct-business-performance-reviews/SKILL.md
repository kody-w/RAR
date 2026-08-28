---
name: "rar-cowork-cookbook-configure-conduct-business-performance-reviews"
description: "Applies a bulk configuration change to conduct business performance reviews from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_conduct_business_performance_reviews", "rar_sha256": "8d0a3ee01047558abf1711cfb4e92c63d7587b3567ab56656dbfa65224545a0b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_conduct_business_performance_reviews`. The original RAPP
agent is preserved byte-for-byte in `configure_conduct_business_performance_reviews_agent.py` and in the RCI capsule.

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

Conduct business performance reviews Configuration Bulk Setup — Applies a bulk configuration change to conduct business performance reviews from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-conduct-business-performance-reviews
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_conduct_business_performance_reviews_agent.py` and embedded as the fenced Python below (sha256 8d0a3ee01047558a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_conduct_business_performance_reviews_agent.py` first:

```bash
python3 configure_conduct_business_performance_reviews_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_conduct_business_performance_reviews_agent.py   # or on stdin
python3 configure_conduct_business_performance_reviews_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct business performance reviews Configuration Bulk Setup — Applies a bulk configuration change to conduct business performance reviews from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-conduct-business-performance-reviews
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_conduct_business_performance_reviews',
    "version": '2.0.1',
    "display_name": 'Conduct business performance reviews Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to conduct business performance reviews from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-conduct-business-performance-reviews',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-conduct-business-performance-reviews',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8449dfdda2458567',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/conduct-business-performance-reviews'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-conduct-business-performance-reviews', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureConductBusinessPerformanceReviews(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConductBusinessPerformanceReviews'
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
    print(ConfigureConductBusinessPerformanceReviews().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
