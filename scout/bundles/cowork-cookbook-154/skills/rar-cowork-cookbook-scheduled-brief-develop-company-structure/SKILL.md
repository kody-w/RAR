---
name: "rar-cowork-cookbook-scheduled-brief-develop-company-structure"
description: "Schedulable morning-brief email summarizing develop company structure for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_company_structure", "rar_sha256": "8dfd7a3fd42d25871ab0907819a524dbcf55f76b8df37ff5dd4ff168173f0793", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_develop_company_structure_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-develop-company-structure:031f11cb0eb442410543e53cb70960393ea01ebf00369a1609577b187c20ce04", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_develop_company_structure`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_develop_company_structure_agent.py` is
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

Develop company structure Scheduled Email Brief — Schedulable morning-brief email summarizing develop company structure for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-company-structure
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_company_structure_agent.py` and embedded as the fenced Python below (sha256 8dfd7a3fd42d2587…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_company_structure_agent.py` first:

```bash
python3 scheduled_brief_develop_company_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_company_structure_agent.py   # or on stdin
python3 scheduled_brief_develop_company_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop company structure Scheduled Email Brief — Schedulable morning-brief email summarizing develop company structure for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-company-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_company_structure',
    "version": '2.0.0',
    "display_name": 'Develop company structure Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop company structure for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-develop-company-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-company-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '02cf262855f4353f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-company-structure'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-develop-company-structure', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDevelopCompanyStructure(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopCompanyStructure'
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
    print(ScheduledBriefDevelopCompanyStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
