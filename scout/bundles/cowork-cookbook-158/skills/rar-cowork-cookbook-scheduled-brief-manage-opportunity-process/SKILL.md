---
name: "rar-cowork-cookbook-scheduled-brief-manage-opportunity-process"
description: "Schedulable morning-brief email summarizing manage opportunity process for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_opportunity_process", "rar_sha256": "12149c0d6b8f2a8c63e24f63f910c569516c18ace47ddd6fff00767697670a97", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_opportunity_process_agent.py` and embedded as the fenced Python below (sha256 12149c0d6b8f2a8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_opportunity_process_agent.py` first:

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
    "version": '2.0.0',
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
