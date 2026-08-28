---
name: "rar-cowork-cookbook-scheduled-brief-conduct-post-sale-follow-up"
description: "Schedulable morning-brief email summarizing conduct post-sale follow-up for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up", "rar_sha256": "7bf635a36f060227ad993ead7e349236e5bee5ff1193864338ffab78bbd87a4f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_conduct_post_sale_follow_up_agent.py` and in the RCI capsule.

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

Conduct post-sale follow-up Scheduled Email Brief — Schedulable morning-brief email summarizing conduct post-sale follow-up for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-post-sale-follow-up
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_post_sale_follow_up_agent.py` and embedded as the fenced Python below (sha256 7bf635a36f060227…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_post_sale_follow_up_agent.py` first:

```bash
python3 scheduled_brief_conduct_post_sale_follow_up_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_post_sale_follow_up_agent.py   # or on stdin
python3 scheduled_brief_conduct_post_sale_follow_up_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct post-sale follow-up Scheduled Email Brief — Schedulable morning-brief email summarizing conduct post-sale follow-up for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-post-sale-follow-up
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up',
    "version": '2.0.1',
    "display_name": 'Conduct post-sale follow-up Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing conduct post-sale follow-up for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-conduct-post-sale-follow-up',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-post-sale-follow-up',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '022a9b25a213c7c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-conduct-post-sale-follow-up', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefConductPostSaleFollowUp(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductPostSaleFollowUp'
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
    print(ScheduledBriefConductPostSaleFollowUp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
