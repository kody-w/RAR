---
name: "rar-cowork-cookbook-teams-update-use-and-track-project-materials"
description: "Summarizes project materials usage from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anyth"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_use_and_track_project_materials", "rar_sha256": "647808c38b60fd01ed22b650cbf7d05d9cbc4caffe2592c5c191ca89811d04e9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
