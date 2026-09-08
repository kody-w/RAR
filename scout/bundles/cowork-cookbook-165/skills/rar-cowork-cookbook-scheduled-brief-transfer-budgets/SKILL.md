---
name: "rar-cowork-cookbook-scheduled-brief-transfer-budgets"
description: "Builds a transfer-budgets morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; saves an email draft to the owner and a Teams-read"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_transfer_budgets", "rar_sha256": "1a8102c9a90de8c14017e2c98ab94d92cf9cbee93ac7b7868f9ac23b354268cc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_transfer_budgets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_transfer_budgets_agent.py` and in the RCI capsule.

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

Transfer budgets Scheduled Email Brief — Builds a transfer-budgets morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; saves an email draft to the owner and a Teams-read

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-budgets
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
      "description": "D365 legal entity to query; the recipe uses USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run it, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_transfer_budgets_agent.py` and embedded as the fenced Python below (sha256 1a8102c9a90de8c1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_transfer_budgets_agent.py` first:

```bash
python3 scheduled_brief_transfer_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_transfer_budgets_agent.py   # or on stdin
python3 scheduled_brief_transfer_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer budgets Scheduled Email Brief — Builds a transfer-budgets morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; saves an email draft to the owner and a Teams-read

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_transfer_budgets',
    "version": '3.0.3',
    "display_name": 'Transfer budgets Scheduled Email Brief',
    "description": 'Builds a transfer-budgets morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; saves an email draft to the owner and a Teams-read',
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
        "upstream_slug": 'scheduled-brief-transfer-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-transfer-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ebf35f6dd2f06dcb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/transfer-budgets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-transfer-budgets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; the recipe uses USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where transfer budgets stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on transfer budgets for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads transfer budgets, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a transfer-budgets morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; saves an email draft to the owner and a Teams-read', 'example_request': 'Give me the transfer budgets morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly transfer-budget brief for the responsible owner, drafted as an email (not sent) plus a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefTransferBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTransferBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefTransferBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
