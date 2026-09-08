---
name: "rar-cowork-cookbook-teams-update-perform-license-requirements-analysis"
description: "Summarizes license requirements analysis status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_perform_license_requirements_analysis", "rar_sha256": "2f4cf2db80c4ece722415ac8340de3f6802bc836e0817aa9e1bdff083bf4ac82", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_perform_license_requirements_analysis`. The original RAPP
agent is preserved byte-for-byte in `teams_update_perform_license_requirements_analysis_agent.py` and in the RCI capsule.

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

Perform license requirements analysis Teams Channel Update — Summarizes license requirements analysis status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-perform-license-requirements-analysis
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-perform-license-requirements-analysis-2026-05-24-card.json",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to analyze, e.g. USMF",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_perform_license_requirements_analysis_agent.py` and embedded as the fenced Python below (sha256 2f4cf2db80c4ece7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_perform_license_requirements_analysis_agent.py` first:

```bash
python3 teams_update_perform_license_requirements_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_perform_license_requirements_analysis_agent.py   # or on stdin
python3 teams_update_perform_license_requirements_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform license requirements analysis Teams Channel Update — Summarizes license requirements analysis status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-perform-license-requirements-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_perform_license_requirements_analysis',
    "version": '3.0.3',
    "display_name": 'Perform license requirements analysis Teams Channel Update',
    "description": 'Summarizes license requirements analysis status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; does not post anything.',
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
        "upstream_slug": 'teams-update-perform-license-requirements-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-perform-license-requirements-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47e65aedf84bd52e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/perform-license-requirements-analysis'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-perform-license-requirements-analysis', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-perform-license-requirements-analysis-2026-05-24-card.json', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of perform license requirements analysis. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-perform-license-requirements-analysis-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads perform license requirements analysis, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes license requirements analysis status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; does not post anything.', 'example_request': "Draft a Teams update on license requirements analysis for USMF with an Adaptive Card - save it, don't post.", 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-perform-license-requirements-analysis-2026-05-24-card.json', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update with KPI Adaptive Card on license requirements analysis status from D365 F&SCM, saved for review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdatePerformLicenseRequirementsAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePerformLicenseRequirementsAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-perform-license-requirements-analysis-2026-05-24-card.json', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdatePerformLicenseRequirementsAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
