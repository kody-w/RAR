---
name: "rar-cowork-cookbook-adaptive-card-develop-frontline-team"
description: "Produces a reusable Adaptive Card JSON snapshot of develop frontline team status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_frontline_team", "rar_sha256": "3916005c1a01dc131cbb03bfedb935e25edfd7cef9cf01d3ba8561f0ee5376dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_frontline_team_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-frontline-team:5ded57e5e8d6caae323405edd23e64ffab769e7f126bd273b6919083223a5877", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_frontline_team`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_frontline_team_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_frontline_team_agent.py` and embedded as the fenced Python below (sha256 3916005c1a01dc13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_frontline_team_agent.py` first:

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
    "version": '2.0.0',
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
