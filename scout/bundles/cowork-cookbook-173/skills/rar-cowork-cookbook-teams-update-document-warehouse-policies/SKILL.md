---
name: "rar-cowork-cookbook-teams-update-document-warehouse-policies"
description: "Summarizes document warehouse policies from Dynamics 365 F&SCM for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_document_warehouse_policies", "rar_sha256": "f86e9f1daee9ed0351aae863117433419de4c75b5eea25413e5c8eff4be31497", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
