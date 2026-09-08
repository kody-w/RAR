---
name: "rar-cowork-cookbook-teams-update-process-supplier-rebates-and-incentives"
description: "Summarizes supplier rebate and incentive status from Dynamics 365 ERP for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons for review; nothing is post"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives", "rar_sha256": "45bdc882f81dba46b8fd6b5d90e9f81d521cf9e4fe320929db84652d980771aa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
