---
name: "rar-cowork-cookbook-teams-update-contract-suppliers-for-services"
description: "Summarizes contract suppliers for services from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is po"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_contract_suppliers_for_services", "rar_sha256": "28aba78aaccea4711b8e74ef03e1f789fc7aed5ba98bff228e22e3c784af52ff", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
