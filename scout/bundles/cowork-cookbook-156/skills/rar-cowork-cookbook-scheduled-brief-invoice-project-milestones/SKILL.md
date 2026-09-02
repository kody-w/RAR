---
name: "rar-cowork-cookbook-scheduled-brief-invoice-project-milestones"
description: "Schedulable morning-brief email summarizing invoice project milestones for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_invoice_project_milestones", "rar_sha256": "5422e3967a0a0076f1995e868c745135151ef0d78fc49ae8aae8318606c2f7f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_invoice_project_milestones_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-invoice-project-milestones:abd04476f2406a5633a5f1e00de585a3fb54d3632096de0612bf1012b6bd1a06", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_invoice_project_milestones`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_invoice_project_milestones_agent.py` is
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
