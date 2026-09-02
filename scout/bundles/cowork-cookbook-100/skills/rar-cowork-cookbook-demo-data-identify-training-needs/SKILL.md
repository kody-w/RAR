---
name: "rar-cowork-cookbook-demo-data-identify-training-needs"
description: "Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_identify_training_needs", "rar_sha256": "52ebcd10aff3e1da542739856f9bb9ba9b1d6c7eb446e586548b5f07bac735a4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_identify_training_needs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-identify-training-needs:97f776d3afb62ef3da7440973e96000dd919ae81738d82c6782e420f4dc4a978", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_identify_training_needs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_identify_training_needs_agent.py` is
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

Identify training needs Demo Data Generator — Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-identify-training-needs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_identify_training_needs_agent.py` and embedded as the fenced Python below (sha256 52ebcd10aff3e1da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_identify_training_needs_agent.py` first:

```bash
python3 demo_data_identify_training_needs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_identify_training_needs_agent.py   # or on stdin
python3 demo_data_identify_training_needs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify training needs Demo Data Generator — Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-identify-training-needs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_identify_training_needs',
    "version": '2.0.0',
    "display_name": 'Identify training needs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-identify-training-needs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-identify-training-needs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9686183a09c31980',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/identify-training-needs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-identify-training-needs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataIdentifyTrainingNeeds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataIdentifyTrainingNeeds'
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
    print(DemoDataIdentifyTrainingNeeds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
