---
name: "rar-cowork-cookbook-d365-record-to-report-define-accounting-policies"
description: "A Dynamics 365 F&SCM expert scoped to the Define accounting policies area (a level-2 subdomain of Record to report) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_record_to_report_define_accounting_policies", "rar_sha256": "dd897009fca7fabd5ddfda2b84e267b166c9c7e43b6beab713da981706f91d91", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_record_to_report_define_accounting_policies`. The original RAPP
agent is preserved byte-for-byte in `d365_record_to_report_define_accounting_policies_agent.py` and in the RCI capsule.

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

D365 Define accounting policies Expert — A Dynamics 365 F&SCM expert scoped to the Define accounting policies area (a level-2 subdomain of Record to report) - covers 10 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-record-to-report-define-accounting-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_record_to_report_define_accounting_policies_agent.py` and embedded as the fenced Python below (sha256 dd897009fca7fabd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_record_to_report_define_accounting_policies_agent.py` first:

```bash
python3 d365_record_to_report_define_accounting_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_record_to_report_define_accounting_policies_agent.py   # or on stdin
python3 d365_record_to_report_define_accounting_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Define accounting policies Expert — A Dynamics 365 F&SCM expert scoped to the Define accounting policies area (a level-2 subdomain of Record to report) - covers 10 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-record-to-report-define-accounting-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_record_to_report_define_accounting_policies',
    "version": '2.0.1',
    "display_name": 'D365 Define accounting policies Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Define accounting policies area (a level-2 subdomain of Record to report) - covers 10 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-record-to-report-define-accounting-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-record-to-report-define-accounting-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b6e681706e0e4a1d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'record-to-report/d365-record-to-report-define-accounting-policies', 'uses_skills': {'custom': ['d365-record-to-report-define-accounting-policies'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365RecordToReportDefineAccountingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365RecordToReportDefineAccountingPolicies'
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
    print(D365RecordToReportDefineAccountingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
