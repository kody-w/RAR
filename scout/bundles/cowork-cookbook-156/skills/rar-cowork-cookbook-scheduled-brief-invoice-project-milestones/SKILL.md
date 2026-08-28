---
name: "rar-cowork-cookbook-scheduled-brief-invoice-project-milestones"
description: "Schedulable morning-brief email summarizing invoice project milestones for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_invoice_project_milestones", "rar_sha256": "08a90ef64ef0d660feada5a5b46d76b079ee7c51d9df43ec1ff2c5cd72ba817f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_invoice_project_milestones`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_invoice_project_milestones_agent.py` and in the RCI capsule.

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

Invoice project milestones Scheduled Email Brief — Schedulable morning-brief email summarizing invoice project milestones for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-invoice-project-milestones
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_invoice_project_milestones_agent.py` and embedded as the fenced Python below (sha256 08a90ef64ef0d660…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_invoice_project_milestones_agent.py` first:

```bash
python3 scheduled_brief_invoice_project_milestones_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_invoice_project_milestones_agent.py   # or on stdin
python3 scheduled_brief_invoice_project_milestones_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Invoice project milestones Scheduled Email Brief — Schedulable morning-brief email summarizing invoice project milestones for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-invoice-project-milestones
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_invoice_project_milestones',
    "version": '2.0.1',
    "display_name": 'Invoice project milestones Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing invoice project milestones for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-invoice-project-milestones',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-invoice-project-milestones',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf49216d61b17d7b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/invoice-project-milestones'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-invoice-project-milestones', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefInvoiceProjectMilestones(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefInvoiceProjectMilestones'
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
    print(ScheduledBriefInvoiceProjectMilestones().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
