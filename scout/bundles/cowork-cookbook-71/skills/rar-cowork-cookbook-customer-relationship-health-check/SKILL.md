---
name: "rar-cowork-cookbook-customer-relationship-health-check"
description: "Scores the Dynamics 365 Sales accounts you own for relationship health (contact coverage, engagement recency, open pipeline, win/loss history) and returns an account-health.xlsx workbook with Summary, Detail, and Single-"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_relationship_health_check", "rar_sha256": "fa913eb21736991f61f215ca478c96d600ae0b1c7f95c516d2854600ca28d418", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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
