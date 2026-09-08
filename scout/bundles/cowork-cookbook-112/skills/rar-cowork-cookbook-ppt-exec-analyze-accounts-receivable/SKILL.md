---
name: "rar-cowork-cookbook-ppt-exec-analyze-accounts-receivable"
description: "Builds a read-only executive PowerPoint deck on accounts receivable from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_accounts_receivable", "rar_sha256": "c997a6478e5df10a686f88ffebc8b91332fdf937a35a745bfb4b69457e2245cf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_accounts_receivable`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_accounts_receivable_agent.py` and in the RCI capsule.

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

Analyze accounts receivable Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on accounts receivable from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-accounts-receivable
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
    "comparison_period": {
      "description": "Prior period to chart the trend against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull AR data from, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-analyze-accounts-receivable-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_accounts_receivable_agent.py` and embedded as the fenced Python below (sha256 c997a6478e5df10a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_accounts_receivable_agent.py` first:

```bash
python3 ppt_exec_analyze_accounts_receivable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_accounts_receivable_agent.py   # or on stdin
python3 ppt_exec_analyze_accounts_receivable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze accounts receivable Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on accounts receivable from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-accounts-receivable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_accounts_receivable',
    "version": '3.0.3',
    "display_name": 'Analyze accounts receivable Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on accounts receivable from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-analyze-accounts-receivable',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-accounts-receivable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1528dc0205429bc5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-accounts-receivable'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-analyze-accounts-receivable', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull AR data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-accounts-receivable-2026-05-24.pptx.', 'review_length': 'Length of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for analyze accounts receivable reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on analyze accounts receivable for a 15-minute monthly review. Produce 'ppt-exec-analyze-accounts-receivable-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze accounts receivable data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on accounts receivable from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build an executive AR deck for USMF for our 15-minute monthly review, with trend vs prior period and speaker notes.', 'inputs': [{'description': 'D365 legal entity to pull AR data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Length of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-accounts-receivable-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an AR status deck for a short monthly executive review, built from D365 F&SCM data without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAnalyzeAccountsReceivable(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeAccountsReceivable'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull AR data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-accounts-receivable-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecAnalyzeAccountsReceivable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
