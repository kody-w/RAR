---
name: "rar-cowork-cookbook-teams-update-renew-software-licenses"
description: "Summarizes renew software licenses status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_renew_software_licenses", "rar_sha256": "12bb09a37d5b202e6ce47b9d437b482ba32c23847d360a4bb60333f89142f19f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_renew_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `teams_update_renew_software_licenses_agent.py` and in the RCI capsule.

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

Renew software licenses Teams Channel Update — Summarizes renew software licenses status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-renew-software-licenses
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
      "description": "Filename for the Adaptive Card JSON artifact, e.g. teams-update-renew-software-licenses-2026-05-24-card.json.",
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
    "topic": {
      "description": "Subject of the status update, e.g. renew software licenses.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_renew_software_licenses_agent.py` and embedded as the fenced Python below (sha256 12bb09a37d5b202e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_renew_software_licenses_agent.py` first:

```bash
python3 teams_update_renew_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_renew_software_licenses_agent.py   # or on stdin
python3 teams_update_renew_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Renew software licenses Teams Channel Update — Summarizes renew software licenses status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-renew-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_renew_software_licenses',
    "version": '3.0.3',
    "display_name": 'Renew software licenses Teams Channel Update',
    "description": 'Summarizes renew software licenses status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
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
        "upstream_slug": 'teams-update-renew-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-renew-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6045e6878f955f73',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/renew-software-licenses'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-renew-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-renew-software-licenses-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'topic': 'Subject of the status update, e.g. renew software licenses.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of renew software licenses. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-renew-software-licenses-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads renew software licenses, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes renew software licenses status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': 'Draft a Teams update on renew software licenses from D365 USMF, with an Adaptive Card I can review before posting.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the status update, e.g. renew software licenses.', 'name': 'topic'}, {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-renew-software-licenses-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on renew software licenses status pulled from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateRenewSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRenewSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-renew-software-licenses-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'Subject of the status update, e.g. renew software licenses.', 'type': 'string'}},
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
    print(TeamsUpdateRenewSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916Z9PbRrbmX+G+94PtC+klkQHdmqpFJEEQBInEYE3JyIHIiQC8/u/bICnJnrHvzmztp6VkkwC6T5/4PKfV+PXN7tqoqN8+vem+nS/WdprGkV8v7NxbcMW9qG/gq7g54L+FW+RtHTtdW9TN24c3z2/cOi7buMjn6V2W2XU8+c2i9nP/vmiKoL3btb9IY9fPG3C/ae22axZBXWQLfsztLHabBUrgC0E7LIICLLpI/dBOF37exu340KH2267OG/AISL95xT1fGL6dNQs3svPcTxdl0bSLMu3mIY3d+96C8WygVO8vOLv2Fltd3S/ucRst5IPUPGRWXezePtrurPkCmNMWefNfi7xoozgPF3HzkOl778BGf7CzMvWbt08///3DWwx+v3369c1N7QbcentoYpae3frabLP+Mnn3shgISO08BCPLEXg5B9elXwNLM3DL84PF6+rHxk+DD4v//M8bmB02P336nC9en89v8x+tyxdt5C/awp41W7h2aTtxCpz0vmDSuz02v3NUA4KUh+/Pmd8lFeXib/OzH5+LvId+++PntwKoYM+O+Pz20wKE4PNb3c2/32cp5Y8/vafF3a9//Om7nKZzEt9tZ2FA6/cvr+uXWDDw+9A4WHzRDwL3Wqv23bj0gfDf2Td/nqq/xL1c8uU5+Mei/LD4c8mzPX8D+j7T0AFy/1ws8AGY+faeFHH+42uNuuj93M5d/8ef/kqsG/nuLY2b9l+S+/NTcOTbHvDWyyU/fXiE7+8L6GXbN5l/vWwJEubfsQQM/7rcN0f9lexHZP9BdBrnoDK/xvJPxf3ZBOhvi5//0rb/bsKHRfD5jfdTUJ+17aT+p8WvjxT5+Qfv+80f/v4bEP1/FKMXXe0+JHzJ7DwO/Kb98uXnH5rH7R/+/vMPXQmyGNTol65O/0zmn/n1sc4fPPga9eMf54L1zfyWz4D0rYYWvxbl/6h/e19Ydhp73+83nxa/r8T5Ay1mI74u+nTB76qxAbr+zo8/vf0G0CcH1nQP1JrB5z/+Y6HEbl3MOLvQ3aJrFyDAbZz5s/JGBHAM/J1Ro/aBX5sYOPY1DuT/HOFZ4yJY/PI/3QfQf3RfQL9sZ1z70j2A7csDzb98RfMvX9H8l/eFAWQXdRzGOcBsjTkcPud2CLD7AaG13/j1DMfO2PofQUl/nH8s4nzxy78i/stD0ns5/vKA7PiJfxonzdjXdKn/Plt5ivz8ZZML2MsffLcDi6SFCzQKYgDcH4D1TZECNmhnjzS3OE0XXgzQBbDYi2K6/NMs7JdffnHsJvqcP8EaXTzprVmCAd/UWXz8CEwL0jiM2s+570bF4odff/th8b8W/92sh/B5jQMgjldMgIYPbgI11mVgGAgXCDAAkEdMfv3t5WAgJgd8DCIYB7H/nAxy9OZ7X72tb5iPCE4sHB94GXg4K4u6fTBZ+76QgsU3fcGi86OZI6KZNT2/9HPPz90RSLWBOd88CbgQkGkbN8H4YdE1/mPVX5zafqiYgWK3218WCncAjFSk4H+zmo9BYHKRx8D933LheR8IqX9oFuxXEe+L/ZyVi9Ku7TKq7dcagf2My9wMvKYD4fYC5MjnfKZff3bVo0Se7gGDgGfcV0g/zjEHfQpoRXKv+br2Y4w986bx4M/6M8iwZ/rP/QmYCOgALBp2sTeTwn+9UqqJii71Hv4Dms6SXlHwXlF55KD2F93Os03hXm3Ks0tYfO6QFYwt/j9slmZXMOu1JqwZQ+AXwt7QLs8QzW3jHMpnpznrOqv/KMfvfcxXrPoK2Z/zNAb5Vo//9Rz5COxrzBMGuxqorzHaQz7IKhCiWe4j6eckruu5XOzP+Vdu+ACMfgAhMAQgBKigOXG/Ljg//appBGBgvv7eJzySBDgIeAQk9qLsHBCoReD7nmO7N6BVPRfuK7qgAvy5iO9R7EZ/sGoOFkg0IH8BlIhBKYIYvX/D6+fTr6r/YeKzHZqnPFrFDtRt/RDwSBig4ByrOXJAvfbZpQM7Pz2EADOysp1td0DlAEufN/3aB8Ft4nZGyadf/RKg9Mf5+2npfNcfSlAswFmgJMoOePdRRHPwM9DsAB0AjoCayuIckD9wyssJD4F2NiMCQNxXZj4lPm6/DPIflTez1teJsyHznLkReKa/nY+/Bw7jz9IEyMvmEY91/zHTvq02y57BswEACFb8+vTZMbw/Sf/ZVSy+yv30T9ugH/+9ndKDxs0/JsCnRdS2ZfNpuXxS71fmfQfQtXzq2jxZ+OOTJj8+YOLjV5j4+BUm/iD7afanxb+n3x9EvOrj0wJ+X72v5ke7V369PsAd3Ef28hGbn87g9x1cwfJFBhJsDt4IaP8bE34dAugwrAFmgcFPZmxmQr0DDn9QAYjE5/z3CT8X3Ixc4ZygTfE7IHi0BCD5n4H7xljgUd6Ctb25kQz9eQP3ctTbp7xL0w9vAEf9f23jNhNTNid2M+/4QAmB1qyN/ccVqFDvy6zIU9yv/7AVFl9PvuXXn4CsDYTNZPdh4b+H74t/JdYfkRVCfFzhHxHs46zBe9IAFgSqtmM5G/Xc982d4gPHhvafNVMfP+z0fcH7ADPT5vfF8aK7me5/V8PPOAD/u8ADHxazgs1Mz8D82Tlz/dsNKChg65/q8iCpL0+S+meF+JnR/sBjAJKrDmDCyzGmroh/Kvdbq/zPQk+gO5nleMWnmag/vAAQfIPtzYfFt50KsOa1d3xs9fMObMt/nndJc/gfU+YfYA74+jbp2z98OP7b3/9Er7YoY/efddJfu2ZAC0+ofbD7M+AvU/+iE/gT68EyD+wGDDhr/N0V3xUqHsvNCgED2uc/Ofz6BhLaBivar5R+bQLAcAB1H5u56VmCwgcLgutniYJn/1fbg5eMJrJBawqEwIjjrGgbJT3cAXnsE66PkQ7tYSjpYBTi2CjiIiiFkR5KrGzMcYgViqIBRcMYEsB0AOQ9i/3L3N3Fs144TQYrmkYCDEZWnucHCOZ5FEERLk4iK5t2bNzBadv5PvUW597L2Kdxsye/7VRmp7xs/vXNITAwcoM1EvP8cEsadpbozhnqM5SvoEE7eXITWyyM5ca5rrth6zSJCu03l2VabveaGjD6aStLR4ZnmXKL7691eVwet9BooCrioccjI2y9DCcuNIazwpbcYrSP4hAOTTJFTuwJP1UysZ6s8y3lxpOuinpppRVlonI9uOm6rFJ52Hn4VmjSZb9Ge6yb7LqztGBcrkXFBVC8O1lXu5bKRl7haOVN60KzgyAQpcNmSWrVOB5vsVbtLCUS6l23v28z0w4t6ypWvSDDHBSTXAXvJP0UGZNRurERF9fCt28xZei6r6WBnAtxvEoomr6hNWVZ5zUpLMkBr655lsCme74N6Um5XuXyap1OdhnEk17vJ4GwaiHLsmpkKSXPSRj2+vw8wTS9HEygG012KNrnMWrqO2UVSQ2XZlZG3EOjSPGJuZ6VMtipsphD4jV2t+e6CflNOGq+WO8uB+PCW+g6RllGqYRtI5DjMgiq0+g2mHU8GYnZBj03sB0XxaPIqG0i761VdRaQCTOjk70vxRt2tLIUzujNDoaDNXFDWx7tlbCz9NowhXVzOTrRkS34gwydVlvxImtmez2HbH5jokuFZMBUoY2252xK3PZw5fW4RDSxY0InEWqiMaW83XTTod8oUGtbIT5F1t5U0kqqipUZWofrpLA2cYxWrcekmakdJ/SCbYcyPNDtuZWzlJSVxjxPJmvK69YaqsAQxvSQriCr02saj5faMXAji5MRuebqibtt6XSVerdGRpV4C2myJlunKdkrTnLbBIdBPZ7WpbfFbsNg8hB8gsXQ5gLmthEErFyux9FcTbtLt8JhzLpx6WUd1YYc1aLNweVxTV33fkeUJ8lj5VyEy0appgztqka+SSJybIchgsRiKs5AC8tKp9BC7WHYUIOaKqNoQWyPhvxdO4hkxIzr4UpZXTjYG9KB+8h1lGKEl4frTtW3xRXNIzpFrlFiNfiW8sRy8LfReNjGhM+zMGWzWyQb8F1CqN14EYl7OVHnfhkGFOOQBEJnxvKoHfMVEgTGtNzoKx3dn8Nqu7/xaUMgDRfoiIk13kreaNfx7Hf2mt3I9C7izgobBtLRaPGpxVgRT0xvxxTr3MNF18z311uSlHXHt200Th7BtOtbvMs4CT7blyyVKL25hCvaL+JlOLL3JMIErMiwTctkBxbuLlzinzexOB2UspkOfFIjW/8ChVXPIpB81ibvWA5jeFOYYnvi1qy5SkKRl1eafC9iF88F9ZqT+c0kplHrKKalEgEvKjtKNmG7tOgQzhlyrzv7bHkvCtSZdDI/ZZsVlOzVIszBFnvHCQUk3qXC2enxXrTZVShLDma4tBLI2sE4oYY3ZNdOtuVCGbnd2ifLyBv0RDxo500CDUVP6pWWnl3GP/rVKLm7ER4lyu8aZL9B1vm+wnOo2XJntpDuVnznhovVpb4qrV3l3qUMbvq3jDzvDeSmd7eI1wSs4nO09G7ETk3hjVj0CjQdUapFWwOf2KB3HGlXRLFqkcRmoAQ+Ju+Mh7lXjieJjF9dllm8dcz1jlq5iaoFpCIJVpkq2BkN2VWyVXkFTkXd1XAHKmLRTx0UMVGtV9Y4BQ8ptxH4YWnBWtXkdD6E3nBlDItq+wgzkjzQVg4RpVfxeNv3nOXuRxeHjkei8i4rcsKGfhswqN9CxrYuzrakFUni7+/BNdbvibjckmik7n32jNpHTQpFTZGjkVid2dXeNNzg1OqNuz81W9kQlpvGx0RxEKJe3uhatGrk7Whz+w2vIDLH79a7ye/PY36ijvndkvVwe1t7N6W9mORtJDnJ0hIplTar1mCINXvNMNdk5J2ZHw7SzdS0k8uwN/2KoK5/JwxNTsUb21hlRONdg/MxVeGoRA+Ml6/jkEREHkW65hzD12moNEDjPAqNt+vRn65Xqb3eNeKaQsvDJoeg7o6z14GTLvWak1TSIA7y3aShcb9t/BUXDXc88tBdNvTN0hZ0OsMuXrtW5LV3PPMTvix3JIYNS6g7VL2G0acA5cqVSY5Eyu+VCTIdQZDsKwMcTGC+Lhi1Ho9D1Vob8bKVuh2lMPfcFPdtfl9jWdGfj+oWA+V95CMBiQNlrdr66JkTT5QMrbmxbzYhEl/EURPZm6nqR7cpIMmcdo5a6PdKGtJ2d6Bs8XhmiqS5EbLJd2Jn3nFm9Cp9iEqvGT2RGLKmPjPXqxht6UKhVwf5bOIdTEWtd5ykq5NF1nKloDG0CtkBYpdFbEQ7m+zNe8TIE3lljVsUcRehO92LdHuRxZ2L7C5MOGQn0jxNFbRh4/iuVVzFqLeCCwdOOXfE+XRDBVTYxdfoskzWeExdOEtyQMSmIHRF/bCrjhUtXSECwrfhGpGxNdj8Vf0UN2nBZccaDTWRrNyoZo8s1h6XFtcqo9BclVsrU8cp3CNmWEYnF9+fqLMK3/RzeOryeEqKzLsLUXC0Cvwg1th6N5ixPuqNui+PwXLc8iWVhOyFx+pqTNRBGaNqe8O4QWCFq6ikp6omqnaf5mwRwl7CmN1WGpYRjSJWb+njlh2xcp/s04xHDZUZ2QNNEDeNxxV5PwUq3LNx2l/KUuZGpbHzBHZYqVHTTGFjhthOeVbvjjAr7W3uEDtXzCrP0TrBSf2GbQiBK2631Lta3LnyLBsaWc7PB1eM41N2ZfUhn7i+gP2bFUsSxt4KSbAzhHMKhRWdK++O1UGEdgckkQxif9xZbH/Hg664XTAej03qip3XznW/YrJLSieFXRNULO+8Vq3XxwZTFGXXIHBw2Fj3w13CLdgJEFMtKBotFGW5BkUsXhHIz/GBvNYx6gsTHK4tKqvMovPKWmLNQ3eB2QJUHSiBJuOM0a9w5sYX0Ur2D2pqDjrcn2IsHgV50DYma5x3qmB4WKCwnnkP4ZQ5GqVU1nsKZbWoNDNkh5f4ocQ7esCpazfdYI+LIt0zLk5+vgkqfz/IpXF1mYuS+9kqhm+tenbTmxTaiHHDnFUQ9fxmYITjoNIAknIVQeH1al0wK3nrcE0klFaWLPULEh429eG8v4g5H3h7JFgGOWDzqyZzl5OW3ZW6OTgovU1POXtK8A1PRrequzT8csuSnLrqNKjSxbPZ09QUhztXIKO7QMtMhlcp3EnsOmtH5hglpyavc/28r3qZ6XJpy8a3GGMvku4nhoPcc6hv6a0eN3GSiMGO1bhoSV56crsLyvvdPfR4CPm8RkOHzIQzDbvT3YBJxmlZXGr3mmNYq4VoZpOcE/fHPON5MUXvq6ll+fv1GF+Mo9/zl3uh7wBtmEO7J8J2f4LWacfLqH9Zni5j26R+I5HbgSMVAjqcezjM/FMsMxFBDvYy5C46iedZ3rt8wpItrqotg1N6dVCnVbIq4yOqZ3cLt8ekq3QoFdK0MbAVh0JTVp8QrYG13lpXm32VHUNy04JSGowqCkvdCUYNZsimtEXRvpHHgyV1RSDsK8icWD/VRZGPC4oqQq6SkmPC69x2dOiYQLLiQrLtSqWZYH3qIfHcbcYNKd7t5TU5I7mpcNPSwIbWW+nT4GF94dA9d72N1eWwvl1XOUyPJ+fa3BCdVdDdKcsE9iIerdTmpSVZhEEz5ZUOektud0/i8/bQSpsklQYwz1fWdarCXnRdNSrYA2nLSKnHS146+V30thf2eInUfg+imi6rYc0hZauOu42yPySRxXMhe94Kmyo0ERe/r8VVRoYariagZR6kGhJ2NQG2OJph5Go22nl6q3dEVPPCChuYYhAYHc8vbJm3fBU1Eq5YB8mwXeriOsx0IyTJNOx1Ym69S6ghPIFIyM4ixXVRlS0unpk93in3I5d4KZHrEcAY53K1TBaVD1uGzn10YG+2cbPBbh3Fi26ZeJiTcYW4Nu2tosQTmsibA9jaueQ13GMIt4HZIZNAVy/lW7mSOqzYOb6cCpCWckwp0YEV8n6Hiw2EEDimewzG0fJaOdwpoCgVKOmukB3ZIbxon07B1K12xkU7NCsSkbo4Ot07VQ95bLC1Y2Wd7FOeYA5sY8V4hJUQntAI0yF4uxrZE0JO0bbux423dmzPjNYCfMe8wTTk5YVuEIiw6CxiU+ZmnfcjhcNacgjZlt1INc4IHUQEG46u9dJMurhHacLruDT1OdxO0CNe+TlJXQg2JFe7gD1EK0gtDfvYjeuNZmThLSWMErlMtIexZZfQnLYq3HBvCzXOTTpr7G7yHslrQK3moal7RMwgkBN9l/PbNawqfb6J9xNUYrzOFoKOJ2V/8zGr2uBVsuLu4wqJovKmxCl8hdhxu+JPbAulw+CbYONgnCjZ3dum6uexSQpThWV9rW/X0L320hbxcWwt2MetQvS7ax75u+U5Zcthk1CQGDooGlSq77TBdN+1xDpE9tYyP9UsxKgi0se3pVNPvRhSd37qD/C4uqJXNTIaYz1SBEUmVVGq5Plct7IF2h4Tya9WVotw7yYxx8iXSs8PF0+MnaXf8YnfnLLDhVOhCgr4NiQht8PRCiMsDTuM65RmuZ6DKGjMoWgKR0nzMjdJpAy6K4bIK4apBQmyddvBXPlG1bcl7gwHfSTU/rxUlyKcknXZWDgZs/VwPN3aiiCc/drxSRGh7z2vIWtaFNSDRRrMfdMmKmEsoWUSULEEy24i7amlucQqV9shCNigoEcOi+haa4cbORHHDik0NsW9eKg4jIoEdHV3zjykbWpUTWATIH7oCttSWh3cYcloOkDR2hgAeCsQRa+xvQ772TWfmMF0Vuva55PicMLSkKEYJrqW9MnFnGkjxhJlu6a72/QGlGZOiBy8rcqmk3uTNjfOrZQD2nue5fsZpeMu2A1gkFfuV8ja2R6JbZZRcskJOZZM2nW5cnzQtSsINTj3ehfVCC5lhXc+FqpVLI24hymo3jiKelY92F4LwigJ5xFTBRStw1qdVEjSbVk9IS19DOvCwczxUtANbcNwsItNOcpyUWVLwyscxVccdQkoVCJ3qqqFV+iCnPd9eNzdA9XcupeV11wls3Lj44kZVWND8zgWaZYeHgk252lVcs7w3ch32uqCqgTYV2qllvOJfS8VtRRsVl0CeryokFBbwkUHHci05iOyUHjZX+2ZqdwSVBtUYMSGB/m8H6hiGqdkz2+9pTe1hsEo9LmSYBdBL3cy89Do4gmICJ0oIlVa+eyw+YDTpLFSCBnakbl/lQp7TbqkcISJteXSEcjAg34aR1tL06Dmb0x6MyUKKZL9pg+uZ7GoCxUxZNyhsOteF0LtihrX9YnpfZ8HMKI2dbjreZBJAhz4Y0Cud+VynNbdnjTp+r6dzpnh2BvYMYWhzkUEOdEEqFVyjZRuFFWbdTyqm6JfnwvabXwFddlYKOSuoEgHul/EGw8RB+g4+FmxTSSfh/B7Kuw10MIntCuc5JMt2nTIG5t2qRxvzgFPTn1CETXhwuS999SG9vjI9KCJP/CEh6hBUCQ3VJnUjrfp2qUJZ83zPg2diUwNYHLacW0dBARTyhhEE12vSW0leBua7MoWuqLEWRCN86E8VdBxhEb9cq8axqQmR6eO+5HE6bS2Lq5eYFadKPwpa0jEd2lti62uMH4nV6Y2pbucpYLtFuWUYypfAskvt6YDJ/01vaOccE0PyWki85U2OFSwqxlu35y3SnA7icLZvtLj5uiEGH0He/pe3NyE7SY3qK2yN8D+kqQNS1nqlqbhxK7cGEmsH6ppx4P0MqhyT6+yBvT/UR2QFzG7VOvhwFuwgqfL1vIHC8UU2mPVsDMaTETd27GqQfa2NSUo+wnHLj4eqxMXOUdrR1A+GjDN1Cc7u51kCrTQNKgmp2v6e+LYFCMHoB/e8AHFe3oPel0ktU8KbqNWWyGKFdRL/gTr2e1ab8zDOEzXlPIyOKrN/TYfujUdXTZcP5HHa4mTQ2A2Izz1Zlqd4y5Jgg3WxaBBkXAuoZwTH+x7pk0K3j/X4mVVUlnIlvamVDmaursSNI5xWrTjGvZs9RYepD3KJ9meoekM3wn1iV5W+RrEFcp8ebOXA1wU8kDB+/a8O0KkF6KbC6RQpUK7ZzWWxiNxZ0uGGll04kaZHfagKpdp4J+hxAwPpB5DpHW+HGTfb+/YiXcm2ySuMIfuyGDMu2LHIec7JG/9Ou90z+90vDbKTVHS4CK9YUc7yYb8tIuiqxLaVJAfu7Zy+8kgnWOfa6cBuuzl1qeNEQGpS8YBtjHTmKP3zMXY5gXUu2sny6fgfBXoqfKZkdAoKWynUTly2oXEQymLg3V7bxi+Xdk9H94QUnf2EOiRSmM6HrEAzg1s3VD7K4ygxB0thhW7aSjrSI8htKsAy7nbQ0VE/ZYkR6MPULe/WtflYY0MKGHDq0OndOeePJzZrF459xEL3FPoUevEDRSI8fbqJrfqbnmMS18unLTaEeO0tI4bL9B9Q90XywiH4MYkQE9tcuh9iYh9Z3UYDKx1p4Ec9KXirmpu5TcrvmlJig7XG2S92zT9ZQvaQKTDBQwlE+KC3Y+Qdj7eZIaFZXy5ti9yGXIhBZunY45oZ29T3klC7tY+bTdbjsXI8Ey1NwUJ7Ruvh0S3ofVDKMUZSJOUvg/njcbUJDUgGH6Hlri3RCRaPhwvKH0HtarvfOTmG2OFmnxpY8tzdz2zzlgPh0jsXb0SuktbXFdbjb9TVnQ+q8vloe+FK7XGGcId/LQPZKFHMt1lC9Fa90sY6xK1u1sJip22fmXmQ7bZhEuKt/oJvjYDyzDM394+vH0/En37t97xmk9o/p8dFD3PdL6+uPE40fNt79NjrU//nlp///BWu/Gs1ONQrEm78HV89A9HYh//lfPbWcL4fH3q6/ns81C6tcP5BeO3OPe6pq1HoFL6eH0DzAAYNr+Q2MzvrLrg+/dHk783Blza3vMdDL/+0hZfnoeC8/04n1/P8L34+2X4Oi/88Oa9Xi36ghL4F78uZ5tfLwEAU9H31Tv69tv/BoLHK1gmLgAA -->
