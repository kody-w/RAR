---
name: "rar-cowork-cookbook-teams-update-analyze-and-reconcile-compensation-and-benefits"
description: "Drafts a Teams channel update on compensation and benefits reconciliation status from Dynamics 365 F&SCM data for a legal entity, returning a markdown post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits", "rar_sha256": "64cfc12b15c180ef0281053be3dc387a1fe63dbef5ffafaae4df0238380822b3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` and in the RCI capsule.

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

Analyze and reconcile compensation and benefits Teams Channel Update — Drafts a Teams channel update on compensation and benefits reconciliation status from Dynamics 365 F&SCM data for a legal entity, returning a markdown post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits
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
      "description": "Filename for the generated Adaptive Card JSON artifact.",
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
    },
    "quick_actions": {
      "description": "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` and embedded as the fenced Python below (sha256 64cfc12b15c180ef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` first:

```bash
python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py   # or on stdin
python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and reconcile compensation and benefits Teams Channel Update — Drafts a Teams channel update on compensation and benefits reconciliation status from Dynamics 365 F&SCM data for a legal entity, returning a markdown post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits',
    "version": '3.0.3',
    "display_name": 'Analyze and reconcile compensation and benefits Teams Channel Update',
    "description": 'Drafts a Teams channel update on compensation and benefits reconciliation status from Dynamics 365 F&SCM data for a legal entity, returning a markdown post plus an Adaptive Card JSON file saved for review, not posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-and-reconcile-compensation-and-benefits',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fabfb2687117fadc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-and-reconcile-compensation-and-benefits'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-analyze-and-reconcile-compensation-and-benefits', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'quick_actions': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of analyze and reconcile compensation and benefits. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-analyze-and-reconcile-compensation-and-benefits-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze and reconcile compensation and benefits, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Drafts a Teams channel update on compensation and benefits reconciliation status from Dynamics 365 F&SCM data for a legal entity, returning a markdown post plus an Adaptive Card JSON file saved for review, not posted.', 'example_request': "Draft a Teams update on comp and benefits reconciliation for USMF with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'name': 'card_filename'}, {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel post and Adaptive Card summarizing compensation and benefits reconciliation status from D365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}},
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
    print(TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916+fOiWLbnv+J8X8Rk1SMzQZAtX7yIAQVERZRVrKzIYt/3RaGm//e5qLlUd3XPdHT/NOaicu89+/mcc4Tf3+y+i8rm7dOb6tvFQrCzLI78ZmEX3mJd3somBW9l6oB/C7csuiZ2+q5s2rf3b57fuk1cdXFZgOObxg66dmEvNN/O24Ub2UXhZ4u+8uzOX5QFOJ1XftHa8/4Heccv/CAGZxofUHbjLH6utZ3d9e0iaMp8sRkLO4/ddoER+IL/n+paWgB69iIogYiLzA/tbOEXXdyN7wGZrm+KuAjBSm43qVfeikVVtt2iygA9oB3j2UDcwV+s7cZb7FT5uAjizF+09uB7D5qNP8T+7f2iKLvHUd/7CDT173ZeZX779umXX9+/xeDz26ff39zMbsGlt4fC+kNPprCzcQJvnvLSyV//oDa4zr6UBlQzuwjB8WoEDijA98pvgAg5uOT5weL17afWz4L3i//8z/RmN2H786fPxeL1+vw2/1H6YtFF/qIr7VnchWtXtgNs2Y0fF0x2s8f2ZZjZNy3wXxF+fJ78TqmsFv89r/30ZPIx9LufPr+VQISH2J/ffl4A23x+a/r588eZSvXTzx+z8uY3P/38nU7bO4nvdjMxIPXHL6/vL7Jg4/etcbD4op649YsXCIG48gHxH/SbX0/RX+ReJvny3PxTWb1f/DnlWZ//BvI+I9QBdP+cLLABOPn2MSnj4qcXj6Yc/MIuXP+nn/8eWTfy3TSL2+7/ie4vT8KRb3vAWi+T/Pz+4b5fF9BLt280/z7bCgTMP6MJ2P6V3TdD/T3aD8/+FeksLvz2my//lNyfHYD+e/HL39XtHx14vwg+v238DCRoYzuZ/2nx+yNEfnnnfb/47te/ANL/VzJq2Tfug8KX3C7iwG+7L19+edc+Lr/79Zd3fQWiGCTul77J/ozmn9n1wecPFnzt+umPZwF/vUiLGX6+5dDi97L6H81fPi4MO4u979fbT4sfM3F+QYtZia9Mnyb4IRtbIOsPdvz57S8AkgqgTe8+lgF+/Md/LKTYbcq2DLqF6pZ9twAO7uLcn4XXorhdgL8zagC885s2BoZ97QPxP3t4lrgMFr/9L/dRAz64rxoAdzPYfXmi+hf7CXfg3fvyFcT9Lz8C/WPpK9D/9nGhAZ5lE4cxOLlQmNPpc2GHAMBnearGb/1mRmJn7PwPINU/zB8WcbH47V9h++XB4WM1/vYoO/ETL5W1OGNl22f+x9kqZuQXLxu4oFT4d9/tAfOsdIGkc5Vo5wrTlhkoH91swTaNs2zhxUACUBDHB21g5U8zsd9++82x2+hz8QR3bPGslC0MNnwTZ/HhA1A5yOIw6j4XvhuVi3e//+Xd4n8v/tGpB/GZxwlUn5cPgYSPYgZyss/BNuBeEBAAcB4+/P0vL8MDMgUo7cDjcRD7z8MgplPf++oFdct8QHEClGZgfWD5vCqbbq6ocfdxIQaLb/ICpvPSXFOiucJ6PrC95xfuCKjaQJ1vlpwr6eyUNgAlum/9B9ffnMZ+iJgDcLC73xbS+gQqWJmB/2YxH5vA4bKIgfm/xcjzOiDSvGsX7FcSHxfHOYoXld3YVdTYLx6B/fTL3Cm8jgPi9qLwb5+LuYb7s6ke4fI0D9gELOO+XPrh0RmAoAL44bVfeT/22HOd1R71tvlctK90sRv/0ckAUcZF2MfeXET+6xVSbVT2mfewH5B0pvTygvfyyiMGX+3DM5S+BvY/aJyerdb61Wo9W5DF5x5FlqvF/7f92MNQgqBwAqNxmwV31BTr6cC5P50d/WxpgQwPEo9k/d4VfUW+rwXgc5HFIBqb8b+eOx8CvPY8QbVvgDAKozzog5gDDpzpPlJiDvGmmZPJ/lx8rTTvgcIPWAXGA/gB8msO668M59WvkkYAJObv37uOh/GBMYBDQNgvqt7JQEgGvu85tpsCqZo5rV8+Bvnhzyl+i2I3+oNWsxNAGAL6s6tnpwLjf/yG/s/Vr6L/4eCzuZqPPBrPHmR18yAA5PBnAedQucUdADe7e44DQM9PDyJAjbzqZt0dEDpA0+dFv/HrPm7jbsbQp139CmD7h/n9qel81b9XIJWAsUDCVD2w7iPF5vjJQesEZAAoAzIujwvQSgCjvIzwIGjnM14APH71uk+Kj8svhfxHXs418OvBWZH5zNxWPKPbLsYfYUX7szAB9PJ5x4PvX0faN24z7RlaWwCPgOPX1Wf/8fHZQjx7lMVXup/+Zt766Z8byR5Ngf7HAPi0iLquaj/B8LOQf63jH0H2w09Z22dN//BEhg+v4grevQ/fMOjDj2DxWPoKFn/g+TTHp8U/J/cfSLzy5tNi+RH5iMxLh1fcvV7ATOsPrPVhNa9+LhT/OyQD9mUORJydOoIm4lv9/LoFFNGwARgFNj/raTuX4Ruo/I8CAjz0ufgxEeZEnIEznAO3LX8AiEcjAZLi6dBvdQ4sFR3g7c3taujPs+MjbVr/7VPRZ9n7NwCf/r8wM841Lp+zoJ0nUJBvoCvsYv/xDaSz92WW7snj978a0PnXyrdg/G64P8FhG5CdK+isQjdWs8zP4XFuNx/wde/+lof8+GBnHxcbH0Bl1v6YE68aOPcAP6Tu08zAvC7Q5f1cTQAiAQmBIrOac9rbLcgjIPWfyvKoOV+eNedvBdrMderHsjQjcduDot7EE2Dnfww/LnRV4v+U9ree+28Jm6BtmWl55ae5gr9/YR94B3PS+8W3kQdo9BpCHz8kFD2Y73+Zx63ZmY8j8wdwBrx9O/TtxxXHf/v1T+QCaOqmX+yv/f5fy3aelz88lxcgx7pyhqsS9DBu1nuP4v/sr2a7PyzwzgBVdoZX4LN37xfvZBB+c8szm+/dn5gGyPDAdFAZZ3W+2+m7tOVjUpylBdp1zx82fn8DsWvPDcMrel+jBtgOIPBDO7dKMEh8wBB8f6YoWPu3DiEv2m1kg0YXECdWbuAuUWeJu0sK8QMEpZYIjjk+5rkYRdrLwCcwDzTEeBDYgW37Kw/swSiMQigUdTBA7wkCM8s8nuWdhQVm+gBwxP++DC55L0Wfis1W/DbzzAZ56fv7m0OswM7tqhWZ52sN00sHxg7OvblABQLdFdPbt7HB3tFClWFluSN36RW7D2QQ2VpSXrOzNISquVsz6vniMmNN89KW2J3QtY9jU04yDHfOhDNJWPQKZzlwfEX7GA7h0LSnyIlV1VrDDMhIhTTtmHo6ijdt5+7anBj0cX2Q9YJYGvvMvlu64uCaKxQCkZp5zQ18t22zdXyBKdKHY01qDSxtMbE4J2rSrq8iqTVH+0hqnTbuRcSqzanREqe6iE6EXCm41y+rLhumlA7Wx7VmVUZ12Jllp48cqJcrlFsyVRwthdprhmO2D5QsM4hClJayeGI4OrdqTZWvPMwRO51IE0qDC4y86Xu67lOf1u8bdemDolSvMrFd7Yu6DYMNR0Dw0CwRgj5hyY3mEDoYioIeVNh3uEiwLSGL1PGg2Q7LKFJ5TDj0gMn4fUveNkdqv1njk46G4rXacOqILcmK88Z9T4pKdI66kJW3GU1VzW6cIiNvCyFSIZ8f161nj7eM4s1q4Pe5uV9PwJBotQnTeKTu8i2ucT/p7mYgoClKb7ALqvXGmCj6YRuKTFtaq22Oa/Lu3OzUfZbsKZaDQu7A98g48ussiO1I3ub0FVJPEaGQyu5uK9KaRWIfkckWouoiG7R2u3f3eB2mncFlQp4eOWq7XlWWeJPxuByOZ9bmk8rNTNd2bWsDOwZ5rir/xqOTcsoUGzYSYRcTeq5FeF2MBMZh1RGFlG3dYP25joyrYCgGvq4FarTP9ZjbqBSzlFLrh8q5ToLPTiNZ5RbGHRIpzd3smrGwp3SKJUTFmd0sI1QM7uWQ0cwtJ3eSB+13UdqwyNG29aNbn4XuwGDJrskwY3/fVjtuNSRelJr7JWGTOzW61SMP7d3Tqt4T2eheM/86tOpAbvc7GN0hTc/Il5UM+8yJ5ahLz21Ehy/GfFJCZECXTbBeocpVcCDzZlKtdp6CU4Qnp0O9Sw2eqfNjqEiVhSAQuzwSSDg5usUHmcFHvq0akTJRJu8ex3TF4/lhgm9bOJQp6CpPEuyexKT2TkMGQUVPbQ93057W0c5Ld1lLoCsRR3rldCi0dZQMp/W0L6PQGIejL57ZXkoi4UQFjHe6mW2rVuX1uEd9WFzGK7yRloJ6lLiNI56hm19q94pVuQ1PZOzVlrlDgAgg1rmDvj0bDB+umXNCXZbhxonyC7Nh4EN+66RxIgJpCm8kHTvoydxXt26IjOW1QJCqMjKBNQwt5MVLoBtMs8/DOs5oI45KYpWSnHKip/WpmIgi1fNpVHqCteF9IMobo7t6l2g5YDxes/VAW4q9bwM8bAyY2/cb8xpsZAnZ54LeU2y6dgNzpZ+ljDDYW8LlZzE8UtfeR83oUOAleu4orDWubOry3LoY4x3G70vjyLdKx2K0Zxv9OdlRLuOGoz6V7uG+NEXK7yQSjYJES5fLCTLTYlfpkrqnb6vOaVtdI0p2e6qXUsnvMXqL8o2Bn4+tArMTHuE4ecH5YNo56n3PL42WOoKEWBm2x1/I+1LWZNEaoopSLDtsT/VFlMkbchYyjOQ2IQzqiYqWklHVu21Ca0RtiZeKP6zsS7lHEvZ4cJeFoOqKKfTZyggSudJSO9wWzaqz9kQZb3CURmrVIT3sSnGcZ+prBNveCbnGx9GabrSI9B4isU5ZADyKzeC21rK8v9Jq3JS7yw07TTTPg6LZR9tK3iEIO/GQZNi5oTuVr1PIKru4FcIxIAd2+pDfhHJ5LkVLJAgKlIAw3NoTKCNnCjLwkNO4USCyztzpunUPofh8pYSsO6ep0SYx5A8w1yFbbaVxWSiP/VReuNKmRd4I1XxzPFXiPrWTO9IS9N5lYsKIMqmWrwBbXAnnhCJeFgi3ReJEOaYGdywNr4F3+3VquplLFj4V5ZkahwoiCZh9u/dNlg7GwK0Pl0N6kLVsQCWjzdHLTjCFAa0gv9CWkH8idKZSLmvHuq/6oF3V0S3Dg7adHGvLb5s2xQ9iwzYDjDLnnUnZXreWz6Zy3pOZe1BoCDJoGJLH6UTcU35Tk24lU3LtTNPJ5c07uxYF5dCeD+5pJ+90RQUVVa83bctxFwUSDpZW73N0urHu5BoHnmFX7YgqfMTncSAJsq2inj5tiIiBFSsO9DLGBEtVVZuZ9tudOFrueCc1sYrx6cDWmz23XSa7zHCaQdFvdz7sYhu1fIIqd4a2tUyDzQpUzKQbjJ6tytfGSVctGYN79YY2xxZNcMq8IpvgfNByKV2pXLtdSuIZbSH0TOGpdS6qQ9aO1XTBo0yV2XpXn289MRltwdPGWihEfnfyWCfkbyar2APKYaBZF5zYiXmFu7UwnriKKbH79NjolTPcGLHdpmjYOAfqgh099nC3GCbrNAPqTD1hrD3bUupkVlUsSLzrHLBVC6BUGdzLebzyThZGPXO0KkVTEzyxihXk1eKtZzpC3J/73goYn5tYnclcfwjdLe/iW1EKESyJCHeny/YkSxwhj9R+L604Utr7FMb5VnSLT2y6R40LatBdW2pJIWx1Qo3uwl6xLQOuDriRQoc6PUuEuTpdpXbDcDB6tWPLESOl3XJ5hUvOleS809nh9Zu1X6469abiTXndMFYo9z7eJerS09sNv8pWOeoTHAeXyDmlBTvBSn1n+leev9o7/9qa0+awJWrPKqddrBquAt2am3y98nassoxqLeOreT4ErehxJM/XsbwReniLJJS96iTR2DgIAbPZUeE2dQlb2cb09y3W5hOjtTZc6BJPe9eM76HCSBjdReWt7XTtZUeJWRYmad0doCnBhSK4CxGSYlrKVfIWXtInbd1SMn1XpXpznxJkvPO+5/kMluHjHtGF5rITsyC9jaqCbyUQi+ox1HB6CXDV9Orxkqp6ZIJuLlrbemK0qKzRzOXI4v7ubLeb075V8YqhLlf9XjPwulH6fUDTBiPVquh4Ek2P3eizYShVhi2E1xN9rLhi57uchRbNktoJk3DzLgc7lq6wRXLcOsdvVg8a+mw6VSi+ZLbVeS/y2c44mwg8KoJ+JKldTDdhhgtkNIwDCdPx7TCOyLVPB0dade41hytS8yu5k0P8clpFHAiyuHTVDckAsScaaY99QBI4dhRMlb0YF55Tw71oR14VM0rVuCEnWsjhQBBqNpKamtb+seXCy1nj1kl6dfz6Ci3vw5Wi7xqd1p4iDCmbW5Ll4rFUYhcRPtxZr+DbEs2XPuOOZr2VVaJvvFwdEwbADZkv2W7j5QxzYYT7pOnZ7pQjEasNrHLB1sQGuVStRiFjsanDqhtjuCThdXnYX+AhRmHpMmEh2mwEaiPc1+LEr2DEPVWDxSKpoVxBoyutQkiTahG9OdzuXBwQpYIiuHLN3SQbVaeRV3+0zjQNhgiBU++ZSR6dwDFrL7tuLxcZTpGikjaEvj56o1ooueIsrRZ07sKhyZVwFXj0qrhrAIUrg0xctYi8VgdlfGOZnWuc90l0VHZ5eoh1JVOTPSscIOk87kBrqqwSVyDI0WNB/K8sh/fCE7kWIJVGwnVjcOce2yUVGiNOdxsO8LhhUQVibZJHztAwmKmg7gyhX96TEcdj/AamuN157ZEtqaMGWh3Ha8JwSRDiVrCciqm2040RH5AkDnan7rBNMvFeL9HcdJ1jbZzM/l6Z/Ol6s5XAEGt2PMlgAnCxSGKic3YceCKFWNhSiB0CMq06npaqiTKEK203JOSehiiGhg2mk7vRnHaKckjjOICHGvLccntINuHa8MIczqcI5M0pBWGRjz7Wb6SWHqHKvLDIbtwLqHyLCBGXjJNYEx59pS78JnXFS6tdt9xx0KzUiaBrdkqN6z1CndLdn/0VmTgbURuvjefvVoNRhcbStFMmPt/JAzwIe4SbDtK5CAfHCGABQ5bxztobh7bXWRc38iF3j/K49fnBREpYZOM7dy1Z4SgZkbDcKYHLI7ds7M5nrmJcwbKWy9435WNH0Nd76J3BNeHSpkZoWf5yM11rgssnEy9s7VpiNNkxOmpr5EESA7SLj1Bot4d5bj1a8RoZp2GjaYeVs7RXlXleduFyxMqVCpGsvqzOAjkpjK4bit4s/RO97LrOgU8m6XEjfzq6oZyNis+EYNDyMEoHAxPk3uL98WD2ZDhQIc8zURHZ5gq0gGfY0kReWCpRl9PqNCKIfL73VTdsj5tt2aln1aS7dOk5clMxOKlAS4mgQCPYxRoXFdW6yid3mYAYhZV0A6Z0c4qNbRvWJ2rFXtYqss2b+KjuhZBaSx1ogNby5GboSTtMGzcvDjhDslYqxZlO7HisWmpW5HPZ/Z7qqnFGTKrxeNs66ddJwbjCDlQibupi42MhpMhFTgtQUwR833t4KXQOi8sEsbUKzNzBypGvMDiigmPh8GaEMNfSC2V+K2k3dyu01uUQ2GvPvNoHLK5OKOFizfW09Wn7QLue4KNTDJD2Pgz9IK/OwHTr/XVJZDJcgeqVFOHUhcfBTeI1s5/USMMQOZ6mAMysBqmfHQlii8sxWCurlt4eL1GCuZ7Y8Bpyc07nQecvaUBrtDbeLK5E7zJ7JzTY4fZqBe3qfYeQEmYQG+dU9RfUgsAoF4FJz6fgXUAjkJNUkqFgTjTcUfPWjXt8exQcnzygxP20UVCB5jl5YByLCjbLEaYVGobvHXTnrEz2chkOyoDyZBFgNtGPZI1fL7pNy2IOaUyGVts8inAnHvWVxvdlCKG+SwT6mthe6mAaU0S8c2HpmOoOAj0x06Z36IoVyQVTr9PK7giH30/dFNQsiGGnQ5FtYamt4ogbpzTW5IHy8HAqZK9VrcA9srfTMBzZ06VrTrZq9Qdh2p9PHMdTqT/0ELmvR5BI2eTe1scVmqKaqARCkqZ2M51HCj3eWz/WgIMwNAdlHo+wu37ZbBPK7KwVaFCD5o7mVZCRNCpgK6n2D1x8FNlaEbfJRN2jDruawfZIKRxj512n4GA21WIxy+9X2ia8rPK3TGMkdaev5PAodP1dpAeytQdq03arq7wuvMFxTYIRBj7Cz9k9UYhbqqj1uGPtjUgfA8TKUkMoeSZZJjmPU6tV19yqWHby22ncpcQ5SQpkB9o6y47XAha3lC20igzhgp655o2MVsK0g/ph4H2OjMbqjlHVdrqvoOMGC4KeLYd01OIjyVfsxb/LkuYgvlXoAYnHG0hBfD4D+RQQziYzs2ZNWi4kDcNOPmtVsrrWJR0LSUmmYnvfXkqcvaEXaZRp1j5U2db0sFQO97psGXgnyXaPrm/ydLmcszZb2jRxi4NVuSon3zvbK3/crY7QCiDzwEDEaTO1quGRNWxT9+IMH20Lbqdtsik82z7SqevSlibUuu/gzhII4U8O6CAEoXbPmLjq8/DqD+h4p8Zm/gmP9ZC0SDx0w7RhACvwCAY7g5Wuyc3DZKmO6h2Ywi/NEEcqeUsuLWPb9HDr+UShJZumqcILtDzzFadaXi4GZWyD/jbdoAIkMUbsKnmSRie8DTnG7YsmnLAJToVaQ6ZAUq3GxjAoJLT+NAitM0gHO6KVKdDW2kRcLrUEoWF/0UPTrXJ6hYdrm9po0yFuphXWjM7S9JTwbjeJKYv7I6GrNxxWlkgTHrAmpwNF2RqBx5ySaWfc4lTNREPsux1A9Gi4dvca4W77oa/yy2WIxwSCL2uWI9fdRSR3xlLS7SskbW/XKPD56z7SkmRc80lSwmtto4+7bb/u4nGH5HpTnBSaWbmuqtGyYjnGTYL2SeDtmn2jWTYGoevKMRSUxVlDk68BaVzczt9vTqCRKw9LSGY9bMeJNTYKpA2zG8wlfGHbW0l/Kz3YX4PKOMBlFQW5jzimAVVqSstCSvbUMG7IM70xDn2jXKKh94bqEtEIqXYHwW1JYgT7j0YTyJflOs+uzkY+KffpylN+vswa/XhM770MRdaWHTRSu1Z3YspcdDSmQWf7GhY6utXoSDG3eiplCnQcGODFsF5BoG0n7vJRDHYrxjYjQgsHjwt1j4eNob6Na8yz+Yz1ueuwPYn29eYdR/lk0gVu9F448N2JRtSrBFfOvq+rCTC6RPhI4sT9Rl1hrcoMzZYSsTlxQrohxO2J2RE3SShdwYNoGA/Q6xSdSofWymO3Wtb8iCQRInfd0q0LifECANkQzF02ZRlS/oW+HDyLuDsZqWy1wTuTW5lwr0i63PGpTJ3WG/W4WZbhELWkgQ9jhlqKY/Akh4duXmPmycxIctUmNHugEtW8R0IcSXh+Rwq/LWhSxU9Fvzbv6OkceKIgqyaY/ERWbj0O2U7SKUMZdx2ZK+kSoarjDad90ZuSm5DeSpHdTQYnoKVpCcymGYBmhBCjglz6d8vll1pnQgd1DxVOvIfoNqCM4oLpKAkyrnRgc7IEMjilpEfIoTLAZnjssQ1WXk5siZF36Yb5itKR18NhKdVJX+edk8hURleEvCJzV1PgpKAacbnMO7Pl4AhqD4HV0PfucmydMily3hfhKt921C7cWA1Mk2dOcilfVHyYvzjl0osNrBrqxBwF/qSToU6pe5YxQ6e/aDKH3nhlzVdkKVLVqY3T1YnMMP3oH7313RpddsLOCXE5e2D+Zniehb3TmHrMdSORNC6SUdnKxEnHrh2obR0EE0uoZVe6v8I78l4te1eFjyukyPi02trk5A+go1LxAosv64M5Frqi30iGrkb7EK4aYegzDIZP/kELjyPbTgnNa2AUufYSMrI3tZfgnL3TmGhuWgPmk6LB76BLua9OMDuOISYQ+DlkmLf3b9/vjL79W54mm+/s/NtuIj3vBX19CORxi9C3vU8PXp/+PeL++v6tcWMg7PMGW5v14et21F/dXvvwrzwPMFMenw92fb1J/Lzx3dnh/Pz0W1x4fds145e2zB6PjoATTt/Oj1a289O3Lnj/8d7oj8qDr1Hc+F+6EqjegU9v86OP8zMhvhc/1+ev4etm5Ps37/W40heMwL/4TTUb4fWEAdAd+4h8BKb/P7kRky0ELwAA -->
