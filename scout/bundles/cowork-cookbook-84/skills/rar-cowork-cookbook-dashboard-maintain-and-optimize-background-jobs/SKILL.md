---
name: "rar-cowork-cookbook-dashboard-maintain-and-optimize-background-jobs"
description: "Pulls background job data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs", "rar_sha256": "a42787cfcc409f67996d231be83d8166fa822aaefe683d773bf9c7298019444b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `dashboard_maintain_and_optimize_background_jobs_agent.py` and in the RCI capsule.

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

Maintain and optimize background jobs Interactive HTML Dashboard — Pulls background job data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs
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
      "description": "Fiscal period to pull; defaults to the most recent available.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-maintain-and-optimize-background-jobs-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_and_optimize_background_jobs_agent.py` and embedded as the fenced Python below (sha256 a42787cfcc409f67…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_and_optimize_background_jobs_agent.py` first:

```bash
python3 dashboard_maintain_and_optimize_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_maintain_and_optimize_background_jobs_agent.py   # or on stdin
python3 dashboard_maintain_and_optimize_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and optimize background jobs Interactive HTML Dashboard — Pulls background job data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs',
    "version": '3.0.3',
    "display_name": 'Maintain and optimize background jobs Interactive HTML Dashboard',
    "description": 'Pulls background job data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-maintain-and-optimize-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87e2a2b5d76a7772',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/maintain-and-optimize-background-jobs'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-maintain-and-optimize-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-maintain-and-optimize-background-jobs-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of maintain and optimize background jobs with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull maintain and optimize background jobs data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-maintain-and-optimize-background-jobs-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing maintain and optimize background jobs.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls background job data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl', 'example_request': 'Build an interactive HTML dashboard of background job maintenance for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-maintain-and-optimize-background-jobs-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable dashboard of D365 background job maintenance/optimization data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMaintainAndOptimizeBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMaintainAndOptimizeBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-maintain-and-optimize-background-jobs-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardMaintainAndOptimizeBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZOj1pbnV9FkR4ztVlWCQICoFy9ikBAgEItAEgLXizL7vu/y+LvPRcqssv3qdbd75q9RVaYkuPfs53fOycuvL1bXhkX98ulF86x8wVppGoVevbByd7ErhqJOwFuR2OBn4RR5W0d21xZ18/LhxfUap47KNipysF3p0rRZ2JaTBHXRgd1xYS9cq7UWfl1kC3rKrSxymgWKYwvmf2o7ceEXgM0iiHovX6ReYKULL2+jdnrw9qPGAVdKr44K98OiDcGioY5arwF7mhYssdIi9xZR3nq15bSAyoI7i0fAsgntwqrdxY/alV04oVW3zYdFU9StZafe4vH7w0KlWLDXjRwLaPPToi1mFouia8uuBZKlrlf/bVF7lvuxyFOgrDdaWZl6zcunn//x4SUCn18+/fripFYDLr3Q70xFCwgEfqjclYFlsujubb+ahC/s2W6plQdgTzkBw+fgO9ARmCIDl1zPX7x9+7HxUv/D4t//PRmsOmh++vQ5X7y9Pr/M/9Quf4jcFlbTeu7CsUrLjlJgv9cFlQ7W1ADx267Onwarozx4fe78RqkoF3+f7/34ZPIaeO2Pn18KIII1e/Xzy08L4KPPL3U3f36dqZQ//vSaFoNX//jTNzpNZ8ee087EgNSvX96+v5EFC78tjfzFF03Z79541Z4TlR4g/jv95tdT9Ddybyb58lz8Y1F+WHyf8qzP34G8z8i0Ad3vkwU2ADtfXuMiyn9841EXIA6t3PF+/OlfkXVCz0nSqGn/S3R/fhIOQQwBa72Z5KcPD/f9Y7F80+0rzX/NtgQB81c0Acvf2X011L+i/fDsn0inUQ6y7N2X3yX3vQ3Lvy9+/pe6/UcbPiz8zy+0l4IUrufk/LT49REiP//gfrv4wz9+A6T/UzJa0dXOg8KXzMoj32vaL19+/qF5XP7hHz//0JUgij0r+9LV6fdofs+uDz5/sODbqh//uBfwv+RJXgz54msOLX4tyv9R//a6uFpp5H673nxa/D4T59dyMSvxzvRpgt9lYwNk/Z0df3r5DeBQDrTpnMdtgB//9m8LMXLqoin8dqE5AM0WwMEAhrxZ+HMYNQvwf0aN2gN2baIZEJ/rQPzPHp4lLvzFL//LeWD/R+cN+6GvsArs+oS4LwCDvxRvIPflG/B/AcDf/PK6OM94WkdBlAMcVylF+ZxbAUD4WYSy9hqv7gFs2VPrfQTZ/XH+ABB58ctf5PTlQfS1nH551I3oiYrq7jAjYtOl3uusuz7Xj6emDihz3ug5HeCXFnOR8SMA7B+ATZoiBWWkne3UJFGaLtwIYA4oEM+aBGz5aSb2yy+/2EDIz/kTwtHFsw42EFjwVZzFx49ASz+NgrD9nHtOWCx++PW3Hxb/e/Ef7XoQn3kooLC8eQpIyGuytACZ12VgGXAicDuAlYenfv3tzdaATA4KN/Br5EfeczOI3MRz3w2vcdRHBMMXtgcMDoydlaAogrqwiNrXxcFffJUXMJ1vzZUjLJp24Xqll7te7kyAqgXU+WrJvGgXDQjPxp8+LLrGe3D9xa6th4gZgACr/WUh7hRQp4p0LrP1W90Cm4sclN/0a1g8rwMi9Q/NYvtO4nUhzbG6KK3aKsPaeuPhW0+/zD3E23ZA3Frk3vA5n8uzN5vqkThP84BFwDLOm0s/zj4HDU0GUMJt3nk/1lhzNT0/qmr9OW/eksKqZ1c4oEgApkEXuXOp+NtbSDVh0aXuw35A0pnSmxfcN688YvC9N3jE0ns4/6ljahaHPzc0X3uLxecOgVfrxf/PndZsJ4pl1T1Lnff0Yi+dVePpv7n5nP387Fdn4WetHrn6rfV5h7d3lP+cpxEIxnr623Plw+tva57I2dXASSqlPugD5wD/zXQfGTFHeF3PuWR9zt/LyQdglQd2gqAA8AHSa1bpneF8913SENhn/v6ttXhEELAXsCmI+kXZ2SmISN/z3NmbQKrZDO9uzmejgwwfwsgJ/6DV7D0QhYD+AggRgTwFJef1K8Q/776L/oeNzw5q3vLoLkHwePWDAJDDmwWcA2KIWoBtVvvs9YGenx5EgBpZ2c662yCtsg9vF73aq7qomePlw5tdvRKg+cf5/anpfNUbS5BJwFhPx78+M2wGnwz0R0AGADIgvrIoB/0CMMqbER4ErWyGCwDHbw3tk+Lj8ptC3iMt50L3vnFWZN7ziMRHXlj59HtUOX8vTAC9ueg8rfbnSPvKbaY9I2sD0BFwfL/7bDJen33CsxFZvNP99E/D1I9/bd56VP7LHwPg0yJs27L5BEHPav1erF8BrkFPWZtvhfvjezn9CHh9fMefj99w5OOMP39g87TAp8VfE/UPJN5S5dNi9Qq/wvOt41uovb2AZXYft8bH9Xz3c65630AYsC8yEGuzHyfQKXytmO9LQNkMaoBnYPGzgjZz4R0Agj1KBnDK5/z3sT/nHoCpPPAeOPU7THi0DiAPnj78WtnArbwFvN25DQ2813l6m8VvvJdPOYDhDy8Aa72/OgDOpSybo72ZZ0iQVwB728h7fHuAx9jOH/84X8uPD1b6uqA9wCBtfh+RbwVoLsC/S5ynxkBTB3D4MJcIgAcgWIHGM/M56awGRDEI4FmzdipnVZ6z4txdPivDl2dl+GeJmN8XjhkES2CRv4E89q0uBbZ8Q/ps7iCAKA/w7oHkc0p+l9+jNH15lqZ/ZkfP9ewP1QswqDqQ+B8W3mvwurhoIvNdul9b6H8mqoP+ZKbjFp/mUv3hDeXAOxh7Piy+TjDAem8z5czByzswrv88T0+zOx9b5g9gD3j7uunr30hs7+Uf35PrAYVf5gB8htGfpZNmiAMlYDbjo+Q+YhWI+6jPb2r/xQT/iMAI/hHGPiLr17DN0u9b7E2yR3X+jiu8Gbqf881zzVcQ/Ja93wT+kS6cZ+cKPXEDetKHfvoOc8D9UVFAXZ5N/M133yxYPIbRWU5g8fb5t5NfX0BGWXMX9JZTb9MMWA4A+GMz92kQwCDAEHx/ogW4938757yRa0ILNNaAnrVGiA3h+I6zhkkfJ0gSdxF0ZXsb1N2scNy3NghiWaBPxMEVgkBtn3QIhNzAK3K9XtuA3hOCvsy9aTSLiJGED5Mk4q9XCOyC7ELWrrvBN7iDEQhskbaF2Rhp/W5rAtqtN72fes5G/TpyzfZ5U//XFxtfg5XcujlQz9cOIlc2jh7t6cgt77hnBCuNMffCLo49QkluXElaui16ZWshWs/31iUNhh018vqOYqNhn4hTecU0bgq5TNugN2W9L09Jt2qOXTcdVcHAvbzESYc8bNxxW0GkIObjGQp5gdEsleyLenVoIG8LwivZ3e94UapWn6Rj5pdbLl0dNxsXrYmNNtZ394jpXrgUfR+KMDmKYz2/JBHJSX5NCyvG8YhRItlANX3fl1eewtUNrtyM6jKtjWaF7y5RmjUQEx/5Ar1ztjBEnLflhVo6hKqs2ne6EIp2qs4Mh41xNE6VeujKibmaTuxgS2+X7WITSr1IgKech9hLv4VgaI+78i3btmxgLmt7N07qpTlcPbVMDPku82fTwBhewaaK367FvMY2nl9vMFdC72uI2dz9/pyT8HhuRHpU9TN6DBkoZU3nhBNa7qtMsfe7oi+wyFurvXpMBTdYbpH93j/eRRKJNyh1PWkZsaVE4SBsJvZ0gBLcVKRTJE6GjVnYOjWkIU0uSehw+hkXrisl2e/r7JIZ6wsmRLvd5s66TZ3iLMpjgzUVHlmW0RZWhiRpw6CYqHri5C3WGFN8EqaE3mfq+pAkg1xKmhRWPEiBi70tCcOD0w45tAFFX4y1f10nBHucYtRMUd5ZttY1wLToKiUKUx0yahI7pTT2e81CTux1xS5ZP8Ty5HY8NA6LwQMNsdA5py2SZNl2D7UnsxfyQ8sn/Fasz1gqp0RTQt6phRMFE83rlo72pnmRz1PrYqlwZ1bBkudGRkCkE6JFhw2dx+hZvPunTlpyB+mO72I1WFYlahT7073ZhpGqHHqsVPjGldesT4jand4VzGnVxqcUqSkBbmmPSjvUvNYXLVlPEQazQtwwNXatmmg3qclxczL98ZSu7GR9SZ2q21CKa3N7BY04cquM+35k2CHyBM7iEikb1oyejTiN+dc+dgiO36zOiknIFD+YSB52BeEMQ5V5VxnGUakpxcbV4Jg+nuVsKwpOAV/vLJGvW8UgVH641cxNucu+Ry0Hvu9rNjcVjBZg/2zGpOKvl7fgKqxTX4RzeENrVtCfD/2tHbkDaFS2jGVhOabSyg3f3MfdII6JfzgRfUk3+Ha1ii4pzRRsXGHsjleb0nCisPLOJGhE7l4VEHASORUzVk0ykodwnVZImBTuCATFsMuSQPMosgMP3hkgCsdA3GCOzIMUT6XMXBuuPCp3rmBu6w4ddFzOLCvL9dj1KrVRCC5K7Xq0pJEozSwudSvRJmsTrHBIwBA2gckYDFRX/IaVulDXmiYtu+WllSVZ12MvP9sxJC3FHutsSM84eDmKBXPn6NxSr3dqu5JHbmta7Olan9E9fKIg3Ez4yj+VtXzpwxwr1hUt9sx9K7bxGj/pR2Pq6UphyNh0kcjdVoMh6gqfpcP6ltKscLKwW2uxS0lWb7kyXpb8Be7j6dxzBJPok7q+BETA8iRPOHmS1Na6EoYkvQShZmz3p83StTeJbSatr66Z8eI4MmRe1pUv+AJJ2AD1mL093P1hSQd8m1knuyNjUeeUZOzumbMKj3YQ2nkGG9N9WRpBqGcXNCwcitP88GRnTRNFiSKkyF6vb8ebHB85it72nNQap/Cab5TRvTYhDzm4SOLH006oU1RUSMe6+m4wFSaiqeP5PKQ97eXMWRhJaWwsE8vH+O4huXt3+NwsY2+lFmF8lRhnpOm9DidXxDrmvbs/rErGvxW7PKKZBBE4TA/33jndT/R6tbNXe+u4c4tJGYm9t1Ud9XDALYORWU4JKKXQOPW0l+LgzlymvY0u2wuxWm7ZHeElNB5mI32+MLEqdXHENzyTyeEquIps3evXdpfIh8NS3ePm0dEQjQk1+GTp95t/Go/nDW9k4eU0TlekX7GXDcdDVyLT8WmbpYKwxQtHWlnL0auZJNWb/UDoUmjLcZrkYloz1r0Jdma7JOW8XmLdgIUWI5ZBTajHO6YI5f4AOVCVqC05xXC2U9PimmBojwT7U9uzuX2KYzW5KBCh0QTMTThEhyS5vpM4KUdhqzXEZGWRtIE22VFkDu5224YndRDho0Ja2jpDYD25bveaJN97jwZwsbr6dhlYHeYdZCeMfRvgKYAHLqdvh1Khs8i4XoJ8Ek7nKTtlqxEMK8qR2Z6wklbP5Tot68pMszSAx5Rn5Xi4REkbqMzKz11UKUavsc4HtIaHfkCTPHFzdKmt0xbpkm4q2JLDl8XVJ2kOm1KKSWmHq6IhHMxLJOzw7bFVV9M95OmJJXgqTjA/2ydXp95AXHmQ96K5vIgjl/Iavs1FIzeHbl12fHfQ9yEzkldpw6xhpqIm6X7SnCJerW0GK7gSxSpigIkrOXInJUkHKbdvwApmTAzHHTXJPAOqxYZtKO98odfVhWZMjtKo6pC203DqjZ2wH0pTbzDJam5+tUZ8akOnpqma6vLkHAStDw6w4wcwdbziPLJbagarlKcrLCAaLhkRXTfEcDhM14w3JiuyRWpzIsZxpSFtKEBIFRnUCPhTraGF93wnx7fUT7VlnISjdmWs1ELQs7y9B/QGR5KSjQ43m526enlmRHm1UvfKVcj8i97zlb47Fy4tGvR+C99zSRL0TIgDa7N398jWNy73Zaxe0GJKths6ss+jXlyZo7QsIOpmYpDYnFY3Jj0MER7kdyG1GCe6bMCYRWmZlOxybUeP8qhq6zgY65uxTBT6xpRbsdCWNQc15XSgvCtni4UB6i+HVzavSmeGFavenshLx7fe/RpTeZh5mY4Q6yobMk3cd/bh0hNKf2F1FL5heqzyp02DyXm4dGXEWjdoIPKmJ+5XZ991TWodriZ8LbH2VS0iVDD4I78WEvbURQCU193uGvNHnQRIwVyoVRVsT1dF2Aad3dNtcKxinYUK88KCdgEZ9XDdTC2thSBVVMRzydCk/MtuQJbmndhNyYbeBzcjNEyaJ4rWSI3jPcnYhlTOa41npQCXNZhb1Q57FLbWNnLxW4bKZBZVq0AbtsZF0xlTlDRU4pbJ2FKeUt2uEsXUtK8qCAT5nBBFiCkHCOhiRYnPyJJw+z2aOYFpH9eq2HVGcYAwaUPJh0JwzSNtZ5dl697VgvXEIb7JwikpBBXpjeshYTQh3nJaxxFRlrulg0f+8trZp2E4FTKywYzaiFer0Va2aQPv9zGjB8OeEqq+vJV5sXWDnoKNU2V2Ayc2NLveTxabLpd9SyXM0rYZ0fIEYywH1Ze0MhEQVbsuWVFgzjgVTtgRwVFN1lA2dpmjuDd2plE6Htls1OBsVmnByJdw0MoAQDbmbnzUxEeXDaPRiVEV8L1kPc4EFOZFvJ14GFkct8dw3Q6npai3CnfH1ksRhQfXP4cEiUpQgtgVKpXn6n60UnfaVavtbUw1QsdWu0miy1xAhKt4s4vJcr0L5JiyXlygDGaubQrhjrOflgdsKk78JsYvitSfMq3QW/Z0NjfxCYTsjXLCnBdGEErpumWNtbKpRHHXlUi2H9uB6s2djTJ0cKrI9dkuE0va5cy22dCC3BzuS2hAuxQ3zUPG6CuxkREtPrIHyWcNqtek5JjVuQrlaK8Z/L7KdatYYVBZE6MOQwfHMxoFci+4nimIzaD9+XTtu3ptQZfDkBzx5oBmyG51PS0h+KizfOxmq6PCT6Jq0baFtzCYUYtOjVf8zZZiofbVa5xWjLSBKQZT9cw92VVi3w9nPxx8B8mNWN3nEu8HlHSoSU3fRSy3zkBldUK/sA4Vf9iR5z0fuYFlICU1rQxXuSpctjG8gNns8KO/LThaVKdpFOpDufL4sFt6nC+T/hSXMnm7UHtHvB703W4rMdU4OEy767qISHfmut1kmyo5i1m2SXyZIsC0cVsfYKFeyaXt2NHhjBwY1aB5iTuRSDLKu8uEQvzhjKH5OLZLhqBwhky0nYDtA02R24uTqmV4RwiBlIGPd4bhHiQxaMDwGbO83DldtsGq+nqc+N3GAS0AS44nExP7fJQ7cph7LF2WbyPbn5Xu3vCoEaept5xgU0pZK7kpQ0UKtyvJZmkl+vcLp/T+kJ95oVgfdjbcyzeKllUtDImD7vkx0txS6cKWhdXrpUmjEIioTlgqO1jnistJuKocCCqcNFy+3J3kmA9DNzprqrCNbiIQ7CpXHC/BYwJaLHFyYXXpI6NKFYUud3utS5Qpghilux5s3b+0pLahpel6vBn0dSRP0N734Zq9B6vTitkO6pb1PZy93Txco3Ydb3scyZRHzo8lmwLd9nTNUQq7R/FhlFPxpmfmWUuNTIu9lt4gyUZi5aOyk0BfGeNocEZVs8zWEa3vh6MhnsDsdILVeo2K/FLN8zvb23YgHsPN1jHWN32EKOqCixxea5iEuSD5bHPM72U4rKSL2p4LkUF4PIwGZW9uskLtaz2BqvGM8GOMVCwWIAK+X9+DwMyLJMErwjhAgXpDErhLz93tfkDafmkdT0RWIfLaRzCOWoNokDt9g2ibOkL0zNb8FsZMHfZ25hK9TTgurvq84hE+vvmudx2XcHk5oOfKqlrsfF7zcj5ea5TPm3janY5HxcnFYRWREckq0p0hrim0OcE3KTx26K1T7lBHTndLMHTowKGrvbDB6Ry5QPA0sBt1J1nOOYNT8licdtYkVMdA21u35lRW4THq0JyMIFyXhhpXSFL2KZ1sKgtCfDm8wrKdl5uJx4gQnRDglzWOT1J2dlfDLhl8WkX0kZNG3kTEbaHYAhiJUAiMx3i0PpTnTXS8kzYU2ZO0BKGTIKRzu6I4sirg9bmv8IRuK7YYHHm007SRgyTGjcvQL0vpUDh00dpLYnfgRtrSJBoVb8P+EoGyc8DubZD6lhU7emu19OGOoU0ltb5wl9othuxr0UxwRCaOTosFcSp2om57Dh3CUEkVjr6ykBJ1+mMQUnAaXxkCwtDz7XbOU14ktGjs11SyJKwzn1BQEWqedN3m8QCm2H5ZqT27RLJpmTRYuhphm8rPsJYWKMrDfqlemsi/3smMxXEfTvTzXjvRl+ikcDkRx8duEpeibQBQQ1zTioldYbJXs9FdvatN69YNx5Ux1FedBu1ubYuaYi/vbA1t7aPMngMVsRGUyQ7our6nmrKXbvZeqw4TXPIGTWGigjM0WtMH0LzCMcvgsAHXdZAXel2p3a2mVjxjy6wm18BvXGIWe4Ks7W1ArK12VEOBa2vRl7mGmpwCOxhhqZ1RTIO4AHiHq7vOojEVQHkI3TVG1DtMEvdbxCvCqz0PUp2JeEwIn40bZt/LS3bpiLUkywrqedtcg8e1PsknpsJlzDmK6sqQL47E3MWYO+kRbqrX3AvJYtsxzW6DgKHjljIWwfd1sUPOOGltDFU2Ls3JvN0MFtk2a4/2u53Q1YPS0KsNsU9v0uW2qbMTkWKlzeEOhYqyuSoLqGwqsz7JLFY1q+lYxmvNhjt1WNExxcc0fMuPsNDdFN30thFVOV4skPY0GquAWloKcbrc+Gp3mLgA6hxeJS/2Sjj1ucokqyzUe4OCJ6JPOjb2SMlabdQ89c9Z7+F2ubrd+uLK+c1wh7zcjVPQyfKXUbzXvdmvfeClXKtYI7/3q/CuK5mdrFqTcM+tiHLwCiExUFk0pNz1G1eqc7dLR/tC3nHPQja8XyWZKNQUo6S2iY7bHu24rrViMrpyu9bxDRe+Ms0dZGLJMWWfKxKk7WShgnSfq7TjyBwySxVUyTqXXE17sR+nhRRcZfMsLnuPWXEbbLnfCcj2fAkRYC9TLTk4Nc6bg7n05OJyGKFgq+FCfI+GLR2q9zIJLJNdIUa6yq7An+j6ENC4s5yQY3TeXDMMP1vqTYcvaGtvxVhSEZOg0pg1fUK9NVfvTkL26WzQmdG5DsrvD5UJguuK0NyywsjmbEA3FUyp6fGIqcub0tdcLxIFAtebTSfChXxt6wuR3vCI0C+B6W6svWtyh4slrO6uhKwOpYGmdanDtoB0bj+puqAhdOthYaYphNPGol7IFh+LHjnBIi0TcHa24xUtL+l9n3mFb10U0zeX/oo6i6DWmiLdgMajN1uKhBpKjlvGaFLoluwqgU4PWrK+T+o6ldR9GRiqkzY3vTROebMnQuzOwrfkvmmja62TKyK4wvgy8wROEY8+Ip1le32NYKW7eT0r0qwP42bqIiApD/dxW1JeRN6HnSfSoOthOb/3l7dN5qwRnPcxfFsnkhU57RqjQGa7N6G8C5xPOBGoMzY+XChLOeJ12iUu0U5Yee+UrnDDm8s7ZFwl6IRabKi2bFgNan5attUG5D+hkG0Eqo4IK2ferrla25ANYi6HdKliR2OI1VMm3k2crlF7iZUOiiLbo4NzB6VLzvTh6Dvxnsp1WdN2WMThxEmgTgSYWSCblzo0G7dDEV8PS6Pj45LC/DWRh7XcIv2JI/dyWLRhVHGNnm/dC3HtoynqS2QN9OmORHhlPPd+6gR3GfWurkTHFFoOLp5U0g4SPRqpjd7bniD27jf7M91iKwFtk6LbR5VcWRrSXf0CYm9nNBhJzvDBDN3arNyswPxUbbhuaPBSJ2K9vUtnn+mZ+2Z115qjit9P8oD2ZEYbvmmIyyUpXpAbGPI3uYZBMpb1QbsdqZKs0uhUUNylzjdmGVQZJdDjVTUpu5oaXLFD9OJ6ogsa2kncjijVYzY1x9OBZbaoo0yJT/GcREgj0JTqkEq5oVjYqkSE+6QH6dRGUJwTSq4HAvV4Lyu88xQhF7o11/2tMVEw7BOjEjK1C0pEZbiBAWPudmiu0A3dQRCU+ftyYDEKccdlu2pxsY9RokYUoYGh4gZKmu94YUSYzq5Y5WN045zNkiPdfXdxV4lIUdTf//4yn8m+Hxa+/HcflJsPiv6fnVc9j5beH3B5HIp6lvvpwevTf1vCf3x4qZ0IyPc8sWvSLng70PrTed3Hv3j6ORObnk+mvR+0P8/xWyuYn+1+iQDwN209fWmK9PHwC9hhd838BGgzPyTsgPffn/l+5Q8+W+7z8RWv/tIWX54nl97L/JTm/GSL50bfvgZvh5qAwNvjWl9QHPvi1eWs+9tDE0Bl9BV+RV9++z9kCi7Ppy8AAA== -->
