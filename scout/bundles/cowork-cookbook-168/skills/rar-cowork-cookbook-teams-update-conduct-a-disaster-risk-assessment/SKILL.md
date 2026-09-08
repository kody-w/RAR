---
name: "rar-cowork-cookbook-teams-update-conduct-a-disaster-risk-assessment"
description: "Summarizes disaster risk assessment status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_a_disaster_risk_assessment", "rar_sha256": "7a7baeea6fa357a26087d0d0c5195d9affed0b67165f2ac74caa261b1908ee70", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_a_disaster_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_a_disaster_risk_assessment_agent.py` and in the RCI capsule.

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

Conduct a disaster risk assessment Teams Channel Update — Summarizes disaster risk assessment status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-a-disaster-risk-assessment
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-conduct-a-disaster-risk-assessment-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_a_disaster_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 7a7baeea6fa357a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_a_disaster_risk_assessment_agent.py` first:

```bash
python3 teams_update_conduct_a_disaster_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_a_disaster_risk_assessment_agent.py   # or on stdin
python3 teams_update_conduct_a_disaster_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a disaster risk assessment Teams Channel Update — Summarizes disaster risk assessment status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-a-disaster-risk-assessment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_a_disaster_risk_assessment',
    "version": '3.0.3',
    "display_name": 'Conduct a disaster risk assessment Teams Channel Update',
    "description": 'Summarizes disaster risk assessment status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.',
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
        "upstream_slug": 'teams-update-conduct-a-disaster-risk-assessment',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-a-disaster-risk-assessment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8abcdd6f2f59f475',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/conduct-a-disaster-risk-assessment'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-conduct-a-disaster-risk-assessment', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-conduct-a-disaster-risk-assessment-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of conduct a disaster risk assessment. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-conduct-a-disaster-risk-assessment-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct a disaster risk assessment, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes disaster risk assessment status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post.', 'example_request': "Draft a Teams update on our disaster risk assessment status in D365 for USMF, with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-conduct-a-disaster-risk-assessment-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on disaster risk assessment status pulled from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConductADisasterRiskAssessment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductADisasterRiskAssessment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-conduct-a-disaster-risk-assessment-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateConductADisasterRiskAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
