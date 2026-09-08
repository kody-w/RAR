---
name: "rar-cowork-cookbook-ppt-exec-monitor-asset-performance"
description: "Builds a read-only executive PowerPoint deck on monitor asset performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_asset_performance", "rar_sha256": "dfb9b5dbbfe663682b61aee11bf37632eaa2e318b24325f4a4caf06b29109ea0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_asset_performance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_asset_performance_agent.py` and in the RCI capsule.

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

Monitor asset performance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on monitor asset performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance
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
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-monitor-asset-performance-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period to compare the trend chart against.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_asset_performance_agent.py` and embedded as the fenced Python below (sha256 dfb9b5dbbfe66368…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_asset_performance_agent.py` first:

```bash
python3 ppt_exec_monitor_asset_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_asset_performance_agent.py   # or on stdin
python3 ppt_exec_monitor_asset_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset performance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on monitor asset performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_asset_performance',
    "version": '3.0.3',
    "display_name": 'Monitor asset performance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on monitor asset performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-asset-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f639c30c1c80af15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-performance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-monitor-asset-performance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-asset-performance-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period to compare the trend chart against.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for monitor asset performance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on monitor asset performance for a 15-minute monthly review. Produce 'ppt-exec-monitor-asset-performance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads monitor asset performance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on monitor asset performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': "Build the executive monitor asset performance deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Reporting period and prior period to compare the trend chart against.', 'name': 'review_period'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-asset-performance-2026-05-24.pptx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a monthly 15-minute executive review deck on monitor asset performance sourced from Dynamics 365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMonitorAssetPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorAssetPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-asset-performance-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period to compare the trend chart against.', 'type': 'string'}},
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
    print(PptExecMonitorAssetPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVpbnV9G8jhjbrcyUWIWyoyMGCcQqxCZAOCvS7CD2HeSp7z4X6WXarnJ1dU3MXyMvQnDv2c/vnPMuv745fReXzdvnNy1wihXjZFkSB83KKfzVsRzLJgVfZeqC/1ZeWXRN4vZd2bRvH978oPWapOqSsgDbD32S+e3KWTWB438si2xeBVPg9V0yBCu5HINGLpOiW/mBl67KYpWXRQIIrZy2DbpVFTRh2eRO4QWrsCnzFTUXTp547QrBsdXpf2rH88p3OmcVLltWESBarLIgcrJVUHRJN39YjUkXr8BlFnxYCTL3YdU1QeF/APL4H8PMiT6sHG+Rtf3wVM6pKvA4mVZtlgBNVlXWt6u2CpwUaF+UXdB+AjoGk5NXWdC+ff75Lx/eEnD99vnXNy8DUgOd5aqjgY7nlyrkoon8myJge+YUEVhXzcDGBfj9ria45QfhN6V/bIMs/LD6939PR6eJ2p8+fylW758vb8s/al+sujhYdaXTdoG/8pzKcZMMaP1pRWajM7dAya5visX8LXBREX167fyNUlmt/nN59uOLyaco6H788lYCEZzFKF/efloBy355a/rl+tNCpfrxp0/Z4rgff/qNTtu798DrFmJA6k9f33+/kwULf1uahKuvmkwf33k1gZdUASD+O/2Wz0v0d3LvJvn6WvxjWX1Y/TnlRZ//BPK+gtAFdP+cLLAB2Pn26Q6C78d3Hk0Jomfx0I8//SOyXgzCNEva7r9F9+cX4RhEPrDWu0l++vB0319W63fdvtP8x2wrEDD/iiZg+Td23w31j2g/Pfs3pLOkAKH/zZd/Su7PNqz/c/XzP9Ttv9rwYRV+eaOCDKRv47hZ8Hn16zNEfv7B/+3mD3/5KyD9T8loZd94TwpfQbolYdB2X7/+/EP7vP3DX37+oa9AFAdO/rVvsj+j+Wd2ffL5gwXfV/34x72A/7VIi3IsVt9zaPVrWf2P5q+fVoYDIOW3++3n1e8zcfmsV4sS35i+TPC7bGyBrL+z409vfwXYUwBt+heCAfz4t39bnROvKdsy7FaaV/bdCji4S/JgEV6Pk3YF/l1QowmAXdsEGPZ9HYj/xcOLxGW4+uV/eU+Y/+i9w/ymqrqvC3R/fYfor0+I/vo7iP7l00oHlMsmiZICQLBKyvKXwokAFC9cqyZog2YASOXOXfAR7Pq4XKySYvXLPyf+9UnnUzX/8sTp5IV96pFbcK/ts+DToqEZgwLw0scDdetVaoJVVnpAnjABkL0gf1tmoPp0izXaNMmylZ8AZAFs5ydtYLHPC7FffvnFddr4S/ECamT1KmztBiz4Ls7q40egWJglUdx9KQIvLlc//PrXH1b/e/Vf7XoSX3jIQNF3fwAJee0irUB+9TlYBlwFnAvA4+mPX//6bl5ApgC1CHgvCZPgtRnEZxr432ytseRHGMNXbgCMB+ybV2XTAfRfJd2nFReuvssLmC6PlvoQl+1ShJfiFxTeDKg6QJ3vlgSVb9WCIGxDUFL7Nnhy/cVtnKeIOUh0p/tldT7KoBqVGfjfIuZzEdgMXArM/z0SXvcBkeaHdnX4RuLTSloiclU5jVPFjfPOI3Reflnq+/t2QNxZFcH4pVgKb7CY6pkeL/OARcAy3rtLPy4+Bx1KDmLIb7/xfq5xlpqpP2tn86Vo30PfaRZXeKAUAKZRn/hL7P3He0i1cdln/tN+QNKF0rsX/HevPGPw/A9bGPrPOh9q6Xy+9PAWQlf/H3ZLi0VIhlFphtRpakVLunp7eWrpGxePvlpNwP4p1zMrf2tlvsHVN9T+UmQJCLtm/o/Xyqd/39e8kLAHsgLoUZ/0QXABSRa6z9hfYrlplqxxvhTfygNQZfXEQmBQABQgkZb4/cZwefpN0higwfL7t1bhGSuNvxgDxPeq6t0MxF4YBL7rABd18eLIb94FiRAsuTzGiRf/QavF/iDeAP3FqwnISFBCPn2H7NfTb6L/YeOrI1q2PLvFHqRv8yQA5AgWARc3LV4F4nWvNh3o+flJBKiRV92iuwsSCGj6uhk0Qd0nbdItYPmya1ABqP64fL80Xe4GUwVyBhgLZEbVA+s+c2mBmRz0O0AGEKUgtfKkAPUfGOXdCE+CTr4AAwDe9wb1RfF5+12h4JmAS+H6tnFRZNmz9AKv8HaK+ff4of9ZmAB6+bLiyfdvI+07t4X2gqEtwEHA8dvTV9Pw6VX3X43F6hvdz383B/34r41Kz0p+/WMAfF7FXVe1nzebV/X9Vnw/AQTbvGRtl0L8cUGFj+/Z//GZ/R9/l/1/oPxS+vPqX5PuDyTes+PzCvq0/bRdHonv0fX+AcY4fjzcPqLL0y+FGvyGsIB9mYPwWlw3g8r/vRx+WwJqYtQAEAKLX+WxXarqCAr5sx4AP3wpfh/uS7qBclNES3i25e9g4NkXgNB/ue172QKPig7w9pdOMgqW+e2ZHG3w9rnos+zDG0DJ4L8zty21KV+Cul3GPZA+wOZdEjx/PTFi6pbLP07Al+eFk30CSA/wKGt/H3jvFWWpqL/Lj5eWQDsPcPiwYDZIexCTQMuF+ZJbTguCFYi2aNPN1SL+a8RbmsInpn99YfrfC0Qt1eD3sL/AXdUvbdCzOCyp9WPwKfq0umrn009/yuF7T/r35E3QCiwU/fLzUhU/vMMM+AZzxIfV95EA6PU+pD0n6qIH8+/PyziyGPq5ZbkAe8DX903f/77gBm9/+TO5nlj0dQmHl1P/VjppwRiAwYuZP4FMml6hs1igKf3eA+Z+qv7Pk+wjvIXxj1vsI4w+Cf2pnUCXnQTj0scmpf/30qjBt9bsteIZwhW4ar7dAIKB3K+WtuQ56y/leAn/BoRA9IS+P+H7ZAwwHFTCxaa/Oes3k5XPcW4REZi4e/314dc3ENzOEgTv4f0+D4DlAPI+tksPtAEQABiC369kBc/+LyaFdwpt7IA+dfmzR+juXcx33TDAcQQnYBeHnCCAIDdEdjgCB44DBwhEuDCKwFiIOqjnhFvchffQdh84i0SvpP+6tHrJIhW234Xb/R4OUQje+n4QwqjvEziBe9gO3jp718FcbO+4v21Nk8J/V/Wl2mLH70PLYpJ3jX99c3EUrGTRliNfn+NmD7kbS3Rnnt0UW2KK8RZPo5Rf53I3d2xR764ZsCZEOJhAJA5UuVTE6WTaKtxBJJ3xcbpUQrRWeWLWEWG/O1QErfo57xE5jh04/iHr2/0FIOLWuaDjI+At5sZjuWLWnVcdK5f3M3NqUM3G1ldrrcfqbF3SqTcKzY8LrtMxYy0Omx0mrnmIvjqHU8anWuTqPIfBymBIRyY+0uXQjZZhmi5nVLvu5qZSmOChXKApskFOGJGi9LnyE9WQaSZV77STQ3dOE4gHFeqeKuUMQcupXXPDrthcIBrjcyEaC/ToOI0moIUyVFh+Vhx2zZMzpZ/wzVHfnuibcES0Wjocq20V1NsHrTn49jIlxLrHd8lOHqxmu7lMRoHs1pv1OTV2D19Y07l3g65xgsy6fUq83iuRUnXW+uU63y+RPfTXmyUozv187ziytnJvgkXiQRpqUnlRxJxYLIhOp4kI6uPsteMh7mipnXxCv7GoNoqjc/MU+h5rferBExkajjPxKp1t7kaObXOIFbfd2p+4wWEHx7ZJ9/i463LGnyoyOhRxIAqycpr7LKpN2h84CbePEJMEE91mAsJMx3AvOxSR7uHp1G1z54bufYnimX21h21/tuTGzG6X62joBqU6iSBcTqStj56YZNEds8n+8BDlFjnY6XmX66RMuPuLJzXwNbhFXV569XVHXEsFj9syN6ptXcx7+BoOZxN3WDw7lpsYO2pcSohH2dhzxTWY8n7KFHYiieFsuDcJnY5y6KN7GpNc5zQxtJ6w95zb1/wOODMaO07OUCWTuAGrBvAcquxsOFyGMx5dKQaWjpbZkY0GS9zR2kmV0amCem9F1Cw7KeosoXuU1TnbH/YpCPHUV68VLKZrJZ+d3STssgBtiJullXay3pDWLjmgHJgwxsSmlHY9h8pNYvetg4y9VOQBPmQtNkg0QmCPjanszuijNu0mvyLiprash+AOWHdhc93j8xGRp8AdIcGI2Zwb2F0iI7S/I5Cs1jeKfyjoKdw89P0hIdgTXHfoCdca8iTyUHej4azlsduuDLetzp73AuqjXoNcaCYamQMRkz2cXzYRZeWSmg7ryPGH1AgxZsrbWa2224KHYQWx+4686ol6yuKz01zOoUZeeacrbyar6HEUBIbbYxhamyjrkzl7gYbb0b1YVGSPXXCF7SyeiB090CFnsNFuI9mlndV13OlxqpdEPeIyFNAQRDFbXhijxKv0ROartT5yvtrwheH1hGJUZSJkd+7RnZvNcTqxPSRFAGzFhyj2XkH00NTPzU2N2IM5tdg6TdGSRAvuHrcdxdFZtUu4dh125wc9i1gKXbHQvq3JXMsH6jFp3Jo3BuWqpCZx3dIcPOObBmbnrJiiQ5AdUn4nbHv26PXGfUM1vN9ow1TNAg4RgqYUyryVTwHq86CRUA6BsaO6wN5WuCDvxf5UGX7KUHHnRfZeemBZPRFdpeB7DmkullsO6PAQKhNDS1ny9pE7HHcbkg2oNWxUh96F05Hw9qS5E7GHSnf98VQHFzXbXfA4OZwcWw94bEP53HwnHxJvpx1sXkgkMHvfoGBXPwysdLsp6nVDyNPeqGN+4+Hn/ZbHpWBEd9ZhY10ygvWHijGylFZggoc4hMesmbDUa8MUARFS/mWDoHW0kandVpQETj9smpw732S4TYq7fN3vdojGygFEKgcSTyyI8gYVkw7UQRrFFD2JIGDEi56qDUJoJq2d97Sd8y0lKqQQe7RajXwwkYrBj4IL7XpoB43kPkHX14N4m9M4qxOEyy3zQN3o26NQcK0OKQVpOJjUikhJSV8r3FQ9co14xknteNntouHmTRM91zO5FuZxvYWOYJfVE/XBIoNDqSpSR0Gtw/YSdGszB0rvcA11Ld/7nTBFXTlr2G0eH/0DcQGUDw1BlFCiC4qStaXsZxCdMU1BZGed98v98T4ZmlIlBgqqt6SIgeWdL/DA0BTTQJtLtlmnRLi+bfbIA9ZqIpSbE2JrV9QoiiKvsLE7Xuhzm5ibw8MfbEExDr4xdkqz59oKGTfZ+sDhUdWWa9k6ns5XIpCtdB2GarvuFfvuR+bFs+s74ioc13odiWHBIYcq9O5c0cbhk0wJh+N8IEv/eseno8k4/P48c9rokHMxsIcISXfM2R/Wzf0s17DJbiz3EMxuQpzz85nBT5kpbi4+XiQGZM11PK6zMGes4ToSFamQaelsO9G6qbp6z3FWjjXD5QLPbxWFzIpZzXtPseWLPKT1Oeaqg9VBl4dSRtz1jFsDdy5PxZnT7TGE8J7vuWCb0NPlOmx12jlCx2nt60V1GQ5yeDl2oLmG3XbWDCEm/aOZPqattWFMbT5cyFMz8e20lQcjDucbuTkJUSXQRzsVuKni3VMZm6NITrGWdFhix2jv5xwiRXUzn4W+VwqSoSVOqVkWlfrjECRpZLbuetofqfZApS2lyRF67onjmacfdOVJh4sl95yLlttKNuEqFCWeizCPOKXt7ZhN1lG6WVV40WbjQVaGmLRzG+66Yizp9VoK9etdpR/d5kaddnyCsFaPHRm+7r2tqfM1zKiERPk3iiS3eiFLrhkIKu2UtEnDD533BsZhGzjhx/NpvRWcgAdZ5GhrfcMhx5s4mLYTH3JeUGMWitnUyEcBoiucZWIDGr34uiUVAbQ6IkJfYcnZsds74aAdx50O7NbZ7LOLSlNzubllFBOc883VusF8TbfFiR5CKwkPblE+buNpZxdx3vWwYBB8nkRUOmcN5jCXaM6d+wbE11RTqWXjYWGMmN0kj4Ckswx9uHjNQIdY7FK21SWm1g+iXcdpmji4JxyEfE9aMC5QhNHu1Gy4RRHh0Y6vxKXWpYebLSEHYjwZpk3lCu1mCXu2ixMqKBJDby2ZwTJQG4NI4zfHJoHommSUsb2Q1nzKU4+NEgN3E9nUrjg/+QXd6xJFQm1WkVOziUaarRnkkNiYle8kKRMqhDxOh62imSeDPmmDxAbRoxtNqbbUcwsVVJjLyGaEi+QEtbPP96w9OsKD2inwtE98uz5kbauejjh2jAojRUYSTiIeSlup1118QiSm1feGHZyOWsTVeKwq5SmtzinPobjAOfsg021vTqHeNdJHUq0RYuTN7n4ar4OVGWJ2bw71rb5St0iArhKfXXRSGDAU9MaT1sDklEU3hMx1UI1qh4Dmm4VhvWjwMebcYTgy/ZPGPMiOO6r6HuKvTJIhu1sZivv1nrH7fQuRRBpDp4MmPmTlyvekMGFHAQnvQkZLrICSxNpkzsm0l3sQPi3yIGMI1/E7zuDlDaPyAxkxGVqC8TC1gpuNTchNZu2ehQ9VJJpX8p5QptAItRsczWNjITT0EJzelFO/PpMmcjWTBmPsvaFYD3VKjeECWsc0PzLjQDp1UaEuS5ZHh2PjqR13URTbB4PtUSKXIJVPNJsLbgZLBdzOvd/ELJda9wTadTXqHnqfT/15l8kgm3ODkNCHNlSbPWjzTxMngpb2uK86pvPEeUNwqD9rs2iWoWpYcDnvTsip7s7e3tG67jAf6LwrBTa1pqpH051WrkP9Bkvbc0zQa7g9u/drOR83wTWCEMu0Oa8rxdSRJ/z2sEEXy6W2POXC3QblMhUyO/b4cc/qHlHCct8bDCOT0iFRwKhx629k9HDykXfyh4ox/p1KKVd0jSBqGl2ySgDgnX+dJEFnNgeO1nSdP5dmsPcI3QVy84qt+u2cbUc6xqyunXHDrc9NV2Sap5OF4/HotRP6y6meEGg2y6TRBQyB7cOaPPjZeJcgieKEm9TtnSRAc+FhpQFnUmZWH9bOIaB0iNon+GPM206aBVZeU+uA76ORYEq6VGvgoqbeY1B0bTI8NNj8Jnr+mVwfUiOOirw9ZGejOjba7Yr5zjQb9Dkkrzu+vjk609g7KBOrtersvHBbCgqPmJvM7ycyvV62h4Ny4/tpQNOSWU9QbEeaC8aWqyYV6HpjQ4beyr2vsjnWJ0ec0vxxX0N3Ny8tj9qm2Vkhjs1V3iKaAsoq5QzWiTGZCkxSl2ZHWfDAZqOAIIKjEkl0ETInHR+tgQ1JhVzI/aUW93TnXYt1+VBvaDOKB6gSGccT4+pIDHqVUl0iZ2JEM/whK6NoO1jUwGz0TdU3UsQcWUgMc5O+3kVtutoIJtbc9djUkmXUvCHdWRt0BwrIVJbfmaoozI+ITAXYgh3WvHXBg82pgY84VrYcGWbClulnl5zvmq4aKmxmUE/e+s46Wop/IeJmMMtHpmyU6t7MuCmPkhnYJ89Mr84kodituaqBl+b3siaPxaTf7XVxsaEWti6DgWsAQcpHuatu3WSi6COKbnJ5SPFa6/rwUN7RKy6rqUXt1viMQAxu7Ft8DJF2Y3vssUTEfScpsjASF2Ev6Pu+OJMwNUcDU28sVi26dre7xGd3t2sevTgnZ6TwL9mxQjJZ0s0gPpqDmQezzLFa1Xazxz9MsRORG9GA74bb3A6lsONg/9LvBrrBdlldCIiIQps03tM8KaX31D9uH/U4BtfjJKmZC5BOgwjdsalreMlU6xwmCFCTIvD94I2QBt0GCGV2R2wNwTK/b8ctysqqVht+BhfnQRj8oaXGrR93kyre0QBWzofdze+rcLPhi41AXZKTMNuhDFlroaD1rBtFX9r2rZs7EMShvAaLe/OCV5iKov7x8cjOPJ5Q+A15VHtlJ1eXascKoqLQVy3ubC7ZMRR6nHX2RHqe3eO67FNqryudZfc2oRNW7lcn7LKOCFe40gKY567ieZiRnLpcsXECoD9uWX7tECjtBrnnN3zMtbtzRW6VyJqRLYYgtqHrveD1YkIxm+O2n21KqscgvauBfb0zImEZZbrBuwpqgry43DrUOI3Qbm3w10tXW6ywlVXBXDfF7ixlk35Ex4ixySQIqfECh15mb21kIvXYc2CoqGnVuu5ntNy3ewGCQj6x8Di3hPSowRsF5lAb9nHZDEzEPN9i8kFMYIK7KMNkWsLW40x84iBH4+KrTZfDIQqKwmfK24lPj5GNAuZrwiOu3XitROmhsGCQ8uebNiHnxCFrSY4pd+rFU7zjtEGbMp6VmkvYU22kXBsMG8lCsyAi3ZzKrS8XTdI7D0yBTjjjmYe62eleDpMoPihKvavGeHqcd+FxxPlSIPb7bU3xmJ8zIWttskEWK5LLRLKQL1vQ02VGwpn7jQCbazQ/FJV4sKUSf/TbYDo8zjMbuJaaN0jQdhECbU8u3wRd4J1zWdC486a5MSY1+AHl98dL20RcSMVguIZAn2ltkQzdr7HKYvDkDCYQf1uVSE2jU630klKC8i/aDY6K105VMOpuSgyV+pZ4vQzW4NwCNSdrMYlOXU+0pnQj5fy+Rs7aVF+EmY2Iy4Ur1ziPM6NPXh3bO2sgSWIsgofrnmcmwoWaXdUnRN45BMfqwyBzSX2532IkX8s7S+yvAKFSPrf6vT9fbsyFNcpeHiT/cZJOm/Np3F1gpAYd31pEKWOJqVQp64uLSArmNcO254W8t7SDQUTZhsOSYz0e9EnqAiiX8N28N5preNZqFLrHMRUUZLP2R98X0MsexnbWqKiYYV0odDPbHlfRk8ZrYgPmiP3NhV3P6w7nY/Oo7Qxi0bLcDNkYqeZYO/Rl1oO7IHGgZ0flscuNGx4rd2pNnqim3vAtqaBXD9dKsoBZXjjxdnbrcxWh6ChUC9OcvQ27V92mkm0qcA8McCCf2zUzyxTR3x7ixqmXmd/qdvjRJj0IGsUSTZW8LBTWQVDOw4v7dvLvhJ8bLOxEZsbuw2BdEeHddboHsxduSdc5iM+vqxzOUOYamh1tsuH6rqrDDqvhzNHOmAMbXQ63DWutT6c+68iH2Zd+du8f4k2XGsqsnQd797oHOfaSVMDlpIubXODtoqHda9a6d6npm8dVVRnKTr1YJKSd1DID6Me3Utuc0gGfR1VRvI66FodA2BzLmjFEVmPTLsG34pEmIsS7XG6wjsBu2mqdi6xLz0HCBrfR0ttWm2CrdXsqXxuAxq7b6l53RyFMtWEXxTmKpxqSSfcPjg3PIleyJ9NjHxthHcg+N5HhXjpla6hXArP2/Xrs1kh+rRCqlnvLfOTDXjRP5yImLA2xZF/A/W32OMlXcnLxjNnzqnqAtO5+bhGKnG0OGZ089l0PC/MKRtQgO7ksFrXZAykvJtQgW0KXyV3aKmZVskf7jDHQLiWI9Ojiu3PRS1bMyBoZ06e+V9egdaYunEpvdXQYTiPp9XcDba9r2NHDAhviPJOFAxVvHF+OnMcIFZYbNlSQsAodPCaDggQKHeoDZqMAVusLUQwFf8HHFvd9yx5IG1HZdZePMhvKqbxP7UMc4hLp+gO7UfqAOvRyokZwm4N2Z2tZhH9lT4bkIIxbyWtTsfxNeqJv0HkT2zDcbvEpbzyqGT08sZrC7ambpcj5JQkTyzFiV2acA8zs1+0YUjvulCBFO2RrjEC8xBeHPWdc4/gey6gs0qmiMKW5Sbd6LJ0PVz2utfqIcAkIelWDGyZp4mIwm6MSBRf0tBFBoSkZUIrKSxGj1ztKctUAylrocca8VfH15uz3Fw8AalOsJzZW8YTZ9IwV4JO73VJzYARz5DfyCd8/BFSEr2v+zHW72lBOOttRzF0og1My4Bhmyrs9hsYyiXAsaDS2+91DOcHb+U4hslAiG5M9bTFud4CPMKWK1kVbX8BEwW5IZbwkKbNTFJJ8+/D224Hd27/wKthydvP/7Ajpddrz7cWO51lk4Pifn7w+/ytC/eXDW+MlQKTXUVmb9dH7sdLfHJR9/OeHjMv++fWG1bfz5deRdedEy9vHb0nh923XzF/bMnu+2gF2uH27vK/YLq+0euD7Dweq74qAS8d7HhF+7cqvftJWZbtwS4rlnY3AT5zu28/o/fDww5v//j7RVwTHvgZNtaj6/m4A0BD5tP2EvP31/wDaXFRSPC4AAA== -->
