---
name: "rar-cowork-cookbook-ppt-exec-release-production-to-the-shop-floor"
description: "Builds a read-only executive PowerPoint deck on release-production-to-the-shop-floor status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_release_production_to_the_shop_floor", "rar_sha256": "cda0d55284188e6cfea15c55343c1a30bbdd44035202948dd9472a7156da5dab", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_release_production_to_the_shop_floor`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_release_production_to_the_shop_floor_agent.py` and in the RCI capsule.

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

Release production to the shop floor Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on release-production-to-the-shop-floor status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-release-production-to-the-shop-floor
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-release-production-to-the-shop-floor-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_release_production_to_the_shop_floor_agent.py` and embedded as the fenced Python below (sha256 cda0d55284188e6c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_release_production_to_the_shop_floor_agent.py` first:

```bash
python3 ppt_exec_release_production_to_the_shop_floor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_release_production_to_the_shop_floor_agent.py   # or on stdin
python3 ppt_exec_release_production_to_the_shop_floor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Release production to the shop floor Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on release-production-to-the-shop-floor status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-release-production-to-the-shop-floor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_release_production_to_the_shop_floor',
    "version": '3.0.3',
    "display_name": 'Release production to the shop floor Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on release-production-to-the-shop-floor status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-release-production-to-the-shop-floor',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-release-production-to-the-shop-floor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'da4d97241f24c88f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/release-production-to-the-shop-floor'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-release-production-to-the-shop-floor', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-release-production-to-the-shop-floor-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for release production to the shop floor reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on release production to the shop floor for a 15-minute monthly review. Produce 'ppt-exec-release-production-to-the-shop-floor-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads release production to the shop floor data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on release-production-to-the-shop-floor status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build the monthly exec deck on release production to the shop floor for USMF.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-release-production-to-the-shop-floor-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (monthly review).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on release-to-shop-floor production status from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecReleaseProductionToTheShopFloor(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecReleaseProductionToTheShopFloor'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-release-production-to-the-shop-floor-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (monthly review).', 'type': 'string'}},
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
    print(PptExecReleaseProductionToTheShopFloor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
