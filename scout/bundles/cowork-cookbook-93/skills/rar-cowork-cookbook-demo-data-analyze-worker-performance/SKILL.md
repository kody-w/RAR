---
name: "rar-cowork-cookbook-demo-data-analyze-worker-performance"
description: "Generates and creates realistic demo records for analyze worker performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_worker_performance", "rar_sha256": "0189cbb023211e4646e4cee9d39df1cdc4d7f5dcbccfa4ea98b6aefa231b9988", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_worker_performance_agent.py` and embedded as the fenced Python below (sha256 0189cbb023211e46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_worker_performance_agent.py` first:

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
    "version": '2.0.1',
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
