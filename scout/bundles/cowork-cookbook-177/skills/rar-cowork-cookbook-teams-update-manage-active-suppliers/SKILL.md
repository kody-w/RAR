---
name: "rar-cowork-cookbook-teams-update-manage-active-suppliers"
description: "Summarizes active supplier status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_active_suppliers", "rar_sha256": "a29455ee80e4f197f73e55f0091d8b06ed529c32235591248c8facf27d6329dd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_active_suppliers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_active_suppliers_agent.py` and in the RCI capsule.

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

Manage active suppliers Teams Channel Update — Summarizes active supplier status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-active-suppliers
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-manage-active-suppliers-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to scope the supplier summary, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_active_suppliers_agent.py` and embedded as the fenced Python below (sha256 a29455ee80e4f197…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_active_suppliers_agent.py` first:

```bash
python3 teams_update_manage_active_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_active_suppliers_agent.py   # or on stdin
python3 teams_update_manage_active_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage active suppliers Teams Channel Update — Summarizes active supplier status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-active-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_active_suppliers',
    "version": '3.0.3',
    "display_name": 'Manage active suppliers Teams Channel Update',
    "description": 'Summarizes active supplier status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.',
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
        "upstream_slug": 'teams-update-manage-active-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-active-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3833d56f8c9be519',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-active-suppliers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-manage-active-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-manage-active-suppliers-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to scope the supplier summary, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of manage active suppliers. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-manage-active-suppliers-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage active suppliers, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes active supplier status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.', 'example_request': 'Draft a Teams update on active suppliers in USMF with an Adaptive Card I can review before posting.', 'inputs': [{'description': 'D365 legal entity to scope the supplier summary, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-manage-active-suppliers-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on active suppliers from D365 ERP data, with an Adaptive Card artifact saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateManageActiveSuppliers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageActiveSuppliers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-manage-active-suppliers-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to scope the supplier summary, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateManageActiveSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
