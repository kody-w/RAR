---
name: "rar-cowork-cookbook-scheduled-brief-conduct-post-sale-follow-up"
description: "Schedulable morning-brief email summarizing conduct post-sale follow-up for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up", "rar_sha256": "7466e508077be2e328998c793196fff8c6516b0ad30a190f57ae490bd0c32297", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_post_sale_follow_up_agent.py` and embedded as the fenced Python below (sha256 7466e508077be2e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_post_sale_follow_up_agent.py` first:

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
    "version": '2.0.0',
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
