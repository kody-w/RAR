---
name: "rar-cowork-cookbook-scheduled-brief-define-service-terms"
description: "Builds a morning brief on define service terms from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_service_terms", "rar_sha256": "0f84b9c57cc88eafc20609ee85918e86654996a9095dc7c39d50779cb45dbb92", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_service_terms`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_service_terms_agent.py` and in the RCI capsule.

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

Define service terms Scheduled Email Brief — Builds a morning brief on define service terms from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence/time for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_service_terms_agent.py` and embedded as the fenced Python below (sha256 0f84b9c57cc88eaf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_service_terms_agent.py` first:

```bash
python3 scheduled_brief_define_service_terms_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_service_terms_agent.py   # or on stdin
python3 scheduled_brief_define_service_terms_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service terms Scheduled Email Brief — Builds a morning brief on define service terms from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_service_terms',
    "version": '3.0.3',
    "display_name": 'Define service terms Scheduled Email Brief',
    "description": 'Builds a morning brief on define service terms from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-service-terms',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db3269076f986951',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/define-service-terms'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-define-service-terms', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence/time for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define service terms stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define service terms for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define service terms, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on define service terms from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the', 'example_request': 'Give me the 7am weekday define service terms brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence/time for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a recurring (daily or weekday-morning) define service terms brief for the responsible owner, drafted as an email and a Teams post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineServiceTerms(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineServiceTerms'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence/time for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineServiceTerms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1Hf98H2U+ZlHpQvKqIBMWhAAoSEwOlIM88zCJDb/70PkjLTrnK9ruroT62MDA2cs+e91j4Xfnuz+y4qm7dPbyffLhainWVx5DcLu/AWXDmUTQreytQB/xduWXRN7PRd2bRvH948v3WbuOrisgDb2T7OvHZhL/KyKeIiXDhN7AeLslh4fhAX/qL1m1vs+ovOb/J2ETRlvlhPhZ3HbrvASGLBa8rCszt7EZRA/SLzQztb+EUXd9OHReN3/VNsV1YLYhF3PhDiTIs4r2y3+wDsLXM7i/12cWsXXeQvqI+ePS2aEvgDdtk3v7FDfxbklnnuF57vLQp/7BZgN3CgBRIWLVjlLfzcjrOF19hBB5TNsoCv/mjnVea3b59+/uXDG1CavX367c3N7LadQ+dGvtdnvsfOPq8f/p6e7uqzt0BAZhchWFlNINoF+F75DfAzBz+B8Cxe335s/Sz4sPjP/0wHuwnbnz59Lhav1+e3+Z/WFw/nutJuO2Cra1e2E2cgRO8LJhvsqX1Fak5EC5JVhO/Pnd8lgfj9bb7241PJe+h3P35+K4EJ9hyJz28/LUACPr81/fz5fZZS/fjTe1YOfvPjT9/ltL2T+G43CwNWv395fX+JBQu/L42DxZeTwnMvXSAHceUD4X/wb349TX+Je4Xky3Pxj2X1YfHXkmd//gbsfZajA+T+tVgQA7Dz7T0p4+LHl46mvPmFXbj+jz/9M7EgtW6axW33L8n9+Sk48m0PROsVkp8+PNL3y2L58u2bzH+utgIF8+94ApZ/VfctUP9M9iOzfycadAnona+5/Etxf7Vh+bfFz//Ut/9uw4dF8Plt7Wfx3JhO5n9a/PYokZ9/8L7/+MMvvwPR/0cxp7Jv3IeEL7ldxIHfdl++/PxD+/j5h19+/qGvQBX7dv6lb7K/kvlXcX3o+VMEX6t+/PNeoP9cpEU5FItvPbT4raz+R/P7++ICIMn7/nv7afHHTpxfy8XsxFelzxD8oRtbYOsf4vjT2+8AfQrgTf+ELYAf//EfCzl2m7ItAWCd3LLvFiDBXZz7s/F6FLeL+AmJjQ/i2sYgsK91oP7nDM8Wl8Hi1//pPgD/o/sCfKj9imtfHmD+5YnkX15I/uWB5L++L3Qgu2ziMC4AYmuMonwuANYW3ay3avx5OcAqZ+r8j6ClP84fFnGx+PVfEf/lIem9mn59UFL8xD+N28zY14LN77OXRuQXL59cwGL+6Ls9UJKVLrAoiAFwz8jfltkNYOcckTaNMwDyMUAXwGbTQzaI2qdZ2K+//urYbfS5eII1tnjSXAuBBd/MWXz8CFwLsjiMus+F70bl4offfv9h8b8W/92uh/BZhwKI45UTYOH2dDwsQI/1gJg6kC6QYAAgj5z89vsrwEBMAXgZZDAOZpqbN4MaTX3va7RPEvMRJciF44Mo+zMzlk03k1/cvS82weKbvUDpfGnmiKhsO0DQ1UyIhTsBqTZw51ski7IDrNjFbQA4uG/9h9ZfncZ+mJiDZre7XxcypwBGKrOZLpsXQ4HNZRGD8H+rhefvQEjzQ7tgv4p4XxzmqlxUdmNXUWO/dAT2My/zKPDaDoTbgLKHz8VMv/4cqkeLPMMDFoHIuK+UfpxzvpiZHiS2/ar7scaeeVN/8GfzuWhf5W83/mM0AKZMi7CPvZkU/utVUm1U9pn3iB+wdJb0yoL3ysqjBtd/NeZ8mwwW/GOseAwIi889CiP44v/jkWkOCCOKGi8yOr9e8AddM5+JmofIOaHPuRNY+jD+0ZTfp5mviPUVuD8XWQyqrpn+67nykd7XmicY9g2wQ2O0h3xQWyBRs9xH6c+l3DSzo/bn4itDzNY/4BCEG+AE6KPZ9K8K56tfLY0AGMzfv08Lj5A03owaoLwXVe9koPQC3/cc202BVc3cvq8sgz7w51YeotiN/uTVnCpQbkD+nPMYNCRgkfdvqP28+tX0P218DkXzlsfA2IPcNA8BwA5/NnDGsyHuAIjZ3XNmB35+eggBbuRVN/vugP4Bnj5/9Bu/7uMWVEn74RVXvwJY/XF+f3o6/+qPFWgZECzQGFUPovtopblecjDyABtA7c7lGhdgBABBeQXhIdDOZ1wAuPuaUZ8SHz+/HPIf/Tdz19eNsyPznnkceHaAXUx/hA/9r8oEyMvnFQ+9f19p37TNsmcIbQEMAo1frz7nhvcn9T9ni8VXuZ/+4VD04793bnqQ+fnPBfBpEXVd1X6CoCcBf+Xfd9B30NPW9jsXf3ygxMcnRHx8QcTHB0T8SfbT7U+Lf8++P4l49cenBfIOv8Pzpf2rvl4vEA7uI2t+xOernwvN/w6xQD2Al26mgGyaYecrH35dAkgxbABigcVPfmxnWh0Akz8I4QEifyz4ueEA3xThXKBt+QcgeAwGoPififvGW+BS0QHd3jxOhv77fAqbzW/9t09Fn2Uf3gCU+v/a8W2mp3wu7HY+94EWAgNaF/uPbw+cGLv545+PxMfHBzt7X6x9gElZ+8fie5HKTKp/6JGnn8A/F2j4MIM7aH1Ql8DPWfncX3YLChbU6uxPN1WzA8+T3jwbPijgy5MC/tGg9Uwaf2SJGfLqHvTch4X/Hr4vzidZ+Eu53wbSfxRqgBlgluOVn2Y6/PACGPAODhEfFt/OA8Cb1wlt1uAXPTj8/jyfRebwPrbMH8Ae8PZt07c/Mzj+2y9/ZdcAiukfbdL8tgIM9Rh1H0tAXZVzcH1QC880PNjqG3c9euovPf/ad/88vaDg5uHJhx649RVFHhJfYR18P52p9cXzgIe6BWXnf6EPKHzgMGCzOTrfw/7d+fJxKptNA8Hqnn9E+O0NFKc9jwKv8nyN9WA5gK2P7TzGQKCJgULw/dlu4Nr/1cD/ktFGNhg2gRA4oHFn5RKU69K0bwcuCpPwyvdpYoXQPk2SBL5akfYKXhGeS7nYyiNgilq5Dk54jrNCgbxn436Zx4x4totYUQG8WqEBjqCwB4xAcc+jSZoEWlDYXjk24RAr2/m+NY0L7+Xs07k5kt/OHnNQXj7/9uaQOFgp4e2Geb44aIU4EEo5WuMsrzA9ZkPnnpz2lDnAvswmeiOKjzCYZLSbSZ7wXUNz8rSV+DzeWus8k2Tm3qrLQacqxaWIwTqnx11bIbC/XPXM4BvTNr1bNKXM13wCx46C0RyFC1cvN+S6OpcXR7rg8d6td9HuwunHLtkex00bX+LbmFDQ6upMJR7rJ7WsukutjX1k7YPKyDZ9mXRcPTV64lXXjRMhFU17xhXv73RjRunOPdc7mMnPRm9xW8NwndyJ+d0lOwmO1RT4GbjIVFKmt7oDtmeaHMIoXaaXrHJtROgzJSLFNvd2+01aXorJiC4TkKvmIortSnSILtpqx1zyEclr9SyUyabm8RIRwLKLsRnLteooVwomFeyGQAfMqvWEojqMSCgCj6Yrt+cwttyyl95Nd7SctxnRmTGyzt0oLVbcgELCidiHbdbhcnqN7AldwwiDeGPZl5EocALK+eZRWi3vvZptBXdAnQQe/fYUbXrOi1PJIApxR14qathR8CoWTvv9wDUK6zWwe7MxAuPjVemviPSCNpedpbJlnsQct7I36wLRd1uVEk67rNnRTEmH5z2PpvDdXrNObHUHSSTs5cRfBL2Pdac+nqCJPAUYi7NYd2+mxjeIw0BXI5iEuFNm6uczn7BnWuLwymRgKN7GOMYguaE5U3vikXsVSssOy7Y5Qu3k1jTu58Ol3i4bQ5bhlazvzsurThjE7obl+5XAribhYqppZF188xIpZZ9SZSquil2sxOzN2m3HPJfHSbqB6XO719U+pXW7jHBYXyKGwCY2p3Opz+5HfalkfFTlLhFU6xBfZ+YuanQxajKDQSpTpLdbr0crY9NtBnJqu0OUGfUKqhuu4lgv3bsuH2hnBNmn5JSTEz7UUGuXBWQWp8jiKj90VjhD8/ro46octUYgOKVsJEv44OBX8b6Tu+COnu5pbIseQSusVVqa4h2Q2zaajtvYNtYc0hrrXesyoB1NWhghqTjf2L7dusHRhGgLCu/WslW8DOLl63YlGwp8h2LCZ91GO7v6drMyxZznd6FbL/GyO8ZDrBxO92UZhZfpxsFqtpYtieMlaqnifuh5ZsYcBXuFpZelIFZ5O2kETFAp5WzOLbYsd1olZgZXIlfbzLNyTFKk45JoCmlus7dh88Ao7BFjVjWvYXvvlNP9jd/nS0u3ckOSsPZEa8h48dc3Gumj3Ii7oiE4RtA2oLM0Y6PyjSXGW0PgT8WJDu8cVBOI2NKw3ocFaH7U30XlZhqa6zmgj0S5IkfZuNuU7FtegkKZ2B9QK1gfN3AtHtIeFgpOvvI47x6y6sTnjXrkx4iDSCvfprdTVWIHUuDLg2V4bHkZJvdccpeMl0VyCTWoRK6KS6ppBENs+JruJU6OvBhagxmlUVcWTK0heXmpBNXM9kLMW4xZj5pChrzbu8K+PGwbtDfi1jq64xYVzwxgAgrPXILuKpNY4/jRl4KSoh1nazcE7iAHn5cvww3arCCGWBpHVejXN1mF1udqeQc4i+wdprML3nAFAWvD4WLkPB4hAbOrdsKkYoet1Y6GQZ8auPH9KcVBgLBCzA8lE+b+bWrrg5cDk4/r43rHgTnxRkusS5myJy5Ly9DO27UzFPa+1+1byh/rwjgc6TF1pusgK02QThMpYBx3Ud2Vh7BrzofTC+8tpZvP4wguBF7FSjFz4YdaOtgJ76wv/EHCME5PxVxiTykx43rAaqa2oVAtMgtUrjbMfqPl0eaQj6GZWKzoIMTtSmHTejmN7jnaqhMd5TWHlflVG9c579yvKjnsbFYbgj2aT7zNN5vovgmO1qbchS21Oez55taeDxUixvqm2YhmQ0mkfvbxmj8JDRuEfpnKndhHFHmMqMQzmq3fWRto1zk+5xSO3pp7S257Qy5lqNXJlXJvSOq4OzJnMqSHO64ZOnnYdXxJmK5MByijlrR3Dm0L8ZVVcT/FWIUk7BI11dC87B0IB6JvRXFfIX7tQFBT5xMNtZiVbbHsUB9tS4JrdLNR4Wlr0dJqorNNZghCkSCn8lgPquZecTOKjmXtSAoj3A/jNWBwLL4351qGVWGkqvUed+RxbXTcKlIjHy4jdFLFKRLY9CxqKl1WGYPmoA2RtpU48RwTBB3iNTcJy/MYSZl8vFxSsroIJNL3NIeYtXGxVAK/R6YxWFTqX3riTt/5LE88BRw+72o9krkUeRuV6WX2VtZ6tLexJTxE+3qiLEZP2YhT+Jt/CGVTLFYxnVllu7pxQnDNKG/NMJpJrVghvJ/CYSPrLY5RB4zHeOWkxfhNLwiOtzmEscRMHq+MNSD7/UnZVuHJwLTbUpmYO9ezom6TDXlqKo0pVY7A84tLSht7CMeDpMSEWgtry4V5zxA92XIvGoO4ObJL4bzq3dhbOok9sdymIZfclLRpofJJwCgrHGJL1dgPRmzfT66oVIOaTtVepvWSO+zpso4TeaxJ6bRWmJOpEtE4ntKu5JaooW7HaYnvI3vI1jHNX/RAWGn77fnG5XC7g8WB8dolL8HK0JA+Ym8it99L29uWv6oUj8mgiUPlvAlXNi1G5lZcwQc2lNUiOLjnQbRB7tj9oHEtuTnvl4nmYuV0ZldcZNzHbSzrUIw3V9TeDIYnhE692WmZQHGBnI+McBw9IKq8dO5+gxwMfj1ZcTxqIptc/YS8QAf5VPCnsCUPQTRhZcx2agBGpESRriSquOQ23wZ6KAQB1l8051bdzUGQtkkUeTm6J/B9fmfidNc2JBM47Bk5iSOcw/dQqPx1THnFtjJ80cf74iJo5hiJzllAEQTmltJ1L4Wp1bVtYsAJu90eV254YhDFZhVpMiqzstGGdTXrJJglVDNVp6143SICmnXP+zOaMZf4rGGCs94UEI+ZsKpfOpjgCirY51UA+VdpYjPQBIaoj03apbKyZsRzZNWVlgukEyvGCaZKWI74tTH5RWIk9Gowk/KAC1us8R2ZRC9VfWRiRoi0rXlJt5edCwekLsIsDlkkUapt6VBVf4coeHlvD/Wp9DpYASxkKbaPFWRQdzLXScOxwNbby3lgiqW6pnibcPfQOZX7DMJux52SFHVMxCc+ZbQlanMVHzrayQJJHENXyygwpN05Zt87F2L0NQhtKeyq6LuR9Qs2s8lAQ5h6KC/sYXuCMXMi1DQ0hvi4zfTUTJYqo5uitdqfG2JPnqqDm4t0HxiYUQZXk+1AMx+r07pn9DKYkD1G4r6inCglFNVargi4KVDJk4NTtzxJ4kUUeDXpxesZznQK250AH+zgFVwFG/iiHJWjsYOhIj9YvSDVcVj1BgQn8jaIbZLdncocuROMqatIJxx2dZkVPvhM763DLjcR5jSJ7IUOu6in182OOUU+ol6Rwy3b7Bx1coYrezjABaxPezMMt5rFSgyUXyar2pxkLueuHJGquYXip0Z24vBYbrbCwU9aQ+GNeyzWphQl+hKjYVqvLV69YVWyQYNdUJvMhTZrltys1W6V4mJTUCq2P7O1eegTAi6Q1Xh0Li2eBzp/6Y+ngmmIlSV6le0oaMGzV2o8DuRpxwuj5Hb34CRvdUMR+GRrJc7tvOxqGOZaTzLgdsOvRjnMU/t6P3hbv79uliUJnxRUQ07r88nGMzXiHM4drnB4r+vY23dN6Rm1fEECZ381Np5mXKtMOUiOhk37HJxF/eoUnmpZrM8OFW7NrkEJQd8EY4oyN8YYtZNJCVODhzbPwEm9uwudVMW8796LnVmputuB8Rnt4ar2azAJ7Mv1lgIZG8q95afwXqVRGInJhmsj/owvGQGL9qednrmhfsSq9gYlFumMo6dGZ+y+xpRjFlzlKyZ1ewxDjb0jKClUXvEh1SpWtIAbYjFd+dyrta1wvwPQJAq0laUK45F8R5IBP6nH8CjGiQQfuOlgr7SmZdm9BUaGo+s6qgPGc+CBeXdVuNBXho2dN1VlJKacWmzA6EGyPtBppdzGAW2mIl/zKItCGhpREILFpOBSxYEfL6onaGJk06rJ8MXdqJmmMarVkrqeNkdUy8R9Z5yMWO6NBupzaeg8Gzm0XqvTy/WoqNtV3m0ZTiBoL21ohgVGivxd06ApCBnS9bTGdc/BkS1PfZoRenUyb52Dsu0xWXEaVrj+4cr3Ccfm15134lEwf8lU6opHf0iQTp/kK7EpKIQAbbHRj6QHw6oiYjKBNHuHvIYH5lLQkyFgt9YPkNglemUQcdLos4Rmt6GxvQrVRQwT76jmyPmqb4mw3uiRge3MpYNP7tK7b4oL64nn5Wpztg8ryAAd1UJ3Vd6dye0x7/dnqUP3Qdsv4dN1WFZ+390qpEZJFI4GaDxEg1vTws0YL2TgNld+u4SvWAAsnfRRvqETfMGsvqObRNF8z/fG+1mRLKhBSkGiCXxn6jV8F2IK67WB5QTxYun5Tfa7YkOIqbBs0rree5mStbCHxnUX8BuNitfuxRqh7Iaw+7Bk/UPtiZChQRKzDtejpl5IycxIhNUdUbt0ndJcIMrYqxme0PdLoLY4ctJuyN4nOYJE0ON2lQ4TXiiSlmReink51mNe1+4H2ItumqokpYFepXDVJtAmCCDaCVpN3OqFVd4K0oGkZFzjTidiBe1XopDfupFnT3B1tc8aTNL9aDowIPd1jrkJprtHS9nx7LpZHTtiX/qqxu7EsYiV0lZUaSsH/UiYBATnJiQ2RjFO7eRKZGKGfHD3OpZAmaYWB3bYHfR2wva9LHvbOArvzj0ufWXpWf3e8DiZQo1x1Ab7xBCaCC0PCHgRq5N+tPGWWjKs0mOy1ebSmO/0sU5ZLjiZvYBhp+6OnGByPQm3Y9+Lidmifgx7YkSIyeq4w84N2QbtgAREoW5NRt+GLPiPB4HvH3tKHnENHs7EobLJUTDUDE7S6EJZ9aGpl1ehvKwPvVAKWUcxqIlbqEcqhn9WDNlMmDs9tsvAV28je93h9MYgxw1inzbR2eLLG5v62Y001L4OS4FJkCQHDUfgnROWtuHkwzEmUhIO90lr8Qh7tlVOxGIZDdYok2I8gJwkxwpZWqOVYlxWhMXkpytC7aBLOvlBsKSo2y1jYgO2mFGYoPt0W02meS7K1bhtjuial+h7S+/3dT7cJmqdGcVwIoZ2Kd9uvhsVbjNU50K/SR7sTamBJzbshrgn3OXk5l65g9vkRVuyJ27kcsF1HK9oNni3dkcUtq57BwzTMK4hQnEQEAvnVjIuYDhODn1Y0Qo4dejCSGyhrmmlyZdzGu4S+spcD761qgBN31VdYo9cV7YUbNwVGmlPhLROpQM6LqWyza/l3W19maTX/PYM2DtDqH4whXS9JBUw9ft5udE3/nokhow/aLcznqxc3pBEWzBW4VqXOug+uI5CJMatUgmHtAkEhcAAFwQ9q3rL+1pZkx56DIJyShv5fuzXPQ253m6/5CQ/XXq75Gh41FRwXRMEuVKu8OV6194Mt61FRMxI69BQ2johuyhPO8wyL65VWxaX3xgYvjsGVRzvXubXd0BrYG53cbwz75VA3vOxWCfXbN1eYxyKa6UWR9ktllrNInxea7m6Otkl1kju3UlgcLo8L/tLgbVmEl8H+mowomP3sRkw/W7TYzohy+FVGMkobIQld9iAdjxeB9UUe22jnPHpQNVdsylzAYaDgRUkuFplsJ4dIVJ3vS20qTmWJkJ9D8gt80nrOqL6ErlQAlYNK5SXMcaqG19SRpXbpV7Ipt7QLWsOsnhUVmCCtyyfbs5KM1LqlVqaitZVV+Jylqrh3Dhohhpg0OyEE5thY6mBYr1pZY15JNFZepb4AO4drW9sAoWqzKz25hGhchGcZW8TKo92iEy6aEKUEJriCqrkHJNq9rIKttJhpYqItcvJ/QSh1lYtE22yJNxergPvxnT3kPOLm2CmGZSHjG2DAyLX4XtWwy/dBa06XHGR0jAOplbQMh6N9/zgnY7K1SvIS++X/aVTVvDJOkPlXULrzR0SO0MjJoog7IG2IN0qLokdJptE4SWOXaXrIuRhU9TbAMID9HbbQ6qprldLTffMfStk7s3IXYntOjQ7ph67msAEV1HNbugyWolrwyaoUtJvaW8xJCvugjOKJcSRP1ZjayFgLNC3aQKONbaAdPcMcruuj1fxBlXurNVgtzPdVZis4cWSRbZmeNNVkZ8sUmmwY4RXMoagGjgAFaHspzq32bt0wjOpcVya3GEE004rMBuvX19wNy2uHVHDRBgVWcAla3aivVtr3QekuFLXcr1MJBV3TDOPKGEcrhcWcXBLuyKQq12xvljC7bQkAZxkCRreVvYWOh+XkOhRabcMA1RhqIsCYaGhjC0msfxA+d6pA+cCMg1P+8a6Afxx9hB5ZKgb3qb3xFZwP+gc8WjQiB36tOTjAN46TOyc7JIbB38XEJ3YmUaCpOHqdgskmhn8STNXGYFWQYscsF1BUrR0uLgNXuiHLb5BOLViMLeRjmd4EDROqEhzQ1dKG6W4ImXYuQ9EAA+tddwQ1MaCDqWIMGS61gb/qNMRr5KGU1yLveQeePYWUKKzvnFU0GGQeUPKA5sEkqL0B7mj6guh7ApXXWZl4vlURgurXSCPvEGMe9zIYzErVEE+rjVf8lwsofslpBWDna67QahdqNgYS3t7GMVQM+zgLoU7WaKGXIb0Sj5w7UoecEq6DTdJzABpeCzDMH97+/A231N93Rn9t57Qmu/G/D+7KfS8f/P1gYvHnULf9j49dH3698z65cNb48bAqOcNsDbrw9etor+7/fXxX7nHPkuYng8/fb3v+7yZ3Nnh/HjwW1x4fds105e2zB6PXYAdTt/OjxO28xOnLnj/4y3Pv3Nmvvtpt8CJ8svjibWvIuJiVu97sd35r6/h697ghzfv9VTQF4wkvvhNNfv8unkPXMXe4Xfs7ff/DRNbmrjsLQAA -->
