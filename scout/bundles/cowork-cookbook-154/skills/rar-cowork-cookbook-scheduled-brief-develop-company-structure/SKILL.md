---
name: "rar-cowork-cookbook-scheduled-brief-develop-company-structure"
description: "Schedulable morning-brief email summarizing develop company structure for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_company_structure", "rar_sha256": "8dfd7a3fd42d25871ab0907819a524dbcf55f76b8df37ff5dd4ff168173f0793", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_company_structure`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_company_structure_agent.py` and in the RCI capsule.

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
