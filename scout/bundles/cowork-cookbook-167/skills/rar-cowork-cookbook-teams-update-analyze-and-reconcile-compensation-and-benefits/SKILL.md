---
name: "rar-cowork-cookbook-teams-update-analyze-and-reconcile-compensation-and-benefits"
description: "Drafts a Teams channel update on compensation and benefits reconciliation status from Dynamics 365 F&SCM data for a legal entity, returning a markdown post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits", "rar_sha256": "64cfc12b15c180ef0281053be3dc387a1fe63dbef5ffafaae4df0238380822b3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` and in the RCI capsule.

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

Analyze and reconcile compensation and benefits Teams Channel Update — Drafts a Teams channel update on compensation and benefits reconciliation status from Dynamics 365 F&SCM data for a legal entity, returning a markdown post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits
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
      "description": "Filename for the generated Adaptive Card JSON artifact.",
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
    },
    "quick_actions": {
      "description": "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` and embedded as the fenced Python below (sha256 64cfc12b15c180ef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` first:

```bash
python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py   # or on stdin
python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and reconcile compensation and benefits Teams Channel Update — Drafts a Teams channel update on compensation and benefits reconciliation status from Dynamics 365 F&SCM data for a legal entity, returning a markdown post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits',
    "version": '3.0.3',
    "display_name": 'Analyze and reconcile compensation and benefits Teams Channel Update',
    "description": 'Drafts a Teams channel update on compensation and benefits reconciliation status from Dynamics 365 F&SCM data for a legal entity, returning a markdown post plus an Adaptive Card JSON file saved for review, not posted.',
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
        "upstream_slug": 'teams-update-analyze-and-reconcile-compensation-and-benefits',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fabfb2687117fadc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-and-reconcile-compensation-and-benefits'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-analyze-and-reconcile-compensation-and-benefits', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'quick_actions': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of analyze and reconcile compensation and benefits. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-analyze-and-reconcile-compensation-and-benefits-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze and reconcile compensation and benefits, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Drafts a Teams channel update on compensation and benefits reconciliation status from Dynamics 365 F&SCM data for a legal entity, returning a markdown post plus an Adaptive Card JSON file saved for review, not posted.', 'example_request': "Draft a Teams update on comp and benefits reconciliation for USMF with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'name': 'card_filename'}, {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel post and Adaptive Card summarizing compensation and benefits reconciliation status from D365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}},
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
    print(TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
