---
name: "rar-cowork-cookbook-lead-qualification-consistency-check"
description: "Read-only review of lead qualification and disqualification consistency in Dynamics 365 Sales for leads owned by you or your team, returning an Excel workbook of findings; call it to audit lead qualification hygiene."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/lead_qualification_consistency_check", "rar_sha256": "8a1f868359589d216f42e3b2be644f46165235bd8f7cc9628d3c09e285e7bba9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/lead_qualification_consistency_check`. The original RAPP
agent is preserved byte-for-byte in `lead_qualification_consistency_check_agent.py` and in the RCI capsule.

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

Lead Qualification Consistency Check — Read-only review of lead qualification and disqualification consistency in Dynamics 365 Sales for leads owned by you or your team, returning an Excel workbook of findings; call it to audit lead qualification hygiene.

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
  Upstream entry : https://coworkcookbook.com/recipes/lead-qualification-consistency-check
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
    "analysis_period": {
      "description": "The period analyzed; chosen as the most recent complete period within the available lead status change date range.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "The Dynamics 365 Sales environment the plugin is bound to for the analysis.",
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
    "output_workbook": {
      "description": "Name of the Excel workbook produced, default 'lead-qualification-review.xlsx'.",
      "type": "string"
    },
    "ownership_scope": {
      "description": "Whose leads to analyze \u2014 leads owned by you or by your team.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lead_qualification_consistency_check_agent.py` and embedded as the fenced Python below (sha256 8a1f868359589d21…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lead_qualification_consistency_check_agent.py` first:

```bash
python3 lead_qualification_consistency_check_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lead_qualification_consistency_check_agent.py   # or on stdin
python3 lead_qualification_consistency_check_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lead Qualification Consistency Check — Read-only review of lead qualification and disqualification consistency in Dynamics 365 Sales for leads owned by you or your team, returning an Excel workbook of findings; call it to audit lead qualification hygiene.

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
  Upstream entry : https://coworkcookbook.com/recipes/lead-qualification-consistency-check
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/lead_qualification_consistency_check',
    "version": '3.0.3',
    "display_name": 'Lead Qualification Consistency Check',
    "description": 'Read-only review of lead qualification and disqualification consistency in Dynamics 365 Sales for leads owned by you or your team, returning an Excel workbook of findings; call it to audit lead qualification hygiene.',
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
        "upstream_slug": 'lead-qualification-consistency-check',
        "upstream_url": 'https://coworkcookbook.com/recipes/lead-qualification-consistency-check',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '113bb93c7f191892',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/qualify-and-disqualify-leads'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/lead-qualification-consistency-check', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'Prerequisite: The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'Prerequisite: The plugin bound to the environment you want to analyze (gear icon on the plugin tile)', "Output matches: A multi-sheet workbook. The disqualification-reason distribution is usually the most revealing\nsheet: a large 'blank or generic' bucket means your loss reasons cannot support any real\nanalysis yet."], 'confidence': 1.0, 'deliverable': "A multi-sheet workbook. The disqualification-reason distribution is usually the most revealing\nsheet: a large 'blank or generic' bucket means your loss reasons cannot support any real\nanalysis yet.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'analysis_period': 'The period analyzed; chosen as the most recent complete period within the available lead status change date range.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'The Dynamics 365 Sales environment the plugin is bound to for the analysis.', 'output_workbook': "Name of the Excel workbook produced, default 'lead-qualification-review.xlsx'.", 'ownership_scope': 'Whose leads to analyze — leads owned by you or by your team.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Inconsistent qualification quietly corrupts every downstream conversion metric. This shows where the qualification bar is being applied unevenly and where disqualification reasons are too thin to learn from.', 'expected_output': "A multi-sheet workbook. The disqualification-reason distribution is usually the most revealing\nsheet: a large 'blank or generic' bucket means your loss reasons cannot support any real\nanalysis yet.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'The plugin bound to the environment you want to analyze (gear icon on the plugin tile)'], 'prompt': "Using the Dynamics 365 Sales plugin, review how consistently leads are being qualified and\ndisqualified.\n\nUse search and describe to confirm the lead table and the columns for status, status reason,\nqualification or disqualification reason, rating, score if present, owner, and the relevant\ndates. Report any of these your environment does not have.\n\nRun a read_query to find the date range of lead status changes available and report it, then\nanalyze the most recent complete period inside that range. State which period you chose.\n\nScope to leads owned by me or by my team. Then report:\n- the distribution of disqualification reasons, including how many have a blank or generic reason\n- qualified leads that are missing fields your environment marks as required for qualification\n- any owner whose qualification or disqualification rate is a clear outlier against the group\n- leads that sat in an open qualification state longer than the typical time to decision\n\nProduce an Excel workbook 'lead-qualification-review.xlsx' with a Summary sheet, one sheet per\nfinding above, and a Notes sheet listing the tables and columns used.\n\nDo not modify any data. Do not requalify or disqualify anything. If there is not enough status\nhistory to draw conclusions, say so plainly and stop.", 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Treat the outlier section as a conversation starter, not a verdict — territory mix explains'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Profiles qualification behaviour rather than lead outcomes: reason-code hygiene, missing data at\nthe qualification gate, per-owner outliers, and decision latency. Read-only.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only review of lead qualification and disqualification consistency in Dynamics 365 Sales for leads owned by you or your team, returning an Excel workbook of findings; call it to audit lead qualification hygiene.', 'example_request': "Check how consistently my team's leads are being qualified and disqualified in Dynamics, and give me the workbook.", 'inputs': [{'description': 'The Dynamics 365 Sales environment the plugin is bound to for the analysis.', 'name': 'environment'}, {'description': 'Whose leads to analyze — leads owned by you or by your team.', 'name': 'ownership_scope'}, {'description': 'The period analyzed; chosen as the most recent complete period within the available lead status change date range.', 'name': 'analysis_period'}, {'description': "Name of the Excel workbook produced, default 'lead-qualification-review.xlsx'.", 'name': 'output_workbook'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you want to check whether leads are qualified/disqualified consistently and find disqualifications with blank or generic reasons, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Treat the outlier section as a conversation starter, not a verdict — territory mix explains'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class LeadQualificationConsistencyCheck(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LeadQualificationConsistencyCheck'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'analysis_period': {'description': 'The period analyzed; chosen as the most recent complete period within the available lead status change date range.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'The Dynamics 365 Sales environment the plugin is bound to for the analysis.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_workbook': {'description': "Name of the Excel workbook produced, default 'lead-qualification-review.xlsx'.", 'type': 'string'}, 'ownership_scope': {'description': 'Whose leads to analyze — leads owned by you or by your team.', 'type': 'string'}},
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
    print(LeadQualificationConsistencyCheck().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
