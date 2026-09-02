---
name: "rar-cowork-cookbook-d365-record-to-report-define-accounting-policies"
description: "A Dynamics 365 F&SCM expert scoped to the Define accounting policies area (a level-2 subdomain of Record to report) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_record_to_report_define_accounting_policies", "rar_sha256": "5d6bfd1a2661a353bfce12896469eca39e78cc99f8c0088595b66e02096ca0ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_record_to_report_define_accounting_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-record-to-report-define-accounting-policies:efd8d0a334c59330c3a175a2e2c15e1c1fdc83ce0303b99299c0768dffcee09b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_record_to_report_define_accounting_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_record_to_report_define_accounting_policies_agent.py` is
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
