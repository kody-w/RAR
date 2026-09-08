---
name: "rar-cowork-cookbook-ppt-exec-plan-software-releases"
description: "Builds a read-only executive PowerPoint deck on software release planning from Dynamics 365 F&SCM ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_software_releases", "rar_sha256": "310d3bd7be3a864af306239adef536a7d8c0c9e1055c29e779ff318229a64c55", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_software_releases`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_software_releases_agent.py` and in the RCI capsule.

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

Plan software releases Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on software release planning from Dynamics 365 F&SCM ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases
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
    "comparison_period": {
      "description": "Prior period used for the trend chart comparison.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-plan-software-releases-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Intended briefing length the deck is scoped to, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_software_releases_agent.py` and embedded as the fenced Python below (sha256 310d3bd7be3a864a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_software_releases_agent.py` first:

```bash
python3 ppt_exec_plan_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_software_releases_agent.py   # or on stdin
python3 ppt_exec_plan_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan software releases Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on software release planning from Dynamics 365 F&SCM ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_software_releases',
    "version": '3.0.3',
    "display_name": 'Plan software releases Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on software release planning from Dynamics 365 F&SCM ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-plan-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a3386bb4bb31719c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/plan-software-releases'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-plan-software-releases', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period used for the trend chart comparison.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-software-releases-2026-05-24.pptx.', 'review_length': 'Intended briefing length the deck is scoped to, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for plan software releases reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on plan software releases for a 15-minute monthly review. Produce 'ppt-exec-plan-software-releases-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan software releases data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on software release planning from Dynamics 365 F&SCM ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on plan software releases from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-software-releases-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Intended briefing length the deck is scoped to, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period used for the trend chart comparison.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX summarizing software release planning status from D365 ERP data for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPlanSoftwareReleases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanSoftwareReleases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period used for the trend chart comparison.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-software-releases-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Intended briefing length the deck is scoped to, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecPlanSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZOjVrbnV9Hkixjbj6pkR1AvOmIQmxZALAIJuRxldhD7JoT8/N3nImVW2e3q190R89eolhRw79nP75yTl99e3KFPqvbl04sZuuVCcvM8TcJ24ZbBgqvGqs3AjyrzwL+FX5V9m3pDX7Xdy4eXIOz8Nq37tCrB9tWQ5kG3cBdt6AYfqzKfFuEt9Ic+vYYLrRrDVqvSsl8EoZ8tqnLRVVE/um0I1ueh24WLOnfLMi3jRdRWxYKfSrdI/W6BU+RC/N8mpywEQ1sEbu8uogrIt4gB4XKRh7GbL8KyT/vpw2JM+2QBvubhh8VO23xY9G1YBh8Aj+BjlLvxh4Xrz/J2D/3cugZP09uiy1OgDJBg6BZdHboZMEBZ9WH3CtQMb25R52H38unnXz68pOD7y6ffXvzc7cCtF63uBaCmBoQ33zQyngrNJgJ3Y7ConoCNS3Bdhy0QvgC3gjBavF392IV59GHxn/+Zgd1x99Onz+Xi7fP5Zf5jDOWiT8JFX7ldHwYL361dL82Bxq8LNh/dqQMK9kM7q7XogIvK+PW58xulql78bX7245PJaxz2P35+qYAI7myQzy8/LYBVP7+0w/z9daZS//jTaz477sefvtHpBu8S+v1MDEj9+uXt+o0sWPhtaRotvpiawL3xakM/rUNA/A/6zZ+n6G/k3kzy5bn4x6r+sPg+5VmfvwF5n0HoAbrfJwtsAHa+vF5A8P34xqOtQOS4pR/++NM/IusnIEzztOv/Jbo/PwknIPKBtd5M8tOHh/t+WUBvun2l+Y/Zzjnw72gClr+z+2qof0T74dm/I52nJYj7d19+l9z3NkB/W/z8D3X7nzZ8WESfX/gwB6nbul4eflr89giRn38Ivt384ZffAel/SsashtZ/UPhSuGUahV3/5cvPP3SP2z/88vMPQw2iOHSLL0Obf4/m9+z64PMnC76t+vHPewF/q8zKaiwXX3No8VtV/6/299eF7QI8+Xa/+7T4YybOH2gxK/HO9GmCP2RjB2T9gx1/evkdAE8JtBme6AXw4z/+Y6GkflvNMLow/WroF8DBfVqEs/CHJO0W4O+MGm0I7NqlwLBv60D8zx6eJa6ixa//x3/A/Ef/Debhuu6/zND9iIcv7zj95Q2nu19fFwdAtmrTOC0B9hqspn0u3Rhg8MyybsMubK8AprypDz+CbP44f1mk5eLXf0L5y4PIaz39+oDn9Il6BreZEa8b8vB11u2YANh/auKDivUsMuEir3wgTJQCpJ7xvqtyUHf62Q5dlub5IkgBpoDKNT1oA1t9mon9+uuvntsln8snROOLZ0nrYLDgqziLjx+BVlGexkn/uQz9pFr88NvvPyz+e/E/7XoQn3looFK8eQJIuDX36gJk1lCAZcBJwK0ANh6e+O33N9sCMiUoQcBvaZSGz80gMrMweDe0uWY/YiS18EJgYGDcoq7afi6eaf+62ESLr/ICpvOjuTIkVTeX37nmhaU/AaouUOerJUHBW3Qg/LoIFNKhCx9cf/Va9yFiAVLc7X9dKJwG6lCVg/9mMR+LwOaqTIH5v4bB8z4g0v7QLVbvJF4X6hyLi9pt3Tpp3Tcekfv0y1zV37YD4u6iDMfP5Vxvw9lUj8R4mgcsApbx31z6cfY56E0KgAJB9877scadq+XhUTXbz2X3FvTPpsMHRQAwjYc0mEvBf72FVJdUQx487AcknSm9eSF488ojBudy/5cOplsI32t4+Lnh+TxgCEos/v9skmaLsJJkCBJ7EPiFoB4M5+mpuWOcPfpsMgH3h1iPrPzWxLwD1Ttefy7zFIRdO/3Xc+XDv29rnhg4AFEB7hgP+iC4gCQz3Ufsz7HctnPWuJ/L98IAVFo8UBDYFAAFSKQ5ft8Zzk/fJU0AGszX35qER6y0wWwMEN+LevByEHtRGAaeC7zUJ7Mv3x0MEiGcc3lMUj/5k1az+UG8AfqzY1OQkaB4vH4F6+fTd9H/tPHZC81bHn3iANK3fRAAcoSzgLObZqcC8fpngw70/PQgAtQo6n7W3QMJBDR93gzbsBnSLu1nsHzaNawBTn+cfz41ne+GtxrkDDAWyIx6ANZ95NIcfgXodIAMIFBBahVpCSo/MMqbER4E3WIGBgC8b63pk+Lj9ptC4SMB55L1vnFWZN4zdwHPCHfL6Y/4cfhemAB6xbziwffvI+0rt5n2jKEdwEHA8f3ps114fVb8Z0uxeKf76S8T0I//3pD0qOHWnwPg0yLp+7r7BMPPuvtedl8BgsFPWbu5BH+cgeHjnO8f31Hg4zvQ/InsU+NPi39PtD+ReEuNTwv0FXlF5kfyW2i9fYAluI8r5yMxP/1cGuE3eAXsqwLE1uy3CdT8r7XwfQkoiHELAAgsftbGbi6pI6jij2IAnPC5/GOsz7kGak0Zz7HZVX/AgEdTAOL+6bOvNQs8KnvAO5gbyDicZ7ZHZnThy6dyyPMPLwAlw386q81VqZjDuZvnO5A4oBvr0/BxBXwDHqddVc4TSloF880/z78auN0unk/nyhd8DbEHvM4qtf3iG6FZzH6qZ7meI9vc5D1Q6Nb/lfr+8cXNX0E5AYiXd38M7beaNdfsP2Tg05TAhD7Q5MNcFACwAJGAKWcl5+x1O5AOQMzvyvIoGl+eReOvAv2p9PyxvszAWg9zw/WoQiCJPyzC1/h1YZmK+F1GX9vev3I5gp5jJhhUn+by++ENzz486uCHxdepA6j3Ngc+JvZyACP2z/PEM/v1sWX+AvaAH183ff0Vhhe+/PI9uR6g92UOvWcA/b106gxmAOxna7+ClL09w3Q2QFsFgx++af5PsvkjhmDUR4T8iBEPKt81Euji03D8AkSJ++Svomzm6hXMTTeoH9GM0M+VD9ke3cTcCM+RMFe+N7ncBUp+BOA9t88FiLwkn7F05vMdER4ygKIBSu9s229O+2a66jE5ztICRfvnLzp+ewE55c6x8JZVb6MHWA4w9mM3N10wgB3AEFw/AQI8+3eHkrftXeKCrhjsx1EkwL1g6YW4S1OEG+EIheEMqFoRiVPuMqB9xGdCFCFJH2PC5ZKJIhylMYxxKcInSUDviTJf5sYynUUimWWEMAwWESiGBIAQRgQBTdGUTy4xxGU8l/RIxvW+bc3SMnjT86nXbMSv89Fsjzd1f3vxKAKsXBPdhn1+OJhBwc2lN8lrqKWiahxXayvdGtdmCowNoaEJpYnIOV3S/OXgk+mmZ/sutW/JtCOv67TjWW+jQ/qWng5k09ZbNc0bVTuH2XDnOCTPAtxGTx5FBRv4st/s76bipAfUE3N/sibRzM47cvKj2oCOlhHlfCrLuYnZmXmrbKKKbjLtQzCMKLRMK9W0OQnhKley+8XlAgvfuOwWsGWyo2zvN/eTU1v5ERZTke57ah+lRKiuieEElzVEi01wvSN6zE350XTOKJqyfoqk/dk0rNPmIHrpbhiLzYXmbVOA1+sO9Q/WUW/49OxsyHTYtEXI7bOTY+z4+z3WlQy/qdexotNY6RQB2ZV7o0bqsMnugumKU3BfEUxvnzwEgsOrNzAbi4gibQChMoRyYIwZnLJVtzsarrdVNPcumjfupCUTqg8jkYaEHa7G49GNR4hcW4dEqbXzssrCga0uto6vYnVzNa9sjV/I5QQZubRR1E3SHdsyseM1d0yOqwPfOhOf+428ZAPaEvP9ycmqzoRv+zFtzuGlvx0jicyv1Dp0t2fOvawxcwDmZHUw0+2jXIlrprM3zVGoqkZNdSkvbr6xaTP3LqCmh6gUzmRqel8HQpE4jqg1ZJrux2BpUXCDJ8PB13aOW1dxVR8FdC3Ffk3s80S/rao6QXUyE45G4g+mzZ9LaVjBxc1FKNfq9OJmaKh5hlpCoW9sU9wSsilNChfwOlsGG545rW0tE5OtaRl2zTV72iyMIPPz7izw9HjPtjl2Z/d0cCnxg3IbnJN0NsyVD8XVPY5Qa6nYK+eMKfxIV1YpaAR2MrHUudultIcFOkbaFSK6nqX6jS71Motftm2O27vbut5txqu/FLed2KJqBu/uYqhfDb6ERduyQcxt5XzXZT293QYyzDESObYQbJwI7u7rmrju+FS6O75QHg+EdD/CrlRD8sGWMug0YjRepB7kklG7C1zLux/P1dFCduzuUGL9WsZd3SrV/Mhgy5JQlXPHdY5MDjsopCEmuQew0pwzuFKsQ+NpVxKF4nPI91jTE+JgHlhR3qKDIzR5uyWdZRb152Llke2qTafIolg6iRWZTOFl4S0HVgk3qGhGMY8t+W0dTepFDbL0lKfhoe4T4uY3Y4sJupoaG/LkO1LO0qtzXzm7tcmPo6Y0a9inadvweSw+HAby6nDa/sTH50667pbKNDpYmOKjMokBsb8yRlPYZ2pjo0TNDlqwF+3hyjYn/a5GnCpuroLulzdH02FuvVLxU3aCrVEVDlZQU+cKjeosqZimU4vWJanwHByOcLbv/G6CJMeYLEVmA2bl3ESWKJ027nzaXGtayKY8AVHnTDJgsmAEPDq77OpwtMPslGyn/KzK08qNt8hOH664lMIqVwlGPQa3MK3lZLzyxQa+UdPBQwK32x9OF5wMzapmTsmmwXmUd/KLFNqs4rT83g6nFtL53kf359VYnbxNIes+FMjKVTtbg5u0OK4plgpv/WWj790dM3m70BI2/XQNRwYGUVu4sXdlEFbRIl+GOIxGbrIb35w1n3b1mb1tHefQiBRcnDYczpuq6mfXo3nUz+eBq32CWne4tApDasSSVc3S2i2wm3pLI5TG0FuWo9q89zXGP1t8MEzlGTPPxuEwivWEbdHTREe76qTu6Q3EB3s4IrLSV3gPt+TjLb3I/toPKN2lc0tR4XtZpEKzXGn8eKFrMTFxmXUPIUGvVBdCzxJuNnYsTX5JXAucrYaN5RGJLm0rjtMngXAOOww5UxjA6iCtTi1DkVAl3CFDNNNdiRSbM5m6y+KkH6SsTlXthih1TPFM7aGdHianUd/pS3F/2kTZ2SquxGqzWWqDgCbTWjB27cixdn9hto24sf0kWB6agUWmymBVm59Qu12K1HDUbZLmqN6RKMwq5ZXkyTux3O+U8AyHpT2FhUeje66wppyLnK2mZXSTmZdsBR32ajlYYXzTnUrqsIaGUGTfysNtuePUrWTo9LDm8Tsayi3jyAkcwhDO4PBVarsxq8dzWV6Lm8N2XCZIGKmtY7I5Kn5mE1JDHiubkUZlTWrXRLJEtS9vFFFUHW7K99s5747SVl3e5Fzka7FcB7tRatKS3Vc161n7laHbV25abSrfMs7VqHCY6RqWJPZnh7uk64Re7nqBszA4OmK6UJ7a1TT5O3pXbBQZBJHaQPLJbQnbwGC3YbSzJyU2jHRrQM5SdmWOQpJlGUugKQWwc1qfZEuw1M2Zzj2v3ahFeaAQOzTyDMlJ59pWPsEf91s9cfxYwGMqZdjlICK1elNvHFHogzZC++x8Yc2a90wLWqGIpuWNtXfgPblrqouWn07SlpVZayoxPLSXji0MWdHl5U3p7pMztDx7sYRIhNICoNLZ2pwvpoTLG/FkSqsL2+T+/XQcbzLUXsxJtxLLbpsb78e+PqWiQUSrlpTbNHeSTIo6Tx8h85BwMHJZcUJ5C3NBclKxsEUaFwYdElhIrqpesSY79LaSXMV9kLLWfps56EQ35+qU1mdLpMitdCvIc8dYt7aKYYY+VoU0aZknLNE2PK1D5tBk1YFtDmncni5HOWfvAc86vLDF7ycRz6moZc08EQYBO7QrXqMC4R5etrrCEULaB1tL8JqDvaMPoLWr0UJiq7h2LQsRIAfdx3azPYxaVHGpszPaM1JttsVOpgRLUo9LCSkBpuwso+H4yoGZXDUEvmlgJ+fdcFduENiZtu6+Kmyhjk6pt/LKCnVGcRmWadFD2O5My0Ia81mTtqQrDPGlCC/wIXZvDZ+VZygo85EAg+s9ZDe5TUwe2+zQVSb3mdyZqtQcVrtzmGRZ6jX+brUrbuwJoxoesbulkV+dOKZ9wUVvrmNdLQjbHwL2pK7OQa6fu1jewePkG+MwdUW66pX7jvQ0CKssytCo4tII5pW21pXni8fNUdKnkJKPW4ljSP1gVmMvbWIXOyCjg8DFEKwbblyZEXlVKd89w9ZJVzNh1PNuN22mDHI1ul0jK4IGcz5a+zqJ80EB4zC8ua5l2Sio1NfvpXNX8F7zWkxDN7HS55BwkNtst3OVEjJXfXXnHZk/ZdhwKUliYstJ2dgTlm33hljqm50q9aJRsUhbpUQkYm7DZffhYN1WnpqJ8c7WtqwqEC1licXmGl4iNheqRouklemgnMPKd9sopkk3VI1p5VrNyd2Ok4cmHeF4S7fK5LRbNEPqk9pdltH+1uu5dd1uFHtj7oiztQzkcx6RnS7KtG13mzzqxaWsDIhZ2M3OBQ0ahWzcTV1tSJcEQw5OUmTgFtwtv5DGShE0C0/4ZpTDjXILEqjZDw2RWKs4uueueNtuttqauS3pdUItmTUyGgFYZp9HItBPp9zxdtghRkOrGy3BLFdUc8WECEwzPqywUddPVURVR7vYQQRUmFy7i8sRki+OEYTcpsuG21BuC6SBBlI+5r1Uk2plUsKVjityg0foJoWuHGWy6gE3vAxiuV43FD3OqVPui+plSxbp4IpE2m35LHGVpDXyYTsNmGnf+voUcANX2hivN+I9IiG94IxjrmMh2pswEkINJ3QdvqojzBj6XZWKMFlWoa5fRQIvK6ZdbhtYwMVWLdLohCtBvx8zcqQPyGrHa0e4d1Z3cwhRfd2et+560EmDuN7bXlGOh/queBWMVsjgHYSDcqpGMenyeLxg5hK55tvmkkDKUSuxuGr1lRLfCTbem+KKsnNoRRolMuknZCquNxB6HIIfa1zdIPfrOqa9S11aI5INGZQoCBGUW6U6hgxok1qsum912w76KUdQIbmepm6iLC9U5Cw/7fTsFIaTnGhbmxv4xO38IECbDYW6Q6UWwjV2TrbO2/khS0VVZrGbsaeO4XTKwh12x7I6wRxjdG0LCbll1ChZDR11UoKvjA/jEj6e0pC2ukPDVfcyv99b+Tgc6/sROlv1Erdlgh+OuySlYhVE8yQe12i1o06jvWtGZhN0RZCUdj1u0abv183+eErWvSxtJFEbu800sfB54w7r/BLoh3OJEFB5vezjPqSXcqeu1mvJJPtewmPD1Pmte1xLro5bO7LZ87tIq6ujTBfM6tIgbT4IOgOPJpqOhUkeTK0ZXS1E6prymv366vWeslFBqHUJu98wmZSFfIH7JGEzpNcUS+eyXE36CpTGK2nYPrP2jhCXH2Ki2XqZZ97oUCsvtkMtg0MuL21t6phWuVy35Iiv2JzVkhO6Twp0oMrlhbAI3ZXuB4lamWjlMQ6WHdqyH3N1GrYIscevAKX4+9LwZNhBs0C9rAIu4rou3Z8nsbw7bWhznYYiCXIwvb0bhPTk62rE8wWsbxONg074JOA0mP1VuT1sLb7E1ZCFSNAi0daOMUikgthODi/+BYwY9wod8KQ6SQdbXYGBxV+NoAk9Rk6+PUF7Vzhe9LV4RsPM78usRXpud80d2feSNhxVY/SpTPT7e2WhJ7E4nCIz6hEy90ztwMGufIuCwkXvk0IKFIri6z6gA8GKPRIf0T1UCxZXdmPZotuyu1B8ZktHURv4pr3d4PUurcJkB3BaHNDEPIXIlUYVu+DvYQBdtTUvWEzDnNCoZ8yIkiRhB9rV821vcp6616cumORmHbOYe6lAe7W78FcwEmZClOK9zSi0uy87gko8V0O6zTLa3hBIFcmYJQlBS4+tHQRLu8Avpm5hMuHuJ9BuTRfzNuxvsXY4wctSg6l9NKVWVRvKEYbpFk5K3XO2CnVuAdDfj3v/GKz28WlXBXnYXW7ETcRDY2yyJGIkYRUh+2B5GYLDZY9rMR9bar0RcP8WsabpEBvxdiuWtcIgqkSqHBpQZHnTblGT5idiSfG37mbumhMl6lcT5gff8hPUTg8yk1zWMiRwUXosQ3MPi7hvKVKWOVUVLTXKpZY+mCfWm+ykwuymLM8XBTN0puYyGvRw3HVlnbg7VUswhS0bkuLuxem0NrpdoBkudon80oBKdmACrQEtJo96pz233YCWYLPml8ztluNnKpKOBZuesbxtBcNBt3lyXG4LtK2wowj3HBoqjWgkFIt1y7Awlhre2DjGnpPxThsKFO7H603CpZtfmcStIh3Tqa1ayLpVHBYlI9Zuviq42KBuF46hFcdGyYMitU2iDWpJxXFTCtL+wuXjPe4rAQ57/qiU0TpXTEjWg6u76iY/Px7yMhcc18pg+NiD8gZxK2rZUhx9PJ6dOItpGkKK+hrXalwTgYNbLE1KqyEhAhFFTSdihqRJefd+iFSIvZaFRZduOdW2AdFHuVkKbH9bGh0Jka5Mndd7pxC88wmrXQ4CDeLk2Pf+oK4DRrxei31xkUm5Qj0sLetKJ6oRCtgQtBIMBSY5udld+aE59iXRVaTrEjWNls5VPTs+5Yhkfd/3onivRVXrBJLE0hGvinxf9b15XqXTPUfOl5R0k5yCl/z6zlVc1TRCSAR3VzEBuqprRo7Li2WhmbYifP9sMJaHcperZqBCTiXHqwPmruVwNsVLyKguCrllEB2WbH/oaaptu+PuUuIVCfeHgRyXgapU5713v3rXGpeHkk90fHnNC4CgvDasu9bFcShpjvs1ecaCkRcZA66Fa4+ukvsAm0TUhGSwDc4Td6IvF1ZEK640j8u9SU3e3UOPvUM7gVcX60OxDljZ9ZmK7lzKCCYSWtPTpYk7MG8ts2acMi7f2kbvHOp1nVyN/tYgwri74uqlrfG7eYFoeMNtsFVg3jDTQ5wKaYltx8Ic5hwvjcFLazq29kNL63rOl4fSxPUYimrVqOUNJWaYRq6E9VgzCeJVO9oGvdbBNU5HxLxKOKv0+8rbEMwOuRcX2GnIqr3jCUWxNh9V20neEJI+xIOOH05EdT7XPO0NyaQwUz+iVcRfigvEFitGxFAvs2+FuJrU3sGDLVQVWE5IVuj2Ira6DS6XhziTYrlr+tOta72gd+zwSquH8841is7XYX6tFqcR845SYXr39QVg9QqMjJHW87mmhcCamDkYjHm87TfUgKX7ACTG8bAhC410hyO9pH1kv5UxxrlImYbQbHCsSZNt9/5oheLhuGsOewFTz6rsdlZZq3iS3FtEraV1u59oF9+npwkvB3JVGBFyRi9WR8IXe4nQpEow+CZUYVKfGqZ2VqBtTe1iy4jLLBaYSrLTtdBFoBrKkD74NrMP+kC7jlKuD8fOd0NmwHKo8vseg3ClJvMccm3W1WTomg9ZgPUTVR+YEvQ4ySmQMjptkmQqXSkxkYvO6BuZ8CQ09OgRW3KyWV2dq8JnzJFaTdg1svHcq+QoM01MYRFrWyrY0FF5fr+6py3NjC6ydxg2YGOXJA8Elx25QJ9244FWr+LI+sPFJjoLQEvd3aNjDIIic1IH2u3LSSXJBvSKV5S9NkmtqIMS6Eya0TxqKi0sczuo9NIdFIj+MqyaQ9uHhLhm1JCCSl7JYaZrs4OFeTRGaB6aBoTIQ3Jx0vnDYUWi7vJKKI2XNhLpplCXwWdaGa7D/aLs4lAnYBfyqeBityuVUILEU6cel3qPMCYyyG6Ay8i0mTM5BgQfrwyzGX1ye2ZE0qqHHoD07mTj0NWkIi3a3tkVmdmcvou9wb6UpgeQ5RI3JsXhm8twFuNkaSfGGVKD3YQD2mu/gHdnTq335g61gjWPV+sxTj3z4k8QqeOlsW5x6FaMHnFuoVPEpJpdVhuPIs8MgLdrZGqrm+U1ItIpXov717ivV6RIGB4uNIlcyK5gcyed1sQoR+89fFmWhKix+GZ9GWQEpXFdxJDpwuPaboPDfqkiGI1Jnd0lhoxvwKTaErQEs6sib7dLXo9Z9uXDy7fTvpd/9W21+cDn/9m50/OI6P3dk8cpZugGnx68Pv3LEv3y4aX1UyDP82Sty4f47SDq787VPv6Ts8l58/R8/ev9aPp5pN678fxG9EtaBkPXtxOQJn+8dwJ2eEM3v0bZzW/a+uDnnw5h31QAX93g+eJI2H7pqy/PA8XwZX7TcX6nJAzSb5fx21njh5fg7dz5C06RX8K2nlV9e31hNv8r8oq//P5/AePMsgTWLgAA -->
