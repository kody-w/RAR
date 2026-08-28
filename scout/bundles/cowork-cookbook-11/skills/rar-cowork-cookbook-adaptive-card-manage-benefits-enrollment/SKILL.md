---
name: "rar-cowork-cookbook-adaptive-card-manage-benefits-enrollment"
description: "Produces a reusable Adaptive Card JSON snapshot of manage benefits enrollment status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_benefits_enrollment", "rar_sha256": "01b818cd530ae636f3747588af46f9a64a1234a6ec15fd77901237b352c0181a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_benefits_enrollment`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_benefits_enrollment_agent.py` and in the RCI capsule.

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

Manage benefits enrollment Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage benefits enrollment status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-benefits-enrollment
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_benefits_enrollment_agent.py` and embedded as the fenced Python below (sha256 01b818cd530ae636…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_benefits_enrollment_agent.py` first:

```bash
python3 adaptive_card_manage_benefits_enrollment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_benefits_enrollment_agent.py   # or on stdin
python3 adaptive_card_manage_benefits_enrollment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage benefits enrollment Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage benefits enrollment status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-benefits-enrollment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_benefits_enrollment',
    "version": '2.0.0',
    "display_name": 'Manage benefits enrollment Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage benefits enrollment status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-benefits-enrollment',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-benefits-enrollment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea14ec9bacd09ac8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-benefits-enrollment'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-manage-benefits-enrollment', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardManageBenefitsEnrollment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageBenefitsEnrollment'
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
    print(AdaptiveCardManageBenefitsEnrollment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
