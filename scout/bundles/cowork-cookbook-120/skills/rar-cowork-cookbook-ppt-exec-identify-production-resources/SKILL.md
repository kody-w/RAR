---
name: "rar-cowork-cookbook-ppt-exec-identify-production-resources"
description: "Builds a read-only executive PowerPoint deck on production resource identification from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_production_resources", "rar_sha256": "d4a3468f6c45b0743c54c6612d247ac62fa9c25f14a62b76415b21737a640b00", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_production_resources`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_production_resources_agent.py` and in the RCI capsule.

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

Identify production resources Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on production resource identification from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources
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
      "description": "Prior period to compare against for the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-identify-production-resources-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the meeting the deck must fit, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_production_resources_agent.py` and embedded as the fenced Python below (sha256 d4a3468f6c45b074…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_production_resources_agent.py` first:

```bash
python3 ppt_exec_identify_production_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_production_resources_agent.py   # or on stdin
python3 ppt_exec_identify_production_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify production resources Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on production resource identification from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_production_resources',
    "version": '3.0.3',
    "display_name": 'Identify production resources Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on production resource identification from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-identify-production-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6722916bfda5eab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/identify-production-resources'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-identify-production-resources', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-production-resources-2026-05-24.pptx.', 'review_length': 'Length/format of the meeting the deck must fit, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for identify production resources reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on identify production resources for a 15-minute monthly review. Produce 'ppt-exec-identify-production-resources-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify production resources data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on production resource identification from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on identify production resources for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-production-resources-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the meeting the deck must fit, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready deck on identify-production-resources status for a short monthly review, sourced from D365 ERP without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIdentifyProductionResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyProductionResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-production-resources-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the meeting the deck must fit, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecIdentifyProductionResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916edOiaLbnV3HeGzFVdclMFlkkb9yIAURFEJFFlMqOLPZ9XwTr9nefB/XNrOrOvtM9MX+NuajwPGc/v3OOD7+/2X0Xlc3b5zfNt4vF1s6yOPKbhV14C668lU0K3srUAf8Wbll0Tez0Xdm0bx/ePL91m7jq4rIA29k+zrx2YS8a3/Y+lkU2LfzRd/suHvyFUt78Rinjolt4vpsuymJRNaXXu/NmsKMt+8b1F7HnF10cxK79uB40Zb5YT4Wdx267WJLEYvM/Ne6w8OzO/rC4xV206OIu8z8sREX4sOgav/A+AGrexyCzww8L+0G+/fBQxq4qcDseF20G2LSLKuvbRVv5dgq0LcrObz8BnfzRzqvMb98+//qXD28x+Pz2+fc3N7NbcOlNqToe6CQ8xZyUbyqoLw1ms2R2EYK11QTsWoDvld8EZZODS54fLF7ffm79LPiw+Pd/T292E7a/fP5SLF6vL2/zH7UvFl3kL7rSbjvfW7h2ZTtxFnfTpwWT3eypBYp2fVPMJm+BW4rw03Pnd0pltfjP+d7PTyafQr/7+ctbCUR42PfL2y+LsgH8mn7+/GmmUv38y6dsdtbPv3yn0/ZO4rvdTAxI/enr6/uLLFj4fWkcLL5qCs+9eDW+G1c+IP4H/ebXU/QXuZdJvj4X/1xWHxY/pjzr859A3mfgOYDuj8kCG4Cdb58SEHA/v3g05eAXduH6P//yj8i6EQjNLG67f4rur0/CEYh2YK2XSX758HDfXxbQS7dvNP8x2woEzL+iCVj+zu6bof4R7Ydn/4Z0Fhcg/N99+UNyP9oA/efi13+o23+34cMi+PK29jOAA43tZP7nxe+PEPn1J+/7xZ/+8ldA+v9IRntk2Uzha24XceC33devv/70TL6f/vLrT30Foti38699k/2I5o/s+uDzJwu+Vv38572Av1GkRXkrFt9yaPF7Wf2P5q+fFmcbwMr36+3nxR8zcX5Bi1mJd6ZPE/whG1sg6x/s+MvbXwH+FECbJ8LM8PNv/7Y4xG5TtmXQLTS37LsFcHAX5/4svB7F7QL8nVGj8YFd2xgY9rUOxP/s4VniMlj89r/cB7R/dF/QDldV93WG668vCJ6+fsfnr+/43P72aaED6mUTh3FhZwuVUZQvhR2CLTPnCiz0mwGglTN1/keQ1B/nD4u4WPz2zzH4+qD1qZp+e2B2/MRAlRNm/Gv7zP80a2pGfvHSywU161lm/EVWukCmIAbw/eFRUzJQebrZKm0aZ9nCiwHCgNo1PWgDy32eif3222+O3UZfiidgLxfPotbCYME3cRYfPwLlgiwOo+5L4btRufjp97/+tPivxX+360F85qGA8vHyC5Bwrx3lBcizPgfLgMuAkwGIPPzy+19fJgZkClCXgBdBOfSfm0Gcpr73bm9tx3zECHLh+MDOwMZ5VTYdqAKLuPu0EILFN3kB0/nWXCeisp0L8FwI/cKdAFUbqPPNkqAKLloQjG0wfVj0rf/g+pvT2A8Rc5Dwdvfb4sApoCqVGfhvFvOxCGwuC1C2s2/R8LwOiDQ/tQv2ncSnhTxH5qKyG7uKGvvFI7CffgHV6H07IG4vCv/2pZiLsD+b6pEmT/OARcAy7sulH2efg+4kB5jgte+8H2vsuXbqjxrafCnaVwrYzewKF5QEwDTsY28uDP/xCqk2KvvMe9gPSDpTennBe3nlEYPvPcCP+ph2wf+o81nPnc+XHkNQfPH/Qbc0W4HZblV+y+j8esHLunp9emfuE2cvPltL0LIsQIg+M/F7G/MOVe+I/aXIYhBqzfQfz5UPn77WPFGwB7ICyFEf9EFAAUlmuo94n+O3aeZMsb8U76UBqLJ44CCwDgAHkDxzzL4znO++SxoBBJi/f28THvHReLMxQEwvqt7JQLwFvu85NnBJF82Oe/cmCH5/zt9bFLvRn7RaAOogxgD92YsxyEJQPj59g+vn3XfR/7Tx2Q3NWx6dYg9StnkQAHL4s4Czm2avAvG6Z1sO9Pz8IALUyKtu1t0BsQE0fV70G7/u4zbuZoB82tWvAER/nN+fms5X/bECeQKMBbKh6oF1H/kzQ0sOeh0gA4hKkE55XIDaD4zyMsKDoJ3PYADA9tWcPik+Lr8U8h9JNxet942zIvOeuQ94RrFdTH/EDP1HYQLo5fOKB9+/jbRv3GbaM262APsAx/e7zwz69Kz5z6Zi8U7389/NPT//a6PRo4obfw6Az4uo66r2Mww/K+974f0EUAt+ytrORfjjjAIf32vkx+9p//EbuPyJ+lPxz4t/TcI/kXhlyOcF+gn5hMy3pFeEvV7AINxH9voRn+9+AbPOd2QF7MschNjsvglU/W9l8H0JqIVh44fz4mdZbOdqegMF/FEHgC++FH8M+TnlQJkpwjlE2/IPUPDoB0D4v8DvvVyBW0UHeHtzJxn68wz3SJDWf/tc9Fn24Q0Aov/Pzm5zXcrn4G7nsQ9YH3RnXew/vgFPgdtxC/oVcDUuvfnin2dgBVxuFs+7M9Q8twDZw0csfwu/B/bOejbdLHA3VbOEzylu7vsesDR2f8/g+PhgZ59AMQEQmLV/jPVX4ZoL9x9S8mlUYEwXKPNhrgYAaYAcwKiznnM62y3IDyDbD2XJgPeyr7PRuunvBfpTvXksXTyXzupX/dx1gfLzzOqf/U/hp4WhHTa//JDTt1b479mYoPOYKXrl57kIf3ghHHgH48uHxbdJBOj3mg0fw3zRg7H713kKmn372DJ/AHvA27dN337KcPy3v/xIrgcMfp2j8BlLfyudPMMbgP/Z3J9AEo/PiJ0t8IgyYPaH6v9cfn/EEIz8iBAfMfxB7Ie2Ag1+7N++AonCLvp7iaTHdXgeq4HhXqLlvv9A8fnzo6/I+zkm4+4lnr1AiY8A1edeOgcRGGUzyM58fiDCQwZQTUBNnk383XffLVg+hspZWmDx7vkbyO9vIL3sOSZeCfaaSsByAL4f27kDgwEQAYbg+xMywL3/y3nlRaWNbNApzz/A4PYSJ1cB6eKEg1D40iVwlyRRzMNwynZJLLBpFyMCFLdJzKFIHCUcDKWWlE3iiIPMUj0pf52bzXiWbBYLGOQjSGn/+21wyXup9FRhtte38WhW/aXZ728OiYOVO7wVmOeLg2nU8THYmaQLfCHoWAo7V7NRfu9lslMP7mU7xke8D3NyUq1N216EbTTtd7xsnKejffJu+vq0pjcKxtNTAAWH9QaKLS6gbKlnGWRI7/v0TsA8lYwplSQyvnHrNN5cqdQ/VyZjbTLuGmdT2a0QpnYDS2VzQ70Y2VhklASvJzlNRXfqWQ1WlAEemWGKw2MWMOPtBBW2Kg3RcXJ4WeCRI2qdUpWEteQGBWmtU0Hs7QMcm6ITXrZFsrpI8JJYrrKaD/qNMu7OhsOf1I2zdeM1FAxELQiVtz8yW9SVahEOzjwEMBw3DhqXwNJq3ZDiRjtYli7gmbDPjAI2+musnfpqediFkOcFw31JQUNBtag80r1DYxDtrS54olpMzqqhHmRZiyS32svFM1FLV5UvgSzXoSRiHz/37M0085sQwztXVw9DcF+eD7TLXjZISLHMcVqxohJTwXGpy6TCNyxriQq3sVcif6Du3PZOhiCmVK6vuHxcXw6Zm5p6LEsJT3Fil9XHZdZCcnN3kJ0mQmmZBydJJNaysNrz/GElje6Y8eE5E7faCNvi2k4PtBWnsaVVXDcO15zTzRZmKv2+8/icMoxNkCEFL2cUVqGQtcx63VVEQ7OqsBwvPMrnpTsSxyw+jWxZRcsTsRLaOCGuGWnej/JhDctxVyJIe2Ulu9ytKhfOoq1YSuI+tf0DmMA9VCHv5z6N4H2yLw/cKW0kIW4jVPGrBi9L89p3u1GA24PKEV1bxgGD4zJyP1xWUhJ04/pARiVykuvZ4qNwoEyW8HlRj3crm5qg6KpblkLn+809M7jSxrBSI8/hxjbHhtGWTldn9V47eKpbF/y+Pdd0vcQ2beTHOzBDakAyPdo3tLLiG1ibpgsU0zxFakFsw8zF0Vi87ELvlDvrMKXv8smRKbq0C7yTDVOtlardKGv+tqJv4dLFkRKrTcs1jeUOrS+7cNkEKGWmGwFkjU9vxtW2oGWuvVpEL0bQiqXDdRBshXaCJ+6QQrlEkV6A95ewOY9Sv4+UTbnNkAlp40bD+FXvGTzvW1fTxrStP6BU4abYeqXyjpGTWIjAoaxes91psukU8zfmfWXxyLb2xO2NlrFJvspDeIaY+qRyNaQxab+7HazV2kBIRoZYAs0u9P0+6vLtYLPHI5dcbxvT7Qv2dpLzM2Z18Xigd0N4xTUH9wLbRw/NpRL2KlmN0qFemfXZ35/FqLQPvGapUCjF8EGA1tPxPAbUsV11K6uMy4lPO5tSDGdiS2yPVj5pyYFVbTA43wyofQ307SFtON7xkVXmXg9Re9xvOUKKTnG0OaanMHMQ/XBIgrtYEy00FstoY1enjlT5lBM5/XrS1l0HX3qTriLEuu5KPZv0myOFo5SKkVvB+VHuzKtB7VZXKNMJ5ShqirRlTolzaHn9iHPstmwma7ff+GhnnFM2juxVbHbsnZj6ifIK7Yxuw52Lj6flqrjXbUiUpbJv98T1pAbinWImn0V8y173MHZjKG81pbi0uet8V683J/ugpsHB3jprzmMqmJsIFivpWL/IezVtzA3kqHXBySYljeGl6Kqu5MVOZ1awR4hagB7viD/U4Qa9SGc8wHESw70JSi3Tv45rfeIQF92fE9KP2xa9O23gKr7W74ZMx9vjcG0RV8iiIcmFwy3OCFNTh96lkRMD0dt0I564KvdOeCcq++bqMxjlkmzXp1xlTW689wMOusVsXCUW3fiKt97dUxFEfRKqRdNxjIy5qj8sm4HMdMXiE01d2lmly8a+hSxvc3C03DUQqEgP2XnbSX7L6Sst17ba7lShBH+LJQTLGWu3tTqsaI9tmohnn7HDtg06WWu39WrnnwUqPfIHUWSjMpATDRr7JksTswt3WcMs83sKsOm+t8a+GtUuUSiiu+xB8C6t24ns3VGjWKVcFZkRG04UIJPuSd2udF2NC9DCa+5UeJOmpe60pYA01mY9TcFq5Q9aESGQWdMsLClY1mrtfbIzJs89SJJjjtn2JylI4X5XVCNSan16bUbxOrFxc6RJHo+qsoZgnUHP0+p0qo8y3U83Nsl435XdMmJIPN6eHYZmzVHhHAvVxHWJH41qs85Tm5ei66ZOjbE9bkpU3ewkkm1RrlpnY56Y9GbfZzazTgoVXeKh0WTT/dDCmwQ7cNY1wEhsa2oX9Dw2ikTeuRUGi80a22EsK54MS3T78h7nkocfGDJsliec4IQ0GiUlLTyXYFOEhMZEMIVBiIciturwzkRXwjvyEVGe/MYg1YSybheuX/LLLa/yqgtHSaCaB1ZM5W6fNPLK51LVznDvSA5cPsgDJNcMJjQGN7bn82pzhiPhaO3UuPJUMD1VDKsYW4VNYqfe1lW4r3R7u5QE/spt94Q3SpOTH4sgJpZDvAFWi0LT8FIdYlJhz0fucUh9SDxPEjZN+nW7q0+eUN0yYD2+3yxVNdvWVmKx2zRfhiZz5Lljk9DycJlozVS2UhN2m4QztnJZSiTcEOQF4VZlnt30Y7Ob7hZZu8zADVV2RVSOuuZb1p+urd7Krro20Atr+kqWBbLQg/jGFZbh9ULZuJdAqrb28TQIXZXbZ1LYwHp51BFLY8OL0J4bbNu2S1LfTKOO+4RTiIJ4TTOLV8yNfzsfyvNKuhtiHB/YpDpUzRTixVUoJvV0XTZtoClREyJMZvCwV8G25sWhggm6WSStvU2cHD2oG4Qqzw1JJoLs0UqzPQ1XZCXfBxO9KKybm8IptG5DfqTa9dlgHOoUaCLDZxS9JDA335S4S8Wkd2rzi5sxWCerbBPRU1huto681rIDctNCvdcFPqTXfaKrAQIUNToSMXn7tDZrHmUM7OZE/NLf6czlvC9lWB2rMjRu/CqJyupG2emNdm763T/TLB66/K2+xqVGMCwgKYbtGI+3rQ7rtipMl4IV5ZYKilN82HYpcdzSEu4sz1B4FMxCjIhOL3TNTm2ODwuOr0JT357LtQpXB+e0S6YcTc7ZxDR9Tq3h4B7J4XIvRTnBrYyxEKiDQiuOo+6pvDwaU3AQsvNNVxk33fnqsLld6kpQvf1wJwpWmayONw7iKd8btq8xLSqmOh8mpzaVsvqyLxKyd1bo4WTe4fWNE4s03JKGQdfbidsN6pLM2OrmsYPZ9dzGoAhX1LHQIm7WZKnCXggOA9qqECXuMakOb2NTCm5jnIhwiMzOHpHmqrigqcX2mV6dkujKZiJnTU3tBUVtdDttAL2uEBuYcL2b9pgWw6iT+2AbZBazut7O66URkzbqrWiIQieKN0V+sAXcOKEsR8j4abXi6PhuXHi4jiTJFrMbHPGH/Y5iA6Uqb75SpLdA2eMQVIn7Xq/XvdCk3dVF0XulQsIVvp8SHvfVfGVjxlLhkjs9stjeTkMxvK2VJMZ9pZLTRgy7Gyzq15H2TaFNuwiDS7Q+VxearkpzMGgMUc/FGSZcN52OAE7iXSRXgmY5kT3BIkPbjDYhx7ZeBgcay3RV2uz4vc5z5moAgVtWHTKYrijS6tKtMAVBdVYjd0wo5Eh26yrp1skUFFlEeZ3I0V3rcVusMC5WzJsZxKSKCH0djwxzCb1VLfbO2b4SFEpajpJu6YMuH5ioEJFieXZXtiYKd0ts1M1Uwa25OqPKthFbIpcQVxyda1dBe/DZ5m4YEtLJdn1GpzMnJQ1+lceNdNnszmZ48Nhi2jNmvj2ImdiuySSp6jCJKjlIAOTLVV/7rY7GGIZY8rg0RceutDGffAlpwYzmKeg9Moc0ZvoTVjgOKvcDwZ96K8rRcjnBQazJe1+t97uiqG3jjorMHsl0MNiaeCuaGnbD6i3MRifs1hfqjuWPts/f6WxP5uTSaHu947GuZn1TBUNfaTrHS5GxE7oUOgYXFAgHSbW+lxGdGnGz2uJ9r1oOClJFXGLyRqFIAtzH1TRRfMZLJzMVQV9yMtDp1hiXzBOiNiei7FLdZLTtsoQqpD2yxrIsl/bB1eTh88677s1+36/ZUg+LZQqlQXK62mpNibXM7YRc3+kGXYbTVAsXDiM2HL9nQ7KoLau2bSWiz01YaZHUbBt42N06WoBB/mAdmrbKSSBq53LH4whaMi3JCQnOgCkWN5Ld2txcs046O2nAKZOxbJmMFWk49Jv4PonQ6XCO/H7IxN29hf27pJoS5PWB1sFNuq82aKRMPb0/3xj4kOPoyixVAy/YNKyOFzNqEbrP4d6wfPsg1VUWZ/LU0ai/OQ7nqOM8LlIOqbTMVcOFeFwhyoCnY0pKbSyrQqtL71Qi1+I2ltV9mq7Ue57YQ7oM1+Jp2g3Ilj9Dl4md1PHS34bEsFDSYwhFt/EBU12VQNfOafCu9wRkaF22iEcQxMVcZnWW+CUWHdPuKOBroWn0g52R7NHGTfpU7Ai0T1dtkVOonPCOXnb5bStT8vLC3up9NiJgoMQkRY2HKYWd6t516Sqg0HJAR8Si7ONBb/UtBJErKsKrbburi/N0lrAiCQWPtu32avqTgu8ns0ovUM+1w02nMXW9oRMPOeE63dSERqMOUdmDuctxMvLvINdGMqt7m12iDWyZpDYxTlUcSIcojOpelklsgz9RWJG2V/IHWGsSxTEuSOtEl2RYNWGOKFcaE+GzC7oqBHKK1p1AHxktb8BNgAmVy7njolB1uipRTUnnRD/J8rYadgwt3mHoCsH4LdicrUmNQTTAIw+vVWa5cj2kjKEBvkzdNgcW3AmVh+q3ZLzdN41p3pA0Dzxmxyu3fXahQk9qLkv+wGYpgDlk6Y4Bo2oCvt9FY0HtBailt7isoTZpFXdFvTQ+eicpe31vWdOrj/bmNJjQ+ujKRJL4fK6Qa/N4XlH0XswJxKNKPWf9pcWxViJJDUzc+z4ednovnAYn3qgwh2CTtWaBLTS1Htz+tL2v9E2ZwmSV+/2WcI7XDj9vbihFp6Nx7MCoKyIKQYhws6MQORs9MBSEW4uJ/WB9M7HAzSzEX46MLphnx74vuTK/bie8pFtaRJFgH1/IiCw2Jkhor3R4X3GO9K6BhZ10PILGBC6xi1wIAR5KmX3k18GV17p9WpZI7F7Cm6Lej3UoT+jEnQ6raxUFXt+L2zYb1zItXFgiJK9hX2SxnHDV7cDQDRjY7W2rHqFMvGauGVLQam2lBNYWO0WUblhlLVfN7j7i9CFCLwHGntrbdCodlphya2kNISUnlXC2UYFZEbk8RFePRze+DZNnBsuK691YK9CtSH2ES70lUZyjeyovz5gQOeE+2U/rqByq1CViRNdFsqO0S2M77J0bvG5fNtGho1sURfbOXjcHv93nGd+LhyYp13cFsQa2W0by+Ywr2B07UHx2kbUlLuUr6kxUzo4smPvhaKFVCdfXet+cjuusbtFJqhLKc9JevdrRmLXdzZP5iT5WWUJkDiMKZATX4mplH6+nXZpAuGJb2kGMpWTlM0eVTi+o3abqBhSkyZ9/7WgZ2/KW8MCNg593Ppze6666u91VhQILBGN8HWESCihD6t3j5QyJ+S5HPdj0ehg2br5kKjSNo/bSqYiJ6IKzv/QRzaOhjdwFB9Yyqt7A6czrsxE36LttNki7D279SjAwRvb3Ze3Ca61fJ56NXqh4s81sHE0oITqeL92x5XzZhGrPh4zdaoooDXL0kLrLp+10aqPM0ol1HQXnfpTM9XWjk8ZdqZeJn0BKIHH4xHhGhmoSTpQGMFrLQ9zRvSS1xW13q9CA4nI1udl6c8k1xe0gBnQy2NE6U5vST13f1darrXp10KmFxDuIDLpA9+3F2cbjPXGbHJbV+DDQdYNJvQ7BXam2DO1cDr0TJvxGvDCOSDE6bFjHJYsp6K3ifQuaWiPI7qB9utyP9BbbBFmm9ztWk4frxarosl9mwvbi29HO3E8bO078pe514mFFZYllYo57N48FLSWbvc3mg3u7szu6N2+5A0YdA82VI+Fs1zmOYIFdiD6Ek31ricSy5lB55FHIUFfH8s7W01ENoW4QQIbtHTBtkj5yjqcd7Z/E0mi7tVGwvqYwZX2VD2tN4rucqO2zjOsdbrlRs1umy/Sgtc4Sql3yEjSkShpH24RXtWDC4z2oeyOae1FGTnBpSu/YCiGF9V5u9huBQowjJGjmyT8ccIiiG2KCkYHfwoHhLs14xVimhMaFsAS5pC2NI4njQ7cU/Rrp9alfj5ZzdulVMpB7iQyOuB8X6Eamd0nO1oWz9a79dpPGbKOOHodj1QTL++7GQd3G2REhUhMUokg2jVL9Hg49zRQkBGGjQ+4nJD35vR3INJhCl8fyxnZIct2zDhUfTpx3JfaClHNBNTIuF5n44QJhmuMVx14n5O3WWg0rNdMiEh4vO8X0nM4/rSHDW6vOemMqeCcz9BU/B1m1Caw7PiV550zB+WwG96bnPSjvvIxKpAym4ybbGJizwkDmnmMa36whKQ9Oa11nCdSmhvRQ7+J6W9kx0SKg6rr90Es7xIvAHAahLYHmndnyl5DGNoUhLl0HhWtTOkMtH6zGtdnrACd4SvHhJTKs73KWI5eByDVydQlaygpWbs6QI6THbHK/dtxJDJ3+oh/55WmjrlkDNfhe33gEFvOd1It97Pidt+f06L4btDyI7XUXSZoah1S/I07Kfr+TSXmUqIz1O94fhvvOUZuYDGgfNvmV6ZfRQEXZsm9NWmZWu0w7GuvOwodLa+2Y3qKRLT6eefGs7vSk5MgdW/Z039sQkDa40attxVAuqxUDUW+HPNYNf0+oebEayW3ioyOxlVpTFGu0yPPL7gRDO4hV4xL3TjeGefvw9v1c7+1ffEhtPu/5f3a09Dwhen/85HFs6dve5wevz/+qYH/58Na4MRDreZTWZn34Oo76m4O0j//cmeRMY3o+A/Z+NP08XO/scH5W+i0uvL7tmulrW2aPB1HADqdv5ycr21lWQKP90xnsS6HXcezXrnxpNB+ixcX8eInvxXb3/jV8nS5+ePNeJ85flyTx1W+qWdfXIwxAxeUn5NPy7a//G7E6BUXXLgAA -->
