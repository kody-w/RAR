---
name: "rar-cowork-cookbook-demo-data-establish-compliance-policies-and-procedures"
description: "Generates and creates realistic demo records for establish compliance policies and procedures in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures", "rar_sha256": "93fc5828b3755da1a6680730ae27824f8b20cfa5945d1308bf0bcba142a9b41a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_establish_compliance_policies_and_procedures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-establish-compliance-policies-and-procedures:439507d2f7652a517f95b138f579dd6abc99b58ac522817e56c88d43c63c41d7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_establish_compliance_policies_and_procedures_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_establish_compliance_policies_and_procedures_agent.py` and embedded as the fenced Python below (sha256 93fc5828b3755da1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_establish_compliance_policies_and_procedures_agent.py` first:

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
    "version": '2.0.0',
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
