---
name: "rar-cowork-cookbook-ppt-exec-manage-store-operations"
description: "Builds a read-only executive PowerPoint deck on manage store operations from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_store_operations", "rar_sha256": "ce6434072c3088edfcf836b4d6d6a05a24dab6bb8463d6574ae0dc847bf0c5cc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_store_operations`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_store_operations_agent.py` and in the RCI capsule.

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

Manage store operations Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on manage store operations from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-store-operations
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
      "description": "Dynamics 365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-manage-store-operations-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_store_operations_agent.py` and embedded as the fenced Python below (sha256 ce6434072c3088ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_store_operations_agent.py` first:

```bash
python3 ppt_exec_manage_store_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_store_operations_agent.py   # or on stdin
python3 ppt_exec_manage_store_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage store operations Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on manage store operations from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-store-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_store_operations',
    "version": '3.0.3',
    "display_name": 'Manage store operations Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on manage store operations from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-store-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-store-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06974d93d1d609e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-store-operations'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-manage-store-operations', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-store-operations-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for manage store operations reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on manage store operations for a 15-minute monthly review. Produce 'ppt-exec-manage-store-operations-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage store operations data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on manage store operations from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an executive store operations deck from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-store-operations-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready store operations deck for a 15-minute monthly review, sourced from D365 F&SCM without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecManageStoreOperations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageStoreOperations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-store-operations-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecManageStoreOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
