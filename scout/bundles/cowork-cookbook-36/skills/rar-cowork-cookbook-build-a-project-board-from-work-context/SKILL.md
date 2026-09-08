---
name: "rar-cowork-cookbook-build-a-project-board-from-work-context"
description: "Reviews your recent emails, Teams conversations, and related files for a named project, then builds a monday.com board with project name, task owner, status, due date, and priority, grouped by workstream."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_project_board_from_work_context", "rar_sha256": "8cd82b69f908fda7e0daa99d82cbae515e735e140ecf7fb6b9bbeb1841dfaa81", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_a_project_board_from_work_context`. The original RAPP
agent is preserved byte-for-byte in `build_a_project_board_from_work_context_agent.py` and in the RCI capsule.

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

Build a project board from work context — Reviews your recent emails, Teams conversations, and related files for a named project, then builds a monday.com board with project name, task owner, status, due date, and priority, grouped by workstream.

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
  Upstream entry : https://coworkcookbook.com/recipes/build-a-project-board-from-work-context
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
    "lookback_weeks": {
      "description": "How many weeks of emails, Teams chats, and files to review for scope, stakeholders, and tasks.",
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
      "description": "Name of the project being kicked off.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_a_project_board_from_work_context_agent.py` and embedded as the fenced Python below (sha256 8cd82b69f908fda7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_a_project_board_from_work_context_agent.py` first:

```bash
python3 build_a_project_board_from_work_context_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_a_project_board_from_work_context_agent.py   # or on stdin
python3 build_a_project_board_from_work_context_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a project board from work context — Reviews your recent emails, Teams conversations, and related files for a named project, then builds a monday.com board with project name, task owner, status, due date, and priority, grouped by workstream.

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
  Upstream entry : https://coworkcookbook.com/recipes/build-a-project-board-from-work-context
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_a_project_board_from_work_context',
    "version": '3.0.3',
    "display_name": 'Build a project board from work context',
    "description": 'Reviews your recent emails, Teams conversations, and related files for a named project, then builds a monday.com board with project name, task owner, status, due date, and priority, grouped by workstream.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'intermediate', 'integration', 'monday_com'],
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
        "upstream_slug": 'build-a-project-board-from-work-context',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-a-project-board-from-work-context',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27367604374329b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/set-up-project-boards'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/build-a-project-board-from-work-context', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: monday.com plugin enabled and connected to your workspace', 'Output matches: A ready-to-run Monday.com board grounded in your actual work - with owners, statuses, and priorities already in place so the team can pick it up and move.'], 'confidence': 1.0, 'deliverable': 'A ready-to-run Monday.com board grounded in your actual work - with owners, statuses, and priorities already in place so the team can pick it up and move.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'lookback_weeks': 'How many weeks of emails, Teams chats, and files to review for scope, stakeholders, and tasks.', 'project_name': 'Name of the project being kicked off.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Spin up a fully scoped project board without the manual setup tax - no copying from emails, chasing owners, or piecing together task lists from scattered threads. A ready-to-run Monday.com board grounded in your actual work - with owners, statuses, and priorities already in place so the team can pick it up and move.', 'expected_output': 'A ready-to-run Monday.com board grounded in your actual work - with owners, statuses, and priorities already in place so the team can pick it up and move.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'monday.com plugin enabled and connected to your workspace'], 'prompt': 'I need to kick off [Project name]. Review my emails, Teams conversations, and any related files from the past [X weeks] to understand the scope, stakeholders, and outstanding tasks.\n\nThen build a Monday.com board with the following structure: project name, task owner, status, due date, and priority.\n\nGroup tasks by workstream.', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A ready-to-run Monday.com board grounded in your actual work - with owners, statuses, and priorities already in place so the team can pick it up and move.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reviews your recent emails, Teams conversations, and related files for a named project, then builds a monday.com board with project name, task owner, status, due date, and priority, grouped by workstream.', 'example_request': 'Kick off Project Atlas — review my last 4 weeks of email and Teams and build a monday.com board grouped by workstream.', 'inputs': [{'description': 'Name of the project being kicked off.', 'name': 'project_name'}, {'description': 'How many weeks of emails, Teams chats, and files to review for scope, stakeholders, and tasks.', 'name': 'lookback_weeks'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when kicking off a project and you want a monday.com board scoped from your recent work context instead of assembling tasks manually.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BuildAProjectBoardFromWorkContext(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildAProjectBoardFromWorkContext'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'lookback_weeks': {'description': 'How many weeks of emails, Teams chats, and files to review for scope, stakeholders, and tasks.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'project_name': {'description': 'Name of the project being kicked off.', 'type': 'string'}},
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
    print(BuildAProjectBoardFromWorkContext().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1Hf98H2IzOFGATki4pohASSmAcJgdORZp4HMQiQ2/+9D5JueijX63JHf+pbdkmCc/a819rH8Mub03dx1bx9ftMDp1xwTp4ncdAsnNJfMNVQNRn4qDIX/LvwqrJrErfvqqZ9+/DmB63XJHWXVCXYrgW3JBjaxVT1zaIJvKDsFkHhJHn7YWEETtHO229B0zrzBnBx1tAEudMF/iJM8qBdhBXQuyidAlypmyoNvO7DoouDcuH2Se634GZRlb4zffKqYuFWTuMvhqSL3xc/toIdTpstqqEMmg+LtnO6Hijz+2DhA1VPtXWTVE3STR8WUVP1NVDnTovZ17ZrgKmfgHPB6BQ1MOrt848/fXhLwPe3z7+8ebnTgktvm9keWnmq3cyGsE1VmEACA2IUjB2QkDtlBJbWE4hvCX7XQQMcLMAlPwgXr1/ft0Eeflj8539mg9NE7Q+fv5SL19+Xt/l/Wl/OIVh0ldPOkfKc2nGTHBj/aUHngzO1IIhd35RzdID5SRl9eu78TVJVL/4x3/v+qeRTFHTff3mrgAmPXHx5+2EBIv/lrenn759mKfX3P3zKqyFovv/hNzlt7z7CDIQBqz99ff1+iQULf1uahIuvurJjXrpAPSR1AIT/zr/572n6S9wrJF+fi7+v6g+Lv5Y8+/MPYO+zAF0g96/FghiAnW+f0iopv3/paKpbUDqlF3z/w78S68WBl+VJ2/1bcn98Co4DxwfReoXkhw+P9P20gF6+fZP5r9XWoGD+jidg+bu6b4H6V7Ifmf2T6DwpQc+95/Ivxf3VBugfix//pW//3YYPi/DL2zbIEwACjpsHnxe/PErkx+/83y5+99OvQPT/UYwOQMZ7SPhaOGUSBm339euP37WPy9/99ON3ff1s5a99k/+VzL+K60PPHyL4WvX9H/cC/acyKwHCLL710OKXqv4fza+fFmcnT/zfrrefF7/vxPkPWsxOvCt9huB33dgCW38Xxx/efgXwUwJveu9xG+DHf/zHQky8pmqrsFvoXtV3C5DgLimC2XgjTtoF+GdGjSaYETcBgX2teyHlbHEVLn7+n94D4j96L4hfPoD2q/P1te7rA2S/hgDcvs4Lv3pPePv508IA4gGIRknp5AuNVpQvpRPNoA9U103QBs3tgatd8BF09cf5yyIpFz//mxq+PoR9qqefH4idPFFQYw4zArZ9HnyafTVncnh65gH2CsbA64GevPKAUQ9S+QBi0Fb5DSDoHJc2S/J84ScAYwCLTU8S6svPs7Cff/7Zddr4S/mEbHTxpLd2CRZ8M2fx8SPwLsyTKO6+lIEXV4vvfvn1u8X/Wvx3ux7CZx0K4I9XZoCFR12WFqDT+gIsA0kDaQYw8sjML7++YgzEACZbgDwmYRI8N4NKzQL/PeD6nv6I4OuFG4BAgyAXddV0gAcWSfdpcQgX3+wFSudbM1PEVdst/KAOSj8ovQlIdYA73yJZVt1iJuo2BBzZt8FD689u4zxMLEDLO93PC5FRAC9VOfi/2czHIrC5KhMQ/m/l8LwOhDTftYvNu4hPC2muzUXtNE4dN85LR+g88zJPAq/tQDgYCoLhSzmzcDCH6tEoz/CARSAy3iulH+ecg0GjAKjgt++6H2sec4bxYNHmS9m+msBp5lR4gBSA0qhP/Jka/utVUm1c9bn/iB+wdJb0yoL/ysqjBh+zADDxfQh5ziVzQT9GisWroBdfegReYYv/n+ak2X2a47QdRxu77WInGZr1TMvDaeDZc7oEIh5GP1rwtwnmHaXewfpLmSegxprpv54rH8l8rXkCYN8AGzRae8gHlQTSMst9FPpcuE0zt4jzpXxnBeDH4gGBINcAFUDXzMX6rnC++25pDFr/wzONrwnhURggdCASoJgXde/moNDCIPBdx8uAVc3crK+0gqoP5sYd4sSL/+DVAkgHxQXkL4ARCWg/EPNP35D6effd9D9sfA5C85bHkNiDXm0eAoAdwWzgnKM5scC87jmZAz8/P4QAN4q6m313QSEVH14Xgya49kmbdDMyPuMa1ACcP86fT0/nq8FYgzoBwQJtUPcguo/GmTGlAGMOsAFgB+ijIikB7YOgvILwEAhqC7gDUPY1lz4lPi6/HAoe3Tbz1fvG2ZF5zzwCPFvHKaffg4XxV2UC5BXziofeP1faN22z7BkwWwB6QOP73ees8OlJ9895YvEu9/M/HX2+/3unoweBn/5YAJ8XcdfV7efl8km675w7N+nyaWv75N+PzsdXp358NO/HOSIfX0T9AJM/iH96/nnx90z8g4hXi3xerD7Bn+D5lvAqsdcfiAjzcWN9xOa7X0ot+A1TgfqqADU252+aAeKdAN+XABaMmiCaFz8JsZ15dAB49WAAkIwv5e9rfu45QDBlNNdoW/0OCx6TAKj/Z+6+ERW4VXZAtz9PkVEwH98eHdIGb5/LPs8/vM2A928e22ZCKubibucDH8gDGMy6JHj8ekV//vrHw6/8+OLknxbboJux/PcF+KKRmUZ/1ydPR4GDHtDw4QG67Ux7wNFZ+dxjAJ8fYD871E317MHzhDfPhPmcVIBDX4cgyNp/NmlfDaBZQRc97s/Q9CeWART+Ypcnq8wk/uCmR4u8zAK8kAVxlQPkeS2eWaP9S4u+jbD/bIwJlM0K/OrzTJ0fXvAEPsGx48Pi2wkCxOF1pnucwcseHJd/nE8vc2IeW+YvYA/4+Lbp23+KcIO3n/7CrvdJ81kEfzZNmoEJROcFmk8KD2aoy5IHX1Rh+BfuArkPKAWENJv4m++/WVA9DlMPCwB7P8/+v7yB2nJAsp1Xdb2mcbAcIM/Hdp47lqAJgULw+9ku4N7/7Zz+EtPGDhgQgRzS80nEXVMhBZOh7xAB7DsORYGLnusE+AoPCBQPVhgceCERumuXct3AXZHYyg8dh1wBec/e+zrPWMlsGk4RIUxRSIitENj3gxDBfJ9ck2sPJxDYoVwHd3HKcX/bmiWl//L36d+vjyS9jgxzXF5u//LmrrG5lLH2QD//mCW0cpeo4Gq1AJUwOcZLZFvvJMaoR8npy/u5MFjSrXuMiFs0sHWmam06k0Y13tDiYZOXWX2Gxi0RK20GoRdlSyd0xahEbtS3dT5OiaqBCbNZ45RHVRN92GRkU3oakzT3Q5jbGm87tsDxI9/wXS9e+dRKpo41bvptr9yW1PbG2rfOrSar9s+xHp9q6ahfefSU2MXBm0w0zpzl2TK12sN15ajV6Z47CpvzYZ2pNsg+LxxdXrDX2FEPkgvfnYRDpkV46AoHNBeqOx2Zl0Kvw6ZIISeJS93daUju1MkhG+ppuAqjfdJF25kmyGHvUe0TiZu0bXLdi23nE0N6Gu1I0gbRqMlluERbKCjxdr1kWzwsG5Q8jGHuIOEquRCH6wqeaFMnLlzdG/35fo2PRMzhkXk21/VW4ymB08cAGfZw7lI7eqqq5nAdxG0DU754KZrhbmorzqouRzW6xJY94BzdnIiVvkl5LYrUo2hVWXJ3rIvprrybYZJEYdopMkJl35zqnEtS3VDNSR2irXJFzORAsDqfE7xDy4HKsIXv2PY105Fd7jd7Z+VCIxdd5OnQRfS2T9XMwdK23NslihaBSclD22Jn47w9Ogl/lViLNQZPSPIovdv0ekMcWoZA2mmHFwatkO5S1qUG2VHmUBLX3XXFQGepqU92L2TXUKi9NMhRYmSDaxrgLi0xTNFMzcScRPLunK7+pbp26SELd06ns+fed9JJDhRf3IrOrtTVo3wI5FMqV0B4x28ZeIdsDqRuJCXpCkfDEI1EMMpL7Kj8OXK4Trpy7bkSzJx2x2y1Jq65FcNVJ0u7oBWvywLdNJjJA0hMtiF5uiRXEeXM1uoD28+LJKQSaucez9thH6KVNGgKS8T0xI02ea6j0VFw1ITEe6sTAiqOspHwASfkOH6Ayzxn70ONrfOzUma5gsBJfrTg+l4neCbxpXvxljvovrdqmSEt3YK2GsRtl/uiIdcZuqUOGHJfU4ewxtEID3i4Zy+TiA1r895YA38W3LTi6US9+jnk7rar8jCRHXPxj1F4UD3jGKVnhi6y8HhkLLmIbKnRzN6+1Ee2uN5j0lV9sXQasYuP4MSXi/vknOfRepVsUOZ84hih346eQEDFIS6rtKFNOBElkJFYEDV2e1CO5CRPoeUZzEhM5RoL0IFf98HVD5SVlzNCPcrsdTI2QZ6pqngxEn+rkf4xgyMqSocQCoJRKrPEH/rlPUXu6n3lm8FuDTdQGcoc6jCI7d98qOvvZb4UdEtx2RPvjxv/SsRepqeVsk20qOcxJbPoey16x1tQWOkBRflW4Ril2fCWAQ3phOz0ioL1iJVHrSLIjrwxUHY0p/1mK7jbPhCzoU2FRkq1S3xNHRhfXnUj7zOzZgPy4hH+OUl8iD6EhVoXrN4t9bx3Vmyg8pkBSdlmWQUhfeZC5XiKK99USQGV6GXC+iskalhjWpeCeZDwqV5GUUlPQ11tUhzPuDSKsaWtQ+w97SKz28aStD8OrUqyJrdbx5bEcjhd8IjuuLvghPdHpiEbFdI5QjwmaFhkqwvmHZUteePTi30jlJS9X5GoaHD8thnKfXBL2z2c8hMf026wq003I0aSTZxaKMpAOUkrAUMI0IhKLDGEnoi6Z2q3bSGcLH7Kwv32FpxImNo16Fo91+WoSUl8X8NqyjtVdICoprioUGYxXWlDQr0deCE5svZEHjl/kwvYhpd5FVXFxlYPh5s9CYAVNNwJZF/N7CN9Zi1SheTh7qiCPaQMx7vGoJMrJq2tVXHyNoZ6iHaKnfrjkQXdx46bGutsait2soVd444WADYL/Wos83ol9E7u8TSs7oXxWoVSDOJ0NhvcaZ1KinwoT1Avt6dRk/OsQBSG23lL4cIioXIB4dIirjztCy7UeSjcxOcq3/P+qnBclayoY5TQTUaSgbItByRBQWduu6sWq/drO5FhGO5zdpj5wMhxjIQgSplOiH9x86OqIX7ZI+OG4SZVOJ1oT5Elgx6n8b41r7gpXyNt9C6WFcdydXVdZeMmTmIHNKrpGg8B1t0tk9tu18eQf+V6m6FqjelamMk3tKmp1nmbFJuWa1dZy5CiBZpNIoGx+Hha+1ZwrhkImsLTTsSbkEeg8VrY8KrGziLbnk/lIQx6VL5kRgXD57BDhLZd3YJq8gIKo88Vd0gPbqnrcAl18YZf0Yfj2A27zhTKwr0P8RlWonuxVpOcbArDyoM7txxWerPd5rEl7GhyrM5e7uPFsqWxfZZUG4WwioZwrkeD9iqGx+LOL/YHR/X3Joyu69OWVUNjs4mC0x0mjoxJ02uDyUxua95ltVqekc5OMv2MlvBNOmc+c8ya6HClL4N0SGIvyc4np9FgqmALrjvumw2d3o1zycqxWO5LyEu2nkZHmYesbKSJecosvKM2RNhmtId8m9A7eeuf17ZwPLXMOWv5SB+JDvEYa9xj0kq8ccnh0pxRvZEvLCTbrnGS72c9C0D+90UeCoeCUwuSjWj+cC+LTuDVHuLu8WbNIQHrnDGAQfLay+mb1Z6wG4ea5yFfF2czrMV4SuGGydWLIWZXK6XicxRsTB7dWdVO3x1iwqa7EzOsUX0jZHGgUKZS71X44NCXWL4NeAhVmYVtqeRE2Vh42AbSgNCC3CcbKZ2uMGwSa/tynO5RrK0ChEP2WK5j2WbalgzFEuuJWBPqKGfjRY7MfLS7y53EejptyWJLFoD6rRKxaqc2EA6cxtSJoBxfXSerlcbUM4UOZ4YVUFqpxJMf1XZRCkHMjmy1W/Htpk4KcmjFYk9DDuPU61igt/uQ3oxr7dBPcSqNV+qS2iq+W8IIbreC34na5rTdEC1XbMq6O1Sr9WBZHHFsSOli1cpp1QmRdRTyCWPEOB/5kbJHEWayanBMW2WFswFkTMV0OA7TQHRqdN6RW4ZQatE4WbknmF15BSsdXEgZSsy57HyUhoteRto2BuDFg+6Si6DK5L4aVitZr/vEoOVtCqJgeI1xZrwjPZJamPPHs36AK/y4jpfjJklpnKwvR1OVMGHj7yzWMfNOjLoIxzcrnXXrk3RrBLoyi7sG9425vaAoJ/G1pIYcrFmNaNC4dqp0gzb6msscGG1F8bDfIZh70FKW1fKBa6XWwviM7M542sYuw6f34MjzrpthZ2jiV7GU1Fe9rLepz9RxfzwZJb8irQvGrshlqxZ4rO+TdCf6aZ56Ut02ZrzDrhelNhr+cL6shGpIr32PuI0Pn6De33snbzSv6AYDmDbl9a5z1whsDqeeIcTeoJZ8LR9ZtDdU3sylhmmuzZ0JPccP1Z3DxJy6jXf3Y0jTuEj39NZwTvaNWYdiqEU3nmaHcWf1SSxN0OHg+xFrLfmtWFymAuuJXTmOLbbS5bvKCNlNutcSv8V7ZhmqIcLFSzK8ZSkh7NYBipcRMp3cjXifZKZfi9iGDFooJAKa4y5YfELMfUZD6gbrj+dqJcJbCo5jKu2JAj9nRoci+TmLoHHQ5TDBSqjtSAgPTkvJ48FEeHTXfet5XOnSFZWKiJsvjT0l3qHeZFf3DqHWMrtifftU6Bd/f4K6MaZarhNZApMvl63AiPu9sRvxDW+yYedvI8unZZPZDQxeS5Zv74q7it3kzFrzjdrX6Bbhb6fDsT7b7LWJLhZMyvv0jmnKaJfbfbZaQs38m/UKd4VS7IHvcFTcrqE2hxg3HI1RHrQAp3eVhtDncqCt3rpMFTOQLSPaKC1HvcdOG3iU9uqmYEvFOXV75Hq0aPM03Bm1toQbvxPIcDvF/cVB2+vuNCYuW6spMij2/qRDeuLxCEP5KJVpgD88KK3uypnDU5vlvZXgeEo+FKpO5BWdTYm4aa3RKnNJ3/KrfXlTL8gR9uxVfdJ98oKHoris18eM1lTfhu6nPSqTbZd3YHo/C7jt3a4H6ModVvdQ4A2FxBqWum/MVbMUrqwS3v3OpWvUi0FPR2xggx64wbf9kFOH7dCdTvKoaucVAGMoviUkvcKxs96yUG9sYcJVaKWxYT2f9lGg0mQZbok1HbceIYTDdtQodSnDccEFOb2kery+M5EwEoLNOAgT0SyxIYKS4nB87yG8I4kRw3g3uxQFNbuzrKcb10KpdSRCaA+p6wK5NzK+lHj9dNh52/O1h+/XUBYjs+HvRKHAR4uZBooUWc4nlvKKTBDlsIQCBoW9XpRMfaknmo4Ew71wnQ1l9eo04Pr10FfoWnYIXN1v4xUcqDUSqKglawShoOIpbjrkLvf4eNjRZmptOyYjagSjUWdU0LL2ZZZRsqZzAwwu0lLSWmIweoeLEJEq+87ckEk4+u7pCA77paOc8LK8aeEtv237u281TuHH2ApH97VO+N6d6aL1ba0YZ2fNRbi1hLmMFDX7eL3yMoJfXClSqiS/oacNYXdMV912UZBE9Q1bMgpNudKpS9K1fLv6BXd2ju2Y4RSiLdmDTqsbE0zcHX244rXlSrBZwMtO3msDwpfichtfXVuA1u4+LocWx5XQTGPfQlDxJmXEnt0wonbdC6cAuXVnZLztad9ZLiELWmJw0J5t3mD94rYcrWXqbnP6SjS6CfX2nq25nhOMvZxySiHTqYcUEq2dPVwCM02ghXS5kiQNlgGSwjYDHQRdq20skXcp4FZjM7gbmdEo/CqNDl4HiF3c6fHi9isBIZztvd2YygqmrROfgvObTA7aUHKcIN56dtgpY1lUeYOsw97mBXyr5YfySifQRVEvF+8M7QovgyxU3MuB30nZBA5nFi5w10E4UFiBFYp/RNGL4gLwLkRojV2PsYGvD2YW7LOrsvLP1xpdWUs/buMDvdehKNFpvdA3A7RkPNsHY+u4NVgt4/KmOfkWczkx+tltC9fsS9stY5hfYcTA74XVxgIQaO/bpV+flXY30psenyhmshJ4uRv1SsXiirCSU32qd7mokV4Rrvk081OnqnahKVtlgx1H4xybJ/+CYNK6rtbDnfawA+LxAO40pNXLVF2lR/R+m+AmQfaWTCO+ouYY2wyxKp+PSngdAuV2b9s7LRKqzwu7m7TUDSkf7i3aJyO72ymiLabKmoJ9CaQmwhRyva5FhZLi5bEGbYSjSiJgWz0h71coR66Kr13X/bi5exqMyydPYgkxjZYF6djGynB225D1dyJPIkZ5uASys8fTupogfS2ZS2vDWScPMJ08KF6omSSHBrvV+RItLda1ocNVlm6hJDtGlxddGyJHzo4EuZM4CJKDIBPSDZ9KZI7BEKr0Xazi2+1Z9o3Mu7iqeLsQtgWKl95wU43edi3pyJa6z1JorxQnfC/Z+zHYM/tqnPh1ZF4HNOjPDd1cRDGwpIYoVq4FiRxMNejFNJAuCG/1qiwh7XqrkINPhWmymtCcXmEnWERIualDMEcLV3i1cacbk5/KloHwaDTz2406w1cv9CkLDc4F2S3XEWXcp6aFe2UqA1cHh+E4X9JEkhTDJh1Z3G1uXnMTJndl+lo0Ok1qytLW9A+p4+EWmCuHHUHdfaW6pkvOPFPwctpXe+wonzTzBIIboQ1q3ZsNyVUE7xerBr5VtxTzDjuj5Vdc2hZoxaT6rfAH7qALCbnRKy1ebpgcXilFA4Z8ac9nez2wuY5kz6cgSNYajGFZuvamARHymjxx67Vhapf1MN4okptadm+XvrIuxGmJXHssIat9AEWFum8lL3F7/aCdpp2ErCBmH1xbSgytYe/nGpFYQm0v1aWKbgkRrxCyIa/XLYzxRkcwhIBSCsLUm8ldw6BnV0uevDTF2u5sI08DM8hd7XbvvLVyPUv8hDB+cE+LScAYqVHMinePqehTzCBvNyhS3I10tT2T/vEiUyo44PDXtZAskVhQr2mcTfLQkRxVwFsUjFlrGT4nk0JZKl9VwWnkVU1xg94IehYmroYgNAa8OxIbGQu8sWRhccljub26+RaR9cszbOAGXtzWegLgSUSnJsdCr1+HRKvsw1PhQLuLtrOPtkXDUWjTBBYfzxsMvifEDblF/bLuDwe5D/Ieu5vVRdBkSV0j6Hm6epO2glC+wQAL7Y8G2INQF8WP1pSVE+7eUDSDiAocOg7l6tiVcrvfbqcjvaLEi9r7V/F2VwkHVW6aOUKWxN8CypiQm98QSYjtT3kyESCEh0lqSknAcQxZAQzx+FsqBlHAWIpHpjQ4bTJbazpW+4QIhYjGfO42LI+bFpxMAsST1ZNHlEo5bbpWuQScha+J2ndherlJr45gOWvAVpAKQI294L52gQnyfBmoEF9jAnF1Jcy+7aRlY7c7f1lOKDVI0dhQ5iD1KOxWl3BTocKoDHvd0CjUETokO2/uZ8PsxjK4LE+nDRri8jG9hQpm+l0jya1dozSFyVvoQuRurzhoE0qiQ56Wd0tyMHAw3WwIUqbpuCmNmyCgXKlWRi02vaFABrJmWcXCInV5V+iMVyWUr1HOsZg2YjJqtdPUAtFMf99NxJW7cf1otbZMY0R1JoVKRmgz2yYR0Ze4rkRiXPg9lvvDcNn728YlJ+RATVBIBUuTJnnFs1AKGwg0OAZFGxhTgpzSzsZul9ZGj9ZEjEqMN/48zlh+5MC4vxnCPL2gzHIZxvfROW37gS28ZUrb0PUorUt99HZNqpCeh15QThlwquSTS1AcKH+ejXGbahwNVyOafvvwNj+iez3E/LsvUM0PXv6fPf95Pqp5f0Pi8XAucPzPD12f/7ZlP314a7wE2PV84tXmffR6MPSn510f/83n4rOQ6fmG0vuj2ucD4M6J5ld535LS79uumb62Vf54WwLscPt2fvOvne32wOfvnzVWXRw04PNhf+HM7zTNLyC9ze/kzS9ABH7idMHrZ/R6BPjh7fn6zfyQbPbx9XQduIZ+gj+hb7/+bxDVG2V2LQAA -->
