---
name: "rar-cowork-cookbook-dashboard-receive-supplier-credits"
description: "Pulls receive supplier credits data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_receive_supplier_credits", "rar_sha256": "2a245b687ee4a38d4a4368be83699cdafd407fd832f9d29bfe042cef576aa5ef", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_receive_supplier_credits`. The original RAPP
agent is preserved byte-for-byte in `dashboard_receive_supplier_credits_agent.py` and in the RCI capsule.

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

Receive supplier credits Interactive HTML Dashboard — Pulls receive supplier credits data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-receive-supplier-credits
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
    "fiscal_period": {
      "description": "Period to report on; defaults to the most recent fiscal period available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query; the recipe uses USMF.",
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
      "description": "Name of the generated HTML file, e.g. dashboard-receive-supplier-credits-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_receive_supplier_credits_agent.py` and embedded as the fenced Python below (sha256 2a245b687ee4a38d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_receive_supplier_credits_agent.py` first:

```bash
python3 dashboard_receive_supplier_credits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_receive_supplier_credits_agent.py   # or on stdin
python3 dashboard_receive_supplier_credits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive supplier credits Interactive HTML Dashboard — Pulls receive supplier credits data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-receive-supplier-credits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_receive_supplier_credits',
    "version": '3.0.3',
    "display_name": 'Receive supplier credits Interactive HTML Dashboard',
    "description": 'Pulls receive supplier credits data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-receive-supplier-credits',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-receive-supplier-credits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b65fe8a6f38d4bc0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/receive-supplier-credits'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-receive-supplier-credits', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Period to report on; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query; the recipe uses USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-receive-supplier-credits-2026-05-24.html.', 'output_folder': 'Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of receive supplier credits with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull receive supplier credits data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-receive-supplier-credits-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing receive supplier credits.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls receive supplier credits data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard of receive supplier credits in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Period to report on; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-receive-supplier-credits-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of receive supplier credits for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardReceiveSupplierCredits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReceiveSupplierCredits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Period to report on; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-receive-supplier-credits-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardReceiveSupplierCredits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
