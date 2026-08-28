---
name: "rar-cowork-cookbook-d365-record-to-report-define-accounting-policies"
description: "A Dynamics 365 F&SCM expert scoped to the Define accounting policies area (a level-2 subdomain of Record to report) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_record_to_report_define_accounting_policies", "rar_sha256": "5d6bfd1a2661a353bfce12896469eca39e78cc99f8c0088595b66e02096ca0ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_record_to_report_define_accounting_policies_agent.py` and embedded as the fenced Python below (sha256 5d6bfd1a2661a353…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_record_to_report_define_accounting_policies_agent.py` first:

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
    "version": '2.0.0',
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
