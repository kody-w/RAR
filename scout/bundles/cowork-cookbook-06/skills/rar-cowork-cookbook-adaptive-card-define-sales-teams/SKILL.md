---
name: "rar-cowork-cookbook-adaptive-card-define-sales-teams"
description: "Produces a reusable Adaptive Card JSON snapshot of define sales teams status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_sales_teams", "rar_sha256": "cdaa7b9c62d9ff8c8b5b09f050d0b6cfb28258651dcfeac33b3ceac789c0c57d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_sales_teams_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-sales-teams:39f428b76467964f4dcab4d4bf3eb8bb4682161efcef788c6c78411112deb615", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_sales_teams`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_sales_teams_agent.py` is
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
