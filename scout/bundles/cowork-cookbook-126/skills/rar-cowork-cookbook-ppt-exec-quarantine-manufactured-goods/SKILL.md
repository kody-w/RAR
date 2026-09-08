---
name: "rar-cowork-cookbook-ppt-exec-quarantine-manufactured-goods"
description: "Builds a read-only executive PowerPoint deck on quarantine manufactured goods from Dynamics 365 F&SCM ERP data for a given legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_quarantine_manufactured_goods", "rar_sha256": "b1c7dcd4995051ba6913ea0b5e2131e8703c28621cc8570edd7211d86ee3e820", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_quarantine_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_quarantine_manufactured_goods_agent.py` and in the RCI capsule.

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

Quarantine manufactured goods Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on quarantine manufactured goods from Dynamics 365 F&SCM ERP data for a given legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-quarantine-manufactured-goods
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-quarantine-manufactured-goods-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison, e.g. monthly review as of 2026-05-24.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_quarantine_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 b1c7dcd4995051ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_quarantine_manufactured_goods_agent.py` first:

```bash
python3 ppt_exec_quarantine_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_quarantine_manufactured_goods_agent.py   # or on stdin
python3 ppt_exec_quarantine_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine manufactured goods Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on quarantine manufactured goods from Dynamics 365 F&SCM ERP data for a given legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-quarantine-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_quarantine_manufactured_goods',
    "version": '3.0.3',
    "display_name": 'Quarantine manufactured goods Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on quarantine manufactured goods from Dynamics 365 F&SCM ERP data for a given legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-quarantine-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-quarantine-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f48104c424534fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/quarantine-manufactured-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-quarantine-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-quarantine-manufactured-goods-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison, e.g. monthly review as of 2026-05-24.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for quarantine manufactured goods reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on quarantine manufactured goods for a 15-minute monthly review. Produce 'ppt-exec-quarantine-manufactured-goods-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads quarantine manufactured goods data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on quarantine manufactured goods from Dynamics 365 F&SCM ERP data for a given legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.', 'example_request': "Build the executive quarantine manufactured goods deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-quarantine-manufactured-goods-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly review as of 2026-05-24.', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone needs a monthly 15-minute executive review deck on quarantine manufactured goods status pulled from Dynamics 365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecQuarantineManufacturedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecQuarantineManufacturedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-quarantine-manufactured-goods-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly review as of 2026-05-24.', 'type': 'string'}},
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
    print(PptExecQuarantineManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
