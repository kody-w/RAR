---
name: "rar-cowork-cookbook-quote-aging-and-follow-up"
description: "Reads your open Dynamics 365 Sales quotes, reports each one's age, expiry status, value, account and related opportunity stage, and writes a three-sheet quote-aging.xlsx. Read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/quote_aging_and_follow_up", "rar_sha256": "6701f28e8fc0ef0543ea843e258baad26d2c65bf6b951f0201b461712bec97c4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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
