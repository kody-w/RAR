---
name: "rar-cowork-cookbook-opportunity-slip-risk-analysis"
description: "Analyzes your open Dynamics 365 Sales opportunities you own, flags ones at risk of slipping past estimated close, and returns an Excel workbook 'opportunity-slip-risk.xlsx' with Summary, At Risk, and Notes sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/opportunity_slip_risk_analysis", "rar_sha256": "56dc4c7c155ea78628f0cd1436826224294feb9e511e63df6915c2d641506785", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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
