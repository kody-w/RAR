---
name: "rar-cowork-cookbook-teams-update-inspect-manufactured-goods"
description: "Summarizes inspect-manufactured-goods status from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action but"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_inspect_manufactured_goods", "rar_sha256": "7e7fbced63cbd45f93f45f373feed2fa426ec4b33db04223b3301177d9fc6272", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_inspect_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `teams_update_inspect_manufactured_goods_agent.py` and in the RCI capsule.

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

Inspect manufactured goods Teams Channel Update — Summarizes inspect-manufactured-goods status from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action but

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-inspect-manufactured-goods
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
      "description": "Output Adaptive Card JSON filename, e.g. teams-update-inspect-manufactured-goods-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_inspect_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 7e7fbced63cbd45f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_inspect_manufactured_goods_agent.py` first:

```bash
python3 teams_update_inspect_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_inspect_manufactured_goods_agent.py   # or on stdin
python3 teams_update_inspect_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inspect manufactured goods Teams Channel Update — Summarizes inspect-manufactured-goods status from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action but

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-inspect-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_inspect_manufactured_goods',
    "version": '3.0.3',
    "display_name": 'Inspect manufactured goods Teams Channel Update',
    "description": 'Summarizes inspect-manufactured-goods status from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action but',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-inspect-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-inspect-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f9d1e64ee0dd3adb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/inspect-manufactured-goods'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-inspect-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output Adaptive Card JSON filename, e.g. teams-update-inspect-manufactured-goods-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of inspect manufactured goods. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-inspect-manufactured-goods-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads inspect manufactured goods, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes inspect-manufactured-goods status from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action but', 'example_request': "Draft a Teams post and Adaptive Card on inspect manufactured goods status in USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output Adaptive Card JSON filename, e.g. teams-update-inspect-manufactured-goods-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams channel update and Adaptive Card on inspect manufactured goods status from D365 ERP, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateInspectManufacturedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateInspectManufacturedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output Adaptive Card JSON filename, e.g. teams-update-inspect-manufactured-goods-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateInspectManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
