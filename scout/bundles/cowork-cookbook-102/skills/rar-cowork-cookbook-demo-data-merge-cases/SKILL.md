---
name: "rar-cowork-cookbook-demo-data-merge-cases"
description: "Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_merge_cases", "rar_sha256": "ecf7f76578d245210568234cbc781874d0cec8bfd833bf0a5406db3d885b607d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_merge_cases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-merge-cases:959e5b8173778fb22b12de297cd0db83e86c09837ac6817b1dab6e5c7bb07540", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_merge_cases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_merge_cases_agent.py` is
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

Merge cases Demo Data Generator — Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-merge-cases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_merge_cases_agent.py` and embedded as the fenced Python below (sha256 ecf7f76578d24521…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_merge_cases_agent.py` first:

```bash
python3 demo_data_merge_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_merge_cases_agent.py   # or on stdin
python3 demo_data_merge_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Merge cases Demo Data Generator — Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-merge-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_merge_cases',
    "version": '2.0.0',
    "display_name": 'Merge cases Demo Data Generator',
    "description": 'Generates and creates realistic demo records for merge cases in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-merge-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-merge-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '23620edfb71957ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/merge-cases'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-merge-cases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataMergeCases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMergeCases'
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
    print(DemoDataMergeCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
