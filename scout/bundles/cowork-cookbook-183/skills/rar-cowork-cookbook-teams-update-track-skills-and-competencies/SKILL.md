---
name: "rar-cowork-cookbook-teams-update-track-skills-and-competencies"
description: "Summarizes track skills and competencies from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons for review;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_track_skills_and_competencies", "rar_sha256": "b495bc4b8606d0c67d86226ee47ead9f9c732d56d8abbac7bab8fb4d61933c6f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_track_skills_and_competencies`. The original RAPP
agent is preserved byte-for-byte in `teams_update_track_skills_and_competencies_agent.py` and in the RCI capsule.

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

Track skills and competencies Teams Channel Update — Summarizes track skills and competencies from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons for review;

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-track-skills-and-competencies
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-track-skills-and-competencies-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_track_skills_and_competencies_agent.py` and embedded as the fenced Python below (sha256 b495bc4b8606d0c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_track_skills_and_competencies_agent.py` first:

```bash
python3 teams_update_track_skills_and_competencies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_track_skills_and_competencies_agent.py   # or on stdin
python3 teams_update_track_skills_and_competencies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track skills and competencies Teams Channel Update — Summarizes track skills and competencies from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons for review;

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-track-skills-and-competencies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_track_skills_and_competencies',
    "version": '3.0.3',
    "display_name": 'Track skills and competencies Teams Channel Update',
    "description": 'Summarizes track skills and competencies from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons for review;',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-track-skills-and-competencies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-track-skills-and-competencies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e65c1b68d2b99ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/track-skills-and-competencies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-track-skills-and-competencies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-track-skills-and-competencies-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of track skills and competencies. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-track-skills-and-competencies-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track skills and competencies, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes track skills and competencies from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons for review;', 'example_request': "Draft a Teams update on track skills and competencies for USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-track-skills-and-competencies-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on track skills and competencies status from D365 ERP data, saved as artifacts rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateTrackSkillsAndCompetencies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTrackSkillsAndCompetencies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-track-skills-and-competencies-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateTrackSkillsAndCompetencies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
