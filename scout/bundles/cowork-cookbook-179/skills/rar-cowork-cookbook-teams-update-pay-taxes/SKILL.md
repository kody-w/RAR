---
name: "rar-cowork-cookbook-teams-update-pay-taxes"
description: "Summarizes current pay taxes status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_pay_taxes", "rar_sha256": "d423203be819792b024974383019e03a7443862de989336a7a285621e2fc4631", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_pay_taxes`. The original RAPP
agent is preserved byte-for-byte in `teams_update_pay_taxes_agent.py` and in the RCI capsule.

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

Pay taxes Teams Channel Update — Summarizes current pay taxes status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pay-taxes
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-pay-taxes-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_pay_taxes_agent.py` and embedded as the fenced Python below (sha256 d423203be819792b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_pay_taxes_agent.py` first:

```bash
python3 teams_update_pay_taxes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_pay_taxes_agent.py   # or on stdin
python3 teams_update_pay_taxes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay taxes Teams Channel Update — Summarizes current pay taxes status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pay-taxes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_pay_taxes',
    "version": '3.0.3',
    "display_name": 'Pay taxes Teams Channel Update',
    "description": 'Summarizes current pay taxes status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-pay-taxes',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-pay-taxes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '250aaec89cd78091',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/pay-taxes'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-pay-taxes', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-pay-taxes-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of pay taxes. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-pay-taxes-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads pay taxes, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes current pay taxes status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not', 'example_request': "Draft a Teams update on pay taxes for USMF with an Adaptive Card — save it, don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-pay-taxes-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on pay taxes status from D365 F&SCM, with an Adaptive Card saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdatePayTaxes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePayTaxes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-pay-taxes-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdatePayTaxes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
