---
name: "rar-cowork-cookbook-adaptive-card-optimize-service-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of optimize service performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_optimize_service_performance", "rar_sha256": "f740e92c770489aa642ba4923bb338eb0dd16a33d3daa85a032f0e99913415b8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_optimize_service_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-optimize-service-performance:b546d5b078230f605266a8492c3210a8fe74e69dbc972bd4d008a58fadd6dfcc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_optimize_service_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_optimize_service_performance_agent.py` is
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

Optimize service performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of optimize service performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-optimize-service-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_optimize_service_performance_agent.py` and embedded as the fenced Python below (sha256 f740e92c770489aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_optimize_service_performance_agent.py` first:

```bash
python3 adaptive_card_optimize_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_optimize_service_performance_agent.py   # or on stdin
python3 adaptive_card_optimize_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Optimize service performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of optimize service performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-optimize-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_optimize_service_performance',
    "version": '2.0.0',
    "display_name": 'Optimize service performance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of optimize service performance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-optimize-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-optimize-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c2a33be94c80b864',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/optimize-service-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-optimize-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardOptimizeServicePerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardOptimizeServicePerformance'
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
    print(AdaptiveCardOptimizeServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
