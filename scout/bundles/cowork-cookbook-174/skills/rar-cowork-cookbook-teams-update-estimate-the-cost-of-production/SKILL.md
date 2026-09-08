---
name: "rar-cowork-cookbook-teams-update-estimate-the-cost-of-production"
description: "Summarizes production cost estimates from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rather tha"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_estimate_the_cost_of_production", "rar_sha256": "14c01f7e5d40fde75da2457d4a4a9abff5846e784211a2a48e72314143b7ab08", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_estimate_the_cost_of_production`. The original RAPP
agent is preserved byte-for-byte in `teams_update_estimate_the_cost_of_production_agent.py` and in the RCI capsule.

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

Estimate the cost of production Teams Channel Update — Summarizes production cost estimates from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rather tha

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-estimate-the-cost-of-production-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_estimate_the_cost_of_production_agent.py` and embedded as the fenced Python below (sha256 14c01f7e5d40fde7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_estimate_the_cost_of_production_agent.py` first:

```bash
python3 teams_update_estimate_the_cost_of_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_estimate_the_cost_of_production_agent.py   # or on stdin
python3 teams_update_estimate_the_cost_of_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate the cost of production Teams Channel Update — Summarizes production cost estimates from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rather tha

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_estimate_the_cost_of_production',
    "version": '3.0.3',
    "display_name": 'Estimate the cost of production Teams Channel Update',
    "description": 'Summarizes production cost estimates from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rather tha',
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
        "upstream_slug": 'teams-update-estimate-the-cost-of-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '78ea31cea7f2bf23',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/estimate-the-cost-of-production'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-estimate-the-cost-of-production', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-estimate-the-cost-of-production-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of estimate the cost of production. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-estimate-the-cost-of-production-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads estimate the cost of production, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes production cost estimates from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rather tha', 'example_request': "Draft a Teams update on production cost estimates for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-estimate-the-cost-of-production-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams update on production cost estimate status from D365 ERP, with an Adaptive Card artifact they will post themselves.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateEstimateTheCostOfProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEstimateTheCostOfProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-estimate-the-cost-of-production-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateEstimateTheCostOfProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abPbxpLlX+HcjhjbTekCxEKC6ngRA2IhARIEiJ2wHDL2fV9Jj//7FMh7JfnZr2fcM5+Gkk0CqMo8mZV5MkuF317svovK5uXTi+LbxWJvZ1kc+c3CLrwFVY5lk4KvMnXAfwu3LLomdvqubNqXDy+e37pNXHVxWczT+zy3m/jut4uqKb3ene+DKW238Nsuzu0OPAmaMl/Qt8LOY7ddoGt8wf53hRIWQQk0LsJ48ItF5od2tvCLLu5uDxiN3/VN0YIBXmMH3UL17bxduJFdFH62qGYNVdaD58WC9GyAZ/AXlN14C14Rz4sgzvzFGHfR4ihx7UNg3cdu+tF+IgTmdGXRfli09uB7DySNP8T+uGjsbvZEF9nAWH+y8yrz25dPP//y4SUGv18+/fbiZnYLbr08IGmVB4xk3oxVI58C0MRA+uoNICazixCMr27A6fN15TdAYw5ueX6weLv6sfWz4MPi3/89He0mbH/69LlYvH0+v8x/5L4AsPxFV9ptB0C7dmU7cQYc9rogs9G+td85rQVrVoSvz5nfJJXV4h/zsx+fSl5Dv/vx80sJINgz1s8vPy2AKz6/NP38+3WWUv3402tWjn7z40/f5LS9k/huNwsDqF+/vF2/iQUDvw2Ng8UXRWKoN12N78aVD4R/Z9/8eUJ/E/fmki/PwT+W1YfFX0ue7fkHwPuMSgfI/WuxwAdg5strUsbFj286mhIEnl24/o8//SuxbuS7aRa33f+R3J+fgiPf9oC33lzy04fH8v2yWL7Z9lXmv1ZbgYD5O5aA4e/qvjrqX8l+rOw/ic7iAqTp+1r+pbi/mrD8x+Lnf2nbfzbhwyL4/EL7GcjZxnYy/9Pit0eI/PyD9+3mD7/8DkT/b8UoZd+4DwlfcruIA0A7X778/EP7uP3DLz//0FcgikGmfumb7K9k/pVfH3r+4MG3UT/+cS7QrxVpUY7F4msOLX4rq//W/P660O0s9r7dbz8tvs/E+bNczEa8K3264LtsbAHW7/z408vvgIMKYM2TWGYK+rd/Wwix25RtCShSccu+W4AFBlzkz+DVKG4X4O/MGoDe/KaNgWPfxoH4n1d4RlwGi1//h/vg/Y/uG+9D3cxuX/oHvX15J/MvQNSXmd6/lMGXb4z/6+sCMB+gjjiMC8DjMilJnws7BHw+668av/WbmWidW+d/BKn9cf6xiIvFr39HzZeHxNfq9uuD0eMnH8oUN3Nh22f+62y1EYF68rTRBdXBn3y3B8qy0gXI5sIAaB8AKjNQMbrZQ20aZ9nCiwHbgCL3Vn764tMs7Ndff3XsNvpcPMkbXTyrXwuBAV/hLD5+BCYGWRxG3efCd6Ny8cNvv/+w+J+L/2zWQ/isQwLl5G2NAMJH/QI51+dgGFg+sOCAUB5r9Nvvb44GYgpQpMCKxkHsPyeDmE19793ryoH8iODrheMDbwNP51XZdKAiLOLudcEFi694gdL50Vwzormoen7lF55fuLe5BgJzvnqyKDtQLru4DW4fFn3rP7T+6jT2A2IOkt/ufl0IlAQqVJmB/80wH4PA5LKIgfu/xsTzPhDS/NAudu8iXhfnOUoXld3YVdTYbzoC+7kuc7vwNh0ItxeFP34u5qLsz656pMzTPWAQ8Iz7tqQfH82AW4JOpfDad92PMfZcR9VHPW0+F+1bOtjNvBQuKA9AadjH3lwk/uMtpNqo7DPv4b9Hm+C/r4L3tiqPGHzvB57mz34tg+87pGc3Q711M88eYvG5R+AVtvj/uaeafUPu9zKzJ1WGXjBnVb4+12xuM+e1fXamM+JZwCM/vzU672T2zumfiywGAdjc/uM58gHxbcyTJ/sGQJFJ+SEfhBmAMct9ZMEc1U0z5w/A9V48PgDvPJgSWAQoA6TUHMnvCuen70gjwAvz9bdG4hE1wF3ANSDSF1XvZCAKA9/3HNtNAapmzuS3ZQYp4c9RMUaxG/3BqnnJQOQB+QsAIga5CQrM61dCfz59h/6Hic9+aZ7y6CV7kMjNQwDA4c8A50WblxDA655dPbDz00MIMCOvutl2B6QSsPR50298sMpt3M20+fSrXwH6/jh/Py2d7/pTBbIHOAvkSNUD7z6yaiacHHRDAAMgFpBkeVyA7gA45c0JD4F2PlMEoOC3+HxKfNx+M8h/pOJc1t4nzobMc+ZO4ZkMdnH7nknUvwoTIC+fRzz0/nOkfdU2y57ZtAWMCDS+P322FK/PruDZdize5X7607bpx7+3s3rUee2PAfBpEXVd1X6CoGdtfi/Nr4DLoCfW9lmmPz7r58d3fvgI8H6cGeNjGXz8RiJ/0PE0/9Pi7+H8g4i3PPm0WL3Cr/D86PQWZ28f4Bbq4+76EZuffi5k/xvrAvUlgDpXhewG+oKvJfJ9CKiTYQMYDAx+lsx2rrQjKO6PGgEs/Fx8H/hz4s1UFs6B2pbfEcKjVwBJ8FzAr6UMPCo6oNubO87Qf503ajP81n/5VPRZ9uEFsKv/d/Z5c93K5zBv520i8Dvo5LrYf1yBfPW+zHCeQn/7p420+EibxfuAr0H3Zx7+sPBfw9fF31n3jwiMrD/C+EcE+zjjeE1aUCoB4O5WzQY+N4tze/ngtqn7C3yPH3b2uqB9wKNZ+33CvNXEuSf4Lq+fawLWwgV++LDwHnULmAVsnF00c4LdgiQDpv4llkf5+vIsX38GRM817w8VDtB03QOeeHOQpgjsX8r92l//WagBWphZjld+mqv5hzdSBN9gT/Rh8XV7A6x523DOGvyiB3v5n+et1RwEjynzDzAHfH2d9PUfTxz/5Zc/4QLAHkwL6tUs6xvIb0PLx5ZsNgGI7p7/gvDbCwg4G/jWfgu5t54eDAfE9LGdexYIpCdQDq6fiQSe/V91+2+y2sgGHSYQtsJceBVsfNzD4MDzN7hnIxi+8TAbs7e2EwQ4ga39DYEhq5WN2BjhbxB0ha0w1NnYDkwAec/U/DI3afGMbwYH3PIRZLf/7TG45b0Z9jRk9trXzcXsgDf7fntx1hgYecBajnx+KGi7ciD05Nz4w7KAiSlaXbzb9cIM5hXp7ZOkI91pWznDtYaORI7XCnLYXZAddw01CiGZMNf31TFcyjxxU3Gx9/cySV60AlllGLLG+RNP0yq8FaBhiVm+haE+m2uEbhtKdXF499geGQNhmkIs47LFbqO+wU2X7fmU25413j850vE4QVDioISOd97qeAi2OuuikcqwVl7q17UxNmrhV6hgRZwFvKkN0zqBJHW75nTbZllxwJRaizWjtyjeMFwnVYUSYfTcyOCRo7l4ZVaGFnXUPe2Yo68fQNfa+/Kd6S6M4inykofumy1+XFlT2corc79hIBzZnqokTFaaa6brDDN3VmYYBhud5RvV6oLi2aZr1kYe8nsj5C4htr9voOWyQ08NvoQCNK3NBt9CS3xjbqZiaV+y/c64HRPf4gscxHjOj9ZGwFVeXO/yZapSzUCFK2NHpITOnwazq3cJD3lhuL/s1/ougoai2SZEwovjRZQTrQsGCt8ZYnstK4VutHvCGpdNaCh9RuHlGU4NM+eR3DNPsD4ccPhq7KFS3GkHRQhhfRtVObMzGaGl73ZVMKUeVqyyynwy9y8UG29ty6rbUGsSb+r3oC1ZKZkHy07I7bHpCDWrHSGgndTf6eHgIq2tl/hdls9aW9XcsUQ0vM/Ci8w2FVUpKEMZ1XUd8cg03hOVhO7XwfbOJ8oTbYTzjsd1jMR7tmJunZRpS7O/FVs8RpULpE06wvCcoeu57l7WQyeMKa12XnKMpVBOlVpHW6tKBDfa4Gv+psDwqZKYva+EQV6jZUtf1JKMsOnASBhiKkh8PenLXIRY6rLWQ3vfCfW+1cuTkZHOlK7Wmzq7RjBT+2bkRakhgBhw+GM01jd2eXSlsTp4Ci62fSeYS970moIJ7sxaR6lrQ7CByloie+ro2366EnzaTzWNO/qQuBumum1u1ztyjdTx3kk0JHSJRNs009z0vGBdn68vLaPdyU3lkeNdd9TAkctTvkekyA+m3FDDwuD7IKGC5QUaqxYynP4G3SglXeanzdqHJmLYiRvdcGmZ98p9JqCklS5x5NqkqmwnyUBNuZOG4Qrpz0fO3C3JKGIP62WIBOFW1g40rZdGUuAsbDRnK8tS1XSLxqLZHIJ3+ZmH16O209cZb9kiIxTwfmhghg8PF590pTBhBJS5l8wKk514N5rRHTNyC1+dcwu7ev4k3Q81a2A+Oh7XYlLroqJpU8juBGy6qKGk0OzunNYI1eU2l1mpfNzyE10zkEsAyiBSZyBPwRVXbCWvrjdso9YQ3qhxl09tYQYbxXN6vPJupkEjk7oTy7FCurE/no65gLXyaMgmx2n6bhnepxxfWyRTB3nugCU/WrtczzN3KWGVSpXXKhYxZdlsmJNyX97ckAi3MF0Fp3h0OO06EBs4SRwjZ8U7ZAjZUSX2lj1hxBg6yK1hmbtPjpvMkG1aOW6boExs2aRYp6LYG5Wg6BCfnOK2yphrsOdUeLOlg7hh8NUwRCGBkJcpoFkiFDXqGGj9xUIjIuWdodcKueztMusu105VbudhjaLpSDbqMRingZSrveLv8eZ4TLFIua7VRPczp0MMaQdJ++QKWyuWYe9bqFFSFNkQd4zj1kLJ1r1Ejy4+3abrHd5yt96DBXLDFdk9rc6SRql63ltbpUgG3lShZbVUFbM27fQygGA8X64jTsXCPZv0NRqJZ39novYlDkNdFo8RsoavSW6XyQUS8NS5BPSV1gp+eWK34/EUs/sp9eqUTLNoChV9B4zd3yhZNqbeWa2h7QhjHR8dFZ+cuPU5uloHuSL7PUVSFnfWd9Ld2ItZYlTAey7HH7Kdw7dXpT/R9k4BWbDJpKu/K7NbfSOJIzIu4dU+thGt39ZVQELyWKZ7PyJAcm/2685Qtjoc7mq8o/ib14lT1KW3G369jzAI3Abe+kOygpQLyx1HtdmT7LRFM0283I/JKredC1Fuz2ECKoaIHhIoGk+G1/VjiNoCd5XWGEpUS185aUIKNRE26NjWWzWKOtBVSRA3idfbyyWaUmXDkOjppig2U8Kt3ejyZFDKKYVosuVXO9WxiF3P16dupDv/JHZKWqukefA5Lmi7Eq+MHUpVYxJpYxPxqX7pwgjepZp4dLqLXcUG4ilZlOoJezTCIWXuUIOj931uHPF2bw2gT+H4lTJejZ693Dac4mImzvXuwK+mumpMhzjsctNEdWy5UTiy5NiIjdwpzSh/A1tRt3NAgbhZEQ+4r+C5JJx8ZYIRDRMMKI4Ejr+PzRLbyw03cjUZhXxaKeF4Ecx2neMeqm2YgyLH16E44DRmUyvS2vfCFJDeiDpc7dPqjkOCZFju653FtaSRI7JOZAZTk3q+iwmlMZi9wI3ohaQCTdY1Qc14oa9uWBPRBxLj5VhfH3K+GWIcLRNlTSFwaTieNvlkemLPDiVP6+UuF3Sw1QxrWvWNQzfGF+J0wkb5smxubZmEqjD6idVzhCzuaI7mV80R2TR3zxoj5nwvR/ZEaaLPqe0WNTGtzRVGFJVLYjlhB98xp71AO0/lpzJmEbztayibVLpTtYkWkJ0Y1rWoE0Jc2oEzGiRZFqJvg3qjIRrMcGuuQ/NcgfbUIUEKfpRWgq5yB2QbtmUGXGgMQqpm2apOkj1/lKPDhgqEtc3oNX/lyJ2yPcY4U01jtlOFi6FcYcFuxkCBtmXMEInGBZeGEE0n5vY9B10zmvGzFY2crCOPsF5Qn/xl395iNJDXU8iJ98Ou63rkhBPHPCWT1BTZrYP7kVqIyQiBcFuTc7JvpVMxgrEDIctHr5ykdlJZ49CeLZGMzveqXFH2ySFTMYUv6/ukcVpNMMtBlkerXNtCt2Z0xggTvT5vSW0F41EKuYc7qekeLFakInvqSaoOyua4PvMM0pz3cQWhukrcqvOuZZIOZVAe2wtkzxpXe5dCMJIqbYaPSmIFw71U+P05XIvGisE2xFST+x1TjRqBVvcuPqvnG0cKcayNJ0455nwF1eH1gg5jfkJ6ShNM97zUoACibdkyjDsP5+tdsaslQepox1nxqzo9nHCI5LPVndXJ4yXg6PxID302VbdjYEL3KctCUMdaiyOzbbNieyM0Koa/RLWpsff7KV8dM7mqbsrlWnE9aVBMUcIri3C6w9bGRGqr8Jq0sVl8qWC1LR3u6HKEVDnbSocBh5RbOXU+Kxi5Sh5MvjhNO7/YDSSCrDgykPX64Kt8n3c5FefkTaaU/Bpza1QfEwUl60tXd0QRtzXlESzvVt3Qyst+OjlW7WEyqsYyEm2X/oAWmTbxsJkeKWEyVpq2b6r8CjjDnDJtrKktFbFofFpd+xW7r5Zs1ANOZju6BzV52V20elTruMZ7LVCELLZAD53xvpychuwylI52qzKK2ZH3Xl2t9NodGypHVE4OrxGDnZcrJ6bcs4fdtIPOSckR3VIIalvKNsbcjTtZjn+kpytUEVbur3n52gOaZyF0uqaGctKNGp7U9Rrs1UqEdzgvP1qNYGWIbmsrXA8oaXuf9MJFW3SqBZlyC64HUQznyLAblNSG10jbJw5dWteLJhRXY2tG9pEq/Uuu42DvUfPEjqOu1AUR1Ea9niArYLWEdxIORypMg5ClwuBEovPZoXIYZB9ywhiXGbprbtZhuVrFMoPxqDkdGgVXGVTyb8dcShtuHW1oAcbGsNwxzA03rzu86Ogoajhc0CXuuraIK+Ht8qEl8QOlyC4V7vPctcWx1UC7VA/XED2wAsox5S72pnR/cXftoGFaAxOnzYk/koSm4TzbQojLXNhalPGkDaEidtaCtCvkY2qcJN7lrDtaFUgBw46/pLu+RFYBJtW7rXBlLsK0v4DlitMO5209No8gkki1OG5AAkm9Hwhdf/OZiRPJMxInNCxSt3OLGj7CQL0VD/ZG5a+rLeijNURUN45AslgnhyWt8xdv4gSi1upkW+enNe7slqrHFvax8fre3UBnEw2o/HZDEL/mSKoyuK1fB0LSXIS9R2T+Zkqg9U4k3HafjBuaQbi9QQueEfsnBbJ1kTNx1nbaDZNsQys15N1o275en1Jhw0tb1hXMaYVZUreUr6TI1GtV59eDrGDTEEbeOoAZJvBQIsPkNPSs7LZ2A/Gig+3Etj7Y7cRqhoiew+i8bHRTvt+UVYgnaX0RM33Q9FVw7LNUbrADezrL6ZKWgguMNuE0XYJSm9o6NqSRDHfXzDUqzc7OJX7cGLJL5DJjxG6cdyrlSPld3KviZkf5ZkmJ5vIu1v1KPJfm/XQ9bpNRipjpLNV5Y5gDeYQsD2LwYBI9dTjjN5Cl/hkeGswVsAO5FjMPQxv35BYX01Dgu93c+8IX0PtUDsgN1lGrH4QmESfCxjYJ3HpiPg4ASrQ1+zpYZqWAnM8+LtHM9eJkyuZ88XbRGMinWIv7lPZ1aTP0Qw1iVuKLpmHXvZhrpkpEYnC5NMgQS20FVfWVjxnTKkjM5Ic2odlLzawO5s2Lzcbi8b2lGwix7NpT26LD9Zolq00iRUTr4eQK4xwBgVAzi6LlPmm71d0V2Tto2VwaQQpi2kIQeDJpWiYuEz6AbqvlPjycp1xypM2NyIrKO5Oc43tllkaFcnPj+xVjOYm5plthDydBqtZtc1lDF7fXrYPKSYpc2liyZJJ0d1Mbc/ARytvi9XmyVzUhJFKxu5WIcaaIg3nxO0CNuygNqMTctNWI5qJEXLCbdV5OGFosi9wJJ8nVxTJr3LQ8pNSVJiA08Tzd93PiUtkoc4qWbNXByN4RQ4zPcwJuY/1OqGyZQuuuO1dIevevHaaz42qzTe8a2H1phyMcVLi59gM96frDqSA3GxknBYVnCF+Ku/Nyc7yX0xBzKXXRu0Zy+WO9OzNtfpKag951zoixxxLs7+RwfYFt5M4kCNRONTSKNzRKMcrLt93klCdlbRwyCt3vDg0ls8eES9lSSGACKmEKqTvyuCsSVjhtNqvpgkRS2qLnMiDVHRKl64Nx40sqhEXmPLDslZCulL7dCxWHdRVKj+dcrfTA3/tMB3ZslrmuDsmEQdsCDYIjHQ7YXb0d1B0oBehoJPL6xhrdphdFKwkw4yCfZTMfltnllOkwbIVesGS29DJrI2Mr5JFFXFDXvMZsf4mHohXZ2KoV1KCVc9usJbekCY9M7nYpFD68Sl0j7sONJThZc49SBJYjtvDOmnUVtxR2RjBufevJaCniSanq2w0PhVhbYI1gY2in3gOyOPvWuSvR7bLlExOH8qWxtSWrSHO4cqOoLoTdJJ6qcm8227YNBPNCxneGQE3RPx9cgbrtoO1hw2EHT2emXtpJV/x2PDambV+WSNxQzYGkfWxXbZbQ/SoKB3hbokIfrDrRWeXJUPRGb5S5EOBDEa2oTXHIVsDgAsd6OhZQ3649aecY9nJtROINx27OHm0GZ11wyzVEGe2wvwx1mOf0cOkhBSNOplWdWMRgzb1lHthzSJuxzQbW0ekl2zlu9YNmC/saW9HRNhHDoRFN3z2LWOkhmH4gdHnTNnR183Cwg3HT4sg1lMdvr87Kaa1ViOw0PBPu6zumacH95nKM3h7Ta9JmpjbJVTGmwS5nt4CDa1YUJY4zRLEglOsxlkHtVfKNhadx5OHrUyWpSaxI9f1EX8VJJZrzFs7avjtHTbC5HrOzDrbrHoXlxBpCjoPVbwTG70PAhqe9E6OtwlmmkJ7h8/K431vaUpC06WBVytbT6Gra+Oh6GaBy1xl45ttwKYJMMjYnacsgWyG0PMJmfNxZa/bxvPHOCFHdpuFkKF2L4HntDWvZOCoI2OzhUa5IG6JLBKMUbT4R/O0NFmhxs8pVJ1kdxGWWJrlfQnabqe6aG7YX5XIsMUtI2lOwG6yOXG23O0lF4tZQoGTcrc70Ld8pBDuWxLGvS20g6N6GTycZYSyIFjnbm6ZzLUgHK1uveo9YnnvJg1VL21QOeivxO3ro0Aq/nVYbloQd6J5lOGjnZVjOY9ogt8whDxniulcVezkEQ7A0t3nQbLcnT/VIqNtll95oXWq37fpTp+GrU7bpLRMdTjGskbZ0Wg5Zn3q0d8MruhD88pyYlZrRKRtrG3I8nbFRMBRxuWcrM4dE0yq3PebcuPtlK/SFIRnZZhO0Jr07EYliTNEebEHxfIILvbXpjYJLRU8ZEyJdLltuLypGNO25ndh6DHy4q5LVky4VGZhgRojieAUgmszbi9YSJfjsGK2hCT3QhucMfnjABI+WHfpgSFgnUusEbqCTclzmm/i43MLBdM5NVEMcLPHKDWSQwbQdhpsngS4HdogJk65R0C8peSnll/GYF+q9XhVOZWkNq3kIzCaeBUWE3Q+dyBd7OBgxyEZEz0r0ZudgwYZCkSPqOqul1VscjldBjNp65Eh7e4fst5A/0vSGzgLE7LJMwU3T7TzYiZQrh6lLPpFSmyRXxxWxr12+Co8xwV7Mi7lWTE+qxqt46nObsAmW2pWbxGyjQkBCJ6VtsGmiIyVIuXg/5fgKv00oLZMOupzycTP26MaDkNPWpi9XdLrfN4l68teZr94qlDlUNoeaPR7sTKW4czLbu4rP9mVUWfBOpUPYjFDzPEKn4XQTlrQbeiI3qCbRUSboCkUSpuq7ugS+lMk1QSYH2DyJzaqIcvRwgZaU7xzNRFhdLiT58uHl25Hjy3/pVav59OX/2UHP87zm/XWJx5mZb3ufHro+/dfg/fLhpXHjGdzjkKvN+vDtiOifjrg+/p0T01nS7flW0/uJ6PNIuLPD+W3gl7jw+rZrbl/aMuvfZjh9O7832M44XfD9/WHg98a9nQ1+6co3i+Y7cTG/HuF78XPAfBm+nQB+ePHeXvT5gq7xL35TzVa/Hb4DY9FX+BV9+f1/AY35qb7WLQAA -->
