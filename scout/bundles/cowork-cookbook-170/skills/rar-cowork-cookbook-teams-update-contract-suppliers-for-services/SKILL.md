---
name: "rar-cowork-cookbook-teams-update-contract-suppliers-for-services"
description: "Summarizes contract suppliers for services from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is po"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_contract_suppliers_for_services", "rar_sha256": "28aba78aaccea4711b8e74ef03e1f789fc7aed5ba98bff228e22e3c784af52ff", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_contract_suppliers_for_services`. The original RAPP
agent is preserved byte-for-byte in `teams_update_contract_suppliers_for_services_agent.py` and in the RCI capsule.

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

Contract suppliers for services Teams Channel Update — Summarizes contract suppliers for services from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is po

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-contract-suppliers-for-services
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-contract-suppliers-for-services-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_contract_suppliers_for_services_agent.py` and embedded as the fenced Python below (sha256 28aba78aaccea471…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_contract_suppliers_for_services_agent.py` first:

```bash
python3 teams_update_contract_suppliers_for_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_contract_suppliers_for_services_agent.py   # or on stdin
python3 teams_update_contract_suppliers_for_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for services Teams Channel Update — Summarizes contract suppliers for services from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is po

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-contract-suppliers-for-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_contract_suppliers_for_services',
    "version": '3.0.3',
    "display_name": 'Contract suppliers for services Teams Channel Update',
    "description": 'Summarizes contract suppliers for services from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is po',
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
        "upstream_slug": 'teams-update-contract-suppliers-for-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-contract-suppliers-for-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '549beb00cb62926f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-services'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-contract-suppliers-for-services', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-contract-suppliers-for-services-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of contract suppliers for services. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-contract-suppliers-for-services-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads contract suppliers for services, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes contract suppliers for services from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is po', 'example_request': "Draft a Teams update on contract suppliers for services in USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-contract-suppliers-for-services-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on contract suppliers for services status, drafted from D365 ERP data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateContractSuppliersForServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateContractSuppliersForServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-contract-suppliers-for-services-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateContractSuppliersForServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
