---
name: "rar-cowork-cookbook-scheduled-brief-manage-opportunity-process"
description: "Schedulable morning-brief email summarizing manage opportunity process for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_opportunity_process", "rar_sha256": "c3b2013d85df5625b5e631cdcf2f575d728bf55e3084dc5feaf490ca0da313d4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_opportunity_process`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_opportunity_process_agent.py` and in the RCI capsule.

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

Manage opportunity process Scheduled Email Brief — Schedulable morning-brief email summarizing manage opportunity process for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-opportunity-process
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_opportunity_process_agent.py` and embedded as the fenced Python below (sha256 c3b2013d85df5625…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_opportunity_process_agent.py` first:

```bash
python3 scheduled_brief_manage_opportunity_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_opportunity_process_agent.py   # or on stdin
python3 scheduled_brief_manage_opportunity_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage opportunity process Scheduled Email Brief — Schedulable morning-brief email summarizing manage opportunity process for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-opportunity-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_opportunity_process',
    "version": '2.0.1',
    "display_name": 'Manage opportunity process Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage opportunity process for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-manage-opportunity-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-opportunity-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3af66bf7564c6f08',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-manage-opportunity-process', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageOpportunityProcess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageOpportunityProcess'
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
    print(ScheduledBriefManageOpportunityProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
