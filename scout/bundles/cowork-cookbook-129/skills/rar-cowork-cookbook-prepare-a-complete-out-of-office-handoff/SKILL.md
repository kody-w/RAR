---
name: "rar-cowork-cookbook-prepare-a-complete-out-of-office-handoff"
description: "Builds an out-of-office handover from your meetings, emails, Teams chats and calendar \u2014 projects, status, next steps, action items, internal cover owners and doc links \u2014 then drafts OOO auto-reply and calendar changes fo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_a_complete_out_of_office_handoff", "rar_sha256": "80aa756c2e49a7e989a5d8a1c60597e22fa161279dc43f9db4e0ecfa8822d839", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prepare_a_complete_out_of_office_handoff`. The original RAPP
agent is preserved byte-for-byte in `prepare_a_complete_out_of_office_handoff_agent.py` and in the RCI capsule.

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

Prepare a complete out-of-office handoff — Builds an out-of-office handover from your meetings, emails, Teams chats and calendar — projects, status, next steps, action items, internal cover owners and doc links — then drafts OOO auto-reply and calendar changes fo

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
  Upstream entry : https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff
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
    "internal_team_members": {
      "description": "The internal team members allowed to be assigned as cover.",
      "type": "string"
    },
    "ooo_duration": {
      "description": "How long the user will be out, in weeks.",
      "type": "string"
    },
    "ooo_start_date": {
      "description": "The date the out-of-office period begins.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prepare_a_complete_out_of_office_handoff_agent.py` and embedded as the fenced Python below (sha256 80aa756c2e49a7e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prepare_a_complete_out_of_office_handoff_agent.py` first:

```bash
python3 prepare_a_complete_out_of_office_handoff_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prepare_a_complete_out_of_office_handoff_agent.py   # or on stdin
python3 prepare_a_complete_out_of_office_handoff_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare a complete out-of-office handoff — Builds an out-of-office handover from your meetings, emails, Teams chats and calendar — projects, status, next steps, action items, internal cover owners and doc links — then drafts OOO auto-reply and calendar changes fo

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
  Upstream entry : https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prepare_a_complete_out_of_office_handoff',
    "version": '3.0.3',
    "display_name": 'Prepare a complete out-of-office handoff',
    "description": 'Builds an out-of-office handover from your meetings, emails, Teams chats and calendar — projects, status, next steps, action items, internal cover owners and doc links — then drafts OOO auto-reply and calendar changes fo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'read_only'],
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
        "upstream_slug": 'prepare-a-complete-out-of-office-handoff',
        "upstream_url": 'https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c6ef61e55f6776a8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/hand-off-work-during-absence'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/prepare-a-complete-out-of-office-handoff', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A handover document built from your real work - projects, owners, deadlines, and supporting files - so coverage stays clear and execution keeps moving.'], 'confidence': 1.0, 'deliverable': 'A handover document built from your real work - projects, owners, deadlines, and supporting files - so coverage stays clear and execution keeps moving.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'internal_team_members': 'The internal team members allowed to be assigned as cover.', 'ooo_duration': 'How long the user will be out, in weeks.', 'ooo_start_date': 'The date the out-of-office period begins.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Step away from your laptop knowing nothing in flight will stall while you are out. A handover document built from your real work - projects, owners, deadlines, and supporting files - so coverage stays clear and execution keeps moving.', 'expected_output': 'A handover document built from your real work - projects, owners, deadlines, and supporting files - so coverage stays clear and execution keeps moving.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': "I am about to go out of office for x week(s) beginning this coming [date]. Build an out-of-office tracker to cover off on all ongoing projects and tasks that will require things to move forward while I am gone.\n\nThis should cover all team meetings from this week, all emails, and all Teams messages (both in meeting chats, individual chats, and group chats). Please also analyze my calendar for next week, and any projects that have action items for next week and include these in the handover. This should cover big project asks as well as smaller project tasks.\n\nPlease limit the team members who are covering to my internal team members.\n\nFor this handover, include: Project name, Project status, Upcoming next steps & deadlines, Action items that need to be done, Who should cover it while I am out, and links to any relevant documents.\n\nThen act on my calendar for the OOO window: set my out-of-office auto-reply, decline or delegate non-critical meetings I'm invited to, and flag any meetings I own that should be rescheduled or covered. Hold all calendar changes for my review.", 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A handover document built from your real work - projects, owners, deadlines, and supporting files - so coverage stays clear and execution keeps moving.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds an out-of-office handover from your meetings, emails, Teams chats and calendar — projects, status, next steps, action items, internal cover owners and doc links — then drafts OOO auto-reply and calendar changes fo', 'example_request': "I'm out for 2 weeks starting March 3 — build me an OOO handover and set up my calendar.", 'inputs': [{'description': 'The date the out-of-office period begins.', 'name': 'ooo_start_date'}, {'description': 'How long the user will be out, in weeks.', 'name': 'ooo_duration'}, {'description': 'The internal team members allowed to be assigned as cover.', 'name': 'internal_team_members'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user is going out of office and needs a coverage tracker plus OOO calendar and auto-reply actions held for their review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PrepareACompleteOutOfOfficeHandoff(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepareACompleteOutOfOfficeHandoff'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'internal_team_members': {'description': 'The internal team members allowed to be assigned as cover.', 'type': 'string'}, 'ooo_duration': {'description': 'How long the user will be out, in weeks.', 'type': 'string'}, 'ooo_start_date': {'description': 'The date the out-of-office period begins.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(PrepareACompleteOutOfOfficeHandoff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
