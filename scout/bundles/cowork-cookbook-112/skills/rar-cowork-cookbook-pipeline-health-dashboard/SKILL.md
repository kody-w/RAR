---
name: "rar-cowork-cookbook-pipeline-health-dashboard"
description: "Reads open Dynamics 365 Sales opportunities owned by you or your team and generates a single self-contained pipeline-health.html dashboard with value by stage, age distribution, owner breakdown, and a sortable detail tab"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pipeline_health_dashboard", "rar_sha256": "7b13e935c0a3872c04e9c224871968fd0e6fb88c98a7bc78661831acdadc1a58", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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
