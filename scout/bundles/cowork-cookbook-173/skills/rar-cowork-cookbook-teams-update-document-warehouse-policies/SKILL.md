---
name: "rar-cowork-cookbook-teams-update-document-warehouse-policies"
description: "Summarizes document warehouse policies from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_document_warehouse_policies", "rar_sha256": "f86e9f1daee9ed0351aae863117433419de4c75b5eea25413e5c8eff4be31497", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_document_warehouse_policies`. The original RAPP
agent is preserved byte-for-byte in `teams_update_document_warehouse_policies_agent.py` and in the RCI capsule.

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

Document warehouse policies Teams Channel Update — Summarizes document warehouse policies from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-document-warehouse-policies
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
      "description": "Filename for the Adaptive Card JSON output, e.g. teams-update-document-warehouse-policies-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_document_warehouse_policies_agent.py` and embedded as the fenced Python below (sha256 f86e9f1daee9ed03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_document_warehouse_policies_agent.py` first:

```bash
python3 teams_update_document_warehouse_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_document_warehouse_policies_agent.py   # or on stdin
python3 teams_update_document_warehouse_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Document warehouse policies Teams Channel Update — Summarizes document warehouse policies from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-document-warehouse-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_document_warehouse_policies',
    "version": '3.0.3',
    "display_name": 'Document warehouse policies Teams Channel Update',
    "description": 'Summarizes document warehouse policies from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-document-warehouse-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-document-warehouse-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d39892e8d9c1c36',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/document-warehouse-policies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-document-warehouse-policies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON output, e.g. teams-update-document-warehouse-policies-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of document warehouse policies. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-document-warehouse-policies-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads document warehouse policies, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes document warehouse policies from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons.', 'example_request': 'Summarize document warehouse policies in USMF and draft a Teams post plus an Adaptive Card for me to review.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON output, e.g. teams-update-document-warehouse-policies-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on D365 warehouse policy status, with an Adaptive Card saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDocumentWarehousePolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDocumentWarehousePolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON output, e.g. teams-update-document-warehouse-policies-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDocumentWarehousePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
