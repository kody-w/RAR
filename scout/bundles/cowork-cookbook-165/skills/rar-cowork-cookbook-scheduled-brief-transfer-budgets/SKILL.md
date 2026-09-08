---
name: "rar-cowork-cookbook-scheduled-brief-transfer-budgets"
description: "Builds a transfer-budgets morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; saves an email draft to the owner and a Teams-read"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_transfer_budgets", "rar_sha256": "1a8102c9a90de8c14017e2c98ab94d92cf9cbee93ac7b7868f9ac23b354268cc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
