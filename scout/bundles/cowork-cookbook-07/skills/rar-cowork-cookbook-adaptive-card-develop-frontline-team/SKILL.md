---
name: "rar-cowork-cookbook-adaptive-card-develop-frontline-team"
description: "Generates a read-only Adaptive Card JSON file visualizing develop frontline team status from Dynamics 365 F&SCM (legal entity USMF) with a header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_frontline_team", "rar_sha256": "e2922b37983ad758fc4d30d0b1e7f3e9c4362b53779d1c09a25184180a0ed3c4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_frontline_team`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_frontline_team_agent.py` and in the RCI capsule.

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

Develop frontline team Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop frontline team status from Dynamics 365 F&SCM (legal entity USMF) with a header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to read from, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce, saved to Documents/Cowork/output/.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date used in the card timestamp and output filename, e.g. 2026-05-24.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_frontline_team_agent.py` and embedded as the fenced Python below (sha256 e2922b37983ad758…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_frontline_team_agent.py` first:

```bash
python3 adaptive_card_develop_frontline_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_frontline_team_agent.py   # or on stdin
python3 adaptive_card_develop_frontline_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop frontline team Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop frontline team status from Dynamics 365 F&SCM (legal entity USMF) with a header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_frontline_team',
    "version": '3.0.2',
    "display_name": 'Develop frontline team Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing develop frontline team status from Dynamics 365 F&SCM (legal entity USMF) with a header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-frontline-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-frontline-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c53e5fd3aacb89bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-frontline-team'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-develop-frontline-team', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, saved to Documents/Cowork/output/.', 'snapshot_date': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop frontline team status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-frontline-team-2026-05-24-card.json' that visualizes the current state of develop frontline team. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop frontline team KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing develop frontline team status from Dynamics 365 F&SCM (legal entity USMF) with a header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card JSON of develop frontline team status from D365 USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card snapshot of develop frontline team status pulled from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopFrontlineTeam(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopFrontlineTeam'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, saved to Documents/Cowork/output/.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopFrontlineTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916a9Ob1pbmX9G8XTVxGtuAECC561SNAIEQCCGEBCJOOdzv9zvp/PfZSLKdnPbpOWdqPo3sRAL2Xvf1rLW8+f3NbJsgr94+vV1cM1twZpKEgVstzMxZ0HmfVzH4ymML/Lew86ypQqtt8qp+e//muLVdhUUT5hnYzrmZW5mNWy/MReWazoc8S8bF1jHBgs5d0GblLA6Xk7TwwsRddGHdmkk4hZm/cNzOTfJi4VWAfhJm7qJxzXRRN2bT1vPddMGMmZmGdr3ACHzB/s8LfVy8S1zfTBZu1oTNuLhejuzPiz5sAsA+AOzd6v0C+4AvBJlfNIBj/R48ULbcosr79w/tlh+whWnP0i+ASk2e1R+BUu5gpgVY/vbpl1/fv4Xg99un39/sxKzBrbev6szaME+x2a9Sq0BoQCAxMx+sLEZg1gxcF27l5VUKbjmut3hdvavdxHu/+Pd/j3uz8uufP33OFq/P57f5j9JmiyYAlsjNunGdhW0WphUmQNWPi23Sm2MNjNy0VTabuwZeyfyPz53fKQGT/m1+9u7J5KPvNu8+v+XF7Cag9ee3nxd5BfhV7fz740ylePfzxyTv3erdz9/p1K0VuXYzEwNSf/zyun6RBQu/Lw29xZeLvKNfvCrXDgsXEP+TfvPnKfqL3MskX56L3+XF+8WPKc/6/A3I+4w7C9D9MVlgA7Dz7WOUh9m7F48q79zMzGz33c//iKwduHachHXzT9H95Un4GWrvXib5+f3Dfb8uoJdu32j+Y7YFCJh/RROw/Cu7b4b6R7Qfnv070nOo1t98+UNyP9oA/W3xyz/U7b/b8H7hfX5j3ARkTWVaiftp8fsjRH75yfl+86df/wCk/49kLnlb2Q8KX1IzCz23br58+eWn+nH7p19/+aktQBSDPPzSVsmPaP7Irg8+f7Hga9W7v+4F/K9ZnOV9tviWQ4vf8+J/VH98XNwAmDnf79efFn/OxPkDLWYlvjJ9muBP2VgDWf9kx5/f/gDokwFt2gdEzeDzb/+2OIZ2lde51ywudt42C+DgJkzdWXg1COsF+DujRgWgqapDYNjXOhD/s4dniXNv8dv/sh/I/sF+ITtsvnDtiw2A7csLkL98A+QvMyD/9nGhAtp5FfphBpBX2cry58z0AQLPfIvKrd2qA1hljY37AaT0h/nHIswWv/0z5L88KH0sxt8e6Bw+8U+h+Rn76jZxP85aaoGbvXSyQblyB9duAZMkt4FE3hPngSB5AkpOM1ukjsMkWTghQBdQtsYHbWC1TzOx3377zTLr4HP2BGts8axnNQwWfBNn8eEDUM1LQj9oPmeuHeSLn37/46fFfy7+u10P4jMPGRSOl0+AhI8CCHKsTcEy4C7gYAAgD5/8/sfLwIAMqKQL4MHQC93nZmCl2HW+Wvuy335Y4sTCcoGVgYXTIq+auZKGzccF7y2+yQuYzo/mGhHkdQMqbeFmjpvZI6BqAnW+WTLLm0UNArH2xveLtnYfXH+zKvMhYgqS3Wx+WxxpGVSkPAH/m8V8LAKb8ywE5v8WC8/7gEj1U72gvpL4uJDmqFwUZmUWQWW+eHjm0y+gEn3dDoibi8ztP2dz+XVnUz1S5Gkef+4zQvvl0g+PbsLOU4AHTv2Vt//qRZyF+qif1eesfoW/Wc2usEE5AEz9NnTmovAfr5Cqg7xNnIf9gKQzpZcXnJdXHjHI/LhfuTz7lb92PJ/bJYKuFv8/NEez6luOU3bcVt0xi52kKvenS+a+cHbds5WcOYK4fKbf977lKzZ9hejPWRKC+KrG/3iufGj+WvOEvbYCdle2yoM+iCLgkpnuI8jnoK2qOT3Mz9nXWjBr8QA+IDVABJAxc6B+ZTg//SppANJ+vv7eFzyCAngBKA8CeVG0VgKCzHNdxzLtGEg1u+2rO0HEu3PS9kFoB3/RajY5CCxAfwGECEHqgXrx8Rs+P59+Ff0vG5/tz7zl0Rq2IE+rBwEghzsLOLtl9iEQr3m24UDPTw8iQI20aGbdLZApQNPnTbdyyzasw2Z28NOubgFQ+cP8/dR0vusOBUgOYCyQAkULrPtImjn4UhAqQAYQhCCH0jADxR4Y5WWEB0EznREAIOyrG31SfNx+KeQ+Mm2uUl83zorMe+bC/4xgMxv/DBTqj8IE0EvnFQ++fx9p37jNtGewrAHgAY5fnz47hI/PIv/sIhZf6X76L3POu39tFHqU7etfA+DTImiaov4Ew89S+7XSfgRQBT9lrb9V3Q9zWfzwyvQP3zL9Q/PQ/0+0n2p/Wvxr8v2FxCs/Pi3Qj8hHZH4kvuLr9QHmoD9Q9w+r+ennTHG/gylgn6cgwGbnjaDMf6t8X5eA8udXAHnA4mclrOcC2oOa/YB+4InP2Z8Dfk44UFkyfw7QOv8TEDxaABD8T8d9q1DgEbDNCMAf0PPdeWB7pEftvn3K2iR5/wag0P3nBrW5EKVzYNfzhAdSCLRiTeg+rh44MTTzz79OuafHDzP5uGBcgElJ/efge5WPuXz+KUeeegL9bMDh/cJ5lAEQl0DPmfmcX2YNAhbE6qxPMxazAs+Zbu4CH1D+5Qnl/1Ug5jvo/wXz5wo9I9acX+8X7kf/46MM/JDDtyb0v5LXQN2faTn5p7kEvn9BDfgGg8P7xbcZAOj1msoeQ3TWgoH3l3n+mA392DL/AHvA17dN3/4NwXLffv2RXA88+jIHxNOtfy+dNOMMwOHZzP+omALhgQBOawPb12b3rAlMbj9bMPiZOPCTFfxD89QZaECDvPkyu+4HHgB3Z59/61nnbH4AHijS6QNnX8i6+KrJyyFLZEl8QPAPy9UP+ALGD/gGRXA25XcffbdU/hjbZhGBZZvnvzL8/gZiGgBLY76i+tX3g+UA7T7Uc58Dg9wHDMH1M0vBs/+rieBFow5M0I0CIu5ys1xaGLlZY6ZD4mvPXjkY4iAW6pIe5m7sFUYsLRwjyY2D2sgGbEPXK3SNmIjrYPYK0Hvm+5e5oQtnuWahgDk+AMhwvz8Gt5yXQk8FZmt9G0BmxV96/f5mESuwcr+q+e3zQ8Mb1II10hoLHdaR9TD2fFUaWi5xqaBr2tTyqUOd4mWo7QGGBj11v4fKIHSCIejnTaVwvkXs9hgt1xk0FbHh5emYiWrRRE5/51P7pMupJ0+nYdU7w5DaY1obBZ7ccS25DOwuVC77TWX5OSwcrqtYzw3khoi2dshWXlhhMBRifrTDMzK4qTRLZki/TM1B7E6ttHG8vd/dkl096Fp8iaATHDkCGoq1jmRF4lGIgOBYaEHSNtRcWDYLV8Y6dvS6gQ41c1prxzAN76ELdViEueHQ5qnA4Kpz19u7utZU4iZP8vLWKPfdFe3v3cQuN7usIf37IAjD5pj1PiQIO2xXh6Mgsfv2LjPhZHTTbblxvf2ACgmxgbEI8scassoz31O+tstww5IEG03apL34y1gRqAzOREEwMog1fPuQFltfvDPtIU+9DieL2B2lenmeaJ/h8zEZ2fsp9Ua5M53jJs3to25tc3WS6UPBVAa0K5exkPp7dDrow56zqcS966Z6sztVW1fZgN5NyMASQlSOMH1RrrtSPW+ZO9TL0shdXUrbxYbYYT4djcqQhNLlXOFgtBvqVUqrWg0fTsVaIc8sx/sCLBYHXhTkhuk2UyfaaW7ecmS6UFTaHcrDMadalwnucX21BP6ISLAg8jzk0xzeT4xHw9O5MjcS3/HpoMj4BYeF9HhjL+dbdV0bquGQpYWkpMMzkJ6p2zsbHC6acjPoktqo+nCLbba9U1O4XSnXEUOMQ3C0KRInDtCtyTF+E9nblXPQirOs3izfQsN6SfHrUA2ztUVeluF9cm6y0x4SptDo3ESWuYnffMnUqI6+6FZb3kLxsub96qDei1sldbdblfp3tQ6syI/Wh0t2b9UNbUkVvK26WxV2Q+BcmLVirSmv4fd+qB0w+hBL9ERKqOIj3XJTefRqqRhcAWm9tj6q22l/YhymUyOhNKxh2NBBzRdrMynwm6iu0yQlVBAqXjiSQXWN6PZIubATQHgEM+lmbboTA/GrVCXWuVdYMDXaNKlTxYbWosrpC5w3pnbAtvENZ1mtPMTOqssq54wjvUatA4q+phDm7/RQUq4x4xMGGqNrlps2RjylZXPatw21HB0B6bhdein429ndagW5O/Oue6sIaUdh/mo9TSWBr7JslRnbFKOuNc8Fp70c4HtCU43U4XSrVmWFXAnibgmxmBY5aokPAq+sioE5CutLybrC5Zxf2FDZJUgW0/cIwqYjezDI03rdrn194C9CIKkXyVVgJtnTVry0jiesHFfTfQrhdWOL9bjkrgGtH03XLSTOQjiE3NlsXFosXzDj9r5i7A2CBXyGgqH77Ah44/YeseFzt70zfOsqfhxk2z4KpQHSERkycuxMH0emZ0bDWJ/Y+wXbQnvNJJfBFKnxjZggRctL54ZcLtR5Gy8P90PW+FQk0fjtgB+rNJXDNUjRPN7G2zO/g1UbupNHMJggN0XJdUw+IizE12NBtK6g0hrqcse9FMZQz8CBlbW6b0Ww29Mnr7ZgGurHQdSCoeHC3arqOcrs+8wWb37YnjeldEfQUbsqw6XZdpPJaqshlI3U5tabhGro4Oav5GzfHS4qVCAuiWgBm6jiZeWRK2LsnMuYG8uLMUxqv8+oVq3EcX1T7CrN3PNAk8maGRxrHQvyuUWArkrnpfxuZSUHU6G80N0g50iLbxsu3tuHQVPp3FlKPGUwOTfiU9Uv4164ZYeRT0iIF2meE1IpWzZXHAeJK6RTUu1PlCOcJ7dzliuondrNUQuVTcEqphRLSVw0BwmHgv3uPmTXFX0lbpS7bs1yK+2K7bjngx6P60CMUXxbiKyxGZL65CdRebPBiq72CukS0dVad2+7ypeQWhCoLrclz4QGt0pi+dL5WFNtsXaMjbM7GUbfGrgaTnsS3rTqDVo1OsWE+MSK9W4djc7tclBaFlYLCWkRNxh6nOlgKnOqicx7scRUvc55pCAPuJytw6yE6QPZeyIMR3JxR0OjOKhbVZdhduyp8/7Cs93o6cy0zKHbgbtIt7LOBe7or7LeC9JTXloHmUEnadC7GNPDSTy3QhTgAxbSeq/ZEZcY1Ca4nOWLzqMpR/H5RS9QJo5pQQjPlsoXmGmKVM4IKm8vGXval4V31zfXiLlPZ2JFrsTbpbKSpekPpCCKNYWrJCOONXLPS7yH1qta6twiIFJ2u01yoU4k/apMKpwS+61zuVm5bfvH83mVZGOTdHjQCGGtCFBHYaV7hC9BkK+DQ3VGhnRndBsocAZpYJCYT8W+gP17dNZyRtRYihoI2cDy9Smy9bmw72EKPWtjsxXZ/mahN21ko/GsnsxhtXe1Mt2avdxikIxr+Z0IytRk6nrFjtpZqGLxnlIsJUyZzg9HWBrCzU7ctqLgtry+5XbodnnZ547Hr483C9HrBEn7o6f40JiGGmWxlz3ShZFwvEbcBDnsUd8qW4mgpSpyJE8fp4t24kTdr9mIvnLSNd8RcIWbOkIjeZKsVLHagzgiyuu2o7siuSMKTQKBAncEvUSF2QpzRXXq4p6SxJP48rZzVjK13amZzNq6K+alKZwbvilS80bwCazmlIoY4xGilAO1SlZGIkpQNrj1FZHrckL3yyOtNeG+orudkF4FYocTu165xD2SXqfifFXrqx7z+dFEl3Kx79HBPKsl1ZUovDmchi1DAsdchvQUKQ0mpHxIaPFhs5HQG9cSqTQdtVpw9zhWWVXmB+qh58/2Sht3Lrm9XWsOwvYI7VMHFw5JST8U5ml/WjXZVTwkumQfSfV6NnLPjgVKSaczUqiH4y7akfFI8fIZyxFEZwUjTUS3YQMu3qJlROd0uiTtXUr2xJ0eKy7IiBMp0XSyygKbZU+cqmlZpIeQOHZst2O2ydrprKycICoYuW1gNGfr6EjVbmLBjJUjerH06DtyXzI5LppySeGImR969rAsXMvGEbUsua3KH/zgEGwPehptzvdlLu9RsUwHNqI8RV7CCJSZN6odHUpiD2ShcOoydHDoclIKJsnbfnRsO7gpegyPZ7vgeItyzdpHkQhyj2txrUqVGRiXXSaAXmG7O8RxqRwvtESMfKsVzkXp7/CGtNPsFPbqpsN74NM92YU3zlUn6y4dy/wSnE/h1bndkOR6OFbX7X6H7kbm2hs8LfVGfG1Mae2YN16sewwlkJRoKKIgr05zLUyf7jBy7kxigTBxt9JFFGPzYl+H0pVnRND5qD5dq5fczK0DzXn1dtoWsNA5RjfERwU0FPqK0zQlEa3+WDoxsvEhc9VpeRVJe/W0qy8YRnADKJLxNDEbaCOHGII4crHawCuUjxsT55DGQ5vGiErokEo3HV1XVy9ZTzsOGiT7sj65iZwkWW/LocPte3Y3impwmnbjcM/O2vmA5JElsnwfRortNzmBG8YxRemYQDLYhy87sSB7eZ8Pq/xYrPGztzvvp4gcVGPYYY6OTAKpHEoDygxZgtVdl8AOdbfYPGXd1TFsUTqyOM7xaD3enzlccZetcISgA4n0pWOUkZ5Bade29xIejiSrMcZxZcq1XOZl1hj78ciiBrGnIg29p6R/S6pySYFxZOz2q8mudevAR+LuEHZL9MAZLBu0eXgjMDBr6KWt32+SDoO+SFIukVFVYnDHmgO9vYb3w5ksu8a8yadNqEn3swIAjCF5PrrW68suJUgVca9Hvqsuh/wG6j1399alVktn36gLw0CuQSnfomZ59aNGz5KeqRF0M3JK2BN0WylsFh8nx+i5qyIYlUtDmFUHmJOmBt9vLigr+ecJiljBSu6GevOcg4dx2Opiuk0X+3FGWdtJlE+uVq8r/b7cLk+E4G2jeKcwsrS14+U1Pw+IT0NFzF5CpSq4Mc7WUtlfvHY91I18x3GHd+Nq3RuOM0eVDDJf3PmEz7oDV8CrJka3mplwqX+IE2oY4oJk9qZR3syuQDQRSXkqK+vKKcktDks56mzT40q79Js+MgvJE0/dVO64s+20NQIBxKzjhPUvkczZt6NGlQpCOKlCNM7OU7pSG+IdS9ycVQbpvITeawPhNjSGWw4PSs0Kw8g4GvoTNIqRngsJpcroGPKMm21oZT+5kmfwwIeB3IpB3B1qoz00pXK6TF13P5EnQuaQmzb4yqnREFAajLpzQkqOq1A/3mg+q7PevHvpOGoxccAz+wrwWoshJaWLsdTlUVy7IgdLYnUN9ShrJWUrdLdV0Dr8RkhaFNGWqHIuxmAIO8sseU87EWFlJ5J5Wq3ondids9s9qdXMYTEX7iS2seW6qip3Z0l6O+nB2l0tkdWJVQ8YaZXevr5qFOc17AZjurnqLnXScEWynjTuhoMRSHKcAdfVTOWqpMwOzo0USq8wGCkh1VKFFe4q2uUa4R128oqKQVPIUdH0gsGOsKRl8qDk3uD1ZJKmZcqQaOdHuNH7nGBMROfIRHJkCxnKLW64nQZuWTQ3hen0PbqxGO8ytaxRwfxJ7VbmzQoxgqyBOLBA7v0jgpvHIMuMa9ri5CXdJ7qLtYeVeRqWPa+QTtAcKF9WeRmpMBg/YsQZXp+N1GIgKIQHZEUdfVhLST1BV5BToXfqdO76atR1fmTY6Kryq2ynKtQGa/AYyrXzKUPG6nZwDlOb8yhSKw5DQRR+iGwM23NiG0/cCrUQArTBUeZdSQ46CKrHRLmskey2IG6pvrImKjvay5U/wHdzGGUwR1Ma1ga6Sd8F8TQJZ3FnoWtpc3I2y9t9dIYTO9n9GV0tk6XK309pMILeccrC9V4aWjdUuzQ7Ey1xr/EAG646k0VrPbmTy8PVqxQkLjoChTaMYcvESaRG0LGXCr+PpvUUJJhhentprexCKdK0HOoFNpwqyZ8EFLHEC7wMzGqvKde7m8uc06n8JiMRoYJp0LUaEJ+6sm5rpRyD6Fydm42vCEh6CaPLYXCZ7YY5Esx5EnX+sJ2GMGU3S3xV3MdLfMQQ37uqFDIE0mkVqztWjXrKckU9OqPRAZuyy7ULkb219K1jxqE+Dvp0kbuJMoyeIbdTV7XbEpAvs2Gq79S7yzMbD8V8JcvjlVybpeHUEYVtV3JIEMVR3kgByQ813nWpx+lT3m6jXF2dyzt00qKcTPh6mJlQPaLvRtmhTLFIWM1Zyku7rtf+PkXjSZkMTRssgmCaeGg1+MRN5njecQ6CKYlPppmPWX5UCSt6j69QJzTb7CATYYh4eN2DdlLbH1PmRFx7C9XsC3pXueNVs/BbjmxubKmBSnZeLZnzyoxG3Axu44acpJ7esdebw7NLrPEHkWfWiIcMkXFQFO283gfDkOxRpbveGgi0YYJestrGZ1SxhbTVRSIRtNLh0L5tTuYNI9tMczp7VZ48N8og9ERmTIOoFyPEG93ttKq9o5IaNNK2S+iCgVPX9ioNzRo0QHy7WwYVGW1Fs8IU0N3yGrF13GTYgXmUCMZuffDG03Gra77gFsfIgTjSGV0CLfcTVzoCOhhBpexupGy7aWyfNcJeZvidwhNyqaxdg8a4uy9do3tE9Mmlsxg3soLljh8Eb1lw2N1JWXmzdu87paYJh6lj7DAoxX6pg4GOggjNLwN5tz/m2unUQWkg7IX9Kel1UCLsyzQJgSFF0Fmh1oIHuoAh6Ta32o2h2EHrazU2vSrqJTecqBBJ1wS8FFqzJZuV2/rsWYchKxxPVCzmfCwhDSTslkYPc2RuR7Jd2EnJ9Cu8EiH4FJlSK8CMkK05Orbcvp0s8rzJhPMxhVD61LVdYYXkDVObRjjaWBIVGmLVpH7KBiFKDhbFdXY/HdjNSRvS6spK8ZDK0GBwTEsiqQqaXsVZG4Z43NwjE4lVGy889HixhXxlHJnShCNnxDIvSilcdPVqd0eSdebTJSrTZxYnrrsIF0D5O/PndKqK4r4MXC/OLlxm3xlLoYip7rhmahOkwcn2bCQqFBxDs1TltYma+0zs9pnKDBWUTNykEznDSyLL8RWin9ytqvlghF+JEYSucY9QGEquVFHMIaevy4RYTkGFNhLulRkDO91mElyTa1W6ZAbUu9kNqlb7VkdPDph/mVojq2F/9K4cdyX7NS/xiHwNaWI/NHoKC7rh3pq7uBSnLS4tsftJQ0lSWasMRSL+RcN9ji6OOIdimV77jGWSctZSWjDt8+2ZY7A97/nXsJ/CnSJtIZoc7O1ezFFXZOUmjTEDrmKjUAftTABAUVdcvUYNdIkRvY6ckWRfr2/nzSWEGPYiVzKN3RwV2wGdC/i6ScmqtFi8Bp0RjJYZfLzBkE/G0pXT4WXOWFLvEOw08mm/plRGwlEBa+Ky3YXlqTQvaItAk2e3UctgKzvwbhPExiS6TLQasfyNRmVXE7at21QJOGLggR7qhBFYHj/Eq2izLhzSNHz8chkIa1Nd0MsS2qcWhBZKm3XssA3WsRbwu7OECQXGmTld+37plvRejDa8cWIG3EYZfaiKq2a3/IqMMVzdKs2BALVmr/ZrgVrzfFIrrePauTfmEUrAd8yQavEGWx006OWI7KS1vYZWyIi1hR6vSjD9ExotoWSrA/MF63HHN2SonxN919AnX8xdLoSXBJ7uhw2+ZrLeiplgYon7ZswvsAlgbpUlOxPu9yFxilC/Yqu7eTAJK1ku5b0P97RNKa5nXXfb7fZvf3t7//b95OztX3oFaz5p+X92qPM8m/n6nsXjWNA1nU8PXp/+NbF+ff9W2SEQ6nmAVSet/zoG+rvjqw//zNH6TGF8vt309bj3eYbcmP78/u9bmIHmuanGL3WePN62ADustp7fF6znV0pt8P3n882/KDNTd6sutIES+ZfXu45v80t987sULqiIjfu69F8ne+/fnNerPF8wAv/iVsWs8evEHiiKfUQ+Lt/++N+7Tn5MtC0AAA== -->
