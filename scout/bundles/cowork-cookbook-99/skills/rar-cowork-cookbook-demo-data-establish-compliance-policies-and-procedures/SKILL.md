---
name: "rar-cowork-cookbook-demo-data-establish-compliance-policies-and-procedures"
description: "Generates and creates realistic demo records for establish compliance policies and procedures in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures", "rar_sha256": "4520ad7acefa262bee4d58bda76611579aa1e40e35517db988d205bc2afd357b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures`. The original RAPP
agent is preserved byte-for-byte in `demo_data_establish_compliance_policies_and_procedures_agent.py` and in the RCI capsule.

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

Establish compliance policies and procedures Demo Data Generator — Generates and creates realistic demo records for establish compliance policies and procedures in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-establish-compliance-policies-and-procedures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_establish_compliance_policies_and_procedures_agent.py` and embedded as the fenced Python below (sha256 4520ad7acefa262b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_establish_compliance_policies_and_procedures_agent.py` first:

```bash
python3 demo_data_establish_compliance_policies_and_procedures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_establish_compliance_policies_and_procedures_agent.py   # or on stdin
python3 demo_data_establish_compliance_policies_and_procedures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish compliance policies and procedures Demo Data Generator — Generates and creates realistic demo records for establish compliance policies and procedures in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-establish-compliance-policies-and-procedures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures',
    "version": '2.0.1',
    "display_name": 'Establish compliance policies and procedures Demo Data Generator',
    "description": 'Generates and creates realistic demo records for establish compliance policies and procedures in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-establish-compliance-policies-and-procedures',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-establish-compliance-policies-and-procedures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9805adacacd0a624',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/establish-compliance-policies-and-procedures'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-establish-compliance-policies-and-procedures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataEstablishCompliancePoliciesAndProcedures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataEstablishCompliancePoliciesAndProcedures'
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
    print(DemoDataEstablishCompliancePoliciesAndProcedures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
