---
name: "rar-cowork-cookbook-onboard-a-new-hire-with-a-30-60-90-plan"
description: "Builds a 30-60-90-day onboarding package for a new hire: a Word plan with learning goals, stakeholders, weekly deliverables and check-in cadence, an interactive HTML getting-started dashboard, and twice-weekly check-ins"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan", "rar_sha256": "9ac68e409185a2acf7bb1da1cb165b22706489409ba2ba8bab65060a1a1c2425", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "hire_to_retire", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan`. The original RAPP
agent is preserved byte-for-byte in `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` and in the RCI capsule.

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

Onboard a new hire with a complete 30-60-90-plan — Builds a 30-60-90-day onboarding package for a new hire: a Word plan with learning goals, stakeholders, weekly deliverables and check-in cadence, an interactive HTML getting-started dashboard, and twice-weekly check-ins

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
  Upstream entry : https://coworkcookbook.com/recipes/onboard-a-new-hire-with-a-30-60-90-plan
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
    "new_hire_name_role": {
      "description": "Name and role of the new hire joining.",
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
    "reference_folder": {
      "description": "Folder holding the job description, team charter, 5 key stakeholders and SharePoint link.",
      "type": "string"
    },
    "start_date": {
      "description": "The new hire's first day.",
      "type": "string"
    },
    "team_name": {
      "description": "Team the new hire is joining, also used to locate the team's SharePoint.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` and embedded as the fenced Python below (sha256 9ac68e409185a2ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` first:

```bash
python3 onboard_a_new_hire_with_a_30_60_90_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 onboard_a_new_hire_with_a_30_60_90_plan_agent.py   # or on stdin
python3 onboard_a_new_hire_with_a_30_60_90_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard a new hire with a complete 30-60-90-plan — Builds a 30-60-90-day onboarding package for a new hire: a Word plan with learning goals, stakeholders, weekly deliverables and check-in cadence, an interactive HTML getting-started dashboard, and twice-weekly check-ins

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
  Upstream entry : https://coworkcookbook.com/recipes/onboard-a-new-hire-with-a-30-60-90-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan',
    "version": '3.0.3',
    "display_name": 'Onboard a new hire with a complete 30-60-90-plan',
    "description": 'Builds a 30-60-90-day onboarding package for a new hire: a Word plan with learning goals, stakeholders, weekly deliverables and check-in cadence, an interactive HTML getting-started dashboard, and twice-weekly check-ins',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'hire_to_retire', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'onboard-a-new-hire-with-a-30-60-90-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/onboard-a-new-hire-with-a-30-60-90-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '541a741fd8d80c56',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-employees'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/onboard-a-new-hire-with-a-30-60-90-plan', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Calendar Management', 'Scheduling', 'Communications', 'Enterprise Search'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A Word 30-60-90-day onboarding plan, an interactive "Getting started" HTML dashboard, and recurring check-ins scheduled with the new hire across their first month.'], 'confidence': 1.0, 'deliverable': 'A Word 30-60-90-day onboarding plan, an interactive "Getting started" HTML dashboard, and recurring check-ins scheduled with the new hire across their first month.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'new_hire_name_role': 'Name and role of the new hire joining.', 'reference_folder': 'Folder holding the job description, team charter, 5 key stakeholders and SharePoint link.', 'start_date': "The new hire's first day.", 'team_name': "Team the new hire is joining, also used to locate the team's SharePoint."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Set a new hire up to succeed from day one - without building the plan from scratch. A Word 30-60-90-day onboarding plan, an interactive "Getting started" HTML dashboard, and recurring check-ins scheduled with the new hire across their first month.', 'expected_output': 'A Word 30-60-90-day onboarding plan, an interactive "Getting started" HTML dashboard, and recurring check-ins scheduled with the new hire across their first month.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'I have a new hire - [Name / Role] - joining the [Team name] team on [Start date]. The reference folder [Folder] has everything you need to ground this: the role\'s job description, a short team charter, a list of 5 key stakeholders the new hire should meet, and a link to the [Team name] SharePoint.\n\nBuild a 30-60-90-day onboarding plan (Word) with learning goals, key stakeholders to meet, deliverables by week, and a manager check-in cadence. Base the weekly deliverables on the role\'s responsibilities in the job description and the team\'s priorities in the charter so they\'re specific to this role. Keep the tone practical.\n\nThen create an interactive "Getting started" HTML dashboard with a progress tracker across the three phases, a people map of who to meet, and first-week priorities up front.\n\nFinally, review my calendar and schedule twice-weekly check-ins with the new hire across their first month, fitting them around my existing availability.', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Word 30-60-90-day onboarding plan, an interactive "Getting started" HTML dashboard, and recurring check-ins scheduled with the new hire across their first month.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a 30-60-90-day onboarding package for a new hire: a Word plan with learning goals, stakeholders, weekly deliverables and check-in cadence, an interactive HTML getting-started dashboard, and twice-weekly check-ins', 'example_request': 'Onboard Maya Chen as a data analyst joining the Insights team on March 3 — refs are in /Onboarding/Maya.', 'inputs': [{'description': 'Name and role of the new hire joining.', 'name': 'new_hire_name_role'}, {'description': "Team the new hire is joining, also used to locate the team's SharePoint.", 'name': 'team_name'}, {'description': "The new hire's first day.", 'name': 'start_date'}, {'description': 'Folder holding the job description, team charter, 5 key stakeholders and SharePoint link.', 'name': 'reference_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a new hire is joining a team and you have a reference folder with their job description, team charter and key stakeholders.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class OnboardANewHireWithA306090Plan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OnboardANewHireWithA306090Plan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'new_hire_name_role': {'description': 'Name and role of the new hire joining.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'reference_folder': {'description': 'Folder holding the job description, team charter, 5 key stakeholders and SharePoint link.', 'type': 'string'}, 'start_date': {'description': "The new hire's first day.", 'type': 'string'}, 'team_name': {'description': "Team the new hire is joining, also used to locate the team's SharePoint.", 'type': 'string'}},
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
    print(OnboardANewHireWithA306090Plan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbebWJbmX1HfeojIwjbz5Fq1VoMEYhAgCSQkwrkczPM8SCg6/3sfpGuHozKyOrNXP7Xse8Vwzp73t/e+8NubOw5J3b19fjNDt1pt3aJIk7BbuVWwWte3usvBV5174Gfl19XQpd441F3/9uEtCHu/S5shrSuwnR/TIuhX7gpHPlLIRxb5GLjzqq682u2CtIpXjevnbhyuohpQX1XhbZWkXfgZHNt1F6yaArC/pUOyKkK3q5Ydce0W/YdVP7h5mNRFEHbg7BaGeTGvgrBIp7BzvSLsn8L6SejnH9Nq5btBWPnhB3B1lVYDWOMPYOlKsrTdKg6HAZD+CGh2QxisArdPnhJ+eBIZbqkffnxn8Y3iomt4d8sGsHr7/MtfP7yl4Pjt829vfuH24NKb8dKS08ObBHSygRYcjlAIi+yBVmA7+B2Ddc0MbL2cN2EHzFCCS0EYrd7Pfu7DIvqw+vd/z29uF/d/+fylWr1/vrwt/45jtRqScDXUbr8I77uN66VFOsyfVlxxc+d+1YXD2FWLG3rgqir+9Nr5O6W6Wf3ncu/nF5NPwCA/f3mrgQju4sgvb39ZAf98eevG5fjTQqX5+S+fivoWdj//5Xc6/ehloT8sxIDUn76+n7+TBQt/X5pGq6/mXli/8+pCP21CQPwH/ZbPS/R3cu8m+fpa/HPdfFj9OeVFn/8E8r6C0QN0/5wssAHY+fYpq9Pq53ceXT2FlQti5ee//COyzxgo0n74p+j+8iKchCAEu5/fTfKXD0/3/XUFvev2neY/Zrskw7+iCVj+jd13Q/0j2k/P/hfSRVqBNPrmyz8l92cboP9c/fIPdfvvNnxYRV/eNr+n8OfVb88Q+eWnH/L6p7/+DZD+P5Ix67HznxS+lm6VRmE/fP36y0/98/JPf/3lp7EBURy65dexK/6M5p/Z9cnnDxZ8X/XzH/cC/qcqr+pbtfqeQ6vf6uZ/dH/7tDq7RRr8fr3/vPoxE5cPtFqU+Mb0ZYIfsrEHsv5gx7+8/Q1gTwW0Gf3nbYAf//ZvKy31u7qvo2Fl+vU4rICDh7QMF+GtJO1X4P+CGl0I7NqnwLDv60D8Lx5eJK6j1a//03/C/Uf/He7hd+z+6n4FYP11AeuvCz6Dcxz5SiFfWeQZKb9+WlmAfN2lcVq5xerI7fdfKoD01bCwbrqwD7sJwJU3D+FHkNUflwMAzatf/0kOX5/EPjXzr0+QTl8oeFzLCwL2YxF+WnS1k7B618wH0B/eQ38EfIraB0JFKQDvD8AGfV2AWjAsdunztChWAeDqg4o2P2kD231eiP36668eKA1fqhdk46tXqethsOC7OKuPH4F2UZHGyfClCv2kXv30299+Wv2v1X+360l84bEHxePdM0BCxTT0Fci0sQTLgNOAmwGMPD3z29/ebQzIVKA2Az+mURq+NoNIzcPgm8FNifuIkdTKC4GhgZHLpu6WgrdKh08rOVp9lxcwXW4tlSKp+wHU0yaslsI5A6ouUOe7Jat6WPUgHPto/rAa+/DJ9Vevc58iliDl3eHXlbbeg7pUF+DXIuZzEdhcVykw//dweF0HRLqf+hX/jcSnlb7EJugQOrdJOvedR+S+/LL0C+/bAfFn6/ClWkpwuJjqmSgv84BFwDL+u0s/Lj4HPUsJUCHov/F+rnGX6mk9q2j3perfk8DtFlf4oCgApvGYBktp+I/3kOqTeiyCp/2ApAuldy8E7155xuB7I/BDf/NqadxFDiAwiMfv7dGz4fkyYghKrP4/bp4Ws3Db7VHYcpawWQm6dby+3LW0k4tbXx0o6GKe2j1T8/fO5ht6fQPxL1WRgtjr5v94rXw6+X3NCxjHDoh25I5P+iDCgLsWus8EWAK665bUcb9U36oFkH71hEYQAwAtQDYtQfyN4Yen816SJkDh5fz3zuEZMIvDqyUFV83oFSAAozAMPOAxIFW3JPG7l0E2hEtC35LUT/6g1QpQB0EH6AOnA1HB16369B3BX3e/if6Hja8GadnybB5HkMPdkwCQY/Hk0zNLZADxhlf3DvT8/CQC1CibYdHdA1kENH1dDLuwHdM+HRbEfNk1bABof1y+X5ouV8N7AxIHGAukRzMC6z4Tagm9EgQRkAGEGQigMq1AOwCM8m6EJ0G3XNABoO97v/qi+Lz8rlD4zMKljn3b+IxTsGeJ2lUERAdX5h9BxPqzMAH0ymXFk+9/jbTv3BbaC5D2AAzL8PvdVw/x6dUGvPqM1Te6n/9uPPr5X5ugnoX99McA+LxKhqHpP8Pwqxh/q8WfAHzAL1n7b3X5o/sR4MDHBQc+Lg4G53/Alj+Qf2n+efWvifgHEu8p8nmFfkI+Icut3XuIvX+ARdYf+etHYrn7pTqGv2MtYF+XIMYW/82gEfheGL8tAdUx7sJ4WfwqlP1SX2+gpD8rA3DGl+rHmF9yDhSeKl5itK9/wIJnhwDi/+W77wUM3KqGBfoW4IvDT8tQtojfh2+fq7EoPrxVIPr+mVluqVLlEtn9MgKCHALd2pCGz7MnUNyH5fCP07HxPHCLT6tNCECp6H+MvvfastTWH5LkpSXQzgccPgCwBfm41EKg5cJ8STC3BxELgnXRZpibRfzX2Lc0it9bqkWxr11dhH8vlr5k3LPvAbcXaFoYfy9dS1O6zJB/Rv17j/r3RG3QECwIGtSfl9r44R1nPjyr1IfV9xEB6PQ+tC0cwmoE8/Avy3iyGPm5ZTl4Gf37pu9/d/DCt7/+iVzP+rxE5dfoWfT+XjzxeX211MQFrBaNs9pb/bAIoN4SZiC+QJnrPqzIVR7Of6ikT5uZ4H64BzYantjxp2Z6lsqvi+/+XhDrB1v/tERvt/Rh7vynhBaJvr5C9O/oLML+wXEgF959B6pVAdIDhNazqC3N8PDqrhaCgOvvSvwJ26c9QS0AFXVxze8+/93y9XNKXCQEnhpef9T47Q3khwuUdt8z5H3MAMsBdH7sl4YKBigCGILzV76De/+3A8g7mT5xQecL6LCuTzEhgbAoQ7qY60e056GBi/oeSpEehtEIRTAsuO+5mOcynutRJEhwFwVLMAIjAb0XeHxdmsd0EY1k6QhhWSwiUAwJgjDCiCBgKIbySRpDXECJ9EjW9X7fmqdV8K7vS7/FmN9nocUu72r/9uZRBFgpEb3MvT5rGEI9Ct95x8aDHlRU36M5NgR9PWcZZo0Zei4tke3icmrMojofVScV9VrIUy4WBJHJ+8LtSjm8KiRSYQYV0rfDVaYaVRsYxypxRVV0noUmk4zGAEFgg7l5A1KBcUgo1JzK257IVaWlE5e4jNcu0oXzqWaMBvw4DeM/LEUgSzWCHwMNKaRkBsfUkvQWSUYgiXIPC5PcqEwu9IVYVMlJoVPmxjhiqa8nYU4dRTKz7anMcbmf8yZsRds+qh03zGOxa1Q9FQ/mhWrWj8QQj4EuJ+v+fMkf6Vk+zKeyrO9V3BKdtS53m/VpL1X9I4pSym7VZh3GW+fYnhLA+XZPMK08FbhYO+1VMR+in3FENF3aGzFc7pg/TYk24Q3JQrpwceZedK88Y8eFc6bGPlV7naZQ927a19k4MdYYO1Nxul6MoDibKSml1n1SNiLZ5uEox5ZzDeIDj9rBYQvtkzt83cuzVVx4x9irIsV0wppSy92VsbUeubTpzI3+Ok+zbMefFbEg46A5oTOBOi7Z7UXL2eGwlo6o2SQKL9Qn2dxPV+i216mqNxN7HZ8frtAz3EEV7B5/nGWQ4TZh95ek7U4R53diUiYbLOTMiCLN6MERNYs3AelVaGb2khEC5ya5dnTQ9XSZgx3PQaXO5htEc8TTmfHmsdeEBrltYIqeU8tnC9E2dlArtOiaRS+ae1b7YFulbfTY+BbUD14jR+2JItenCrXPeK7XDln0qekJ2/66yVLO9cUarQSXwCV5xILUjzF9ng88yXLHTlVIUFHTm85v47Uk5mxcaw6pndcPTmvI/r7X1mp83rgYur64PddZJ51Y23Qw2P1RNS1jh9R3s/FayBnK4Cy2a56WTzRZ0/ypgeR8ZFp1DT+U3egRl/vsq1MmqTB36WaeqIc4OJTeJu4h1Y9NF2b3NiSafZvWU0OEknxitId1iw6hctDQOtxOUDRzuR/lsrGftwFR9V3cZSfWpSqiFLQxMTUdeYhnmDpGxAHH76OlTSy/TUOLfLDG1Hu72yFEz3vubpou33gaasndaUikR2ZmG7mnOmbgjHV4nG03Lja+I82qhDA3zOda6K6ui4Tga2I8u0Q+luZut9MkGapoZ313yQtvDTLSIqZyxgoRuaIpdldbll8bPCLGkYXI941+37u8Hq4vKYI21AkSzlrPVA+NSIJx1tmoPzV1id8wCA1Tx96j1yo+zHFO8IjQ8Aazx4+naJOr+6xU1+tgwyGBjCApe8jmaGtGR3yrXJ2J66b9odOlw+ncqU6NwsTjngbUbag2Hq3xI87MI7nbSHTEp9XpgHbY7VgUFc9IMi36InUx+abYmryWTMnugVtCIzCOtzPjDfXA1bg/PKK1UvVZnVfK+qgwDcMFTlnOW43W67WqR05vbzHdG3MxgaI2LxyvjdPkMq2nJkTnMsQ4wS+54cynLatoTpWFzaNw1FN+xOsx8ocy2iUXxbm3e3ynITqssARu+v1lT5aamB/uF3Wi1hYhSvM0c1XnWpZxA+nQ1zBHHLCbbje3vOLuvsdp/LlJNHuLxLtQFxBytpyzaqZEQ5yiartmS/7mPTCzxSMlz2LoXBxbWMKqIxHdFcEGznkk9JR1ko4+VKVyRCTX92u7NO5GP8nK3B5DpLvT/NiE28qfYJ9HkN2oCoRPdN242W6Mk13I2LAPGeXe3eWRttakDAGnnAzPzARndxb2EhozFCXmHn/OSQPkW8Qfr0ceOqti1oYzEq+LML0OxKmX7+i5r1Od1vBOQ6GNQRhKwZkhMspOEXtOthviJF5rWU4ErK7EtYIWlkceb7LK6aTlzQoqnI5DzzlC6QxY1Rs3pJ+E/e2cJCw1an1hiMi2PxPSKK/RK3LaV4dTlJstGzzOla3kuysihPit2Z7UBNby8s6YU1Yx8HRRUjqsdrhZz9a+FyipQFGh2DYXplAvTlgH62wutn2jSkH3gH2ijMNwfz1Y45wLAgtPdQc5bBTRtgwnFkuZCQNr1rVwqly3tlcHp1pMlg/YmvfSeBOTqT1v2J2syfUlfaS9wFiia02uUgDLkb084hks1pznsQ7Km01xEG90IymEd3psktgClM0KlJvT9njAG8Pi8OJcCPd97DBEbKYce2USPX20o9KtN+nlcjYTuXSt+QKL16Syfa851WVbI3W/L/ly25qZVFy8izIra1/Xz1QwY524LYeHP7IcB+oDKerhXSjWIV2HScFLQ0LOZSx0tnWpuqNM1IZQDQori6OqW4ZgudhsSA2T4oKPHva2yUO5lmQ4X1jpZko5IeaOlhqr5dHLTK47U4YCB4Q62LVDnG9S2ZZF7B7rs3/WPTXqQ0Ji7hdus+n6FrK59spNacIyljzOZW3eshnxYNKsGTluN8r2YDsPzLtvZW7rWuuCKrZt29876OKiOX/kT/Y1iO6lWcniMeTsOwHzHXeib3bqPix/e6nla1CamyNZcetjVTiouI1SxFDNAy648nSIRSNREdEczwR/lsR9bNW7ZC9KaS5oXHielEdj92v9oat2OiP9HK59TCR2kG/rwmG88AVS3rIdc2U9THbLFGmZMFMIwrk8TJkvmom/cuv0RFKdOTM6mqC5HCpoldjnUKD22VgpBwlRRXNHlLd5W+tkifq95keieHI593pqXCHoFWR2+uO2TuKYKwBoU7FJ1urF2N+PTZNc7vjAozuYFQ4VcuUegxHhToDJsXfN2PSkJ4SHdIGedNJVzITapil2Vnc6abQH/vioieslHFLISA5VKviZg0wXw+hQRedCem2SxsHMiSiCU1IHlY/GndOcOVpGJLJeONyjuM0qst52F1Uu9sItNY8nSRPj4TjEG9BLKQMYTt1evIuFfI6zi8BanmCsrYCIND44yTdcOZInAGEef8tPDhpWMcuSSl/sjx5qYFtXwKXzDhGNW+ht25hF6Op6NvVavBvyGRsP09Xe3RLXuNsiizQXgVFOAgmAw6pRPnIOIv2YmpY7NFfSNatAtYVGZ8yLU4WJAwIwlxuFi8sSZbJivpmni3b0iQNFWarFDua8NTEnvAm37mYEOZtghanGvDFCoLZe1YuZcOuEvp/brKqUdFIPLanTA0dWOw/O0sEsoywFcKbjh6tGiFvdjtdNA+V76iRv+nUvHDG939qF52jHiZvKEyqmJnk6K8d+YHT6hEMWbA6JR9lErezWmtpKa75IeehRyq0rYYGd+LcLFE+2xCsmrUdMGvC6SSoF5EGVhoknbJuR6bbaFGFelXIv1f1usIvzvXtQ6lVyWTQdiIywdkzcKuZmXe4zjbCH67bFuSMfF0jSMrs7qaxpF+PODGoQAqiN6yZfa/jOMTTQhm47JxbHYthGBlRyR7NXUVR0KQynysR2C028MG3uDNuw7bvBCg5kd85sZpv3j7wAHVtsCrTDN5siYIri6JchzyOqTxoQBAkKcxeveuwS7gQgZqjKyN4RKEXv9wZysfwNa4wbrHzQ3pHDRkhMR6WyBky7SxWtmhIR634ge9O9ccgzFPS0bVEahDY3YV8182HM4viBR+chEoMav18qrNIrXPCqfSbP2zwZ+6TuXCi4ivFRMvRLo2epmMrwxgc7FP9UdXqCBWZeQ4WoUReJKnJHC8S+O9vl2ayJ9V044hlBwlF+g5thZkYKxY8ziRyUK06N8JG2VHtrkW5mNbG0bUc7pO2NYe+qgAosjNfvwAhBwiIE095PW9vQefnRrFVNaANWPh9wSJhlqE/EELkHYRlucy9vbpYfJfPxNK65M4+2KrqF131HEymqkm0AYLw/xOfbeAxOqeuw5uOQFYYWbfmuTLyO3uSOL2yzJr+gWx20Etg+oLnckklqw6ddn9wVZ0YfUaBa3vW8tzHvQipUOWKGcLoehRqmLv6pDZiHKITHalMOrsAiM9lc+p0RP3rqykDyJtWY02nHqQxH0+fpusFRNXArI5JNM5i4K2nAZ5Xe3Lre97OTuPH2ItwW7CSoJjlK09oy6TuC+NAFNi/wHWX5/SBMV58p1cY/x9fDvthZ/kWvuHNYnnA+PwzbkZwNs6CT+O6YOVprRzROjndEktFQjuS6NXTy8NARr6qKtTDuM2VNDMIRrtF1nIy6JNskQ9treW4QDT4wzlrstLvfnc2ZFA5DIATaMKvZw+LsQwm69aGs9LtVnt2andmk5A9ZguDFTPlptCOLCjWOW5dr00w25jMrYINAXG8SIXDnB12GMaP2me5X89jcGClzp/ESxtgD1QM+g8Y7mwhKewgUwjrtlLM9XDDaCHVcSO6HUtwhE0XGwrm3MvfQNX15mffarohOpcWRTIydXUg+lrMrpEwpCKh+h1TqiKXC0YGN/YngrsF4CpCAifb3gcDqaHM98MFtYhjR6PvpelEmcwoTMJKvD+GJZTfExNk8aW8rAQSPJovtxbTZR65L2sWaeak6QncNzBJRtg3y6rK5F5s638W5ts0glFONKWEMxxuYVBir6WTFkJeomGs08i4LSyzLDsf4tI9hKjQjhGjVcCIfc6Jx47G5ziMFj7QfPDglmVridoNqmirZBh/uSlb7E3q+RITnwNyGlDYMBTpA5BGIdGqIMUbVD9iK9gzCc8FtL1lHWL9ooD3HDdrKI5vE9gSeuxHCJo8S7zbYI/c20xWFKNLrTjyd6tBB6oIoYOgYv/ZrEsIuPURraFvQDrV7dNm4L+czcnCdvrrkGE1V2bHyTQ3UP50lgsPJbdK8jiCvHgoSr1mv8LTdlW71UZE4hRofKiz7E7IDY0G3r2sY4YKTYR5UZQTzAYUrhKplSl2iRXYVm+vI6DoF25N3eSA9O5k2XLKWeWP3XeRZN1AGNg8bP8Bnx8dRnHb6MHtsLvKsQtywvR7ZCK2UHMdg0J/CGT9vYVHhkQZrxULfrCVtggmIhW8WdT/ljbZldX8iGsaKT3iqCf4gouFsK46hqB5y8NytKHVx6YmHpI8AaNC18PCgwjjfKck2nEf6kJNk4x5CdwTdND9zZF1laWgaEavkUSZ2FlHboRGgx94j5lZnDCNmvda2C07Pd/0Mb0Zf8xWkSa0dnBCGx57JVnFxnEH6su7v/Zxv7vw18qJLFQWJ7Ve+TQW4z1mh3uozySkPuM+zsy/We+LhW3SX0wRogeUgKBmMvra7JENpJakD+tQaaA1bdoWGcJgMkMxh8dqXcu4u59adgGQEp/rGyPBIOG63WOedwqt5OeWmA0ZMHxszx61GRD1foYeabRC+JzFWy7BoOrQRw81SUhGpQ7Cs7aUbSGGIQ3HPjtg977I1kh5LUJUsnDXOsZtsg7BDM1ukmCsydXFuben2PnXSGlW2V0h8zDclXh+wUNCn7bnHpD5RGdjNqx5jyJEwZl68TWDqFjcHqHPucFdTMguzEhpF1Pqwv7K6iF7yoIQR0IBPCZpZQzBVV4mSErS6nJUERikRDC70+vjYQ/imN6hj6nZY1CFIIwVQkCotuZGh6OBbAOqbSb+oet/1j+Ggn9JEKtGTA4Hp1vP0IODt2bt0l2IjYo5535QEzd1uIh3dvOFwPBchzxJhUl3zHY0dacIh9rka6vfuKt1AVaSQG40p1EZPDL8GsDmj09FT2WlQL/LVT8lO2yTU7l5QoC2RMgPnrqkqbpu9RSLB7baTJRxfywdfzwOx9uUwo+WuDY5tY1Fej5iDf7uTMTb0XcJmxKOzMDZkG43BWL7Kur003m3c6g8POKqCrsBVnfYfwuMC0cxcy9NZ1L20aWYlgAY08XdVJhMuNLLj+VDTHYl5OH2U1bQzLXhfK3o5IeMeu3FIwbAKyd+hO+Jj65KHkkPjF2RmSBEatmyrbznU9yGyuWutD+Pm6MpzICFHJOrVm4hEzoj2ewuW7TiIc+coOha5azfhFGTbXrq5GaI8og5PgiMMsJZL9fhyhYccqHRyQebbV3zNR1XVOmvtQuxPY1ozD59P4iuJlIInYZ2iiKKYE30ZQGt5H1b73sh8CW7OY5hjeSApqKVVNn+l1GaiuexaMiSMqaMTwj0RjnFxwG9hmGa9KXunQt4NHSMYLOYQ15EcDXadPA7XycwwFpozg9XYFtM6plU3yNU9jvQMyxJWEPxpdAdxlDBM0HdM1G0HF+mdGaTA7jhcac+GnNhtvIOGdql0vdL9jGkP94bOln1FqKK/bvVHp2H4tnUDJgFRwh4o1HFLYtdTuH5jD9tNPmOHAZbCh8d3tCgNG0+9Oxto8JVa3toQZcX7wB8uRpuJjwsrtfJuZ2KCA28M2Q/JEyRupc6YGRc3eEcf9wFiOR6VERjdQjl878556I9weAaSRAjlYGfvKjUAuWPqgPe5z3D5wIEek4BodkffIkozMyInzIgfTo+il+TH5AVN1FbaJpiGx9qYiWmjWDxBDOUYEiTeojsKxHs4ZxhgIMh5WSNMgyX1KZCRvZ1qkHQf7BLWzsPUY71IS2R8Kmm6oHcuCz/GBo712VT0022T+OUpc8mHDc2hPgSVha872JJqKS43uCTjXCPG0wVJfQ2+enefk3Y1Gu6cHdrZHgs3B3LeVMwM+nCWTsDYfa6kS9BlYUzftMCrx4Q6C8xOzcLeV6aWSiaFpm/TMIYTBnXW5M/0EadcFKtHbbzA4MvOrPpyH24QADuaUGgCcliudZ1IXw90oO4Kuc2aMh+6bs/sb11Nt8ycuvvBhxNnC40E6t6OkOTedHYc8S3qU9iUGw5ziTaC7hJ7acNvaDhk8asSk6V6pzw4ooksJfNmMuFJ9XdTdvcPamSitSnKa6q4so+y5TqZA7hylHKFzc/VkfZHKnkQKLITM+Um7c/rfaPzGLE5xa66geao2Jsb8+FTLLn3kjpBKfgKJvPa8tgRpkRo4OtoIsiGvDfo5Ju4Dp+6UkQGwu1wf4rBCEpWSIqD4Xadg+RnKG5Mbu6j8rpymgoch3Roc4gDlqvusdSlj6vTIGJcaC5sPiiCoOj1vAv4uqiq8uJdkJCHuZMIM0p5Ph447u3D2/J8/P0p97/65t3yYOv/2fO116Owb6/QPB/6hm7w+cnr878s2V8/vHV+CuR6PVHsizF+f/D2X54nfvwnX5xYiMyvV9u+Pc5/vSEwuPHyAvhbWgVjP3Tz174unq/TgB3e2C+vjPbLW8U++P7xGXY9JGEHvp/KDPXXLhzAEbjgBtNigWB5ggks8LWuiqc+769aADXwT8gn/O1v/xszWG40py8AAA== -->
