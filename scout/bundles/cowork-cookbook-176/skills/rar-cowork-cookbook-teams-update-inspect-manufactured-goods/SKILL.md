---
name: "rar-cowork-cookbook-teams-update-inspect-manufactured-goods"
description: "Summarizes inspect-manufactured-goods status from Dynamics 365 F&SCM (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action but"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_inspect_manufactured_goods", "rar_sha256": "7e7fbced63cbd45f93f45f373feed2fa426ec4b33db04223b3301177d9fc6272", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
