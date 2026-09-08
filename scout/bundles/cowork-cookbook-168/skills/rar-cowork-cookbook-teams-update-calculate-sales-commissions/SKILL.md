---
name: "rar-cowork-cookbook-teams-update-calculate-sales-commissions"
description: "Summarizes sales commission status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_calculate_sales_commissions", "rar_sha256": "f88deace942c108e60cfbca92e948bc80382c8aef77250824d1066d094215048", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
