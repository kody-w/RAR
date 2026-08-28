---
name: "rar-cowork-cookbook-scheduled-brief-qualify-and-disqualify-leads"
description: "Schedulable morning-brief email summarizing qualify and disqualify leads for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_qualify_and_disqualify_leads", "rar_sha256": "d054f90cd503546e023f9a3a2b2daf5a70775401afc44fde1629b68f51b0ca3b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_qualify_and_disqualify_leads_agent.py` and embedded as the fenced Python below (sha256 d054f90cd503546e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_qualify_and_disqualify_leads_agent.py` first:

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
    "version": '2.0.0',
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
