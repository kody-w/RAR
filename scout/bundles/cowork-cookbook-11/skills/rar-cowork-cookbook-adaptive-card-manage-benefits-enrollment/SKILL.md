---
name: "rar-cowork-cookbook-adaptive-card-manage-benefits-enrollment"
description: "Produces a reusable Adaptive Card JSON snapshot of manage benefits enrollment status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_benefits_enrollment", "rar_sha256": "01b818cd530ae636f3747588af46f9a64a1234a6ec15fd77901237b352c0181a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_benefits_enrollment_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-benefits-enrollment:11dd586e2e38c2b6fe2044f2d2409f116d8543013a3fce16d78bc351f92a2953", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_benefits_enrollment`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_benefits_enrollment_agent.py` is
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
