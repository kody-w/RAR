---
name: "rar-cowork-cookbook-scheduled-brief-invoice-project-milestones"
description: "Schedulable morning-brief email summarizing invoice project milestones for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_invoice_project_milestones", "rar_sha256": "5422e3967a0a0076f1995e868c745135151ef0d78fc49ae8aae8318606c2f7f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_invoice_project_milestones_agent.py` and embedded as the fenced Python below (sha256 5422e3967a0a0076…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_invoice_project_milestones_agent.py` first:

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
    "version": '2.0.0',
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
