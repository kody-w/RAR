---
name: "rar-cowork-cookbook-project-margin-health"
description: "Compares active D365 project budgets to actuals by cost category, flags projects whose current margin is under 80% of the original quoted margin as Red, outputs an Excel workbook, and drafts (does not send) PM emails."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/project_margin_health", "rar_sha256": "f640c10599de0999ed48edddea0ab0b7afe2e5b8d174fef239d42e2cacb1f2e6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/project_margin_health`. The original RAPP
agent is preserved byte-for-byte in `project_margin_health_agent.py` and in the RCI capsule.

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

Project Margin Health Report — Compares active D365 project budgets to actuals by cost category, flags projects whose current margin is under 80% of the original quoted margin as Red, outputs an Excel workbook, and drafts (does not send) PM emails.

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
  Upstream entry : https://coworkcookbook.com/recipes/project-margin-health
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
    "active_project_filter": {
      "description": "Which projects count as 'active' \u2014 adjust for tenants with older data (e.g. USMF demo has FY2017 project data).",
      "type": "string"
    },
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
    },
    "report_date": {
      "description": "Date used in the workbook filename Project-margin-<YYYY-MM-DD>.xlsx; defaults to today.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `project_margin_health_agent.py` and embedded as the fenced Python below (sha256 f640c10599de0999…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `project_margin_health_agent.py` first:

```bash
python3 project_margin_health_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 project_margin_health_agent.py   # or on stdin
python3 project_margin_health_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Project Margin Health Report — Compares active D365 project budgets to actuals by cost category, flags projects whose current margin is under 80% of the original quoted margin as Red, outputs an Excel workbook, and drafts (does not send) PM emails.

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
  Upstream entry : https://coworkcookbook.com/recipes/project-margin-health
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/project_margin_health',
    "version": '3.0.3',
    "display_name": 'Project Margin Health Report',
    "description": 'Compares active D365 project budgets to actuals by cost category, flags projects whose current margin is under 80% of the original quoted margin as Red, outputs an Excel workbook, and drafts (does not send) PM emails.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'project-margin-health',
        "upstream_url": 'https://coworkcookbook.com/recipes/project-margin-health',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b1f16a68ad5cd83d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/project-margin-health', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Project manager role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: Workbook with red/all/by-PM project margin sheets and one email draft per Red project.'], 'confidence': 1.0, 'deliverable': 'Workbook with red/all/by-PM project margin sheets and one email draft per Red project.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'active_project_filter': "Which projects count as 'active' — adjust for tenants with older data (e.g. USMF demo has FY2017 project data).", 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'report_date': 'Date used in the workbook filename Project-margin-<YYYY-MM-DD>.xlsx; defaults to today.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Catches project margin erosion mid-flight (instead of at close-out), so project managers can act on overruns while there is still time to negotiate a change order or replan.', 'expected_output': 'Workbook with red/all/by-PM project margin sheets and one email draft per Red project.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Project manager role', 'Cowork D365 ERP plugin enabled'], 'prompt': "For every active project, compute: total budget, actuals to date by category (hours, expenses, items), and current expected margin vs the original quote. Flag projects with current margin < 80% of original margin as 'Red'. Output an Excel workbook 'Project-margin-<YYYY-MM-DD>.xlsx' with a 'Red' sheet, an 'All' sheet, and a 'By PM' summary. For each Red project, draft an email (do not send) to the assigned project manager naming the specific cost categories that have overrun and the dollar impact. (Tenant note: USMF demo has FY2017 project data — adjust 'active' filter if needed.)", 'steps': ['Paste the prompt.', 'Review the workbook; release the email drafts after personalizing tone.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork scoped 'active' to Project Status = In process + Project Type = Time and material or Fixed price, yielding 6 projects (000057-000061 + 000184). Real workbook ProjectMargin-2026-05-23.xlsx with Red / All / By PM / Notes sheets, and an email draft saved to Outlook (not sent) to Prakash@contoso.com about the one Red project: 000184 San Diego Subscriptions ('In process' but zero posted transactions, PM Prakash Kovvuru). Honesty notes: USMF carries no quotation headers tied to these projects so Cowork used a 50% target margin as the original-quote baseline (typical T&M services benchmark), with the Target Margin column editable per project; 5 of 6 active projects have no PM assigned in F&O; all Fee transactions in this demo carry $0 cost.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Identifies projects with margin erosion and routes specific overrun information to the responsible PM.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Compares active D365 project budgets to actuals by cost category, flags projects whose current margin is under 80% of the original quoted margin as Red, outputs an Excel workbook, and drafts (does not send) PM emails.', 'example_request': 'Run a project margin health report on active projects and draft emails to the PMs of any red ones.', 'inputs': [{'description': "Which projects count as 'active' — adjust for tenants with older data (e.g. USMF demo has FY2017 project data).", 'name': 'active_project_filter'}, {'description': 'Date used in the workbook filename Project-margin-<YYYY-MM-DD>.xlsx; defaults to today.', 'name': 'report_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a project margin health check across active projects, with a Red/All/By PM workbook and unsent email drafts for overrunning projects.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Review the workbook; release the email drafts after personalizing tone.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ProjectMarginHealth(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProjectMarginHealth'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'active_project_filter': {'description': "Which projects count as 'active' — adjust for tenants with older data (e.g. USMF demo has FY2017 project data).", 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'report_date': {'description': 'Date used in the workbook filename Project-margin-<YYYY-MM-DD>.xlsx; defaults to today.', 'type': 'string'}},
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
    print(ProjectMarginHealth().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
