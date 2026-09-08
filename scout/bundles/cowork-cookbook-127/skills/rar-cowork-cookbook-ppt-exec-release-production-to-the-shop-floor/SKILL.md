---
name: "rar-cowork-cookbook-ppt-exec-release-production-to-the-shop-floor"
description: "Builds a read-only executive PowerPoint deck on release-production-to-the-shop-floor status from Dynamics 365 F&SCM data, with title, KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_release_production_to_the_shop_floor", "rar_sha256": "cda0d55284188e6cfea15c55343c1a30bbdd44035202948dd9472a7156da5dab", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
