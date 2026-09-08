---
name: "rar-cowork-cookbook-teams-update-process-change-orders"
description: "Summarizes the current state of process change orders from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; do"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_change_orders", "rar_sha256": "afd8c87599cf34dd9b575e64b98eec95927dd0c26977711f2f65186791e3a27e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_change_orders`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_change_orders_agent.py` and in the RCI capsule.

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

Process change orders Teams Channel Update — Summarizes the current state of process change orders from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; do

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-change-orders
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-process-change-orders-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to scope the summary, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_change_orders_agent.py` and embedded as the fenced Python below (sha256 afd8c87599cf34dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_change_orders_agent.py` first:

```bash
python3 teams_update_process_change_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_change_orders_agent.py   # or on stdin
python3 teams_update_process_change_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process change orders Teams Channel Update — Summarizes the current state of process change orders from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; do

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-change-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_change_orders',
    "version": '3.0.3',
    "display_name": 'Process change orders Teams Channel Update',
    "description": 'Summarizes the current state of process change orders from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; do',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-process-change-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-change-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b66b2476a3bd0de2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/process-change-orders'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-process-change-orders', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-process-change-orders-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to scope the summary, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of process change orders. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-process-change-orders-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process change orders, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of process change orders from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; do', 'example_request': 'Summarize process change orders in USMF and draft a Teams post plus an Adaptive Card for me to review.', 'inputs': [{'description': 'D365 legal entity to scope the summary, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-process-change-orders-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on process change order status pulled from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateProcessChangeOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessChangeOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-process-change-orders-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to scope the summary, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateProcessChangeOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
