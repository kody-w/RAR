---
name: "rar-cowork-cookbook-demo-data-onboard-new-employees"
description: "Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_onboard_new_employees", "rar_sha256": "404193e6b7c80654ca96b20fa3478d834a604e6b9e45ca3120a55ec7fe67b401", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_onboard_new_employees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-onboard-new-employees:f0520a7a88c0958b038b26381115a93ecdae0c4dd9d9f65da22dad09579ae356", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_onboard_new_employees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_onboard_new_employees_agent.py` is
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

Onboard new employees Demo Data Generator — Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-onboard-new-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_onboard_new_employees_agent.py` and embedded as the fenced Python below (sha256 404193e6b7c80654…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_onboard_new_employees_agent.py` first:

```bash
python3 demo_data_onboard_new_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_onboard_new_employees_agent.py   # or on stdin
python3 demo_data_onboard_new_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new employees Demo Data Generator — Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-onboard-new-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_onboard_new_employees',
    "version": '2.0.0',
    "display_name": 'Onboard new employees Demo Data Generator',
    "description": 'Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-onboard-new-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-onboard-new-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0263795c7214d6a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-employees'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-onboard-new-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataOnboardNewEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataOnboardNewEmployees'
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
    print(DemoDataOnboardNewEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
