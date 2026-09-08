---
name: "rar-cowork-cookbook-wrap-up-projects-and-organize-related-work"
description: "Collects a finished project's OneDrive files into a new '[Project] - Archive' folder, shares it with the project team, and adds an HTML recap page; call when closing out a project."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/wrap_up_projects_and_organize_related_work", "rar_sha256": "189dceb72a28e49a7b9a67177cac64485326efa65613d1b8aca823a15af50a54", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/wrap_up_projects_and_organize_related_work`. The original RAPP
agent is preserved byte-for-byte in `wrap_up_projects_and_organize_related_work_agent.py` and in the RCI capsule.

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

Wrap up projects and organize all related work — Collects a finished project's OneDrive files into a new '[Project] - Archive' folder, shares it with the project team, and adds an HTML recap page; call when closing out a project.

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
  Upstream entry : https://coworkcookbook.com/recipes/wrap-up-projects-and-organize-related-work
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
    "project_name": {
      "description": "Name of the completed project; used to find related files and to name the '[Project name] - Archive' folder.",
      "type": "string"
    },
    "team": {
      "description": "The project team to share the archive folder with.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wrap_up_projects_and_organize_related_work_agent.py` and embedded as the fenced Python below (sha256 189dceb72a28e49a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wrap_up_projects_and_organize_related_work_agent.py` first:

```bash
python3 wrap_up_projects_and_organize_related_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wrap_up_projects_and_organize_related_work_agent.py   # or on stdin
python3 wrap_up_projects_and_organize_related_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Wrap up projects and organize all related work — Collects a finished project's OneDrive files into a new '[Project] - Archive' folder, shares it with the project team, and adds an HTML recap page; call when closing out a project.

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
  Upstream entry : https://coworkcookbook.com/recipes/wrap-up-projects-and-organize-related-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/wrap_up_projects_and_organize_related_work',
    "version": '3.0.3',
    "display_name": 'Wrap up projects and organize all related work',
    "description": "Collects a finished project's OneDrive files into a new '[Project] - Archive' folder, shares it with the project team, and adds an HTML recap page; call when closing out a project.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'beginner', 'read_only'],
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
        "upstream_slug": 'wrap-up-projects-and-organize-related-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/wrap-up-projects-and-organize-related-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f08adf774a926df',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/organize-information/archive-completed-work'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/wrap-up-projects-and-organize-related-work', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', "Output matches: A single OneDrive folder with the project's deliverables and references, shared with the team so the work stays findable and easy to reference."], 'confidence': 1.0, 'deliverable': "A single OneDrive folder with the project's deliverables and references, shared with the team so the work stays findable and easy to reference.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'project_name': "Name of the completed project; used to find related files and to name the '[Project name] - Archive' folder.", 'team': 'The project team to share the archive folder with.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Close out a project with a clean, shareable archive - not a scattered trail of files. A single OneDrive folder with the project's deliverables and references, shared with the team so the work stays findable and easy to reference.", 'expected_output': "A single OneDrive folder with the project's deliverables and references, shared with the team so the work stays findable and easy to reference.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'I just wrapped up the [Project name] project.\n\nFind all files in my OneDrive related to this project - docs, decks, spreadsheets.\n\nCreate a new folder called "[Project name] - Archive" and move everything into it. Share the archive folder with the [Project name] team so they have a clean reference.\n\nThen build a lightweight HTML recap page for the archive - project outcomes, key contributors, links to the headline deliverables, and a one-paragraph "what shipped" summary up top - so the archive is navigable, not just a folder of files.', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': "A single OneDrive folder with the project's deliverables and references, shared with the team so the work stays findable and easy to reference."}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Collects a finished project's OneDrive files into a new '[Project] - Archive' folder, shares it with the project team, and adds an HTML recap page; call when closing out a project.", 'example_request': 'I just wrapped up Project Atlas — archive all its OneDrive files, share with the team, and add a recap page.', 'inputs': [{'description': "Name of the completed project; used to find related files and to name the '[Project name] - Archive' folder.", 'name': 'project_name'}, {'description': 'The project team to share the archive folder with.', 'name': 'team'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a project has just wrapped and its docs, decks, and spreadsheets need to be gathered, archived in one shared folder, and summarized.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class WrapUpProjectsAndOrganizeRelatedWork(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WrapUpProjectsAndOrganizeRelatedWork'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'project_name': {'description': "Name of the completed project; used to find related files and to name the '[Project name] - Archive' folder.", 'type': 'string'}, 'team': {'description': 'The project team to share the archive folder with.', 'type': 'string'}},
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
    print(WrapUpProjectsAndOrganizeRelatedWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
