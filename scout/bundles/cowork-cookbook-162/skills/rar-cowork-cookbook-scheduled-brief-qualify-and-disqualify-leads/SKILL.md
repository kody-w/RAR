---
name: "rar-cowork-cookbook-scheduled-brief-qualify-and-disqualify-leads"
description: "Schedulable morning-brief email summarizing qualify and disqualify leads for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_qualify_and_disqualify_leads", "rar_sha256": "d054f90cd503546e023f9a3a2b2daf5a70775401afc44fde1629b68f51b0ca3b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_qualify_and_disqualify_leads_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-qualify-and-disqualify-leads:aad7f0ea32cc15909f9571f1d758c24258b188c778d87fa5244dac7061db41db", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_qualify_and_disqualify_leads`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_qualify_and_disqualify_leads_agent.py` is
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
