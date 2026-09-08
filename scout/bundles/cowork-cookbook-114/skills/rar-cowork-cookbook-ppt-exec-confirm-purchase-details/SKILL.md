---
name: "rar-cowork-cookbook-ppt-exec-confirm-purchase-details"
description: "Builds a read-only executive PowerPoint deck on confirm purchase details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_confirm_purchase_details", "rar_sha256": "158bb33d8eb0f43cea3817de72ea28404ee0c40d15067ca3d167698d80396b51", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
