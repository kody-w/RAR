---
name: "rar-cowork-cookbook-lead-response-time-audit"
description: "Audits how quickly leads owned by you or your team are first worked in Dynamics 365 Sales, and returns an Excel workbook with median and 90th-percentile response times plus untouched leads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/lead_response_time_audit", "rar_sha256": "a911e692ad8ba7c7fa00551bca0e1e518e0a113e42dafb12b0be2e3aca911639", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/lead_response_time_audit`. The original RAPP
agent is preserved byte-for-byte in `lead_response_time_audit_agent.py` and in the RCI capsule.

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

Lead Response Time Audit — Audits how quickly leads owned by you or your team are first worked in Dynamics 365 Sales, and returns an Excel workbook with median and 90th-percentile response times plus untouched leads.

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
  Upstream entry : https://coworkcookbook.com/recipes/lead-response-time-audit
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
      "description": "Optional preferred date window; otherwise the most recent three months of actual lead creation dates is chosen.",
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
    "output_file": {
      "description": "Name of the Excel workbook to produce, default 'lead-response-audit.xlsx'.",
      "type": "string"
    },
    "ownership_scope": {
      "description": "Whose leads to include \u2014 leads owned by you or by your team.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lead_response_time_audit_agent.py` and embedded as the fenced Python below (sha256 a911e692ad8ba7c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lead_response_time_audit_agent.py` first:

```bash
python3 lead_response_time_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lead_response_time_audit_agent.py   # or on stdin
python3 lead_response_time_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lead Response Time Audit — Audits how quickly leads owned by you or your team are first worked in Dynamics 365 Sales, and returns an Excel workbook with median and 90th-percentile response times plus untouched leads.

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
  Upstream entry : https://coworkcookbook.com/recipes/lead-response-time-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/lead_response_time_audit',
    "version": '3.0.3',
    "display_name": 'Lead Response Time Audit',
    "description": 'Audits how quickly leads owned by you or your team are first worked in Dynamics 365 Sales, and returns an Excel workbook with median and 90th-percentile response times plus untouched leads.',
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
        "upstream_slug": 'lead-response-time-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/lead-response-time-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f358938a00e3753c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/manage-lead-identification-process'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/lead-response-time-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'Prerequisite: The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'Prerequisite: The plugin bound to the environment you want to analyze (gear icon on the plugin tile)', 'Output matches: A four-sheet workbook. The Summary sheet is the headline: median response, 90th percentile, and\nuntouched count. The Untouched sheet is usually the most immediately actionable.'], 'confidence': 1.0, 'deliverable': 'A four-sheet workbook. The Summary sheet is the headline: median response, 90th percentile, and\nuntouched count. The Untouched sheet is usually the most immediately actionable.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'analysis_window': 'Optional preferred date window; otherwise the most recent three months of actual lead creation dates is chosen.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'The Dynamics 365 Sales environment the plugin is bound to for the analysis.', 'output_file': "Name of the Excel workbook to produce, default 'lead-response-audit.xlsx'.", 'ownership_scope': 'Whose leads to include — leads owned by you or by your team.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Speed to first contact is one of the strongest predictors of lead conversion. This makes response lag visible and specific rather than anecdotal, and surfaces the untouched backlog before it goes cold.', 'expected_output': 'A four-sheet workbook. The Summary sheet is the headline: median response, 90th percentile, and\nuntouched count. The Untouched sheet is usually the most immediately actionable.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'The plugin bound to the environment you want to analyze (gear icon on the plugin tile)'], 'prompt': "Using the Dynamics 365 Sales plugin, audit how quickly leads are being worked.\n\nUse search and describe to confirm the lead table and the columns for created date, owner,\nstatus, rating, and any first-contact or first-activity indicator available. Also check for a\nrelated activity table that records the first touch. Do not guess column names — report what\nyou find and what you could not find.\n\nRun a read_query to establish the range of lead creation dates present, report it, and choose an\nanalysis window inside that range — prefer the most recent three months of real data rather\nthan the current calendar date. State the window you chose.\n\nScope to leads owned by me or by my team. For each lead in the window, compute the elapsed time\nfrom creation to first recorded activity. Where no activity exists, compute age since creation\nand mark it untouched.\n\nProduce an Excel workbook 'lead-response-audit.xlsx' with:\n- a Summary sheet: median and 90th-percentile response time, plus a count of untouched leads\n- a Response Times sheet, slowest first\n- an Untouched sheet, oldest first\n- a Notes sheet naming the tables and columns used and the window analyzed\n\nDo not modify any data. If no leads exist in the window, report that and stop.", 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Read the Notes sheet to see whether your org records a usable first-contact signal — if not,'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Joins leads to their first recorded activity to derive response latency, then separates the\ngenuinely slow from the never-touched. Percentiles rather than averages, so a few outliers do\nnot hide the typical experience.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits how quickly leads owned by you or your team are first worked in Dynamics 365 Sales, and returns an Excel workbook with median and 90th-percentile response times plus untouched leads.', 'example_request': "Audit lead response times for my team's leads in Dynamics and give me the untouched ones in a workbook.", 'inputs': [{'description': 'The Dynamics 365 Sales environment the plugin is bound to for the analysis.', 'name': 'environment'}, {'description': 'Whose leads to include — leads owned by you or by your team.', 'name': 'ownership_scope'}, {'description': 'Optional preferred date window; otherwise the most recent three months of actual lead creation dates is chosen.', 'name': 'analysis_window'}, {'description': "Name of the Excel workbook to produce, default 'lead-response-audit.xlsx'.", 'name': 'output_file'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want to know how long leads sit before first contact, or to find leads still untouched, using read-only Dynamics 365 Sales data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Read the Notes sheet to see whether your org records a usable first-contact signal — if not,'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class LeadResponseTimeAudit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LeadResponseTimeAudit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'analysis_window': {'description': 'Optional preferred date window; otherwise the most recent three months of actual lead creation dates is chosen.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'The Dynamics 365 Sales environment the plugin is bound to for the analysis.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file': {'description': "Name of the Excel workbook to produce, default 'lead-response-audit.xlsx'.", 'type': 'string'}, 'ownership_scope': {'description': 'Whose leads to include — leads owned by you or by your team.', 'type': 'string'}},
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
    print(LeadResponseTimeAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
