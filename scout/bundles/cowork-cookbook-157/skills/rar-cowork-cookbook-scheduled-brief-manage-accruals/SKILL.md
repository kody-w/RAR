---
name: "rar-cowork-cookbook-scheduled-brief-manage-accruals"
description: "Builds a morning brief on manage accruals from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_accruals", "rar_sha256": "f3075ff25d372038623b09cdd2f558eb17c78bcfeb2076a0b30cd044889624b9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_accruals`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_accruals_agent.py` and in the RCI capsule.

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

Manage accruals Scheduled Email Brief — Builds a morning brief on manage accruals from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-accruals
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against (recipe default: USMF).",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "responsible_owner": {
      "description": "Person the brief is written for and whose draft email is addressed to.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_accruals_agent.py` and embedded as the fenced Python below (sha256 f3075ff25d372038…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_accruals_agent.py` first:

```bash
python3 scheduled_brief_manage_accruals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_accruals_agent.py   # or on stdin
python3 scheduled_brief_manage_accruals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage accruals Scheduled Email Brief — Builds a morning brief on manage accruals from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-accruals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_accruals',
    "version": '3.0.3',
    "display_name": 'Manage accruals Scheduled Email Brief',
    "description": 'Builds a morning brief on manage accruals from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner',
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
        "upstream_slug": 'scheduled-brief-manage-accruals',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-accruals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f7224d7755dae695',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-accruals'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-manage-accruals', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (recipe default: USMF).', 'responsible_owner': 'Person the brief is written for and whose draft email is addressed to.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage accruals stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage accruals for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads manage accruals, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on manage accruals from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner', 'example_request': 'Give me the manage accruals morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to run against (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Person the brief is written for and whose draft email is addressed to.', 'name': 'responsible_owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner needs a daily or weekly accruals brief with an unsent draft email and a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageAccruals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageAccruals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is written for and whose draft email is addressed to.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(ScheduledBriefManageAccruals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
