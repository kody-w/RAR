---
name: "rar-cowork-cookbook-customer-relationship-health-check"
description: "Scores the Dynamics 365 Sales accounts you own for relationship health (contact coverage, engagement recency, open pipeline, win/loss history) and returns an account-health.xlsx workbook with Summary, Detail, and Single-"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_relationship_health_check", "rar_sha256": "fa913eb21736991f61f215ca478c96d600ae0b1c7f95c516d2854600ca28d418", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/customer_relationship_health_check`. The original RAPP
agent is preserved byte-for-byte in `customer_relationship_health_check_agent.py` and in the RCI capsule.

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

Customer Relationship Health Check — Scores the Dynamics 365 Sales accounts you own for relationship health (contact coverage, engagement recency, open pipeline, win/loss history) and returns an account-health.xlsx workbook with Summary, Detail, and Single-

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
  Upstream entry : https://coworkcookbook.com/recipes/customer-relationship-health-check
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_relationship_health_check_agent.py` and embedded as the fenced Python below (sha256 fa913eb21736991f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_relationship_health_check_agent.py` first:

```bash
python3 customer_relationship_health_check_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_relationship_health_check_agent.py   # or on stdin
python3 customer_relationship_health_check_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Relationship Health Check — Scores the Dynamics 365 Sales accounts you own for relationship health (contact coverage, engagement recency, open pipeline, win/loss history) and returns an account-health.xlsx workbook with Summary, Detail, and Single-

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
  Upstream entry : https://coworkcookbook.com/recipes/customer-relationship-health-check
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/customer_relationship_health_check',
    "version": '3.0.3',
    "display_name": 'Customer Relationship Health Check',
    "description": 'Scores the Dynamics 365 Sales accounts you own for relationship health (contact coverage, engagement recency, open pipeline, win/loss history) and returns an account-health.xlsx workbook with Summary, Detail, and Single-',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'customer-relationship-health-check',
        "upstream_url": 'https://coworkcookbook.com/recipes/customer-relationship-health-check',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '04732e773c708440',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/nurture-trust-relationship-regularly-with-customer'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/customer-relationship-health-check', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'Prerequisite: The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'Prerequisite: The plugin bound to the environment you want to analyze (gear icon on the plugin tile)', 'Output matches: A three-sheet workbook with an explicit scoring rule stated in the output. The Single-Threaded\nsheet is typically the one that drives immediate action.'], 'confidence': 1.0, 'deliverable': 'A three-sheet workbook with an explicit scoring rule stated in the output. The Single-Threaded\nsheet is typically the one that drives immediate action.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Single-threaded and quietly dormant accounts are the ones that churn or get lost to a competitor without warning. This finds them while there is still time to build coverage.', 'expected_output': 'A three-sheet workbook with an explicit scoring rule stated in the output. The Single-Threaded\nsheet is typically the one that drives immediate action.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'The plugin bound to the environment you want to analyze (gear icon on the plugin tile)'], 'prompt': "Using the Dynamics 365 Sales plugin, assess the relationship health of the accounts I own.\n\nUse search and describe to confirm the account, contact, opportunity, and activity tables and\nthe columns for owner, contact role or title, activity dates, and opportunity status. Report\nanything you expected but could not find.\n\nRun a read_query to establish the range of activity dates available and report it before using\nit. Choose a recency baseline from within that range rather than from today's date, and say what\nyou chose.\n\nScope to accounts where I am the owner. Score each account on:\n- contact coverage: how many active contacts, and whether more than one has recent engagement\n  (a single engaged contact is a single-threading risk)\n- engagement recency: how long since any activity on the account\n- pipeline presence: whether any opportunity is currently open\n- history: won and lost opportunity counts\n\nCombine those into a simple red / amber / green rating, and state the rule you used so I can\nchallenge it.\n\nProduce an Excel workbook 'account-health.xlsx' with a Summary sheet (counts by rating), a\nDetail sheet with one row per account and its component scores, and a Single-Threaded sheet\nlisting accounts that depend on one contact.\n\nDo not modify any data. If I own no accounts, say so and stop.", 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Read the stated scoring rule before reading the ratings, and adjust the prompt if the'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a composite health rating from four objective signals and makes the scoring rule explicit\nso it can be argued with and tuned. The single-threading view is broken out separately because\nit is the most actionable.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scores the Dynamics 365 Sales accounts you own for relationship health (contact coverage, engagement recency, open pipeline, win/loss history) and returns an account-health.xlsx workbook with Summary, Detail, and Single-', 'example_request': 'Run a relationship health check on the Dynamics 365 accounts I own and give me the workbook.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want a read-only red/amber/green health review of accounts you own in Dynamics 365 Sales, especially to find single-threaded accounts.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Read the stated scoring rule before reading the ratings, and adjust the prompt if the'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CustomerRelationshipHealthCheck(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CustomerRelationshipHealthCheck'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(CustomerRelationshipHealthCheck().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
