---
name: "rar-cowork-cookbook-report-route-loads"
description: "Builds a read-only route loads summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_route_loads", "rar_sha256": "c7ea746278b74a2953305416988ba976e27da6b0eec9de771f1d42bf32ab3bd9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_route_loads`. The original RAPP
agent is preserved byte-for-byte in `report_route_loads_agent.py` and in the RCI capsule.

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

Route loads Summary Report — Builds a read-only route loads summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-route-loads
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
      "description": "Name of the Excel workbook to produce, e.g. report-route-loads-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_route_loads_agent.py` and embedded as the fenced Python below (sha256 c7ea746278b74a29…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_route_loads_agent.py` first:

```bash
python3 report_route_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_route_loads_agent.py   # or on stdin
python3 report_route_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Route loads Summary Report — Builds a read-only route loads summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-route-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_route_loads',
    "version": '3.0.3',
    "display_name": 'Route loads Summary Report',
    "description": 'Builds a read-only route loads summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-route-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-route-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '61c05dfc125819bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/route-loads'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-route-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-route-loads-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where route loads stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of route loads for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-route-loads-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads route loads records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only route loads summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a route loads summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-route-loads-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a route loads summary report with totals, dimension breakdowns, and a top-10-by-value list exported to Excel from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportRouteLoads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRouteLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-route-loads-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportRouteLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adOjVrLmX9G8N2JsX6peQOzV0REjsQkEQixawNVRZl/EvknI4/8+B0lVZbfdPfdGzJdRlS0B5+SeT2bW4dc3d+iTqn379GaGbrkQ3TxPk7BduGWwYKtr1V7AV3XxwH8Lvyr7NvWGvmq7tw9vQdj5bVr3aVWC7eshzYNu4S7a0A0+VmU+Ldpq6MNFXrngfjcUhduCe2Fdtf0iaqtiwU2lW6R+t8BIYiH8T5NVF1EFWC/idAzLRR7Gbr4Iyz7tp4c8ddX1IfgK27QKPgBS/dCWaRmDhwv+5of5Ypb3Ieo17ZOF+eT5YcGFvZvmHx5ErKpeoMjCmxajmw/hokvCsO/egT7hzS3qPOzePv38jw9vKfj99unXNz93O3DrzXgIbswqKbNGYEPuljF4Uk/AgiW4BoIB+QtwKwijxevqxy7Mow+L//zPy9Vt4+6nT5/Lxevz+W3+Ywzlok/CRV+5D/V8t3a9NAdKvy9W+dWdupems3E74IAyfn/u/E4J6PT3+dmPTybvcdj/+PmtAiK4s3s+v/20AIb9/NYO8+/3mUr940/veXUN2x9/+k6nG7ws9PuZGJD6/cvr+kUWLPy+NI0WX8w9z754taGf1iEg/jv95s9T9Be5l0m+PBf/WNUfFn9Nedbn70DeZ4h5gO5fkwU2ADvf3rMqLX988WgrEDxu6Yc//vSvyPpJ6F/ytOv/S3R/fhJOQFwDa71M8tOHh/v+sYBeun2j+a/Z1iBg/juagOVf2X0z1L+i/fDsP5HO0zLsvvnyL8n91Qbo74uf/6Vu/27Dh0X0+Y0Lc5C9revl4afFr48Q+fmH4PvNH/7xGyD9fyVjVkPrPyh8KdwyjcKu//Ll5x+6x+0f/vHzD0MNojh0iy9Dm/8Vzb+y64PPHyz4WvXjH/cC/ofyUlbXcvEthxa/VvX/aH97XxzdPA2+3+8+LX6fifMHWsxKfGX6NMHvsrEDsv7Ojj+9/QbQpgTaDP7jMcCP//iPhZr6bdVVUb8wfQA6C+DgPi3CWXgrSbsF+DujRhsCu3YpMOxrHYj/2cOzxFW0+OV/+Q8Q/+i/QBx+AvCXBzZ/eWDzL+8LC1Cq2jROS4C4xmq//1y6MUDemUvdhl3YjgCZvKkPP4IE/jj/WKTl4pc/E/vy2PdeT7880DZ9YpvBSjOudUMevs8anBKA7095fQDe4S30n6XCB/yjFIDwDO9dlY8AF2dtu0ua54sgBcgBqs+zHACLfJqJ/fLLL57bJZ/LJxBji2dZ6mCw4Js4i48fgSJRnsZJ/7kM/aRa/PDrbz8s/vfi3+16EJ957EEReNkbSCib2m4B8mcowDLgCuA8AA4Pe//628ucgEwJ6ijwThql4XMziL9LGHy1rblZfVwS5MILgU2BPYvZlnM5S/v3hRQtvsn7Kpoz/iegBC6CsA7LICz9CVB1gTrfLFlW/aIDQdZFoOoNXfjg+ovXug8RC5DIbv/LQmX3oNpUOfjfLOZjEdhclSkw/zfPP+8DIu0P3WL9lcT7YjdH3KJ2W7dOWvfFI3KffpnL92s7IO4uyvD6uZxLaTib6hH+T/OARcAy/sulH2efg/4C1Osy6L7yfqxx55poPWpj+7nsXqHttrMrfAD1gGk8pMEM+H97hVSXVEMePOwHJJ0pvbwQvLzyiEHjd93Jq1NYPIv84vOwRFB88f95SzMruRJFgxdXFs8t+J1l2E/jz43c7KRn7zfLMgv5SLTv3cdXhPkKtJ/LPAWR1E5/e658uOy15gleQwtUMVbGgz6IF2D8me4jnOfwbNs5EdzP5VdEB+IvHvAFPApyH+TGHJJfGc5Pv0qagASfr79X94f722A2AAjZRT14OQinKAwDz/UvQKrZaV89CWI7nNPzmqR+8getZmcAHwL6CyBECpIMoP77N5R9Pv0q+h82PpuYecujwRtARrYPAkCOcBZwds3sNCBe/+ybgZ6fHkSAGkXdz7p7ICeAps+bYRs2Q9ql/Yx/T7uGNUDbj/P3U9P5bnirQRoAY4FgrAdg3Ud6zFFTgBYFyAAQAmRLkZagZAOjvIzwIOgWc64DLH31lE+Kj9svhcJHTs215uvGWZF5z1y+n2HultPvIcH6qzAB9Ip5xYPvP0faN24z7RkWOwBtgOPXp886//4s1c9eYPGV7qc/DSY//vdml0fxPfwxAD4tkr6vu08w/CyYX+vlOwAl+Clr96qdHx8g8PEBAn+g9FTy0+K/J80fSLyy4dMCfUfekfmR8oqm1wcoz35c2x/x+SkAsfA7SAL2VQHCaXbVNKPB14r2dQkoa3ELEAgsfla4bi6MV1CLH5AO7P65/H14z+kFKkYZz+HYVb9L+0dpB6H+dNO3ygMelT3gHczNXhzOQ9UjGbrw7VM55PmHN4CO4V8PU3NBKeaw7eapCyQIwMQ+DR9XDxS49fPPPw6d2uOHm7+/8LD7fWi9ysBcBn+XAU+9gD4+4PBhEQBrdHPZAnrNzOfscTsQjiASZ/n7qZ4Ffs5dc6f2gPAvTwj/s0DcjPt/QHkAaM0QzpAdvsfvi4OpCn9J91t7+GeiJ1C1ZzpB9WkuYB9e8AG+QUv/YfGtOwfavOalxzhbDmAU/XmeDGbzPrbMP8Ae8PVt07dB3gvf/vFXcj0w5svs9qfz/lm63YwdAFtn4/5TyQIyA77B4Icv7f+cQB+XyJL8iBAfl/j7Le9uf2mbZ3n8M+v976vno5t5luKq/BswReQOOYjRvnqIVsydE3D+XE3+UHUX7ggiZ8a2v+ANmD8wGVS22ZbfnfTdVNVjonqImbv98x8Afn0DoeyC2HJfwfxqycFyAGEfu7lNgUGKA4bg+pmM4Nl/oVl/7egSF7SOYItPhS6Fk0uK9ijcXTIEhiEEjpIMTXsuQ5Hhkgpc0kPC0GeCkKLQCA3wpRdhS9fDvIAB9J5J/GXuvtJZCoKhIoRhlhGOLpEA2HGJBwFN0qRPUEvEZTyX8AjG9b5vvaRl8FLtqcpst29zw2yCl4a/vnkkDlZu8E5aPT8szKAekN8zZQ9qybAi9FXrHkDliMxLgHiOwjW30lyv5Btmk8YF2UsyezFPsmfXl46O8bgQ4k2xDX2ZuIyY1qQg9x1urKmAqlldlqSm10qrOVPo1FCbMsS5qTXTwlSk9DBs0+WS5Oz0rDkOcqjhscQiPD4fnXtsmauteLAshUeXVbkutpyWIdzuZHj2saY6ZKm6CZ8zDHwwaViFlMs9SHPjEHc2Dk+5fvET5KI3Tn7WCP7C2+kd1WvaFBVN6gpJOJ4Moyld6npwCIYt7KxtlcR1+uI4SJSShcdJuhC56FtyIhX0HVNupBB3ASRnF8EwG2l5qCNpE0PheK6X0XhuIXi4HUoFZSKY5BSGGOtVeu9XuiI12dY62rpMG+lgF0dWUumTast7Xxv5SmvP8tmGS1e/qR27vcPHFRrcpAHRuW3C0hLKlBwNO7C8LtWGnUBtUVDyLAnXQ2fr3Zrp4uwYmPlpHUSyKaSZJsn6MKrKqJLDGYw1xztPxjvYJxWOk1QkX7NWIZwMxSJWDnGeJl27Hdqtuy74I8TKjHpwLWV3SItr3mbBbRDLLgEBgdnicrXa3VIbbgVWpixqtKjpvs9Oua35eG45nOym22YnS4J19ZVLHmeJwzbri+AIozht281aDNQVzAx0zSNjfFdEYTxyJz+NmjwT6qNuSQjkWERIbc/YJAxFAsuWcuGvwrpOzrzWUoqwyk9+tUylOOL93BT6Ds8iHid2yL07rZRMD2S7uClc2JRO2pmchvCiLNFg8ChpnzfFwvW4fhuEgrCqT+uqQZaVZ5zi3j2sR9Hy2qE5phvdrNFg63HbzumhpmVrlg0uiu8LUeIeSH7ynaVFQ+qA8NW1k+9YLMCDtFvz9GEJMsMTsuvJ3YjVPmcOkHrvzFI5q0stu2xDUa6JqE767G5m5CWlGNlkIr8NqUQxRWKS79BeqE8rNZrsEPIjSA0I2iXvG1jdixZpj1GdQbxJbwhM6vEDvnYNRnHQ3uaWeWXcyPGaKpqJHS/JNLGMV62mYnUdC0WZOgbrNhB9a6QLhQvtBBkCbjoSujToban5BeVwQbNEV8ROQsjrgW1gk7/0m6uySzkXJa67zdouNqC75vU7be1izkua84rr4HVxTQd2L9OThkR2Z0UGdRWPfAFtsGWys7ZIk+3js7LHhRRjqjrJ1og7jZLSjNRerY7lxaTW7okQhUu7DCTFqjnKCjXm7JyXmVHrBFOWGwcS3evRyWkNv5uNzbpU4lfmreUSYzWdc3173VKHVS6d8Vr0XTRMPDvUW3V9YVe7Mqi66+lyuEvH0bjHaezcrPUewrpdcz9fpGmvr3WTvPAHqFwPg17dovh27ycit3wYtYQjp55q80YoGJd7wTFNg+WK33VScGTrhKlDeO+yG0le8wyHc1eGofDEvKPuOq20PupxZ8jGm9KR8D5LYzzfpVMqEoQe4Zx8rUxpvAoIZqucXLaScm14tTPRSg2uVOdZNnTPTwVPJfuQP5r8HisG1/Rkiz0eLb5hJMzqPIgNXRRZXtqG41d3hj7nzr3DoPKW3jMzLioca1fUPasPE5aQRu4IerwfdSHALvV5r6fnYzE4qOQFGLRfthvVu54rSauylT3gKl6nAxPh42YfQrLRTluI1IMuHEwvQFTqlMXN+soKKoMeFaPm0ntMgMCEeCHmLcEsSE6X1jd+5UmiEetlbWStLqOCx9UAJmEMAFXuJ7Yj7WDjksTNBcvVZXcRZSPdkp45pfd6QwIPx5XBt4l9LVrRSrfS1Bl0avkTaS3F0XUMadSV1bFQsAK/sWZSdm4c3fbnFBL0JaJhJjLQXoM6W7SJ16WL7wpj8netQfeX5Y0w9uUG8cLRoqnwXN+cnSpBrG1CKdsaW2m3Pzl1r90MsmXx7TRwUjYG8JFnkRPta0WZrNfjGa1gDjc9fbu5oxDdBJsIxYfsuHTMI7kb7/f7gb6c1krKemoxXn1MkQTRPHA7MGNur2a1XnYTxcv52vIcWvG5g+UR/AGnl8ttJoiKndwT9KpF+A1AArY50Nwt19Z2dUfWe0S6C1x5iH05hj1LrROvJWhCZ9PLxkDkfnu4VUNaX8YdeTgQ2bZnJ/Yob0a1i6NBx2mHPpmBiXbWOtMwNcnOtUuVwl1lDyQ6QsF6CESWHMSCu6vXIyKoZFprfN9Kd4vlnVbpL5omibxkmgwe3TCWCcyRm4g+4TcyLmE5i6w6Pi3S5AIAhAiQdCSWkoZk/G0X7KczghDNakI5ULwu1zOtstMhm0hWcPNdcI7883ZvbGteanfHSD9aosm1Oi0l584Vto2fUHxHQTx9nOK4EVO3GorJPqHOSoJMY3sQ9UumBvSeg8NEO0zyepve2raQrkGy09EuOe3P0z4XtozA50Y9cBvE3iGOna9CmU4Eha6aNNvdnLXmSRhv6OVmxaPYUEQKEtZqzvH3q2ne4i0nDIdTQytoeFbTuF6hV5Nut+TdwevmOq5HonYRgyV8UU19Fhmt+h7eOB05ESdfyOtwZw8HZHfV1rGql5Hgn49wvduhsnYxacKy7msLJa0LLfJAZ3W/KlKy5scO2+a3csW41+og+VfZXUqwbTiZtTTOUimsykPij5rR5lXd8DAvtKLMiQ29QUbYlZK9RHASgkRY7SylVWS3u+a0u9GuEJlBIo1ezjLKySPJyeVCZl9IawW2rnoBewINCamuG9OuJJkdkY4ScaqW5CETdvopn2jtPhDM3rh6MH4wW1clURMedJslHY5aWUZzQU7FoTrKUtqWfGzWtb5moDRey56GON5S2q7GtTickZ16XG6C7ALrwl0PzobKpvoSLVQ1512lq+SS9rYBQl7K8XgUL4KEb9tMvUWBZl1VyIz4TJVy+1zvpM5RrKoUl9GFAvDBnaawzE4ZHdxbvKJwXl7WJ4/GEWWoyY13YXX7AqC3vBvLSqV8IWPapugFbx0d90v4CpWnY9JPwXpXcpjZ+J6xxlrqbNZ7luEm0aKSSzPYXbk1OUKa2FKhatvxsf2dLNebA8HIp02jXxwO27FxIl127tZarevz7nitvOKgZRJveCv0cNA3Qd9qATqJ6yofzQzLg8tSV9GjBN1EnmxcrU0LPcXPsctKaTqorNpxIs5P2+EirodcugiQ65kobwWnmOkrQYx0IInORqxWjFG0YW7OcAaTW5fGRzlT2JXc0rkrrTie1fouOR4kaarY5pQg+LJE6GiTUVC4ySBnP5IZaKaNEouPZ0Oy6HMwZIc7YqliUB9oeVptL5pdhS7BWKD5YlfKzjjhYyzhhjSNfh0L1V4iNy2Up22L8kmHeQ1UO60LKaVw1PcHQlivlXzAk7vU6U0V6gXEsyRuRvYt70Ny0hPMxeyd2cd2f+RW4S2xCnuDx9nG7y4qckrFqYIIzui2veixmT9UsC+I+6XFU1I1Ss4QK62zgY0pvOI2YQ/c3u5OHb7WfQXWh4RaU9digANeOh8ZvNILPkaP5b5Yn/rBuTtMLN0gu2q7aofd4jMR3I91sqdXommvffW4uVdrPTvFLrk8uaw9pezqJqz5TUtcoX1mwLRgeKh2Jc3tVnZPptqukQJ3b8eVxtDNWZXZllUFOTU27PbQsBWbyD6dwB5Pqi0Oqk2FOLfVSpzorS3jpsLzPZ2dj9zW4LjjhalTNtuLrj9avFXtmlRksHEJuqRBSGxkNPtbkW9AYPLIeVji2GEycX+rm6i+LDVmKoIKTG99tF7lF7sM68JSVp6CavIm2JliSLVsc90fTqkj9pAB55srjlRyNMQRnHmktNc0XTOuXa5UbLvX6qhjOKOnUNEBCh8pDkqNHrREbCY661I2eR/z9LA633FWV1M5KY/Le4Z6/eVOlWslWVtbbCvu4asvXyIXz8k8Xm0R/pgO53zMA9m08Gg9xHxko45m3DgXIJ5yPmIujTbRsaEN6bI+17avyGvnmqQgZ8madHYJ7NSq16QK0jaGNt4wd1Y/9ry9zCsxANUg2rCVKgen60ahdt1JvEnb6YbaBwEZogBRksg9tEnuSSUo7Ip9G5LNdbCd7hJd4Yzaa3jqusyEUSyka0F/XNalrIyxI10OxcgfVSpvW8vcjhWsF8FlIyq7Zq2yy9iphauKNcJ1461UY/TX/epsq91QZjhVmzzkicVJRDcSx5+xpjmcksgXWJFX44HUtigd7yy/lRv/rnpec2/v2wleD2ztNqf9JNnKaQ0qG0+6SzxQjEo6WzIvpUMp5f35tm/1BIe4MT3k2WjnXZNTex/mBGEpWGDyR50bnZZIOwYHmY7KuKGiVRDXTU/EYV8CGIvJI2qFu2r+B/fdmZc77Nz66sjcuaEb8wmrKUdbGa11tsI+DG7iYV/e3fpGCyxcM83pPiITWuMYaZOxwNOn2iIw3x4SrvBopDsZrb9DcR8PUbI5R7EdMzd2TOkYmkooV2JNMoJCLYbGisIuLKw6HVmk60zGOg6NlB89T5lQGUKz7rhZwutawVRBOicts12J3d3f9VkP2Rc1VKxr3hw9Pbg5PTWU3p2ldxvbW7ICM/jFSrpu6ktJ3DGY3kSwYKQ2cXIpCHJGnJrYLD5zVthOJFc1qJ+wZry/bakm2YplXiicDGewmkCNRN3H6445nas+aI5ao0MV2ksSgvk3eGWYEiWTd3SkZBWiGRFXTTQkneKeVTWqNWXE5dVeJFgYd8nV0okSTBQ1/Wbf6p6+rjclXJ68FBgrO1FCH106MR5kEEdw1gdBEJ5t06BKQrEmtmaWJLe+6HvTqEe20s81JE9YETH80jpuwmrcF51i4i4zTE6zOR9yY+o3ZHiERdDbUlFSEezRtUzW4dktoW44j0JvJ8whR1Yt4s4s0LLh8+MqS0VLKPOyXRYJgSWnZlMER1uLd6WGVRcfY0jhDMXigVbHlbU/j8XdP0Q37bzlIUnUllLuG/36QsR77nIDOB0Mh+NR4rXYucJWekJh/7CVK1L1SFFOawlPrkFmT3XHEfJ2vdtvpGUmY1fDXPXpYe+Rulxat+2V7gkjLRxpH/VecL7TkLIZIbhSqsifjJKSuMjyqQt6jYcS5bedd8Z9/y7CN1WEPHbcj1qt74phidyrCWZkchOwdy64ySgY8gzMPdkpMeoTlyNnftozmnNHp6xdTqdAUCTJPlI7TL35UJ1g9/NZz9V8ZzOUbum27B/s6HTdq56e0iIV8ujRi6/EXkA78xhQW9jxq8223bk2PHC8xZW96+5AXLKMbpXNlpPpHEcgaA96ft1J6jun4W424W6CTgx1311Zfn3YB1KAEMPVFi4cRO4h+xYWlZxJIQcRt3xLVucmNGDR2vIexnLhdV23S7i0tV1A2ih1v2tkUQ47p6II5tJmjZxv4JoIlo3n4/RQ0ZYKjOMroRuq2NEetI3aX++oHvSW1YObDTOSVUZRROO6IGG0IkFk4gIGDNLb9JGIyZB8QK2NCceBrTfd6kDfHZNktCSwQnLZpLcEHQbXP9EOku1ABebymxeLGDUg4X2770Y7At29tFxRwnoqnMv+IDYC43l84Gtxvqm9JXWITolIu9BZuMVrkmnry+aq6PWm8M8AD6ResVAw9HCQvvWsA+SpZpLVYOK0i8LoA45whI09FAykG2t6G9kBT1gwlC435nna4pgYUMPVU/RGnDTSvBY0EtyF897oPW0TxNwhh24FXhMrU0W4ScNFWOCiLg6yARKk7C6dhTSjIc2DoOEW9iLKR3muhxxn7kr3TDhMHV6PUuEFbrLvhtHx0ruLtie01AZvuiGNu1se29Ijc8PsdnF27myiS6E9595vKXd2VC8bq5MRYz1TdyhBxsfIYo37eAj6k1kPaTcyF1PfSohfrJldJMNBL7eUELsmdpwmkZF9ueLxnkPKdTht1hWpF8rmxPK70W3c4w63csKhkxuX9wHB8a3IME1pmhgJXcKcK/KR3CbEGKsj1OZSFC0ry+hgOTwUJ9TbGKwjD/YFqTFp5cC6WrIkDEdjBJ2ZXMdFcgtZ5Kr1ODfxdx2+1/p+mS+rQO6XDKbWVNsQ6rbab47wcaJMrdaI6GAgwP3ardU6Q+KHZtPVaGL7kcRz53QihVtvlLAv91cfAh39hoiRhqCQ/dZFpy6UxzgwT5KCIOtELbTMRTEz3HI7JrhYmFZd1xkS2/LaCxJRWmtdwFcCVZYDttI4PfM3dyUvz15P1SsiN+4XH4lWdwsvOhohJhRz8TOyovPNiVSqkDCiNVlh7Z69k0NFTS5EXygsWCrLowuCKbyGsHXQKAi+Ex5k6zBCQowvYsp1hYBuApQpmhVZdwKu95wgrI+6jx7Q1nf2OYwKqwCj5UuWuXs8jHZnNeiJCl319J4ZPCoPhp2LLXu1C+nDeCvE3i42d01eagyMISV3l4RkeQbDn0s4Z92nnAj2LwVu0meeLW+By8fGivLbjXbAdMHg1gcU4aFDvrRcf8NNVHNWbm0tnXxNIqjDHbd0p5MbR9tyCR7mK/pyOREIlR6xLQs3iNaPd842vB6CSRTq5GvH3LgIy4QxAB2fm+D77cbRNbRMmfBW+oIlRTEQUZvKg3G43ldDDWbTbESzwz6lYFgcY0TaRPGWJ+BGrxnE9LJA4a/moMK40aNevFQjvVN24bFcXjabGPTi+gZ314d6PvP4+9uHt+8Ham//5i2q+Yzl/9lRz/NU5usLFI+zwdANPj14ffp3Qvzjw1vrp0CE55FVlw/x67jnnw6sPv75gG9ePz1fPvp6ivs8Cu7deH7V9i0tg6Hr2+lLV+WPVyTADm/o5lf1uvltTh98//4A88nibX5nDmgyv3X0pa++vN4wfNye330Ig9Ttw9dl/Dq0+/AWvN7P+YKRxJewrWfVXmfuQCPsHXnH3n77P6jm0gMVLQAA -->
