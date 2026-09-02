---
name: "rar-cowork-cookbook-demo-data-analyze-worker-performance"
description: "Generates and creates realistic demo records for analyze worker performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_worker_performance", "rar_sha256": "15ed8e81b33bcaceae0b7421be1052f57defcfd9ed752649b9e9f3caa5306125", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_analyze_worker_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-analyze-worker-performance:7953b6f34f9bb96fc92d168f35f52a16d8b96924eb939733f36d7f63588ba1e2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_analyze_worker_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_analyze_worker_performance_agent.py` is
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
