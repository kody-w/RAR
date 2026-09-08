---
name: "rar-cowork-cookbook-onboard-a-new-hire-with-a-30-60-90-plan"
description: "Builds a 30-60-90-day onboarding package for a new hire: a Word plan with learning goals, stakeholders, weekly deliverables and check-in cadence, an interactive HTML getting-started dashboard, and twice-weekly check-ins"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan", "rar_sha256": "9ac68e409185a2acf7bb1da1cb165b22706489409ba2ba8bab65060a1a1c2425", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "hire_to_retire", "advanced", "read_only"]}
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

<!-- rci-capsule:v1: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 -->
