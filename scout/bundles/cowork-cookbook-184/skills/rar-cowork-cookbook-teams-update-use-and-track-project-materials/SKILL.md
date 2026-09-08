---
name: "rar-cowork-cookbook-teams-update-use-and-track-project-materials"
description: "Summarizes project materials usage from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyth"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_use_and_track_project_materials", "rar_sha256": "647808c38b60fd01ed22b650cbf7d05d9cbc4caffe2592c5c191ca89811d04e9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_use_and_track_project_materials`. The original RAPP
agent is preserved byte-for-byte in `teams_update_use_and_track_project_materials_agent.py` and in the RCI capsule.

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

Use and track project materials Teams Channel Update — Summarizes project materials usage from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyth

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-use-and-track-project-materials
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-use-and-track-project-materials-2026-05-24-card.json.",
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
    "output_location": {
      "description": "Where artifacts are saved, e.g. Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_use_and_track_project_materials_agent.py` and embedded as the fenced Python below (sha256 647808c38b60fd01…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_use_and_track_project_materials_agent.py` first:

```bash
python3 teams_update_use_and_track_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_use_and_track_project_materials_agent.py   # or on stdin
python3 teams_update_use_and_track_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use and track project materials Teams Channel Update — Summarizes project materials usage from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyth

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-use-and-track-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_use_and_track_project_materials',
    "version": '3.0.3',
    "display_name": 'Use and track project materials Teams Channel Update',
    "description": 'Summarizes project materials usage from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyth',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-use-and-track-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-use-and-track-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb86cc0a27277708',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/use-and-track-project-materials'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-use-and-track-project-materials', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-use-and-track-project-materials-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_location': 'Where artifacts are saved, e.g. Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of use and track project materials. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-use-and-track-project-materials-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads use and track project materials, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes project materials usage from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyth', 'example_request': "Draft a Teams update on project materials use and tracking for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-use-and-track-project-materials-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Where artifacts are saved, e.g. Documents/Cowork/output/ in OneDrive.', 'name': 'output_location'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on project materials use and tracking from D365 ERP data, saved as files rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateUseAndTrackProjectMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateUseAndTrackProjectMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-use-and-track-project-materials-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_location': {'description': 'Where artifacts are saved, e.g. Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(TeamsUpdateUseAndTrackProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
