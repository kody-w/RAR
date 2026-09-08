---
name: "rar-cowork-cookbook-sales-target-attainment-tracker"
description: "Reports sales target attainment from a bound Dynamics 365 Sales environment: closed-won value vs recorded targets, attainment percent, gap, open pipeline coverage, and per-owner breakdown, as an Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/sales_target_attainment_tracker", "rar_sha256": "fe735c43813e82fd33e01df3c5f261c67417470c08b879c97f23f7802c1eee16", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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
