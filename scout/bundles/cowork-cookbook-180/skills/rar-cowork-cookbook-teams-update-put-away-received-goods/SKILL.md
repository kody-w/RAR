---
name: "rar-cowork-cookbook-teams-update-put-away-received-goods"
description: "Summarizes put away received goods status from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON for review; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_put_away_received_goods", "rar_sha256": "4503cbf7d087114a7b22e5ca17a4ca3cff290c95bc65324d4d90c34b8d43b803", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_put_away_received_goods`. The original RAPP
agent is preserved byte-for-byte in `teams_update_put_away_received_goods_agent.py` and in the RCI capsule.

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

Put away received goods Teams Channel Update — Summarizes put away received goods status from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON for review; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-put-away-received-goods
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-put-away-received-goods-2026-05-24-card.json.",
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
    },
    "scope_date": {
      "description": "Date or reporting period the update covers.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_put_away_received_goods_agent.py` and embedded as the fenced Python below (sha256 4503cbf7d087114a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_put_away_received_goods_agent.py` first:

```bash
python3 teams_update_put_away_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_put_away_received_goods_agent.py   # or on stdin
python3 teams_update_put_away_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Put away received goods Teams Channel Update — Summarizes put away received goods status from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON for review; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-put-away-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_put_away_received_goods',
    "version": '3.0.3',
    "display_name": 'Put away received goods Teams Channel Update',
    "description": 'Summarizes put away received goods status from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON for review; nothing is posted.',
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
        "upstream_slug": 'teams-update-put-away-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-put-away-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd40282411026eca3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/put-away-received-goods'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-put-away-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-put-away-received-goods-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'scope_date': 'Date or reporting period the update covers.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of put away received goods. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-put-away-received-goods-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads put away received goods, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes put away received goods status from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON for review; nothing is posted.', 'example_request': "Draft a Teams update on put away received goods for USMF with an Adaptive Card — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-put-away-received-goods-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Date or reporting period the update covers.', 'name': 'scope_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on put away received goods status from D365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdatePutAwayReceivedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePutAwayReceivedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-put-away-received-goods-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope_date': {'description': 'Date or reporting period the update covers.', 'type': 'string'}},
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
    print(TeamsUpdatePutAwayReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
