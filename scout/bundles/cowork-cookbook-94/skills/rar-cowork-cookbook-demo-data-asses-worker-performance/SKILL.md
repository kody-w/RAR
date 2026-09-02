---
name: "rar-cowork-cookbook-demo-data-asses-worker-performance"
description: "Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_asses_worker_performance", "rar_sha256": "4e799db82acf71817873208220ad89b886f26221ae395494c6aa5c52fec40d11", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_asses_worker_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-asses-worker-performance:f6d31703d5110061dfb1306e24dbb69f0959c944b87e5da0495a43f0eac4da08", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_asses_worker_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_asses_worker_performance_agent.py` is
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

Asses worker performance Demo Data Generator — Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-asses-worker-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_asses_worker_performance_agent.py` and embedded as the fenced Python below (sha256 4e799db82acf7181…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_asses_worker_performance_agent.py` first:

```bash
python3 demo_data_asses_worker_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_asses_worker_performance_agent.py   # or on stdin
python3 demo_data_asses_worker_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Asses worker performance Demo Data Generator — Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-asses-worker-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_asses_worker_performance',
    "version": '2.0.0',
    "display_name": 'Asses worker performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-asses-worker-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-asses-worker-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a77e388bfc101ec1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/asses-worker-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-asses-worker-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAssesWorkerPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAssesWorkerPerformance'
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
    print(DemoDataAssesWorkerPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
