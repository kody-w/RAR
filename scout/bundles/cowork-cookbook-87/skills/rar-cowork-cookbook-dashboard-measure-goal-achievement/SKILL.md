---
name: "rar-cowork-cookbook-dashboard-measure-goal-achievement"
description: "Pulls measure goal achievement data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_goal_achievement", "rar_sha256": "3a058812a11c17982a6e5ecbbcd8c90953f5233318d6f10ab0ab6759dd5cbcf8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_measure_goal_achievement`. The original RAPP
agent is preserved byte-for-byte in `dashboard_measure_goal_achievement_agent.py` and in the RCI capsule.

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

Measure goal achievement Interactive HTML Dashboard — Pulls measure goal achievement data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-goal-achievement
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
      "description": "Name of the HTML file to write, e.g. dashboard-measure-goal-achievement-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_goal_achievement_agent.py` and embedded as the fenced Python below (sha256 3a058812a11c1798…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_goal_achievement_agent.py` first:

```bash
python3 dashboard_measure_goal_achievement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_measure_goal_achievement_agent.py   # or on stdin
python3 dashboard_measure_goal_achievement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure goal achievement Interactive HTML Dashboard — Pulls measure goal achievement data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-goal-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_measure_goal_achievement',
    "version": '3.0.3',
    "display_name": 'Measure goal achievement Interactive HTML Dashboard',
    "description": 'Pulls measure goal achievement data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the out',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-measure-goal-achievement',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-measure-goal-achievement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc3eeb7cdccfd7a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-goal-achievement'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-measure-goal-achievement', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-measure-goal-achievement-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of measure goal achievement with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull measure goal achievement data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-measure-goal-achievement-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing measure goal achievement.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls measure goal achievement data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the out', 'example_request': 'Build me an interactive HTML dashboard of measure goal achievement for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-measure-goal-achievement-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 measure goal achievement for a legal entity, without the viewer needing D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMeasureGoalAchievement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMeasureGoalAchievement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-measure-goal-achievement-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardMeasureGoalAchievement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaWLLmX2HeGzFVdbGtfXNHR4wALYAW0Iood7i0S6B9A6mm/vscAV6q23379sR8GsoukHRO7vlkpo9+f3P7Limbt49veugWC8HNsjQJm4VbBIt1eSubK/gqrx74u/DLomtSr+/Kpn179xaErd+kVZeWBdh+6LOsXeSh2/ZNuIhLN1u4fpKGQ5iHRbcI3M5dRGWz6JJwkZdtt2hCf34Qpa0P1lZhk5bBImrKfLEZCzdP/XaBkcSC/5/6Wl4MqfvY+RKJ0w6LKuvjtHgI2rpD2C7cRduBKzcri3CRFl3YuH6XDuFCNGQJCNAmXuk2weJnP3Gbrn23aMumc70sXDz+/26hsQLYF6S+CzT8ZdGVD5Zl3wFlw7ubV1nYvn389W/v3lLw++3j729+5rbg1tvmC3H5qb8A1Ge/aQ/2Z24Rg4XVCKxdgGugL7BGDm4FYbR4Xf3chln0bvGf/3m9uU3c/vLxU7F4fT69zf9pffGQqSvdtguDhe9WrpdmaTd+WLDZzR1bYNaub4qnNZq0iD88d36jVFaLv87Pfn4y+RCH3c+f3koggju78tPbLwvgpk9vTT///jBTqX7+5UNW3sLm51++0Wl77xL63UwMSP3h8+v6RRYs/LY0jRaf9QO3fvECnk+rEBD/Tr/58xT9Re5lks/PxT+X1bvFjynP+vwVyPsMRw/Q/TFZYAOw8+3DpUyLn188mnIIC7fww59/+Wdk/ST0r1nadv8tur8+CSehGwBrvUzyy7uH+/62WL50+0rzn7OtQMD8O5qA5V/YfTXUP6P98Ozfkc7SAqTQF1/+kNyPNiz/uvj1n+r2X214t4g+vW3CDORnM2ffx8XvjxD59afg282f/vYHIP0vyehl3/gPCp9zt0ijsO0+f/71p/Zx+6e//fpTX4EoDt38c99kP6L5I7s++PzJgq9VP/95L+BvFteivBWLrzm0+L2s/kfzx4eF5WZp8O1++3HxfSbOn+ViVuIL06cJvsvGFsj6nR1/efsDgE8BtOn9x2OAH//xHws59ZuyLaNuofsArhbAwV2ah7PwRpK2C/BnRo0GwFHTpjPiPdeB+J89PEtcRovf/pf/QNf3/gvwoa+Y+fmF659nXP/8Ha7/9mFhzBjZpACLAYxr7OHwqXDjGdkB16oJ27AZAFJ5Yxe+Bwn9fv4BUHbx278m/vlB50M1/vZA+fSJfdp6O+Ne22fhh1lDOwmLlz4+qGDhPfR7wCIr57ISpQCz3wHN2zIDlaCbrdFe0yxbBClAFoDz44M2sNjHmdhvv/3mAbk+FU+gxhbPEtdCYMFXcRbv3wPFoiyNk+5TEfpJufjp9z9+WvzvxX+160F85nEANePlDyDhTleVBcivftYYuAo4F4DHwx+///EyLyBTgJoMvJdGafjcDOLzGgZfbK2L7HuUIBdeCGwM7JtXoLYB9F+k3YfFNlp8lRcwnR/N9SGZq3AQVmERhIU/AqouUOerJYuyA4W1S9tofLfo2/DB9TevcR8i5iDR3e63hbw+gGpUZnO1bF7VCWwuC1BFs6+R8LwPiDQ/tYvVFxIfFsockYvKbdwqadwXj8h9+gVUoS/bAXF3UYS3T8VceR/B8UiPp3nAImAZ/+XS97PPQa+SAywI2i+8H2vcuWYaj9rZfCraV+i7zewKH5QCwDTu02AuCH95hVSblH0WPOwXPpuXlxeCl1ceMSj/s7Zn+/dtyNdOYfGpR2EEX/z/3DfNpmEFQeME1uA2C04xNOfpsrmVnLV4dp+gf3npCNLzW0/zBbe+wPenIktB/DXjX54rH45+rXlCIjBhAMTRHvRBlAGXzXQfSTAHddPM6eN+Kr7UiXdA+wcogjgAiAEyahb/C8P56RdJE2CH+fpbz/AIGmAXYDsQ6Iuq9zIQhFEYBp7rX4FUzZzILzcXs3FBUt+S1E/+pNUCUAeBB+gvgBApSE1QSz58xe7n0y+i/2njszWatzzaxh7kcfMgAOQIZwFnH9/SDsCZ2z07d6DnxwcRoEZedbPuHsgkoOnzZtiEdZ+2aTej5tOuYQUw+/38/dR0vhveK5A8wFjAyVUPrPtIqhlvctD4ABkAroA4ytMCNALAKC8jPAi6+YwQAIFfneqT4uP2S6HwkYlzBfuycVZk3vOIukesu8X4PZAYPwoTQC+fVzz4/n2kfeU2057BtAWACDh+efrsHj48G4Bnh7H4QvfjP4xGP/9709OjpJt/DoCPi6TrqvYjBD3L8Jcq/AFAGfSUtf1Wkd+/EOP9jBjvv0OMP1F+Kv1x8e9J9ycSr+z4uEA+wB/g+ZH0iq7XBxhj/X7lvMfnp58KLfwGtYB9mYPwml03ghbga138sgQUx7gJ43nxs062c3m9gYr+KAzAD5+K78N9TjeAQkUcPmDoOxh4NAgg9J9u+1q/wKOiA7yDuaWMww/zJDaL34ZvHwuAvO/eAGSG/60Jbq5S+RzV7Tz5gfwB0Nul4ePqARL3bv7556lYffxwsw+LTQgAKWu/j7xXbZlr63cJ8lQTqOcDDu/mAgDyHgQlUHNmPieX24JoBYE6q9ON1Sz/c9ib28NnYfj8LAz/KBH/p7oxV+1HQwCw5y8gaSO3z4AVXxD+fb1xByD+nH8/ZJoBJ2afwTqQYP/IczMXpMeSxXPJzKDuQZa/W4Qf4g8LU5f5H9L92gj/I1Eb9B8znaD8OJfidy9IA99geHm3+DqHABO+JsOZQ1j0YOj+dZ6BZp8+tsw/wB7w9XXT13/e8MK3v/1IrgfufZ5D7xlAfy+dMuMZwPvZjI86+ohSIO4NYFD4UvtfZ/N7FEbJ9zDxHsU/JF2e/dhIL2HKDBSAH1g/nKH5OZg813wFuW+p+pDx503pP/tQ6IkP0JM09MsP+ALGj2IBSu5s0G+e+mav8jFAziIC+3bPf+/4/Q0kkTu3Na80ek0gYDnA1vft3HVBAGsAQ3D9RAXw7P9iNnlRaBMXdMaABObCBE0jqIsgPkIxNOqSIRH6nucHtM/ADIFFBIphGEIHZITArgf+kBTBBAHhe35EA3pPdPk8N5fpLBXBUBHMMGiEIygcgPRB8SCgSZr0CQqFXcZzCY9gXO/b1itolF6qPlWb7fh1TJpN8tL49zePxMFKEW+37POzhhjEg2zc670TdIKhlXqz+4p33MrMsdXZyJ1EpvSj0rZXV8dsKVnHJXKE80mMkSKZFNSSFVYkdwd0HVXU/T4eLvZY2JOBLnEQ6AB2Twl+KKgixqcidA4nvSpTE91fzvr92m4xswrqarcKh2t2z+Q2vejjackcKERZ7sy8R/bjeDMh6OJhtHXm/ECgtmS3yc3+blXFtqPrNpBznrjuXYEN8uNqMgmLVxOjMVSIIw1S68f4hnfiMNy3AzREwWh3d8HMwtDdD4HoJEVDMxya+d5+x43ro6lleL0ljzf1RBqtSZqp1PhJYmMlyjYtc5cThT9LWXjnhgniIBElzb5dkwpLXEovRaYpa5rtClcLCVkuo4gayWgoqqVE5FAwRNCGD283XmiGeCNJ226qJbqBKcfWuC2vEmkukUm33BqV4B54ZVTw9GLp7gTZMuVr6Io1fJ7DyziB7mv6sLdHvy1NLTcup100yNVKBQZUeyTeEUrZmLflzb8Olu2khZM4q3vgbAJPouwUJkRZEoLN4LrOYOl747jjbEU4rvsjdhusC2/qG1svzUawRnaHrG/kFdnWYtk1zVlrBTTQ8NXYpZHLxndOjUhSH6YVvkGDqSStgxTaDig3lqex97Df7Xe749m7+dI6SS+GRvHhyYv9aZL40lKPOH6+N3FERHmgpta0ln34RJh5VFcpN5r7SbnTmVEFkh3BHUNrh7o81E49rrnrfuN0W8XA7Kqk9cs53cGHVMOP+65RpWucRuyEMxwhUy4/CbKRipdkC6xNkiW9sX0rvlVirNEmNKG+4bSCPfI0PdarI9hw2wUuvO5EB469qEUzG+EIQS2XxjrdY4LX2yVsmvZeTsJUjOhyTKvpOhzUQCSd8gSlAUfttAOIjztv39JwL7rFVclvuGjl93pDnKzh4lOiQjOGfKZUlr+d+0KDSsy/jW7uWigMBwp32wm1o7hCrHdxGKYwdGnMYqX6Ox9SzhC+gdhxE6l5d4c42dgxyvUAICPxDyvb0wxfJ7aII/RMPNnafTinnebn434LK5QyjtmuV6rChQWDXsuuUiypZHO/CFVqQMdARUe3ZRU5E+RgCxc7VD1i5747moau7YM1riY7ObK3Otug8FoSuxXe8qPtNYSfzgPsdS3S3HhLzhnuL/lMvqLFJOPyDnLyIJnw2mBJSKnqc1bXVeaJcJ1d9LBylO54D9a6v90W+y1+Gc3oyly4mztC6Iip2wm/WryeXc89iixHTbgepC3ib5quIjK8N8iTgB8sAj60ZrtxmGt/cWBPwM2jbOHWqt+s8rXDyvQmYFok2R1wG4Fk8xhnx5UvLM/keIJHfyDum9bSms2dHnzFUBhtQyDH7L6pzfxU+arg3PLC0vKAUrPzxfBPsIHb16N0kbe0Ja4mqk1jLRrjXEaJ66gTlg/3VztzhOs655K1xtKkNGDKuaC8taXwfBwxymSe8Hza1x6Bl7IUyu0tHoZMRNmUluV28jeBo+nraiLyA34+qfmWgtUtCMrL0T7CNipwZHJsBX5ku5K56KeVpYn8Vt5ISllEg2oyxe7mTchJaDn+vImXUN+aO4WcZCLSas6y5I5K8GjSU6hFOeowrfeSG267q4L4lgwCJGQvnUr0osoE0RD2zI02B62FnW2pDVO+427ZhbDUddTSOOxcbPNMo1c2P4bXjLlhW/TGl0rs3QdPj3t/7JxRznfhwd3c1uf0zLJHHnTKexDl5gq/CEUho4IjqrlhhANWDzY9HSq/3GuTd4/qBDSLarUbEpM/X3IOLyr3qpe40p304/qUieoREQ4Fl1wTs8W3iuRQUesw1ci13pZi97FlNJDFS8HYu7Q/HkJ2s7fKUkWSI9N6FE+2ttwKrhTcnY1PuVax8lanBnFGveiuWAOTQKQCK2Q2N8lCUB2uLuDQclVjLGEKpsrV+nK3dH+XWzQERxttM1Q5J3rGLYmRUrwQmgvp3DZG2QC68ksinPZStK1D1bVETEW3MnuOdeq6yYlwVOLy2Fnl4JDrbey4U0wn6trdSj0yrV0qx2N0zcFnVHNw4nzNfYW+nHMOGAPM8WxNFivFRwV+5duC46bJXRfXxeW2MU4mjm9S2oHTi8u0qDNeI3HZoJWrVTdQjemcOibQGfaDUBb2O9BJZRf+oqo0t7uEIYUcxvbq4XV2W2ZRbicx6fTxkou35AqR73wiaBedL3flOmUETHI4U96eW0s8XDrGsS1tPRh0eL2cY8lbJ4F+Stdlcsw8tXUwfLCwpXJX7ms83/aHshrKQWAzXUBSdn1pdlIvKKGwI4PxZIVojw69NLInUdLT5bVBT/vdYaVUDcDxs7a6sII6YQNhxKYknC8aq8JBbx3X7lW65gkXCJONwPfdsmn8O98ctvrx4mi2gW9zHYQ8aFG29NVq4GObjoajFuUtcFA2M5172zFYqPGC3U4gXOMci01WxteSZCRBfBoRxBAu/OpmClOy3wh786L4PA03u+KwJ3ifu+2ZPsg1acseRs/Vr+42CdqTl/aEbO2Qvt9WfYVMRXYd3S67evsop/mY3e+mU942B751lM3W5EJEP2+LVDghpJ7RApmrMbdSQpJabxGtDwZmxaJ9cE7aWtxbGY+wQ85ra95NUVtH9Lxmz0KXk/lGWK+bTX4685tLmFKMhih0Xop6HOGkuL6dnKtEbG9EdnF9mSvMwRmlOo6vGdz5J7W7HxrUafG9HYDx97Jc7itf4JKVlI/HhpxEa803HZ+M25tu8vVSxbql31NnMqBS+az58oWy1mFdMAm5ra+HXlfWrRSY4okT2d1KSM2bvUYUnT0UsFn4jcXXxxMXlmzD81G8c83oSKPhCWJPPMso1fHMtZzeWNM2KbsxyC8rmrxpXR8wlXOV1wLStao7AqwXt1bO55wpxGNAerqk6jC502pVP0a4VKGmAwXnnK2T8ubkZwsPpuas1g6+4WKX5bLEMjCzaDTUAQ0Yf3EzxNjkUzzEBQXhgSFqR66iHR47F4qKOpF7MDxth+Slak6RvM2Qu5DR62N0FmKTDusuyW5bKGoJkDoHy8rz625/ZBu7qbxt6VxPQrw59rGXpCf96gn2MQ9GUkDXyeEO5TaJXM/LpWTuSkgZYliv2S3CXndHxHLH1THW2xvrG+5lfz9dY/Z+k6dcL8XxpCS6QMjKEkUzzHUrH40Uro5woco25coXjTE/rNZb0Cye9ZMr7YZs58WX2pDOAmvtqO32bNonAy+hdZQedXHl58fh6p2wCaMGU9rDqU3vtuZRW21Shj7i7XpwubYvvFxgS6HZqF6zVm5B4/oHcZpoKDJWFqOKA6RiS53oPTe6mMJJrl2pF91OR/dLaxNY+S0b5UtWiOg+ik9iOewDwyYDB7Yrk3Qpsm5HJjsd1ruBFG8V6M3ucL1mKVUxe75mOTFXcVRztb194rw6vWpTJ2Or/Z5d1vU6nkpVuU9nfmv3sWmwnSlsC0xS4bCTblF7SPdmv6oMzIVIdZO5gmlLMXKVJE/RS48fquLWH4OblJYn7WZhIoAnLr3aTYvYsOx5nYuKDteKtOWwhshgwtminIM53GKJLEosRNYIfbtBmIUKSktkCCftxt3KlVyUzGFzXTi9pnFw3eXj0mgdUkPE1aq97PZp2smojVobLz8uiSlmrEBNAO4Erp7tWDY93PcOKTubVAqjiNFR3jlXbSyTe9dgS7MdnZMj5CBrlM6ODM3zlQ4Vqj2+Egqfrw5rOWDSu9Rsq+wIJ0tEFdA9NvBHBFM0RsHrFZ/o7J2oR/vYDPCpOQynmOS18Hbi6gk7oV5dH+WGOnMamEuuRepl1mqsL6FniyKWUPpyRR62zW1Edl18ntIYAR1xcnbaiFpDS2m4xzDKVVy72mzaTWHZtHWDTW8E874nQIk2rjcbDd1yWdpuV60XikqdgB68HfHkCEkrxzJxn1W9jTfQxqUguWuW1QqAmXZZZv6JMcVk2+zPbVzB+V7ptk2YnJf7i8nY1rVWD5hFEYYabpNduE9ZdkvtcZwYxV4yOQSxq0tl0Uqdsy1mT8wJCqVEoojI4FmVwBvrWq0020Lvp2JzbS4KxjRtN1Qrbi1zNezrpg8SGe8GVFpOMirX2BYCVroFmd5t9hIFqn61oRHyeCdOXifts2EYl+eS0PyAVy+HC7VUwkyaSAc9emUisZtr7V1ON/LSGZbPjlxSQVu9V6irJaXZDrSKx3UQaYXcOaZMwbzpgrp3s9uqy+9gyqqX2C7rELkuR2FzvcGtXqzs3clD98mA+ztOQA1bysXiLCDhbnlT9fuFjkoe98rGutCXNmtWSAV3no/pfZJge/PGNMuVg2w8s/Q2y6QviEnBnKE8o0V32gmBB60UjaOnm8yjzN6xZJgNCK4jr71sZMOOwAYJywm+nAaN4m4yha46dXOx2ybpFcPYu/Ryz9RHBpNy0uPJrmh8kWdQqzkP+6mVBFv0gwy/wHm7hr1yXfth6cFrtD93CHml5XOm7mtJ8k+OjKzp22o7FEZiRw7u8SoHebyXYnhiqtC5t9QeKm8sYqq0G2OwGeETERxjvi8J7NzJZNeeES42TM+Utrx4kqQVYltSe2giDZYBKgYi492QW4etTKS3IqlbIQoFVb7WYeV9GpuTkE0kASmZFyKrxHAOVUlJ4XGkdzsBgwSWCSCojSIId6B6h6XZahKhoYpoN1zBI7ns99R4P59kpXZXoPrXa8ou9gV07b28LDZ3leuvYkgU7IEU6A11V3dESe3MVbsXkGsa9c4hlnayI4B4RRg490mhCW3N7im/IGNnaLcjjqtqwnisn9qg3/cvgyz49/shNTjqFl9KCFQ5vKvQ/NKvAozfrCpJ2O9BRC+Hvoe8vQYSlJ8CYEAChVFj60TxXbfl8ri8Q9sWP0XBDoNsyIsOR5smSdxVamNHSjrsilf3QJd70BMiDs0kKWOE7fYe5xqb9sYKRpe0bwVoUBAbY6tLnosh621fG4QDmkE3c8kou7v8kfLu+sqhwlLkfJVSGLEZJI9aK9rtvHSy6DA4J/xiJFEI73wc1tvdutyITsHj8mWUqSrYOAKyVdgpWWa8QpF4lU427GBtYDCGNmpJt7oR5nJ15Rk2j7oWlzlq3dB1u9viAXFn8RDbH7tTICxd+cKEx+HuyOLmDpFDzkDlNh2PMdJQsKfT+bhukeWQIBcrmKbcEUkxgU8na3eBqqtqXT3VO0sNQTCUEQuUv5SFZjgnFQl8IskagqtHX+EneRqOdkqeNateyptEcqXtiugsZcNASeHbaR9TZ7nJhiZpET9brYpAyc84TzKOMPmcdT7FUXSwjFZCGAKM5fqZops8871aHekbgdn2JSybAq1W+N0tp9O2y4c671OET2pRGPRpA58KCd4PK/EiD6yT7IVTHR+EpS+szizUX6B6r1ytFXe+3AJMleuk5vGsjJoyTVXqNp1a1j2DflVa345Lu9Mgc6q7bAoDoyPxBqP7/aXAHAoPpJ64U4wal07vKTevQ7whM1Z4ZcgncnR75ihiBx3pzhSj7yTsgB5RD9Z4Rl9VbDQEbFEEy+yO+xRT68mK9Cg9w29Vy55pxHeZWiDpsCcR0IdytbJH7pUFa5vwevAi7Uo7Bk2TF3qvENYhXxKBuol2+SrjhHqSEzLOjkMj+hfvct1puQW5Vy9Yoo4JYRkRa+pNctfqaPgXXsghfhNzeDj5LXLc4jhzXScIAtUjV/qlT4Ywl2s9o1jBmXf6PFgeNY3eRw4l3i11PzndXKwGF3jBdnbZ2RJdrFqbOY1AINzuFIHLU8CqcWTeCB7zuWNfBUfRO+HbgKwN2AnvwODrCePL0/qyhJa+b9BGo3XaiaJuMrJDmTwwLpDGXPZHv1bs5GBaCXFKGRMzusLY9944wY0LYOuknu77AjSGK3UIbtOOZ0L7njdmplzv+WE5nYVNTyG54RV1COGsXp/JO1IfaQsqzthJobflZVWO6rlZKoUUBf3eE82MDOlTqovLkN03Jl3F5iCEeyzl9YS4uEcn6bBAHw2VI0I72rrBHVEIUaTCO11jqoaRaBEimzwTSBCWV+iOQhZTrSgGhlnvcJfGempPGqzl+snW98fDNg7oW1vHvtHdGag4YRVU4aW0JIH9jeYmAJiwId9btefOC3QK9HFMTxkwwo+kdQtDyW2GPgvQzmYaqju1JZPYzLoEY1IbjoUtXpKKS9yrURyXQe1DZIaeMi/jKY6I/XzE0IOdUVTggylNogs9vMdCmshEfocLwx8ZSicORb+275hYii23ESXpeDumt1MjasoaYDoTsOKmRHqD3wZ5jp2nMwpGmHEIxIiLTNxu6Y64I5iLn+AtnYk+bB8Z+7LcaMfBVsUCCTQMJmjqjNkGIdV1cyC8gVUhzwwPzJSNzJLS7rzF5LTSH1C2LKJNSSWESK/gFI4CNCUJfR/jddXYeFYXEKGsAgaSVLZpKGg9BTVlNIIb3NRhh9VS2Ac93qVMbpKTdD8xCmgTMmfEtSVkDxtmC1ABPTMTca0yMJ9ju2EsIGmEaYLc1CtvZCQu1ljMrwv/3MX7cb2uyHJL5woDulaRGak6Ly4nPW4JX5uwuRuPG8eAr06tNglkbkhd27gXf1wSDlZorIct7/nNw8NmeYqY/GAVpeyRBBCg4odIP6wI06t5uJO95uAPcVetCBHXPIyrk30uuVywto/0gXcsZBqgC1Xg/IHFtuKll+CJIBNpqq7ZejwZeUEbUyYGE1IJhzbTs6N38MSlmlA0R6CXUjy1x5hl3+aT1C+ne2//xstq81nP/7Mjp+fp0Jc3Th4Hl6EbfHzw+vjvCPW3d2+NnwKRnkdrbdbHr2OovztYe/+vDyXn/ePzHbAv597Ps/TOjecXpN/SIujbrhk/t2X2eOcE7PD6dn6jsp1fuvXB9/enr19ZzkYvm9B32+5zV35+nco+3knKwyB1u/B1Gb/OGsHe10tPnzGS+Bw21azp652F2QEf4A/Y2x//B6nNIovnLgAA -->
