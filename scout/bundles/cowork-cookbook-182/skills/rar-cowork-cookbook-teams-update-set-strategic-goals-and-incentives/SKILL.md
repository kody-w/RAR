---
name: "rar-cowork-cookbook-teams-update-set-strategic-goals-and-incentives"
description: "Summarizes the current state of strategic goals and incentives from Dynamics 365 ERP for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_set_strategic_goals_and_incentives", "rar_sha256": "c72764bc6445b57eb9bbcf4f279eed42f245d3d51e6b3df0256f3da03b48aa01", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_set_strategic_goals_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `teams_update_set_strategic_goals_and_incentives_agent.py` and in the RCI capsule.

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

Set strategic goals and incentives Teams Channel Update — Summarizes the current state of strategic goals and incentives from Dynamics 365 ERP for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives
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
    "card_filename": {
      "description": "Filename for the generated Adaptive Card JSON artifact.",
      "type": "string"
    },
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
    "scope": {
      "description": "Optional adjustment to the scope of the goals/incentives summary.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_set_strategic_goals_and_incentives_agent.py` and embedded as the fenced Python below (sha256 c72764bc6445b57e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_set_strategic_goals_and_incentives_agent.py` first:

```bash
python3 teams_update_set_strategic_goals_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_set_strategic_goals_and_incentives_agent.py   # or on stdin
python3 teams_update_set_strategic_goals_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set strategic goals and incentives Teams Channel Update — Summarizes the current state of strategic goals and incentives from Dynamics 365 ERP for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_set_strategic_goals_and_incentives',
    "version": '3.0.3',
    "display_name": 'Set strategic goals and incentives Teams Channel Update',
    "description": 'Summarizes the current state of strategic goals and incentives from Dynamics 365 ERP for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-set-strategic-goals-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '82beea4c94701f2c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/set-strategic-goals-and-incentives'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-set-strategic-goals-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'scope': 'Optional adjustment to the scope of the goals/incentives summary.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of set strategic goals and incentives. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-set-strategic-goals-and-incentives-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads set strategic goals and incentives, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of strategic goals and incentives from Dynamics 365 ERP for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON; nothing is posted.', 'example_request': "Draft a Teams update on strategic goals and incentives for USMF with an Adaptive Card — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'name': 'card_filename'}, {'description': 'Optional adjustment to the scope of the goals/incentives summary.', 'name': 'scope'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on strategic goals and incentives status from D365 F&SCM, with KPIs and quick-action buttons in an Adaptive Card.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateSetStrategicGoalsAndIncentives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSetStrategicGoalsAndIncentives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope': {'description': 'Optional adjustment to the scope of the goals/incentives summary.', 'type': 'string'}},
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
    print(TeamsUpdateSetStrategicGoalsAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8/SEzG/sVu4QrOmKQQICEFvYlXeFk33cQQjn13+ciyUtWZXVP9cynkcMWgnvPfp5zji+/vzlDH1ft26c3JXDKBefkeRIH7cIp/cW2Gqs2A19V5oK/C68q+zZxh75qu7cPb37QeW1S90lVztuHonDa5B50iz4OFt7QtkHZL7re6YNFFYKLFlxFibeIKifvHgyS0gNrkivYE7ZVsWCm0ikSr1tgJLFg5csirIAkizyInHwxr+ynD4s26Ie2TMoIPAEcM78ay4UaOEW38GKnLIN8UVddv6jzAXBZdM418Be079Qzo8XWaf3FXjmf/rIoqz6eySTdY0PgvwOlgptT1HnQvX369a8f3hJw/fbp9zcvdzpw6+3BRqt9oIkS9MpXlbhZI7r0hW/6AEq5U0ZgSz0B+5bgdx20QJ0C3PKDcPH69XMX5OGHxb//ezY6bdT98ulzuXh9Pr/Nf+ShfNizr5xZxIXn1I6b5MAS7ws6H52pexnkoStwTxm9P3d+p1TVi/+Yn/38ZPIeBf3Pn98qIIIzO+/z2y8LYOfPb+0wX7/PVOqff3nPqzFof/7lO51ucNPA62diQOr3L6/fL7Jg4felSbj4olzY7YtXG3hJHQDiP+g3f56iv8i9TPLlufjnqv6w+HPKsz7/AeR9BqAL6P45WWADsPPtPa2S8ucXj7a6BqUD/PTzL/+MrBcHXpYnXf9/RPfXJ+E4cHxgrZdJfvnwcN9fF9BLt280/znbGgTMv6IJWP6V3TdD/TPaD8/+Hek8KUHeffXln5L7sw3Qfyx+/ae6/WcbPizCz29MkIP0aB03Dz4tfn+EyK8/+d9v/vTXvwHS/yUZpRpa70HhS+GUSRh0/Zcvv/7UPW7/9NdffxpqEMUgWb8Mbf5nNP/Mrg8+f7Dga9XPf9wL+GtlVs6w8y2HFr9X9f9o//a+0J088b/f7z4tfszE+QMtZiW+Mn2a4Ids7ICsP9jxl7e/ARgqgTaD93gM8OPf/m1xTLy26qqwXyheNfQL4OA+KYJZeDUGgJY8UbgNgF27BBj2tQ7E/+zhWWKAyb/9T+8B8R+9F8Qv+xngvgwPhPvSBf2Xb7D95QHbXwBsf/kO27+9L1TApmqTKCkBRsv05fK5dKIZ+WdYbYMuaGf8dac++Aiy++N8AXB/8du/yOnLg+h7Pf32qhwP/eStMCNiN+TB+6y7EQflS1MPVLPgFngD4JdXHhAuTACuz/Wjq3JQCfrZTl2W5PnCTwDmgKo2PWgDW36aif3222+u08WfyyeEY4tnueuWYME3cRYfPwItwzyJ4v5zGXhxtfjp97/9tPhfi/9s14P4zOMC6srLU0DCuS4tQOYNBVgGnAjcDmDl4anf//ayNSBTgvoM/JqEyavYgsjNAv+r4RWe/ogS5MINgMGBsYu6avtHoevfF0K4+CYvYDo/mitHPFdMP6iD0g9KbwJUHaDON0uCUgkKaZ90ISjAQxc8uP7mts5DxAJAgNP/tjhuL6BOVTn4Zxbz2Qc4ZVUmwPzfwuJ5HxBpf+oWm68k3henOVYXtdM6ddw6Lx6h8/TL3Ae8tgPizqIMxs/lXJ2D2VSPxHmaBywClvFeLv04+xz0LaA1Kf3uK+/HGmeupuqjqrafy+6VFE47u8IDRQIwjYbEn0vFX14h1cXVkPsP+wFJZ0ovL/gvrzxiEDQG/1Wz8+xWtq9u5dlPLD4PKIzgi/8f+qjZDDTHySxHqyyzYE+qbD3dM7eQszrPrhPI8RDtkYrfO5uv6PUVxD+XeQJirZ3+8lz5cOprzRMYhxbIJtPygz6IKOCeme4j4OcAbts5VZzP5ddq8QFo9IBG4HOADiB75qD9ynB++lXSGEDA/Pt75/AIEKA9sDwI6kU9uDnwRhgEvut4GZCqnZP25U4Q/Q+3jXHixX/QanYECDJAfwGESEAaAge8f0Pw59Ovov9h47NBmrc8mscB5Gz7IADkCGYB55gYkx5Al9M/O3ag56cHEaBGUfez7i7IGqDp82bQBs2QdEk/I+TTrkENwPrj/P3UdL4b3GqQKMBYIB3qAVj3kUCz8wvQ/gAZAIaAfCqSErQDwCgvIzwIOsWMBgBtX/3qk+Lj9kuh4JF1cx37unFWZN4ztwbP0HbK6UfQUP8sTAC9Yl7x4Pv3kfaN20x7Bs4OgB/g+PXps4d4f7YBzz5j8ZXup38YiX7+16amR2HX/hgAnxZx39fdp+XyWYy/1uJ3AFvLp6zdsy5/fFbLj6BafvwGAx8fMPARcP74HQb+wOZpgU+Lf03UP5B4pcqnBfIOv8PzI/EVaq8PsMz248b6iM9PP5dy8B1jAfuqALE2+3ECjcC3gvh1CaiKUQugCSx+FshurqsjKOWPigCc8rn8Mfbn3JsRKppjtat+wIQHFoI8ePrwW+ECj8oe8PbnLjMK5jHvkSld8PapHPL8wxuAy+BfHO/mQlXMwd7NAyJIK9DA9Unw+AWy1v8yS/Sk+/vfjcq715NvMffdWP+Ir6Ak9clcBmex+6me5XzOeXNn+ECpW/+PPM6PCyd/XzABQMS8+zH0X4VsLuQ/ZOjTtMCkHtDlw2K2QjcXXqDIrOac3U4H0gVI/aeyPMrLl2d5+UeBmLkW/ViBZsBtBpDxHxbBe/S+0JTj7k/pfmuN/5GoAfqOmY5ffZpL8IcXvIFvMM58WHybTIA2r1nxMeOXAxjDf52notmRjy3zBdgDvr5t+vZfHG7w9tc/kethp39u+YXjp0PXz/3JLOIDW+YdczV4OH2OquUPpbt7VP7pT2wAmD3wGVS5We7vBvkuVvWY3GaxgBr98z8afn8DAeoAPzqvEH21/mA5gLOP3dzULEFGA4bg9zP3wLP/26HgRa6LHdCFAnreCl2RuOuROE64xCpwKdf1QjxEVxSomTgaojjhYz6BBKSL+SEMdoWY78CYi68dB0YAvWdCf5kbuWQWcZYPWOYjwITg+2Nwy3/p9tRlNty3GWS2wUvF399cEgcrebwT6Odnu6QQd4mJ7rTnoRJe32JE2dnsYWsO1LCqyHOLOIa79++d7+eBGiC1y0SCSmf2qG0N+hYVOlcfIkjerycVO3kUfaNpSStQd3lKTfOw33A2GVzbErnD6X155AiykuouzivfInfnXrtlrrDfCORW1xXyEh4S0T+4FYxjXpRpLo+LVTcalzvVYmuVgHT0gF2oHT7Wp6xhbZtImS6VI15GdhSil8VqhyqkbNxgZx2Y12tsX7DVaDR3ydQ6uRGN00bAr758VprD5cTu0WE9Wo2pmY1+Fu3tDehaZPvMs3I93vNXXZHPQl3K0rDXiJrHx2WBtTdyv9/CqMxabtnQSXin8SBcre/+pdyjUFhWRdlSJAR5rOmi2d3RRckuZNs9CZ7JbNJCgHNbccxzY5foQK7v4kbvmLNAqQcTCkiZd1OlcxrOYmnbiv1odcT23GRdfWc/7ZtONFdjJTHp5SRJ6QYZbHKvTTdJWQUONVXUib1xOZ74+c5IKN6dOuhE7TuSH4waonQh2eXKFjl25kkILaYk1AMn5PZB1jrbrIRSE2Ir1QqnE5vhlLZef7GZbRdj8m6gaR2LEETbZi6aY36O7Tyod/TYtvGqaPgIYQ1NaeypjEZ91+7Z3DznyZHY7LKgzw1jy3iktVm2vi3ZfTBl+zRZOvHU65dadUiNcxPiUEykKWC1D61ls6kuhdTEO3tnABZbh4NUR6uV884F3fVSyA+7qfVI2Iy89UDaxem2xe+Hc+kYthRimqsZm8qGaYlyp8RcOyIRSsfTcFN5N1EkUo8arj853KBbjJFH7pjl6KrJvQRud2exwqx6BxrC4qoco7Vub5fs2VxrO98gzix6ha+jcqVEcR+SIuwWSmJG5+VV4qIkOGDKLjsld/zE+Cl8mYY25Ah0I+/swbkbXqRK9/DCUJf+zuwbO9IIXFSzgKGRpk6NZUrkIUElOKiJGDG06Am73DzvhjZqdOWE4XqlQ4hejkS1PPencamcdRgaFJ7UffxsJikSNdC+y+COV8jYKGSotJNBPhZ3XjeKXYbs90zrW6sxWvP49uycSgiLeD45yVpmR6QTZ3gvs7tGte0GxsPMWxUMrJfGmI9qLN+StRJVHa+xFSRXDSVvuQ28kyBzlJIjGASzrbtmJzzyENyD+PwIIP1+xI/npVVQKZLUa9HFVd9Q/dNBRSws8vUTfYLZ3sC3SAbTRHWg3Mo5l/WxycJR8a7oFMREna31aYeobWiIRnPMamBgDNmu4xSR3Y6wezuUbn2OnUQQHdbF3WlbX04s7ErXF47fQDx733l5ZO9HIqItVWRdrC6EyaacpPGv2ZE9ZBLNCBUcXRoryvCKPtTCcOfhUMJuQ6Ql+7VFW9FNKyPYTBtIOu2Z4kzVtgWvThQM5bUwWrtde1vFbNUXxnZPaTQzbIljtTtg/ZHbrbTepltCkApZDhKCGlEbKsaaMSad8Ym7hK1zsw/3dzm8mmdLFCLMPFCrDQFtmcB2mGF9gjdbirox+DHFVLZvmN3kKHITnqjqSB/gqfTE1cg6Tp4q2Mkm0ySxN2ke5CZ+z6726HFrSq/bDaZJY3jGAicrIMxHwwOdHsjEIEb8ckP0M3LnwrLe5Xx/oQ10j3mIkJdrhiXstggNmV6ROnIah7BgCFJHr+xhjTN3jTuerEk399oh6HGVcTElNKstSPVdhh54xIjxa1wlfAvdULfZmqutDyOXG0EHG9lTBZDIA76CMvy4k+S7Et37aJswclJhVwJvkKvk8IyWVdsYyW6MhTDy/jhst2Jkwad4szQ19JxHhh2EO2abnfajOLkIa6b1ka55zu0RvrtIWVLrPu3vHCsM3Fzc24IZIM4yC6zMyrkmhtAdQ3HNYCqIQ0hK7A1whJ9R1L5xo12vOxt3RJtHIO9SIsiyVrfaAZf01EzwYaU2PADyzVLZn+BAO0c3xU6icmemS3l9sobdaRxXTmZZR7JdB2JtKCZuLpe+vrxc44RSN7A/aEVgmh2I8nDbWtGGqQ7AOKuBzzga8TR3qTe1d5zkevL40S0LYY/Z9noz7BtRH5k2EI/9QS2ciImvGXtJjKJz9CicDpJI5PSBuMuKdhKEdawc+JxTGoZhezjJy4TVU+5gJFjO3bdsVKkVtzTVpjF5DxtwLxSRZGlz8ibXFa4M6DtGr2s/LgljuoiIR4aTAYBkXFkQlAp0I3BjqpjniqgnKmTYSy328OWsoYIQKIjNNh7a4Lq+ii/MLm3Gghx0j2epfLsr9VwQThstkmFjIysn1F6F7YqzEjfh4iQwQrztK5Hd5I6AASVgqdtWp3S9ypsm7pa67/XadrtRFPJkoroF4MigOeGmnn0JomPmJHPJnjogrK8xGixw93yabmKcHmjnpm5TInVNfPAbYezpjhQOZ7Q/YdF+S0S1NAUXMzpek9iK88KSXHlcDpkiUjYwVJri1wl0W1buxE2d4cyNpVl70/HBtVk1/YkrT1mEnFJaC/b0bbkBDZV/zZVJOG2x+sSc8oFBVZaeNheqMKqCmwTNzZe3NlB3TUDmtSNWDSf4xnVXGVvt6jO0xbB77G7uOhyND2lkBixW2LVZRSV1TtgyumsxQsfp6nas7nujpcTEsNpqyagXTTve9s4gLC2Z4N0x6WVhk4kEZ6rcRKhpnFilJbSFLFkYZkFZyIS7eiNUElSaeFc3Au3rvHusHJXQLSpBlcRPTDNJ0GubHysKg53O2jLDfcS4lbubwm1tCwJxaLfQGh8kAhvkyq/1JIh2+2kJwIXE/TLGBkGOzCUPMfJJEwoEgemCL4FesN3DXaLjzGZfX/RjpDCI0mwuPGS0Vu2g7caTa2VnVauGrnO13zE2Ea43nsZpWM4AhJdN09w3fHIXjZ7mMV+56HdqyO/uKSwJCNoxh2zLweqF99RjGVnVdq2rTHYshwRJQHk9O9eDcOtuHa9PaJVyIXqVabROPU4sqMD2ZNIeZHrTadtkY3u6NvriOpNzJlhurauD7zUAZSLhN3iP2Fxtu8dSMRvOM5r1PYD9/spihhER7gWXj8Pg7zV2v1lH56pSINLkyn1OWcsyFfd03TRJTEgsepKGK1kpyU2zBVK+SZ6Rr3LRvm83d9AMudaeHujisCuFEaW8G9W2wZ1YJiMda5O4lA6FxdrelDANfxdl1ziG5q4YjeHeSxKtk3tScsj2jEDoiRZGRuRWibM9bv3rRdHiUWWP/RHNBkbldwrGUitVsFovRJHtNDXqcj8ZdJKLS/RmhqVILG/qjown5TCuraXQJfKq6CSnZvjMbG9LpTfuco1cBxYd11PW6yXBVK2U94h+aKC4KHwvX2OdnY8kKSGXkSe92r5fNSbV3NpqYnKMM49TQb4dOousyMFH+KI9VkUlSLVSVpHWb3PRi33TKViu1+JYEppTePDo43bPCuMARjUUt4Z4j7LntSvtLOvSXkyKJdH1VITs2GB2yqFLzT6MS2Z903tYLmV7dcEv0DU9ZoayR+CLfFtDisOtdv04yWLJRClcUrKM1Cf/7qDhud5K4iA0ynkvZSR8DDhtxaUmgkiOLqOlZ+gaM+7OjSsIumG615Nj0ix+g/e8RV604nZdbi+bQ7qXjVPo8JG1vqKkd+QZbI2FIYNQ552prfa5AVGSJ0bJEK6u5M33THnP3kQrReNk7UD7qEzslZ1JBzAvbc83K/VKuQJ9f99WSl+oRWif5F7Rk1qi0tLQWgk+NltbW6/ofdkzfdwK0FFfChbp9qBM8vcUgBarbthEh6Ab3XbibkV1njgdjjfK1benFX0QfTvGWca/IOfcWV8SdFTWnTekYZZD464dC6s/TZfuVK2gtRnKw7rj9loy2rgYs0lAWRaxYuWrTpiuG212l01Y1MddttP5K1D/NMAg/KMxpr0SupC3+HwPEtQ5tASuSDS8JQ+csRzXgmBevdEcqqS7cA46omYeqq6En9IRgu9RUlXVvdr08PXMSNvcdpTC0R2H9EMGSo1d5bB9cu6G9YU24dEotC2JGc64TarpoAeOr9nZTistmSTzLCj9fuvdVIQXb1XTHaeBle2zvwZtg2p5qFiyEWhxIjIKYNvAe5TgsSWyQzb5zp0IqoGlpXA/shMix51JKdgEhUnc2bfdXg2ziGZuh4FEDKhytXHtj0IZlBSYisNA2RtsLfCo7Z3zikZUMQvI3rn5YwswbzJPia6tb5CZrmtLNTsJa9PMuQpKwOtxdr2HfoWEWXMjCDDuRQgR7nnhUEV5NpS6NCjnddCLXTScrWgL706gB+9rpF5TfVqbN7PIr0GQXffHLMi51m2l64DA/crMAjA9HMJcNG9n0jLOt8smbf2dDaxYDiKVOTKW3KV46RdeGuF6dwr7qV2TmQJImkrYw8SWmwIjB+PbRJJHpC/DGt2nZugH+niHnYJyZHREzlCdHSwGrlVkpcFn+cZ4Op/Hd8I7H8jl8j7Fhh4aKONtzsN2eQZ6TyXZWyTEFdqKouRcrAQdNyce1Zaw5O82WxFOC//M3lHiVlVa4iRi3dxAUzOh6OTkp/4iuv7KOEwNvF+XDSaZ13Nxk0vvzF13tj2ht7bPMLtfdaYbsusTb7m4xpGk3vc3/GLul/cVtlwdMBDVnWZzVkpBxfIGjwkr1spqNZh57t3NOmalSeuuiLVS8GN8t8YddREsiDqyaBtm6qFPJRKT1oMC0RKA2lS53XjATGCyglge1p22JO+smyKpQnXppdxMDQqdDhBvSkGfiOtNRm+2rbny6hErzhdNtu72CbrX2ACp+u7upoVV3iZkmNjtxJ3N7RJLfV/3g5NV3LFA4MSOUd26Og56jKinPZ4rl9MltszkvqqHO9m65p4AzaNpMmq3Nk4yCcWS1yqQmrXIGmp5tzubnA6vOZadBNac8DOLYW3Unu8DJCjO4cKhPSVFbd3g6mRVVEc5CLwUE+0Qo+ZB28roUkIF3Ed98mIGBmYcrZS+Q0gHhQHdm+7Nq1Q8rlZWotVazeadHHlFSDrqlUyOuRfBzJkjg8w1kVG1eBnuVfRgD42A2GMlr4HDdl7SC9mVi6+ceo2CfG+yXQB7m44MEHE1mfFJ80gpWK7y9frMxBK1xFYSmO3hwZdFiy8RfcWOI3yViQR0an0hXAhexg1TP8XLujvrgVGIVX3HJ2idEZuzf02gOoVp55wOUnJn/SDNeMb27sIK3lVDofk2Zo24ZN1W2+upESYEsQ15ckiS7jPoalw5VsVznuVc7MrwNHa8bgZsszN0nMdifOsnyvXq82smX1MZ0ZocVXitdVy16ubapzcweFmYGqeuGFB8p8Kqqw3SiDDpEsc2MKyKMFQYl0L3NglX7YZ8vXIhMNNmDEReIIssZI29FZcN5uFTw1VmosjQsG2Y1XV7CsZN3aJLA1dOPHxrsTHwQbFyKDA6l3rorzeSD62YC0P66DkMK6m6FUSHbXpjGEqn3I8J0l8Lub5DVXDU7JZcoZCoqMO1Cts2jUSyNeXQQJr0kvtBPqYwMpF1Aqb2ErscJdOIDkHtycGWI3w0ILHmyImad0Bu1KGs94dVifAXZdjy/uCf1jvW1/MJhy5dbm4P8kGLtYSEc+VqAHNhXCupdAORhe0HkHi4rBBPYNVui8hpl2H1lCqXmoWYo0jERlBrwriMYokkr2M37uhUvjdpv8aI884mSmsofGgrCFB56fwIz65QhvGKOx1w9OCvhgjVh2olrFjylhyvVNNCwkDGq66yO3qlGcvBjVJWP5yYPvejG9UYV5dFjyfYZgPiPEJaWN6wHqMgeyX3tknqGlaPcGmjOWqFDhglFbHA9EpduS2q41f9BK9cJRW5dUcd0FQ3kHu9VmtCMUa1xebRMjTzzm6QjWof7XTZGZvIxaBscr2gIkwcz7wVwrhGlrTXs7h02HLbnDlVWG2x0UVd6RIu6bRayYYoLJGanltXla0Ddq1h1pTayYiYe8Yd+u0UXekjlpbZSSDuBcHzbXBbN9jJwBy0DEjxCBruHWuaR2IZG+IIET4OUVZwXNbrqVn1tJzpecIoGypjyohFLC5VzpthGSzXV4KtRxPOkR7eQrijbwknHiseRfEBUfPLUKJEbvqJGKPaGFzEoC2Hxld6harVCusqKjJ91yJSJx2m0uDjuGZjB0rEyjwjZ5Oq/R42cjm4QRa/d3o0zfsAmjB2OQaUwOaDtYka9Sz3PgG7wsVAhzuxivTOT2EGVjZtmVuSlIxmy8sneg25iE/zTIUMzE7wiwJzJ3RzP6epQDUQkxQj5eNuWrZDjlwlZs2d6wp0ZTW/NncbysL1SwMl1xrDp/TqYqvW1gnsBKE5Rh4o5M5Dpogtr+mVailufRp4RK/4cFNh/P0S8aoqE4izArkDRqSGI5wE6mAIX3vDtQ9uaetc8CDs3d25I2qE7tcXKnZXuTucHKy7H9fntXQFk9Rh9PnyRK/A1HO2NvGqnEZShEflFhDtoJ51HjooqScBXTbp6LVsrNBDrV/wu7rRM1orQY82CUv1cK+ogfdlBL9hop4KI89722XubQpgtcjSeH9cHmRQxjysw9jrwG1xsjqFYcEh/AB6qraEbnwskym3HDgzIG8uDKdToBtT5LfhjqTuB1w0zGC/Fnq30aXdne8ZLhWrgE+6A0mYyxWF4PGFxgT+PohwvGqlHYooe5iP8qO9jJiEXELoptOXuwRr9zfKvoPyvqSJHXmqphiMUPTbh7fvp5xv/903uuYDnP9nZ0XPI5+vr2o8TvlAA/vpwevTf1vCv354a70EyPc8LevyIXodNP3dWdnHf/GgfiY2PV+h+nqS+zyR7p1ofgf5LSn9AZCYvnRV/niNA+xwh25+VbGb32b1wPePh5g/qji7p2oDz+n6L3315XW+mZTzGxqBnzxXzD+j13Hihzf/9ebQF4wkvgRtPWv+OvwHCmPv8Dv29rf/DdMcTJw1LgAA -->
