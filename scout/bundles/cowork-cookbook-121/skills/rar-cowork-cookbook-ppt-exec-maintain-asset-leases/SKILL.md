---
name: "rar-cowork-cookbook-ppt-exec-maintain-asset-leases"
description: "Builds a read-only executive PowerPoint deck on maintain asset leases from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_maintain_asset_leases", "rar_sha256": "60cd9fd4c38f6d2eaef96a1f1050c70bf2b5e4a6471eee9f75fc061c58a8b338", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
