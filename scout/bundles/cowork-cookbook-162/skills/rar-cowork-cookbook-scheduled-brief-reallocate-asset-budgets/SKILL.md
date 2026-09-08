---
name: "rar-cowork-cookbook-scheduled-brief-reallocate-asset-budgets"
description: "Builds a morning brief on fixed asset budget reallocations from Dynamics 365 ERP (legal entity USMF) \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions \u2014 then saves a draft emai"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_reallocate_asset_budgets", "rar_sha256": "eb1e1aaae7897652af53c982e6e89aa54d0feb090b226ae497ee2445e1d1f78b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
