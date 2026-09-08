---
name: "rar-cowork-cookbook-ppt-exec-produce-assets"
description: "Builds a read-only executive PowerPoint deck on produce assets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_produce_assets", "rar_sha256": "bf11133fc7aa8b12d0ec997e2e72045003da83fe30ef91e34e5ba3250876aca3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_produce_assets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_produce_assets_agent.py` and in the RCI capsule.

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

Produce assets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on produce assets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-produce-assets
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
      "description": "Dynamics 365 legal entity to pull produce assets data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-produce-assets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Target briefing length the deck must fit, e.g. 15 minutes.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison prior period for the trend chart (e.g. monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_produce_assets_agent.py` and embedded as the fenced Python below (sha256 bf11133fc7aa8b12…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_produce_assets_agent.py` first:

```bash
python3 ppt_exec_produce_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_produce_assets_agent.py   # or on stdin
python3 ppt_exec_produce_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Produce assets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on produce assets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-produce-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_produce_assets',
    "version": '3.0.3',
    "display_name": 'Produce assets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on produce assets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-produce-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-produce-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d12831a0cc19c2a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/produce-assets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-produce-assets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull produce assets data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-produce-assets-2026-05-24.pptx.', 'review_length': 'Target briefing length the deck must fit, e.g. 15 minutes.', 'review_period': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for produce assets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on produce assets for a 15-minute monthly review. Produce 'ppt-exec-produce-assets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads produce assets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on produce assets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive produce assets deck from D365 USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to pull produce assets data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-produce-assets-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review).', 'name': 'review_period'}, {'description': 'Target briefing length the deck must fit, e.g. 15 minutes.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready produce assets deck from D365 F&SCM for a monthly or periodic review, without changing any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecProduceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecProduceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull produce assets data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-produce-assets-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Target briefing length the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review).', 'type': 'string'}},
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
    print(PptExecProduceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
