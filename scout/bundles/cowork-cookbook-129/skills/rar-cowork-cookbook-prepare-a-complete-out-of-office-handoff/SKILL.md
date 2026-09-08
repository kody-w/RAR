---
name: "rar-cowork-cookbook-prepare-a-complete-out-of-office-handoff"
description: "Builds an out-of-office handover from your meetings, emails, Teams chats and calendar \u2014 projects, status, next steps, action items, internal cover owners and doc links \u2014 then drafts OOO auto-reply and calendar changes fo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_a_complete_out_of_office_handoff", "rar_sha256": "80aa756c2e49a7e989a5d8a1c60597e22fa161279dc43f9db4e0ecfa8822d839", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/+V6WZOjWLLmX9HEfaiqq8yUAIEgr7XZIMQiVrFJQpVtWez7Inao6f8+Bykyq6q7+k732LyNMiIRcI7v/rl7wK9vdtdGZf32+U337WLF2lkWR369sgtvRZVDWafgUKYO+F25ZdHWsdO1Zd28fXjz/Mat46qNywJsP3Rx5jVg36rs2o9lAH6C2PVXEaBU9oBiUJf5aiq7epX7fhsXYfNh5ed2nIGj4dt5s3Iju22enF078wvPrldfOngL7VZVXSa+24KVTWu3HTgW/tiCE78C3213kWEVt34OzuKi9evCzoC4C9tyKPz6RdUr3VUWF2nzjWwb+cXKq+0AsFUUZQVsUX6s/Sqb/igFEKwI/WYVlEBtf7TzKvObt88///XDWwy+v33+9c3N7AZcejuD7Xbtk1S5LGp9pWuVQHmaglssEQSARAbIgbXVBExfgPPKr4OyzsElzw9W72c/Nn4WfFj953+mg12HzU+fvxSr98+Xt+Wf1hWLBqu2tIEhFnEr24mzuJ0+rchssKdmVfttVxdAe2CqGpj802vnb5TKavWX5d6PLyafQr/98ctbCUSwF5t+eftpVQIvvNXd8v3TQqX68adPWTn49Y8//Uan6ZzFQQsxIPWnr+/n72TBwt+WxsHqq36mqXdete/GlQ+I/06/5fMS/Z3cu0m+vhb/WFYfVn9OedHnL0DeV2w6gO6fkwU2ADvfPiVlXPz4zqMG8VLYhev/+NM/I+tGvptmcdP+S3R/fhGOfNsD1no3yU8fnu7762r9rtt3mv+cbQUC5t/RBCz/xu67of4Z7adn/440SBIQ7d98+afk/mzD+i+rn/+pbv/dhg+r4Mvb0c9ikLC2k/mfV78+Q+TnH7zfLv7w178B0v9HMjpAGPdJ4WtuF3HgN+3Xrz//0Dwv//DXn3/oKhDFAG++dnX2ZzT/zK5PPn+w4PuqH/+4F/A3i7QAmLP6nkOrX8vqf9R/+7S62Fns/Xa9+bz6fSYun/VqUeIb05cJfpeNDZD1d3b86e1vAH8KoE33BMAFfv7jP1ZS7NZlUwbtSncBFK+Ag9s49xfhjShuVuBnQY3aB3ZtYmDY93XvGLtIXAarX/6n+0T/j+47+m+qF7J9tb+679j2FWz7WgZfX0j/NXrh2y+fVgagX9ZxGC8wrJHn85fCDv2iXXgDMo1f9wCvnKn1P4K0/rh8AbC9+uVfZfH1Se1TNf3yxOn4hYMadVowsOky/9Oi7XVB95duLihL/ui7HWCUlQDXV0EMIPwDsEJTZj3A0MUyTRpn2cqLAcqAEveqAcB6nxdiv/zyi2M30ZfiBdrI6lX7mg1Y8F2c1cePQIUgi8Oo/VL4blSufvj1bz+s/tfqv9v1JL7wOIMS8u4bICGvK/IK5FqXg2XAbcDRAEievvn1b+9GBmRAdVsBT8ZB7L82LxXO975ZXOfIjzCKrRwfWBpYOa/Keim+oFp+Wp2C1Xd5AdPl1lIrorJpV55fgeLnF+4EqNpAne+WLEpQeUFANsH0YdU1/pPrL05tP0XMvy5l/JeVRJ1BZSoz8N8i5nMR2FwWMTD/93h4XQdE6h+a1eEbiU8reYnOFQgGu4pq+51HYL/8AirSt+2AuA16geFLsRRifzHVM1Ve5gGLgGXcd5d+XHwOuoIc4ILXfOP9XGMv9dN41tH6S9G8pwEIRWCVZxsxrcIu9pbi8F/vIdVEZZd5T/sBSRdK717w3r3yjMH3dgAI+S2i/6w9CoJvHcn/H13UYhmSZTWaJQ36uKJlQ7NeHltazMWzr64UtDJgdf3Kzt/am28Q9g3JvxRZDMKvnv7rtfLp5/c1L3TsauAWjdSe9EGQLYYEdJ85sMR0XS/ZY38pvpUMYI7VEx+BRQBggIRa4vgbww9Pf74kjQAqLOe/tQ/PmKm9RXkQ56uqczIQg4Hve47tpkCqesnjd+OBhPCXnB6i2I3+oNUKUAdxB+ivnm5pFid8+g7jr7vfRP/DxleXtGx5dpAdSOP6SQDI4S8CLm4Z4hagmd2+Onqg5+cnEaBGXrWL7g5IJKDp66Jf+48ubkBwNB/e7epXALg/LseXpstVf6xAgAFjgeitOmDdZ04tcJODHgjIAGAFxFUeF6AnAEb5LYIAouQLQAAAfm9aXxSfl98V8p+JuBSzbxvf4ytb+oNXatjF9HscMf4sTAC9fFnx5Pv3kfad20L7FedRCTh+u/tqJD69eoFXs7H6RvfzP4xMP/57U9Wzupt/DIDPq6htq+bzZvOqyN8K8ieAKJuXrM234vzR/vgNZz7+AUA+vuPMH+i/VP+8+vdk/AOJ9xz5vII+bT9tl1vie4y9f4BJqI8H6+Nuuful0Pzf8HbBiRwE2eLACXQD34vjtyWgQoa1Hy6LX8WyWWrsAODmWR2AN74Uvw/6JeneQQZAXPk7MHh2CSABXs77XsTAraIFvL2lxwz9T8totojf+G+fiy7LPrwVIPz+1aluqVb5Et7NMhCCRAJ9Wxv7z7MnWozt8vWPY7Py/GJnn1ZHv11g/Pch+F5jlhr7u0x5aQo0dAGHDysP2KdZaiLQdGG+ZJndpAvO1otG7VQtKrwGwFfL+IL2r+3SBed+7ryL/EfJltT5XgWWpav3pSvgLzD/PRHRAbZtmjgsFn82r2Lxp0zLsvzqda8+9h95ceUAYBbAxLduAMATQALnWS2XYrQafD9t/illUM/q9utiiT/XY7nzpP3HqgocFJegEfVBp/pPiH/rvf+R7hXU2cUEXvl5qfgf3qETHMG89GH1ffQBHnofRhcOftGBOf/nZexaQua5ZfkC9oDD903f/7zi+G9//Qe5gGBPPAZVbaH1m5C/LS2f49qiAiDdvv668OsbCE8b2MJ+D9D3fh8sB/D1sVn6mg1IZMAcnL9SDtz7v54E3uk0kQ06UEAI39r2HsVc2N8R9t4ncMJGPdyGXGyLEnsfhgMbwiB4T3juDgkIz9n5W98NbByHYQ9HCEDvlcAL3zxeZFsEAyb5CDDA/+02uOS9K/VSYrHY98FjUf5dt1/fHGy3xN+uOZGvD7VZQ+Di3tEqZ11jfomqZG2b9xjdi6OoGNCpg5V0DK1x57S5fiwpsmKyhyaY08RmqAUlqpOffItHtwWsYP7jQfGM5wQJ5R/viEvOaRM/TCxQUKO7PUKMss7UI+UyUz+w/JXdzBfmrmPiw8ai27q+qM2oOwJdDJfNJnEQ/GZcHxdesIXGwSdIlPTHlulGCDGjNuOvQtbd6IlFUrMe15c7C0MinWNhDHDrVEJarl/UAXVm9Yx3u6GmpvhR2gWa4Zc1y81nmojjLpMw+tG5Zp9drtMknExOVmy/CvihOkgeNerZBb4Y4tme6CHVHIMKYyLoI027+WnVVn0Hr7tjdR1afc/pIc6hMrHGg96R115b3HZZgewhYmNKJZLvUqYR9KtpmnJdqZCGJhRxuMH02tS23WWbnPGhEuK56R4Ds+Mel/JqOszGIe3uQtUeTU7lDiu7O8X7xZ7I8YoTdG4XPrBKPQsE2VGh2Z1KFp4iQ4Cya3o6k1Ha6JpdJwI+dZ54diPmUq7lkUat+1rF6ptUNtNDiNVG3+lwH5Lzus0euTCmCX/XevrikwITna5XTB2uzUHYJ1aJ1MH2ZFJ7WGO6QUwfenAMrV64efnNV1DC2tbCOOmanHbV46SkbTp450MYG1f9kO4v1y1rXsyLneVGnXsSuRl7fFfCvTU8Ih22o72g9oT+iI65SU/tOTfXt/WUEXjkVOVtug3YKeTl6HFLldJBLmaawoJzV9XzJBxazXMyPcWTCuHjo2jriaAw/HjUoBS1+b1dm+HQHrxQP59SeztW7UlnYVWJHWrtMxlZsXJp0+vKPlyj1lbJHnau9T02Y0cdsXLP2j7UUwN84mG1H6MaFzTEzMVeUxgo2G0ZT9zQawlJkx02B6EBb0NfEC3O5PNhJ940I2VnY43Ixs7IsVqYiOJ+dQfDmpv+wAouazpiQ8zhdNRtJZrubXKI7YKjeXgNn7VzP2LMeXDqo8ENdhDx6zDxNk1yzzY7aSc+7ucATdYHaKfcmg6KeJm5HxT6cOktRslaEb3vTddmpkc/zSR015QWOnnulmXwCNhJIjak0FOOGmoW25dXw4FSl7S0al5fKgU2Wi13h4yaDfJo41NcNoUeq9etciPdw65hwt0dwpvxII8SdpAP7BUPHZqWRto07+g5v2/n/TG28rN7dw5yH0G4vTEnL6xGnWk5Sriah0qft3bOmk19ENhLRV2qkcYQ6URwZ+TMMFmROvvo0pelySa5vpZ9CmkBZkUjizjwMWjX522DSHBfFlcevnvHTDchh4U3AncT8GPsxgo7iRE9T4VwMNxgV7EuKym5c2gbJrCZbBKqUAa2OhqwkOadQKkZwa8PAUbN3nHtwZAWwj3hMEUfwkhFYlGBVaddtY23FY9E9rbHtvOZo48sH4pXHU29FHbnsTlOFJ36lB2T8/bcx5p4zlq2sh6yP1xgTNnQj+leRv6pYAn6Glt8+UA3oVkdxlTzVKRgrVCT1vfIZ+IYHsVrNKZnMnY5jiTtYShcYb+LO5XvwXSQdpMxVJNuM9fLNfbS8/Y2H7pCJqtOIsUzMtpQcZj9PKDFTItAnoyzf5yV7uJwYlGxUHoRyPWGvHNrkD3r2FAaaL41pXl29e62aYndluvddqdIBrkPN3Et0NumEC2kV3xbiC9YK0lDglV5pqKeoBym2+kUclC7e6BixZItMwYxpuJUvIu07sqp4cZjdUvHI/503elmaw3SScnp2d9wuHNNdAVtLpMa3rM7d25EHZ1t3ZmTgyndIWXT8qlqBiJckkmqbuPB5kIt3IEhucqZ8VDZrUcc5V5JM2AN9SjQdR/YZHW+OFpfUKkUkqMiy0d0K59R9tHfdOIOURfNuULkvoOT+9CmE+Q2IFaOyqY38F2bIQ66uzdSChFhNqxvFzM2rUvvKXckQjVM5BheeMTS7K43Yko7LYp57ZFlCsfQEBECaYuOml9ryAbfYefyjEEebGYHEpdwHEIYJtTKEB54Ej/KEMQAzKLuwlGclNCc5rba5VueSa5byj9zawUzXF9UWto5kYWrQ9r04JCptOWHYSKnE74L4HjLHN1UOR3DXcfhN7lnyKvWp7TKng/6/RLN15QrTKTaaBnKc81jU6WpXDLQuYQvvK5dDflmb12apdZsRSU36La/nSdexy3ZwjyNuLK34oL6RmSHTMif7pebkELVbQ6O7LHW4Inh2JlKHtOlJ8ZigYz1EN5KBtuGa4nPmWSmxyPTUB1qsj0NvLxRnA1n2NIgXfnEDXvnYFv0/GiJsSwJ+mEKfh8j+/jhPtQHxl0YHq+tx5Q39nDoFKEn1FIA6aVKdnwLDjaA5eGOmtqV16Z7c7I2Haxu1Og0BQVyrZh7mFGoipQazjZLmqO6IGHx7F+5Usi13OAvVikRNHThtw9RQn2+OKWIdFWVefazYoIu3th5UmmQ/h50QK56UodiLG+apzf708ifhrS9JMR2ZPRhXk9YahzvrCjPdif3IsgpnykfDHaxijOHIECGyqrIOfMS0gqVWELRyp4mo7jFZQQdnZumX/3tQ579RFD3oOYMHBal8+OCrIuHPWytgLHMxxGz0oyjLVdoVCuj60aLQThpbFCcLiJpPuLgZAjd6cZdcJbuN9s7pWrxgah2mySDd/GhjnuYV0euDMII21PaYRKYSq1u0L66Hzde4bAkA993lmN5cSFHktEclItfI1lnyQiTeYf5fCHvoGHx+yKD3EN+30kcLvFGz1YowIL2Tk6HdnJ2BxZoFD8g2+IVvhBTVoXDXr3vEsqYefFKWCLqQWGiV9u8O2E0O087i0JLvirZw+0EH+YTzIUCsza3c3r0hGmdz6m+MZyiC4lsazBhBR8RC6KPfaXm+8eBP3T38dCBlCXTez1EnMJQXX9TGHVa77bEtdRMqJIsutXSTFTOCRe1+J43inwT5+KUkSf0MsmqQHspc3xUCflwjnhsQbrQ8YoJuobtKF/1bRh13UU6hbNjDpFO3c0843Oan9ZZjPJ4ogDF776ZoRPT25U6qKe8MQtSfET1QAhxfuPjMPIeZCnLHBmxjo2nDYhqacsw63sibfqaOtaPO5ee0HCbaISh6pQTN7RGpL12lUi1cWBBT+VLbMd4GQr9YkXSyUNcLKyp2+olHEV4p+fdQ78N9c7U2X4790abNSEAOaGVtrWlx9LuNGAtM8S4eGBj4oH48UUD1WHCeU3fnZCD5zaQfLdnS79lF7mQojUAfZE+Ybcu3M8wdoNHah8WTUcbu8kQifaUhOI20nstvrZ4ZWZIpAcLtuFbvu/OPqyOd1QSQvPqiMp4ueYerBYxOzjr0BAfkN7K6O1OaQm7wc8eqbIWH8ckxtfjXlCg6913xe04bSpmn5+6cVRsj747BAANLnp4Cd4iO8UgdpLweKA7AQvM/hSXdiPb+a0sSUijxb0Hz0yJ8M3+yBjO+WhasuesC5TXkuE8axzt+l0pPMRd3FcTXF/mS9w9dlI+7Y6drR/jQ7NXH15uKjo80S2wB0zzKE+o2Em+w+adsbC1RtQ8y0YzkZ9hx12L1s6K7Ayyp02+NvQHv0dUr3NwMrlNPk/RNSFrcAMy1jHPY9nudAf43AYGvmrlFDyusQl59izRkzCIhe7lQ5CY4kTJ6lEzj1XZnxB9c8G129nnuOjC50kbZ1Efn+Qm4KXzBNOG1cl4bW/xmXO3jdF1tGmbacPKOze4nzl/3dm8/TCtw2FrRXTYIklDjNTxkCRILXdXSYPPWGGTxYSO55vGiGkVDtd+IO3EdnxiK/VpX9iFXO6N2OtPiVwpvZjw+3booa2Du/C+xeXDmTlvOmU9oeKEX63Jckp6vRv6xt+L9zRMINRrLmWQJ7sLWl1MPDLL4tGw6QDGWIRPOI2WW/QiSTnPVjcSoY3+3oSYMNaGV0VHBpUHHrt7pjAeoYaURaPk8lgk3TLALWl/jqD2tGeqS3+8HUFBkaFmfliaVgSzk+02205wKp1F+6k/qVcrzFRyjTqFViIYm4OZTUNO9vqCcIwYdjclP6vTuEFb1OUt3aTP8TUFMTysj1zXC8cePqKixSL4dMb5Fm9lOiX1OD/oImcY2iOYMr5ubemRkKKWJKx0qKxxBnkzErMz3fk7lSknbFBLjKpdfd2oGV9p1b7phO4orfGS1dnRtSD+ZFCNRMWg6FG0lU1Kg813ZlasxGdPMRIRrCOaiRTTeBjJxXglXVQddE/uskgL9heKvq3lsoSpoQalLMh34XbdIZzy4CNgsVGUcZ9KkpuUB1B+cGrecnMJtEmQ62P13FXjWrqOvjsEZMtitrUros0uSyi3ck7doxepxJ28Ew2ALzmOvXKf7JusoDRVZIfx7uwKxt06Ad165gEdTauraZ08koIWbW9No1dHr1E7fzK6CPbzklbKWYRzrzyJhbbRgjuBw3rgoPJIaEe8qW6BSDCu1K51XTgxGZx3W0+gDnqxPtTecU+hUjOtp+E8qNt0zW63U6VTwxWMxZuqPvqoRmVnG5aQxGYGqSPv9KXJ1MdFuqlpn1nSdQfDW0iPoYvW3o61fAQA5KUBl28Qbl/szs7d2aYck6db72THWAYrhMuKfGVwiLFjW3Mru5AU4Q2IYDSAqX097Susu9U82gst5lDKMd0OMJEKYXigDZ5ot4Ve7o9bzjVCCtuomDrv1X0OR74OoBvawj2/3u/8gyms4Ry6RrO2Pslrs9h7vkfCMwH38LQpOK9oS2xSRoXwCAhFBCFcT/cMG+LRNzeEeKwjCJsjizvhYTkaZHXNFCfF5ONDGZQH4hTTDqnaCkpos1AezIZXDi0bZEbdp6C4HKhAaJPmwY0Ou2Yu8/6x2+wIVKPVSeCLiKYNdc9FJdXG18i2Ks3MLduyTSIlAucmtwomynsYFoQ2i6T1BOPw9njBnLXTDjemPh7W8jBaMXsgWmVz2Vkk7mx6DunXNOjwBHcvGfiGD3bomg2iK7qPOAqKdxWE+XRIBvGlkqtLQoJU7zNjOKdGYNAgbEYZnUpFaVyFkxsyhI72dCDP0m2g0/w8oRRpRZhxDo5aZ1ykWkJkuGL5GUQazt1Uvy0PRAirICNu+6Ya9zPHlqfGkdidfdmJ+CRe91JjnoqqgfpOG0+mFeAecfC8EYw32uyhtTewPApjs5yGAWtWZ/ZBChZO34P53BXOMOwNE3i5wbCdLccGj4na1uFSm4MvUCAgkLW5a2WSkmFBUfzpINxP3HGPy2OG3POA9XMyPMFZXdPa/Wbrak00IwtBjojDSpQXjHK4O/4gdwrrFX4CFdkRCvMTqWwkUS6Gy4yrl6kjY6ZrKPlK1759PBXoTjK2F8QYEisMVftQHGXZaDF2V9qzuc1uADAuxgExJh/gfR6einpHwridI5Y/0fWGvuv32Z4TZiBCA74ElGAmsog1+ZnQ/SA43+/sycmpnXfUVEjEsj5z8o3LRfzhuKcnDR054lhUFstyEVLcLny0QTDGfShh7iAOfr+R/haMz8gswRVC+ft4z9zkGaQuNqIwn9+PVLDeOnfkvMX0SBdZxbnMddBk9ow2TqrAiYDaAILWYeqf3H3ZJWcSSTZUhzDcldky52Q47OnRPWg+l69lXDpWtcxZux2pzeo1sDHueIW285D0G1s8ELS7j69b3ooH9IBQEjF4cjoRyj1L0HRPCic99DFm3g/eMIgnDlcC8w58EYsJ7pO+NqdXKJCa1Cea7ZW5dieaGET17K39Abflan/rpQa27QBF2rkA/W4tlvDJQ4NkgiYkI6E9bkoQ7m+clGwJttoqbCe2uCaHoJLOueEoHdFpTbGv8Y3z2OQUXMdbD7+bhzTwugwEKzo/bJm+z+dbQuXDIRmZoz8qYlWLaA1dPWuwDKfOEYNQPW723c0l3LVIsydmMNlmXBe03H7cpDfVicPKECfuQV2odeNNSscOeiK1G/xx7tVEEZNp6JqQRhiXfqwPNnNaQ/VJUsNbtmMjNYo2p+xcPs7KkS6t3MV0Ucq1TtLwWnaY0k9x39VF/KrZhD+zGyFxPN44YRNXx+H1Eply6g9GK6HlBhZ6m117tN+FnHpjOy++NdTp5qHE+sRuGNJoSS9JcEVjr2bPZdyO8pGgkuZO89oryrtMpLq1c20RpSDO8NSSU72DTsm43Zy2pgOjBEycUHQjXvW2gdH8Acyi1BnvHK69P8w8QxyuY16b7HqyZi5Qm+QwbDCD72fo6OFTmuR+ubE96t7FTX8UDFw4bfGcJ+RA3Hgtv98zsa0jl2m6EgJuqLxsFxVP4bK6Nf3M1xnOOJkp0t7U6kwF/fFY+BvVDHx/FqDaBYEWY8RNPU/FyARjxiWBew+Sm6iu9143UQMAJv3+QO/ulk+jKr7pB4I59jGdWgzSFMfNJgsOBDKXYCTmDy3OZm5/hV1Da3s4UzpP8aY1QjV7UQAFbHdmLg00I4RSK7yLaNtBMtfE6JNWPghyegdjj3RkmONNxdoHjuwiYp3kc9NbvXRM4b2Xos6tT2pIkrhe13gnJy0hHVPn5rsUFMpt3az9HWMXkh8eSOvs4lEMuqjjQdC4nYaDzB9IBdFK/Dw5NYxvgfbDNPUpHfv43tuE9jyMxc0J6kOgGboVBFYeYYyCc4/eb8BAfCE8hL7gzC3ad1GE1UY/H7Bkg9rEEHT4+rqBuYYxgnt/FCPigDHIcFd2a+1ItrzMIV7ZlUR3apjk1h4sROnXCFnXex3VH+iZdIPWUbxgfEBhDfAjtjjI6eTHXib80MWnehQJZWj73DJcbb3ZdIksDT4F2URL3I/ufd9h8oPdaPKDVrO5kKgiLHc0eaEQvGcUejswGphbGJqOQFt8uaXxvsaSGbexC1OIsaKg8vo60I7up7e4xHwuUs8VQ69bFs2IqeqV+HQriKQtoSHaoN4GPhFXP6z6OisQJb0SxAnnLkZXcvo0dj1wOdWl51SN+D7Qbbqy2lLb8tpx2GTjLVCG9bkdd7JCIic2Uc6wpwQak0PG3crZy1gQoYLUpGMxI3ai4qvf8a5XjDsOJ7nY3BsZQZMk+Ze3D2/Lc+v3p8//9mtxy5Ow/2cP3V7Pzr693PJ8dunb3ucnr8//vmh//fBWuzEQ7PWgscm68P1R3d89Zvz4r77TsFCZXm+efXvK/np439rh8pb2W1x4XdPW09emzJ6vuoAdTtcs73Q2y2u/Ljj+/mFs2UZ+DY6LOMtLpED25cUycMX2+sUI3vJkExjha1lkT43eX4MAiiCftp+Qt7/9bzcwHAJYLwAA -->
