---
name: "rar-cowork-cookbook-ppt-exec-produce-assets"
description: "Builds a read-only executive PowerPoint deck on produce assets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_produce_assets", "rar_sha256": "bf11133fc7aa8b12d0ec997e2e72045003da83fe30ef91e34e5ba3250876aca3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
