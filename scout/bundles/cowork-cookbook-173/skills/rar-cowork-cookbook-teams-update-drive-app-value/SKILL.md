---
name: "rar-cowork-cookbook-teams-update-drive-app-value"
description: "Drafts a Teams channel post (markdown summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indicators and quick-action buttons on drive app value status from Dynamics 365 ERP data; saves files without post"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_drive_app_value", "rar_sha256": "04b90dd712c0555198997ce2c1ee8c0bdfb008a27b4edba3da60bc4e3a9ac888", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_drive_app_value`. The original RAPP
agent is preserved byte-for-byte in `teams_update_drive_app_value_agent.py` and in the RCI capsule.

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

Drive app value Teams Channel Update — Drafts a Teams channel post (markdown summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indicators and quick-action buttons on drive app value status from Dynamics 365 ERP data; saves files without post

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-drive-app-value
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-drive-app-value-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to summarize, e.g. USMF.",
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
    "topic": {
      "description": "The initiative or area to report on, e.g. drive app value.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_drive_app_value_agent.py` and embedded as the fenced Python below (sha256 04b90dd712c05551…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_drive_app_value_agent.py` first:

```bash
python3 teams_update_drive_app_value_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_drive_app_value_agent.py   # or on stdin
python3 teams_update_drive_app_value_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Drive app value Teams Channel Update — Drafts a Teams channel post (markdown summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indicators and quick-action buttons on drive app value status from Dynamics 365 ERP data; saves files without post

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-drive-app-value
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_drive_app_value',
    "version": '3.0.3',
    "display_name": 'Drive app value Teams Channel Update',
    "description": 'Drafts a Teams channel post (markdown summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indicators and quick-action buttons on drive app value status from Dynamics 365 ERP data; saves files without post',
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
        "upstream_slug": 'teams-update-drive-app-value',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-drive-app-value',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e010a6edbeda491f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/drive-app-value'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-drive-app-value', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-drive-app-value-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to summarize, e.g. USMF.', 'topic': 'The initiative or area to report on, e.g. drive app value.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of drive app value. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-drive-app-value-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads drive app value, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Drafts a Teams channel post (markdown summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indicators and quick-action buttons on drive app value status from Dynamics 365 ERP data; saves files without post', 'example_request': "Draft a Teams channel update and Adaptive Card on drive app value status from D365 USMF — save them, don't post.", 'inputs': [{'description': 'Dynamics 365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The initiative or area to report on, e.g. drive app value.', 'name': 'topic'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-drive-app-value-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on drive app value status pulled from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDriveAppValue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDriveAppValue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-drive-app-value-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The initiative or area to report on, e.g. drive app value.', 'type': 'string'}},
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
    print(TeamsUpdateDriveAppValue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8/SEzW7bZQbijIgYkkFiExC6RrnCy74tYhCC7/vtcpNfOzKqsmq6I+TRy2BJwz37Oc8715dc3d+iTun37/KaHbrXau0WRJmG7cqtgta3Hus3BV5174O/Kr6u+Tb2hr9vu7cNbEHZ+mzZ9WleAfNe6Ud+t3JURumW38hO3qsJi1dRdv/qxdNs8qMdq1Q0l+D2tmmLoVtjKG4oi7LufnuKAeCZwAb97uNq6bbAS9ZOyGtM+WUlnofuw6nq3B2RpFaS+uyjxJLsNqZ9/dP1FD8Cw7+uqW4GfQbswcptmdXeLIfxGHbV1udpNlVumPlCBJFacdl4Fbu/+16pz7yFYkRbg30VuPfRPA4Cx4cMtG3D/7fPPf/3wloLfb59/ffMLtwO33p42mw3gEu4WsUzTWItQQFi4VQxWNBNgV4HrJmyjui3BrSCMVu9XP3ZhEX1Y/ed/5qPbxt1Pn79Uq/fPl7fljzZUqz4JV33tdn0YrHy3cb20SPvp04opRnfqVm3YD221RKADUariTy/K3zjVzeovy7MfX0I+xWH/45e3GqjgLr778vbTqm6BvHZYfn9auDQ//vSpqMew/fGn3/h0g5eFfr8wA1p/+vp+/c4WLPxtaRqtvupnbvsuqw39tAkB89/Zt3xeqr+ze3fJ19fiH+vmw+rPOS/2/AXo+8pDD/D9c7bAB4Dy7VNWp9WP7zLa+h5WbuWHP/70z9j6SejnRdr1/yO+P78YJ6EbAG+9u+SnD8/w/XW1frftO89/LrYBCfPvWAKWfxP33VH/jPczsn/HukgrkO3fYvmn7P6MYP2X1c//1LZ/RfBhFX1524UFqJLW9Yrw8+rXZ4r8/EPw280f/vo3wPr/ykavh9Z/cvhaulUahV3/9evPP3TP2z/89ecfhgZkMajNr0Nb/BnPP/PrU84fPPi+6sc/0gL5ZpVXC6p9r6HVr3Xzv9q/fVqB6k+D3+53n1e/r8Tls14tRnwT+nLB76qxA7r+zo8/vf0NoE4FrBmeQLeAzn/8x+qY+m3d1VG/0v0FrECA+7QMF+WNJAVQ2T1Row2BX7sUOPZ9Hcj/JcKLxnW0+uV/+0+k/+i/Iz3UL3j2dXgC2tcnkH4FQPr1CaS/fFoZgGfdpnFaucVKY87nL5Ubh1W/yGvasAvbO8Aob+rDj6CUPy4/AGqvfvlXbL8+OXxqpl+eqJ6+8E7bCgvWdUMRflqsspOwerfBB/0ifIT+AJgXtQ80eQL3B2BtVxcA+vvFA12eFsUqSAGagI4xPXkDL31emP3yyy+e2yVfqhc4Y6tXP+sgsOC7OquPH4FJUZHGSf+lCv2kXv3w699+WP336l9RPZkvMs6gQbzHAGj47GigpoYSLFs6GQBzN3jG4Ne/vTsWsKlAAwYRS6M0fBGDnMzD4JuX9QPzESXIlRcC7wLPlk3d9gDxV2n/aSVEq+/6AqHLo6UnJEsfDsImrIKw8ifA1QXmfPdkVfeg+/VpF00fVkMXPqX+4rXuU8USFLfb/7I6bs+gA9UF+GdR87kIENcV6MfF9xx43QdM2h+6FfuNxaeVsmThqnFbt0la911G5L7iAjrPN3LA3F1V4filWtpsuLjqWRIv94BFwDP+e0g/LjEHgwmYKqqg+yb7ucZd+qTx7Jftl6p7T3e3XULhA/gHQuMhDZYm8F/vKdWBjl8ET/8BTRdO71EI3qPyzMHd3w0Wr4Fn+z7wvKaA1ZcBhRF89f/zVLT4gtnvNW7PGNxuxSmGdn3FaBkUl1i+ZkswpKxAor7q8bfB5Rs4fcPoL1WRgoRrp/96rXxG9n3NC/eGFgRCY7Qnf5BWIEYL32fWL1nctku9uF+qb83gA3D8E/mA4QAiQAktmftN4PL0m6YJwIHl+rfB4Jkl7eL/pe5WzeAVIOuiMAw818+BVu1Sue9hBiUQLlU8Jqmf/MGqFeAOIgv4L95PQS6AgH/6DtCvp99U/wPha/5ZSJ6z4QAKt30yAHqEi4JLmJd4APX611wO7Pz8ZALMKJt+sd0DpQMsfd0M2xDkRZf2C0y+/Bo2AJ4/Lt8vS5e74aMB1QKcBSLdDMC7zypaAKYE0w3QAQAJKKoyrUC3B055d8KToVsukAAg930cfXF83n43KHyW3tKmvhEuhiw0S+d/ZaJbTb9HDuPP0gTwK5cVT7l/n2nfpS28F/TsAAICid+evkaET68u/xojVt/4fv6Hjc+P/97e6Nm3zT8mwOdV0vdN9xmCXr32W6v9BLALeunavdrux1d//Pis1I+gUj8+K/UPPF/mfl79e3r9gcV7XXxeIZ/gT/DySH7Pq/cPcMP2I3v9iC9Pv1Ra+BuqAvF1CRJrCdoE+vz3FvhtCeiDcRvGy+JXS+yWTjqC5v3sASACX6rfJ/pSaAs2xktidvXvAOA5C4CkfwXse6sCj6oeyA6WiTEOPy0brUX9Lnz7XAH4/PAGoCz81zuzpROVSyJ3y1YOlAyYvfo0fF6Bigy+Lgq82Pz6d5vd07MwVt8WfE+rf0TqD6vwU/xp9a8i+xGFUfIjTHxE8Y+L3E9ZB5odULCfmsWE13ZuGQCfaPXo/0Sf5w+3+LTahQAZi+73JfDe1Zau/rtKfXkdeNsHdn9YoB4AEDAD2LS4ZKlytwNlA0z7U10KEN7iK4gCKLp/VOgPreS5dPVaugDwq92lc/juHFM/8n8q4/s0/I8CbDCQLLyC+vPSmz+8Qx74BjuYD6vvmxFg2fv2cJEQVgPYef+8bISWBHiSLD8ADfj6TvT9Pze88O2vf6JXXzep/486LTAFMLFP3WcOLCMNSPDnsPScw0AHeLf477rwnxgPpDzBGrS8ReHfPPGbPvVzl7boA/TvX/+p8OsbyGh36dvvOf0+5oPlANs+dsuYA4GKBwLB9as2wbN/awPwTtslLhhCATGMezQcBBSC+jBBEAi9oWnKD1EfCcOND3tB5MHwxkUpD1+aJxa4JOz5eIi5tOtvNhvA71XdX5c5Ll30IWgqgmkajXAEBazDCMWDYENuSJ+gUNilPZfwCNr1fiPNwfzzbuTLqMWD3/ciizPebf31zSNxsPKAdwLz+mwhGvEgm/Im+QJd4M2jGO2h4d20o/NzfWyVh+6gXZ7c8/mSUuxVtlB2T3BZWqYScVCkU1vu4x3NVZR4hoMNdTS3Gj+ZJIriGyUv4tQBip+cNeSjXhcGVNwK6b1wWEK+EYWZVg+jKxX+FrSle71xAVTk+mStlT6C0va0bfOud1hU2ycHQsyHhx1nKQmshku+zTz8zlqEWVaPwUpM3RWls3adsog9n4U+v/TStqEk4cFuhnsFZ94gTnJE3SHRDrc8JnH9OVWEZmfbLk+UOWRdeFxxrGRv+81WdIqivLEZsj/4c0/Ztur5nqMQ+vU0+uLlgtcXb7Ph+3QfbbfonTc9bhuRVeCdbgQDH9luvV6HXp+i6/B+6R9iQW7CKEJZZL2xp05zyrKBC1nYlid5UCbJsVzBT5AMmqVLOqeJAyX2tdpaJCUxHuOI920cx1NQChJWJiXL8I5j1br8oPvCE1Mos1jrqKQEvXFrDnclYXQ2vrdXXZkwB/GxI3u9hikDEsf0fpRbhTxd2nbNP+S7691Dhw9uiF7WmsRvgcsddqNs5IcrHri6yBt++wAQpgdqyqe061xvuY7xs1GfEBKjt/x2r+V7r2GpHXtj62hmcY3qZuoxn1u7uJ583DKsnein0k3hBd4YfTkt4oxwBJtthS59pO5DdSqDOW88SNKVFlWd69iXdXgzd8z+4ASSQY4byyACT4rgnAqEHW0fLoJZJIzRE4nNrVPSGOrZKIJMSM+xluuN1V0rYy/QOyyDjfzR15ftVTwJ4cnM0Lqib72028K8vRNCxngY63PBJE3ZEefGysZ7zQtjv+NKRDYlWGlVhicnF4kQPVfJNDi2cnB1rEq5B9bVqq9yl3hZnG1ErQIyqe21be9MNiBtXD2SQNplvrJm7pf8PGoyRyXHac+q9GWPn8sARZV5o5Py4Uif5lwMbbEmoCLps/yRnW5GfpPZ/iTgR9u+VEehaNaTbjhieZvPD98aEcmKL6VQnSEuWgvUTNSUma1HPz2J8BpCDyRr4SfsdrPiUhG7+NhVNhJrpN62VtIlKimfthCSap0+KfbN3HZuJkDX+9mbZWNkW4qr9Qul9vt2EscGkmZxVxkXv5KdHV9SMHtSBJgczf0N0rm8P+Qc+Yjv+IZVCJbbxYfdKD8sZTy57Cnc9f7I7TflXZDz6TT512MUPuTH4cIr+AmaXXJv3Iq9YHJawrPSBHBJ3VqdoRrtNW3OZaTiaTSsA609K5wXKwdoy4u1Q7bZLu4xi57LivWU1jkOEIy7mDfrVKWXB5h4sNcbqpgozFdb3N7gnK/wjcMZPYOrrHneNHu/FBSpapq2GfDHUeAV3tw7bNEqLIx3eKNvq7rNHtHVvgTNRfAyjEFixSKOJ8IBSlnu0KGKjO4r5UZU65u4t+laGK103LFX/lSEJ2Hvi8xQMIQZ5ihVKeE+T+95vNO45rarsD7Icd2Xb+FZHUSkSiACsPLFmY3u3uUq10kcWhR5uA4sqVkkM0CoyayDzXjDZY0yOOW247fuScuufRAdGQmeyo3cjltXy6tkcFPgPAHt1hMtIXNXrHdheOoeSXZDhUNF4Y1kXLz7fI7jrJ5iO8YpjIUqTKIzdYaz2yQlsRmlPnbSc3gd52jDb3CcpwJSpEkIyw+zqlO1ls/pqIz+w+zZvZiSKE2N1f7OTVR/ZECtNQWvooF01HLaVJnI7SfPPJ2PHEhuiN88NhyfcNndcfltmOpxsxfPIxpfS9EqOZABNzq6R0elkRVB58pY2p6M2nNwp5f4I6N5xnl3u4pXdx2Ovfs4nZhY4G7SIddqPEu7Ot3WMdyF3TpW0YrzzdGOedYuDxiJz7o5lcD9Z/xwk1huxODzfq7D68W6jZfWms56a0/xaS56MqLz3NZlDhYQEaM3QQQmN9+Ut9mWV7v0yEUuWsGuFRPYJpcujlPT2wxCNGJHPHAIjhRX9i/+8YRme27H1fR6mDSIaRibu0wpTUN9q6GOHhCBnZWlRkt9uuWOx9SOWMy/i7poJZqIr81pd+s47rJFD9jVuEklOo+sP/uqp+7RDWoZgsakxuNQ7g68DJDWSYJrGgq5dpZM3dM4hhD0eJIOonCy9QsjOYVSmeJVwa/6uio3ytYIxWPlxufE4GEbToPgQaCz2pU3pvGjpIHxYz8qkucTJyvOXPoCthr9ZLgQaRt5eObYvYpQpASyGe13/VHQpa5D1Rwfr2qqytgQNrpZJjrySFFGMNE8O0xRBbpZojKbzp/iVL1uxbwlZONwwoqBbwdxEITUSa5QWhLZ5upbgrc34jmKVe52FuuxMM4VhrEO4yV2nbZXUib01tGYUt0+8NLyyYPgjvE10HKBVdcXiT3boY6v5W3CycPOLo7SxZq3mgTJiDMhgiq3J83RbEPFt+o9Plw3UYwIEoGLmug04cGF6+PBOSZB6IzMGiFNS9MqvDOSOlEenC7vhdC9qv3RfmRRK58OMetBPNNc9cfsbvG234Yul9ebjtfsEGXlvpJAW91I68rINE4uZm/mMTnFDheSSPdON+ixA2WIxwrqKRmObMqQwlyVXXsqGFPptnKsIIWWDhFMsjm9B4GrTekWighvuXLonC7yjjngmrWPqZKXtGRPbb0jec6tm3QVmEPNu1eAuY4q7DiKZ6FU2u0HaA8nGxcH0eMZCr5C66LEY5ZKj6hznQ/ElQh26DENBlPf3vR7S4n1iYKJq8odnCpJ+gGVnY1YpmOWX/bWxnsM8VymGWSObkMy5kWcoJOMwfOBvUOxJgX149w9DMvEOkVUuiSYxBrZ3WRPgI85bJRzYgpmdtyt75oGtnGl6yskZ3Fg+rvcWJoxkTUd55B/mBnLusKKw7AnUt9f55M1mbEriM06VLwd0SIP4Q5B95SWbVXwrSjfnAjsCCVXf9sjvNBezyzXwhgXdqVzg4Pj47izJzvP9vd1z6hp7Wz2YtXbXjehxlAcmTO3T1jRtUzFEjdwQO5OGHvFXFLJrNNYWa0EEMOxeb40d97l8EjxYyaGWEt5LgDtu0pEoI8X8z4JHeEcs10x9oiukqQC3Uvf1Lz4cpTYilA5R1GHmmVEuLhpugt6u16k/Ozcp1hspq16bYSBsbdcVcOIs/H6A+1SqES7onmmJH4T6OjdeNQArQyNpk8XbPMAyX3ts21JgUESiXK4qMt7Fs+27DniKIU3ZFsKW8j29IfBjFyVNDsu2TbuxPJ+XJp453rrgtYuZZZVjSaYMl4pQauFE04RjcHcb2FRk3cPh4hLgF38S4tspkITHopkNDy/qbPuIOja47oXeRcuxm0ipJdkzxPezR/pqTyfcj9Dne6GounDssM5H+obemV2yV1RZW0+3fqru59NnLZujV/GFJflGwy65bw0cG7+GHCR2+5kqbxxFrHTy2ALM2Y37RGP9K5qofP8DkyU8433TDzRdIGTcIwZ7EoDjbcZ9pZPXVj6epyRyzq25ZjTt3BkHOZeruFHsr7QqS93VXVEsCyu6MgNxC7Xbu2EZMQmt3rE86w8L09K7ojJUbiRUsxzsJq2d/diDRkbK2Z6jan8luUaC7K+K+o+9yl7r1TqdV3ZBd9w7o28mRfJN+C+uxIXcjQg/Y5wGetlDI32uBkeUv1AQDEiUhxreAcJl+ZrCuHn7o5DVmYw1vEW2pVcl5Lbt9tjR01jXJQ1OltCEeRK0TH+2T4W1VYgE8vptag4czqJsbFq4uihWit8EGuDohXmWrTa/f7KJTeR3Wd9eRJE0XZbyxXxyGriEjH5WMDLDD1T5zQ8wpXQxSV2n7UA4igYG3hd4g/dwKk8gRT3MpeiPjrONi55KPTgiqQui604XNutYJXq42rWp5u2Q+Cd+ZC8zO44Y8byoLCxy3E7jQf14ugPDeWTRLIH25J28RHRD3MgIl12p3NUNDzxjE8kWqc1647DaTNuM8vV1LCwyPVgj1GOac4+uWHe7Q7mTYvGzMbMh1s8HqVIaBHiDgY3zOkiUXNcFKrODSnwY2NXUhlg6KTWOh+PY0Dpzbxdy3qjUx25lgyTklhZovl5DuoEmhU9QI9OPBokeV4bnahkjYAFVJcUprqvGyXCb7Zy3F3UWLo0kN6FDMbZNisRqtilZhusuV7BuY1a7nNHgbQdjE5TZYcSerJgFuK7cTo1bT9KD8S9Eof7RlBv5J3PNuxZ1YWLVW72PBaedBSLLxc2ZgOy2vSYid7GxEco3jwlTlXR522S9SmYl+3LECZkWc4NZPKeQCOaTYnVukLW8mxaxH0bbGrUuRfrO6MamzNbq/K6Ly7hMJ2ZckhzyGvmUvE3Tvvo7sQDcyj3tMlqY79ekxsqietMQTCjdm8BbfAmXJVJ0cLEvcumXX0TWr1i5r5AQAUXu3SqIENGWQzjrXINz/TYWO5uDgN8gKNix5P87daSLWFBudbzD5DZSRlo3AMlHnBtbd20bUF+IH21mYVba7iRfTtj3SmR4AM9XoZhCJQgu9894bgWs9lqzItBN7M8e+vLjcfd0wMb6+ABssO3wTTCY9odwhAZilskbcXJbI8ItBbuOMK4+omiLlaI+UnaaB2bQzOhl2izTwoiSGcm96M43ZFXPgsgobWoKiLrCeQm6cvWxO6w42Xk8vKs30FvigKxOoOUbDpLPmIntEHFWTRT3J3QPiHhY8dcp5iTlXs6V7vwiucPPiNilBogH3J1ZzCi9ZxDMthDqnF4lSS8WtNU28gzjKXELoTiNQbQqyvV2YkPjgBfkoswgJmb8B7ndXttXaRJsWq2ec1XQqgxkV3rFo+pP5ChtS4vyJXykhGzrH0Nx3uHScNoN55QyC8c2MEejJE4E4pUN66wdnJqG3xVVC1aNgTotOZxQzajIniK7GRa62FXxCMOjveYjux5DidHAWNxQFVwImd8ViQir/hdGlXxeAZAH9vHWy6x6nFzbZIoWoeSvZFOxZ4YZtd1T8IRjT1bU2KbK9Xmjrcyn1CCdj8lhXhQ2lM07LpRFWWKmNRyuiD0EbJqODwfoGHtzYSK8GSsZmqwpufeMHYDfbgJyAVF1JECxZ5eAxjl1/aGLLgeTPNa9UBocoYFkl3LbbF28VraU/rMXXoSNA06GY/GWS83a08riiimi13BmcIGbXbKoaMcj7i39Qk19oS3wR3F4GLNwYxgb2/v7mkXDNtT18ZClCU5xRFRSIbEVnageN7fFMok0lGcL6XhuQfTMLlHU3Eoagek7FTOGm38JLkdeHc6HequvNS034VHzGfTfS2ShXzcZ8MeTMfQOqNL37jdUjDDxVjnOxZttrQoRN7OSq0q4e9XBqaJQNjIe5p0kRaLTmRZKfZMHAgqpypJzA5rj4B6dSAeVJALpRN6CEiyxkMH/BYPTlucnJwayx3heSG57nf4nWj7yNt3NxY98CjUVK6LkZeDaJyVxhowNSUnF8cbkOOb2dNpjB7wmO5bK+rA1s1psyvw6ZHqw44QRByWZwJupzh4FPJgbiJexFJOLUjVF4ZeNFskuTv9A9OZaxFV5izXZ00zoKjNmG2fmWId5TbCmK5DR9QYJXgvzNY22x9gRjpcLmv5yKoC7JOwEdHrSdM0B5WbO6hj5tzMlHw9HXdQozxgY69i5Pi4B5v9dOQPziFOyfI4Qujtfk2pggrXcakezrM3eYN+1cwbp6D9entYNzl9vFyhg1NodH3lGg2KLr0dYVrf20QR8Y4atrLeY/aF0OgmZCwZbbVD0nbBvTkkFELpvbz3O49EYc8+Dci9mN3moh+LrD00V6JL1+fZHZHbPp9w7BCN3S6+NHRzhEkaVwbdkSjstkXkh408BuP+0PYHMz8W7Fq5M/cSi+3HyNw9JO1cFTJUBul3Y86Ga4Kp11LYnk3X5AcSFmV2zTn3w1lwnblQ0tP5ElSkNYTxUPRnGtadI3TjBfumzdC2vyTERBEEMW4cSHdKou8ZNteKdKdv6WKuYg6+7jPjxKyhEKLPBPcYz3CKJLCzxm1rS3jNmFAoig+IUfSnlvLhaijbaTLH8NSGLbgILproowQcH801Xg+nyRdpjXLmlh3HTaoqoSzXFxvZX+im7+/lXN+v0HGb21AYE55597PHccMP+oNxy9gX80fuXQaVmlTx3nZTiCMhd6WFLafaJHHAeaFT8IQz1HOCb2SGoYJ9NkciPcAlpsxGdpbWob43UJ+MBKRK2tOAQuae5k5xTRfp7dCZh0dgUuARgVzMB56DVnQOCqcPkKDczBf3DBU1xoTUTIRQv7tyLqR1O6/flCSPjVflsdGPWziHowBNSVq/5fitudt45skQOTBUS150be6r7nxGi7SyfcSNw80+hM7B1GP73qsOpa2EUkRk+/5qZ0gOSu0eUR03hhhxpQvy3li9r2BSi9lre5tWR18VosMMph5hSxYmlClH3lRZPSRTWTAowTtlCO7zh0t28Hv7mDF+MMpre9x76llnEzU478bmMG61OZx9fY2rcn/LEHp99cwQv0TrIaK4kAe4661xJ6Ba/g58KxJmVjCUHcoItdcecqmuRf98yvhTnTYNzBpGDlcn6KKokHyHNuHGBqs71qkOuMVDt9TwnYbj0wI8cbOYCMUko+RsNqV5RLKsDiEWI3wLhx2OYxjmL395+/D22/nm2//ozazltOX/2aHP63zm29sWz0O50A0+P2V9/p+p89cPb62fAmVeB1pdMcTvR0B/d5z18V8dvy6U0+slp2/Hq68T5N6Nl9d939IqGLq+nb52dfF8xwJQeEO3vCbYLW+S+uD796eJv1ceXLrB60WJsP3a119fB3nL/bRa3qEIg/S3y/j9jO/DW/B+fvoVI4mvYdsstr6f2AMTsU/wJ+ztb/8HU+K3f70tAAA= -->
