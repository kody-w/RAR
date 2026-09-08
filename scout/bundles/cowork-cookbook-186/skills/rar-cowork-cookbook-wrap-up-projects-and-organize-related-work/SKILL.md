---
name: "rar-cowork-cookbook-wrap-up-projects-and-organize-related-work"
description: "Collects a finished project's OneDrive files into a new '[Project] - Archive' folder, shares it with the project team, and adds an HTML recap page; call when closing out a project."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/wrap_up_projects_and_organize_related_work", "rar_sha256": "189dceb72a28e49a7b9a67177cac64485326efa65613d1b8aca823a15af50a54", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "read_only"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adeiWLbmX7Hf+yEzrxGBgChErVqrEURBQWWQISNXJPM8z2Tnf++D+kYOlXW76nZ/aWNFqHDOnvfz7BP4y5vZNkFevX1+k1wzWxzMJAkDt1qYmbOg8j6vYvCWxxb4u7DzrKlCq23yqn778Oa4tV2FRRPmGdhO5Uni2k29MBdemIV14DqLosojcO27enHJXLoKOxfcS9x6EWZNDhZmbr/47sfrc9VPi48LsrIDsOq7hZcnjlt9WNSBWc3rm0UfNsGiCdx3oYvGNdMPDztNxwFqs8VR5s+LyrXNYlGYvvu3hQ28WfSBmy3sJK/DzF/kbQP0vkR8Ak64g5kWwKS3zz/+9OEtBJ/fPv/yZidmDS69qZVZKMXLwJrMnEvlm1k4uaKbmI3rqCA+QEhiZj5YXYwglBn4XriVl1cpuOS43uL17fvaTbwPi//8z7g3K7/+4fOXbPF6fXmb/4ht9nCwyc0ayAbWF6YVJmEzflqQSW+ONXCuaatsjnENMpH5n547f5OUF4u/z/e+fyr55LvN91/ecmCCOefpy9sPi7wC+qp2/vxpllJ8/8OnJO/d6vsffpNTt9YjyEAYsPrT19f3l1iw8Lelobf4Kl331EsXiH9YuED47/ybX0/TX+JeIfn6XPx9XnxY/LXk2Z+/A3uftWYBuX8tFsQA7Hz7FOVh9v1LR5V3bmZmtvv9D/9MrB24dpyEdfMvyf3xKThwTVCb379C8sOHR/p+Wixfvn2T+c/VFqBg/h1PwPJ3dd8C9c9kPzL7J9FJmIEmes/lX4r7qw3Lvy9+/Ke+/VcbPiy8L2+0m4BWrkwrcT8vfnmUyI/fOb9d/O6nX4Ho/6MYKW8r+yHhawpaz3Pr5uvXH7+rH5e/++nH79oCVDHAgq9tlfyVzL+K60PPHyL4WvX9H/cC/UoWZ3mfLb710OKXvPgf1a+fFnczCZ3frtefF7/vxPm1XMxOvCt9huB33VgDW38Xxx/efgUIlAFvWvtxG+DHf/zHgg/tKq9zr1lI9gxfIMFNmLqz8XIQAmysH6hRuSCudQgC+1r3ArnZ4txb/Pw/7Qeaf7RfaA71ANu+tsXX17r6K4DSr/kL30BnPgDu67zn508LGWjIq9APMzNZiOT1+iUDCJs1s/YCILRbdQCxrLFxP4LG/jh/ACC/+PlfV/L1Ie9TMf78wPTwiYUixc44WLeJ+2n2WJ3B/OmfDRDfHVy7BaqSHED9k1s+gEjUeQKoppmjU8ch4AAnBEgDaGt8yAYR/DwL+/nnny2zDr5kT+BGF08+qyGw4Js5i48fgYNeEvpB8yVz7SBffPfLr98t/tfiv9r1ED7ruAIieeUHWMhJF2EB+q1NwbKZBgHQm84jP7/8+gozEJMBAgbZDL3QfW4G9Rq7znvMpSP5EcE2C8sFsQZxTou8amZ2C5tPC9ZbfLMXKJ1vzXwR5HWzcNzCzRw3s0cg1QTufItkljeLGhRl7Y0fFm3tPrT+bFXmw8QUNL7Z/LzgqStgpzwB/8xmPhaBzXkWgvB/q4jndSCkAsS/exfxaSHMFQqYGZREUJkvHZ75zAtgpfft76PBl2ymY3cO1aNdnuEBi0Bk7FdKP845B4NJCrDBqd91P9bMlbWQH1xafcnqVyuAcWIeEQA1AKV+GzozQfztVVJ1kLeJ84gfsHSW9MqC88rKswaBA4u2eG+w+lFT7zW9mEeOV10vHuPTlxZZwevF/4/z0ewteTiI+wMp7+nFXpBF/ZmFeRScs/WcHsGIAiyqnh3329jyDk3vCP0lS0JQUtX4t+fKR+5ea56o11YgKiIpPuSDwgFZmOU+6nqu06qaO8L8kr1TAXBw8cA9kFoAAqBJ5tp8Vzjffbc0AJ3+4enbayx41EHlzCECtbsoWisBdeW5rmOZdgysqubefKUPFLk792kfhHbwB68WQDqoJSB/AYwIQYYBXXz6Bs/Pu++m/2Hjc/qZtzwmwxa0ZvUQAOxwZwPn5M15BeY1z8kb+Pn5Pctp0cy+W6A5gKfPi27llm1Yh80MhM+4ugWA44/z+9PT+ao7FCC/IFgg30ULovvok7kAUjDbzOXkuKBt0rlQGxCUVxAeAs3UfRbOaxh9SnxcfjnkPpprJqn3jbMj856Z9xceMB1cGX+PDfJflQmQl84rHnr/XGnftM2yZ3ysAcYBje93nwPCpyfHP4eIxbvcz/9wtPn+3zv9PFhb+WMBfF4ETVPUnyHoybTvRPsJoBP0tLV+kO7Htvj4jh0fgaaP79jx8YUbH+ftf9DwdP7z4t+z8g8iXl3yeQF/Wn1azbfOryp7vUBQqI87/eN6vvslE93fUBSoz1NQZnMKR8Dy3yjvfQngPb9y/QeZP2C8nplzRpYH5oN8fMl+X/Zz2wFKyfy5TOv8d3Dw4H7QAs/0faMmcCtrgG5nnh59dz65PZqkdt8+Z22SfHjLQAH+6ye2mYXSucTr+bgHsgFmsiZ0H98eiDE088c/HnEvjw9m8mlBuwCdkvr3Zfjijpk7f9ctT1+BjzbQ8GHhABPqmeuAr7PyudPMGpQuqNrZp2YsZieeh7t5HPw2K/6jNSqg5BnsnPzzzE4fXpAA3sF8/2HxbVQHWl+Hp8d5N2vBufTH+Zgwh+GxZf4A9oC3b5u+He8t9+2nv7DrVb9fn1H/s2nCDAYALB/zQT6TePMb2/1tjtEDpgEPOt+48kl8c/rBnVnsY/c39ntc+gsK/MuozdT3j1bJfyLHWdGDP5/48pT7EvuA3b+QDYQ/EBbw1BzF39LzW5Dyx8HqESTg2fP/AX55A8Vmguybr3J7TeZgOQCkj/U8fUCgMYFC8P3ZQuDe/8XM/pIE/AOTIhAF44Rju9YWMRHcXRPm1iLMzRbebm3T3qzXOIYiG9czN9gGRh3Ywk3bxBHUhDHTw1Ymtgbyni35dR62wtk6jNh6K4JAvDWMrBzH9ZC14+AbfGNjW2RlEpaJWRhhWr9tjUHCXy4/Xfz1UUqv48Mcmpfnv7xZmzVYeVzXLPl8UdAStjbo2RoCbTltPD2PCLYJ5ZzbrzpHQLgz3RbGcLbYsROM3e1C9tzZDvnb7UiJ08FfrdZevocMblkgU4uT1I7SDOteZEWQoklFbQ186W5Q71JF6PWAjvIOS3O+OCabGz6eyVrkOIbFV8it5JYxdeF0jGYvUpBym0mCmCuELydob4rV0S0LvVzd7mo/mpgtUN2+imt4cCR9YuqALE93gZcvEnxgNjhc8aoeFhc8o86qchnkVmCxQBAt9mJjhReqxd1S1E3CScXp4PbpxPg30ZaC5aXD7vCSqkUKN3DmcA30wNZKItFjdr0Vb6Nixnc9IehbAvF0hK3zdsLgpZ3RBMQVG+hKQ1s48DKE4vgYZtOUSe/IJGqYuMUxIbAZiTJ2Un1fTR4udoOi3o/p+qDcSlhxsWt3dEPWgffbXUDldTn04UWuMR067aRUvhiMVoSDnVAXF+uTA93fMEmr23C4HPeJ3Z8TSQ/lWjhXrKVsj/rK7DJ7V9+RvCZgzuB9SlI51l5F+xon0U1zr/anIYk4c+fuE5c8MaGgqgUbKxuxkJT2gDjiejd2qWuSdZ+faIOgy93IbwvnWPF4M5hBAd+5NN1Fgi0r0v3GUfiRwjidxVRR8J2d6hrl3VDWa2EsncK9O5fgrlC5rWhLpfXGQcmV0pD3A17IhnNWvVVD4OI1z1HEup302/6o2vfgWLq7+M5JDc7svX3EJtnJ23sHVWFN55inTDvGTSHat9jheDOE0lJg+fNN0/fRyLYnD/Ptyjz6QtIxyRnbpgoV60gay5skZ8wLnJMpZIBD0IYbWadcSuNeqJWWyES2REdlf0Zu1RQc12pyyT2vvrVu0WYJ1eFyPtlS1ZHMkhEsilvnTuneEIv2V9te95eWZunodbD0ukbYZbpWcZ6WK4imnUmWosHtzb3Kmcadt1jT0s1DHg2CuA+AK87k3XbY8uwsr2KhkrYerpd4AGHRRI+FtS/xAd/bUUEsW3TlDL6d8akQcM2Q82d1cwOBNyorJO4uczi0dXXSESk76+crh+l6ul65bN5R01Wxr6sIKnSXNi/HRGtJRKLFJInl4iLjgKkIx/Q3cSzdyxMZC1xorqLdOcBJBN5QZ4nGnNNmibJFlocWKaLUCWebiVctqifCqbT4ye8zIjQ2V5aB9Uxep451g08lC1unui7v93E48+cTbCax3khwPgknib+xmckNdMFBxrZg85rujHNLqNtCl8ywEUM4atYdfot1VW0tw9nj6lY1V3dxV9RUOS4PpzwuEYFZquZt2G2hQCQHjbFMVVQOJgXtUc+5BvERO9mmaXvlrhkPZ3J5WyO91CViqHLH0uy7eJRdmrBTBqbLgyRjWReqcLOxdtmmvuV5NMJnzkt0+0I4iUudQXcFDMY5YyudLgykSPUqzrNcYjtLdpb4VDdn4xQGSsmgRx4WoPN9q53sWEOxBm/0XulOFp6lg89CfB1s9Gvc+/b2fFTDMRdqEc7tW9Hjaecu6QBJ99vgAvpUIu0SjkQtASgtpYxYNRa7dKodQnu77qivK5BTCDoS1xMUF7tMxjG7XOVceXHQ3uYwOM0xh+DHGi/8FA2YAVXu6rWuwyoyV9uWCVrO4yGrhdzt1KF2yPHBuEaVlKf6vDkP7dbFTS5IyurarvzauGwkA6YvQz3c+7Vo19jKqO43SjQmNyxdL2z7UAwGjKYD1g546Ljzx7ufLScxVKCuHKy0I41pd5VZ0mhY6dZF0jaqCjLQqZNcmE6wO0Uaf2kihRNv5460uRsenrJ9liQ4KewPRUMc8csyXkcU5yKkTjXDMoVPG9PmiepOs3rJqZF8Wza0uPTN7X3sVCc/sk102IEONevcMk4xpvE429cj4WU0Bi1dE6Mj39BDi0KvW6LcnQQ+Cy2uzVp/f7oKirE72FPtXZdHsjpOcHWgnawPfKiKls3e85GICCYIP3eRPGyXV7g224k6dXSt4niKckwu92IX72zfRrPeGVibiQvBqJi7PuTtBT9qQlSeQkS+iV50xvclgAgwaO2Kuy/B/aagz5vKFMpbf7Y5YidPCRqfhtuqAG1I2u4Z74uECU2xW5UDImIKeRHPumQIRn7mk7xR2hDRmoJs1GOS3Valzq7L4CIczBo9eLGorMsyWW0oPG9oTcVczmFJjWV2jGiXUZjyxIq/Lf0Iva0wZE05DTMNirGEaFWtC5VKnO1hPZiEiVMHz7ml8nlsQ349jToDmwjkwyx68lPjvFc68X5RFVIirT03YZp7Zy63Mbi7hHRlLBJivRUnhaoVwPod3eH+eTx456VoG6OMt876UOiUUhlNyzCxRu007UbmLt3z1zCwQ7rMY3RXbKKjeFmtJoZki24MC6k0AkOh97K1Yvc0HfZVw/CylhKyernsjiRlHcjcNkkfFSolpWqDv+xMxQwiyagnBVVEvyNCwPw0xp8ayTjA3S5cead7blZ5O0guBG3l9G4JrH4REH4Xkhtu0jYlx+qIf2RuITwSJ0BgULHqE+KgRDmjHdFykkodgM5ZJq57G3GxKT3tTmbMOPs6FbzLsU5hlVrvWP9gi9tKKU79di/XMQmd1rZ80aCSL671ihxLE6J9r7nFY39dcjckC2r2sD1B6yQ3/UbZY4RTNMzSjeCIlCCYYHoPGeysz2WXuoi1oiXd7g52EUygJix3olCvO2JLtz0WG2cb8oZYHwxcoi5T7ds9jFEn10hReeQkjd+nca+MFHtVdvke9wgjiZPMrJnhkLB3PzL3YHA8taTsrD1+5yit3xfw3rd4BcwPbD2yDS9utqp8aN0Q3Rh1uiK9SyndOMInZD7qtTarQ88/jLVir0JNoSPTWub7s78WSvLkXo39lDBTuiJawq7qvUSEDX8U9/C4CdY1l+qawUin8HjlLmczQ4WNchm5zigvW/ig+F3bMAoTx75yoxH1ZqQdxYm4CQ9iw2+5DOEclWl3h7YvdoCdy8DWwWTFL5nkvj5tUtrGyONluLKOoicKGjHEHb8tlydjlxbt2At+cWOX4rDJLxNrQhchZuXQDNlQOu0Lwe+G/hRuV357GtnDdUXrdnzaWw4nlBp2UXvM4CxXshpV2y+LElnHKx0UC/iqnSSLpild51QYVTJvmRfXJGm5436DoWmGU6J0SJlxtXLB7K7VNAJVd76hVpOaMtmyGlO5gCMtBMypeQIn30/jqJm42a2O8XAsouO96owOLziZ408cuWKVjSTeNknM73TqvF2Te1QGY1AS1GuvJK9Gss8O9sGjjJMAl7kc4KK4dabAFsjN6Xpfssee8nbUoacpt+QjjB7WRqMtL1vs3MU2yu42GaRHeadvxQZTGzyXNe+sNqGy71k7XrIbQK8isjnqks/dxKuidJgnNYcNr5TRmUzOLq97o3oalPWlQU6TsW9TxhdJdBRQF1McvDhKd4mGmpNaOP19b+JZcqFvls2SgHHrEek4D4aaFaEQCGsJ23Po7+NwLMhEswuihJSJt1FbCTqZSc/UjohHkbg4+9BniuC2FGDahWOa0cuGjY11XjbIBamQeCXLNFrr+FkWbnLA2aWyEu5nJdgxxqlRlzKmMbsxsNBTfQ1oe4rxYN+3tLg5DUzoekXlR1zrYlsR9bwNg+KaJy936YHGWCmupUMlhO75CCANGfNrH4fkUCKld4+SaA9OOGm5n1zznos9KpnrTU+ui3N6uZ9uXSjZtIriw13rq2lMaFYE47aB81ey5GtX2Z7IXonX1mFjNmCEv1LCtep70OY03+tUzoLTy4UwkKpJKKkZRmhw57MM18jbraYkRCWek9Wg8ZkzdKpgR+j+nC57ept5ErZjTEHpLIQesc1GkfaquiMGU/Hzo30f1dS829pqheyJ6aLm5+Jawe22Z4jOLOxe2u85XYkodTD2vZlez5KebEQGMIy9jI5mZKDTxtetsUmMwrCFXQ+Kud6HN5ioY7r1Nmiv9ztFhW87t8v5Tl+avB1MWFQkTc8Kusm7PXIRWEcy83hadZEWOPLJOpMXTdkgzkHrtCTnwvhixRvRd+AiP40xshVWkikI/XRQCE3PzWF7Usf9bU2fWs84SaK62SP+WTmc5cspnZwc0Xw5WFdQQEyQzPtNGSiWIY51xKP5qRSmCMkp3lIvQermeuljuVwD5u1gR7XwnA64PHFTXlNTzbUt6XBUml3D0/hxunK0eNRhDr3V/X27DFvZyx3ujnftsbLu+nq6pSgvg2AdIbq3DsigIFWpMh3l1gLXosHkI547CNhKxGyHcRGrUzYUhgzbKG/pZSx1aeR0ghzBdOub+ElpwGI6dW++XeLwzrlaBYPtOWy5LQGDRclKX8v07b6CCOg40bf9ZuD6PDP4Tjaqyi+isjmXaVGGyQmpXDG07tsMqXBxrV422ghNk0Wcd3nZZpBy3hZWRls6LKdZdA1bfDDDO1o5d8sVAnCS8Yp8e3ZtdWosZOqOJHEJINeGoHwNlaQWRvxwgqDyvLxc9nxwOcoOBONRxQprRV6FvqmMyD6i5XFihhxBLvptgnIn6qCAZlFwxiXUGFPCg3NDYl8mJobYcVxkx9n1ALXxhPQrK4RlcwuP4BwRQhZ3jPr15gjXQxrnqxMjeSNKtzzvYMEQyezQex2NZ6UViZ0TXPyksuOciXm33HVo5HiO62q2VJjZ3DBO0owYzdWsE0/SwU4pn1ty4UpyiNV4VC056Xh3eQo3OuFKXHkU4VPUGZok3SGtQ3MdCvdrg8t3fEoyfEoXBLFZb7Y1cRyO8u7GI3BV7UXrjoLxh6gHE15Z53B1CTZZou50y+3p9JI18TIitklDRAe25yHY7DI0PuP3ZKyvEtPaFKfG4e1uiqdzbxyTaplJ500xUjeWsLHQbTuNoRWGv8EeQCg3jTp5lwy3SO9LXjwlDGQwk86N+2wMCknst1N69Ld8djOXOLyWBnpTJyhsCscjCtXL7XbpK3sUu20tmeCyPdwLLkCW0O85d4NSeb9NHTTQnT3CLDXbGUvrDAaDCR+XeIzRbXH174W12dhHEWVFK+QicaSDlbaaLsRgs/DYVc3YH9NxddHvQ71OJbsIV8J0tMTEbgRTQCXxEKv26n7P/CzZ+hYziHDg7OS1PWqKWlWojCWrGh0twVyv4GbF+VNb14dJ0ThPobDlJp40NkpbvW1GmKHj62WS1GO+btXccemrarTkQAWeVsGXzLnQZO17kAhJjDKWecoPa2F7vNxvd2opSec1TOhXd32zEFIQWtTfBmvSOyMlvsIgZSSm4zVzu3q96sT6BlpQ2xUJerlm1To3qvXaJSchkL1AdPMrcx/pDdwdhn66IlnZob3KLWHomObe0S+KgmBLsyo9/BwhbZnGDXFvmPrEInzKniqS8TZ6uTcnLTupSHcX4UO0K9uL4SJhu7bdJVZx+GaL2dh5veHXY7Ul3asdW8OBle+sGntKXDqbHq2RtROceKmDYqNBjmyeX+nB1km3LTdGgNvrPNxa3aofKVtDQ5OqtTW7CoMcxyBqopWRY1wGJTExsnPXQM5F5/khdS2mLZ1fKWNdEcMqwUMQ9+SQIpSx2QT1NjIa+WJCSNXqzFY/Gks/vV2R2Bq3raSLCqIIiLCkjsvCJnhP749uYmCVcihEyOvOoYcOTaNiiYcVNzc6SwJqasaFKFw64dI72/Ybe1ednK3dVubdyKckMlTEsif10uCJGMaNP2mtbvjREjrrE1PKGscbEVQjO99Cl/Fo2W5ueb7BYVl5RRpuj15u2nRflVQoHLnYC6q1QCA4iV57buPi91A6Lz3yUOSu0p/Q5OrsHSRjPJWMhXazEjjKJa3ueDzZKsKieBE6kUrAVe1uCU28JsfkcFa3ZVFDg7pdEZiwIUzdFSCsH+seqVhwKhl2ve8ZJLbeCeauxpreQzMN7bzVfkVBWl26FYGSY65VXnvwkctWRbU2umxdq0UchrMPY0tPhgU7xNIqphCFaWdPM9eWquoqTLnybh08HaH3o0HCMC9LrdA6HkpbVp/lYjos9eZau401ISkmHSkNu8ZNNGwwIZxiS3OdbLxxXVWP7hr29jrBUvubimEHlmFrYT3srUBrUftMklsnrfo1d+nMSW0IcTqflnTJblf91mPRLK0uLQIpB+Jw8XtkNcA0cnL6tiSWU7+FNcUZBM/Fl+YGOqSbTPQQAok6QiegDAEHX2fq4GXkISi5tWwSdJ4bGTUovyDFzcBCRlWjxPvRcQQTPQEWRM/5NiVAkYCRDAL8r2m22ehsx2X12Siddg1XkKkDywoJOrAm7JvXg0QjKYHbPb2bethDrp0GD0qCyzqeTzR+K2xn8jiUZNBR3ZGqb7VahFJWTuURpcCr/VJjNrJlH+lxW6LHSPNzhT/yLhHzRAwOHb5j0vn6wnDLW8g6Z2E6b5OovYSklhFRE6BB2mEOhOjE6XrTUaKftgDuXSR25bFAFbow15DqGtpOG7OBDZjOlsx9qze5oXAO3eP3QPMuPXRtguFk79qbkNlejjYCqR3vbDJu7uKhw+meONBVtz12/upOqNi1EcCZHMIpTmPdeJfsSJL8+9uHt/k51utZ5H/jx0/zs5L/Z49snk9X3n/u8Hjq55rO54euz/8d43768FbZ4Wza41FVnbT+63HOnx5UffzXn3PPcsbnb4zen7s+H+g2pj//KvctzJy2bqrxa50njx9AgB1WW8+/4Ktn623w/vtHmXkTuBV4f5iemvOvkuafEM27XD+cf8UzPxsDgfiaZ8nDp9ejceAK+mn1CX379X8DISy9sxYtAAA= -->
