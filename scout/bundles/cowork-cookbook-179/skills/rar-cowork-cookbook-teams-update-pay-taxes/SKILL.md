---
name: "rar-cowork-cookbook-teams-update-pay-taxes"
description: "Summarizes current pay taxes status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_pay_taxes", "rar_sha256": "d423203be819792b024974383019e03a7443862de989336a7a285621e2fc4631", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
