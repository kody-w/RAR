---
name: "rar-cowork-cookbook-teams-update-retire-assets"
description: "Summarizes retire-assets status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_retire_assets", "rar_sha256": "805b85051bfb11e7bfd1015258429b94fd0061256eef013c2e1a8720addee368", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_retire_assets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_retire_assets_agent.py` and in the RCI capsule.

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

Retire assets Teams Channel Update — Summarizes retire-assets status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-retire-assets
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-retire-assets-2026-05-24-card.json.",
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
      "description": "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_retire_assets_agent.py` and embedded as the fenced Python below (sha256 805b85051bfb11e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_retire_assets_agent.py` first:

```bash
python3 teams_update_retire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_retire_assets_agent.py   # or on stdin
python3 teams_update_retire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire assets Teams Channel Update — Summarizes retire-assets status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-retire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_retire_assets',
    "version": '3.0.3',
    "display_name": 'Retire assets Teams Channel Update',
    "description": 'Summarizes retire-assets status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-retire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-retire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '348f0c661244a8ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/retire-assets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-retire-assets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-retire-assets-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'quick_actions': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of retire assets. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-retire-assets-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads retire assets, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes retire-assets status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams post and Adaptive Card on retire assets status for legal entity USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-retire-assets-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update on retire assets status in Dynamics 365 F&SCM, with an Adaptive Card artifact saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateRetireAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRetireAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-retire-assets-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}},
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
    print(TeamsUpdateRetireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916V7PiWLbmX2HOfciqS+aRA5ns6IiRAYG8hCRAlRVZ8t4gB6Ju/ffZgpOmurN6uiPmaSgDkvZefn1rrbP1+4s79Endvnx8OYRuteDdokiTsF24VbBg62vd5uCrzj3w38Kvq75NvaGv2+7l/UsQdn6bNn1aV/P2oSzdNr2H3aIN+7QNP7hdF/bdouvdfugWUVuXiz4JF9xUuWXqdwsMXy82hrZoiiFOq0VUA66LOB3DalGEsVsswqpP++khCiA5tFUHFgAmeVBfq4UZumW38BO3qsJi0dRdP1Oal3TuGAYLOnCBbGO4YN02WAgHVVlc0z5ZiNq+e9C8DKmff3D9WYEF0Kqvq+5vi6ruk7SKF2n3oBkGr0DV8OaWTRF2Lx9/+fX9Swp+v3z8/cUvgIpA9YckVhO4fWg8VKcfmoN9hVvFYEEzARtX4LoJW6BmCW4FYbR4u/qpC4vo/eK//zu/um3c/fzxU7V4+3x6mf8xhuphub52Z4EWvtu4XloA27wu6OLqTt139umAi6r49bnzG6W6Wfx9fvbTk8lrHPY/fXqpgQjurP+nl58XwP6fXtph/v06U2l++vm1qK9h+9PP3+h0g5eFfj8TA1K/fn67fiMLFn5bmkaLzwdtw77xakM/bUJA/Dv95s9T9Ddybyb5/Fz8U928X/yY8qzP34G8zyD0AN0fkwU2ADtfXrM6rX5649HWIMbcyg9/+vmvyPpJ6OdF2vX/Ft1fnoST0A2Atd5M8vP7h/t+XSzfdPtK86/ZNiBg/hNNwPIv7L4a6q9oPzz7D6SLtAL5+sWXPyT3ow3Lvy9++Uvd/tWG94vo0wsXFiAtW9crwo+L3x8h8su74NvNd7/+AUj/X8kc6qH1HxQ+l26VRmHXf/78y7vucfvdr7+8GxoQxSA1Pw9t8SOaP7Lrg8+fLPi26qc/7wX8rSqvZhz6mkOL3+vmf7V/vC5st0iDb/e7j4vvM3H+LBezEl+YPk3wXTZ2QNbv7Pjzyx8AdCqgzfAAqxlz/uu/FnLqt3VXR/3i4NdDvwAO7tMynIU3EwBf4N8ZNdoQ2LVLgWHf1oH4nz08S1xHi9/+t/+A+Q/+G8xD/Qxnn4cHnn1+YvnnJ5b/9rowAcW6TQFgA4A2aE37VLkxAOoHXrZhF7Yz9npTH34Aifxh/rEA4P7bXxP9/Nj/2ky/PVA5fWKdwe5nnOuGInydNTomoCw85fdBnQpvoT8A0kXtAzmiFGDze6BpVxcA8PtZ+y5Pi2IRAD4+qFdvVWSoPs7EfvvtN8/tkk/VE5ixxbOQdRBY8FWcxYcPQKGoSOOk/1SFflIv3v3+x7vF/yz+1a4H8ZmHBrR7sz+Q8FF+QD4NJVgGXAOcCcDiYf/f/3gzKyBTgcoLvJVGafjcDOIxD4MvNj7s6A/oGl94IbAtsGvZ1G3/KFb962IfLb7KC5jOj+Z6kMyFMQibsArCyp8AVReo89WSoNyBetmnXTS9Xwxd+OD6m9e6DxFLkNhu/9tCZjVQfeoC/G8W87EIbK6rFJj/awQ87wMi7btuwXwh8bpQ5ghcNG7rNknrvvGI3Kdf5qr/th0QdxdVeP1UzRU2nE31SIenecAiYBn/zaUfZp+DjgQ0HVXQfeH9WOPONdJ81Mr2U9W9hbrbzq7wAfQDpvGQBnMB+NtbSHVJPRTBw35A0pnSmxeCN688YvBZ3Bdvfc2z/2Df+o9n+V98GlAYWS3+/22GZjvQPG9seNrccIuNYhrnp3/m7nD247OhnGWdlXjk4reG5QsofcHmT1WRgmBrp789Vz68+rbmiXdDC8Q3aONBH4QU8M9M9xHxcwS37Zwr7qfqSxF4D5R+IB5QBMADSJ85ar8wnJ9+kTQBGDBff2sIHhECDAQsAqJ60QxeASIuCsPAc/0cSNXOWfvmZBD+4ZzB1yT1kz9pNTsLRBmgvwBCpMDvwEevX4H5+fSL6H/a+Ox75i2PnnAASds+CAA5wlnA2Vez54B4/bMZB3p+fBABapRNP+vugbQBmj5vhm0InNul/QyRT7uGDQDmD/P3U9P5bnhrQKYAY4F8aAZg3UcGzc4vQVcDZAAgAhKqTCtQ5YFR3ozwIOiWMxwAuH2LzCfFx+03hcJH2s3l6cvGWZF5z1zxn/ngVtP3qGH+KEwAvXJe8eD7j5H2ldtMe0bODqAf4Pjl6bM1eH1W92f7sPhC9+M/TTs//WcD0aNeW38OgI+LpO+b7iMEPWvslxL7CnALesraPcvth2dl/PAntPgTxaeyHxf/mVR/IvGWFR8XyCv8Cs+PpLeoevsAI7AfmPOH1fx0xrtveArY1yUIq9llE6jvX4vflyWgAsYtQCqw+FkMu7mGXkHZfqA/sP+n6vswn9Nsxqt4Dsuu/i79H13AjJVPD30pUuBR1QPewdwnxuE8lj2SogtfPlZDUbx/AVAa/stxbC5B5RzF3Ty+gXwBDVefho8rkI7B55n/k8rv/zDebt+efA2mf0bU94vwNX5d/LU/P6Awin+A1x/Q1YeZ3WvWgeIG5OqnZhb8ObrNzd4DoW79P4uhPn64xeuCCwEaFt33Yf9WxeYq/l12Pm0NbOwDdd8vZrG6ueoCXWdLzJntdiBVgGI/lOVRfj4/y88/C8TNhetPFQqAbfel/L2ZxDrI2x/S/trx/jPhI2g8ZlpB/XGuwe/f4A18gynl/eLrwAE0ehsBH4N6NYDp+pd52Jn9/dgy/wB7wNfXTV//euGFL7/+QK5HNfzsfum2/1E2/QfFcpY1rfxiAGBZf+mQZrs/LPDOTsPrjKDAZ+/eL96poB+bm5bZfO9+YBogwwO2QfGb1flmp2/S1o85bZYWaNc//6zw+wsIbxe42H0L8LdGHywHKPehm5sdCGQ/YAiun3kKnv0HI8Dbzi5xQSMKtpLw2iPX8BrxIg9BQsKLAgRG1uiaXKGUR62iAIZxBKwNwwhGMB8NEZckUNgNgjDEcBLQe+b557mXS2dpZlGAET4AqAi/PQa3gjc1nmLPNvo6cczqvmnz+4uHr8DK3arb088PC1GIB2GSZzTSsoLJW4J3eC51Oc4lqlt3yxN8PBKCOSJ1pfqtaMOtVO9NOt+cN7QcK+f1pbF6fXkziUTrCgjjNjTNsCdnCA10tRYkgeNMmJKhcblyQmeFhaIqHtkuyWx+uzkubYxpbkOzbS6JdDsZhKAD/Icge1xdJN+7HFUIF2WYu2Wr0j3riVtsDkPgWcebFQpdQTb9jmlvSyeIUiYY7/kxLNRutXV7mZ2qI3ka7DQ/9M5BsI6duTW7GN43YmHGMH8W+FaUenV3CJPVZGrmhrfcfWoQiJWbqehscbo0Af/bjooibVCGPS5lURqRSMi70dq6DTvb2DvbSrTTo+Fsi+ZS7TtUNJ1pMI7Tuakv7DXkchyHolHL8LWKSjK0S0siGKM42xzRa35X9qxEN8626eUNHsKMf+Xtu3ia7mniQAk/TOu7hSZXbZOljePgFKWrJ/koXGon1pkiLZccdfdzT0ghYM685G8hE26PdKecbwZ73R3XFS+iR1E2PfJUFlwJpxNJX+4pfguzfn2MeDxHAw478aHeWTeO8XieP+ucq9+v4/Za+ofkeMhtibdxRkDY/VEqmiK9GK1vIkK8wtoI1fPxoLp0d91stAimkQ3VOKhDUbYmheU5tFb23WAEd7iJirJ3nZW6TQ43I6nTSEdyK4zPeLfhHfjKQTx0jzOXKjZHWQouu0Pa14h82MqlXJlrWyvaToDCcw/nGrK3/aRnL1PXJRKr2b2QIwzbQ2KqxUZ+uFhY5zSZ7CfEGhemAwxLjZrLnc1AgdEbZz6pdIZDkuU+utVjQdFXnqDkYCmuk7xlYMV1LcW/6Hwv0VgmtAVmi7ddI2zwMVOS/CgiuEsIh+R6mbZLkdVWFxHPJ9/pQ2fsxJHgLwKECqv6qF/G2IFI3WWFVRvsjzoqaYlc3rZ11EfH5ebWpeke65Y5vN6XSXkLN+jJufDmyYyrG2xVolVKJqs3aoyFiRwxN83UW5U+emm3ZAySTkYINK+ThnL0ZlXdseVZk7cSIx2QuOiFLt531RFJDPfQVHY2JHSBVExQHmPEmTTb3d+aRObWKT55+wCiuVF2U0ELGBj3hHKK89bP92bgXMEoqqJeZG/ya2a4usFcoAOd97t0a+BciKxZqeRurjARpM1qjIzR1GXjkHvlLqsea0GSJpBXFdE6lBkB5qUtW0JUi994obHFlqmPdgxLl5W7tc/a2GQ1Aw93be9L2mUZGJ4mbIjkbOPRYOomYh7tDX5poYDaMj26rW8EdMwIKXVPZIpcw5ukwXi2SVzkuI67lcdV2eoISTQyxeZGMiRSH5elw51N+OIW8TJdcz5NFluqZBUhdqLkUm2VwtpKvUHtYGWPBZKxISYWTpb1yRzuN6Ta++4oE2g2mqcSEe6QvWnE4NyldnuD+K1KpoVtjWFEt4LtXDSdIk5MCHJuAKlhbpSSqao+ym1EKyhpU58s9H7FqADbhgKO0ONOdrjTwFW307jimasqIK28C8/OwB5MqkhWJ1xFGRdWNzkst1xoXI+dLFQ0Qu7bXHBu5zIfAG4Iolxs0S1sqEKQe1fvjuTHfh/oBk1CEV6ICrWEuuXGlltoUkvosltNFwynEu1OJgfhbl6zJvOrrSk46C4+ceYYitxQnTzIHYMq3hJsZmab2ruuU4Fnukis66rSlrBdRHV0MNC6ChwRh/ga3m3bNSsWo8fj/ZXZd6vRsDSNYs7M5qYwQ+Pp6WnLOV3Dx3S+3ioUUm2a0cSRYKT1LN1Fgr5x2/2BPGOctJQHh+XP51TRGFyzDmoQH50g3TJspAh3deLLjZSgbLyJzX65NlGedAX/MsQK23Varzixdm0r93zdyPFlo3NS1CmSu7yFbZETRrMZJEvyFc0sRjBoTYYHEnBratAKH82tcvNHUXLq5EBbe+reazV8Ye7Vem8Nd0Lnt7th4Hq/aBSTWMEHjsZMrwNRDKlqTi197WJFWVGsSSoahQ1UbkAuouuDvQryqiqT1b5n1Y3UpRbE3P3ROe4tJtiu+nPLyWmBQsP1ukod3ULRiMXYrXwmIy1aT2QcQxXF771zQQIjCCqa6r1V6kkRGGG9rzUXuMiQmfX5sL1fGL3CxP3hypr7prfYIxfym3S97tLVJeqoyfZUyw36fo3e1a4st4Wdklxn3BRSE0/n9WD7mU0dl2D0THWcwkMpbt2aZeMzJ9vONe/3uaetjKG7YFppnVa5zB8ozHU9LyjYMqvy5nQ93quIuOhHQj0qHiZT7K06nCa2NehOkocrSvQeR9iZrx/2ZVFRInGRb8zteNImLGJXgwbxjju66GHfWHrM+9tO2R0pwS4S/VAyvG5LqNKneb5f4iPNnWtbzDE+4WN/OB4Flz5aZSHu5bIpN5OxbLNwotX4crmkU9blji4nPr1kVhBzoe32ekgPd9NXtfoa1fe1eCVN4ExpVU9pJt9aj9Pt7bRJ+eVeIdw62Jyu1MGR1B3HOARP16Rxy84cNoIBVCxyvSz6g8M7mb/ryppJ2eiuNsZGy681JqHSkeT5gcrKogZ96NkrXPKYnAWIuqpMLOtVtPVBA+PsLzRj5QfybipBqkYwvj+EnHLYWexWGWU8lYtd5MgniZN3WBK4td+kB9s3lqA8qaazdVPfYpFDqEMUd7zFOnsrRQnbWKgSXLTmRMKCSBsio9XIcie56Z63meVNPHakHRBnahp5EGJ+bdxxPL1IQaO1ot6vzuegHZYIXdHpSTyI+gUHUyc8LtWmUzhCqau9dFgNEnkLy8JZBQSJhxs8wbJ8um1bEKL0qjqu8RWXBU2eu8Pu7Eh7tM1Z/dj4ukAybH7fSjziSJMk6i3DuwJe2hKsKGMRX7c3nQhtiTvczjeTP91CvuAYpt9yyOhogjOshPXSIE8NvtxybNWh411pTrDKXZWwCV0n6TbmaJ6N9WRX1aHeb5hE5andypvgla5ZotlNHdbc2owyAvpIC2nqXtu9cTGFGlJYpeZu+B25n5gzrWFmUEHYGinOXl7oWLAO+UsyaTpo8GDUPvpuT4tqveME27rW1aBz8MYRfGlp3aGT3pKkI5wF3z5boqiX9WULw3tDzPvD3kw4fYjbpDt5DSyapymX4dvExNK5PvoZ5yFwhQ49ppytPb5le5dRBUIWMg+L7ts1xBsse2cO52AV3C/sdhws95iCNZJ27YNcpGu9tRwr3lNuAOB5opkLv5GZMyw2Vw5GpkQlXbfaCj563HsILqZoeVqjMaW0BQhPuPYu7YSFWDOsxpOE5ahN5lIJOXurJyCqMRWD3apXXN9onWOuGhHF0WyNkdHlWCTdvXYDC0eP3YAR8Snw4iugyaL31mq8xHTalsVNjBzyQIrDsPYw1YSJCdfAZJ/XdpQOlkNnHBfviqMYWOJOqMwxhWGhY0veWoNC38ZicmtoXLkpe41tODbVLKXBaIsNdcng2cnyYkxzyvrswxi3o9uYW177doBwVbOVUj9K8X1LSJWi1nYxkpXRNsS570kCP+kYFvLCrj85oJ4PbuT2RT7B2i70REwp7AZI4uxvIdJh4a1kAiOL2b0R7f0D4yD1ivSF0p+GFofhdteoNdksd/lSruM6s/crDsVP+E7DdXrjCqZ3DwUtiUoxSAfRTDuXDNYnKl9pdMMXk9mL6U5xV7i7YuOejlZ3LalPcCdPhrYLiC5tVTDcEUndI8haNisuiH2yb3YC269pwjy2YYFtRPzO1Tro81yRtofljc46BiH6zmgnUb42njGpGS6NXqzrpw6ycMu7LiWPkw4xtjmTmYdKnsa6E1zt2yt6HwkhSHhiutHFQdpW8bgxBAJJAPS7pxHy6+PK0zky3UmcUQRnLnXbVLrQPkpwjSEUjh4LB825RMS0I/S+aiCDTCl4c3ZE2/LYfnTXAcuI9Smmt0aSEzyUsDe+8STJ0lFeUrDAE/GxpWrneOsj19GXnFfvx4k5XUf1ANNdKpAmIZKKII8QgLnEqCK7U5CRiqAsCgjxzEmes9alG7rdiqOlUvIBoLSSG5pNtWKMgeZQ0pGOShnSt9xx5EFXThPCsacyaFWYpXi4Fcd+t2SWp2vab+Drnj3JCDpp+JQDH9YrFA7HbDWu/HMWnLxQdY8j09px3uCnM4tPvZEx0JRSeABrcho4nZ5y8XRlbiPoT9Rd4VNGPXFLLpE6VD2e25Q6XQPHUeHALx3vMIA+H9UucBqEdB6vdFASXNCX3HwsVh0PYnD+Lq7PS/p07jdSAy8lPxt24hIvQfLW+8GN7Zrui3VFBIUpVZ0adBLOD0QbbkM/XOO70nNsWcQlb+fvJc2r6DWCmj4DCjoSxBvPxvD7CjrI3fKsZNKZ9exajdVM7Nwz4bX3cQcG5mzyR3TCCswZxlV7V2+kuyIyuBvUeoO1lmovM8xenXS2bDfDGO0SVha9QxKhplpefW2wa6S1FYJVwAjBREcEu8rdeApHxFfkBgBwKQ2FU7MEt8QzKI1qeM8khXy/oLxKagbCydnGDspSGduMxZamD3odykW08IqySBqtjzK8PGV9Fx4x0MfdRDAaH1jC7NVz6PUYxEhcgqvx1nK7jAi5a5nF5eUGQVQfkQcZFbtKCIb7KVqVkdEzsB7giHlZDo2Ne8ZI5zuCOqig34d3Slbrk3Y1DApk2x2qdVbVdJywnUGcWBk0C9zhfqdJdrvPumzUeNLKOeK+cmNEsgmn9GRua3e5S5GqGlMeeqQ5mua3aAWv78ko+/Y+uw1Xj4ulMMJdZ5B2PbIh0JJaHuJQF/BGgsh2/twumyFilgeYjC9RoCTFdA6nc6Ntxf11A23W0V0bSkK4QH23q+5HO/AV9e7IyK7Ft8zU73C/GC4n5Aym6ZS5D5f6mvAGnQ4mc0WXlGUHaFDdOJM56GjRthvbYc3DcNie+rI9DtU6KhNLRVeH+KhiF/a2M4dpNJbEBHAo2/h8VDbVnQDzRadJxSHacCdvcyjEfJ/3qZbFE+Tc1c1FOYg3ruZ9DV71PY0xrBXsjCwk7wrC7FjeI5XqkF9XuVFv1iSi1FNAclYjrooMvedyxWH0WT0Gm1VybwSCGk53GNd22X4GwlVbgjlKIegtfRoQRaZNJAQwXXlFxiUOHAoJZp5Pa+/eWAWAnlReKiNkqHrWHFfN4FHjIam9XpINH6sd5Y7u6JtKid593fPHYFmqFntSa2PdR7w7LEFA3M2TbnelgiPrKJFjq9OdcSBlX/IpkicsYL9TrJO7XEAFcUnB0S08cSuj7H0PZe59fB96mV8SmhLWQuaqqtL1BBxO2pnqD2uOs9TdPfd3piOD2co5Lx37yu/x+IK7Zt8STHzUtdUZErIt7tGlnNQKUfGWjvDUIdWQq21dgtryUFqRQ4z0WKODSsVd8ualbe7HkaXgdUvUtJi16NkhI3NAJqLfFuU6dZSrf+qkvDF72CXq7L6zboSlpZZs9x4B2Yqw20GZfcNQu9CtFTV4ibLipBbmtcg4SZerCGwTkuSNCVy6WRfGEnbPA0F4YLrfbVyVd1fIHVmnKnCSepJDZaDEACWRnW8byHWpZTk2bXWxzu0DP1WpafOUS/Ce7zKiOlXrxqFwfr9qSG17jxmUbItyd0UMZ4f6UZJsFPdUXWxWjlZgzEtrEvWZJKnXcGwxR+icp4GASE3rx5OqNhy0Ow/y8spGRdP2m6DFBHJ3jiTpqEzDet+dWwESByptRy8k2J0Xi3BxTapVs94cVItwdj4XXVIINZSMo1RjF1oDGIxxNrj2EFVSsOfaS+dYUiqbE+EVzPjQgcqM/eAFx0QbOZodtyU1lN7RWp+xomqOsHdBL4GGB6p4QLkgJJKS1Qiyz+RjrbpCJrvUAZY5lUBK08sQeliGm6oMa8i11FOEyyNVHnKxXjly1kkRMzo9jVAUo5lo2h0NKNMZROGmkjmQ62tNiuXax9ficKjCxNFPCe/d7mAe95nMzzLQki9tr7pIvWdCwaY0Nfw4aZe6g66tvQp9wLrsND6CS8e20Gw/ifcb09BLgCtXNuw4pt0xWjRGyxOVWisd55crnG5Dzk38Pl65XOsFJ7G5y7sT5qfjeNte1+Je29mQDXpUtVfXIbxGaM1Sr+2QhYGgHAyHG7lrDGc65e4lDKvcTFvC5Z29H7rxPMpcTh1xY0JHEIX5+SxF+eGAyjRsAbuhQ4dv8zhyTwJJXV1UveH0TqBv00TKe2MvIVldxiFIhP7KxbCIMSSsTqbXrXvYR6/rq+ZHadx02snlz2ucaAIPpiEmu7jS2cUNCAw20THcntahcYIx0rGxvl3CHU7i5TrKQF5F+J1gIo8gR6+vLFGBXJLr1WsJ5mlcKa+kUIIurNuOXmP7zdaaTxta39FKyA2zIVxXGzharSFxUgKntVtGW0UtjWE45Hv23XPxzXqdnNIT7iRExJ5pVIQA3DDcTqlS6zR6Nooz2LkPcOe29/ehADHGOT+ydMFiZFn6Qh+LqSwAMNO3h5OjNKByS8PFBbV+y97yVVbVSUUOsWdxbiyKXDJFxX5ip9JBiMnAOEOP4GUy/00lxQgKQiTK5fQaut1NLDPbcFUsvVuz2+8aV0ZOAxUyVVjc98Fm0Mpgq9Zp08CMZ1b5/Qq1ZR0VGLZUl5weB0u6Mytox2KYIQwK3J0YcXWnnB0DSu+dFi9DoksQJy+HoiZp8qS5uVLmG5qm//73l/cv3449X/6N97TmM5n/Z8c/z1OcL+9fPI7uQjf4+OD18d8R5tf3L62fAlGex1pdMcRvx0T/cKj14a8PZud90/N1py8Hr88T5d6N53d+X9IqGLq+nT53dfF44wLs8IZuflmwm98n9cH39+eN3wsOLl3/cZT3ua8/B2nX1N18M63m1ynCIH2umS/jt0O+9y/B23tBnzF8/Tlsm1nNt+N7oB32Cr9iL3/8H4onmui9LQAA -->
