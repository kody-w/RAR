---
name: "rar-cowork-cookbook-ppt-exec-confirm-purchase-details"
description: "Builds a read-only executive PowerPoint deck on confirm purchase details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_confirm_purchase_details", "rar_sha256": "158bb33d8eb0f43cea3817de72ea28404ee0c40d15067ca3d167698d80396b51", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_confirm_purchase_details`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_confirm_purchase_details_agent.py` and in the RCI capsule.

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

Confirm purchase details Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on confirm purchase details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-confirm-purchase-details
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
    "legal_entity": {
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-confirm-purchase-details-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_confirm_purchase_details_agent.py` and embedded as the fenced Python below (sha256 158bb33d8eb0f43c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_confirm_purchase_details_agent.py` first:

```bash
python3 ppt_exec_confirm_purchase_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_confirm_purchase_details_agent.py   # or on stdin
python3 ppt_exec_confirm_purchase_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Confirm purchase details Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on confirm purchase details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-confirm-purchase-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_confirm_purchase_details',
    "version": '3.0.3',
    "display_name": 'Confirm purchase details Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on confirm purchase details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-confirm-purchase-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-confirm-purchase-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16da316e98e37a91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/confirm-purchase-details'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/ppt-exec-confirm-purchase-details', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-confirm-purchase-details-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for confirm purchase details reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on confirm purchase details for a 15-minute monthly review. Produce 'ppt-exec-confirm-purchase-details-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads confirm purchase details data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on confirm purchase details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': "Make an executive PowerPoint on confirm purchase details for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-confirm-purchase-details-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly review deck on confirm purchase details status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecConfirmPurchaseDetails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfirmPurchaseDetails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-confirm-purchase-details-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecConfirmPurchaseDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
