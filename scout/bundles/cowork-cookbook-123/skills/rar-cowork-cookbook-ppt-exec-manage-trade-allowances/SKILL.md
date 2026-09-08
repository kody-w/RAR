---
name: "rar-cowork-cookbook-ppt-exec-manage-trade-allowances"
description: "Builds a read-only executive PowerPoint deck on trade allowance status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_trade_allowances", "rar_sha256": "00d9d7d29d5886b6840fe88c64e2805bb43371cdff8bee22b067d23c5e7e8475", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_trade_allowances`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_trade_allowances_agent.py` and in the RCI capsule.

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

Manage trade allowances Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on trade allowance status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-manage-trade-allowances-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 00d9d7d29d5886b6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_trade_allowances_agent.py` first:

```bash
python3 ppt_exec_manage_trade_allowances_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_trade_allowances_agent.py   # or on stdin
python3 ppt_exec_manage_trade_allowances_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage trade allowances Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on trade allowance status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_trade_allowances',
    "version": '3.0.3',
    "display_name": 'Manage trade allowances Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on trade allowance status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-manage-trade-allowances',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-trade-allowances',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3de1985ec7360c2b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-trade-allowances'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-manage-trade-allowances', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-trade-allowances-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for manage trade allowances reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on manage trade allowances for a 15-minute monthly review. Produce 'ppt-exec-manage-trade-allowances-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage trade allowances data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on trade allowance status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive trade allowances deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-trade-allowances-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on manage trade allowances sourced from Dynamics 365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecManageTradeAllowances(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageTradeAllowances'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-trade-allowances-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly).', 'type': 'string'}},
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
    print(PptExecManageTradeAllowances().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
