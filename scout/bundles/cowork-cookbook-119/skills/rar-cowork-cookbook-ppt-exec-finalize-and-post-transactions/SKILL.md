---
name: "rar-cowork-cookbook-ppt-exec-finalize-and-post-transactions"
description: "Builds a read-only executive PowerPoint deck on finalize-and-post transactions from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_finalize_and_post_transactions", "rar_sha256": "32a913283bf5f84c9b162ee2e0001aca09c4a36047c458ce8ee514c6293e9974", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
