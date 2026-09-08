---
name: "rar-cowork-cookbook-ppt-exec-analyze-order-management-processes"
description: "Builds a read-only executive PowerPoint deck analyzing order management processes from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_order_management_processes", "rar_sha256": "610c1f3c9439f2eaba3a377a24b2b28b58f3d3ab6485bba655c282090ccd0aa7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_order_management_processes`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_order_management_processes_agent.py` and in the RCI capsule.

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

Analyze order management processes Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck analyzing order management processes from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-order-management-processes
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
      "description": "D365 legal entity to analyze, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-analyze-order-management-processes-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_order_management_processes_agent.py` and embedded as the fenced Python below (sha256 610c1f3c9439f2ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_order_management_processes_agent.py` first:

```bash
python3 ppt_exec_analyze_order_management_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_order_management_processes_agent.py   # or on stdin
python3 ppt_exec_analyze_order_management_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze order management processes Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck analyzing order management processes from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-order-management-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_order_management_processes',
    "version": '3.0.3',
    "display_name": 'Analyze order management processes Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck analyzing order management processes from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-analyze-order-management-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-order-management-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'da8c93e1015e7358',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-order-management-processes'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-analyze-order-management-processes', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-order-management-processes-2026-05-24.pptx.', 'review_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'review_period': 'Reporting period and prior period used for the trend chart (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for analyze order management processes reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on analyze order management processes for a 15-minute monthly review. Produce 'ppt-exec-analyze-order-management-processes-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze order management processes data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck analyzing order management processes from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on order management processes for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-order-management-processes-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX on order management process status from D365 ERP data for a short monthly review meeting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAnalyzeOrderManagementProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeOrderManagementProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-order-management-processes-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecAnalyzeOrderManagementProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVpbnV9G8jhjbTeYDAQKRHRUxEqskNoGQEE5Hmn1fxCIWj7/7XKT3Mu2qrOp2z/w1ysgnlnvPfn7nHMFvL3bXRmX98ulF9+1iwdtZFkd+vbALb0GXfVmn4KtMHfB/4ZZFW8dO15Z18/LhxfMbt46rNi4LsH3bxZnXLOxF7dvex7LIxoU/+G7Xxnd/oZa9X6tlXLQLz3dTQN3OxikuwkVZe4BbDi6Efu6D+1Vdun7T+M0iqMt8wYyFncdus8CI1YL7nzotLTy7tRdBCWRchIB4scj80M4WYHPcjh8WfdxGi4O6+7Boa7/wPizipun85sPCdmdRm4dqdlWBe/GwaLIY6LGosq5ZNJVvp0Caomz95hVo6A92XmV+8/Lp518+vMTg+OXTby9uZjfg0otatSzQcPPQxVdmRaSveqjvagAymV2EYH01AksX4LzyayB+Di55frB4O/ux8bPgw+Lf/z3t7Tpsfvr0uVi8fT6/zP+0rli0kb9oS7tpfW/h2pXtxBnQ+XWxyXp7bIDp266eNVw0wFFF+Prc+Y1SWS3+Nt/78cnkNfTbHz+/lEAEe7bN55efgEMAv7qbj19nKtWPP71ms/t+/OkbnaZzEt9tZ2JA6tcvb+dvZMHCb0vjYPFFV1n6jVftu3HlA+J/0G/+PEV/I/dmki/PxT+W1YfF9ynP+vwNyPsMRQfQ/T5ZYAOw8+U1ASH44xuPugSxYxeu/+NP/4ysG4FgzeKm/S/R/flJOALxD6z1ZpKfPjzc98sCetPtK81/zrYCAfNXNAHL39l9NdQ/o/3w7N+RzuICpMC7L79L7nsboL8tfv6nuv2rDR8WwecXxs9A8ta2k/mfFr89QuTnH7xvF3/45XdA+j8lo5dd7T4ofAEgEgd+03758vMPzePyD7/8/ENXgSj27fxLV2ffo/k9uz74/MmCb6t+/PNewN8o0qLsi8XXHFr8Vlb/o/79dXG2AbR8u958WvwxE+cPtJiVeGf6NMEfsrEBsv7Bjj+9/A4wqADadE8gA/jxb/+2kGK3LpsyaBe6W3btAji4jXN/Fv4UxQ1Avwdq1D6waxMDw76tA/E/e3iWuAwWv/4v9wH2H903sIerqv0yA/iXJ1b7Xx5I/eUbUn/5itS/vi5OgEVZx2EMFi+0jap+npcBOAfsq9pv/PoOIMsZW/8jyOyP88EiLha//gUuXx4EX6vx1weCx0801OjdjIRNl/mvs86XCBSEp4YuqGfPEuQvstIFggVxNhcCIE+ZgarUzvZp0jjLFl4MsAbUtfFBG9jw00zs119/dewm+lw8oRtbPAteA4MFX8VZfPwINAyyOIzaz4XvRuXih99+/2Hxvxf/ateD+MxDBcXkzUNAwr2uyAuQcd2sO3AecDeAk4eHfvv9zc6ATAGqFPBnHMT+czOI2NT33o2uC5uP6IpYOD4wNjB0XpV1O1fbuH1d7ILFV3kB0/nWXDGispmL81wW/cIdAVUbqPPVkqAmLhoQlk0ASmzX+A+uvzq1/RAxB6lvt78uJFoF9anMwJ9ZzMcisLksYmD+ryHxvA6I1D80i+07ideFPMfoorJru4pq+41HYD/9Mtf7t+2AuL0o/P5zMZfkR5g8EuZpHrAIWMZ9c+nH2eegc8lBSHnNO+/HGnuuoqdHNa0/F81bMtj17AoXFAfANOxiby4R//EWUk1Udpn3sB+QdKb05gXvzSuPGHzrCP5Vb8N+rzVi5tboc4ciS3zx/1079TAMz2ssvzmxzIKVT9r16bC5rZxFfXaigOlDmkdyfutx3nHsHc4/F1kMoq8e/+O58uHmtzVPiOxq4BVtoz3ogxgDksx0Hykwh3Rdz8ljfy7e6wZQafEASRAFAC9APs1h/M5wvvsuaQRAYT7/1kM8Qqb2ZmOAMF9UnZOBEAx833Ns4KA2mt347luQD/6c0n0Uu9GftJqtDsIO0F8AIWKQmKC2vH7F8ufdd9H/tPHZKs1bHm1kV8xxMBMAcvizgLObZl8C8dpnFw/0/PQgAtTIq3bW3QF5BDR9XvRr/9bFTdzO3n7a1a8AdH+cv5+azlf9oQKpA4wFEqTqgHUfKTUHYw4aISADiFGQYXlcgMYAGOXNCA+Cdj7jA8Dft871SfFx+U0h/5GHc0V73zgrMu+Zm4RnUNvF+EcYOX0vTAC9fF7x4Pv3kfaV20x7htIGwCHg+H732U28PhuCZ8exeKf76R/GpB//2iT1KPHGnwPg0yJq26r5BMPPsvxelV8BkMFPWZu5Qn+cMeHjW+38+Ej+j9+S/+PX5P8Ti6f2nxZ/Tcw/kXhLk0+L5Svyisy3xLcwe/sAq9Aft9eP+Hz3c6H53xAXsC9zEGezD0fQEnwtj+9LQI0Ma4BBYPGzXDZzle1BYX/UB+CQz8Uf437OO1B+inCO06b8Ax48+gSQA0//fS1j4FbRAt7e3GuG/jzpPbKk8V8+FV2WfXgBIOn/lQlvrln5HOXNPCACs4Mero39x9kDNIZ2PvzzxKw8DuzsFQA/AKis+WMkvlWaudL+IWGe2gItXcDhwwzdAAdAkAJtZ+ZzstkNiF4QuLNW7VjNajyHwbl9fED7lye0/6NAzFwU/oj+M/69BdeHhf8avi4MXeK+S/lr1/qPZC+gNZgpeeWnuUp+eMMb8A0mjQ+Lr0MD0OdtjHvM3kUHJuSf54FlNvBjy3wA9oCvr5u+/g7h+C+/fE+uByh9mcPh6dS/l06ewQaA8WzeV5BSwzN0gLyAp9e575r/hWz7iCIo8RFZfUTxB8XvGgw05LHffwFihW30j2KJj+vvgj0XPw4fBT/vQLMWxO2bbMvVAsBr9/arxT9jBTwUl94/stL89/bwueKRNhU4qt8vgCj0voLhow2YE65uFz8+2OcgwqNsfJdyLl7B4psNfvqOUA+pQHUBNXp28rfo+ebD8jGBzvIDn7fPH0x+ewFZZs8dy1uevY0wYDkA44/N3KTBAJMAQ3D+RA9w7/9muHkj1UQ26KgBLWKJuMsAcykcowLUtx0bszGStFHcQR107azWAeZhtkPg65Xj2MRq5aJrFKEQ1/UQ2yYBvSccfZmb0ngWb5YNWOUjsKz/7Ta45L3p9dRjNtrXWWrW/029314AM7BSwJvd5vmhYWrpEJjoaJUDTURQ9uerPGqpTtGmYnXFcOYH61SnaJJdUImUKubY8KFu7+nN8SjztHVbimdVOq7x07QPOg+RUZzV3MLfM/Je0S8HzMQISszWK2rXDhjLnwYJxu7oneNTf8yGBna1YCSWEl0Jma3T5zS9uUGlbS/GMaiYSBTRM5Sl12sQEwwNC+odphiV7hKFO9EcWSA9mtsD00TQYLOtxBSYvU8DT4Zu0+TFnU8OMsWH2k69Y31q3ieIdNOaDW6cuLSqpMYuuz2xuxxI6sJvh7PS53iyu8ndAZ6WK0XbC+J+P+70Q6bfyqIPx/2BJelrJImqVA6cgF8O5bAlLZOvIumWBj3XpbV+HCNEKgpymqz7yVkRkIIh3ammSAq6CmdycvQtn+oGL0H5ZdBNuRmd3siReN9L8NrSTicPjtteOY4GxNBYT8b2viAhnxiKOj5c87y4sjuL443uCAs5oTU5ibh7lKZHw+cPWW/sVljKyndku99e2oquekHltquwLNiCtU1+u0zPjoPYSeZCSs0EiNIb+2sQ7Xc3Ot5gbHrcYEMgdlLJ0k3VE4aKaUcHiZlaZtPTRdIOJk/EV1kiGCQlsYFrN0c73iTrjsWTRrCWSrLM/cu6692Vtr/ETLI0dIO+5EFWSpxuj5qbxsyGXJfrPLLSps5PG3XtkArN1BgS95Gw5OCDqa4MLS5vunS2i+TgiIV3gppMqGg4G5Ce3151I0vPl+MtuRvZ+mztto46atB173OT6GlsJ9QhC6uD2reyQgrSKRaSaLe8ifhSW3GhTQebVNG4gYFlahUcJa7rC2him6G/bQ3ZcYy9d+vpVjSwUHRa9Owv2UqRyu68jVN0hylErUvhOrVomL3AeCnKl5XCpncE7mmVOoj7ADdLMtBP6yOG07B9VLdsc+q4aXflCsi6Mfs6aCcD4lZdPMraWg5b/HphLp3BE8Ul45f6JMZxuoKXJ7KzxjFDqFpcURezJd2jRa3FjuStvUKvr/GqU2DfhahoxbXJubvCuqKlUDcKhOZeBXHU7D6F1+u0aYQLEZ1zjSisuNOk23hQGoORyCFQTWLo8XBd4DEtlTJ130onWjoZqRYStpZiDcdPlJUuL7dWEZbeth/9A4KibEl3W/ZwRPJtbUjhpSZ4JUI364aZapEiiyKM69BCaNbleCoWpcFTmGh0pKSZCjm2CIENq+ZUrnnQ6d2KM+sX3I5c4lq89on1pab8/dmPUvuS2rGm4JGl1scgovhDeaeKS4BB1YQbHm9cuiq/U5SriUKxFCxFI0en8u7LyKEuFwGBkv2hjySsVfcmn+xPTKyFnY6bfWmdznsTLRpLgnlNCadlTWp+ydFbAdnaxz2z16Ito2B3gorgqzXa9Kk4mgd/EtWoTzbGVcWJyfSQSrLtuOMDvYLoMvPYtFzLJV5d0uPUKqyMi5VRpD2FNOw5Y2ntpDBMTAvYPWARXl3eiUN4Q7ipyokC2jXjbd35Byo2lz4vsdsYDnpViEDRPodOsg6Px1FFLTXKcOfK1Ue8YLTYO5PM1rSvp45n++N5By35xtbJvRmnbpREHq5VgXVyhTVVYW2A1wdJwEh4r5+6clA9SLT55Lr24AhOpjqI0ImwMmuVcPJ9w1M53jUB058zFJTT3tuRxHkK1FaltwSlTMYxJuSNO+wL3qjEaWPTRSGofBdDQbXJU2m/Lw2JzMmBpBkNKiEFOTlDKI1ugbepuqm6XerVeGdYsArr2jDRpbw/uI2BA6PSMumZokeslC2CXPbmMr1yFXtEz2NppBhs84ZGyNqegqrmZlOOsUTSJvRTbavtaR1ji6xqIn4nMw6plja3R9mGOhIbuyxOzvJwsK4X+LacDt5xcz4n2hEi6YhKzqi48hsnNMvLcE/zFYpMPI8mspolzCFGHfd+QgjYx9oDsVdFUTJWm5MSaNW55FRSkNkc8weNmPZc3DeT4mGUEUpMHUUowl6v0uGuw/SdrEtngEkYTyBrrQrYMiOlsnHjW7OqjIAmr+FmO6Q6Em6cjMQbawcE527c8ZyZysivsaWU3Ph8THDK3RkrBsIpSNgTJCUgva7YjY6IE2eAHna75UKuEgIOiSH5hKux4XKDQKu7SkSgCCQlx0FLVDvVGSFuy+kAuoKJyqz78gw5tGbr1qTJx3YTiA1XEevrBj3lZormYe80jNJEeOvti7yM8/xMoB7U2HwkZxS2ibRjj1CqaWjDaeev+dA6XsjSc7OQJhztum6Lers7XgoTl6zDyFnSeR0kpgEdeVEQ657dnenT6J6h6IjZ0JnY5XjIaryprk3BpofN4J6ccKeMW9Rt9aSyhat9dzQ6w0OtMg3eNjCEMyE2UQyzOyxXbKff8o09aP2aU/duGR6KMs+U/uo2jY7uzog8ChujOHSbsYbMC7nepNnleuJyweLqcE/Txs5k+nUsDUajQaihO5ueopmWS6Qu5uliQomdVC5PkiOVCIuumXKLHbWVX1f1CGGH49AP4ZrfNle9HMZMEsxVYOlQeM5y5E6D/hRWTlIWhQIeIYiDaPTqyktxQBv3U5P52um4NLWLa2aVL187Q1wi6jaUjkUg26YG3+zbQVvuojInzqudRWpnBK5ynGcDnSvvbM1IlRNU7kXkuO0679wyW8X6GbR2Vw6Pznpk9nf5uCQOLK/kt3x14GMvjNOKkxO/W1FbSnYvKU+EGNGcqJJDDzR8jRjbVwbDPnURO7Dm5RLV95rYhUsMWTcWTSUnBJMph3PXnG51Eb0tCKhLpuvx1pYYekVvRrgXMaqbkJU8acgK465jYkk5eYjbq0+LLUPmwbFmETtPS2dfptciTY/V/rqjlDw2KlNCKme5a3bIhm+NSN7o6HSOUswVpo1xdg0J1qBVeXUn1hPCar862hdpbbsm5p9JAd8c+UvSOa4sJeHVje67i631EL03AQ6tLbHQFBWZrOJY7vgkpRReVqHlKToft6V0ku21Yg3l/eyst/nxEtF6X1f54bwsYYOXb8xA6URVa1ZvIifqDmMTpYT7w3Dex7Xq8bvRB2WoHtSVunHbbGANsc4PoPwWkE5z5Wp7dSYzbbrcXOFjr64UtKHZbGcEtyVnhxc9Hbc3bUBcjSPP4g1XmAJubZazEB4RON9dF/UwEjfc3t32+LDcraWbcb6Gh+wsH87otBMksZd59pb57nYSN72/leK6su51ddxvgzwnWovFolIl7a1VZiKo5SeB9ugub81AhdHlsaWsyOa1aZfIBybDBhbvN5cdpwVbypa61NgwZZgAHgf8SI3eOSokDpm0ZSBAx/F4Vy/jepkL1AVepS3lMPCeJTfcHTSjWz2Xsbs6iM6BzpbYGdHCHjSm+0OLa+2eZzvoVsPJYXNVw2iSuWG7usjp5QyTBhKyXYLFjKjpeGz6Fwa6sXWqUUnNiRtvJGQ0czMYs73sxqmrlj87FrxWFH1lDvouIgfE2qRWXXPjlmW4kG2PFJmHYrV0nR6AYZ4R7J3YNMQl4c7I/XByxTZD2G6578pgaxw2UUltz8d0g5+CA7K92gXjaybFlk6A5xxPSHcIvSVmvucC+oAKqXDSroh423TweelINZjvCLhfUnjgnNIUUhjO254TEfdwcz9ZQmvD5AV2g5Njnj1lMqvj9aD4kKff0Q7rV5ZdSEOXQPxdswdQ6Pc8g1xjHEMA1qCnG4Jwhy6JIOVyxpZHMQiYiF73O3cptT22Es6oVvM7QxgiUuavV4wnqqN2sk9Rz9+jyayduCK7qWJKAKHYeXeCZORuqtw46rtxydhyixoodkxPNwLNzXOyLVbr/rzdHtMAhaYxA40vHdQn2736gdyJB9A39PINA2h/4M0z5uwIPPKdac/SUXXygvoi7JL4rKMbWN11w2kpA/SZxiizk9S+unsSvnYk48G1LKcmbbPJJuTvfqYklr+cqiQP82EHs8Vq1Gm20QmdNYXzRrzF9zMwNoRvjNwbGuWQi9s1fBULFB4uhbtjSRGRl5eiDbtTnC+pFS1GcUru1GS8uR6JCYOVDrcENfDqHFAjVJma0UjZeZueobvNGY4QyWtHZ3QiyTYipuPETt9T0ZaSkANlAiTf2HuQL11K3JVWZTDUKvKI8TDUHqhNGFaeU4ChD5U3ax6dRlreaD4MkpQamZKgr5PDMVVYp8mKbNJDciVt3SBNdo/F6konrm1227dbKhAQejwmDLjdnTeBuoJOtnlGJb9w5CO7X3Mifw9WPGn6ROxuBiW4RPzS68agRdbVFOniZe0bN6gd5MKCYGg1WhMn1t5Vm6Qyx5ja2gYr5GwGWVPpWmODERiJwsu12MOnzsy99dC4V2taM8YBPlQuvGvg6VpQlXwIxKwhvXaT7nTSyjLWNFbepo0dpSkFMO5PGJ7XJ+SWiXpuXkLDQ1eSguwGjNvojCfss7PTgxYvhku+8pTQvRd2KwZ3xAcAIDRuT7WDsu1douTc9lSm1P2wRHNRFzrSzafr3ZdgJ8Tv3dg6rc170ZUYySRvFb8dwXziHZencLnrwg5kh6ysVIq3TtBYT8cMY+SxMFQZIzu9vaInUzcjB50MaoDO4VTtzvAZFlAERip5Z21EZCq8nJ1u/lAYkiZr1JHrpRbA3p69LD278CKGuMh9jZjQMpcDxnT8A4xBsnwNsFtfU+ZYXLwkJ0lQqF0I8dbtGbUukbdFieZ+WG1v0glBvKjdWROfT9YmOfo5DmNqAPcevKTZQctW2Z1cYtA+2KwpWWH2FLlrRXUJ1dsbcZpiMk2ykt2tA0kzsNzdVXsBPi23JnVoxqhX6uXdqZENcuORVHe6673c7SWf1Ut88tI8QC+JO/8eS0n1qijrZTmxlNJFa/RYGedty5Sgs4juEu8OAxSfWKqPmAqms/1gmZ1jBjGlHGyG1kXDIinUL7oOE5tdSV5j9I7TNEQ6yT49qsSxYnijh+kgVmWugDV5WKKYAvqCOw2q4d1JYztCWnq9QgGgiQXlw36UdGJF8yk77lhzxJXCnOqwViYU3ulXmhSdi19q3OkIXTizzatLl6zcC2SoxvrW7xmH2uBJRVpqCfurK3wdYpYBUVCv1isa5ni3HvqoLjbxudql3CXVY9C9rawJj+bfW+xtwbSKWGfLQTPye6ndKw5MloLOK9Ia1aSjqSRHrsULMumZcK9i5ClNIqQQsJBkM/3c4FZldfxyr8BZEHSqmYTdjYSOe67jj4IAna55gwbJmd3gqqvfqs6ItphEqvRIVI24lgfsEN21TsrrvJhadUPWCd77BBTfytJpp0bbmqHFTYiwAXOdbIn7ir+cUA5N2/W6Z/Kli3vTscsGh1gxbTl2YJznJ/t0Ng4ucg2UrSodt6iaJDVN0PVASW1rdcJeIeLADJgGqyftgpGHrWL7AKO0QMoMADKe4lhWjXgahqNgFA77pVPurKRZOWBIlakqXm31zc23E1jhIZffWhsYFK+cdfY3ejcKIaQo0g26cXi+M3ekaZwqwV6FzMS0UJxaTE1gtYpsfA5v7Ylsu4L3Au9aK3c7AjN/gHamW5rekT0pd6olrTWGgJ4Ew5tyGyy78kKiqoK1FVEPxD72JbVeo46X8tTJvIUnCEFapFMJbLB1CBojB2Kxgc/7bd07di0FBpZkpn0/+0iigUCSdXK7I28n0ingItH9QXD9RoOlEhrEnGwE3+q2KL3NJPLg72RDJCh0Z4/B9qbqhdXqYEZ1hnrlmvxGqMeOOAaCTKeB40QCcpyatXe6glRI6RzhhMIaDensW7t6MvGxgdTrKjObS0Tsd2ucVXEJ1HuBt9ZGjuI66hv5cAnlrM54y1RbO+GtgNQwyYcGak0emStDBL7nCpucXcrjhjyQGwY+X/wJeHuYqovvLGncCJZwPwxwX6L1Nb5jK8QitJakSZnMI1IxYsvQMRpKLFaHhVuXZ47t2qu7KOigt7cunXePz9xhRGnZH5J8FHFXrtVLdXD2ieRR/CgJHlxJOawaLdznWTMtY7nWNW7KVqArksJbEqW9UtWQjIm+BylXIW3BMK4lejHam0NtrPcbs8iPuppG9WF58GhHAVIkNreCdG9ne4PhrVgBIMHaxpQDvu1UD2WkBq5O61vZTLDgUCaaCnfseOQaWAFGu6A3QaOtfWvtKtWNt9gAMm07eKawBoN6UWN6fTShmwatoxphsjsY3xozaFaZ7R3Im9Mum9WJunD6xewp47I0Az8m19eW8jFX1E5kWhHIMAlLmyqURhCYcbtZlnclch1jBVP7ZhzRhiOFVWiAOoAIoj1BZmdhoTfqe9HomcjN3cQmJ0KxL3LrFSeMrvshQmJ8u3XqXD3S2nW12uzyLKjkvtkwLWrf5bBASd2RMHQlSzXelfk9Y6p14vt2Q5AOdRSJ0tYT9HIo/UjDNpSRKNgAuldkWlvmdBdI9cz53mT5Bw0+mX5mDdM+gK/VyjnLOSx3DIrgk88c4XiVg/ox9r536cgVfYjwW3S7lF0tq63HtBg1XKGkUXE/aB3Fs+pzveVw1cusJbjJUwGR6DjcbwVYDpd1ikOWpvRqQEViv+6XFiWQ3v7mjxxGKKgJU1XU3eCUCC/rlXhM6ZInM4SMZGRrHPuzfN6K6XD3tTIStQQMwidyWVU73VdwijAm5HT0UtHWWUNoe/iwXYk7qzh1ewAdInVLlhR0dXTZxRy4xoi+oCeMlWFfUigsNqubEK5LOduQF19cAvTpDSmHGHfXOIczqDNMQxPFvuzk+G6juBnA6+WaB6ubrVaoOMHDt/iI2PvVkGdrD3JAyV9tcrG51HRJFV2Mmdc1xMC6rJ3r0pA2m83f/vby4eXbY8iX/86bb/PDof9nz6Gej5PeX2B5PGr1be/Tg9en/5Z0v3x4qd0YyPZ8AtdkXfj2AOvvnr99/AsPU2dC4/MVs/cH6c9n9K0dzi9mv8SF1zVtPX5pyuzxUgvY4XTN/Apn8y7ln54gv6kGDp9KteUX126il/ntyvlFFd+L7dZ/Ow3fnkt+ePHeXp36ghGrL35dzeq+vQcBtMRekVfs5ff/AxYHLVVQLwAA -->
