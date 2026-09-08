---
name: "rar-cowork-cookbook-ppt-exec-handle-quarantine-goods"
description: "Builds a read-only executive PowerPoint deck on quarantine goods status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_handle_quarantine_goods", "rar_sha256": "d457c8028541fe9774258418639f65d5e776005d6a95fe069f55e6a882d6a29c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
