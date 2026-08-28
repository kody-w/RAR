---
name: "rar-cowork-cookbook-adaptive-card-manage-benefits-enrollment"
description: "Produces a reusable Adaptive Card JSON snapshot of manage benefits enrollment status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_benefits_enrollment", "rar_sha256": "a223d0d36e3b966624eb53ce99a13a8c99c5d69275fd0714f93687a7974b22ea", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_benefits_enrollment_agent.py` and embedded as the fenced Python below (sha256 a223d0d36e3b9666…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_benefits_enrollment_agent.py` first:

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
    "version": '2.0.1',
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
