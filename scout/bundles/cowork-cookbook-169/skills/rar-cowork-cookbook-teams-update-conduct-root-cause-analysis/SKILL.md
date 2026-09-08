---
name: "rar-cowork-cookbook-teams-update-conduct-root-cause-analysis"
description: "Summarizes conduct root cause analysis state from the Dynamics 365 ERP plugin for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_root_cause_analysis", "rar_sha256": "1d7b1f787c408ed143a0c43294d46da3de308c4661a14999412b52f290d6579c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_root_cause_analysis`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_root_cause_analysis_agent.py` and in the RCI capsule.

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

Conduct root cause analysis Teams Channel Update — Summarizes conduct root cause analysis state from the Dynamics 365 ERP plugin for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-root-cause-analysis
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-root-cause-analysis-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_root_cause_analysis_agent.py` and embedded as the fenced Python below (sha256 1d7b1f787c408ed1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_root_cause_analysis_agent.py` first:

```bash
python3 teams_update_conduct_root_cause_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_root_cause_analysis_agent.py   # or on stdin
python3 teams_update_conduct_root_cause_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct root cause analysis Teams Channel Update — Summarizes conduct root cause analysis state from the Dynamics 365 ERP plugin for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-root-cause-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_root_cause_analysis',
    "version": '3.0.3',
    "display_name": 'Conduct root cause analysis Teams Channel Update',
    "description": 'Summarizes conduct root cause analysis state from the Dynamics 365 ERP plugin for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing',
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
        "upstream_slug": 'teams-update-conduct-root-cause-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-root-cause-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f8e6aa44d0c458a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/conduct-root-cause-analysis'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-conduct-root-cause-analysis', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-root-cause-analysis-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of conduct root cause analysis. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-conduct-root-cause-analysis-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct root cause analysis, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes conduct root cause analysis state from the Dynamics 365 ERP plugin for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing', 'example_request': "Draft a Teams update on conduct root cause analysis for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-root-cause-analysis-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update on conduct root cause analysis status from D365 F&SCM, with an Adaptive Card saved for review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConductRootCauseAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductRootCauseAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-conduct-root-cause-analysis-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateConductRootCauseAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
