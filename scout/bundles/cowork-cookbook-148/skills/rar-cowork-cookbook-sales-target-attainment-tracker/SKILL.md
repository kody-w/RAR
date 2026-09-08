---
name: "rar-cowork-cookbook-sales-target-attainment-tracker"
description: "Reports sales target attainment from a bound Dynamics 365 Sales environment: closed-won value vs recorded targets, attainment percent, gap, open pipeline coverage, and per-owner breakdown, as an Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/sales_target_attainment_tracker", "rar_sha256": "fe735c43813e82fd33e01df3c5f261c67417470c08b879c97f23f7802c1eee16", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/sales_target_attainment_tracker`. The original RAPP
agent is preserved byte-for-byte in `sales_target_attainment_tracker_agent.py` and in the RCI capsule.

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

Sales Target Attainment Tracker — Reports sales target attainment from a bound Dynamics 365 Sales environment: closed-won value vs recorded targets, attainment percent, gap, open pipeline coverage, and per-owner breakdown, as an Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/sales-target-attainment-tracker
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_target_attainment_tracker_agent.py` and embedded as the fenced Python below (sha256 fe735c43813e82fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_target_attainment_tracker_agent.py` first:

```bash
python3 sales_target_attainment_tracker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_target_attainment_tracker_agent.py   # or on stdin
python3 sales_target_attainment_tracker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sales Target Attainment Tracker — Reports sales target attainment from a bound Dynamics 365 Sales environment: closed-won value vs recorded targets, attainment percent, gap, open pipeline coverage, and per-owner breakdown, as an Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/sales-target-attainment-tracker
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/sales_target_attainment_tracker',
    "version": '3.0.3',
    "display_name": 'Sales Target Attainment Tracker',
    "description": 'Reports sales target attainment from a bound Dynamics 365 Sales environment: closed-won value vs recorded targets, attainment percent, gap, open pipeline coverage, and per-owner breakdown, as an Excel workbook.',
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
        "upstream_slug": 'sales-target-attainment-tracker',
        "upstream_url": 'https://coworkcookbook.com/recipes/sales-target-attainment-tracker',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd113919bafd5b90b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/sales-target-attainment-tracker', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'Prerequisite: The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'Prerequisite: The plugin bound to the environment you want to analyze (gear icon on the plugin tile)', 'Output matches: A three-sheet workbook covering attainment, gap, and coverage. If your environment has no target\ndata, expect an actuals-and-pipeline report plus an explicit statement that no targets were\nfound.'], 'confidence': 1.0, 'deliverable': 'A three-sheet workbook covering attainment, gap, and coverage. If your environment has no target\ndata, expect an actuals-and-pipeline report plus an explicit statement that no targets were\nfound.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Answers the two questions every sales review starts with — where are we against target, and is there enough pipeline to make up the gap — without anyone rebuilding the spreadsheet each time.', 'expected_output': 'A three-sheet workbook covering attainment, gap, and coverage. If your environment has no target\ndata, expect an actuals-and-pipeline report plus an explicit statement that no targets were\nfound.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'The plugin bound to the environment you want to analyze (gear icon on the plugin tile)'], 'prompt': "Using the Dynamics 365 Sales plugin, report attainment against sales targets.\n\nUse search and describe to look for how targets are represented in this environment — that may\nbe a goal or quota table, a target field on the user or team record, or something custom.\nReport exactly what you found. If this environment records no targets at all, say so plainly,\nreport actual performance on its own, and stop rather than inventing a target.\n\nConfirm the opportunity table and the columns for status, actual or estimated value, close date,\nand owner. Run a read_query to establish the range of close dates available and report it, then\npick the most recent complete period inside that range and state your choice.\n\nFor that period, and scoped to me and my team, report:\n- closed-won value, against target where a target exists\n- attainment percentage and absolute gap\n- open pipeline value with a close date inside the period, and the resulting coverage ratio\n- a per-owner breakdown of the same figures\n\nProduce an Excel workbook 'target-attainment.xlsx' with a Summary sheet, a By Owner sheet, and a\nNotes sheet naming where the target figures came from.\n\nDo not modify any data.", 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Read the Notes sheet to confirm Cowork found the target source you expected — target storage'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Locates however this environment stores targets, then reports attainment and pipeline coverage\nagainst them. Degrades honestly to an actuals-only report when no target data exists.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reports sales target attainment from a bound Dynamics 365 Sales environment: closed-won value vs recorded targets, attainment percent, gap, open pipeline coverage, and per-owner breakdown, as an Excel workbook.', 'example_request': "Show my team's attainment against sales targets for the last complete period from Dynamics 365 Sales.", 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want to know how you and your team are tracking against sales targets for a recent complete period, including gap to target and pipeline coverage.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Read the Notes sheet to confirm Cowork found the target source you expected — target storage'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class SalesTargetAttainmentTracker(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SalesTargetAttainmentTracker'
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
    print(SalesTargetAttainmentTracker().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
