---
name: "rar-cowork-cookbook-demo-data-optimize-service-performance"
description: "Generates and creates realistic demo records for optimize service performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_optimize_service_performance", "rar_sha256": "410539822055de7bb6b96843276fc9ca552ce02c92e1059b055116acbb62f2aa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_optimize_service_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-optimize-service-performance:9b3e30608151a5a4dffd294a3b1b443215da630d0348e15c3aa1a997cfa5f604", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_optimize_service_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_optimize_service_performance_agent.py` is
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

Optimize service performance Demo Data Generator — Generates and creates realistic demo records for optimize service performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-optimize-service-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_optimize_service_performance_agent.py` and embedded as the fenced Python below (sha256 410539822055de7b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_optimize_service_performance_agent.py` first:

```bash
python3 demo_data_optimize_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_optimize_service_performance_agent.py   # or on stdin
python3 demo_data_optimize_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Optimize service performance Demo Data Generator — Generates and creates realistic demo records for optimize service performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-optimize-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_optimize_service_performance',
    "version": '2.0.0',
    "display_name": 'Optimize service performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for optimize service performance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-optimize-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-optimize-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d0d80106334bddb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/optimize-service-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-optimize-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataOptimizeServicePerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataOptimizeServicePerformance'
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
    print(DemoDataOptimizeServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
