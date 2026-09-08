---
name: "rar-cowork-cookbook-dashboard-define-compensation-policies"
description: "Pulls compensation policy data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals header, two inline SVG charts, sortable table,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_compensation_policies", "rar_sha256": "64a1459ae93374a2f6507142635a1497f3f1777ab96cacec4ec7b404601593ba", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_compensation_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_compensation_policies_agent.py` and in the RCI capsule.

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

Define compensation policies Interactive HTML Dashboard — Pulls compensation policy data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals header, two inline SVG charts, sortable table,

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-compensation-policies
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
      "description": "D365 legal entity to pull from; the recipe uses USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-compensation-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_compensation_policies_agent.py` and embedded as the fenced Python below (sha256 64a1459ae93374a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_compensation_policies_agent.py` first:

```bash
python3 dashboard_define_compensation_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_compensation_policies_agent.py   # or on stdin
python3 dashboard_define_compensation_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define compensation policies Interactive HTML Dashboard — Pulls compensation policy data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals header, two inline SVG charts, sortable table,

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-compensation-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_compensation_policies',
    "version": '3.0.3',
    "display_name": 'Define compensation policies Interactive HTML Dashboard',
    "description": 'Pulls compensation policy data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals header, two inline SVG charts, sortable table,',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-compensation-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-compensation-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '013090a79fe50bd6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-compensation-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-define-compensation-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from; the recipe uses USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-compensation-policies-2026-05-24.html.', 'output_folder': 'Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define compensation policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define compensation policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-compensation-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define compensation policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls compensation policy data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals header, two inline SVG charts, sortable table,', 'example_request': 'Build me an interactive HTML dashboard of compensation policies from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-compensation-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 compensation policy data for someone without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineCompensationPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineCompensationPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-compensation-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardDefineCompensationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZObWLbnV9Hki5iqetjJDsIdHTEIkECghU0gyh0u9kVsYhGCevXd5yJl2q5u95vuiflrZGeK5d6zn985J+H3F7fvkqp5+fSih2652Lh5niZhs3DLYMFVQ9VcwFd18cDPwq/Krkm9vqua9uXDSxC2fpPWXVqVYPuxz/MWLCnqsGzd+eKirvLUHxeB27mLqKmKBT+WbpH67QKnyMX6f+rcbvFzHsZuvgjLLu3Ghanv1h8WRdV2iyb0wcVFlLY+uF+HTVoFv4CrbvCxKvPxIWDr3sJ24S7aDpy5eVWGi7Tswsb1u/QWLkRjpwDubeJVbhMshrRLFl3VuUDOBNAJmw+LbqjAljwFO/XTZuEnbtO1HxZt1XSul4eLx+8PQNnw7hZ1HrYvn37924eXFBy/fPr9xc/dFlx64d+Z8GEEaHHfWeE4GyENZ4PlbhmDxfUILF6Cc6BUVDUFuBSE0eLt7Oc2zKMPi//8z8vgNnH7y6fP5eLt8/ll/qf15aJLgGiV23ZhsPDd2vXSHJjvdcHmgzu2wEpd35RPyzRpGb8+d36jVNWLv873fn4yeY3D7ufPLxUQ4SHz55dfFlUD+DX9fPw6U6l//uU1r4aw+fmXb3Ta3stCv5uJAalfv7ydv5EFC78tTaPFF/0ocG+8gHvTOgTEv9Nv/jxFfyP3ZpIvz8U/V/WHxY8pz/r8Fcj7DEkP0P0xWWADsPPlNavS8uc3Hk11C0u39MOff/lnZP0k9C952nb/Et1fn4SfIfbzm0l++fBw398W0JtuX2n+c7Y1CJh/RxOw/J3dV0P9M9oPz/4d6TkN2q++/CG5H22A/rr49Z/q9t9t+LCIPr/wYQ5ytZnz7NPi90eI/PpT8O3iT3/7A5D+P5LRq77xHxS+FG6ZRmHbffny60/t4/JPf/v1p74GURy6xZe+yX9E80d2ffD5kwXfVv38572Av1leymooF19zaPF7Vf+P5o/XxcnN0+Db9fbT4vtMnD/QYlbinenTBN9lYwtk/c6Ov7z8AQCoBNr0/uM2wI//+I/FLvWbqq2ibqH7VQ/wsweQWoSz8EaStgvwf0aNJgR2bdMZ257rQPzPHp4lrqLFb//Lf4D+R/8N9OGv+PkleGDbl+8h/kv9hm6/vS4MQL1q0jgtAV5r7PH4uXTjGcIB57oJ27C5AbTyxi78CJL643wAoHfx27/G4MuD1ms9/vZA/vSJgRonzfjX9nn4OmtqJWH5ppcPqll4D/0esMmruYZEKcDvD8ACbZWD6tDNVmkvaZ4vghQgDKhqz6oCLPdpJvbbb795QLbP5ROw8cWz3LUwWPBVnMXHj0C5KE/jpPtchn5SLX76/Y+fFv+1+O92PYjPPI6gfrz5BUi41Q/7BcizvgDLgMuAkwGIPPzy+x9vJgZkSlCfgRfTCNjlsRnE6SUM3u2ti+xHjKQWXgjsDGxc1KCagSqwSLvXhRQtvsoLmM635jqRzCU3CIHdg7AENbtLXKDOV0uWVbeYHdJG44dF34YPrr95jfsQsQAJ73a/LXbcEVSlKge/ZjEfi8DmqkyB+b9Gw/M6INL81C5W7yReF/s5Mhe127h10rhvPCL36RdQjd63A+LuogyHz+VchcPZVI9QeZoHLAKW8d9c+nH2+dyUAEwI2nfejzXuXDuNRw1tPpftWwq4zewKH5QEwDTu02AuDH95C6k2qfo8eNgPSDpTevNC8OaVRww+W4AfdEKzt6S/b0++dg6Lzz2GoMTi/+c+ajYPu9lowoY1BH4h7A3t/HTb3FrOYj670VkFELvPFP3W37xj2DuUfwYMQQw241+eKx/OflvzhMe+Ab7RWO1BH0QacNtM95EIc2A3zewU93P5XjM+ACs8ABKYHaAGyKo5mN8ZznffJU2APebzb/3DI3CAfYANQbAv6t4DbltEYRh4rn8BUs1Gf3dzORsZJPaQpH7yJ61mH4LgA/QXQIgUpCeoK69fcfx59130P218tknzlkcL2YNcbh4EgBzhLODs69l7QLzu2ckDPT89iAA1irqbdfdA0AFNnxfDJrz2aZt2M3I+7RrWALs/zt9PTeer4b0GCQSMBdKk7oF1H4k1Y04B4gPIALAFxFORlqApAEZ5M8KDoFvMKAFQ+K1rfVJ8XH5TKHxk41zN3jfOisx7HrH1SAm3HL8HE+NHYQLoFfOKB9+/j7Sv3GbaM6CC4K4Ax/e7z07i9dkMPLuNxTvdT/8wKv38701Tj/Ju/jkAPi2SrqvbTzD8LMnvFfkVYAP8lLX9Vp0/Povnx++B4+M77PyJ+lPxT4t/T8I/kXjLkE8L9BV5ReZbyluEvX2AQbiPq/NHYr77udTCb5AL2FcFEG923wjaga/18X0JKJJxA8AMLH7Wy3YuswOo7I8CAXzxufw+5OeUA3hTxuEDcL6DgkejAML/6bqvdQzcKjvAO5hbzDh8nSezWfw2fPlUAvT98ALQNfyXp7q5YhVzdLfzRAjyCGBsN9+a58MZLO7dfPjnafnwOHDz1wUfAmDK2+8j8K3OzHX2u0R5qgpU9AGHD3M1APkPghOoOjOfk8xtQdSCgJ1V6sZ61uE5AM4t47MCfHlWgH+UaP19gXhU8EdzADDoLyB5I7fPgSW76iHK94XFvQHx5zz8IdNHVfryrEr/yJOf69efChdgUAMXPHL6L9/bBBijfZS1H7L52iv/Iw8LtCYz2aD6NFfpD29IB77BfPNh8XVUARZ9Gx5nDmHZg7n813lMml382DIfgD3g6+umr38F8cKXv/1Irgccfpmj8RlTfy/dfoY5UAZmTR9l9hG4QNwBQBPwcvgavy7+tST/iCEY9REhP2LEa9IV+Y8N9SZQlYPa8AOHhDNqP7uO55qv+DcL9udI4Cv/2ajCT+CAn8Thuc06lCHfgPz6gRBAikdRAaV5tvA3130zYPUYOmd5gcG7599Ifn8BSebOPdBbmr1NLWA5wOCP7dyhwQCPAENw/kQOcO//cp55o9ImLuikARmKcFGCZNyQwXGacLGIIhEaJTAKJ8ENho7wCKVp2vUYynf90CdCn/YIhKAQlGRwzwX0nig0syvSWbJZLGCQjwDIwm+3waXgTaWnCrO9vo5Ps+pvmv3+4lEEWCkSrcQ+PxzMoB6MK969saESge5rEiO361Y/HYaiDBS0DFKdtqvCyHTrgpAb0mfjllO1+BQLx9GY3MwwEig2mEvZB0uij1lTMputR9LeXV4JW3pLMCFOQiQ0yb4zrYrTfZ1q+gq7nscxQlKzyqWTNqwv/rSmKF0ttKWJeKYZ4TROJt2d7EOvjuTJPE6Zhy9tEjN9ckKNYFQQDoXaXWOeHPom4IizUhISZtwTAQVLu8ZgQd46zfF+HmV3m25pCg6P+1FqzlcFUQt2GszrGB+XPHWyXIPbOTRFnNR8adKEricjfL/uIF26LXfYcW2noMUeN3vHx01P0BK9Xi6Vy0p08r0mbrIdZxX2CV4uhUrYTMtmWZXS6eQRIxrL8I257MQMozrbW1NQeLO7+zYnlxBEdxlFEt24Xp0Nc6CcaK0VFhI7tqwpm63ExjDjBJqxg4fG5+Ndiyitsgzue2Fc0sdAmNBhbQnOblD58cpWu3shd0s43JWXqNmcdvu09pdexRL6kAVRyjcOI8jkxRaQLLaKM5kad2vQTsWaqsOsI61oQ8QcfA2dvna3JTDBSp7iYohvwybMka4y5PHCbwPIZ61Q31MtXunCFfVSJ9mtC8aBdDFysiJWdiv2BImW0UvH1YG5BlEe3fHtdZO7exOJVacZ3dSQWbWMCWurrDeb1A34aExHeZvrxhl17k0cka3VHS65wqIeyjL5tlz21TRcHZ64L2ujDpTCQwo4lDLMFFHJWa84Xa56JFnzkWwsb1Whgl6V3frciuO0m6tdCuE+iDfQQJMWlvkZth/4BMkhdwW5zTkdgtUh5sTthUjgTQtt7kfvtp1u96O0l8E9q0B5W76sGn3YE6NLBqjeaq6WdWv17pw9++q5tKxsOfWmsTa8XpunQ5Se9lhFs1cY3Zs6TJRaEqnGUm2WmtZKZZpgCck77WF1yitmtYR77N4HqXnX6mMN79maOBfipY/b1W5HNkcwanlJcvfr0hWKtbe6626/nxBbXIaR4QvEgN6XhEMRWzwDSSJUywHmDlsEgnGRCunBv21PDadF06jLQ7e/cjtGcY30jksxNMocPlqGLSyZqOFZQYlhQTu3WRCwYTRs2lbPqjN2dPZlZamX65Df74ZCWBfaOXTueeKM7XqzHo/CVfZWSHrkTo273q7QNUmIxemK92HI1f2KVrfbYYntVqdSqaedwezqdjryWY1to4pRZXiNQYptTY2mG9QO/NyEFrXTk145m2y7KQSj3vkG2YtVqJUXF5r6m9WfDR8J9kZROwV1gqaguGCNhAX7BoBGTu09eECnvLAHKtty9yTg29tpWotjuBZAHOd8Ro+4cBj4I+eBwk3oDgxChUx76TJSmi2r6MRv8YaDGFreSXJ+YmC7OMEaX+GXo5mFF/RC2avUYqt7dMXuYkErBcpNsH28mkKDpJfmfpfFxNuWic6HrFS2pX9ZXlDaQrVi8HfSWTUGsqn6aIduIrSlwkCreFzbmXtYWtINfXBlZvTQ0BKE7TiFw6DE2alwY+/GRKwGR74S8vslclfc+B6Ugt6dHGGSh6FUZW0Ye3V/PZ4v6GSZzl3fX4ZJ3p4IrYadky8umRru1NIkVOOIY1Ze8saNEeMb11ixlRFLfMXYkCWKfllv8jzfscRS8PBO32rLW7Zs0cnuztphmfsRLIukj4VJeGcTT4zwVlWJzh+pXGYN/JaaLpLerghb3Fk3PaP89aZxe3RM+Wx5SqOSK/CVeSGP92gXrbSzVt2nlboLmCOsruwsgaxdUjTHDcd1pYA3d4jEqp0rcwbDbuhO1De9umYvI11IzmjsSOQwykWCdNS4TZfJPhHkKrlLU6qPyIVVU17FqIla2XqQKEdT5va+3jPLaizk9Y1qg9E2VUlvNPWw53Vo3zRroreCHXnuaDdRJsf1W91pu7Ni+UKMedGNJ5lliK+5oaIKczgxVVkti9xMTS+JUG6L9aRGKWthzA6T20y0SdBSgEWOavT9RdgE0VEkSGlZwgkM9dttVKYT3xD3oDDzg+hqJFmFnKImCe9JOTz4uEKu5a1g265iyTHIiRMAqASSzu616ZBhb/uw0JmJHXq7ljvj8vGgRFId8V4qeaez3cstj+WtjBpsYYoKulfJLTdylsW77qbYJm3bCBvTt5uNuja3k+x1Fc1plLZN/Ng676bb9c52lpIX5xNkHQlvNKp2os91qNdosW1Ej0a5JdbsJcwdlvutzJkq7pEn1YhBNgerNWdjMUFy50tyV46XxoGiW6COV1+jQqO9JDKHpNya5qFeKNtzXPTHzAINcsrtLlKvXEk4hjZxp26s68TxuhqjO8vxqWyHM6fT3qM3I0Gze0Q+sbh3kyFTxu+xgay8paHIy0Jyh4OOTDDjV+0q4SVQvHZXdbxLK66IscpNzZEuD3mUkliUrtPNSVs5W1Q7no/q7bI3JZpvhvXybrUahJm6xw7MRrlz0OWabaSMqNKM16XcWZ2Tgki3rC4cJORsVbJzv+3TprBYE7+r8kao/JHtk73kYWZ0Ec4eUq6K7aljLkN+YnloiV3yTSrZnjCNTW+v40O314Tj6VrwFSjOV0tX24D3z7ywQqZyj5JuqKzU/pZuUo9NQpmEjWpjIM7IQitt4xDVUhrzDroS1xN3EzHNcVPg6K2l8fvErkAJVLzhuNbb62q16WuiOLL8kOLaepWd+nsnwZte0bmtajCbG+wYpsZS1yO2VbEyrU97HjukVirLW21vo1Dt8yFTeBv2aCBLhOmwu7FPLped5Od2Hm0grxLIuIJxYaNbMbnG/NuUMsFRGxxYEPQrcUbvHHxTnZEiWXptaNcK2Rrqcne5uInBnRWTlljI1vT0kpdum5PClZUH7YZwRa6gKpNdcHU9qYbtIrsly1Ed4WgSbm/1exVTKYl6Y3kLTjucZM0gMDedetAP6ySWCbVdJvFS0G+GrxGjVmrhUcTsQyrFLmYgoDrCJp2xJ50kOD1CyXZSHIu6DDyhyoKQJydDMZtJgy9nrDqKe6UqtO3ER9oRg+GglNMUdw5xwfgEAtUpU9NRtI2klh0xexgD309MreIikpUDDS96a1NuNWbXTVolQPnJ1tRLxQmb2jaqWNBdXNpwmz03yr1d+4UFX53bZJLaIaCwlsTtPUAw/XbYSzoCTQVr6uZ1ddXjvsMu411k24H1DTdr7zYRs9iwm2rNKJfNscFlnYMPnY52x5x2EULoafRqHSRWqFar8XSU1wSh7mPyqJ0L3DEk+GYTEnUZC52seG+byenoetbV264k00WnUuxSj6h0uYti60q0vgQjarIRXRFVWDXptfJA9P2Z42Ct3+XZpAkJTp+v4jbi64rcizaCHm/1AEENRsuec3eRy6ma6pJMTRQqVVo1oG46Xy2vveWXXYEooduvwOTlr3HDZfb1KTq1G/u0j3pc3J5v8Qa5Hrkry5CJw92qXD/r1VoNz0x2Xoty4PgaLG+clRm69H6ot2wEGkn9jiilx6LZuFEqJTrH5lYt8QNs9rkuCXypXMfKPSq4ASN+CfCua20WwbxtY2WmysGEoUIXZrCPWsKKZtjB5VYQUvTU7Is+vPWB0IR5rdMcI4IpnrYFz11N3Tm/Mjo67tqr1fUMtXSbew0VyXIfmPTueiz0i7lBrULpvC7xM/Futu7ZQ4urelHNoWWt/KR7E69Z7t1Z0aS1wguEFlypABCPsUlEbjaVR2x0OdEvV/OWqt656AECCp2FR04gFX2BYZyerMxVEpvZ7XLZrsFgczXHYkme7WJzurDsFF9TYikzuUB0O4c30JYgrHSPyReOWcVWihI4AYGCoNgpBYFRF4rRsTnJoxL2KsXu6gy9bFnQENptqEOClUMrxF3d7e3VaVZGuTrs3PKSSf4Nh6qe5gOmoQ6jspI3qSoqsWUt82SgXDRLC8yxe+02CpwsGjwvydvLTdLSqI67ulq519Fdpmokrs/re+mzG59vSMIobz6rCse1lyVL44IM9DXiTEwiHePYupSEpTW1zsYusBGfZNQGzumpLeTAFJxkk+wp3b9rg5+U8tVslOjY5K1I7isrrK4QRaHTtESj0JXdiR8spTYd3QTqtZuRj5rLHkcvFkSpzNFKz8BUNS66ScqmRVB6PRUN92nELTAfidB2OMjcxUIEtrGRGjnB2Ym9rq995h0p9HbzW9lLa6mvoDIjeSktk2G3bw9E5XDsODaZzbnFzbj6O4STmSNlGacDhUKUdibZFiYC2SfO0AEHnfLgtPXKYAPMwhUHTBe0Yp8dlfZVkjyxGhSCjpvlk47s2HO6R7jIs6aQFRHDnGIVjussRIk+GhR3ifGJVmyoU3/x904vGTR2I043U+0MFxExCYqTYwmPgVVXxB46025ZnepYTA4sVVGiJ9Ub4lLs9ndEG8VgXetKDfFMeaaaHbXBA/N8rDiGCFfqCB0wVOPqLN82UH3EqCWpXUXUD5kc6sPs4G1RKkgdl6abqd/pF2uoSWoa6+jCMKupck7Xe+bQEhz33G1ia6bcnO1r2SakuLOb3DpqfHDCODCMh/eS6y+MjEcybjNB19fOFSIQhsORNaEE1Qq7HjR8Y2yrTCQ1Q0DXuDiuYgS/qdvTXfcyCPUYUSRyWoOrruzHvX+ybUYhDbSvJ5/x0tPBWx6g80idSt6OKMwJEGQnZ+vlXnQ8xMREgLHLTczsIriNInjpRRUrEaTq6zjMZHB6PzflVqWcJrLtzIFuftoXl27sSQmzdiK/s1DH49OtBFG7nQxfDV0WWaq06L7juFTFLpkRTOvlai1l6aU6+PR5a2NFha8bqzH0HRTQcufaN9jw1DBIZCSvqw2NOUaKF4fDUiemen8fktJY5no3XY3yXKo63I8Cr28k24YnMDOegsP+nBtMKB2OrWjQxbgxpAEGE9xyrFitrBpFc2DEAPbdT2Fw94ZGSRqMkYsq8NTb4VTB+qUhw8jKOkik5BNy3pjCKAn2SBzW+NTEzWHCQyHZrcfGAxmorQMtUtIMm9DG1pbFNrqKtV+rW97DVp1GMC2NhLdl1rag+1yVUOP4mJ9Eqd+fQGXrmFiTiVLWkH26M+IBdu4H39+Nl5FXd4RXa3bY95yFuFCygXJpZSLB9XyOyd3VY6tVmhj2PfG0mCacrrUSWeyaXXQQ22FsK3JL3mudxxkXz8dln2oU3VAsYfeOqqsjaIFcz8QHPXMofW0x43A8OJlHWKK21+wCx91Krk9Y7MZOBF2WHJQI2Qi7VLWLdDy0z+m6Z8djOYjS/RhsHWUzZs1hidBnMVSkFdm5m6y3rgjGR7Z6aouOQkn13jdmqzq27W8KpUVDPuo5uW8GKcgwnxZy++jaW7xo6YRsPLEwWHx3cNC6ghzp6pBxacioZZECQo5CR9nS2Y8pBjoNwf4yMsc6z8jcZs+ZLHrV+egFGM+2cYRrsJkL47UqdndiT4sbUKFlyDBFYlg5WkhoHsbu9z1daQmB3wwsCUgSNhGIUizELk/iCddaFWYikbnm+EFsMmc9iSMUoFCYDX11XlpVJsNbKtu7vAt74RW+ReeSVlDO66GCAymMIA5xgIKhP+r00DuX01bP7jl0dc/DtWVN5uQV5GjRYRdSKGhwFRMgKLWs6GqleGUH+hnbwm+2cIZT+XDdTGpUQmoDUii/qleN0fUab/hw8rKTtEpPcKGV+NlP03IJ2xtWaLj+qsLKXpauiDcq7QoSW6Rbm/LuHKlsFQQRacTyepOVKh4vxz3dREqzI9cI3g13SUQcNEWaYrs0C4LaNrKX+Yq3zZPikF49kzlft7fDjQEzhnezQ7GptuYadkqpo4VURPcpR1vwircDN9wofZTd1MpnwjVSMQ2cJllUQIhnnaDitKZ2YG4LrpGe0TrDy8bOGnGOvCSCDovY1Jy73JCtPeq5XbO5ore8OdcAL/IsE6sz2aaQOLkDOvKus/SS29laDfUSQjZuEC75k73rAhqVvBGeXNoTKDBJJM4uu0jRiLfY4EKYKqrY2Foq3Bir9Yofkb3ub0llyaX1BZkYKdQxpdFbiR/5YCBINCtI0S53Y+vih9pn+9sJMUiVJO40raXOFIEWOWFGmhlyMHEyhpObE0WAqY8XFP3A5PwtFfJqjZ5EEYbz6GBDsRnD9CUrCBivFNkJ++GMwR6Ty8FAl9lIYb4DF6fY2BLR2ryhE54e6OvlWN3peLONkBFHD7KDKUHrrBt3x68vWZ8M7om8TWu63XdUukx3yNFYe43Y6Eumx87JkEMaqZyHTFOL3eRQfI17K7LycRxbKT4lSrvwApobJfIzgS2tg65y0DAxPcvHiIyvUhwbuw7zKfSQm35TGuJooYd1c9yHfhBg/Z5iIzZBsZQSe9O++6aClokN9VVGHqKD5e+D0CmujXGrAyKDSXc9ev0SMqNJsOTNDW1YjIz6PgmWG96PhIzdb/ciHlR9b16rg3z10H5r1RF0Um0fhkTB3Ldw4mBYe0bDSev5/XkTac3+3tmH1uv1sliHElwX6265jVfnBmZojdjtkNDXQmbtelUSQMfbsq9v6fEicyukXLJ5qZ0lzlSisTUJI2BPAuFe+ri7n/GAr4fzQTlkt7Cz2IRdBncFUqeNp+51DqkOZUKYGcFKPd7iwq0XONqtmCgqNqjYyw6M0syZHyrmzkd4xt8CIqfchDzKglmJLj2FN3UEYTWKmpKtTbVGheB4iJXK36Q0RpFXkQwYOINjRBKjWBFI2I1RBtHd7H487JBbfNQQ/9hH1RBcO8nUYex0vLXhcQWnNHVbW3eeZdm/vsxPVt8f7738my+zzc99/p89Yno+KXp/G+Xx9DJ0g08PXp/+XcH+9uGl8VMg1vORWpv38dtjqb97oPbxX3s6OdMYn++KvT8Tfz5r79x4fqn6JS2Dvu2a8Utb5Y/3UsAOr2/nNzDb+SVdH3x//yj2K1twnKRN+KWrvjRhB45e5tcj57dNwiB1u/fT+O0pI9j59vbUF5wiv4RNPev69kYDUBF/RV7xlz/+N7DI2nMZLwAA -->
