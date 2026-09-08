---
name: "rar-cowork-cookbook-opportunity-slip-risk-analysis"
description: "Analyzes your open Dynamics 365 Sales opportunities you own, flags ones at risk of slipping past estimated close, and returns an Excel workbook 'opportunity-slip-risk.xlsx' with Summary, At Risk, and Notes sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/opportunity_slip_risk_analysis", "rar_sha256": "56dc4c7c155ea78628f0cd1436826224294feb9e511e63df6915c2d641506785", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/opportunity_slip_risk_analysis`. The original RAPP
agent is preserved byte-for-byte in `opportunity_slip_risk_analysis_agent.py` and in the RCI capsule.

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

Opportunity Slip-Risk Analysis — Analyzes your open Dynamics 365 Sales opportunities you own, flags ones at risk of slipping past estimated close, and returns an Excel workbook 'opportunity-slip-risk.xlsx' with Summary, At Risk, and Notes sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/opportunity-slip-risk-analysis
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
    "closing_soon_days": {
      "description": "Days until estimated close that counts as closing soon when the stage is still early (default 30).",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "early_sales_stages": {
      "description": "Which sales stage values count as early for the closing-soon risk rule.",
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
    "output_filename": {
      "description": "Name of the Excel workbook to produce (default 'opportunity-slip-risk.xlsx').",
      "type": "string"
    },
    "stale_threshold_days": {
      "description": "Days without modification before an opportunity is flagged stale (default 30).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `opportunity_slip_risk_analysis_agent.py` and embedded as the fenced Python below (sha256 56dc4c7c155ea786…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `opportunity_slip_risk_analysis_agent.py` first:

```bash
python3 opportunity_slip_risk_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 opportunity_slip_risk_analysis_agent.py   # or on stdin
python3 opportunity_slip_risk_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Opportunity Slip-Risk Analysis — Analyzes your open Dynamics 365 Sales opportunities you own, flags ones at risk of slipping past estimated close, and returns an Excel workbook 'opportunity-slip-risk.xlsx' with Summary, At Risk, and Notes sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/opportunity-slip-risk-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/opportunity_slip_risk_analysis',
    "version": '3.0.3',
    "display_name": 'Opportunity Slip-Risk Analysis',
    "description": "Analyzes your open Dynamics 365 Sales opportunities you own, flags ones at risk of slipping past estimated close, and returns an Excel workbook 'opportunity-slip-risk.xlsx' with Summary, At Risk, and Notes sheets.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'opportunity-slip-risk-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/opportunity-slip-risk-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '10e74bf17eb9aac8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/opportunity-slip-risk-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'Prerequisite: The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'Prerequisite: The plugin bound to the environment you want to analyze (gear icon on the plugin tile)', 'Output matches: An Excel workbook in your Cowork output folder with three sheets. The Summary sheet gives a\ncount and value total per risk reason; the At Risk sheet is the working list, highest value\nfirst. If you own no open opportunities, Cowork reports that instead of inventing rows.'], 'confidence': 1.0, 'deliverable': 'An Excel workbook in your Cowork output folder with three sheets. The Summary sheet gives a\ncount and value total per risk reason; the At Risk sheet is the working list, highest value\nfirst. If you own no open opportunities, Cowork reports that instead of inventing rows.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'closing_soon_days': 'Days until estimated close that counts as closing soon when the stage is still early (default 30).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'early_sales_stages': 'Which sales stage values count as early for the closing-soon risk rule.', 'output_filename': "Name of the Excel workbook to produce (default 'opportunity-slip-risk.xlsx').", 'stale_threshold_days': 'Days without modification before an opportunity is flagged stale (default 30).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Turns a subjective gut-feel forecast review into an evidence-based one. Sellers see which deals are drifting while there is still time to act, and managers stop discovering slipped deals at the end of the quarter.', 'expected_output': 'An Excel workbook in your Cowork output folder with three sheets. The Summary sheet gives a\ncount and value total per risk reason; the At Risk sheet is the working list, highest value\nfirst. If you own no open opportunities, Cowork reports that instead of inventing rows.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'The plugin bound to the environment you want to analyze (gear icon on the plugin tile)'], 'prompt': "Using the Dynamics 365 Sales plugin, analyze my open opportunities and identify the ones at\nrisk of slipping.\n\nFirst, use search and describe to confirm the opportunity table and the columns for estimated\nclose date, estimated value, sales stage, owner, status, and last modified date. Do not guess\ncolumn names.\n\nThen run a read_query to find the range of estimated close dates across my open opportunities\nand report that range before you filter on it.\n\nScope to opportunities where I am the owner and the status is open. For each one, compute days\nsince last modified and days until estimated close. Flag an opportunity as at risk when any of\nthese hold:\n- the estimated close date is already in the past\n- there has been no modification in more than 30 days\n- the estimated close is within 30 days but the sales stage is still an early one\n\nProduce an Excel workbook 'opportunity-slip-risk.xlsx' with:\n- a Summary sheet showing counts and total estimated value by risk reason\n- an At Risk sheet sorted by estimated value descending, one row per opportunity, with the risk\n  reasons that fired\n- a Notes sheet listing which tables and columns you used and the date range you found\n\nDo not modify any data. If I own no open opportunities, say so plainly and stop.", 'steps': ['Open Cowork and confirm the **Dynamics 365 Sales** plugin is toggled on for your session.', 'Check the gear icon on the plugin tile and confirm it is bound to the environment you want', 'Paste the prompt from `prompt.md` into a new task and send it.', 'Review the Notes sheet first — it tells you which columns Cowork actually used, which is', 'Adjust the 30-day thresholds in the prompt to match your sales cycle and re-run.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads your open opportunities through the Dataverse MCP tools, derives three objective\nslip-risk signals from the record data, and writes a prioritized exceptions workbook. All\nanalysis is read-only.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Analyzes your open Dynamics 365 Sales opportunities you own, flags ones at risk of slipping past estimated close, and returns an Excel workbook 'opportunity-slip-risk.xlsx' with Summary, At Risk, and Notes sheets.", 'example_request': 'Check my open D365 opportunities for slip risk and build the slip-risk workbook.', 'inputs': [{'description': 'Days without modification before an opportunity is flagged stale (default 30).', 'name': 'stale_threshold_days'}, {'description': 'Days until estimated close that counts as closing soon when the stage is still early (default 30).', 'name': 'closing_soon_days'}, {'description': 'Which sales stage values count as early for the closing-soon risk rule.', 'name': 'early_sales_stages'}, {'description': "Name of the Excel workbook to produce (default 'opportunity-slip-risk.xlsx').", 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want a prioritized, read-only review of which of your open opportunities are likely to slip their estimated close date.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the **Dynamics 365 Sales** plugin is toggled on for your session.', 'Check the gear icon on the plugin tile and confirm it is bound to the environment you want', 'Paste the prompt from `prompt.md` into a new task and send it.', 'Review the Notes sheet first — it tells you which columns Cowork actually used, which is', 'Adjust the 30-day thresholds in the prompt to match your sales cycle and re-run.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class OpportunitySlipRiskAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OpportunitySlipRiskAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'closing_soon_days': {'description': 'Days until estimated close that counts as closing soon when the stage is still early (default 30).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'early_sales_stages': {'description': 'Which sales stage values count as early for the closing-soon risk rule.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': "Name of the Excel workbook to produce (default 'opportunity-slip-risk.xlsx').", 'type': 'string'}, 'stale_threshold_days': {'description': 'Days without modification before an opportunity is flagged stale (default 30).', 'type': 'string'}},
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
    print(OpportunitySlipRiskAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
