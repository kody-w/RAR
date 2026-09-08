---
name: "rar-cowork-cookbook-teams-update-pack-goods"
description: "Summarizes pack goods status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_pack_goods", "rar_sha256": "aa7d4fdb8a4e894162c18dba0067fe0446d07d2019e51c67c8bc61c99e0bcc42", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
