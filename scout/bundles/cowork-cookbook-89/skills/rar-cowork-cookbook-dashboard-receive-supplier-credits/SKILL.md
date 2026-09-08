---
name: "rar-cowork-cookbook-dashboard-receive-supplier-credits"
description: "Pulls receive supplier credits data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_receive_supplier_credits", "rar_sha256": "2a245b687ee4a38d4a4368be83699cdafd407fd832f9d29bfe042cef576aa5ef", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
