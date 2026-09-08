---
name: "rar-cowork-cookbook-teams-update-conduct-root-cause-analysis"
description: "Summarizes conduct root cause analysis state from the Dynamics 365 ERP plugin for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_root_cause_analysis", "rar_sha256": "1d7b1f787c408ed143a0c43294d46da3de308c4661a14999412b52f290d6579c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
