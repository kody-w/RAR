---
name: "rar-cowork-cookbook-demo-data-manage-benefits-enrollment"
description: "Generates and creates realistic demo records for manage benefits enrollment in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_benefits_enrollment", "rar_sha256": "d4a6a2419730674efc60e9ef8338576651cc816e4416fba8149b013819e8c623", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_benefits_enrollment_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-benefits-enrollment:cab5b595ff7591e47a4b8f609bda0bb6ab04ac4528d5cdae473cdc957575e130", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_benefits_enrollment`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_benefits_enrollment_agent.py` is
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

Manage benefits enrollment Demo Data Generator — Generates and creates realistic demo records for manage benefits enrollment in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-benefits-enrollment
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_benefits_enrollment_agent.py` and embedded as the fenced Python below (sha256 d4a6a2419730674e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_benefits_enrollment_agent.py` first:

```bash
python3 demo_data_manage_benefits_enrollment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_benefits_enrollment_agent.py   # or on stdin
python3 demo_data_manage_benefits_enrollment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage benefits enrollment Demo Data Generator — Generates and creates realistic demo records for manage benefits enrollment in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-benefits-enrollment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_benefits_enrollment',
    "version": '2.0.0',
    "display_name": 'Manage benefits enrollment Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage benefits enrollment in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-benefits-enrollment',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-benefits-enrollment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d64d513b2325d1f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-benefits-enrollment'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-manage-benefits-enrollment', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageBenefitsEnrollment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageBenefitsEnrollment'
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
    print(DemoDataManageBenefitsEnrollment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
