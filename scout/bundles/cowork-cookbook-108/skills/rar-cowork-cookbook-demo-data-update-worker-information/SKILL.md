---
name: "rar-cowork-cookbook-demo-data-update-worker-information"
description: "Generates and creates realistic demo records for update worker information in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_update_worker_information", "rar_sha256": "2d3874a04f372e320838b95812833da16b32b66d6244586ffbd6acdf9c5a4856", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_update_worker_information_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-update-worker-information:4d8b5c3f856791e69696351d25c1ec1c3bc6f135d446682c385038813a254593", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_update_worker_information`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_update_worker_information_agent.py` is
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

Update worker information Demo Data Generator — Generates and creates realistic demo records for update worker information in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-update-worker-information
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_update_worker_information_agent.py` and embedded as the fenced Python below (sha256 2d3874a04f372e32…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_update_worker_information_agent.py` first:

```bash
python3 demo_data_update_worker_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_update_worker_information_agent.py   # or on stdin
python3 demo_data_update_worker_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update worker information Demo Data Generator — Generates and creates realistic demo records for update worker information in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-update-worker-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_update_worker_information',
    "version": '2.0.0',
    "display_name": 'Update worker information Demo Data Generator',
    "description": 'Generates and creates realistic demo records for update worker information in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-update-worker-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-update-worker-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac1e81581db13289',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/update-worker-information'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-update-worker-information', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataUpdateWorkerInformation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataUpdateWorkerInformation'
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
    print(DemoDataUpdateWorkerInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
