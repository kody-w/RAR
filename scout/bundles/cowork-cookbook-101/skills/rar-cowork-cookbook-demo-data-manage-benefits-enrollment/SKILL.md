---
name: "rar-cowork-cookbook-demo-data-manage-benefits-enrollment"
description: "Generates and creates realistic demo records for manage benefits enrollment in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_benefits_enrollment", "rar_sha256": "d4a6a2419730674efc60e9ef8338576651cc816e4416fba8149b013819e8c623", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_benefits_enrollment`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_benefits_enrollment_agent.py` and in the RCI capsule.

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
