---
name: "rar-cowork-cookbook-teams-update-calculate-sales-commissions"
description: "Summarizes sales commission status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_calculate_sales_commissions", "rar_sha256": "f88deace942c108e60cfbca92e948bc80382c8aef77250824d1066d094215048", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_calculate_sales_commissions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_calculate_sales_commissions_agent.py` and in the RCI capsule.

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

Calculate sales commissions Teams Channel Update — Summarizes sales commission status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-calculate-sales-commissions
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
      "description": "Filename for the Adaptive Card JSON artifact, e.g. teams-update-calculate-sales-commissions-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (recipe default: USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_calculate_sales_commissions_agent.py` and embedded as the fenced Python below (sha256 f88deace942c108e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_calculate_sales_commissions_agent.py` first:

```bash
python3 teams_update_calculate_sales_commissions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_calculate_sales_commissions_agent.py   # or on stdin
python3 teams_update_calculate_sales_commissions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Calculate sales commissions Teams Channel Update — Summarizes sales commission status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-calculate-sales-commissions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_calculate_sales_commissions',
    "version": '3.0.3',
    "display_name": 'Calculate sales commissions Teams Channel Update',
    "description": 'Summarizes sales commission status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-calculate-sales-commissions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-calculate-sales-commissions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4bd75578a165c3d9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/calculate-sales-commissions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-calculate-sales-commissions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-calculate-sales-commissions-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (recipe default: USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of calculate sales commissions. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-calculate-sales-commissions-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads calculate sales commissions, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes sales commission status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams update on sales commission status in USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to report on (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-calculate-sales-commissions-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on sales commission status from D365 ERP, with an Adaptive Card for triage, saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateCalculateSalesCommissions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCalculateSalesCommissions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-calculate-sales-commissions-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateCalculateSalesCommissions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
