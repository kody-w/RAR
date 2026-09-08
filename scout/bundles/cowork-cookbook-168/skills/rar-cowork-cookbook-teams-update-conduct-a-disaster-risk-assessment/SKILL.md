---
name: "rar-cowork-cookbook-teams-update-conduct-a-disaster-risk-assessment"
description: "Summarizes disaster risk assessment status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions; does not post."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_a_disaster_risk_assessment", "rar_sha256": "7a7baeea6fa357a26087d0d0c5195d9affed0b67165f2ac74caa261b1908ee70", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
