---
name: "rar-cowork-cookbook-ppt-exec-quarantine-manufactured-goods"
description: "Builds a read-only executive PowerPoint deck on quarantine manufactured goods from Dynamics 365 F&SCM ERP data for a given legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_quarantine_manufactured_goods", "rar_sha256": "b1c7dcd4995051ba6913ea0b5e2131e8703c28621cc8570edd7211d86ee3e820", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
