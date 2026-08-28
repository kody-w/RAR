---
name: "rar-cowork-cookbook-teams-update-conduct-post-sale-follow-up"
description: "Drafts a Teams channel post on conduct post-sale follow-up status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_post_sale_follow_up", "rar_sha256": "a0273dd361aaf2edcec3e669f2b9cc3795c8a15f77e6272f7aa546d293e47948", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_post_sale_follow_up_agent.py` and embedded as the fenced Python below (sha256 a0273dd361aaf2ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_post_sale_follow_up_agent.py` first:

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
    "version": '2.0.0',
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
