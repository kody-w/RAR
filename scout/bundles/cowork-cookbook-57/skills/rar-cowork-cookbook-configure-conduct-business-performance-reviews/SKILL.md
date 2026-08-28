---
name: "rar-cowork-cookbook-configure-conduct-business-performance-reviews"
description: "Applies a bulk configuration change to conduct business performance reviews from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_conduct_business_performance_reviews", "rar_sha256": "bfcebd5a523e26259969a0b6594f838ec5c2c5dfdc35d7eb02e20f3bdc5d77d8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_conduct_business_performance_reviews_agent.py` and embedded as the fenced Python below (sha256 bfcebd5a523e2625…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_conduct_business_performance_reviews_agent.py` first:

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
    "version": '2.0.0',
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
