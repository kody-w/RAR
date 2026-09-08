---
name: "rar-cowork-cookbook-teams-update-analyze-maintenance-costs"
description: "Summarizes maintenance cost status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_maintenance_costs", "rar_sha256": "4562e5ec6e548cdb551ae16c1a942e67f7d4dac86d57b18bb461d5b2e651a6bc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_maintenance_costs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_maintenance_costs_agent.py` and in the RCI capsule.

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

Analyze maintenance costs Teams Channel Update — Summarizes maintenance cost status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-analyze-maintenance-costs-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to analyze, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_maintenance_costs_agent.py` and embedded as the fenced Python below (sha256 4562e5ec6e548cdb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_maintenance_costs_agent.py` first:

```bash
python3 teams_update_analyze_maintenance_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_maintenance_costs_agent.py   # or on stdin
python3 teams_update_analyze_maintenance_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze maintenance costs Teams Channel Update — Summarizes maintenance cost status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_maintenance_costs',
    "version": '3.0.3',
    "display_name": 'Analyze maintenance costs Teams Channel Update',
    "description": 'Summarizes maintenance cost status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.',
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
        "upstream_slug": 'teams-update-analyze-maintenance-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc9f362c3f48c6a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-maintenance-costs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-analyze-maintenance-costs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-analyze-maintenance-costs-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of analyze maintenance costs. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-analyze-maintenance-costs-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads analyze maintenance costs, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes maintenance cost status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.', 'example_request': 'Draft a Teams update on maintenance costs for USMF and save the Adaptive Card for me to review.', 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-analyze-maintenance-costs-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on maintenance costs from D365 ERP data, saved as files rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAnalyzeMaintenanceCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeMaintenanceCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-analyze-maintenance-costs-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateAnalyzeMaintenanceCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
