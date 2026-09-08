---
name: "rar-cowork-cookbook-ppt-exec-analyze-accounts-receivable"
description: "Builds a read-only executive PowerPoint deck on accounts receivable from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_accounts_receivable", "rar_sha256": "c997a6478e5df10a686f88ffebc8b91332fdf937a35a745bfb4b69457e2245cf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
