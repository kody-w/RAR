---
name: "rar-cowork-cookbook-demo-data-analyze-worker-performance"
description: "Generates and creates realistic demo records for analyze worker performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_worker_performance", "rar_sha256": "15ed8e81b33bcaceae0b7421be1052f57defcfd9ed752649b9e9f3caa5306125", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_worker_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_worker_performance_agent.py` and in the RCI capsule.

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

Analyze worker performance Demo Data Generator — Generates and creates realistic demo records for analyze worker performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-worker-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_worker_performance_agent.py` and embedded as the fenced Python below (sha256 15ed8e81b33bcace…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_worker_performance_agent.py` first:

```bash
python3 demo_data_analyze_worker_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_worker_performance_agent.py   # or on stdin
python3 demo_data_analyze_worker_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze worker performance Demo Data Generator — Generates and creates realistic demo records for analyze worker performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-worker-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_worker_performance',
    "version": '2.0.0',
    "display_name": 'Analyze worker performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze worker performance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-worker-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-worker-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fe9ace6054e97814',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-worker-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-analyze-worker-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAnalyzeWorkerPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeWorkerPerformance'
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
    print(DemoDataAnalyzeWorkerPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
