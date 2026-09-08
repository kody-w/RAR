---
name: "rar-cowork-cookbook-project-margin-health"
description: "Compares active D365 project budgets to actuals by cost category, flags projects whose current margin is under 80% of the original quoted margin as Red, outputs an Excel workbook, and drafts (does not send) PM emails."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/project_margin_health", "rar_sha256": "f640c10599de0999ed48edddea0ab0b7afe2e5b8d174fef239d42e2cacb1f2e6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
