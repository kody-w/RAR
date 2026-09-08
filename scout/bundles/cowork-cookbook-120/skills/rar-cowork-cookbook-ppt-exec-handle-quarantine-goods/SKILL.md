---
name: "rar-cowork-cookbook-ppt-exec-handle-quarantine-goods"
description: "Builds a read-only executive PowerPoint deck on quarantine goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_handle_quarantine_goods", "rar_sha256": "d457c8028541fe9774258418639f65d5e776005d6a95fe069f55e6a882d6a29c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_handle_quarantine_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_handle_quarantine_goods_agent.py` and in the RCI capsule.

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

Handle quarantine goods Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on quarantine goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-handle-quarantine-goods
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-handle-quarantine-goods-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_handle_quarantine_goods_agent.py` and embedded as the fenced Python below (sha256 d457c8028541fe97…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_handle_quarantine_goods_agent.py` first:

```bash
python3 ppt_exec_handle_quarantine_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_handle_quarantine_goods_agent.py   # or on stdin
python3 ppt_exec_handle_quarantine_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle quarantine goods Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on quarantine goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-handle-quarantine-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_handle_quarantine_goods',
    "version": '3.0.3',
    "display_name": 'Handle quarantine goods Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on quarantine goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-handle-quarantine-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-handle-quarantine-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d13dc644022d3f1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/handle-quarantine-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-handle-quarantine-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-handle-quarantine-goods-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for handle quarantine goods reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on handle quarantine goods for a 15-minute monthly review. Produce 'ppt-exec-handle-quarantine-goods-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads handle quarantine goods data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on quarantine goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build the monthly exec deck on quarantine goods for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-handle-quarantine-goods-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when preparing a 15-minute monthly executive review on quarantine goods and you need a ready-to-present deck from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecHandleQuarantineGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecHandleQuarantineGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-handle-quarantine-goods-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).', 'type': 'string'}},
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
    print(PptExecHandleQuarantineGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
