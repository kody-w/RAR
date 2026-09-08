---
name: "rar-cowork-cookbook-teams-update-process-change-orders"
description: "Summarizes the current state of process change orders from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; do"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_change_orders", "rar_sha256": "afd8c87599cf34dd9b575e64b98eec95927dd0c26977711f2f65186791e3a27e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
