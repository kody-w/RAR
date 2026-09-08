---
name: "rar-cowork-cookbook-dashboard-develop-frontline-team"
description: "Pulls develop frontline team data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_frontline_team", "rar_sha256": "f9f0cd18acf4c5d651ab44a5a34ea31d2374c9f98c89253231b2a9155d013559", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_frontline_team`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_frontline_team_agent.py` and in the RCI capsule.

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

Develop frontline team Interactive HTML Dashboard — Pulls develop frontline team data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-frontline-team
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Name of the HTML file to create, e.g. dashboard-develop-frontline-team-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated file, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_frontline_team_agent.py` and embedded as the fenced Python below (sha256 f9f0cd18acf4c5d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_frontline_team_agent.py` first:

```bash
python3 dashboard_develop_frontline_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_frontline_team_agent.py   # or on stdin
python3 dashboard_develop_frontline_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop frontline team Interactive HTML Dashboard — Pulls develop frontline team data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-frontline-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_frontline_team',
    "version": '3.0.3',
    "display_name": 'Develop frontline team Interactive HTML Dashboard',
    "description": 'Pulls develop frontline team data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) and writes a standalone interactive HTML dashboard file to the output folder, read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-frontline-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-frontline-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c0983789ff77e056',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-frontline-team'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-develop-frontline-team', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the HTML file to create, e.g. dashboard-develop-frontline-team-2026-05-24.html.', 'output_folder': 'Destination folder for the generated file, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop frontline team with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop frontline team data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-frontline-team-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop frontline team.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls develop frontline team data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) and writes a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build the develop frontline team HTML dashboard from USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to create, e.g. dashboard-develop-frontline-team-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated file, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of develop frontline team D365 data that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopFrontlineTeam(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopFrontlineTeam'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to create, e.g. dashboard-develop-frontline-team-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated file, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDevelopFrontlineTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916Z6/bWLblX9HcB0xVPdqXYhTlhweMAkkxiGIUJZYbLuacg0TW9H+fQ0m2q7rd093AfBrZhgLP2XmvtY/J39/svovK5u3Tm+bbxYK1syyO/GZhF95iV97KJgVvZeqAfwu3LLomdvqubNq3D2+e37pNXHVxWYDtcp9l7cLzBz8rq0XQgLVZXPiLzrfzhWd39iIom0UX+Yu8bLtF47t+0S2CuHXtbFH5TVx68658sR8LO4/ddoGRxIL5n9ruuPg580OwCmyIu3FhaEfml4eBtybu/HZhL9oOfLWzEuiLi85vbLeLB39x0I8i0N1GTmk3QHycAXvKhxFl31U90F9mnt98AObY3seyyMZ34Jh/t/Mq89u3T7/+5cNbDD6/ffr9zc3sFvz0tv8qb//0lfnqqg48BbszuwjBsmoEcS3Ad+Ab8DwHP3l+sHh9+7n1s+DD4j//M73ZTdj+8ulzsXi9Pr/Nf9S+eNjZlXbb+d7CtSvbiTPg//tik93ssQU2d31TPN1v4iJ8f+78Lgnk4b/naz8/lbyHfvfz57cSmGDPSfv89ssCpOTzW9PPn99nKdXPv7xn5c1vfv7lu5y2dxLf7WZhwOr3L6/vL7Fg4felcbD4osn07qULZDmufCD8D/7Nr6fpL3GvkHx5Lv65rD4sfix59ue/gb3PwnOA3B+LBTEAO9/ekzIufn7paMrBL+zC9X/+5R+JdSPfTbO47f4lub8+BUegcEC0XiH55cMjfX9ZQC/fvsn8x2orUDD/jidg+Vd13wL1j2Q/Mvs3oudSbb/l8ofifrQB+u/Fr//Qt//bhg+L4PPb3s9AQza2k/mfFr8/SuTXn7zvP/70l78C0f9UjFb2jfuQ8CW3izjw2+7Ll19/ah8///SXX3/qK1DFoA+/9E32I5k/iutDz58i+Fr185/3Av1GkRblrVh866HF72X1P5q/vi/OdhZ7339vPy3+2InzC1rMTnxV+gzBH7qxBbb+IY6/vP0VQE8BvOndx2WAH//xH4tj7DZlWwbdQnMBhC1Agrs492fj9ShuF+DvjBoNgKamjUFgX+tA/c8Zni0ug8Vv/8t9QPtH9wXt8DeQ/PJC8C/fEPzLjOC/vS/0GTWbOIwLAMXqRpY/F3Y4YzjQWTV+6zcDwCln7PyPoJ0/zh8AGC9++2eivzykvFfjbw9Mj5+4p+64GfPaPvPfZ+/MyC9evriAp/y77/ZAQVbO9DEDezuDeFtmAPa7ORJtGmfZwosBqgC+Gh+yQbQ+zcJ+++03B1j1uXiCNLZ4ElkLgwXfzFl8/AjcCrI4jLrPhe9G5eKn3//60+J/L/5vux7CZx0yYItXLoCFvHaSFqC3+hwsA2kCiQXA8cjF7399BReIKQDzgszFQew/N4Mopb73NdLaYfMRJciF44MIg+jmVdl0APkXcfe+4ILFN3uB0vnSzA3RzLaeX/mF5xfuCKTawJ1vkSzKbtGCAmyD8cOib/2H1t+cxn6YmIMmt7vfFsedDJiozGb2bF7MBDaXRQzC/60Onr8DIc1P7WL7VcT7QpqrcVHZjV1Fjf3SEdjPvAAG+rodCLcXhX/7XMyc68+herTGMzxgEYiM+0rpxweZu2UOcMBrv+p+rLFnvtQfvNl8LtpX2dvNnAoX0ABQGvaxN5PBf71Kqo3KPvMe8fOfQ8orC94rK48a3P94uOH+duL4NiEsPvfoEsEX/7/MRnMQNiyr0uxGp/cLWtLV6zM582g42/ycJmdLnh6BRvw+uXxFp68g/bnIYlBpzfhfz5UPG15rnsDXNyAD6kZ9yAf1BJIzy32U+1y+TTM3iv25+MoGH4DDD+gDGQfYAHpnduqrwvnqV0sj4Pr8/ftk8CgPEAoQLlDSi6p3MlBuge97ju2mwKo5EF9TWszxBO17i2I3+pNXcypAiQH5C2BEDJoQMMb7N4R+Xv1q+p82PgegectjOOxBxzYPAcAOfzbwkde4A8Bld89JHPj56SEEuJFX3ey7A3oGePr80W/8uo/buRQ+vOLqVwCbP87vT0/nX/17BdoEBOuZ+vdn+8zIkoPxBtgAiheUTh4XgO5BUF5BeAi08xkLANa+5tGnxMfPL4f8R8/NPPV14+zIvGem/mdl28X4R8jQf1QmQF4+r3jo/dtK+6Ztlj3DZgugD2j8evU5I7w/af45Ryy+yv30d0edn/+909CDuI0/F8CnRdR1VfsJhp9k+5Vr3wFowU9b2++8+/GFDh+/ocPH7uH7H+Q+Xf60+Pds+5OIV298WiDvy/flfEl81dbrBUKx+7i9fsTnq58L1f8OqUB9mYPimhM3AqL/xn9flwASDBuARmDxkw/bmUZvgLkfBACy8Ln4Y7HPzQb4pQjn4mzLP4DAYxAAhf9M2jeeApdAbEZAAUBe6M9ntUdrtP7bpwJg7Ic3AI/+v3BGm7konyu6nU92oHcAyHax//j2AIh7N3/88wn39PhgZ++LvQ/AKGv/WHUvBpkZ9A/N8XQSOOcCDR9mqAc9DwoSODkrnxvLbkGlgiKdnenGarb+eZybB8AnBXx5UsDfW8T8iSFmbn7QPsCd/wING9h9BmL4AvU/Mos9APPn3vuh0gehfHkSyt/r3M/U8yfOAQrq3p9R/I86Zyb6ofhvE+/fyzbBsDHv9cpPM+9+eKEaeAenlA+LbwcOEMnXEfBxXC96cLr+dT7szKl9bJk/gD3g7dumb/9j4fhvf/mRXQ/o+zLX37OK/tY6aYY0APlzNB/s+ZUzXVDQHUiv/x6+L/5ZR39Elyj5cUl8RPH3qMuzH8foZcuDgX+QA38G5+cB5LnmG8x9b9fZupdN+9J9Dp7wEyjgp3z4B7qB8gdlAOKdY/o9Wd9DVj4Oi7OZIMTd8/82fn8D7WTPo8yroV6nDbAcIOzHdp6yYIA5QCH4/kQHcO3fPoe89reRDeZgICBYB0vXQyjbDXCX8EgCsR0ctwkbw30bQzwUW+HuOlhTLrVGCQzFEAe11whBeEsEI4g1kPfEmC/zKBnPNs0GgVB8BDDlf78MfvJezjyNnyP17dgzO/3y6fc3h8TBygPecpvnawevEQfGRGfkD1CxpO4RonjjVaEPer/K1/uiXhkZCvl153kZgCikcrYhvY01k6Ov4sZWJuZUCSGk8tSoY5K7Po6bTVgJFAv5mgeqm66SivTT4AJDVzDyECEiEcL5dI4RM2oTXjrGmcCaK6YmR0NV4/NoGwYMy9BaD2JJ0pxKqUVTntYNRukO2S4RTeyLe3+wtMiso32mlnW3rI3S2mmTUd+0w9WsRtZUaz7KHfdSiWGPabbOlCME0zsYoqAp7dQ4c0tEzfmdcYIPHuq3l+udyVsnrNOMr2ml8vC8vwr1ePGk/GhP1kVTKojZn6I6EYZWJIQrkh1vNH7VEdNcDdMWPxViBkH+gE0kPOSVL69y2GmDQKZ9euTbeB+eakxIdr24X+0ClQubyeXzdL2ZgvhQn8k7l3b4cWmqVtReunabcHsvDNkzw1iMzpkrgoSuMBcRjHFDbX15t1st4gBhKstTl7NmIyg9v07aSrsvy0RQ6z7ctSs66u7j2rvc+5bFyCIKaiO3IibNtf7KXTmh3BZZIEpcQWtthbPG9YJzWXoTmqPGETVv46jmqNXq6hnGaeS6cLPXrllwvmf0uiJQa40TRTbo7UHQNKIMl+szfd7m9NTJ2zDWTZPv+F7NaeucpiPZ0NveO27g+0ARHDook7hl2uUeNaKALDU9qAPzUAiB2Li6n2IOQftjCREJXXKjHTp5pkViJbWiY0W6PG2uLN2joypS+yTG9NPd3fRShKbCVLOJvoHrCrs27UFqmfDOF6lOLeHotlPQib0Glp7cmpLhbt3eyBHREJZSo20YcrSRANFSBTC6Ft0NK5ICz6zJmuNZZbhvM5jhVvWFH0sBObs475PmSYBZHuOP2+NwO0Nj6O/4a+FyubIUL9GZ3PNN0OkGxBD9OMlnSio7/JrrBWQd7CkcEz+zVmin726ixoZasVX4U4v6hBtsq0JXGnPvO/Eaxvfw7eAHrNSNAblnaTKfMPIKh/SwheDUbAVCaThGFFC03V00ZIm33pI/qJZw8Xub3Z4Y8qJs78dtGHDKviOmDt8gRGJYIlSyhUUwssq3k2lxlS2dR69LJdMpFGZDpeNZqaUzsRf0Vt/ULCcdLtUGM2jltHPlzcDQl826pAnyJCUbzRlJimunSXCO0w0n1/EllRtexU/wZJPspWZE6aLmuzPt6cKODi1lOWziiilljgsPq6JwbXGSpBvjlIychCXCmUVq3wOicxW+m5BkFLVJn6RMWlFH5F5PE+7xTObe6gwNz26DS8TI4Y6o0dzK3Jib2y1fk1a0U+X2vDKvfZS1RibvNiWja36aF6qxXuXn9so3Ura+UDInBth1l7AbeiNZxPHEWNqwg0Sj9hrtfq9Ge2VBdbrhfWNna9KNclHmahVNuE2OEINwh6OYZ3C8Ll03LPBp5OjdpekDA2Xlc8+eyvzYYRlKsjCNThWAU2G/N+/b4rhXxxBW6GTsx0138+5Rh/MnGTXlKCCcK9Mo+DlRdq7DHrb27Va4olWGvbKvZGPJ3E1NrfSG60WLuZBIHFiFy1LUmUm2yTnF5WJVVoIO6+0kp1HMkbFZ3HD5PuUyiUTyRMW1xhah6O3d4qSnNBQvze5E9fCO9GDRs9c4dpA1zaE2Ko5VE71zRbRNWOUyyD4pqA3PQbq2t1O04j3jiLHVpo2o/cUbHbcfbjxSMCNXrdacuOPYUyaZ25DaQ0eFVJJMqAE+3WM3PutHawC2X4bAOoBgWVxEx2mSkSwquGiaU2eFqAVLj72utk5BiJ67YcculYzYt9elq221s64B3Om0HrrHaHE0K2nXbtL4jA4IbRRudTtPvby60eeCjUMSZfYI2reXGLFAUq/dylKkqatQd9vmdpMlW8FBdX/QKxI+XbqTwsjchWUDhdcClTiX2Yk5gMmt21wNnyXVzbGQE1ilkOWJzK+K14ksiwXyrpCnFUmWa9isUQhKSwg68aINCD/N/P2RgilT5JiNW4YmzBOufIx10UhVGjHrUauNeB/B2y1kkPP5hdpcjhgDPE4GKTN51ynDfTSkxyGqb6lUkwy5q2OfzjTHoLcqp4UGs89TgRWSm6gaxt1lmBLdMix6SviWEDFzaBlK2DSDRQee1zIN34XcRbw6k57txhXVeXqyMncMitwgL+pt5hIok7fTdmE50lNg0WGtxpoeC6VmoofDYU/TLG9RhRMUDX5zi30si5RvDNuL2miKf93idOjmnr6nsHi1zvEcjwx1d5FRA0vPADWq/fWGq/e1u5myyMxT94Lb1fI8tI4Y75SUv3BJY5PNGDYKpGkac2FiUlcIXdvVahbAZLarDYEZFe1cXHt2vDWb6HRbcpOuufkq5gqyl3K6MrKU3DBpYckuGE0gBbkkFFvmrQ/wsj3WcWIbBwVxufMl17j2uBbIFjdMMafrnXXi2o113ZgGIto0CHuJiKwghgXT7Az2yJW4R17udGtllQaJSk6bXoZOhFKr/TbQCaSMmXHZXlkyi9zCFCidrSuTN/1jkgV7rjfWEi5vN7ReyFJguDuHcCAl57oiB1YxR6xZZjx+JI4ex8UCBYr4DFijDgR201KQuOkMyZgEAaWhKzJtjJEwuE2n+aMcHapEyNE9pZq4Uh3r5B7E0xrkEEqMLaGI1Omyqnn2tIGumcz6oFXRg9vwOR8wAn2Ehmp3d4YKud6YA59EkZejIoEL7F2N08MRofglE9xRXC3d7ZHKNoIerSB4SrG9vB/ccyJIKYCZDLVuGI3sDtiBTYwoLrdNdA7TMFF6Rd3aWbcpJlzQ0LzZSYIYMwaN1MlYjXnfUnS+ukHXHVkTUc5uGWkXZQp2dZnDaXdDbkO+pFeXLKBVno1A0M8HKSooeZ8K1g6EY3NTT2spOjS87dE4nK86igu3jXXS2/YG1Ri/QXZIGB3XzeQV+Sgh+m1bbZYs324igVp65P6Eba+wTVb9/XLDltN6oORqrOsu10up10+6dL1Dy+0wUFhqK4wtt8fichDOhsyfqJSB1IHph7WmxOQWlnOXXovZcquU1U7JlB7hdnSuIVwmbdjIhS982lfX9HhVmd5RbvejRaLUiF0a81DHyEk/JdfVcRkHQqYcdjSD4FRsHNJE5IrNsryUJoTTx3ZP4ylpnwwyHKRjzkC6hTjmvjaz5qbag7K1LQ0P9Y3hZcmtbJX4ekY7M5+UDT7cVITP3Gw8mOMeDJvZEi3P93G/dW1Gyowq55aU6dF7khOUiM0pzj9t/W7PXSaBOKpxzTsGSa8lH+p3IDp3CvLlJFsf6csS92BqH2RSjnb31AA+9ZVGuUJnnzHHyLrrim0OydEoKGFJoZLW2IWZWOySLEw0dBp7CCc9ToL1XjnvIkehVJ+WtyapXaTIVvhNpCNSWnBKneHAqD51bfN2Y9tYPtZ1iZv7uE2z87hrSlEPTUHkplWK24GWg4n6ugWzb3iUBzLAlCWDCHx0bvdCA46LKyJKg/WxF297buutzuD8tiaW+U4VKiSvJd9nbXQlxiXT02k97vIDYbloM8SeBse7oXYS19GxIWAvZN3e7lKz68vwLCi0Y5Km3LJMmE1ieo3qTLhf3RNCZUY2hiUqp8RVMbOzJqLRraFdF8hJ2NUUq2F3tNwUjDGbjHGF3YoOp4aANQc7bTL8riRXNmIkKzoLZkXzbaLTSJkbiML1Dm47KagokQ5tLthCezxhg7Ot1UJtGVJ3rEa6b+nsGO8PG8OC2AxjJeky+SeMx0czbO6j2RwOl8BmLP92ocdpuqDOSI2MyZxSDr9GhjNJShxtz36HCE2BKVMThOdDavK1TUM3zhnTtV2koXW9BdPWg1mMugkXujyG2/3O2xemT6WbpeGMp7HXD0GkkrvdToU4hg9bTm31gO7qyDLLTsMjBRbg63kJqudkJ165rqbbWmE5S8DAlKJLtXWgRUYi1TFOnasQDKNuj2dYaYNeXQZWVpJDsBaxzBwwF69og9+ytnk4mAp0tu+FUFPLDhDqcG42VR3VFtxMw/52XhsW3+5YljRGTh51Ne4BERCExQ1eNweIzdcrSxtjlzwFnmxstcA+i4ZXXoiRAP4M1RlMTAenDEZ5POuu2yN0zULriYjg084mTYMKWBjCEUEtrtZxg1k7bLNWU7TvGESyczGBR72ogBe+gZ3Kk6AaYM50rTPVu9U9uYqecsbSG+/fbiWCWKjMnqMRZTGc3O7dsSiNEzrsGN5btmKibxWME3a6pPM5YOCJTC4BD3EmpyZKUBpX0G1ZQiXGJopxxCIrXq8PfWQTte4iAefZ0bmUq3StHAjYolbXix4XQ2nJ6lB2oXk7+QTKQvZZPZKRGBzSnQjbDF0hRUrhWeLcwGB5kcp11LPdBGhme28UZMTySO97UchlNodX0Y0EK+hp3Q7MGrWas8xOrc72EE6Jw1Duy21f+IGxItOLIvhDPFxqMAUcDLGs4zUIymSK95tcQtLEVKfOyenrAUIFbBjuR0EiJ7d2adg3t7XpS33fDCa0lyOmDGmhJQ5XQASt2wuHNi97nFbEHbpHN7GHWF2A4nJ5hZlwKZLFvbg6+YFDvDqQqC3COkkFBtCVEU2Tfdl1y5ospNzxVxKb34a9irJUlG9YU4oEabuyV7Dsw7BqwDXXaAUzcYGMYhCYv7vrcuxyj3JVw7TX2MY5g6Ojd1dX+mpcMYmhbskiDvTtYXu58Xe9S72gOmIyqJVQqq7Lo6vC4BCxIfghuQ8iI0Pt/YCv7aXFnvMpXBvOjlCBWfuplUxuLzJ1h14IZ9oeaO98bUfqqk1LOO50vGuWqT5EHsbst5VQCBwMoVDf97Do8psVHd97fJNCK1vn02UwXiuZrZWNc1P52wDV6tCv+7zzw47IkPvS2RT6UuvKpcwvg4o/t4Vc36Fpr8NH0mzYHc9tBYs77Ffw/Z5hVh7Q0lGll11zMblx3AnV9eyjdmeTQ3a3GQUwQbFJu2EpxSfWK/wEKTIPSVjudoSPjlxgqUjp1TjIO7ZvNcmkszOZtWrssjppTiWW2N0uTPcyK9gXTE7ivOAtbXLvKpwdDy5L0xcp1a+Mfkl3DnRAkts65LFbO6UJOFMYcrg6Zuy5I5wx5rpa8+BaxSnAc8oaw6bwKgrHNotdWFD71ZKfSnZ9yHlEgtlrCKfeIbI8Az1A+W2VhbmLoY6eTCu0oC20oK7nswtN2lJCCRNMuuOxJOwmvrJ+2jEpmjQsJR80DVUVfbJjn19noox3W3eLotZFDPK91VmCdjiRgN9uElHenO6uIpG39XDYhpDj5ZAW0DgA/OfQZjJReQ1OcQhRoHkEl4wk2/x075jCj1EL3neoybWSgq+1M+7HlAWiPN7xybttaV5BvCOPY154E7kDvAwQlZfqmk+O/v50nzKD0YY2i6CONjXTp+11uNexDoJu7VWuGgN04aqxXVQ0nODkTp6vusBrWd7XZ+wkO5WS7fcT1O/9kx6MtS/TuRoFp8QoKo4iXHNoBofoeJ+EYnYa/M1Qi57AeHoVU6th2R+mYp+ZWnndBnU6sAwT7gtwdHKWCubEGGZ2RnTt9Mrs5c3JPkwTQU5EWiRxkRTGEKjysfEuQ7HkTtRIb/30AsiaJlXy6iwd11uGLH8hEG4k19SyhIfLuIm70FgevRRdbwVJgLbYhru1JmGRoXKPYJ7ZNzUMOEYhlsSyXXLHxCdFjRRPkSWtqDBJSgUeUTHhWl2OUxSL/Xtdwlt0T4BCN88rqk9v+QVCzisayxUYXW7QDVGL6UW6qTshFzde5oV3GOyxwhVL48dabnX1KMir1RrHHQJMUU48jGMpb8PKxDq9NwP70DKalGNqqa/wW5vc/d6pcrQqDhJhk+eOxU7IlFFjTWjm7dxg7XFUg0vWWjWy1a2jlcCtqYarfm2lKEFmRSDmxiQbp84+1MO4Oq0hnxK4m31MchtOrBEDkTfvd94vBuaaFrC8ORi1b9yFSyLzh9hAdn6eRNvYnHzE26UUD1HH03Wpr3bOiPJm52DmiVgNiLeBhULit/R06Qg4MsUbRHhLmLz6p8BA7T64nGmLs64cQUPxdrrttNP+Xhc0FnSBf4HyzW0gl5NJ+lgoCb3fuTi6d3T/QkZjjzkrQJN9LaK3OqTcy/oietyqcrJJKRzZU1a7nmQJMkf4KDtR8m6vSXuETk7R2jkTw5ihF8Q57dYxdTvpTocmWedD7YWDb/6ao7P+ug1r/aR2HrFeibKJ9hOxCs+teye3+DZcTyPNMaDd8Dutq3KfU5fNdiSlS3TXRKuSUFjKPbokkGMqx0VN7U2fpUjS6VyRPPoaCLNY+oQabOsSaw47kexLZ/QhKl1hDI6hZzOYzv3Gg/LOs1eJmK0gDLlj9Uqirq7c1eoJ2qnYYZLLbcXjENmdETQ9M/fz3u/uzkWAydNm1eDyctR9GfeD7nLyrOTcbB08WO0wwKyug0BXyOEIogpizD4nTnC85dcGXq8M2rZK6j6uiWYsVGylNa4d+Fh/uDshjuvQVtdTbbMhsyuUeEfauNGqLJ2ZlIdqYSrX/cFTEUpbnbOGi/0TLkHmRDual+4tbeke1iHAWV7krOIy8Ae3F/d9gkio4+zEYMBgY0CqE3PoT45P2Z5T0MPkS1tCtQQV7SlwnD46YW+tlyx+t5cGGQv5QWGkk666B+mKrPEehu8NLu22GL6LTsEqPAYenafjjWskEdcn9dAh65aV2xMHVVkRRcNBgaE9NWqM2BtKuNm8zXdGv96me/uXHzCb7+b8P7tx9Lz/8/XZkcf9R9/2Pj10ffrXTfrLh7fGjYFBz5tjbdaHr9tMf3Nr7OM/u7E47x6fz2x9vYP9vCfe2eH8KPNbXHh92zXjl7bMHk+OgB1O385PP7bzA7IueP/jDdRvCmfJPjiBucD48svrqc23+fHE+ZkQ34vtzn99DV93C8Hu16NKXzCS+OI31ezp6+kD4CD2vnzH3v76fwDZii9Afy4AAA== -->
