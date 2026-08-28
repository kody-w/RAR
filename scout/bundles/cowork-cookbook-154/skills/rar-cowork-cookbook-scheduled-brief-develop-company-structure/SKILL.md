---
name: "rar-cowork-cookbook-scheduled-brief-develop-company-structure"
description: "Schedulable morning-brief email summarizing develop company structure for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_company_structure", "rar_sha256": "971dff369807fae051d249460c4bc4a63425d15e83adc8223f5ebc45d52c7180", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_company_structure_agent.py` and embedded as the fenced Python below (sha256 971dff369807fae0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_company_structure_agent.py` first:

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
    "version": '2.0.1',
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
