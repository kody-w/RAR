---
name: "rar-cowork-cookbook-teams-update-pack-goods"
description: "Summarizes pack goods status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_pack_goods", "rar_sha256": "aa7d4fdb8a4e894162c18dba0067fe0446d07d2019e51c67c8bc61c99e0bcc42", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_pack_goods`. The original RAPP
agent is preserved byte-for-byte in `teams_update_pack_goods_agent.py` and in the RCI capsule.

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

Pack goods Teams Channel Update — Summarizes pack goods status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pack-goods
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-pack-goods-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize pack goods for (recipe default: USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_pack_goods_agent.py` and embedded as the fenced Python below (sha256 aa7d4fdb8a4e8941…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_pack_goods_agent.py` first:

```bash
python3 teams_update_pack_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_pack_goods_agent.py   # or on stdin
python3 teams_update_pack_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pack goods Teams Channel Update — Summarizes pack goods status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pack-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_pack_goods',
    "version": '3.0.3',
    "display_name": 'Pack goods Teams Channel Update',
    "description": 'Summarizes pack goods status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
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
        "upstream_slug": 'teams-update-pack-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-pack-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7cf0b5a6d51ff7e5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pack-goods'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-pack-goods', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-pack-goods-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize pack goods for (recipe default: USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of pack goods. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-pack-goods-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads pack goods, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes pack goods status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams post and Adaptive Card on pack goods status in USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize pack goods for (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-pack-goods-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on pack goods status from D365 ERP, with an Adaptive Card draft saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdatePackGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePackGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-pack-goods-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize pack goods for (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdatePackGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
