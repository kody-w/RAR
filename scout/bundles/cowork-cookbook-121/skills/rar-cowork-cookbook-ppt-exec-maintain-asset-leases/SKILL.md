---
name: "rar-cowork-cookbook-ppt-exec-maintain-asset-leases"
description: "Builds a read-only executive PowerPoint deck on maintain asset leases from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_maintain_asset_leases", "rar_sha256": "60cd9fd4c38f6d2eaef96a1f1050c70bf2b5e4a6471eee9f75fc061c58a8b338", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_maintain_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_maintain_asset_leases_agent.py` and in the RCI capsule.

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

Maintain asset leases Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on maintain asset leases from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-asset-leases
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
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-maintain-asset-leases-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_maintain_asset_leases_agent.py` and embedded as the fenced Python below (sha256 60cd9fd4c38f6d2e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_maintain_asset_leases_agent.py` first:

```bash
python3 ppt_exec_maintain_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_maintain_asset_leases_agent.py   # or on stdin
python3 ppt_exec_maintain_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain asset leases Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on maintain asset leases from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-maintain-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_maintain_asset_leases',
    "version": '3.0.3',
    "display_name": 'Maintain asset leases Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on maintain asset leases from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-maintain-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-maintain-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '598665375e5f827b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-asset-leases'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-maintain-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-maintain-asset-leases-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for maintain asset leases reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on maintain asset leases for a 15-minute monthly review. Produce 'ppt-exec-maintain-asset-leases-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads maintain asset leases data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on maintain asset leases from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build an executive PowerPoint deck on maintain asset leases for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-maintain-asset-leases-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a monthly 15-minute executive review deck on maintain asset leases from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMaintainAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMaintainAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-maintain-asset-leases-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecMaintainAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
