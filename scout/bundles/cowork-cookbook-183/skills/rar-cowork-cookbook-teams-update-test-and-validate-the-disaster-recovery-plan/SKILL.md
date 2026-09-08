---
name: "rar-cowork-cookbook-teams-update-test-and-validate-the-disaster-recovery-plan"
description: "Summarizes disaster recovery plan test/validation status from Dynamics 365 F&SCM for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_test_and_validate_the_disaster_recovery_plan", "rar_sha256": "34d2061a95a0ffabd0263c22867ab755e505995988289ad667065cf81f1e1bd2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
