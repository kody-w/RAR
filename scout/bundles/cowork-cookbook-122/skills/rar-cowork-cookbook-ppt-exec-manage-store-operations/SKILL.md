---
name: "rar-cowork-cookbook-ppt-exec-manage-store-operations"
description: "Builds a read-only executive PowerPoint deck on manage store operations from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_store_operations", "rar_sha256": "ce6434072c3088edfcf836b4d6d6a05a24dab6bb8463d6574ae0dc847bf0c5cc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
