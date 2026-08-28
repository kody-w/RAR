---
name: "rar-cowork-cookbook-demo-data-manage-benefits-enrollment"
description: "Generates and creates realistic demo records for manage benefits enrollment in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_benefits_enrollment", "rar_sha256": "b75421c7da2d11546bdbb71e205e4601ef288ee350aa9863ea93c3d9f3875e21", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_benefits_enrollment_agent.py` and embedded as the fenced Python below (sha256 b75421c7da2d1154…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_benefits_enrollment_agent.py` first:

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
    "version": '2.0.1',
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
