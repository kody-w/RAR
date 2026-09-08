---
name: "rar-cowork-cookbook-quote-aging-and-follow-up"
description: "Reads your open Dynamics 365 Sales quotes, reports each one's age, expiry status, value, account and related opportunity stage, and writes a three-sheet quote-aging.xlsx. Read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/quote_aging_and_follow_up", "rar_sha256": "6701f28e8fc0ef0543ea843e258baad26d2c65bf6b951f0201b461712bec97c4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/quote_aging_and_follow_up`. The original RAPP
agent is preserved byte-for-byte in `quote_aging_and_follow_up_agent.py` and in the RCI capsule.

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

Quote Aging and Follow-Up Tracker — Reads your open Dynamics 365 Sales quotes, reports each one's age, expiry status, value, account and related opportunity stage, and writes a three-sheet quote-aging.xlsx. Read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/quote-aging-and-follow-up
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
    "analysis_window": {
      "description": "Date range for the quotes to analyze, chosen from within the quote dates actually present.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "The Dynamics 365 Sales environment the plugin is bound to.",
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
    "owner": {
      "description": "The quote owner to scope to; defaults to the requesting user's own quotes.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `quote_aging_and_follow_up_agent.py` and embedded as the fenced Python below (sha256 6701f28e8fc0ef05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `quote_aging_and_follow_up_agent.py` first:

```bash
python3 quote_aging_and_follow_up_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 quote_aging_and_follow_up_agent.py   # or on stdin
python3 quote_aging_and_follow_up_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quote Aging and Follow-Up Tracker — Reads your open Dynamics 365 Sales quotes, reports each one's age, expiry status, value, account and related opportunity stage, and writes a three-sheet quote-aging.xlsx. Read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/quote-aging-and-follow-up
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/quote_aging_and_follow_up',
    "version": '3.0.3',
    "display_name": 'Quote Aging and Follow-Up Tracker',
    "description": "Reads your open Dynamics 365 Sales quotes, reports each one's age, expiry status, value, account and related opportunity stage, and writes a three-sheet quote-aging.xlsx. Read-only.",
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
        "upstream_slug": 'quote-aging-and-follow-up',
        "upstream_url": 'https://coworkcookbook.com/recipes/quote-aging-and-follow-up',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c1c69ea66a95db68',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-sales-quotations'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/quote-aging-and-follow-up', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'Prerequisite: The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'Prerequisite: The plugin bound to the environment you want to analyze (gear icon on the plugin tile)', "Output matches: A three-sheet workbook. The Summary sheet answers 'how much value is sitting in expired or\nnearly-expired quotes', which is usually the number worth escalating."], 'confidence': 1.0, 'deliverable': "A three-sheet workbook. The Summary sheet answers 'how much value is sitting in expired or\nnearly-expired quotes', which is usually the number worth escalating.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'analysis_window': 'Date range for the quotes to analyze, chosen from within the quote dates actually present.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'The Dynamics 365 Sales environment the plugin is bound to.', 'owner': "The quote owner to scope to; defaults to the requesting user's own quotes."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Quotes that expire without a decision are lost revenue nobody decided to give up. This puts a number on the unanswered pipeline and orders the follow-up queue by value at risk.', 'expected_output': "A three-sheet workbook. The Summary sheet answers 'how much value is sitting in expired or\nnearly-expired quotes', which is usually the number worth escalating.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'The plugin bound to the environment you want to analyze (gear icon on the plugin tile)'], 'prompt': "Using the Dynamics 365 Sales plugin, track my outstanding quotes and their follow-up status.\n\nUse search and describe to confirm the quote table and the columns for status, effective or\nexpiry dates, total amount, owner, related account, and related opportunity. Do not guess column\nnames.\n\nRun a read_query to find the range of quote dates present and report it. Choose your analysis\nwindow from inside that range and state it.\n\nScope to quotes I own that are still open or active. For each, report age in days, days until\nor past expiry, total value, the account, and the related opportunity stage if there is one.\n\nGroup them into: expired, expiring within 14 days, and comfortably open. Within each group,\norder by value descending.\n\nProduce an Excel workbook 'quote-aging.xlsx' with a Summary sheet showing count and total value\nper group, a Detail sheet with one row per quote, and a Notes sheet listing the tables and\ncolumns used.\n\nDo not modify any data, and do not send anything to any customer. If I have no open quotes, say\nso and stop.", 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'If your org does not populate quote expiry dates, Cowork will report that — the aging bands'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Ages the open quote book against whatever expiry semantics your environment records, and totals\nthe value in each urgency band. Read-only.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Reads your open Dynamics 365 Sales quotes, reports each one's age, expiry status, value, account and related opportunity stage, and writes a three-sheet quote-aging.xlsx. Read-only.", 'example_request': 'Track my outstanding Dynamics 365 quotes by age and flag the ones expired or expiring soon.', 'inputs': [{'description': 'Date range for the quotes to analyze, chosen from within the quote dates actually present.', 'name': 'analysis_window'}, {'description': "The quote owner to scope to; defaults to the requesting user's own quotes.", 'name': 'owner'}, {'description': 'The Dynamics 365 Sales environment the plugin is bound to.', 'name': 'environment'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want to see which of your outstanding quotes are expired or expiring soon and how much value is sitting unanswered.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'If your org does not populate quote expiry dates, Cowork will report that — the aging bands'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class QuoteAgingAndFollowUp(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'QuoteAgingAndFollowUp'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'analysis_window': {'description': 'Date range for the quotes to analyze, chosen from within the quote dates actually present.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'The Dynamics 365 Sales environment the plugin is bound to.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': "The quote owner to scope to; defaults to the requesting user's own quotes.", 'type': 'string'}},
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
    print(QuoteAgingAndFollowUp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
