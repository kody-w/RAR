---
name: "rar-cowork-cookbook-teams-update-perform-license-requirements-analysis"
description: "Summarizes license requirements analysis status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_perform_license_requirements_analysis", "rar_sha256": "2f4cf2db80c4ece722415ac8340de3f6802bc836e0817aa9e1bdff083bf4ac82", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
