---
name: "rar-cowork-cookbook-scheduled-brief-reallocate-asset-budgets"
description: "Builds a morning brief on fixed asset budget reallocations from Dynamics 365 ERP (legal entity USMF) \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions \u2014 then saves a draft emai"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_reallocate_asset_budgets", "rar_sha256": "eb1e1aaae7897652af53c982e6e89aa54d0feb090b226ae497ee2445e1d1f78b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_reallocate_asset_budgets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_reallocate_asset_budgets_agent.py` and in the RCI capsule.

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

Reallocate asset budgets Scheduled Email Brief — Builds a morning brief on fixed asset budget reallocations from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves a draft emai

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-reallocate-asset-budgets
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
      "description": "D365 legal entity to query; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_reallocate_asset_budgets_agent.py` and embedded as the fenced Python below (sha256 eb1e1aaae7897652…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_reallocate_asset_budgets_agent.py` first:

```bash
python3 scheduled_brief_reallocate_asset_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_reallocate_asset_budgets_agent.py   # or on stdin
python3 scheduled_brief_reallocate_asset_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reallocate asset budgets Scheduled Email Brief — Builds a morning brief on fixed asset budget reallocations from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves a draft emai

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-reallocate-asset-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_reallocate_asset_budgets',
    "version": '3.0.3',
    "display_name": 'Reallocate asset budgets Scheduled Email Brief',
    "description": 'Builds a morning brief on fixed asset budget reallocations from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves a draft emai',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-reallocate-asset-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-reallocate-asset-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc510e1cd2c8a022',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/reallocate-asset-budgets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-reallocate-asset-budgets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where reallocate asset budgets stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on reallocate asset budgets for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads reallocate asset budgets, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on fixed asset budget reallocations from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves a draft emai', 'example_request': 'Give me the 7am asset budget reallocation brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly asset-budget-reallocation brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefReallocateAssetBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReallocateAssetBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefReallocateAssetBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
