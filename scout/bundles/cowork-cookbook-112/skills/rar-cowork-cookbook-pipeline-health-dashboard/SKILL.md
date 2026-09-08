---
name: "rar-cowork-cookbook-pipeline-health-dashboard"
description: "Reads open Dynamics 365 Sales opportunities owned by you or your team and generates a single self-contained pipeline-health.html dashboard with value by stage, age distribution, owner breakdown, and a sortable detail tab"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pipeline_health_dashboard", "rar_sha256": "7b13e935c0a3872c04e9c224871968fd0e6fb88c98a7bc78661831acdadc1a58", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/pipeline_health_dashboard`. The original RAPP
agent is preserved byte-for-byte in `pipeline_health_dashboard_agent.py` and in the RCI capsule.

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

Pipeline Health HTML Dashboard — Reads open Dynamics 365 Sales opportunities owned by you or your team and generates a single self-contained pipeline-health.html dashboard with value by stage, age distribution, owner breakdown, and a sortable detail tab

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
  Upstream entry : https://coworkcookbook.com/recipes/pipeline-health-dashboard
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
    "dynamics_environment": {
      "description": "The Dynamics 365 Sales environment the plugin is bound to and should be analyzed.",
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
    "output_file": {
      "description": "Name/location of the generated HTML file (defaults to pipeline-health.html).",
      "type": "string"
    },
    "ownership_scope": {
      "description": "Whose open opportunities to include \u2014 the caller and/or their team.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pipeline_health_dashboard_agent.py` and embedded as the fenced Python below (sha256 7b13e935c0a3872c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pipeline_health_dashboard_agent.py` first:

```bash
python3 pipeline_health_dashboard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pipeline_health_dashboard_agent.py   # or on stdin
python3 pipeline_health_dashboard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pipeline Health HTML Dashboard — Reads open Dynamics 365 Sales opportunities owned by you or your team and generates a single self-contained pipeline-health.html dashboard with value by stage, age distribution, owner breakdown, and a sortable detail tab

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
  Upstream entry : https://coworkcookbook.com/recipes/pipeline-health-dashboard
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/pipeline_health_dashboard',
    "version": '3.0.3',
    "display_name": 'Pipeline Health HTML Dashboard',
    "description": 'Reads open Dynamics 365 Sales opportunities owned by you or your team and generates a single self-contained pipeline-health.html dashboard with value by stage, age distribution, owner breakdown, and a sortable detail tab',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'pipeline-health-dashboard',
        "upstream_url": 'https://coworkcookbook.com/recipes/pipeline-health-dashboard',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6d2aa6bb87aae92a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/pipeline-health-dashboard', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'Prerequisite: The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'Prerequisite: The plugin bound to the environment you want to analyze (gear icon on the plugin tile)', 'Output matches: A single HTML file that opens in any browser with no network access, showing pipeline value by\nstage, age distribution, owner breakdown, and a sortable detail table.'], 'confidence': 1.0, 'deliverable': 'A single HTML file that opens in any browser with no network access, showing pipeline value by\nstage, age distribution, owner breakdown, and a sortable detail table.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'dynamics_environment': 'The Dynamics 365 Sales environment the plugin is bound to and should be analyzed.', 'output_file': 'Name/location of the generated HTML file (defaults to pipeline-health.html).', 'ownership_scope': 'Whose open opportunities to include — the caller and/or their team.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets sales leadership share a current pipeline picture with people who have no CRM licence — finance, the exec team, a board pack — without exporting spreadsheets or granting access.', 'expected_output': 'A single HTML file that opens in any browser with no network access, showing pipeline value by\nstage, age distribution, owner breakdown, and a sortable detail table.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['A Dynamics 365 Sales licence and access to a Dynamics 365 Sales environment', 'The Dynamics 365 Sales plugin enabled in your Cowork session (+ > Customize > Dynamics 365 Sales)', 'The plugin bound to the environment you want to analyze (gear icon on the plugin tile)'], 'prompt': "Using the Dynamics 365 Sales plugin, build an interactive pipeline dashboard.\n\nUse search and describe to confirm the opportunity table and the columns for sales stage,\nestimated value, estimated close date, created date, owner, and status. Do not guess column\nnames.\n\nRun a read_query to establish the range of estimated close dates present, report it, and base\nthe dashboard's time axis on that real range rather than on today's date.\n\nScope to open opportunities owned by me or my team. Then produce a single self-contained HTML\nfile 'pipeline-health.html' — all CSS and JavaScript inline, no external dependencies, so it\nworks offline — containing:\n- a header with total open pipeline value, opportunity count, average deal size, and the data\n  range the dashboard covers\n- a funnel or bar chart of value by sales stage, drawn as inline SVG\n- a distribution of opportunities by age since creation\n- a breakdown by owner\n- a sortable detail table beneath the charts\n- a colour-coded indicator highlighting stages where value is concentrated or deals are aging\n\nUse a readable, professional visual style. Make sure the file renders correctly when opened\ndirectly from disk.\n\nDo not modify any data. If there are no open opportunities, say so and stop.", 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Open the generated HTML file from the Cowork output folder to check it renders standalone'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a shareable single-file dashboard with inline SVG charts. No external CDN dependency, so\nit renders offline and can be emailed as an attachment.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads open Dynamics 365 Sales opportunities owned by you or your team and generates a single self-contained pipeline-health.html dashboard with value by stage, age distribution, owner breakdown, and a sortable detail tab', 'example_request': "Build me an offline HTML pipeline health dashboard for my team's open opportunities in Dynamics.", 'inputs': [{'description': 'The Dynamics 365 Sales environment the plugin is bound to and should be analyzed.', 'name': 'dynamics_environment'}, {'description': 'Whose open opportunities to include — the caller and/or their team.', 'name': 'ownership_scope'}, {'description': 'Name/location of the generated HTML file (defaults to pipeline-health.html).', 'name': 'output_file'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want an offline, shareable HTML view of open pipeline health from Dynamics 365 Sales without giving the viewer Dynamics access. Read-only; no data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Confirm the **Dynamics 365 Sales** plugin is on and bound to the right environment.', 'Paste the prompt from `prompt.md` and send it.', 'Open the generated HTML file from the Cowork output folder to check it renders standalone'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PipelineHealthDashboard(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PipelineHealthDashboard'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'dynamics_environment': {'description': 'The Dynamics 365 Sales environment the plugin is bound to and should be analyzed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file': {'description': 'Name/location of the generated HTML file (defaults to pipeline-health.html).', 'type': 'string'}, 'ownership_scope': {'description': 'Whose open opportunities to include — the caller and/or their team.', 'type': 'string'}},
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
    print(PipelineHealthDashboard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
