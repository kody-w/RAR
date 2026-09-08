---
name: "rar-cowork-cookbook-onboarding-checklist-generator"
description: "Produces a role-tailored onboarding checklist as a Word document (IT access, mandatory training, intro meetings, week-1/2/4 milestones) plus an unsent welcome email draft from the manager; call when onboarding a named ne"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/onboarding_checklist_generator", "rar_sha256": "061e0ddb67049f3ea5f387b837786f05806ad2673074d9ddad00d78e9ca61a1b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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 -->
