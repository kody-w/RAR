---
name: "rar-cowork-cookbook-adaptive-card-implement-project-governance-approach"
description: "Produces a reusable Adaptive Card JSON snapshot of implement project governance approach status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_implement_project_governance_approach", "rar_sha256": "aadca1df9e62ed204be9cb0922dc31b06bde275d71e479a3e607b34222b5c243", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_implement_project_governance_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-implement-project-governance-approach:867aa861ec92bfa446acdd353efbdcc241d2309b921815f45ade62a4f282bedd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_implement_project_governance_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_implement_project_governance_approach_agent.py` is
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

Implement project governance approach Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of implement project governance approach status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-implement-project-governance-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_implement_project_governance_approach_agent.py` and embedded as the fenced Python below (sha256 aadca1df9e62ed20…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_implement_project_governance_approach_agent.py` first:

```bash
python3 adaptive_card_implement_project_governance_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_implement_project_governance_approach_agent.py   # or on stdin
python3 adaptive_card_implement_project_governance_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement project governance approach Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of implement project governance approach status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-implement-project-governance-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_implement_project_governance_approach',
    "version": '2.0.0',
    "display_name": 'Implement project governance approach Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of implement project governance approach status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-implement-project-governance-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-implement-project-governance-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cddd364a41a228c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-project-governance-approach'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-implement-project-governance-approach', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardImplementProjectGovernanceApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardImplementProjectGovernanceApproach'
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
    print(AdaptiveCardImplementProjectGovernanceApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
