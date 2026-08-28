---
name: "rar-cowork-cookbook-adaptive-card-implement-project-governance-approach"
description: "Produces a reusable Adaptive Card JSON snapshot of implement project governance approach status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_implement_project_governance_approach", "rar_sha256": "aadca1df9e62ed204be9cb0922dc31b06bde275d71e479a3e607b34222b5c243", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_implement_project_governance_approach`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_implement_project_governance_approach_agent.py` and in the RCI capsule.

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
