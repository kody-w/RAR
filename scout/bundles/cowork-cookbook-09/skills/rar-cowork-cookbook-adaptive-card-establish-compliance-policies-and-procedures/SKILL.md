---
name: "rar-cowork-cookbook-adaptive-card-establish-compliance-policies-and-procedures"
description: "Produces a reusable Adaptive Card JSON snapshot of establish compliance policies and procedures status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures", "rar_sha256": "fd55041fb2a3c038fddde0fd3773dc5eb1d2169da9b3bab66d07185055e082da", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_establish_compliance_policies_and_procedures_agent.py` and in the RCI capsule.

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
