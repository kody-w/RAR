---
name: "rar-cowork-cookbook-quote-conversion-funnel"
description: "Reads sales quotes for a fiscal year from Dynamics 365 F&SCM and returns an Excel workbook plus a standalone HTML funnel chart showing sent-to-won conversion by salesperson, product family, and lost reason."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/quote_conversion_funnel", "rar_sha256": "269a51757375252f20b0850263e499bc8ddf9cd6e7525e18c073b643b6d22544", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
