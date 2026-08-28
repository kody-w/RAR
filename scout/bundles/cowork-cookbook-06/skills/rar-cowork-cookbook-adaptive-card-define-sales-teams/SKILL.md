---
name: "rar-cowork-cookbook-adaptive-card-define-sales-teams"
description: "Produces a reusable Adaptive Card JSON snapshot of define sales teams status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_sales_teams", "rar_sha256": "cdaa7b9c62d9ff8c8b5b09f050d0b6cfb28258651dcfeac33b3ceac789c0c57d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_sales_teams`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_sales_teams_agent.py` and in the RCI capsule.

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

Define sales teams Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define sales teams status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_sales_teams_agent.py` and embedded as the fenced Python below (sha256 cdaa7b9c62d9ff8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_sales_teams_agent.py` first:

```bash
python3 adaptive_card_define_sales_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_sales_teams_agent.py   # or on stdin
python3 adaptive_card_define_sales_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales teams Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define sales teams status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_sales_teams',
    "version": '2.0.0',
    "display_name": 'Define sales teams Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define sales teams status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-sales-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27763364487f6cd0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-teams'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-define-sales-teams', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDefineSalesTeams(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineSalesTeams'
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
    print(AdaptiveCardDefineSalesTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
