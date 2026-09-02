---
name: "rar-cowork-cookbook-configure-conduct-business-performance-reviews"
description: "Applies a bulk configuration change to conduct business performance reviews from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_conduct_business_performance_reviews", "rar_sha256": "bfcebd5a523e26259969a0b6594f838ec5c2c5dfdc35d7eb02e20f3bdc5d77d8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_conduct_business_performance_reviews_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-conduct-business-performance-reviews:3288773c34700e0869e73e5d3fc3a60107996dc79fbf9f11ac888419bb5c910b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_conduct_business_performance_reviews`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_conduct_business_performance_reviews_agent.py` is
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
