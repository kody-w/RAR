---
name: "rar-cowork-cookbook-adaptive-card-establish-compliance-policies-and-procedures"
description: "Produces a reusable Adaptive Card JSON snapshot of establish compliance policies and procedures status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures", "rar_sha256": "fea3e0589472aa0a0cae9c61a2543fc5b118a3919522a987588c59fd992eb083", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_establish_compliance_policies_and_procedures_agent.py` and embedded as the fenced Python below (sha256 fea3e0589472aa0a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_establish_compliance_policies_and_procedures_agent.py` first:

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
    "version": '2.0.1',
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
