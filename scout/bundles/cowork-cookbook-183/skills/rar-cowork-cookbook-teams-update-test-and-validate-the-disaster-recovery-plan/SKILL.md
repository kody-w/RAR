---
name: "rar-cowork-cookbook-teams-update-test-and-validate-the-disaster-recovery-plan"
description: "Summarizes disaster recovery plan test/validation status from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_test_and_validate_the_disaster_recovery_plan", "rar_sha256": "34d2061a95a0ffabd0263c22867ab755e505995988289ad667065cf81f1e1bd2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_test_and_validate_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `teams_update_test_and_validate_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Test and validate the disaster recovery plan Teams Channel Update — Summarizes disaster recovery plan test/validation status from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-test-and-validate-the-disaster-recovery-plan
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-test-and-validate-the-disaster-recovery-plan-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_test_and_validate_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 34d2061a95a0ffab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_test_and_validate_the_disaster_recovery_plan_agent.py` first:

```bash
python3 teams_update_test_and_validate_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_test_and_validate_the_disaster_recovery_plan_agent.py   # or on stdin
python3 teams_update_test_and_validate_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test and validate the disaster recovery plan Teams Channel Update — Summarizes disaster recovery plan test/validation status from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-test-and-validate-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_test_and_validate_the_disaster_recovery_plan',
    "version": '3.0.3',
    "display_name": 'Test and validate the disaster recovery plan Teams Channel Update',
    "description": 'Summarizes disaster recovery plan test/validation status from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post.',
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
        "upstream_slug": 'teams-update-test-and-validate-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-test-and-validate-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b37439ccee4f0e6f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/test-and-validate-the-disaster-recovery-plan'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-test-and-validate-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-test-and-validate-the-disaster-recovery-plan-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of test and validate the disaster recovery plan. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-test-and-validate-the-disaster-recovery-plan-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads test and validate the disaster recovery plan, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes disaster recovery plan test/validation status from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post.', 'example_request': "Draft a Teams post and Adaptive Card on our disaster recovery plan testing status from D365 USMF — don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-test-and-validate-the-disaster-recovery-plan-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update and Adaptive Card on disaster recovery plan testing status pulled from D365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateTestAndValidateTheDisasterRecoveryPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTestAndValidateTheDisasterRecoveryPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-test-and-validate-the-disaster-recovery-plan-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateTestAndValidateTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
