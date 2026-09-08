---
name: "rar-cowork-cookbook-ppt-exec-finalize-and-post-transactions"
description: "Builds a read-only executive PowerPoint deck on finalize-and-post transactions from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_finalize_and_post_transactions", "rar_sha256": "32a913283bf5f84c9b162ee2e0001aca09c4a36047c458ce8ee514c6293e9974", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_finalize_and_post_transactions`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_finalize_and_post_transactions_agent.py` and in the RCI capsule.

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

Finalize and post transactions Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on finalize-and-post transactions from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-finalize-and-post-transactions
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
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-finalize-and-post-transactions-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review as of a date).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_finalize_and_post_transactions_agent.py` and embedded as the fenced Python below (sha256 32a913283bf5f84c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_finalize_and_post_transactions_agent.py` first:

```bash
python3 ppt_exec_finalize_and_post_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_finalize_and_post_transactions_agent.py   # or on stdin
python3 ppt_exec_finalize_and_post_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize and post transactions Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on finalize-and-post transactions from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-finalize-and-post-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_finalize_and_post_transactions',
    "version": '3.0.3',
    "display_name": 'Finalize and post transactions Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on finalize-and-post transactions from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-finalize-and-post-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-finalize-and-post-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5296879bb19c44b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/finalize-and-post-transactions'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-finalize-and-post-transactions', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-finalize-and-post-transactions-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a date).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for finalize and post transactions reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on finalize and post transactions for a 15-minute monthly review. Produce 'ppt-exec-finalize-and-post-transactions-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads finalize and post transactions data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on finalize-and-post transactions from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build an exec PowerPoint on finalize and post transactions for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-finalize-and-post-transactions-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a date).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly review deck on finalize and post transactions status from D365 ERP, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecFinalizeAndPostTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecFinalizeAndPostTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-finalize-and-post-transactions-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a date).', 'type': 'string'}},
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
    print(PptExecFinalizeAndPostTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
