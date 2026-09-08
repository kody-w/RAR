---
name: "rar-cowork-cookbook-teams-update-put-away-received-goods"
description: "Summarizes put away received goods status from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON for review; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_put_away_received_goods", "rar_sha256": "4503cbf7d087114a7b22e5ca17a4ca3cff290c95bc65324d4d90c34b8d43b803", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
