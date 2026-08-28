---
name: "rar-cowork-cookbook-teams-update-conduct-post-sale-follow-up"
description: "Drafts a Teams channel post on conduct post-sale follow-up status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_post_sale_follow_up", "rar_sha256": "82847dfe118fa8be39a595f75064956dfd9ea45e4944bdc5bba866acdb108513", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_post_sale_follow_up`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_post_sale_follow_up_agent.py` and in the RCI capsule.

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

Conduct post-sale follow-up Teams Channel Update — Drafts a Teams channel post on conduct post-sale follow-up status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_post_sale_follow_up_agent.py` and embedded as the fenced Python below (sha256 82847dfe118fa8be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_post_sale_follow_up_agent.py` first:

```bash
python3 teams_update_conduct_post_sale_follow_up_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_post_sale_follow_up_agent.py   # or on stdin
python3 teams_update_conduct_post_sale_follow_up_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct post-sale follow-up Teams Channel Update — Drafts a Teams channel post on conduct post-sale follow-up status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_post_sale_follow_up',
    "version": '2.0.1',
    "display_name": 'Conduct post-sale follow-up Teams Channel Update',
    "description": 'Drafts a Teams channel post on conduct post-sale follow-up status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-conduct-post-sale-follow-up',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-post-sale-follow-up',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ad8948a4c383e7a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/teams-update-conduct-post-sale-follow-up', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateConductPostSaleFollowUp(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductPostSaleFollowUp'
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
    print(TeamsUpdateConductPostSaleFollowUp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
