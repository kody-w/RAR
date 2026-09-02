---
name: "rar-cowork-cookbook-demo-data-terminate-workers"
description: "Generates and creates realistic demo records for terminate workers in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_terminate_workers", "rar_sha256": "24fc672875e5edbd79108e29153fe37e2c5ccee50c1b9d37d0732c7d791d4a91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_terminate_workers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-terminate-workers:618084e7f32f2cd7648be63dec1167fac45470e44a9ab78d9bd85745b8b0e815", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_terminate_workers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_terminate_workers_agent.py` is
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

Terminate workers Demo Data Generator — Generates and creates realistic demo records for terminate workers in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-terminate-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_terminate_workers_agent.py` and embedded as the fenced Python below (sha256 24fc672875e5edbd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_terminate_workers_agent.py` first:

```bash
python3 demo_data_terminate_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_terminate_workers_agent.py   # or on stdin
python3 demo_data_terminate_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Terminate workers Demo Data Generator — Generates and creates realistic demo records for terminate workers in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-terminate-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_terminate_workers',
    "version": '2.0.0',
    "display_name": 'Terminate workers Demo Data Generator',
    "description": 'Generates and creates realistic demo records for terminate workers in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-terminate-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-terminate-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4396caa24bff6eab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/terminate-workers'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-terminate-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataTerminateWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTerminateWorkers'
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
    print(DemoDataTerminateWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
