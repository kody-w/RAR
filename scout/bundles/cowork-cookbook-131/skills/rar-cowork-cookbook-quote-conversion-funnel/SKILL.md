---
name: "rar-cowork-cookbook-quote-conversion-funnel"
description: "Reads sales quotes for a fiscal year from Dynamics 365 F&SCM and returns an Excel workbook plus a standalone HTML funnel chart showing sent-to-won conversion by salesperson, product family, and lost reason."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/quote_conversion_funnel", "rar_sha256": "269a51757375252f20b0850263e499bc8ddf9cd6e7525e18c073b643b6d22544", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/quote_conversion_funnel`. The original RAPP
agent is preserved byte-for-byte in `quote_conversion_funnel_agent.py` and in the RCI capsule.

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

Quote Conversion Funnel Analysis (HTML) — Reads sales quotes for a fiscal year from Dynamics 365 F&SCM and returns an Excel workbook plus a standalone HTML funnel chart showing sent-to-won conversion by salesperson, product family, and lost reason.

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
  Upstream entry : https://coworkcookbook.com/recipes/quote-conversion-funnel
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "fiscal_year": {
      "description": "Fiscal year of quotes to analyze (use FY2017 for the USMF demo tenant).",
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
    "output_folder": {
      "description": "Folder where the .xlsx workbook and .html funnel chart are saved.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `quote_conversion_funnel_agent.py` and embedded as the fenced Python below (sha256 269a51757375252f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `quote_conversion_funnel_agent.py` first:

```bash
python3 quote_conversion_funnel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 quote_conversion_funnel_agent.py   # or on stdin
python3 quote_conversion_funnel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quote Conversion Funnel Analysis (HTML) — Reads sales quotes for a fiscal year from Dynamics 365 F&SCM and returns an Excel workbook plus a standalone HTML funnel chart showing sent-to-won conversion by salesperson, product family, and lost reason.

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
  Upstream entry : https://coworkcookbook.com/recipes/quote-conversion-funnel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/quote_conversion_funnel',
    "version": '3.0.3',
    "display_name": 'Quote Conversion Funnel Analysis (HTML)',
    "description": 'Reads sales quotes for a fiscal year from Dynamics 365 F&SCM and returns an Excel workbook plus a standalone HTML funnel chart showing sent-to-won conversion by salesperson, product family, and lost reason.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'quote-conversion-funnel',
        "upstream_url": 'https://coworkcookbook.com/recipes/quote-conversion-funnel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6733c3fdab8db06f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/quote-conversion-funnel', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Sales manager role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: One Excel workbook and one HTML funnel chart.'], 'confidence': 1.0, 'deliverable': 'One Excel workbook and one HTML funnel chart.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_year': 'Fiscal year of quotes to analyze (use FY2017 for the USMF demo tenant).', 'output_folder': 'Folder where the .xlsx workbook and .html funnel chart are saved.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Highlights where deals are leaking from the quote pipeline (which salesperson, which product, which lost-reason) so sales coaching and product positioning effort can be targeted with evidence.', 'expected_output': 'One Excel workbook and one HTML funnel chart.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Sales manager role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Read all sales quotes for the last fiscal year (for the USMF demo tenant use FY2017). For each quote: capture salesperson, customer, product family, quote total, status (Sent / Won / Lost / Expired), and lost-reason if available. Compute the conversion funnel: sent → won. Produce: (a) an Excel workbook 'Quote-funnel-<YYYY>.xlsx' with detail and pivoted summaries by salesperson and product family; and (b) a standalone HTML 'Quote-funnel-<YYYY>.html' with a horizontal funnel chart (inline SVG) and a small breakdown table beneath. Save both to the output folder.", 'steps': ['Paste the prompt.', 'Review with the sales leadership team.', 'Use the lost-reason breakdown to drive a coaching agenda.'], 'tenant_caveat': "Validated against a live Cowork tenant on 2026-05-23 with USMF. Cowork engaged the D365 ERP plugin and used the DeliveryValidFrom field as the quotation-date anchor (the header doesn't expose a single 'quotation date' field). Honesty result: USMF contains exactly ONE sales quote in its entire history (Quote 000007, 2012-10-03, US-008, total $0.00, status 'Created'). There are no FY2017 quotes, so a meaningful funnel can't be built. Cowork stopped and offered to widen the search to all years or to swap to a different document type (sales orders or sales invoices) for FY2017. This is an excellent demonstration of Cowork honestly halting when the source data won't support a meaningful answer - the right behavior for a sales-pipeline analytic. Run this recipe against a tenant with real quote activity to get the full funnel chart and pivoted breakdowns.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Surfaces quote-pipeline leakage with both a workbook for analysis and an HTML funnel for sales leadership review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads sales quotes for a fiscal year from Dynamics 365 F&SCM and returns an Excel workbook plus a standalone HTML funnel chart showing sent-to-won conversion by salesperson, product family, and lost reason.', 'example_request': 'Analyze our FY2017 quote conversion funnel and give me the workbook and HTML funnel chart.', 'inputs': [{'description': 'Fiscal year of quotes to analyze (use FY2017 for the USMF demo tenant).', 'name': 'fiscal_year'}, {'description': 'Folder where the .xlsx workbook and .html funnel chart are saved.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants quote win/loss/expired conversion funnel analysis for a fiscal year, broken down by salesperson, product family, and lost reason.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Review with the sales leadership team.', 'Use the lost-reason breakdown to drive a coaching agenda.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class QuoteConversionFunnel(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'QuoteConversionFunnel'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_year': {'description': 'Fiscal year of quotes to analyze (use FY2017 for the USMF demo tenant).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_folder': {'description': 'Folder where the .xlsx workbook and .html funnel chart are saved.', 'type': 'string'}},
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
    print(QuoteConversionFunnel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
