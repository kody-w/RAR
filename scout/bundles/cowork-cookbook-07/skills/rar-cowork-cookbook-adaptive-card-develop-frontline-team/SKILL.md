---
name: "rar-cowork-cookbook-adaptive-card-develop-frontline-team"
description: "Produces a reusable Adaptive Card JSON snapshot of develop frontline team status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_frontline_team", "rar_sha256": "8c4ce85e727206ea276897373f7597d4d6b7a8bc7f4aebc7b4699ce461b9f52a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_frontline_team`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_frontline_team_agent.py` and in the RCI capsule.

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

Develop frontline team Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop frontline team status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_frontline_team_agent.py` and embedded as the fenced Python below (sha256 8c4ce85e727206ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_frontline_team_agent.py` first:

```bash
python3 adaptive_card_develop_frontline_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_frontline_team_agent.py   # or on stdin
python3 adaptive_card_develop_frontline_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop frontline team Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop frontline team status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_frontline_team',
    "version": '2.0.1',
    "display_name": 'Develop frontline team Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop frontline team status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-frontline-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58c3e36e74142fb2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-frontline-team'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-develop-frontline-team', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopFrontlineTeam(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopFrontlineTeam'
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
    print(AdaptiveCardDevelopFrontlineTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
