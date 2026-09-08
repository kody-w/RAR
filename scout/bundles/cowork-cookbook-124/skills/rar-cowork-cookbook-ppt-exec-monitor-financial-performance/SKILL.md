---
name: "rar-cowork-cookbook-ppt-exec-monitor-financial-performance"
description: "Builds a read-only executive PowerPoint deck on financial performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_financial_performance", "rar_sha256": "98bf10b19af30517b23002069df077fde5475d829c00be43d8971fab55010ec4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_financial_performance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_financial_performance_agent.py` and in the RCI capsule.

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

Monitor financial performance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on financial performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-financial-performance
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-monitor-financial-performance-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period to compare against for the trend chart.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_financial_performance_agent.py` and embedded as the fenced Python below (sha256 98bf10b19af30517…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_financial_performance_agent.py` first:

```bash
python3 ppt_exec_monitor_financial_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_financial_performance_agent.py   # or on stdin
python3 ppt_exec_monitor_financial_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor financial performance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on financial performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-financial-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_financial_performance',
    "version": '3.0.3',
    "display_name": 'Monitor financial performance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on financial performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-financial-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-financial-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17cde7e709aa096e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/monitor-financial-performance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-monitor-financial-performance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-monitor-financial-performance-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period to compare against for the trend chart.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for monitor financial performance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on monitor financial performance for a 15-minute monthly review. Produce 'ppt-exec-monitor-financial-performance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor financial performance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on financial performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build an executive PowerPoint on financial performance for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Reporting period and prior period to compare against for the trend chart.', 'name': 'review_period'}, {'description': 'Target .pptx filename, e.g. ppt-exec-monitor-financial-performance-2026-05-24.pptx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly financial performance review deck generated from D365 ERP data without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMonitorFinancialPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorFinancialPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-monitor-financial-performance-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period to compare against for the trend chart.', 'type': 'string'}},
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
    print(PptExecMonitorFinancialPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZObyLbnV9HUi5jufrILhAQIT9yIAYTYBEJskmh3uNn3RSxi6envPolUZbvv9X1z78T8NSqXBWTm2c/vnKzkjxe7a6Oyfvn0ovl2sWDtLIsjv17Yhbegy76sU/BVpg74Xbhl0dax07Vl3bx8ePH8xq3jqo3LAiynujjzmoW9qH3b+1gW2bjwB9/t2vjuL5Sy92uljIt24fluuiiLRRAXduHGdrao/Doo6xzc+YugLvPFbizsPHabxRpDF/v/rtHSwrNbewFmAfohIFgsMj8ES/2ijdvxw6KP22gBLjP/w0JU+A+LtvYL7wOQxfsYZHb4YWG7s5zNQy+7qsBoPCyaLAZKLKqsaxZN5dspULwoW795Ber5g51Xmd+8fPr1tw8vMbh++fTHi5vZDXj0olQtA9STyiIG5ti/K6N80wWQyOwiBHOrEZi4APdvmoJHnh+86/1z42fBh8V//mfa23XY/PLpc7F4+3x+mX/Urli0kb9oS7tpfW/h2pXtxBlQ/HVBZr09NkDPtqtn7RYN8FARvj5XfqNUVou/zWM/P5m8hn778+eXEohgz3b5/PLLAhj380vdzdevM5Xq519es9lvP//yjU7TOYnvtjMxIPXrl7f7N7Jg4repcbD4oikM/car9t248gHx7/SbP0/R38i9meTLc/LPZfVh8WPKsz5/A/I+Y9ABdH9MFtgArHx5TUDs/fzGoy5BAM0e+vmXf0bWjUCUZnHT/kt0f30SjkDgA2u9meSXDw/3/bZYvun2leY/Z1uBgPl3NAHT39l9NdQ/o/3w7N+RzuIChP+7L39I7kcLln9b/PpPdfuvFnxYBJ9fdn4GMri2ncz/tPjjESK//uR9e/jTb38C0v9HMlrZ1e6DwheQbnHgN+2XL7/+1Dwe//Tbrz91FYhi386/dHX2I5o/suuDz18s+Dbr57+uBfyNIi3Kvlh8zaHFH2X13+o/XxemDWDl2/Pm0+L7TJw/y8WsxDvTpwm+y8YGyPqdHX95+RPgTwG06Z4gBvDjP/5jIcVuXTZl0C40t+zaBXBwG+f+LLwexc0C/JtRo/aBXZsYGPZtHoj/2cOzxGWw+P1/ug+U/+i+oTxUVe2XGbm/5E9s+/IVqb98h9S/vy50QL2s4xAMZwuVVJTPhR0CRJ45V7Xf+PUdoJUztv5HsOrjfLGIi8Xv/xqDLw9ar9X4+wOz4ycGqjQ/41/TZf7rrOk5ArXgqZcLytez4viLrHSBTEEM4HsuAk2ZgSLUzlZp0jjLFl4MEAawHh+0geU+zcR+//13x26iz8UTsNeLZ31rIDDhqziLjx+BckEWh1H7ufDdqFz89MefPy3+1+K/WvUgPvNQQPl48wuQUNCO8gLkWZeDacBlwMkARB5++ePPNxMDMgWoS8CLcRD7z8UgTlPfe7e3xpEfERRbOD4wHrBxXpV1C6rAIm5fF3yw+CovYDoPzXUiKpu5Fs+F0C/cEVC1gTpfLQmq4KIBwdgEoLp2jf/g+rtT2w8Rc5Dwdvv7QqIVUJXKDPw3i/mYBBYDtwLzf42G53NApP6pWVDvJF4X8hyZi8qu7Sqq7Tcegf30y1zq35YD4vai8PvPxVyE/dlUjzR5mgdMApZx31z6cfY5aFRyEENe8877Mceea6f+qKH156J5SwG7nl3hgpIAmIZd7M2x9z/eQqqJyi7zHvYDks6U3rzgvXnlEYNvPcA/6WiYHzVBu7kJ+twh8Gqz+P+rcZoNQrKsyrCkzuwWjKyr16ej5u5xduiz4QTcH2I9kvJbR/OOWu/g/bnIYhB19fg/njMf7n2b8wTEDogK0Ed90AexBSSZ6T5Cfw7lup6Txv5cvFcJoNLiAYnAlgAnQB7N4fvOcB59lzQCYDDff+sYHqFSe7MxQHgvqs7JQOgFvu85NvBOG80+fHcsyAN/TuU+it3oL1rN5gfhBujPDo1BQoJK8voVuZ+j76L/ZeGzMZqXPJrGDmRv/SAA5PBnAWc3zU4F4rXPZh3o+elBBKiRV+2suwPyB2j6fOjX/q2Lm7idsfJpV78CaP1x/n5qOj/1hwqkDDAWSIyqA9Z9pNKMMjloe4AMIEBBZuVxAdoAYJQ3IzwI2vmMCwB33/rUJ8XH4zeF/Ef+zfXrfeGsyLxmbgme0W0X4/fwof8oTAC9fJ7x4Pv3kfaV20x7htAGwCDg+D767B1en+X/2V8s3ul++ofd0M//3obpUdCNvwbAp0XUtlXzCYKeRfi9Br8CAIOesjZzPf44A8LHt3L58SsAfPwOAP5C/an4p8W/J+FfSLxlyKfF6hV+heehw1uEvX2AQeiP1PXjZh79XKj+N5AF7MschNjsvhE0AF8r4vsUUBbDGuAQmPyskM1cWHtQyx8lAfjic/F9yM8pBypOEc4h2pTfQcGjNQDh/3Td18oFhooW8PbmpjL05+3cI0Ea/+VT0WXZhxcAlP6/uo2bS1Q+B3cz7wBBGgG7t7H/uHtgxdDOl3/dDx8fF3b2CsAe4FLWfB+Ab4VlLqzf5clTU6ChCzh8mKEbpP+jsGQz8znH7AYELRBt1qgdq1mF545v7hEf0P7lCe3/KNBuLgrfo/+jaj8aghmFfvZfw9eFoUn7X35I/Gt3+o+Uz6AZmIl55ae5Ln54QxrwDXYUHxZfNwdApbft2mN/XXRgJ/zrvDGZbfxYMl+ANeDr66Kvf2hw/JfffiTXA46+zNHw9OnfS6eD/spvF68gj4bF+7QPi4e6/1pufURgBPsIox+RzYPKD+0D+uzY7+cONi69f5RC9d+bsueMR+RW4Kp+fwAMCNK+mhsSO3yg3FdgehTlOQPq9ge8H8wBhINCONvzm6O+mat8bOpmMYF52+ffIP54ATFtz/3BW1S/7QrAdIB4H5u5A4JA9gOG4P6Zp2Ds/3K/8EaliWzQqQIyxNYJVrCzIuxgDaMr3EHWMIzAGOEFMI4Hno9ucNTbIoQLw46/WXtbAl8FtoOi8Ar23Q2g98z5L3OzF8+SzWIBg3wE1vK/DYNH3ptKTxVme33dnsyqv2n2x4uDbcBMbtPw5PNDQ8TKgdCDM1TcsoC3Q7Q6eeP1xFherjHLCrbOadaZpwtidlohqHW/Ecgrk9B0z/dUS4stbpr+NdxerU16gQIpJKUTKuKpMWKDnZkHMpEIJVhPGIpaEySxNcQ3t0DQaoFvJpFPdcaIxpXpO/e9HHduYO3Vy3hpquku1WcLLzTTFqxJxPYcBGEExMBTJVxHkzaAk4rOsrroODqwIDHQoRmpWy21S9HCm2ZN2yqTbZcBTfnQ0XealRvvbu3pSullDTM9g2XuFaul2023dVc1jRxmlJs18ne8gI4mY4oXaRNmm9j2a3k/KCoVmZqFUfexP19NLnQCgbrtNKFShf057iI6yvwxE1JfO5vKEALGjrPaLqEgOCBLXRmgQ7eu1xA8eJ2837O+aUZGxJ1Xo9E1kzGYOawJIj3RlnXQpPVYS4ew2ysh324k+GxZUXfpUgrDNFMuI3ZPceYJXg5+U9Rots1ZNQy3YZ5phG/GlJuFxXVH+ifDEbVbIyAD11piN/AVl8Gxl5nreOCcEQnyFdViXKuiFWnHeGwYJs4KfEgVbXCQ+YLRmmrDGvywujrG0NfyNh3FgD53cprDto9wwx7v4t21km5Fj4233SjjGn4/4eNartnMOtJpqluHmw0Mf7DcQu+vfLpKQ7SSKuq8N7PmNgjW5ZiTAbZWjbNzKS0zjNe3CBcNhfAF7UaPscUWB9E5rC11uR2cqgyG0yjGdKqImJiXPHGG/VtcC6ucd4bmpCQHUUN1R2CS8egrnnSQB3qDsHZYKKW4P+7QW2HFobo7DnNOkOmmgthoezdyTrzirq4zcbk/rdr2lCE1KcLtziezbu2YNaOl8KjhJivq1+mCm525Yo2Cv5ThGtrvr7dCHrIMylDNXKKWd4AoP5GngzQcgvBAZOSW0YbjRpei8BxkSCnlyRKW9c0lx8rbiuuReB3F1tFBDQfzbAPwo+ObeCmWntglo6MPhFgkmIYOdz9Hl7tkeSFrlvWdmIaWftATdygPm/E+7iQJy/X10g3K8yUkvPHg72PeTJmswdYNnWhIumk8WNhbpmDYuc1Rxz120Q5nEDDLUziJh7XT087EljdtF57vAbovVKGZzpZA3rxh9Nv0iNSJwUrb9GRfdfqGTTScsPG5zlkhWTMbgzmd965C3vfXC0mUDIqJckKazohtmXjfjN0kNax8L9ttYqe3LXfBklY/rrCYNSlR03oxTO39STvSpcUmApszeqVtkkmDmq2eaWpU38nD/SggNh8J+LmZTBGq70MkY5mcQ87ada0WXQXROeeQQd8Jm6jK27A1ikJwOQZn3H1aC2SXkaXO0Qeoyq+YAUlZWehogk0CDZPdTeFJzdftNLbJYtPrrOMs79fgyPrsmLIMLYbaeNi4h37PcttjTKxbui30RpmmtcmfdbpkmhRX17vrKqHNQl2TJ6czxGpn+UQN2h+GT+P7dl/lu6K4B6mwVrLbXuS71baICoxdc76wU4P7TrEOZagv9+tVkg/J7ooeXA4gbUfHCRFTmyvGIpQNH3lmgziFq/Z5IwlrmsCEQ0piuinLbtqwmuBaIM+q7QY7NOsz5XfYiISaTW+UwmkqW4f0hlDSKD7Y8RnpN8qwKi4YGh2nbYzpbBHGF+Ce+jDSpmrXSOGvr8LmsCkcE8I2usziMXVMjkcND4ELRBouWMjE19FRtoQLbJ/MPpRVyY4mG/b1y2mj+6upDM4bcq9NKc7ABEidiEnkU37gzuVuKZ18/pLEoZwPURmjO9ZBxO7irGF52Q/AIewpq5yjQRWStCxojueRY4iuXAbZJSF2lu2MJ2MjprKdzSOuZp1XJwrW7Lwwgt7GpqNgYpShlrG3urtp5ZpOVHNSsWZotrHF3VDayiCb9j3Dhiqy6bWc7O9ea4+RnI6T5U4nECEKvtn6EO7lS9fwmMpC+aq5Bl5l8hm7v+B8sx7wk8hxTJy203HYQKO/H7kgQRgGr2t6CNT1fpvfUcKBoejIEso0wkOe5r6BGGiVBmJ9DaOdId4rEu+4VK3SSvOY1fk2ajcD1vfLM1PqcWacoUbqZdMNSHeTJIHTNfx1r+6KXZKnJWfSPXrrFeNyLbIDiMOcglP5hGa7NJVFYToFulgRo5KFm35MKoLH7MjMr/gdvej5OnZB3+K1t8MeGzyp5kihoiMGidklEZh1tdvemixNvOZydc6R2fvSWj8boWDThKxm6c2Gh2UbUfwlQ0a24HWWAWNbQl/HJVMoCnwaV7o4hjW24fJK6hmRk8PIGK57ds+VSgWZozQwhUbrDOpClaOfQGAcjCgShn2Ih1V2bn3uZIG+s55wKELC43hLw+vttvRvME8aR8rZanzFeyWv3uKkl7arWzTebM1mnHBErStyoozYMaxBcwF4CWusk3Nm7+8vFnwQjiMtkxrDxn2nXE4HKK6MZHcsGySKNmmhHaO9kYpnZcxvnZTup+MhPTuxfj2FEUYnt9VeV0yi3VZash/6Cz1EQLmer/xljdmGJG7Fs9bXSs2BcNqIDBNEF2NsAJJ5rb6r7qhkXPG9SZ8g2Rzcnba9VZbAqbA0hNKJ04/u+oJWY8NSW5a39vfU0s4+fJMKgj2FV3Pi9zY0dgyeeetixacuE2TYWeTza5o5TNCIW9qkhwufhic5F6WcTWOkomnqOKgnPgkHgKIED7HdQaflk0Ec731lITwZXBP5dpaH0VYCW074u23u2VvhjPjk73wir1mSnJDtSr4jgypHcGpIbm1t77V5gUUNhs/MTdeFE91irjIt8a2i9g7E8FptSzko5O3JHnFr5+x19ZZu/TzlLYEvjAsTatWm3xPLW8QKzhG2HIQ/8hDJJoZs82DPUe+EZa/kYXhbXc2QFuWStzIevQi6WvbYDYU3WAEFppjvGcNLDEE+6eKRisiDdGrGKAL1+A76vs2oH+NtMK06j1TJVVNUm1UFKa7N2zuD0rzbOp+OxP5seyFPUldDO+8tkdIKmcPSoSV9BfE7WzqI9BJxGmi59FGTJQQDdHCXON+6ScM5a0KpFEVrd+PxMtGC6Qqny6jtUNKx3ANhpMcuhXC02HPhATu1VzgSQsb2rk1p6DbwKc3K2njqrpaLdaoZsWdU1lvOKnBnUlR/c/VvCXFDbKTZX+UNZSZqSYt2UR39lKauJOhwXP2WdQM3YqMxxXqZW+aN3pjj9YKiCWixqZWdIGvycMYqCY5LOmG4EwgSyDHuQZFMWGNeHfSeMdbuKtLkKXJ8lyo1JVMqCqFcvVeVewb2P8QS8oIpJgiEwkAU5pvunkIJppqEetc4nj41ymWiAARxOHs7WXnSIDa1JF1eXIXaYZ1zWZXssjEwMD+ruUmsZMfUlBuGthbm7C9eLdq5VWyCKjHvS3FgnY5GyIKyS6dFuQMScUboXthRr+krAR9rJ13Byt1oxTBTWb6dTG4n8qg9+Ycs3+W6Va71NkwIzT8jucRl7EbgM8uniFIIYOhYenK41elR0/lDJxsiNu70fhjaXlsN3oYwrAtRiuP1jDXoFuv37WXccew+Fov0OjY5CyPFHiNwbd8vcySzSu9gCt72GgbH6jLsLuxOh+Toem1ueHoNdO4caFWrDNLQJdszOxSseB3tc+aWDOMFSbaGmCNhjhjcb+hGGsk2PWSXHc86BhodDPR2EHbbqxvilmM3F6btlvt9D3HLrXMxd4HhiQQVwpqnQxJ8WRLbrS4e4OR2buMUQe3rlbaY+sI6nrgjpMOUMqkYUooFZdSOqdDRrrlLoNga28k12G1dFYzLpmshBrWtnUz+4OlYHDC5CF1uYOOzO2c1tbxSfqSvGC8Rpz6/t/J4CBsSh9xLMHRbWA1Xe+EGkd2hTs82YfX60OJInvOyL4cCcbr60SZpaXlUhXHl5X0ZoufoUpdKQFZHz+9PgeI6uX1o3a1wJD3SL7gj6HX3/SrxrtW5EdTVBQl6npyWLtSiZb/bj6bmm0pthMf1lejVGPS3wpWq+vboGWQGHzgYH8tVoFMNl8n8+VxiBJb3OujRdIDSBs0ho2iSroGP13oEACEJrrem3Gu171YKM2VLUqw7flOpkeR75yy+wKlZqtsyyAOihXOIokVUOq51CMfFVYOUDgOd2iVakDF7Duk10Y10owasbtvLHQC36/EYkg7ZuxjbqUcX1LY610HhXVUbSrVhyrlXbIq4agchh50QKIo9pBeNLE02Uc8mkSJmTTLT7lJl0k4PgGJJRw1wUJqDKV8ORU+bYaK6bLOqSHmDqruL6rkFsuMphXDKrm6Wh7jB6okvzjTWNVsc6dT7HQPNtFl0PhXT+CDAq8FhUGJw8GqN5NOSm8jVqiOOxBk7Y6niLL3uuIvOg7lc28WAq3J8KnA18Db4Zs0qfAw5B/Xi5dik3SVij67QNWeqR+9+u59Lo5iKtKqOd046u4qPciTDG55l3mtpFBFiVx4EFMP3jpzfl73eZNZ6xAWfxdCNmTfiKoHG4OZIVFwwywrBIYtb5iFdhXxVxfuqmSp7ODpiNMeDhOfKUErJ1tpeUC63Mc9PigmYg8pRbCeHbgRGUDkvm2VTTc3o3J0AJO/GXoJcLCME504FSxKSCwX3ACrLICOH6qTZzR1CHWgXUfBWxWFI3N75wyDS3iZN+A694iIi7Ish5BH/NDoYr3SeIhUrcamukFx3c5dsVFlkkSJWQEN64gQJ7wj0ikLw+Tqx9bkQtGbpclh0vQyQ5vS+F2Gr5iQY7l6s15YerfOjslXLqQJF+3BXINEt2BbBaE89xBv+JFVGdNKh5Wr+oF4kFoNkyBeeLdZOKOXnCNNlYWNq/EUZrpd4wqt8aTd4OaDxOrtcdnqzPSsqdoxObn1apoK+vSu1ikDkCqcISoqp/bbbRTKBbcSpIdYRo0fuGVkVN0bVDGzclERDsCs4OMSGGGHF/kyVute3N5lr735iQqmX3Tm+lyAYP+Rr5rDV92OrxOy9iQUj1YyzPbBCbyklOtvf0zKqZF0Jhtsu4PbyTT6c9OBkyabM8TlTypOY90dSL43VdnPur8clixv7Uhtwa2J3EQ5LO/E4ulsLDgkobQkc/Cxx/I71W6OzXIFMtMuZB8GKkDB2N072UNXDMEk4RPeYUIrb5RbLGMS9uGoxZMRGH3ls14FKLmzt4+GGM2Q7cGqKqmADhllgA9cxtnWR92hIeVnESbd+rU0SYg42i+7acuzOONhV3cqUPhwxblWEh/wWXoIkqWmMrnvc7gbpwmXFctutA4GcnElDFJSk3BVaIHkEce1ecvlNicTTXXUkSM1Xh9Q9nlwk4Td+HFt+Io/DZmp7lsfC+pY1iMe5Ej1SEFFAfMpOJjN0CnW4oqMo3i7nUw9XWmPeXX6Fk2x+d4g44uFAZ9uAsuA1TAy4MgYFYnZ+mUvB8l5EKxovuBYxNCtCvQvYkRR3e8VPUZRYQSuf5NFwpZGoMAfbqLHX3TdC7UxX4cRla7OKMHWNXbhI1+VK7TA+m2h8jHNG5PeH8xkzG5RYm1h9LPvrzhymKW30Y43XR+3mHQU/ORK+lSz50h+gZIMet6pGIpqZMavqmPqNjMlLxT7p5A1yC7krvP1eIbBOIvmz7CnDUnWMSK04RAqojhv7FtR+6RqcTqXnBZu4l8lQneorihwriVlliK/FmAZvQGJj0thjKBQHmdAeY3+4pUulVbL4fIxvjgEzTgplF38wJxPywh0BMzd2S06N0cYW8Kuw8+QgjqbcUpLdSlLXN6PTIgpz3fUKqosWdhyzcy6Ww6ptzeJ3JeKRsaXGejJBb7MmcMOoEcJFtuVhuB9YrW0QK++8O6KyoobsZB+NclrBt20inUvZTYdcWQ5XlroHmC60AxZ1S9kocr+829t0cLMhwHl4C3bKqJQ0QkBBHRKeCZRSdCRuzicoOVGyvBtzSttWKN9NGcdldUWN7Mqz2TRSeHm9S4rj1d6AbnESh9rFBOLi+XVZjMmYKCMWr+6pu0brjA+CDuR/A3GKOB3sLikjiVkfSYLh8pAhSlaPChIHALu8EPl1I2P8EsGOtSvbkdsym8uudtpDa6DedCPWUoWX8UbOJC4ZERvFu8Ictcsq9iRvr3TaIUEKUTdZxMX6hgWbeqoWBo/eINUIdTKyjgIjlpNtb3suYRdFiwzDmoHGo3Bg97ZN9rmjqJ6PMWuZy5ddLziFsaVaOLpalMOl15C5DWud1LsuoCrSpaPzRrpEiOp1U3GpJj8JG2JaSmPeE96mToq6y1b3027LHtv+fCKOCai8od804h0bYyVdbVF97azxwjLRdVc5lkPIPkZxtHOAIOFCoiV82CIbxdqH7WafbB2561VJWhdG7SPjuBnFErOqg41Pm4QQsSOqXK2aWS6Dvpmcs2u3Fg/tiCu7HC544XSyczkGORYr8do2Q0dhbRJhCcjvd7tpn8Wry/2Q3dDhcjVwK9iK5lWluTHoDZvPTie2PEPppupzjLwd+hWlUkFarhl0NLysVdGtje/jId3ski669HmIX6nbSd5Ta08ZU4+shM7zt6nXwwZHKKXTLGG+XUIBoUHnEBaVrQsTGxhbd0KQb211DNuDygJ3HzayLgZSx5zRIQWFaDicppLGuKi877rO6paBF/DTRh4peBMTUoDBQtBKaUr3YiIrG3yQGa+OYilQmzKvDd9GXW8HbajTeZsjAkGRJPm3lw8v3w7eXv7NF7vmM5r/Z8dBz1Od9/c0HueKvu19evD69O8K9tuHl9qNgVjP468m68K3I6S/O/z6+K8dIM40xud7U+/Hxc9T6NYO5/eLX+LC65q2Hr80ZfZ4YwOscLpmfhuxmV9YdcH3Xw5J3xSa7V/Wvms37Ze2/PJ2dhoX84sYvhfbrf92G74dCX548d7eEfqyxtAvfl3Nyr4d9gMd16/w6/rlz/8NZNdoMBcuAAA= -->
