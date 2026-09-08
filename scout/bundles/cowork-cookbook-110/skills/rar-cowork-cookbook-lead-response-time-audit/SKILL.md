---
name: "rar-cowork-cookbook-lead-response-time-audit"
description: "Audits how quickly leads owned by you or your team are first worked in Dynamics 365 Sales, and returns an Excel workbook with median and 90th-percentile response times plus untouched leads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/lead_response_time_audit", "rar_sha256": "a911e692ad8ba7c7fa00551bca0e1e518e0a113e42dafb12b0be2e3aca911639", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6WbOjVrbmX1Gf+2D7kpliEIOyoiJaiFEggcSMsyLNDGIUgxC467/3RuectF2VrroV0S+tTFsC9l7z+tZayf71xRv6tG5fPr9okVeteK8osjRqV14Vrvb1WLc5+KpzH/y3CuqqbzN/6Ou2e/nwEkZd0GZNn9UV2L4bwqzvVmk9rm5DFuTFtCoiL+xW9VhF4cqfVlM9rOp2+WpXfeSVK6+NVnHWdv1q4QMWZdWKmSqvzIJuhRH4SvOKqPvwlKWN+qGtOvB7xT6CqHhueUo1Zn26KqMwA4+WlVu4Tz82URtEVZ8VEdjZNXXVRas+K6Nu1RRDtxqqvh6CFLB8yvgJaBM9vLIB7F4+//y3Dy8Z+P3y+deXoPA6cOtFBssub4R0QOepLdhVeFUCHjcTMGIFrgHfuG5LcCuM4tXb1Y9dVMQfVv/93/notUn30+cv1ert8+Vl+XMZqlWfAglrr+uBUIHXeH5WZP30abUrRm/qftN/1QEfVMmn152/Uaqb1V+XZz++MvmURP2PX15qIIK3eOjLy0+L8b+8tMPy+9NCpfnxp09FPUbtjz/9Rqcb/GsU9AsxIPWnr2/Xb2TBwt+WZvHqq6ay+zdebRRkTQSI/06/5fMq+hu5N5N8fV38Y918WH2f8qLPX4G8r1HmA7rfJwtsAHa+fLrWWfXjG4+2vkeVVwXRjz/9GVngfBCjWdf/j+j+/Eo4BVEArPVmkp8+PN33txX0pts3mn/OtgEB859oApa/s/tmqD+j/fTsP5AusgrE/Lsvv0vuexugv65+/lPd/tWGD6v4ywsTFdkdxJ1fRJ9Xvz5D5Ocfwt9u/vC3vwPS/5aMBoAieFL4WnpVFkdd//Xrzz90z9s//O3nH4YGRDEAkq9DW3yP5vfs+uTzBwu+rfrxj3sBf6PKKwBeq285tPq1bv5X+/dPK9MrsvC3+93n1e8zcflAq0WJd6avJvhdNnZA1t/Z8aeXvwPIqYA2Q/B8DPDjv/5rdcyCtu7quF9pQT30K+DgBcMW4fU061bg74IabQTs2mXAsG/rQPwvHl4kruPVL/87eOL4x+ANx9cL5n19h8WvC8mv3oJnv3xa6YBe3WZJVnnF6rJT1S+VlwAgXXg1YEvU3p9g3kcfQRp/XH4sqP3Ln5H8+tz9qZl+eWJz9opzl724YFw3FNGnRRsrjao32QOA4tEjCgZAuKgDIEWcPYsAIF4Xd4CRi+ZdnhXFKswAioBiNL1WiKH6vBD75ZdffK9Lv1SvoIytXqtUtwYLvomz+vgRqBMXWZL2X6ooSOvVD7/+/YfV/1n9q11P4gsPFVSFN9sDCQ+acgLFLBlKsAy4BTgSmONp+1///mZUQKYCZRV4Kouz6HUziEVQ9d4trAm7jyhOrPwIWBZYtWzqtgdIv8r6TysxXn2TFzBdHi21IK1B8QyjJqrCqAomQNUD6nyzZFX3qw4EXBdPH1bDUgIB11/81nuKWIKk9vpfVse9CipPXYD/LWI+F4HNdZUB83/z/+t9QKT9oVvR7yQ+rU5L9K0ar/WatPXeeMTeq19AxXnfDoh7qyoav1RLbY0WUz1T4dU8YBGwTPDm0o+Lz0G7UYK8D7t33s813lIf9WedbL+AWHsN86WTABsB7AOmyZCFC/j/5S2kurQeivBpPyDpQunNC+GbV54xuFT41XuJXy01fvUs8qsvAwojm9X/1/3NouCO5y8sv9NZZsWe9Ivzavilp1sc9NoGgo5jBaLvNcl+60LekeYdcL9URQaiqJ3+8rry6a63Na8gNrSA92V3edIHsQIMv9B9hvISmm27JIH3pXpHdmCF1RPGgDdB3i/WAhHzznB5+i5pCpJ7uf6tyj9d34aLdUC4rprBL0AoxVEU+l6QA6naxbdvfgRxHS2pOaZZkP5BqxWgDsIH0F8BIRZnA9d++oa2r0/fRf/DxtdmZtnybPQGkI3tkwCQI1oEXPy2+BGI17+20EDPz08iQI2y6RfdfZAPQNPXm1EbgTDrsn4JkFe7Rg3A24/L96umy93o0YAUAMYCgd4MwLrP1FhQowStCpABoAPIlDKrQOkGRnkzwpOgVy55DnD0LfZeKT5vvykUPfNpiav3jYsiy56ljK9iIDq4M/0eDvTvhQmgVy4rnnz/MdK+cVtoL5C4JBng+P70td5/ei3Zrz3B6p3u53+aUX78z8aYZxE2/hgAn1dp3zfd5/X6tXC+181PAJDWr7J2zxr68T31Pi4m+vgseH+g96rq59V/JtMfSLzlxOcV8gn+BC+P5LeYevsAE+w/0s7HzfL0S3WJfoNJwL4uQVAtDpsWhHqvae9LQGFL2ihZFr/WuG4pjSOoxk9QB9b/Uv0+yJckAzWjSpag7OrfJf+zuIOAf3XWt9oDHlU94B0urV8SLXPWMyW66OVzNRTFhxeAhtG/mK+WulIuEdwt0xjIFQB8fRY9rzzQo0xd1n0dsyqsx+XWH0dS5fkDFOhX6F8gKQS6rl7X/2VVAwXbMXurWeVSS4GSC8YskLHcARnRLWABytkA6CxOXwXAGs+is9B6NmGge+iialGun5pFm9cRbWnqnqD16P9ctk8rJgIAWXS/z4S3irVU7N8l7KsDgOEDYIUPb+xBkgAHLAZakt3rQPaAxPmuLFF1z9q6WirvP8uz5O0/16bV7/a8AlMxgN5wUdqvAcwtGP2ep+/u+C7vb53vP3O2QBOy0Anrz0s9/vCGiOAbTCsfVt8GD6Dx2yj4HNerAUzZPy9DzxImzy3LD7AHfH3b9O2fKfzo5W/fk+sJm1+XGP5nyU4LFALvL9r9Q1EG8gKe4RAsjohibyj61Q9/xIQnHHx6FN3jh++bBPQNbZdmzdenQ79nGBBWb00G4JdVQTGE3yLi+83H66/X/uM7XAHbZ10BqbAY7zev/Gab+jkdLgICW/av/5jx6wvIQQ8EnPeWhW/jBVgOYPhjt7RZawBQgCG4foUS8Ox/PHi87etSDzTAYKO3RZCI2KJeSPkeGZCxB8M4jviBB0dIhCNUBHsIgkUbNPRiH0F92I/QCPOCZSOBbQG9VyD6uvSQ2SLLIggwwUeAZdFvj8Gt8E2JV6EXC32bc54gk7yli09swEph04m7189+DZkB6cr+qfG3LRHvgoqoUVwwqjtXhrAb6ZQ5KFOhHhxSJo3xhniIJtKSlkuumGZMiFQugugzqyosNbk4uTN3ycW2sBxLsDaHC+QiHmxuDq7Ycb3bW1LdCbaW+dlVP3BVmhfYcDux+bq9cHFmr9ebZo3kD+a2Zq9rW2nxYz/JXLRXpxs8Fk7Lmig5WpFRrLWCbYYLP5m81GiIcriRE/XY78Msin2dx2H/qF3X6zSojoVRuvzZ0g6SGZqFe6fdu5DEN1yrZFWmjGJuvAxGpZ7bXDR1TbW0dx1785Hd2lCqR3jmgsRir1l7RuuOuN1F0rYOB7zajbxOrgmiQ+UWJ6A45oK7cEW2Hayyaw5tDS1wH7a45wqbIGcDMZ2uc0631kFFV2Nt5WZWEOemAYc6t06D6FsRFbIcqK3DFJTG8huRDp3p5Cgspm+pMfLy2dQPrm1g7DTe2AmRGEOvnIkd74WXJ7uYUwrDr0rjOpf7i4kHyLQ9+fPguqUeQvKxgqpjU3G9Cm/kh6LNO0YlYOvmkJwhFZUI0SJVeBcdLiDLhdtcw3gEufNEf6HoabAsb9eNZ/bGaxk/9eSZhChyxg43vrAB9IkHqZhUUeXYQh8DOSuSq+8KKN1KN61Fawl9jNNV360Jr/ZOR3nvWyeMPZlSn1nwxXRT16qkzpNJ9wpRqd/UdhPf5GyfqxIhlbW4teBB96y5CK9iqiaXzGuMIeTdx6A4IbVmD7uRKMrqdrWwsyqYvmHR9YT5bL5J13xG2bC602RFPZjXsa1NcexltkRkQ4JP7XnHEZOHxCctPxNImBfK5WJRKHWK96GVy/DZXT8ukdTogXvTgZdU/45lBDvTIrnZx1h9Gi8qR6a7iX+4lN00V1idhjbmG4sLTcdzqsPMqdcTSmnu465n0xWvz4GnPLY+O028MeyTZh9gkWvEdCqIZ7NaF+rjQVXMZCgUFLZurnYCOlOhuu7TtbLdKHZ2NZNGOQQ53wkalJzRS9V67DlzhtDkXXbe5nIRtcYNqY8Mnm1QV/MVlotEhNOiGwNL8qGAJGTm3DzJHNU+TOh56/bhWWcmWaLYxLt3SSMfHm1u9nRI78/hrMTREIUzZVwCBk30/MzmvnWGOZNtMlQ+kodH8tgK4j0JYKkdw7gUkGPsSI5mH+8XuWzEMy6hQn24tg84fAissruu5/nS5NciHDYHAZY3bjtNm0qB1bI6brFheuSVD+nMvFWP7aBLTqyThmXKjCG7c05ERzdQLvwev+02O8xNcDFb83ZVFHANbxUtnkWWb083bIYCHLGzlLxd+b0UthV5r+WT0ksHdtsFTtP5bN+PeJVJR0sxC+Tumfq+3cRVZRVyntyMGrvmoGaeqkgRheOJ3meVYt499TRfakaiL6MqDvT2fqagWuy21jm9OkQPwZeBoNcsMTmiHmiqnMsndsTUm02wTLDnppvIhsCfO5hESw45H8XNuTsDf0WJwPp2AOmFxYtQiqmJ1kimIgcI14YKmxSuRpQGEhgkv06qsg1PLo8m4+64jovW8MiQBEGohBbLIwIPbVSKII0uhCPgLdeoGZ8SnOAg2fN2yrdOWwpnOcIABLeYYVf3SGPsPQe8Gzw4IbK4YuMrOK7POmzcw4NQ8p7Jljf+3l74OOd3qnS6ukeIclikOhCSO1OivJeU+dAkafpwDukBp48nLufPAbrdhwf0wWPkg1JIoSmPYOZnz7yrGI/TfmPztq0zcI0zJ7XB6f6EtBLW7jrnvDclbZ9s8kARu8p3d6zmDZURj5g3HzgTpZ39MA6krTiWrZUb38ULdtyxd35IN7ySbtLQbunobu1OqcX0oaIXA6EiZQ5FEntsJL1FoOhepci2lpLGvHDXCt6f7Y1reofLFId4Ua5RSdUdOxNBwZUFHdtMoxz54470UJble3uGIXe9poarSg0cs42StYpRhkL2U06IfGZXJbSp+/1px6GupCZ4d3et2nC8NJIrM2jgPUToZNIUtO7g2zlgDLPFd+WGQsv2yvCzWM0JPe5no9W7nRc8RqbqAEbs10eDVtyCKQxFstLNht7aUJjs19PoXEi+iLfZQc+uluyHV/6YORTQRvEPdPnIu4yEjpjO5Cqq0c4DVKAbuNlq+PVhs+FFUTG5v1n4HqMvfBvEyN4s79itU13nrNPhTklLgLxNq90JlD2qkeWLRuAcnYvBtY+QuYPQK4gM34YMb6v1SIjjXT9EDARp0BERU/nUbdvDWZhvqpddWNBdQCEFBU5Enst6NKHLqFhbi3/g4WTZlbxOTjZNZZCU6Ri/PdmBaWh7TZ2MmC0OxnzlFbemHBqvveaayvLpQqUcEzNZLDZGfXNQc5DjG2l1uXoyhPJildXIpMfRhJtJtKeTz2lbThq6zr72RCA6wca7n6VQdrqx9uajdZg3qfLg8uOwUylUaC+IH9oEPs3ymNuPRFLY7hi4oUWCSTM9qNnFybndHPvJNp9MPZmhOczktLty3iOieKx4PO7WqbkJeDfIRzg+3SzvEhC8M/IiUxdKDEosUkIsD4l3rZyOvQRSTNCh6nA+CgA4LGhyj4TprSei6wJLnTKZE/bHvdVmJ5T1ziczM28SdJm4QygTInJHjetmPN9wTwskabNFHKiOeJ1PWC9hiG691nTqvFs/eL/r/OtIZQOns9pA1QIaB3aBlZNgQmEnMlVYpU0/wxd9Y8jCDvQKZxmbyxu0t3ABAlXAJXawit23G4CDXadcUetYo/oRmq8nY6/ACCtEgr1fn2+CFQ2caB/qPLGz5NwcNuyWKeitlznNGWsv2gVggFe3UtDcS4w+XCn3SIeGtYMP0kEXjpfY2HhSICFNF19gdptVbFdASs/UFghztjkTR5IepJQr7cj36VNZhqdK0KyOCvZT6WhX8iR3I5evj8h572FxvYFYjDKbcXKgljLVYasrAx7DPRfnNKxvtmOBxsLBDG/mYxd75t7X5SCJW2f/OHenQnL4ISy0elQOyL21G+bWtPuTcsYPfhKVs6UV5uJkX+RjxM1P4f5+V5LA8LpDvWc8D8rvx4dD6Uh1upoBMip2qZH7hHTOwNGNvG2Fq896yGnuLej0cPfyQOyV9OFbWrjTmSvjbA7S3mVHPsk0K08k02g5xaHSWm2RraElfSGt8enoXRzSafWRbpB7Smf1dcd5hprTD9zVcuyU32b9kvZ4EYutKrZsd8Ow3WV3r2+5dyskorzuHxeWjo6Xa+6oByqv/T46WnMe85crIkTNwfRgVWEC7yFrpJTEk1RarifIc3ayDu6j6KfJnDZQfqb62dyjTM9UxXQlWeUG+zrqs+hhzQy8zXqKUuyYQjufYZNWjUMjn+HrXtuYylUxlIHH6nPNM4ly52Fsvs75/UzUTujCeCEfjKkdr2vxnHgIVMzJ7mAU/flx9FCLrYtbv2auCN9O6tW+p8h4AtSKE9+Hs1DOD5XEDqxql2eOqwKzqcxrupXDltzHfucW59Og0fkGpaHJtlquDlnS85p+/dBvDtJiuCWdhrEv4XhOuKwvYzuwvRPlPggvtV2DOFy9ljkraGdGkSPptnjST7OooSaqu7jRdmdyPGH7MGJrgbApjdoxSD8zm9m7ZI1C5beql92SsI+tQ5MVjxBJWw1Oi+/js6BGkjnn/MMuPet4GvuQDIj7Xk/PUXzZsiCp0YxntP3YxOY6vQuTCpk3gFGbge5SohnxiDrimmr68UAb9+roy9tGu1XjOWVp9HELbf5so3Y0+si97/jd9pwqgiCXZ2F7msh9ZG5p/EyFhWmV1LSZD7eHnqe7EBIxHw5sS0OPaXkpUdokHiGctDyMO+5siu4hynflViTVgZTYLB2oXKF29/JhbMriNtIHjkXwC8iDQithGeugeS1wkzsKrlLrHK271UYolIODOIh1XofJEPCXgZegRha5qMoHIxNRuD/FSoDuJQEUy+M61xisZY/Y9jLGJN9u8nST0M1Yb+Atkd2a2l8zJeYYyR2+0pxxvZO3oZWSc5mk9sH0R9Cw7IXpkuecsmn1Q7/pCX66dgzoCGhFiTBIsC5HgAd62bNoPUu9eSn20aQp7KXUj7BobRh3a+bnVL1R6/ko0bLeMH2jozw/YujYI2J3p1yUtKdRqM4GDBCwoxu6QjbcbQ8r43VoIXFQtVvDebu1aU0Oy+lHHUNFaB9WLl+Hmyuk70jiliq0PIl6sQvOl8N9100CTJ3u/FXPWx9FYV+oMoUeS0WDMPWc8dSxtpJke4+jy9glkWRk8iRp8DyU+ybcEJrOoax2Tj0b53KH4B47ZZabmblslVw1vIRVDXjaHylYpnU+jM89jcc56lAMk8mBsLfy0z64ErwCd10fzQ8XhTXKPhzK9sCPVltbG3raze6N8Q6g9xQu4xG/MCOa77SEikjQKiVjSJfNxTf8eBxOWhterOzYRS2CaESax4wviGs0g3Q9lq64ET/4y6xGR0XMdmWKyXveCLXSOIxOwMyHCTGYy0OaOiLC5XMC+mGrke/leEgLU6T8bZZvsFuVdxjFnSVXVMrtRhUmf1J8eq0nOwSgKTXppcjcIQueuDHHNVpA4IhKOy8XmUF5GKVqJhB2F/FIdEPDbyLUnstdvdcRI3mwXCui0jRqtEs11wplskt0gtweBWO2qa+hlFOkxr9lWOXdJNNUqKSDUO7hJ8fTGt0cFJPMT9dGiq5VH0xJskvT0cK48mhgWQIqEOcHXszgd1vuFEhInCqjTuoa1S5sbuGSKSIN9Th0F5Pd3jZHER2EfWIeU4pj/Mcx3VK6mLXa2nARitNymMEtcmbULIcPyc3nQniD5zF08tJSnPMzoislEYeNvy10U+w4CRuVwidjCMCy3YXWvRDuLrTZ3O6s8Tib/easJkJihm0bCxqq5fEpo3V43ZyHe0zjHp7QNuqP6l3ecZLlwo/DbcdRfh/ccNYrjzsMsiCJNUPb8I0Heiib01XrTp1IMsL+mitHu3EmwT7tQXlpyHuZOkeLHoR1RQgCIg4xIde7vIQqp+8CIhyvQcIfGDBaTaIkIPQew6yBICJBZ6lG4Q+TEl6RHiEypa6zGX8Y1SiTKalsiCxEH1EU104n2bZQk5ucFVTlATFY5/LJRjkFyt0ikCmelbLW09sdIoNgLO4YPmE2RRBHpMPsa60nWBxG4bit0b5sKluvhUIVrJIgDsos3NTLOkkcXjkorrb1tqqdxAlU449726eqWrV9Cz+QnOIVhLRvG8+OJ7VyYJLnEy/QUTmmtm4oGZhi6kPijGgBo9oeNA4B5hqmuhnWbn6Py8IPYYgr7ttJpII2bi0M7d241uHavw+6s5YHs1f34bbzUt3eRggYWWClQuujOt+iXmaUc8H6w2YjkIUO22D0odcb08MNyz3eUWKKH/6G6eSEwDuKlCWkHHSRGfG9ZmfXht9k6eSAwYmNomp7ZKMgViqBN1mEyWNccyaYxiWFlNnDI4Xogyw0yrlWGuKs1sN1s3XgC3uLlBDROwOjyBAgDsq2LsfbXHJDIEwKaOrxwPY2T9Id30TZ2mCQGF2rql7vI8zd05yUJXm75THbsnN3zdZ2g+7W98rTg/Q84hYD514LN814EvCWXRNAR6saCrZDC9tm9G66qBeCT+Og1aC5bJEgNq/9zF9oE55V8ZCfxTYfg9O9HpSBVObNmR3ZhEf77TmT0YHqpLV/vIA5dCJP2zpsHnZiKVjGONcUc7F6G+L6sWNxnq62rQujSammajXBmehBk1h4F/Hi+qwv0AlUDsTgqkZzlujqyh317fb4YIziIRJD38dGyTR7uqCOiiCVo5DPNWhyj2E26jq/xXd47z6oTbSWbDfWPCp/CERXcOuYSav1Bi6NuaNH+ZFGjlVETgtqzH3bnRMiE6xKyYOgpQ/pJnQBDjvr7T6NxWvX3MxhLVTwSXJJUR3bfdWH4okJBzc7ENvrAXTEwSwSR7dVz9Jh8DuhawK6Yu6npmn8IVH6DkNgzj/0UR8Fx/E62axitzYf7RQ4ZoZhr3RtIt8rKEQPGXGFt9jduSf8g9QvqLIp6SaTlV5RwiEeZ0dPPJk8UfkGHta97mv5xOwsLL1kylyALrKdu6N9VM+cThkSvGFs57if6HUFxkoCmmownVCqfGWM2OW2+kFGhN7W+9xsS1Y9KlioW4cu5rcehAQejLpedKowpKog/JFlzmONQjFpyENwsV3fnOXZhWbWWI/T3iogQ6Xv0MXRtmisOCyVoVgz+A9FHmwq2ggP8oKe23VWt8Mpn4itTHDoMNHlcTOk5rwjx1Q3C20XjK3bs3KoowXRWnV8dBtY9pO6iSpNoygwqQjjQNiKvIEVvBAgefAEGitjACYJritTlTHmHrqHmdIJowd8NzM37BpdIRUraIPc9YVIHE6QZkiXbYzCcXq8zxMnplcGOku2bkBep6WZOzeHG8+MXFHeblNm2FdlLYk7SFC7Sxps1J7rohzNTbQPyDlMLLMxwiIUVd6ZhbV3I7MYV+a+vnQ70qF2zSApZzY1xfKCMTZR89uB6eJ7Oon4dJrOzZqdAxkiypA49NJaavNOYnLSmwcS5Nipa8/BbdtroO1wcUcyyTiVPZPDZ1mZ+h7Fs3uobaYG16xRb7HgOIEp0uzcG0LXQR4I66C/0iNFXE/9XKgqJAa6K+HYbY+pD8HE7+1wSzqxzo8VvWViMQ6Hg4/lCRHBZjap22nUwRzrCQ2923YzAnuFZ5xi7Hhzew9KtSjHIr5SdppeJ5Rf2pWFY6QWIsSQhEXVH3tZabf6mu+tCz6RCI4kNbLWDxV+6A06N4vsrElbbq4SFnH4MRJ4LO7jS7/Wh3O8rZp2mDmImaqqjfjLHYU4rTIVCMVD/5KvT43RF5SaTZaHk2Z1bfO7W5MPQgIIsY7gRiea/VRZQjoek/Mp1nFYrrxChljZj1xQIFB1ZhpkRuooAuVlHejrg5N3DtfUzN7teg5pE0AG8glyVwzhJWPIlAWRjmGsk7D8A9bO9pWNyW63Oe370T9tu5sQ3mVH0OGAE2D7wcxHIqYRVbbCsIc6bsueDpdtmnlCbYDgvIXEPBJTe0M3+b2GIjLaDuTtqlCzgArrosWUiJxwHyKjB37altRpEOCqEWI6IVNcoGg430BEbyJ8Q1qjdYJgrg9xyqKKUA2xMmry7eMBIR2OjGVr7e0RUw5tbw4btB2wu7JrjzfqXMEkjUJuKj/oDYWydwYTuQqJ7zPftkW0tzC3CteX0/VKM+R9uz+LiXwzdWzvOfsuSW5RuT+056u/m/Z8gXG2kWKtrZ3zTXDFel1NQxodiyYXa4VMIYOZtItj68PBDmp5e7siW8jxNTVoq7V9R1KVq26iD23ckGy5u35Wadz0JRrtKLvFjm3Su6eNsLE8zCgzqRQctlfscyC7MbId7+v7BqL4Ykd29KVSiTvf72zfPFQUKHI8eErXJNHOm0CfR/SkaLG1p7bCfVR3ueOZKrK8L/zry4eX5R3z22mHf3tacnlD+f/sZejrO833w1LPl+aA/+cnr8//XpS/fXhpgwwI8vqCtyuG5O2V6T+83v34Z2dill3T64HD9+MQr4c/ei9Zztu/ZFU4dH07fe3q4nk0Cuzwh245qtstp7kD8P37t/zvVMGNbjn/9LWvv96Gul/e7GbVct5pOS737TJ5e8n94SV8O+HwFSPwr91ywmFR7+2MDdAK+wR/wl7+/n8B0xVnbBYxAAA= -->
