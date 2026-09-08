---
name: "rar-cowork-cookbook-lead-qualification-consistency-check"
description: "Read-only review of lead qualification and disqualification consistency in Dynamics 365 Sales for leads owned by you or your team, returning an Excel workbook of findings; call it to audit lead qualification hygiene."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/lead_qualification_consistency_check", "rar_sha256": "8a1f868359589d216f42e3b2be644f46165235bd8f7cc9628d3c09e285e7bba9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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
