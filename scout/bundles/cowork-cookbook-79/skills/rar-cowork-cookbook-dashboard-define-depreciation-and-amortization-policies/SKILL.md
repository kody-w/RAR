---
name: "rar-cowork-cookbook-dashboard-define-depreciation-and-amortization-policies"
description: "Pulls depreciation and amortization policy data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies", "rar_sha256": "02713ddfaa76f548c2925e8cbfa901e3c65bc8079e88e2855b15a54ed97baee5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_depreciation_and_amortization_policies_agent.py` and in the RCI capsule.

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

Define depreciation and amortization policies Interactive HTML Dashboard — Pulls depreciation and amortization policy data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies
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
      "description": "Fiscal period to report on; defaults to the most recent available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-depreciation-and-amortization-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_depreciation_and_amortization_policies_agent.py` and embedded as the fenced Python below (sha256 02713ddfaa76f548…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_depreciation_and_amortization_policies_agent.py` first:

```bash
python3 dashboard_define_depreciation_and_amortization_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_depreciation_and_amortization_policies_agent.py   # or on stdin
python3 dashboard_define_depreciation_and_amortization_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define depreciation and amortization policies Interactive HTML Dashboard — Pulls depreciation and amortization policy data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies',
    "version": '3.0.3',
    "display_name": 'Define depreciation and amortization policies Interactive HTML Dashboard',
    "description": 'Pulls depreciation and amortization policy data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-depreciation-and-amortization-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aebc8e176aa5cfa4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-depreciation-and-amortization-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-define-depreciation-and-amortization-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-depreciation-and-amortization-policies-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define depreciation and amortization policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define depreciation and amortization policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-depreciation-and-amortization-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define depreciation and amortization policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls depreciation and amortization policy data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out', 'example_request': 'Build me an interactive HTML dashboard of depreciation and amortization policies for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-depreciation-and-amortization-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 depreciation and amortization policies for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineDepreciationAndAmortizationPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineDepreciationAndAmortizationPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-depreciation-and-amortization-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardDefineDepreciationAndAmortizationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWJbnV9G8jph0NvYDBELgiooYEIuQhITYhJTOcLLv+67s/O5zkZ6XrHL1dFX3XyM7UwLuPfv5nXN8+f3F6tqwqF8+vqielS8EK02j0KsXVu4uNsVQ1An4KhIb/LdwirytI7tri7p5ef/ieo1TR2UbFTnYLndp2ixcr6w9J7Lmmw8aVlbUbXR/3iiLNHKmhWu11sKvi2zBTrmVRU6zwIjVgv/f6kZa+AVgvgii3ssXqRdY6cLL26idHtT8qHHAndKro8J93BnqqPUasKNpwaWVFrm3iPLWqy2nBTQWW006AIZNaBdW7S7eqYawcEKrbpv3iwaIZtmpt3j8//1CoQWw140cC2j486ItFm3oLYquBcp6o5WVqde8fPzl1/cvEfj98vH3Fye1GnDrhf3CgPX8KPfY76xA5y79nQ3k2QSRN9svtfIA7C0n4IAcXAOtgPIZuOV6/uLt6l3jpf77xb//ezJYddD8/PFTvnj7fHqZ/yhd/hCzLaym9dyFY5WWHaXAYq8LOh2sqVnUXtvV+dNIdZQHr8+d3ygV5eKv87N3Tyavgde++/RSABEeMn96+XkBvPLppe7m368zlfLdz69pMXj1u5+/0Wk6O/acdiYGpH79/Hb9RhYs/LY08hefVZnbvPGazVV6gPh3+s2fp+hv5N5M8vm5+F1Rvl/8mPKsz1+BvM8ItQHdH5MFNgA7X17jIsrfvfGoCxB5Vu54737+R2Sd0HOSNGra/xLdX56EQ89ygbXeTPLz+4f7fl1Ab7p9pfmP2ZYgYP4ZTcDyL+y+Guof0X549m9IpyCSm6++/CG5H22A/rr45R/q9p9teL/wP72wXgrStp4T8uPi90eI/PKT++3mT7/+AUj/P8moRVc7DwqfMyuPfK9pP3/+5afmcfunX3/5qStBFHtW9rmr0x/R/JFdH3z+ZMG3Ve/+vBfw1/MkL4Z88TWHFr8X5f+q/3hdGFYaud/uNx8X32fi/IEWsxJfmD5N8F02NkDW7+z488sfAI9yoE3nPB4D/Pi3f1tIkVMXTeG3C9UBCLYADm6jzJuF18KoWYC/M2rUHrBrE80g+FwH4n/28Cxx4S9++z/OowZ8cN5qAPwVSj+7D6j7/D3ifwYQ/Pl7xP9cvsHdb68LbcbSOgqiHCC4Qsvyp9wKALbPogASjVf3AL7sqfU+gCz/MP8AaLz47V/k+PlB/LWcfnvUieiJkspGnBGy6VLvdbbFJQRl5qm5A8qfN3pOB/imxVxm/AgA/ntgo6ZIQSlpZ7s1SZSmCzcCEoAi8axKwLYfZ2K//fabDYT9lD8hHVs862MDgwVfxVl8+ADE99MoCNtPueeExeKn3//4afEfi/9s14P4zEMGBefNc0DCnXo6LkAmdhlYBpwKwgDAzMNzv//xZnNAJgcFHfg58oFdHptBJCee+8UB6pb+sFwRC9sDhgdGz8rZnnmwiNrXhegvvsoLmM6P5koSFk07V3svd70c1PQ2tIA6Xy2ZF+2iAQ5p/On9omu8B9ff7Np6iJgBSLDa3xbSRgZ1q0jnUlu/1TGwuchBCU6/hsfzPiBS/9QsmC8kXhfHOXYXpVVbZVhbbzx86+mXuYt42w6IW4vcGz7lc9n2ZlM9QuVpHrAIWMZ5c+mH2eeg0ckAarjNF96PNdZcXbVHla0/5c1bklj17AoHFA3ANOgidy4df3kLqSYsutR92A9IOlN684L75pVHDD57hv9K6zS7T/zb5uZr77H41C0RFF/8/9yJzfaiBUHhBFrj2AV31JTr049zczr7+9nPzmLO8j9y9ltL9AX2vqD/pzyNQFDW01+eKx/ef1vzRNSuBs5SaOVBH4Qe8ONM95EZc6TX9ewU61P+pcy8BxZ4YCqwMoARkGaz+F8Yzk+/SBoCW8zX31qORyTVD3OC6F+UnQ28tPA9z7UtJwFS1XN2v7k5nw0MMn0IIyf8k1azn0A0AvoLIEQE8hWUotev0P98+kX0P218dlbzlkfX2YHkrh8EgBzeLODD0VELMM5qn7MA0PPjgwhQIyvbWXcbxBjQ9HnTq72qi5o5Nt6/2dUrAbp/mL+fms53vbEEGQWMBZxcdsC6j0ybQSgDfROQAQQ0iKUsykEfAYzyZoQHQSubYQPA8luj+6T4uP2mkPdIz7kAftk4KzLveUTdIwOsfPoeXbQfhQmgl80rHnz/NtK+cptpzwjbAJQEHL88fTYfr8/+4dmgLL7Q/fh3w9a7f24ee3QE+p8D4OMibNuy+QjDzyr+pYi/AnyDn7I23wr6h2d5/fA9cHwAbD98DxwfvuDQn9g9LfFx8c+J/CcSbynzcYG+Iq/I/OjwFnJvH2ChzQfm+gGfn37KFe8bKAP2RQbEm/05gQ7iawX9sgSU0aAGCAYWPytqMxfiAdT+RwkBzvmUf58Dcw4CaMoD74FN32HDo5UA+fD05ddKBx7lLeDtzm1q4L3O090sfuO9fMwBHL9/Aejq/auD4lzisjn6m3nmBHkGULedH80T6AwmYzv//PM8fnr8sNLXBesB4Eqb7yP0rTDNhfm7RHpqDjR2AIf3c3EA+ACCF2g+M5+T0GpAVIOAnjVsp3JW6TlTzl3osyZ8ftaEv5eI/1PJmEv+o5sAGPUXkNy+1aXAsG9Qn83tBZDngeg9EH/O0x8yfVSmz8/K9Pc82bmc/al4AQZVB9Dg/cJ7DV4XuirxP6T7td/+e6IX0LzMdNzi41zH379BH/gGM9L7xddxB5jwbQCdOXh5B2b7X+ZRa/bpY8v8A+wBX183ff2HFdt7+fVHcj3w8fMcjc+Y+lvpjjPugbowm/FRcx+BC8R9FOg3tf/FrP+wRJbEB2T1YYm/hm2W/thybxIWKageP3CJN+P6sw15rvmKkN9S+pvg79jCeba38BNM4Cd9+OcfMAfcH+UGFO3Z1N98+M2SxWOCneUElm+f/+Dy+wtIL2tuht4S7G0EAssBOn9o5mYOBsAEGILrJ4SAZ/9Tw9Eb2Sa0QBcO6CLLNYq5rm9Za8Jf4aSzpJYrj3Rs36IQ1MMcYmU7JLKmPJL0luRqZaMra4V7LrW2Lc9bAXpPfPo8N7LRLOqKWvsIRS19HF0iLpBuibsuSZCEs1ovEYuyrZW9oiz729YE9F9v+j/1nY37dU6b7fRmht9fbAIHK7d4I9LPzwamUBvCDvbYmnCOQKNycaAkQnanhHDcLpZzJ1LXZpFpsbpMkJWwcpjDlUsiOuA4nswaJT5SEbsKc0KFHezKHDjm3JIqNe6P3O7ArKluWsHN+pZ6Eh6MJ3STSSldGtkUUCmnWmOy5YIVa++inumhRLCUPedX6UTGQWeoNikeVhpOwg1m4o2WXaBL5Awb0oFgGDk5aSroGG5etECdEmFv7Ix2bIo+PfbKnfQzUyO1A4y1GMwBMExGsXGuVXON9Uty24y6cV3vYmvfjJTMpQYfXRl5nUtDcJDUG2dCmypmmGbfrQbhaHmxS0Ew16+EW6JDnJZeE7IVN/4aVg4D5RWX1dmLD2KTC0USco3BRftrz+Cn2KjWTm+GS8rHuMjM73e4Q+Q6j2QDIzapt9tMh8N1xySj6g5mdqfNPrmnUnEvBBtXcu1wjJD7bq3S+3SVS24CowOvi0wznNlNTBXNqNP82pPyZMdeDOkYjQ5pFzSuDrHrxIzR2KHamTxz6GCdT09cgavwON0Hs0K3h2ULHUea7c/UXdmLBmlBXMtckporGCz0DhUXNIZYXbga3rITE6S3XhN3R6PbTRxc2Wi+EmUqO1l0M3CMjbtKtg5Ifr0sUciAt06W3JZJVFnF/mAoO2Us2L3Hhle9ceyKvfbHM3Pj+Wh1kCpuhQwsvFyrgaZS4eUYRX4VTJQh3VbZ+cxNRznVCbObcmoVYeoZ1kfDxBlRF0brnIV9QiVmoY2XbEzP8p2OBA5e3ukT6cY5pkljdzWFm6IyDhQU98BH9bVkMNfbkg6GMk80EsGCpaTdMMGDOXIYKkY/2ra+c6th0x7OWLCz26VhUVy5lwa5gfldw1eo25B77eif/dumP53kohIJnvR3t9vexVF36hsFJulzeoW5PSzq9maHF27hnZc2GyTT4AfQDbOvmDxa1wLJByiDExLR/LvJwrd7rMaQNS77S04jl1ul4EFplJjFXXaWorTro7rkOzvwh/uVx0f0Tt7y9bRdckeUtLm7DIs7LCZ8yS9TOFh5m/YS9Xi+OWuDe9jx5aQIYFbrlNMqx40ycaBKvK2c+n7k9ue7oJBB6lKSm9Nq36hBebvQtnxIrCKBSCMcoZoO6eW0jdGp4jBHGfUicGpI3KiDJ97cxKpy/dwOnmfAGbTC0xzPSjrDmMkfZNvx7M10US2tzFzBtBtNVtYhX/EteerbQ5WlNm5tzdRSVkQrDhBYbp16rtyeEdlUd67oD+uVn+IUS4pk7GmnirKp0t0dNYMq7VuE+iSyq47V5AamtfaXTnEr/Wl7OS0vLlvzh81h63p5cnYuoqNJxnQ5Kaq+GtdRhcM+xYGVfaEfZdE8Q0mMZPZ+P+5ldHdPonI99bVTBXJcr6FWMvozKy4HeehvehrgZhhhjUEsNZtz7AaydVumdLWpEjPkKiwemkM68VV95eK+u00xYpgUu+TrC1/SZblTLbbo/JMBnW8NYUpnFFpXy5MAp5aDxrnCK5Q0NJqH73OeIQL3UHapcIvt+3I3EJXfkDkTnJfD4VJObE2r/tHk+D0y5SRvw9u9kgpCZk33vUQ3VUibN7OTrPKkELTnYckyqKtMlPM1iCjtVmJePZhI1YYjJWwhSKowaLhqJCxKRVvgNBJiq5U+Of6hwHZHciSuDFaWWLPe38kB6kE5vl7XWsQuRVHvup2Rpkm5xszsgkNYwa4ihhU5Xa6orUgLlejIq8sORvajI1ziAubJkeT4UIi3B54rB/KminR0Tu6bczLGsX5SAxEb7l6P1Y11YUqx3GhRPmqmxNobyz1wOm55DmFqtD5gDFVeUeK8DGOXNkpjNx1XgsG0wNo7/kZNSSMPeFQaLq3x/hVWrfDGx6LpoVVdSGe9SIRdvEE0YXNEnSat7qvtlZ/sjg3WdpkLNpOk05gzFZWbNU75vix3jH5JtQ1PhtdI7QAK7pSKh3cxN5mWfC6oUu+Im+HJ7hY7cWPWH9i2UsJh3FeVCSuweduuCZ0EQ16SktfuvtdytlJJcpIZozsf89OeO7FZeR0nxeMwc49uenzaY+YG2hJNXO2zpTZQztW5xwoOwTm7IqQcI0Pu1kzDLnZwannd8Ufc40KWgCNo1EZfr0fTc2Q1Mrw02YRnpKB2uSFFS8UqrwR/vDEqKvKjBMmc1FAGbTByY6pURmFyq8ztobiukWI9YEnerXJsVPEUXh+nK4NIepo2BK/7yQAdT+rGP6/vK+8cBNIEIrtlmiZEJyU8suqW3SVxQnlWyhtJDq2FUrQ4qY5dLb56WxoByGBDx0wxUHmkkeTcHaoSCpZC0J4lK7+hSKDAaae3Oz27opQJ3az9lmRZOmfqDHaMVNQ5nL54fASzhw2UycGoK3jkq6VyE2I6PIflNI2HkGVoogyjS7XOT70frTAp2Jz2RDE0OLETSKbwB3WQ8hBFWBuvL+KNydcCIsnrkgu21i1kmBiqo4iVGOG+yeTjyDY+rdCMevPZMp9gbHNWlLXlNJYXjqIgV8U+y3myuihMYvKH4pYvbVmRl5TEw3KFcmdII+Mzx7b2cB3WyM66RNM+jEijHis+SC3zTAr0uHFJdHR9qAD5I8JiO2USZ4OoxF3kdmKgLqhXOw5TDUYgyi7xdklwqkEel0qgcQmYSJOhxiVzzaP4tiuzdKPHpqtrfRmJh5toL10VF/QetsTwIKIsi+xhKqUMjt0H0DWVLW9fc0iuWLtqX2L8pvbNi8cc+nJ1Hfj1KQ8zl1jucYJTVZ2ZeBOFCOwYxbUb+7ZmMxGb9H5HSeaYWaftCe9yHSQ9xKo73YlQFKGzbb6HQfy2Or8t1BDPIlv19uEmSYMeIawDYTh3Ne31KGjOW4tS0WKTGgZ+O2IhMvDo+cpmupDxOS/d5Ay3LpJsXq6ybaiwPfXbUoTGy8XFDwmofQeWFvXwVm4ZXEy9DI/HJDxFpHdoK5dhaLTJS0inIQIV2ClqBz2B6rubC3GLysMxCAhxd9h0EV3GWQyLY0t7smUqxw3bbSHSbuCROoHWyUkqwVZYTLsI5jJwV5BAdBp7UJy4YobJMETmfNgxRHRqMvWO7ti63pLwbdRqHTWN8/6cDPvbUrreRO7o7WOGVbvDOgrysCSrXFodrYS7IpLF9r5TJ42Ieo4lMaW70ukuKXVRCjeuezykd4d27jiepWwYyyjNtME132Q5wDTpjoFMhU8tsTzKKOkhuNRehut0VXP6QKveLkf3ZCLSsWeYhV2eyIK5rEqzYNagudN2du3sZDnaVLZRNTgz5KfNeAqxg173eY+tKv2y4/qriBjnaL/dYSjLBQasABR1HVwX6PS+FwZRvp8OmhDvKPxC7G1Xi8Rrskm17ToKq1MXXcKcsgTUDU8DVRfJcSmZTu2kBqRV+YU9M+2xQkz6mIKenXGmfZpcTPQYaTTbiZPJKDW+05dctUkEQb4u6cuU701Rq5LifMH23W5AeNY3FEi1kXNu42i12caF7V8jfbPaYhIL9ELPNiteTMZovW0J+/gWtrf7XtI2sZmZvXuu8jTQWHyqWlJTFEVS9I0CpSuJiwylPl46z9zKeech2GoTFRQCmkWTqFANQURsbTv3pm3aSq4cSU2PmtmibRrfdNmfBFOACi5Lt/luOmnW2oyzBHciE++UUOTBZD5QStvuaL0SKHxFL/nzJdMrDKWPl2Fa9WcYaqGUi3fWVYVFrglZ/nbd82K5CxDowHK7JLQ3tzGyKivkjCbWtka5NGu4hDo4123uFAxMvHauPD2smpO932T3vWEOZ7tlNzwdHNCzNq5KSFQNc2sEZ4I5babr2R7ayymemMJAx6ODYjLfl23ViZUNpKEVMUZO7pFK1OKIZr1IGsf9fc9vlYB3pK7UyF3nINW1gi49w0kwsYG7Yx8Fjn3VJWt3CPT7pqHwKo7t1hHCZak0rjztBQKMJJQo7zb1QRHsZbBNCQbp8I0UKf1WJyyike6HhJVbKjoSyAkJ7K7d2qVL8rsWp7cSE+Rr0qdXRy/C0XNrRpSq321bw5a6ZnVjwOejlzk7PuMlm1zCSdm7U6vWIrLS6Asmbhg66Om7cUTivS+H+aWesitr6mxxIo4sBqO9yQMlWVHdJrq7Mi+HqTk0h8Km2bIGALHWyU3ce20hKNyeAKY0YG99tfarQxOshTpYX6s0UIP+7ohbT/Tzw3kPTKrdJgLtewwn7H1rEcKekDuDPOv9pal3W/t41q8jzxmUXQTb8/YcnONBWiNwWR0jObTOzD5TwOQsGRoc70esbKCzahNXfZ2fvea0VDXv6o1Jqtt8zJN384RsuISlPBqurOgqDbg9FXsOJfFIxveg9fYOOcmlvRJA3I3qorjK95NtczzVdrzN85h+prhjDNe4rlBxnobE6VqxItLUJXItC+K2vYaFH3cnuhLWrHYqhLBOLHFXxrmO1/eTwWIUfoooQ2nsphzg9n4aB4eoR6f1iwnV+Am4JIHt8k5kjW/cINScCEJC+7y7LXdo3XfyfoUQTilgcZFVFKVB+PE0KqclLXgTUCFoyWLv62WBku366t00lKSMCrExtw3rbjLRHVmwstpiVUf4iXskoqPjxvF6708cxy53jFQ5cYGkd0k0LVs9VHXgJFZeeF1KSBOEstBkUIfTGmX79f3kc8Kx6pdD5J9iAznVeeNM4V1ksHthZh1BrPPLHVQEqDxf5bBa19oGDIPIWiqQbdlsoTsGk1sNKnBrr5tcCcM3GG+ue2LSocw2V9DePqJ2YGBI662WKWh0O/XaWHGw5SyH4gQ/7Tf5jkapkjpWK/wqX+NMP7YHzjyD2dRTr0O5jWMeU2/3wmoJi9/f0XtfuZF/dk/9iCLb2ppSlWjvNi6txts9F6Gd5C+FKyHfYYyL6vxc97cTzlNuIgoZd+1Wspb7bmocj3ioQp147cmDUmcTp2FnaidU5HQVXTAv3pUdhmn40XeNizOu8eoQxuh6lxXuWu9OaADHeo5asBe2HbtPhTsdq7SVqAxOwsfi5i4v+Yi2UVHENzSt5GYfSzcjG2+URRzT0lvTrRETrX49Bcf6hBWJh1EEb0DxUneknolls+8OktaPbr7nPHF/WoqpbqaluhkEhrB8JOHvunDdM9takA7YsAwNMxTFI2awfnBhq4nlHCnxBZ4JGnGt7u7EcLxOLukj1AFvmSUVHHP2Xt5OlsfJw7K8YWS7vaMEfAxR018yToOors1BMJfV/Rmoh+ByY5ea18QMRuNyRBClJEPLM6qv2msr3v3gviKjXEQukE2Mch6BBuWa8SDYj/kWO4y+It7WwhDbe6g8XLZ+LPmrVhdiz+5Q4eCbtNtmxoSuAlB0uEK5YZoiXDYd3W3dbnNq6uDQx5m45lD/5JgnNqdJdrU2hSyRKOnkImWxtCQCJYLclNCLteJ09M4foYtYOCEBbW4Dxd8miq3TO5qZgR5UeV/4fewsY64J5LsCa9wOR8HIwQ4edhILiNgR27NfFUSWUHRpNrR3dXN5xyq9n1EWdL9PfUkl5v1COAaFSnyIrREJxkrsunKhIANVTFphLXxsNlv+qBnXKBZSXEZFn9eUbNX2rm+iktZSZHwErSmTGyzhDRJxM9U1dYiHcp0id+Mu3swDI53NS7B3d3ZEIJeVf/IItJKXBxAoAEYGuNwc4rzbohHmsz0mJXC0P1XVHQQvLBp0lamGaIpeudNtNO5v7Vhx4rj3wbgMWCijSfqHmN6glWmIfprxnGkZ03YZYMxylQUVf5JkUbycTjl5ue4jRUSRk2ie4guMVBUmKxRzdRyVpQTFaruJlqcEwSJvnBKIablpuG9v5vF6IY0ETk1vNO4mNvYshXCVAF3vjd5Gtw0hlKzL+1G4zUY5PqKyglV6dxlZwnFQf9VM/d202ngPT1FACUJid0ivelTpMekhq5Vb6CynqDRD1HbbSxLvLwBxrLYWKrRPa3unqVIax9viumoiaHu3BnRirRtph/31wgwlCSGC5UE42q1uewKraDSFUWOJlmNY3DfTbSue4bS+tgNKNsMpaMEwHvYay/AMOyFH1dnhNbmPigGZjmKnLg+12ojsxLoDvkK7jNyauTQ1FnZKHbnrDURbnVeFK7VE78ukhXrb/NBj2Z6OTWqfGYZbn6UIIc+NeFiaJ4/WLoF9AU1HC6HkyieEO9vXh/O6hLyzXt0IJE5stF0iLcBypjOzdbo9mTkDsoU0M8qUnSspXVPqsnW3irbOorWhjBxqtfmpOTDpTQos3M3P3bFyeipuW8RMlcsIXQ87iyLYtFXhEuOw4bQ6cHxlMUOmnRSA40R+3GZQd9+tYwNXQiTEFcauEz/Qo+EeccqS9vvj0NBsi1j9Mcgtqj9W2qoVKoOEGyXXmCU05vLx4vqtF8iE6DJhO8bVtjGpoCta4Gky6ssMj/q8PKQcaqgu1ZjiBdbMrlDGbKLACLXK0VPoCxi7FhO/DwI/XqXIpiwTkmhvS9JMpdHYui0DMsqvbPZQr83kFiLstM3XlzFOsaNQcFiwQvkG22OOteyZvXc18BjOrhY6XCQhkrHOxZrhvhtRvkaw1ks9rDKdlXvx9V4yOK084Xv5FAVnvhDW6XWFZARdiUN6dJlDqjhJljOY0xHdiKP4nmeZ+7a/sfLtSC/FwyUgTmyn+gkdHdS7M0Gr8zosYnQFX9dXF7/VkOlTkazGCHeEHQlaIRHWltsEr44oTVxOMrrOjEEnK1LFFRuUuvCQHSzB2IDRXOb9FL238H2NjYLPdOdTLpklS07hgSoTYdt5ulLDO+9e0IYTjRlunE4Vmi8TcxvAEKNz/k5VNYWm6Zf5gPbLoeHLf/etuvmg6H/svOp5tPTlLZjHIalnuR8fvD7+tyX99f1L7URAzucJXpN2wdvB1t+c3334F09FZ6LT87W2L6fxz0P/1grmF8ZfotztmraePjdF+nhjBuywu2Z+nbSZ3zh2wPf3Z8Jf5QC/Ledxnvm5LT67UVMWjfcyv+85vwvjuUCyL5fB20kn2P32KtdnjFh99upyNsDb6xVAb+wVecVe/vi/KwiNu/kvAAA= -->
