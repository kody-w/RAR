---
name: "rar-cowork-cookbook-adaptive-card-implement-project-governance-approach"
description: "Produces a reusable Adaptive Card JSON snapshot of implement project governance approach status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_implement_project_governance_approach", "rar_sha256": "bb170c7a1c9d72b154ce7688b4e84cd964d1391f1e68e06796547e83c63f4094", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_implement_project_governance_approach_agent.py` and embedded as the fenced Python below (sha256 bb170c7a1c9d72b1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_implement_project_governance_approach_agent.py` first:

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
    "version": '2.0.1',
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
