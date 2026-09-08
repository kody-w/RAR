---
name: "rar-cowork-cookbook-teams-update-process-supplier-rebates-and-incentives"
description: "Summarizes supplier rebate and incentive status from Dynamics 365 ERP for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons for review; nothing is post"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives", "rar_sha256": "45bdc882f81dba46b8fd6b5d90e9f81d521cf9e4fe320929db84652d980771aa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_supplier_rebates_and_incentives_agent.py` and in the RCI capsule.

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

Process supplier rebates and incentives Teams Channel Update — Summarizes supplier rebate and incentive status from Dynamics 365 ERP for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons for review; nothing is post

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-supplier-rebates-and-incentives
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
    "card_filename": {
      "description": "Output Adaptive Card JSON filename, e.g. teams-update-process-supplier-rebates-and-incentives-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_supplier_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 45bdc882f81dba46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_supplier_rebates_and_incentives_agent.py` first:

```bash
python3 teams_update_process_supplier_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_supplier_rebates_and_incentives_agent.py   # or on stdin
python3 teams_update_process_supplier_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process supplier rebates and incentives Teams Channel Update — Summarizes supplier rebate and incentive status from Dynamics 365 ERP for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons for review; nothing is post

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-supplier-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives',
    "version": '3.0.3',
    "display_name": 'Process supplier rebates and incentives Teams Channel Update',
    "description": 'Summarizes supplier rebate and incentive status from Dynamics 365 ERP for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons for review; nothing is post',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-process-supplier-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-supplier-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '00f220da3f5d483b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-rebates-and-incentives'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-process-supplier-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output Adaptive Card JSON filename, e.g. teams-update-process-supplier-rebates-and-incentives-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of process supplier rebates and incentives. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-process-supplier-rebates-and-incentives-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process supplier rebates and incentives, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes supplier rebate and incentive status from Dynamics 365 ERP for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons for review; nothing is post', 'example_request': "Draft a Teams update on supplier rebates and incentives for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output Adaptive Card JSON filename, e.g. teams-update-process-supplier-rebates-and-incentives-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on supplier rebates and incentives status, with an Adaptive Card artifact to review before posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateProcessSupplierRebatesAndIncentives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessSupplierRebatesAndIncentives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output Adaptive Card JSON filename, e.g. teams-update-process-supplier-rebates-and-incentives-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateProcessSupplierRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
