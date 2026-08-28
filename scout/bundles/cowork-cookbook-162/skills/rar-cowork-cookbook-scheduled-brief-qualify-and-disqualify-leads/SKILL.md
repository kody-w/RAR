---
name: "rar-cowork-cookbook-scheduled-brief-qualify-and-disqualify-leads"
description: "Schedulable morning-brief email summarizing qualify and disqualify leads for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_qualify_and_disqualify_leads", "rar_sha256": "1924b8c6d688ca90706b35f5122901ff4cc950d7ad341d3bbaa86a10ccbfecf2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_qualify_and_disqualify_leads`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_qualify_and_disqualify_leads_agent.py` and in the RCI capsule.

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

Qualify and disqualify leads Scheduled Email Brief — Schedulable morning-brief email summarizing qualify and disqualify leads for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-qualify-and-disqualify-leads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_qualify_and_disqualify_leads_agent.py` and embedded as the fenced Python below (sha256 1924b8c6d688ca90…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_qualify_and_disqualify_leads_agent.py` first:

```bash
python3 scheduled_brief_qualify_and_disqualify_leads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_qualify_and_disqualify_leads_agent.py   # or on stdin
python3 scheduled_brief_qualify_and_disqualify_leads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Qualify and disqualify leads Scheduled Email Brief — Schedulable morning-brief email summarizing qualify and disqualify leads for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-qualify-and-disqualify-leads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_qualify_and_disqualify_leads',
    "version": '2.0.1',
    "display_name": 'Qualify and disqualify leads Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing qualify and disqualify leads for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-qualify-and-disqualify-leads',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-qualify-and-disqualify-leads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd679ddfe4ee1e94c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/qualify-and-disqualify-leads'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-qualify-and-disqualify-leads', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefQualifyAndDisqualifyLeads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefQualifyAndDisqualifyLeads'
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
    print(ScheduledBriefQualifyAndDisqualifyLeads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
