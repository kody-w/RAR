---
name: "rar-cowork-cookbook-onboarding-checklist-generator"
description: "Produces a role-tailored onboarding checklist as a Word document (IT access, mandatory training, intro meetings, week-1/2/4 milestones) plus an unsent welcome email draft from the manager; call when onboarding a named ne"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/onboarding_checklist_generator", "rar_sha256": "061e0ddb67049f3ea5f387b837786f05806ad2673074d9ddad00d78e9ca61a1b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/onboarding_checklist_generator`. The original RAPP
agent is preserved byte-for-byte in `onboarding_checklist_generator_agent.py` and in the RCI capsule.

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

Onboarding Checklist Generator — Produces a role-tailored onboarding checklist as a Word document (IT access, mandatory training, intro meetings, week-1/2/4 milestones) plus an unsent welcome email draft from the manager; call when onboarding a named ne

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
  Upstream entry : https://coworkcookbook.com/recipes/onboarding-checklist-generator
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
    "manager": {
      "description": "Name of the manager the welcome email draft is written from.",
      "type": "string"
    },
    "new_hire_name": {
      "description": "Full name of the new hire the checklist is for.",
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
    "role": {
      "description": "The new hire's role or job title, used to tailor the checklist.",
      "type": "string"
    },
    "start_date": {
      "description": "The new hire's start date, used to anchor week-1/2/4 milestones.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `onboarding_checklist_generator_agent.py` and embedded as the fenced Python below (sha256 061e0ddb67049f3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `onboarding_checklist_generator_agent.py` first:

```bash
python3 onboarding_checklist_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 onboarding_checklist_generator_agent.py   # or on stdin
python3 onboarding_checklist_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboarding Checklist Generator — Produces a role-tailored onboarding checklist as a Word document (IT access, mandatory training, intro meetings, week-1/2/4 milestones) plus an unsent welcome email draft from the manager; call when onboarding a named ne

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
  Upstream entry : https://coworkcookbook.com/recipes/onboarding-checklist-generator
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/onboarding_checklist_generator',
    "version": '3.0.3',
    "display_name": 'Onboarding Checklist Generator',
    "description": 'Produces a role-tailored onboarding checklist as a Word document (IT access, mandatory training, intro meetings, week-1/2/4 milestones) plus an unsent welcome email draft from the manager; call when onboarding a named ne',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'onboarding-checklist-generator',
        "upstream_url": 'https://coworkcookbook.com/recipes/onboarding-checklist-generator',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '90e835672b405339',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/onboarding-checklist-generator', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email'], 'plugin': []}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: No D365 dependency', 'Output matches: One Word document and one email draft.'], 'confidence': 1.0, 'deliverable': 'One Word document and one email draft.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'manager': 'Name of the manager the welcome email draft is written from.', 'new_hire_name': 'Full name of the new hire the checklist is for.', 'role': "The new hire's role or job title, used to tailor the checklist.", 'start_date': "The new hire's start date, used to anchor week-1/2/4 milestones."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts hours of HR busywork per new hire and makes sure no role-specific access, equipment, or compliance step gets missed.', 'expected_output': 'One Word document and one email draft.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['No D365 dependency'], 'prompt': "I'll provide a new hire name, role, start date, and manager. Produce a Word onboarding checklist tailored to the role covering: IT access, mandatory training, intro meetings, week-1/week-2/week-4 milestones. Also draft a welcome email (do not send) from the manager to the new hire.", 'steps': ['Paste the prompt and provide the new-hire details when asked.', 'Review and personalize before sending.'], 'tenant_caveat': 'Validated end-to-end against a live Cowork tenant on 2026-05-23. Generated onboarding-jordan-lee.docx for a hypothetical Senior Project Manager (Jordan Lee, reporting to Mei Chen, start Mon May 25 2026) with sections for cover block, welcome email draft, Week 1 Foundations (manager pre-arrival, hour-by-hour Day 1, IT/HR/access provisioning including PM-specific tools: MS Project, Planner, Jira, PMO SharePoint, project financials, time tracking), First 30 Days (project handoffs, RAID log audits, budget reconciliation, stakeholder mapping, PMO methodology training, Day 30 deliverables), and First 90 Days (baselined projects, owned steering committees, 360 review, stretch opportunities). Every item uses a checkbox so it works on paper or screen.', 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Produces a tailored onboarding plan and a welcome-email draft.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Produces a role-tailored onboarding checklist as a Word document (IT access, mandatory training, intro meetings, week-1/2/4 milestones) plus an unsent welcome email draft from the manager; call when onboarding a named ne', 'example_request': 'Create an onboarding checklist and welcome email draft for Ana Diaz, sales engineer, starting March 3, manager Kody.', 'inputs': [{'description': 'Full name of the new hire the checklist is for.', 'name': 'new_hire_name'}, {'description': "The new hire's role or job title, used to tailor the checklist.", 'name': 'role'}, {'description': "The new hire's start date, used to anchor week-1/2/4 milestones.", 'name': 'start_date'}, {'description': 'Name of the manager the welcome email draft is written from.', 'name': 'manager'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a new hire has been identified and you need an onboarding checklist document and a draft welcome email to review before sending.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt and provide the new-hire details when asked.', 'Review and personalize before sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class OnboardingChecklistGenerator(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OnboardingChecklistGenerator'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'manager': {'description': 'Name of the manager the welcome email draft is written from.', 'type': 'string'}, 'new_hire_name': {'description': 'Full name of the new hire the checklist is for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'role': {'description': "The new hire's role or job title, used to tailor the checklist.", 'type': 'string'}, 'start_date': {'description': "The new hire's start date, used to anchor week-1/2/4 milestones.", 'type': 'string'}},
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
    print(OnboardingChecklistGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WZOjSLbmX9HEfaiqS2YCYpGUbW02CCFAgJDYobItix3EKjYBNfXfx1FELtWd3X3bbJ5GmRFicT/7+c7xcP/9xe27pGpePr6ooVuuWDfP0yRsVm4ZrOjqUTUZ+KoyD/ys/KrsmtTru6ppX969BGHrN2ndpVUJpl+aKuj9sF25q6bKw/edm+ZVEwarqvQqtwnSMl75Sehnedp2K3cZZ1ZNsAoqvy/Cslv9zGsr1wcU2nerArB3AZtp1TVuWoK571YpYF6tijDswC0Y8wjD7D0Kr2F8VaR52HZVGba/rOq8B7TLVV+2C9VHmPtVEa7CAsizCho36lZRUxWrLgkXNm4cNn9Z+UDt1SMJy++ldVelWwAFyhAoG45uUQMuLx9//du7lxRcv3z8/cXP3RY8epG/zqK/qMiGZdgsOoDJuVvGYFQ9AVOX4L4Om6hqCvAoCKPV293PbZhH71b//d/Zw23i9pePn8rV2+fTy/JP6cun1F3lth2Qy3dr10vztJs+rKj84U7tqgm7vikX27bAU2X84XXmN0pVvfrr8u7nVyYf4rD7+dNLVS+iAj9+evllVTWAX9Mv1x8WKvXPv3zIq0fY/PzLNzpt791Cv1uIAak/fH67fyMLBn4bmkarz+qFod94NaGf1iEg/p1+y+dV9Ddybyb5/Dr456p+t/ox5UWfvwJ5X2PRA3R/TBbYAMx8+XCr0vLnNx5NNYSlW/rhz7/8M7JfA/Z/RPfXV8JJ6AbAWm8m+eXd031/W0Fvun2l+c/Z1iBg/hNNwPAv7L4a6p/Rfnr270jnKUidr778IbkfTYD+uvr1n+r2rya8W0WfXg5hng4g7rw8/Lj6/Rkiv/4UfHv409/+AKT/LRm16hv/SeEzSOc0AkDw+fOvP7XPxz/97def+hpEcegWn/sm/xHNH9n1yedPFnwb9fOf5wL+epmV1QMAx5ccWv1e1f+r+ePDynDzNPj2vP24+j4Tlw+0WpT4wvTVBN9lYwtk/c6Ov7z8AZCnBNr0/vM1wI//+q+VlPpN1VYA11S/6rsVcHCXFuEivJak7Qr8X1CjCYFd2xQY9m0ciP/Fw4vEVbT67X/7T7R/77+hPfwNCb+59XP8BdV++7DSANWqSeO0dPOVQl0unxY0BZgLONZN2IbNAFDKm7rwPUjm98sFAPHVb/+a8OcnjQ/19NuzBqWvmKfQ/IJ3bZ+HHxbNzAWrX/XwAdiHY+j3gHxeASRfRUs5eAc0bqt8AHi5WKHNUgDxQQoQ5VlXFtrAUh8XYr/99pvntsmn8hWgsdVrXWthMOCrOKv374FSUZ7GSfepDP2kWv30+x8/rf7P6l/NehJfeFxAoXjzA5DwpMrnFcirZ+UDLgJOBaDx9MPvf7yZFpABJlkBr6VRGr5OBnGZhcEXO6sc9X5NkCsvBPYFti3qqlmK4yrtPqz4aPVVXsB0ebXUhaQC1TcI67AMwtIH9TVxgTpfLVlW3aoFwddG07tV34ZPrr95SxEGIhbAYW7320qiL6AKVTn4tYj5HAQmV2UKzP81Cl6fAyLNT+1q/4XEh9V5icRV7TZunTTuG4/IffULqD5fpgPioASHj0/lUm7DxVTPtHg1zzNgUv/Npe8Xn4MGpVg6h/YL77egAlGoPWtm8wk0Ba8h7zaLK3xQAgDTuE+DpRD85S2k2qTq8+BpPyDpQunNC8GbV54x+K3or75W/dXXsr/61K8RFF/9/9wXLVagWFZhWEpjDivmrCn2q3eWVnFh89pdghZlBUL0NRO/tS1foOkLQn8q8xSEWjP95XXk06dvY15Rr18Mp1DKkz4wAPDOQvcZ70v8Ns2SKe6n8kspeAekfeIecDkAB5A8S8x+Ybi8/SJpAhBguf/WFjzjA3gC2BzE9KruvRzEWxSGgef6GZCqWXL2zc0g+MMlfx9J6id/0moFqAOHAfrAiEBU8PUoP3yF59e3X0T/08TX7meZ8uwMe5CyzZMAkCNcBFxA7JF2ALnc7rUzB3p+fBIBahR1t+jugaQBmr4+DJvw3qdt2i0A+WrXsAbQ/H75ftV0eRqONciTJUj7ru6BdZ/5szi/AL0NkAFACEinAoQgeOx/McKTIIiN17h5a0ZfKT4fvykUPpNuKVJfJi6KLHOWuv8ahm45fY8Z2o/CBNArlhFPvn8faV+5LbQX3GwB9gGOX96+NggfXmv8axOx+kL34z8sfX7+z1ZHz6qt/zkAPq6SrqvbjzD8Wmm/FNoPIA/hV1nb74ru+6+g8P5rbfwT1VeFP67+M8n+ROItMz6u0A/IB2R5Jb5F1tsHGIJ+v7ff48vbT6USfkNUwL4qQGgtbptAlf9a/r4MATUwbsJ4GfxaDtulii5g8sR/4INP5fehvqQaKC9lvIRmW30HAc8+AIT9q8u+linwquwA72DpGOPww7LQWsRvw5ePZZ/n714WnPr3q7OlEhVLOLfLkg4kDui/ujR83j3RYeyWyz8vd+XnhZt/WB3CBdLb70PurX4s9fO7zHjVEejmAw7vVgDIQcKDaAQ6LsyXrHJbEKYgQhdduqlehH9dyC2t3xsq/6Ms5yW3APZ8B93P6x9hPLDpA2QJgLxnnv2QEai5nxNQVj+/2u/v2R2BbZ8l4AtPMH61jH/tA77WsvSfq/K1xf1H6iboMBaMDqqPS7F994Zk4BssS959Iw8M+LbmWziEZQ+W078uq5vFo88pywWYA76+Tvr6VwsvfPnbD+RaKvQ/iqR9pyNoZZZBi99ulQdArMvDZ6f0LCyvxf3PdvihAdrObbrPSwj8W3bPoc9o+cYHlCeQ+z8u9T/gt2i24D6onouRvln/mw2q53JvEQ3YrHv968TvLyAtXMDZfUuMt/UCGA5g8n279EowgA7AENy/Jjl49x+uJN5mt4kLelkwHSHREAkCj9wg+C7CQpeIsO3G22KbzZaMEGKLkG6wJjcYssGDXRC4AYIEm224810SdVEP0HsFis9LO5guEi3iLJAKsCb89ho8Ct5UeRV9sdPXhcui8ptGv794JA5GcnjLU68fGt6hnmddvOnEQXO+HRO4o6SUSdZGM2CBWN43Rt5A58zxuuyEdh5dtftYZYhjnMRbU3B0N7tfJgGWRDgre9KhrnYsSGWIeVVm7vCU9mdkd9EaZEZuMyyxHnHK2V5V1M5LA/pymNDYqK24ZoiMc5y7GMFzt4FOXZk5hkC1SnqYzoR3lYzTXEjJqZbmsCUeNrKpfOSGqHrSGebprtuDVQ1xQunArfY+y5mcC9OZkg1bJpi7oEn6hjXaVrncxELdliKJy7cEMYL0vj45OZul6Ybj8fiOMCiT7w12l5Ws7d3NqwlTt+o22rkpGDXaKV567RhyzOE8Za7KJN5xVLJY/JBdFc+jaSXeclo+wRdrM26hYXP0YS7dRcPMYdjIDZfDmc7rzKXu53XRTzVqX5UmVxIzLihDPAbSDAvi8X5/VP6Yt/vN0SUyFgrJB9e09Iaz+b1hJOZJtOYaCiSu6S3ZORu1ugtzlfYJvGEu1AFzK2OnbQ+1QmSWkKFMybtWcVwXO0tE0EEgaLs6w/5m2glnKU5Vna9BvbpyE9fvic4eDeHoqErbxgOlXKo9PYbJmTfIa0MzxbHYOdCeTg66S51x+yhGx0cOF4dHCVpNDC1Ccyc/2rbKNOcwuvFpp2hiSZr7PVMMsWpMtX+T+Ol2siayYfZFIFHwOLQEvx6uo5Co2D2ZBeuCmndd0NtT5oYSWCsH6IUkaEy9wlmdrY+nJC8M4JlkyKBDXDwEIgGCToJa+xMmHdrtoSwxjZrZikLyfLdX9Hi+12u7YeJ5bydmiNBaWm5tTl2ntqcSfNDzDqtd7XVRaWReHV0WrUFmOGCZRp5UPrhD6sTs28kb+rUqtNv8RO8YGcbvm73uQDwy6M2sYlOWI8NWRLzhJM7ZKUo09pGGAudy2bl44Gd5y/KXgtu1bonnZ9P0jhs5rgi+SIowOuA2jlRbQ8ERWFsPfemOLWEJJ7KdL2NoTcSRf2izdD3Auxge62G4qaYDTzSDQMXMkUGEh1Zs7avepnJb7jA6yxJP3nB+qoqSYdimgnk8n6eDvymKR5QKGyWAul6mrlpVrq87v5/cC30L9m3qHMSjyCFmtnHks6vP9OXE5KIe7g29EGuV53w2aRCGu3IpbqBb36Ave86idnfGQGh5vaU9Wt1e2mIWNvsxGXcEM5BhnHjRwdsYZp3b3S2tzE5dfu6s01QKnzN4rCSXzeXMH43M3+xdE5aRunLwvFPj82jB5YllsUZe28HQEXkxl/mWJR/yJFb6PaVvLmqOSj1Lx0HecwfH0GN+1I7Ujb2OzOESHNLMQxhDiMhJ93I/lzO6ujYRSWVZTFIF/9BvXQNbyMlMWGj9OIy6mRLywE1oVsZYmdTIFd/5V6nA+MKQZwiVDP3keDnTTHXBwO7dyJzzbtYkIm+dw0nZNeYgupJGi9lpYlRqxrAhNeZLXrHJ9Y7esLwgua3a3Q7ElASw5Octoxa4AWcWtLe2orSbJDGMbJPa3jaWbLAF7+msuMVlLbpIBcvSx/uVMHgKnZGDauV2c1ILBnSwFjkmFyf12e0umzpYq6/4pdwMJ0EjaiQc0APidrdx7jlIlruacy81a5S5dF1vT8q0ychxe8wMvzHLcKOxZAA1gbDDByq6qgHCXxXshDG8fLi2w3E/yOHu0TXJ0AHosMvOEd2ktJG4oXz+LoQkrNy3Ct/isKJfLp1i75lRuDn7Jj3jDGVSHK6cE/58Hm/NrR5ZDz0XzW5DsP7V207UgVL1Ljf3MS9BRXrM+Ps+uNSP09XdyI/OnQVpL8eH2/3YKi1+27Z3iuZj5Ny3UJIgpa7OKF3dJKYZovqkXqZib8n4ZuDVvY3oB+2KRJpLjqFolIe9L3rrTMWqnWzulUeHYwqhMIeCvHRWPe3CAev2kupapl3v+DrZsoaZ6lc3QlIt2ORc1epUlkAH/jb48JFKkDOOB50s8WxwxUZYgLWR2MHG9pKj2+AyVwTke3bulBkasbaD4fe1zV/HdO9ty+CxRZHrkRDou3HvjOPtSJg4vsahrRQo+hryaYvlpAckcxYCXTgEicqO5j3DSD2RjTktyTLPMtMq8twDeuxOhNqdHSfeizSfQQlCMznDVDQyC0GRXh/Bw1GyPnOuKOkZ5N1/3MhiLGWlpopgyymdEvceg6eG3Jt2AOk9jwYA4MQORfOrlyflRrOGNKFjnaHs0TUFey2SYZLQByhfT+eMwdW2yzcPK44rBKbM3PfQQNiwIuRjDHF3r8wupk/5zlSE3cnU/DWuUNN+V9WUO2GKAaH6w6Vcnd7jt96Id+1V7gx5Z8hHAOpX+HHNMwQhpkelUBI18J4/EMyj5OBps47VPGWN+mKZ3STtqbsY0/ZwwM8anYa0lVZMA+CC4VLkrhxmgapRYSuQ7N7Yj47PMRlWmTwb7RPL7Z31cLpT2/3xcd1DMaVLJxs3Etb0zFKqY0KgUEJIuesQbE7F/bY/bI+o1LApb3nZY93I1hGXDQkJKP1KVYU5yHcTVFVfk+wDs0fG8oz6rjJ2V4lKznXhGqTgwFolaIgzMVCiyPGOwieJCHsEponjlesVYor94nQylcM5MYZuczoGaXvdS/tTHJKOoDHpGJ8u/F4O7jirDzCi0JES7wlkG0Hq3CoUNFoeAzpkHDtqShfzdU1So8V2RFB3py7kPJY6YjXeNFGXkhGtnLc8wY5jaPq5ZYY8YhGFHmeVGJC7yDqSeFgm2PAYc/bhJBv5BrPpEIdXlGCFUCkwdTqpjsTk2SObaP6iHypmG52dQTdPJXotqaDZM9s6LdaOTxWbB2TTU10mGSNHm2h8FAob0hlHKesAuzWOrzphDfGEaUhnzvIRmMfkG3mLJJG1Uy08bfbXM3GK9KE8xCAVQSfownqm8jJ10Ksz1dlks594kDuy5adjcqz00XWYyefh9brSSp8nc0yZWFnXQktBWq3Ape36VFGgqEj+9nDUx8MGbzJWLPCIkooNlRLHSJi9475BqERlcDZO+azKqLyiUN48HgMtovlGjG/aIToNU1I7pBbYcqnVxu2BB5dQV/buzs/9NN6IqCTUR4ue8O10hHic8404i1Jd0vmresEV9FLdbTsQ4vaUeiimtJJAalyHZzJ5FPS74I0pspsr5GZkxcTfWErDB+Hqr7Pwam1OCJtVlXRwsgZD0AqCA/RQyIariRcBa407x/X3Wez43d4SmVa792p/0w2D2iewjPuqy9m+T7O4ptJ8dHH3dXQ1DS5xCPF+bTKKFTTdUEKYAK0QG6rMSImoI3JpkmywPo2xOMpodi3X5o0mEPYwbafZ25euG5gdwL8Ow+lZrNugJnD0dj2wQ3KjVDK70QxZ+F0tXhEnX1/Wea0iPd8EMmaZkXeCEiAuqB+5eANlJ5cEsy3JscTblqSHedQ5CNkw1+3N5rgORCAX+I7ilnEUbzMp2DTS8QY1lCoxrhQjInvVK82DU2VvioUTGrJZCvkjOCOiMwesT+OwUB8K146Z41HTLZRz1TSxpAy2qyspnQzLO1mHUMGpPTL0kXTwUow3kuSMZLl+bLzCSIvxOovR5uqTuelldOfN3aExvMuOOiPHVNNMpoqMIT21iB6fm7YdLRLn7EjK0nibODj84MVjoXAGefG3hvUYJt3OHldFlVMFPyU6Wu9PzZkNYoKaj7N/5mZpZ6PI9pge2Ra906zHMO3d8iHy2q0ZmDmg9COkGduT21TMAt3VOEJgFTm8FAxX4/gc2U1pXrz9nnLWO3GY+TV6M4ujjinCRojLW3rH0I1R3vDCBG1qcnMguF22FUSH54iDrwxoQIDWv/S2180986I6bRI+P4kOaVaqe7qK2YiwY11wR5KGyzSN3QqXVbd/iOugrRiiFlrjVD/gKDL8Uc5dSRC5eK0bvE08rvFRSfaB5jk2rz1oDRU20T4vWSvjfddRr3GlNZfpyjRyk6Gm0JZGMu94LKcl6mKPvLMO19Tepi4w7wUtuVOLc6fO96MAhVpjb/bsMUPayrlSYxbPUnUVWArGnXASj7sJLPdurl49Sl0C/YyTQxXoUAuHkvJq27UVnUrsuD9urVbEzJPTTz7M0qIuuyCb6yPc2HISYulNPwDsiGf1ltH9DbsMpV3iVzEwRLo4r5GjfULXRqraowPAozj4Qi1qZ6EXSPecwE6dQkfaqjnrEkTJgGFyju3tGPKzI6Gs6866CuZxVMXb+qHMtU3mbQiVkLuXwZpvwIXqca90ldeOJ1q1ePhAKwzJ7x53LXVQ7IIfKnEaQrLmm2TqdhvtsTcOfHWP1w3P7wK+hJnicBJbDydHookOoJVJnDE7lhf9to0Sos5FUd1VjsoimcYOIXEgMnPnF9MBG6Axo535fLunjy1IZhqfGGY+6TbbuafAZKUrDGXrbu/i9AM7b7iR9m/FeVM4iT+g+4Zgc02fD2R50NHEzsRSFOEI39O6itQGDac2W2T3qbfmis1pN9JrsKKqZiElc8giW2TUy7Vg7LfpzalILNHKsg+SHrTbmlyla2Lq0ruHYUVpQdzko117BEaHOoiPsNazfI6uDtghIBPRrjapuxW0XV/KGQHwzfKUaG7a2dwGd+BGuYfwrXjj6kDsqtJo9A2Z2TVxOeaiddcih3vwRMyQOtRxjIhqyAA3umjsWhwBEB3UbpEP2NFGmovbodOOCHlIw0SUXx/B2gGqOFvis1Sf77fbZV3KxyvVAMBwMyGoz2FCSkKxtnb3gmQ55SivYSXf3E0XNVB4ew/d+4Zk1heeSObZvl3Eog0CDZMLq9QUHhEeSHAbRpMP+H2lENr4EJUahjngNjZaS6lNNSIBqfA4P4rNKQ9toh9yw6EHeoq2euvi+WG4Z9V2K42esN0nOqJEgQ8Fg+s6dLOTH4SOi/aN1s+dyETXRxSHqn2TNvN429TS2J/N3UVXW8jfuLltwRfFe4RBQqLbtmb2acrO4lYmHuNcKsVJAjLZxIBesqpuMOfQnc4AcpScP8bnG2i3LcuK8rVe+FrvY1uKDoNemhxBnHi9vBlXgtoiij9f+szbNUyfYPVsBoEfsI8TsmMa97ybAo4U7mXWkG00gIXCSY2v0zVVKbVQ9w8I3vpOsA7L8VbHFdqYKJpKrZDljtFPTueS57wHQN9Zt4aqpMFmZ05bT4MC7aYCGm+Mz0b3upw3EwEJa9zkctDTn7mGVk5Cx2cEqNLIDlYFY6cTCs+Erf24WNYtXbf0zXZ7pIou2h5zYqcFYSEJNxpR1u314GwvNh2FU0dfZc/0Yf/ixmltYXlDx3xkZfPOGre+zA093IijOuWPOs757VVqWuzWazQ5Hc0A5WXZuUVAqPCsWAWG6VVByGRxZqUBpsOkvD5GBbUja5OQMkHPkoG68tWXU7JQsGbuzV7fGWvrYk1uMtPDuYtnAzQaEGSTrjRk/c0YSOEkprf0diOQPRHjLFYhm0df3beXTdXO55FwkHW+1giVzU2XfBBsfJqtInLvhwK7qz6uzHmXJ4NypkLSU/OJ5QRZnDPf8q7SYG0cG7LX1PGYX5t1Vnjnm0kdiAreJoZfVKcbHx4g4pFzqDLoVQr5pS6X96O7iw+a2BMCrp43CNpYu8JHg4ufzhM2NzImZRZ3GbQZdvNgvq1J6i7bkCkOzk2LkrtWHByL3xuQhDIYM+IPZo3dh80jPPUkLICE5uOuXgeC6cqNA+U73LvzWIlkqMuocxKMinaX/ZNZGe065wqrWA9GiHK3/b2XVVAsMrwIH0R32uI50ZIojkv4lG9o6PLIvJHlNYM3s0jP7gH5wNo1HiS0pJa7uYWIHePrMDfhD6pzjojKEUSiHNdxdIcQBh9gChSaZtwTe1ohwPJiPujTie1ZjhqPvjrOcuefReSgjCMf4c6RQLz9ETKLNQi3Ti/HLi7M3t4IRK0ZY6FBrrBLm27oNy7rURfLGOoC58ejen4IU/+wYfS0HNjhNqSeXqTcXwsXDCcGsNyXiGq9bbbSPUJsQek29OZ86S5rv6Ymb6PzxU7ai77VsLtwjVTTOIic2lWYY/bRJTWOwrSmz+F4KyYR356bi8mfg2zsZSixuf2gbTSnnsnbfXfImjKsPBthgohQrLN+80U+8/M9JHcxNnuP+QpRWE6O7PkUgZbfNRNSjYdA2qHrGiVGKzixBD0hXcJGjznlONlWMB7fOesoMQn0RHXEpk9BO01aFXW2uxI66sNhk2ObMaLGcncughxCKVZxTV7OzhuRu1An8SqXOwzG4DwKD7trVc9QX2XdFiX3E6JVu/W5X/coqFVysyYML0QgUb3us+1wnyySINaYd88uFUQm61OEmFghCzYr7FrnWLrS4ZgfrOt0vm8xPNl1SIG2gz1IhwzzQJPoWUOCzpctp8kqEWzvp3DLT+emvHBEja/RNQh+YThIYRzS9sX3b1s6M+nddTo9NDwfjg/KB7mMDxlsdk6PQe1Y5hemZs5bfRNRaFmAOlhsLHZHXeIriY3GARMO+HA/k+OjhZo7uy2HQQjPsK8U90YbohFLYMI9r7V+2+tw4bTMOWqsfTdBTiBvcInFQweiXNW99I0R+HV+9Y0r1vgGWgwod+iwUXTgQo6m9mZZvtvZ/LAv29npjR5Hm8hjkGrX3vEcKmwTexTUMR3g8szFj7kmjvkGQ6M+TtaKEnjzERLT7FDhjyt0E6+ZQO1RYQSDmaN13ashmYr8bSc18g3kGsqVY9OaIqvFMliGRbR76GK2phCd2yGwsEforCDQzaRgtGINCJT08+Z6s3YyTB6hbl/ZEU7UxFijg6/C54feFEekZdwG84d416lEiaTYZTTpUleQLUn1ycOdh6gphiHHMEiGDtc4gKhWK3c+jWHKKTcnc5/mW2Wr3wpyV94Oa89OKwMr0tLSt9ABnvkz0Z4zhqKov/715d3Lsif9trP8PzzKtuw5/T/b3nrdpfpySOW56Rm6wccnr4//U4H+9u6l8VMgzuv2XZv38dtW2N9t3r3/1ycSlrnT68mwLzvlr1vvnRsvZ6Vf0jLo266ZPrdV/jyeAmZ4fbucr2yXI7jLuabvd2zdPkiX7+f+c1d9bsIOXL0sBx+XAydhkC57pq+38dsu5ruXYAIOSf32M0YSn8OmXvR7O9wA1MI+IB+wlz/+L0YdefzsLgAA -->
