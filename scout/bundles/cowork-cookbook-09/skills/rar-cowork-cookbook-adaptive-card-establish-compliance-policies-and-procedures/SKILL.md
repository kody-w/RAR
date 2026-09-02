---
name: "rar-cowork-cookbook-adaptive-card-establish-compliance-policies-and-procedures"
description: "Produces a reusable Adaptive Card JSON snapshot of establish compliance policies and procedures status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures", "rar_sha256": "fd55041fb2a3c038fddde0fd3773dc5eb1d2169da9b3bab66d07185055e082da", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_establish_compliance_policies_and_procedures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-establish-compliance-policies-and-procedures:d3d3a7264877f99d8f27780162d1d3758e21ec9f61ac9b18d631e010c9191f61", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_establish_compliance_policies_and_procedures_agent.py` is
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

Establish compliance policies and procedures Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of establish compliance policies and procedures status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-compliance-policies-and-procedures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_establish_compliance_policies_and_procedures_agent.py` and embedded as the fenced Python below (sha256 fd55041fb2a3c038…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_establish_compliance_policies_and_procedures_agent.py` first:

```bash
python3 adaptive_card_establish_compliance_policies_and_procedures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_establish_compliance_policies_and_procedures_agent.py   # or on stdin
python3 adaptive_card_establish_compliance_policies_and_procedures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish compliance policies and procedures Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of establish compliance policies and procedures status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-compliance-policies-and-procedures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures',
    "version": '2.0.0',
    "display_name": 'Establish compliance policies and procedures Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of establish compliance policies and procedures status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-establish-compliance-policies-and-procedures',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-establish-compliance-policies-and-procedures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c706cff438bffed1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/establish-compliance-policies-and-procedures'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-establish-compliance-policies-and-procedures', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardEstablishCompliancePoliciesAndProcedures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEstablishCompliancePoliciesAndProcedures'
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
    print(AdaptiveCardEstablishCompliancePoliciesAndProcedures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
