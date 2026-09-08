---
name: "rar-cowork-cookbook-teams-update-configure-and-manage-microsoft-teams-integrations"
description: "Drafts a Teams channel post (markdown summary plus 3 bullets) and a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons on Teams integration status, using the D365 ERP plugin for a legal entit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations", "rar_sha256": "e2e5dc5f82fd832f1385e05c43c5e66cea5460b9e7083daa3880e9e99c644f18", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations`. The original RAPP
agent is preserved byte-for-byte in `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` and in the RCI capsule.

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

Configure and manage Microsoft Teams integrations Teams Channel Update — Drafts a Teams channel post (markdown summary plus 3 bullets) and a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons on Teams integration status, using the D365 ERP plugin for a legal entit

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-manage-microsoft-teams-integrations
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
      "description": "Filename for the Adaptive Card JSON artifact, including date.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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
    "quick_actions": {
      "description": "Buttons to include on the card, e.g. 'View detail', 'Open in D365'.",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the update, e.g. configure and manage Microsoft Teams integrations.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` and embedded as the fenced Python below (sha256 e2e5dc5f82fd832f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` first:

```bash
python3 teams_update_configure_and_manage_microsoft_teams_integrations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_configure_and_manage_microsoft_teams_integrations_agent.py   # or on stdin
python3 teams_update_configure_and_manage_microsoft_teams_integrations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage Microsoft Teams integrations Teams Channel Update — Drafts a Teams channel post (markdown summary plus 3 bullets) and a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons on Teams integration status, using the D365 ERP plugin for a legal entit

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-manage-microsoft-teams-integrations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations',
    "version": '3.0.3',
    "display_name": 'Configure and manage Microsoft Teams integrations Teams Channel Update',
    "description": 'Drafts a Teams channel post (markdown summary plus 3 bullets) and a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons on Teams integration status, using the D365 ERP plugin for a legal entit',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-configure-and-manage-microsoft-teams-integrations',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-configure-and-manage-microsoft-teams-integrations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '53e3fcb6294cb5c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-microsoft-teams-integrations'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-configure-and-manage-microsoft-teams-integrations', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON artifact, including date.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'quick_actions': "Buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'topic': 'Subject of the update, e.g. configure and manage Microsoft Teams integrations.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of configure and manage Microsoft Teams integrations. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-configure-and-manage-microsoft-teams-integrations-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage Microsoft Teams integrations, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Drafts a Teams channel post (markdown summary plus 3 bullets) and a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons on Teams integration status, using the D365 ERP plugin for a legal entit', 'example_request': "Draft a Teams channel post and Adaptive Card on Teams integration status for USMF from D365 — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the update, e.g. configure and manage Microsoft Teams integrations.', 'name': 'topic'}, {'description': 'Filename for the Adaptive Card JSON artifact, including date.', 'name': 'card_filename'}, {'description': "Buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card about Microsoft Teams integration status sourced from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConfigureAndManageMicrosoftTeamsIntegrations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConfigureAndManageMicrosoftTeamsIntegrations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON artifact, including date.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}, 'topic': {'description': 'Subject of the update, e.g. configure and manage Microsoft Teams integrations.', 'type': 'string'}},
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
    print(TeamsUpdateConfigureAndManageMicrosoftTeamsIntegrations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8/SEzW7bZBXJHRwxik4TELkCUK5zs+yIWIciu/z4X6bXTVZXVMxVdn0YOv2K595xzz/I85wp+e3OHPqnbt89veuhWK8EtijQJ25VbBSumHus2B1917oH/K7+u+jb1hr5uu7cPb0HY+W3a9Gldgels60Z9t3JXRuiW3cpP3KoKi1VTd/3q59Jt86Aeq1U3lOB4WjXF0K2wlTcURdh3vzzVuavOvYfBig5cIPQerhi3DVZHXZZWY9onK1E5dB9WXe/2YG5aBanvLpZ8eE6+Damff3T9xRogtu/rqluBw5c1adWHces+b74EfFgNXVrFqz4JVyy2IVacpixWxWm1imqw/lURxm6xCqs+7cFiw4dbNkXYvX3+058/vKXg+O3zb29+4Xbg0ttTy6UJ3D5k6ipK46EN6So4u5Ubh+fUb+uujvrnqMPvpixOLNwqBgKaCUShAudN2AL1JbgUhNHq/eznLiyiD6t///d8dNu4++Xzl2r1/vnytvzThuq5kr52ux640Hcb10uLtJ8+rehidKdu1Yb90FZLgDoQxCr+9Jr5u6S6Wf3ncu/nl5JPcdj//OWtBiY8jf3y9ssK+OXLWzssx58WKc3Pv3wq6jFsf/7ldznd4GWh3y/CgNWfvr6fv4sFA38fmkarr7rCMe+62tBPmxAI/2F9y+dl+ru4d5d8fQ3+uW4+rP5Y8rKe/wT2vtLUA3L/WCzwAZj59imr0+rndx1tfQ8rt/LDn3/5R2L9JPTzIu36/ye5f3oJTkI3AN56d8kvH57h+/Nq/b627zL/sdoGJMw/sxIw/Ju67476R7Kfkf0b0UVahd33WP6huD+asP7P1Z/+4dr+uwkfVtGXNzYsQP23rleEn1e/PVPkTz8Fv1/86c9/AaL/r2L0emj9p4SvpVulUdj1X7/+6afuefmnP//pp6EBWQyK8uvQFn8k84/8+tTzVx58H/XzX88F+i9VXi2g972GVr/Vzf9q//JpZbpFGvx+vfu8+rESl896tSzim9KXC36oxg7Y+oMff3n7CwClCqxm8F/I8vnt3/5t9R15VrpfD/0KBLhPy3Ax3khSAIvdEzXaEPi1S4Fj38eB/F8ivFhcR6tf/7f/JIKP/jsRQP0CZF+HJ9599b8B3leAw4ujAeR9Lb9p/voa+wMAd79+WhlAa92mAGwBxGq0onxZZlX9YlHThl3YLkTgTX34ERT7x+UAYPjq1/+Z4q9PHZ+a6dcnZaQvzNSYw4KX3VCEnxbPWElYvfvBB4wYPkJ/AOqL2ge2RinggA/AY11dAIbqFy92eVoUqyAFiAT4aHrKBp7+vAj79ddfPbdLvlQvgMdWL8rsIDDguzmrjx/BoqMijZP+SxX6Sb366be//LT6r9V/N+spfNGhAA56jyOw8MmXoC6HEgxbmA8Qghs84/jbX95dD8RUgONB1NMoDV+TQV7nYfAtDvqe/ogSm5UXAv8D35dN3fYLX6b9p9UhWn23Fyhdbi28kixUH4RNWAVh5U9AqguW892TVd0Dgu/TLpoW8g2fWn/1WvdpYgkAwu1/XZ0ZBbBYXYA/i5nPQWByXQG2L75nyes6ENL+1K1230R8WklLJq8at3WbpHXfdUTuKy4Lq79PB8LdVRWOX6qFycPFVc8UebkHDAKe8d9D+nGJOeh9QONSBd033c8x7sK1xpNz2y9V914ybruEwgcUApTGQxosRPIf7ynVJfVQBE//AUsXSe9RCN6j8szB703EM5leqf1DNf9dU9O9X2Leu65XK7L6MqAwgq/+f27NFm/RgqBxAm1w7IqTDO36iuLSrS7RfjW4oBV6Tn5W7O/t0TcI/MYEX6oiBSnZTv/xGvmM/fuYF7qCoAQAsrSnfJB4IIqL3GddLHnetktFuV+qb5QDnLB64itYIAARUGRLbn9TuNz9ZmkCkGI5/739eOYR8DRwI8j9VTN4BcjLKAwDz/VzYFW71PZ7mEGRhEudj0nqJ3+1qsVVILJA/uL3FOQCCPin7zTwuvvN9L+a+OqylinPDnQApd0+BQA7wsXAJcBLCgDz+tfmAKzz81MIWEbZ9MvaPRBesNLXxbANQUZ0ab8A6cuvYQMg/uPy/VrpcjV8NKCegLNA1TQD8O6zzpa8KEEPBWwAUAPKrkwr0FMAp7w74SnQLRfQAKD83vS+JD4vvy8ofBbnQobfJi4LWeYs/cUqAqaDK9OP2GL8UZoAeeUy4qn3bzPtu7ZF9oKvHcBIoPHb3Vcj8unVS7yaldU3uZ//bvf18z+3QXt2B5e/ToDPq6Tvm+4zBL0Y/RuhfwLoBr1s7V7k/vHFsR+/c+xHoO/jC4g+fufYj6+xPwLRX2l9OeTz6p+z/K9EvFfO5xXyCf4EL7dO75n3/gGOYj7urh/x5e6XSgt/R2agvi6BWUtYJ9BNfKfRb0MAl8YtwBIw+EWr3cLGI2gAnjwCYvSl+rEUllJc0DNeUrerf4CIZz8ByuIV0u90B25VPdAdLJ1rHH5aNnyL+V349rkCAPvhrQJJ+T/aQC5kVy6V0C0bUlBzoEXs0/B5Bko6+LrY99Ly299s2fn3O98T8g/g3QXCFgL9AIDaL4ZgKcDFymUp/dQstr/2k0sH+gSyR//3muTngVt8WrEhAM2i+7E63ilxaQl+KOKXu4GbfbCiD0+d3ULhYDnLYhcAcDtQUcD2P7TlyRFfnxwx/b1BT175gUamBZNfDJjOQF34Kf60uuhn/g9lf2/D/16wBbqYRVZQf14I/cM7CoJvsHX6sPq+CwIret+XLhrCagBb/j8tO7AlpM8pywGYA76+T/r+o4sXvv35D+x6Mu1X99sW4G9t271zLzDvFcxwoYNXh7W4+rnon8w0HBdsBWH66cPqJxn0c0vTs3jspz/0Rl83qf/32vT33wEAI70oZQnhuxL/n+1v/kAx0PxkEsDHi+t+j8nvnqmfFiw2Ak/2r99VfnsD1eICW9z3ennf6YDhAHg/dkuXBgGwAQrB+QsWwL1/8R7oXXqXuKDLBuJDNCQCn4goNAooDI0QjCJCmPBxzCfCzcYPXQLfwN42JGEKC1wXoyg43Ibbrb/B8QihgLwX9HxdGtV0sZjYkhG83aIRjqBwEIQRigcBtaE2PkGisLv1XMIjtq73+9QcdG7vbngte/Hx9+3Y4q53b/z25m1wMHKPdwf69WGgLeJBFulNJxuyYerhXHnRTS83w7iebNkq0bMm822JTarzCOqBF2c681PtYTi8z5bFHplZNVnHxjavBpIYnai+6aRueNkI+xZzrOZmJCpyOzvDiM8DnadmlIA+8ZLvubjPRMudzDDBNtZG0M0UCkSvvRxwZOrPRLnX3bmvCVnKhDPIbshQZUeEZOkePcKqNOfCymNybP0Mzo3q2uomerFU+2wyPNJTWJ3DYqvhx6PD82LhZ1hBiJ5OmQce57sYZqe1KR9556CQFXnqMDxtz9L6CGEkqXMbfi61iDN37OacU5Mino7KI0yiWTCVijt2VSHP8inDkmsXX/M62KV3zSM0/G5oCA7xKRbcU7dHhENv5rXg6CJSHHndT6AipuTZ87br7VrxnDVYB95Zz9PgbJKGohrwAZkP157KUS25D3Kz1j0OKi+3AuW5GWIkMy30yopiJ2H4aRynUDgIbXc8FJfzWCu7+cacVZLYbK/QYcp4W3DOis+724k7b6YLt1fpTdzaTBmoI5teSsuVEr+AYrMk4BLZn+B+HTwOd3d/dx3HvxWZcE9Eh0qkg6AffHxfPjLuGLVHVSx6EaK5dcyddht80qxDUR5vMFZ7SEseNH5Xb3YSFRMJjTCw/EipZos6wWQrrVVc5ctoGiarMcPtQBP2IzgxccqaujgV64NyppgNb3h7VpbOLCR1SAPD95rnO5hFrPJKXzfz0QqtfXkLTq1vhDnmEVx4q9cNVZ0Pol5N/WGnYlOgE6h6sh65qkxHdfBv6FWb085fkw56nBgcO4n0qYJ5odttTWN4XPikujLsrlQOCtHc+QczTsOYMT5JGROrd3sVaRIVmRrahTs2PJeDbV5aLszrjFnDKKNdW3tq8+k085Z6f+wKiGdsczCSY9ucOrpd6+lkr9Ot4OTtHufvEy+MaSju3X0ulSMu88V1y1L3G/YYgiwPXdAAE5XCYTA5Q5ZB+uN4K31iHaxhnI0fW78fz5Q5XR7SAHqjCeNmCRVc3NWJW8Jy9nYtk7rPbSZzpmAbi5WO8RSkP3UQFTdHpaEe68pe7wv8iLgimYZH7r6Du9zaHzk0QEWC27bKmBl2h4mH4zZqWYVjYojT8J4fhlq+4+zFOgbwuawcZZ/7Oz9HhVsjCQeR7XOauhr+kcKz7JgAjpLPkU77x7SvXWGvGvc4DM2Dz84PXnoo7k6SpTYaD7o/2PRUuo7hlKGwNzqDmjfCIzz11G7IeqtspNv5Nm8y8YYYRazbCjhtTdlyugtisjpCiKjm4tqeg8SE2tfqJgsNWSQi6Hwrq/q2OevDLN7XTm4KpLOmlX5b4eHFJxXCbLLtPVexXTjODlrleMqSezpN8nuqC1V/CLzNmsMUQ0oLA0aMOqSms8zrjrkJQ64SjZy7uyLkmLGZ4OQ9kDFYCjJmD0t+KA1oc9rBw2kvq01RV+h1gyJoUAA80f3bYCd4w8dHZj5ZB0pUg1EE2LgtNEr3et88uLpY6i7K+et6iGRprRbdxr7U1tZHSJ6NpntolpXOa9uOvVsMx2+8CGfIsUJniZawNZ5L7H3DYRoke4eiV69345IqlYNZ51FtDdGY7fu4a4SLKxDt4VDjdHekMsYMCXe3jq607Erjo89u8kGpWkhhMqvBiOphJ/FV9Sw/amOorTy1iDEkY6Yppa/hpJ4k3TUphcbYpiqj4tFs9ACSYSc66iR6kqZDdCSy8nC+wmiXAvrgtiReCAPdkj2dqGrp7NxkbdUE5yE7Zgc1yG6n2+cYtYLqkFXKWHeH3NkcUFQtNONkKMlNZWqDhMb8epQoKLxtXYqpHtZDpAfKuakoopkb49THaSxajhEHgaklvYeU3nqnj+JA20ezmJSGM/l7TzdHPtiOFXWg8dQxHbrmoyuku4l0rE52aOJtLR8udS0U2a6zzgf3BtCrjxnJPZXoaB9RuBVV1DiKRaYwNnmG7nNDUKHX7VSrMRj+ntBpMMDrbIp5I8rn1Dn1+9oPmKvDT2ZNYNFWPBSsL8lotj8YYv3AoUtNWBCktEmEYcXpAZHZBgnQSyHzAUEQXeif1CThTmIR0vxgd81BxFsBt2pznVucyLYRu4U1hDecZgwHYjhIwBEUqnmHa5wij33JVlwRa2J9phCZW+slHzrSWRS3uKUeeTbNFeRS5GUaGec674Ty3DgaHMplRyHGwKCSbOaFJm+CaqvY8w6MmymqySV55FqL2x6ldUEcSonnSz4xjVLAWnOGlOqRcl3D8JtI4wXOr8pwSFiUKtCJLRSW2QfH6717CNrhTpDXOHPKkbDF+bbe79rNuL7tbBbKB2qX0uT5MWToHXdSUc7p9Eg46wxF404VzNo4kyOpldRDPB/xxgopcxiaK333KaZow01rYOA6/fBPxUYo/U2ldA/HIhnhViO3ni5FjD16p7HjFJh9lIwYmpVs9BA/945AHI5JHW/VDUg55mDDPCnbo7vZodSl4bo622buZd/o5qGx8ivtbyLiclGP5dEaW92RlbN2SoS1sTf7YeTtcjJS+RCrMX3pjurGMHnsgl25oj3ONNkcGMUcGMyQEm0+hIqO8OraoDL1ohfeeN313rV87OrJ7ZPcZp3Zokda4oh5totWLGChT46J1MGTfXpUO3xbTz67DXh7Ym/3fMMckGOXR0QeFy10ODfaZJzzum7wsYWPQc17jIrDWt2OTqlfd1dHPqLMwcxzQdqQezjDXVyiRYRTMDdCCvlxYKfD7BSZGJxVzM6c9HRjQAeAzb6te4xnd8h1POJO1RT9sBYdUMgVfSqnvb1ryY0kZjdl2+xmoZb14G4jD3/YXHGfTBlH888ZIV0TnSMNS+3xyI9uvFZO+pipwvXI7ehbzqhylqkN3t2sjD9ZW/fE7A5Ry3OSWijiMV57d7aPT7eM3p/rM3eyzoF2vYzcxekB+EGn646VvRQ51XC5NU4YgQb3nacD+BlwmsVk/ogLAg1vNW4W2FlzH/LD7g99dmDPuKfusgiSrzR62cg7bt7cJdQgNETDd5LIq3Q3iLcjU6718za5e/HZswbGQdpBgABAQImkCKeTVm6MsJtj9FHu11kfkNxmvrAnImKPlDOIDAE6I4YtkP2tOTjBDcJmWaT7sR/2tAHXzCS0to/HnO/aB4YRpHSWh5vjozu/O0++nwuiesqQODluJOnu6dFtjcH8GZ4m6mxSHcfdlVzDk+05sw9hh4YaE+w3WdnjglelCM2GTt+danFLK1f9bGJ2YZw4/iwXWfY4l4wKHQAJjQaM9YqY36XTXtAxLvGi87X1Awtx0yHYqqR0RXeUsqUvp6I1sQe0vdfFvPYYLJOa7GokyiniFd11Ir28IXX8yBsxUO5jYvIRQ+9jFCFUcSTiPuzSWrqE8DbI1+lgKuMZypvJieHDtROi9XqvyXZXsU1zUwl4PoxSv7sJLSPeiBN0yV2+1ftY2O9s95FZpphXLRuIxEUmnbgprHptXRNEG/1xazzEXRzFF2qKwZTavRXFhchIpNt4qo2wuEPPF1/wrjQMawdrfNByWN5GOHkoG1kzL5ZwxB/bap1cCLvJkRgvs9lBtBbhujvEwUp28vnx4nXIVgm2mGne2t69gl7LzyyCpI8V2eyvzJUi+KIQmOPICrtxj/Wwd2tg1knlOEvdo9Hv9k1xftwCUkukiehJmb+ImxsT8TZCHdJjV18qaeA33JqH2mZ9gJ2DiJ026vaYS6lcsbtxDVUZgSt7DEcctcMc7caL8qDLLeY9GHk6d9Vjc+ZbxYcPzuOm8WdBqMQbqRK0z8gZ701i2ERCIsxXQqUPJsfsxEK2rYMQpGGPSnkQPrSbvVEDUHfM6YFPe1+4TXYeisjG54O81GiraaiiRXMv5PKilXWffcRQlXr1WdklxYmzFEXWwcYIa/d7RYTRfNurFAefK4LJLSlVugN5BIi90697Yqs/JkSYbRXgFNrJt8eNKcEuglybczx0ISVYascH6fWqo2uiQ7cX5dor5qND3QCy9tFeKrs1OqWZzNTVmaXy7GzRrKKzdHtQcypiN3ebP8lC0+p3a9izNga3lSLuMNHVqDSlxN7tRuQ+YLPwQCRyz5kErqo34VHenL1/CBo76GPDjx1ZPpHcNmF3itlU5LAZ+FAVZc5MUXzMTCRZj/YunqRGhcuNeZ87iA+Hiwoq99ptXXs0vSIWSCi4nB407eqp3a5TKIMDZ9wN8L0z5HtbVC2e7w5gQ+57ncW44Xa43mscD2+EdEpOUjakiQSfDJdGh11IZLsdHQdtLDgnz6kGNrx3Hirtk9GPcBv0fN2eYkQCdCvw42JUk/QoY93ch44KIWd4bFXfuhuF1J7xvKLsnYu5tp6fqU1hsybsIBN1Qg/avKct2+Cd4gKpGkkx0I0jGtmh2qLbzmGSh9kY8J0Xj1AegtaYpzHi1JriVCqp2CHHNWZXruIT2R4Oo3tRZ8McXGavDBIcIbA9okfB1DP9dQPdFO+Sb8BW+Gr24/HeZQxXtic2rKJ7h5DHUPEty36cNBPlsPZcBffBXG9IGUtAMR0j1GM2RRm7WQtfIuoUuCZ95rIykK/z7bK2LodC0iQLAAvRCbhoX2zhAQWqpcXrEwYCUVA1pFwG+xhR0MGVMJOEGkrdknZCjqWdFoOLZ1LphchZyEeF1VAB5U/JGUNrvlRO9JbcQxRkQTindWZj6R0x9NCDo7KLdOeu893gEX+y1r0wii7uuzzq0H72wDe8aMRnLixZ2WFjA1VF4xZ68wW+JsK19iz9MDziNd3lD9lrs4zHdGeu3X7j8uIszfdbkProXbrvEHjfXieYduhdXCNrUvQlIss0bjgXtiveZIUKiOngbuWeLI38ocKOvrsl6/sNbI0QjHB0Q2b9uzfQoGjRcnIYqcT9PDN9Rz3zhu+RdU6Sfe10oIbka0CZ/Ejga96x5G1q7jd48KhtwoGcpB9YsWCmOtNpN9d3OAWdr06AmtUjizhtJ4ytdwmvF/uCp5LTWYE1tI5rD+MJdBmtabENq7XeWVe89Sy0EL0HVWvER9RDMb6M1xkSyZejf4XD7shdbudUteJRMbDt6eHhTL0bD9srkYShLAMvi1hREvUpvYxBqJ4fjZq54+0cJ3v3saM8gXLktXgLcl9PyHDcz8lm7OxTyLUM3BzJdW9ny/6eRTBb2lF1oRPGkajG4hT5pbC7koqv35ThmuywM6kw06bpTpT0QG8z2IsUQrWv5rsSsTcEf9wZomKq2uvnTmPte2PNGEY/ztujczo2ghWgCZrLcKlCs1tKdEiaTWeth5h0zm1xn5McU3WNrwIpd64yVOISih820wD2SbKedYZJEccoBDmzvZeF7938+TwSmF5mYZPVaMPgk97M9qEv7zd4mBCezWWpQ2BZW/u9utmG2yYhhCtTFzdenr3pcUVieu0q5OVxEmq8PYTshD/MPapFlxvba3vrgTq8SyTszPbrGHelFsdaG2ZDk5BcBKfl+Xa/c2on352kGrYKaZ8GWLLq/FjZ4SPartV0VxY8FXUsFp5hgtxJgl+iWxOKhIcMY/c1WoS50OtQfaIDSSa3uwzhinljHXBJiwfZ9WjhDtg7uoohOAvFrUlewjNzw5GsNVm5tHs5EEIwMw9QUttTmkbolreeIoKrhYvuNpzDIsdbFnbBLA2ymgiOgSPdmgg434L202akM7eA0z3hJBqPtr60raUxGPCrmBgZOzF8ltUQM+8u03E/2ESainhzMQcr3egwjufspptGtC166lLim2MrtsZVxAKPPRu8ju7IXWHITkSadgf2M2D/pRr1qZpkLcSO3OnGwzsUWTN79NZtz/YV2juFts3wU6NBNpTZR0hyapRqKfGmwFfR7EmdOJJoQQqXzOlhl9ta5T4PT4gRyGje6I/7yQZtEGr2PhFdN8Ol6Hh3S7Ln3IYJT3B79YIawhUi+fgqBFBzLrH9TTDXxtGWt5qFHE/iZqYA5AtXU1On6x63KHZNujsPu9JbxRUfzmkt0fwFVkSVP84Vk403N0EMfAyJVu160O0r+BFhjUHp7ruCIM+t1c+1TZMtEnDri+xakOvKMpTM0W24JNs1HtDLgqdy7vIeUQVdsGjpQKIXeX3QNTVUDvjd27bEBMFCLkAuHGM2Q+0ae0Zu+z3Wup6O2TJ2xe89JoYbtTs5EYuDBB9CrMECkEtDdd0/vE1qrQlNYxC1z84dxtKTc8BG0BUFHvBVCThdCwve2xNxV8xYLVvIiSJ9I6LJvFOtpt4zzpkQELJY+3DobchzNUh2Iuz1fcLxw6Ctd/qJlQ8aB7NbUWFGWsa0G4UykdcfB4xIAG0ppx2XUGEQxe48IpXtRS0bpnuVC+eHySKijNumsHXw6HzbDAoHar2JfKtps5sXjNs7bEIt0mn9/T6x9wui1fY2G2XU40n4tK8nMKa8BnextrZ3np85U0NswyrGamNR00bG9yCmO0h7rJHuupmt1mLaMSSZ+VZ4g+RiSit1FmUr814Sx37fSjSphBCGS8n2Pk4kCZ8NLyrbQZMLDKKMU8Cs2XSXTdsTl+j00JgKPhs7k6Mv1a1OpwOqi3O9HfaSBkARO5nZYdzvfQYqul0Js3B8vezBokSNonMf6zDuPnAM6dbbKCoFZD+cGgght1d2rLcPNsIy9h7gxcZNCEXkLvXeJefwrk5y40+kdsr4i9qYXKDIsXj1hZREN8SNJIItlEFgy7GP4hNHQMxIbGHdY1FF7uB7rJiXMAr7ICGPnlajp/gW7TMqZCHaRfZqWBw0mqbfPrz9/pT37V/0ktzyXOhf9njq9STp22stz0edoRt8fur6/K8y+M8f3lo/Bea+Ht91xRC/P876m4d3H/9n7zgssqfXO2vfHni/Hub3bry8IP6WVsHQ9e30tauL5wsxYIa3vNQUdt3ycrEPvn98zvujA8CpG7zeagnbr3399fVgc7m+2NCWYZD+fvpu0vJgeALhT/3uK7YhvoZts3jj/eUJ4ATsE/wJe/vL/wG9Mw6c7y8AAA== -->
