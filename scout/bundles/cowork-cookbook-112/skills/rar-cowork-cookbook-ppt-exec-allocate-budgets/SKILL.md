---
name: "rar-cowork-cookbook-ppt-exec-allocate-budgets"
description: "Builds a read-only executive PowerPoint deck on allocate budgets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_allocate_budgets", "rar_sha256": "6dd14d7d6c89a7eba6954e2f3f2598421d0be1259804ff24f65c6cfaca9dd000", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_allocate_budgets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_allocate_budgets_agent.py` and in the RCI capsule.

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

Allocate budgets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on allocate budgets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets
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
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-allocate-budgets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Monthly period covered and the prior period to compare against.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_allocate_budgets_agent.py` and embedded as the fenced Python below (sha256 6dd14d7d6c89a7eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_allocate_budgets_agent.py` first:

```bash
python3 ppt_exec_allocate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_allocate_budgets_agent.py   # or on stdin
python3 ppt_exec_allocate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate budgets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on allocate budgets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_allocate_budgets',
    "version": '3.0.3',
    "display_name": 'Allocate budgets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on allocate budgets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-allocate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1c3b60e13060862c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/allocate-budgets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-allocate-budgets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-allocate-budgets-2026-05-24.pptx.', 'review_period': 'Monthly period covered and the prior period to compare against.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for allocate budgets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on allocate budgets for a 15-minute monthly review. Produce 'ppt-exec-allocate-budgets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads allocate budgets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on allocate budgets from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive allocate budgets PowerPoint deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Monthly period covered and the prior period to compare against.', 'name': 'review_period'}, {'description': 'Target .pptx filename, e.g. ppt-exec-allocate-budgets-2026-05-24.pptx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive allocate-budgets deck for a 15-minute monthly review, sourced from Dynamics 365 F&SCM without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAllocateBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAllocateBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-allocate-budgets-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Monthly period covered and the prior period to compare against.', 'type': 'string'}},
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
    print(PptExecAllocateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adPiRrbmX2He+8H2VdWrXYK60REjQAtCG5JAgKujrH1f0C48/u+TAqrK7rb79o2YL0MtSMrMs5/nnCT165vdtVFZv316M3y7WPB2lsWRXy/swltsyqGsU/BVpg74t3DLoq1jp2vLunn78Ob5jVvHVRuXBVi+7uLMaxb2ovZt72NZZNPCH323a+PeX2jl4NdaGRftwvPddFEWC8CodO3WXzidF/ptswjqMl9sp8LOY7dZ4BS5YHVt4dmtvQhKINAi80M7W/hFG7fTh8UQt9ECXGb+h8Ve231YtLVfeB8Ae+9jkNnhh4XtzqI1D1XsqgKj8bhoshjIvaiyrlk0lW+nQNeibP3mHWjkj3ZeZX7z9unnv394i8H126df39zMbsCjN61qWaAR8xJ8/ZQbLMvsIgTj1QQsWYD7yq+BxDl45PnB4nX3Y+NnwYfFf/5nOth12Pz06XOxeH0+v81/9K5YtJG/aEu7aX1v4dqV7cQZUPZ9wWSDPTVAt7arZ40WDXBEEb4/V36nVFaLv81jPz6ZvAMBf/z8VgIR7NkWn99+WgBTfn6ru/n6faZS/fjTeza758efvtNpOifx3XYmBqR+//K6f5EFE79PjYPFF0NjNy9ete/GlQ+I/06/+fMU/UXuZZIvz8k/ltWHxZ9TnvX5G5D3GWoOoPvnZIENwMq39wSE2I8vHnXZ+4VduP6PP/0VWTcCwZjFTftv0f35STgC8Q2s9TLJTx8e7vv7Anrp9o3mX7OtQMD8TzQB07+y+2aov6L98Ow/kM7iAoT8V1/+Kbk/WwD9bfHzX+r2rxZ8WASf37Z+BjK/tp3M/7T49REiP//gfX/4w99/A6T/WzJG2dXug8KX3C7iwG/aL19+/qF5PP7h7z//0FUgin07/9LV2Z/R/DO7Pvj8wYKvWT/+cS3gfyzSohyKxbccWvxaVv+r/u19cbIBlHx/3nxa/D4T5w+0mJX4yvRpgt9lYwNk/Z0df3r7DWBOAbTpnsAF8OM//mMhx25dNmXQLgy37NoFcHAb5/4svBnFzQL8nVGj9oFdmxgY9jUPxP/s4VniMlj88r/dB5h/dF9gDldV+2UG6C9fgfjLC4h/eV+YgGBZx2FcAMDVGU37XNghAN6ZWVX7jV/3AKCcqfU/gjz+OF8s4mLxy1/S/PJY/l5NvzzQOH4inb7ZzSjXdJn/PutjRX7xkt4FtehZPvzFTCpbBDEA5hnemzIDFaWddW/SOMsWXgxwBNSk6UEb2OfTTOyXX35x7Cb6XDxhGV88i1UDgwnfxFl8/Aj0CbI4jNrPhe9G5eKHX3/7YfF/Fv9q1YP4zEMDheFlfSChaKjKAmRTl4NpwDHAlQAqHtb/9beXVQGZAlQc4Ks4iP3nYhCNqe99NbEhMB8xklo4PjAtMGtelXULsH4Rt++LXbD4Ji9gOg/N1SAqm7mwziXOL9wJULWBOt8sCerbogEh1wSgbnaN/+D6i1PbDxFzkNZ2+8tC3mig9pQZ+G8W8zEJLC6LGJj/WwA8nwMi9Q/NYv2VxPtCmeNvUdm1XUW1/eIR2E+/zOX7tRwQtxeFP3wu5vLqz6Z6JMPTPGASsIz7cunH2eeg68hB5nvNV96POfZcIc1Hpaw/F80r0O16doULgB8wDbvYm+H/v14h1URll3kP+wFJZ0ovL3gvrzxikPnHtoT9syZmOzcxnzsMQYnF//eNz0NtntdZnjHZ7YJVTP3ydMfc8M1ue/aIgPtDoEfqfe9OviLQVyD+XGQxiK16+q/nzIcTX3Oe4NYBUQGs6A/6IIKAJDPdR4DPAVvXc2rYn4uviA9UWjzgDZgPGA9kyxykXxnOo18ljUDKz/ffq/8jIGpvNgYI4kXVORkIsMD3PccGDmmj2W1ffQmi3Z8TdohiN/qDVrP5QVAB+rMPY+A2UBXev6Hwc/Sr6H9Y+Gxy5iWPBrADOVo/CAA5/FnA2U2zU4F47bO/Bnp+ehABauRVO+vugCwBmj4f+rV/6+ImbmdEfNrVrwAMf5y/n5rOT/2xAokBjAXCv+qAdR8JM2NJDloYIAOISZA/eVyAkg6M8jLCg6Cdz9kP0PXVcz4pPh6/FPIfWTbXoq8LZ0XmNXN5f0a1XUy/Bwnzz8IE0MvnGQ++/xhp37jNtGegbADYAY5fR599wPuzlD97hcVXup/+aQPz4/9sj/Mozsc/BsCnRdS2VfMJhp8F9Ws9fQcwBT9lbeba+nHGgI9fc/3jK9f/QPCp66fF/0yoP5B4JcWnBfqOvCPzkPQKqtcH2GDzcX35SMyjnwvd/46egH2Zg6iaPTaBYv6t1H2dAupdWAPoAZOfpa+ZK+YAivQD64H5Pxe/j/I5y0ApKcI5Kpvyd9n/qPkg4p/e+laSwFDRAt7e3BOG/rwDe+RE4799Kros+/AGMNH/Vzuvud7kcww380YNZAvordrYf9w9IGFs58s/7lTVx4WdvQMYB/CTNb+Ps1eVmKvk79LhqR3QygUcPszYDLIchCDQbmY+p5LdgNgEYTlr0U7VLPZzkza3dQ8E//JE8H8W6A/Y/3uwf5TiR5WfQedH/z18XxwNmfvpT5l8ayz/mYMFKvxMzCs/zcXuwwtYwDfYDHxYfOvrgWqvndZjO1x0YBP787ynmG39WDJfgDXg69uibz8FOP7b3/9Mrgf6fJkj4enPf5TOBE2T3y7eQdqMi6/TPiwe6v5lKn3EEIz6iJAfMeKx8E9NArri2B/m/WZcev/MWAYhEoEAfI4vHo2D/ygVL6CNgY9fg8B6IMWrucWwwwei/QnHB0sAzYDKbLjvHvlul/Kx8ZqFA3Zsn78T/PoGgtieK/4rjF+dO5gOkOxjM/cvMEhxwBDcP5MRjP37Pf1rYRPZoLUEKynPQwmP9ih3ubJp37GpFUn4WIAHGLlaEhjqIY6PztcIEQQYEVCkS7mgnbNXnocgsyDPXP4yd2fxLMwsCbDBRwAH/vdh8Mh7afGUejbRty3ErO1LmV/fHIoAMwWi2THPzwZeoQ6M0Y4hStAZgfVxUFTkRrKqm6bWJj4Pk6HKQ4TJmJzmJ0TuGXGbGph4Ieq0kVMizLlQwPaBK8Jpf6s7MoevZn69t7S63W6muqO6moK8M2rhgnt0NOIeKjC733t61l1tgcUM95qxZ+R4qe8rts5JLD9y6j7bbmhOg2nMg/k4UcXD5gSnSAgXtr4LovVos8p+o6w5KIOH3ISDmDSEcYXy4biXi2R5vmK4rEPlsVfyVB1qwYVq/mDo7CkicyIub94ge5d7cwjuKKzpoiCJ4hhB+AaKA7w1tWjN2kfRYqsNYblX/aZoh+ak78Xzjsh2YnYs4GN3iY1DV+GKUELnIOhNnKb7gm7IIKa1Hnfw1TQGncexvM0p0RHirdHAtebuD8cOicVBhpeebpoeHLeDepiO0HaLE3BsizgN+XxV1LF4yfPiwu6u3OZMcDwU9Nh5CiqD2Ro7h7NJ4nxZD0XqhcgIt7Bh2gZ3DlV1n9zXJ1XcbAiDGjokL2m+Pi3pYkLLFXTXNKRk70tRBOaohGwXRgnQe+fphHAx1nkX+HGMiQJv7TwxT2PdacyTFFZYHagHTJO3iOF4+ml99qsTc1XhyhNqedmOdlRhiansNry1yst03OSBMjWbjaicdurtLKUccvTrY2tgV7EKtdXq1G4iFCd04pJQBllI52W100/b612OzGuvoZcjAUOXBKmC6TjZGyZV9tPElrvVGb/dJnHf5lIfLQ8aLW0OkEnud8XgLdX8mkuQMOa8Q6wHymiNEmovrn7ZR8wwaPiKiYkKziEMVGUWv5gDHesH6hTe+JVy47vTZWsVsTNkGUbfikuMFPzxvLmNBs07wulU5QfXaKIgFs7LY9ZVRrG/nu0zJQpQkfE9JE1mX4nQjl6ug3YnzHZEN9dG3Zi4jK5dJMDGCiAvql/5G2kxxlLebmt8s/Wku5HYFZeN18kNLMrzc8rt0kwrcLnSSigTw1MCI/04bNHRvG8nEVNYMoFcGDch4haQyhi6/fXkbGx4mg7x4Dk3gb3y8TYXV+ym3pXUeNjce25JB46gslwKs7qIep1XMs5lHTtpGwnmVc6vQ4UF9S7jUb0alkGl8qZvpfmQMOZaN0JZPFjYNmLl5YQdyWnLJMld8+ugiC2ww0sNweWMIcSPhAEJacxV92vur9l7c9cuBLM3WQrOLvWVJ9BDVg8G0/noRSzaLYPtCXxpa2xiaBsdNin5tHbo9XJl9AWc1lO0k07cFjb9YANNZCvjRmrSmt3h1NAub7VEXHQkuwwFoRZplSSFkOR63BvEmakBKBzXQSjiWFGOJCx3t/S+qvN+I6FulWfqZbUNmSiUyyFUtZ7mmmsT7zzej6iUXKZLnlrK5mSWzrUMKM5QFP2s9eQBuppGH2+MQOAupmPsrljBqz0NUCEdIKTNrOyAHSyV1wxGQvpAbjF/FdN2UyIsneX7At67VI2rxn47XUffYtlgKqFBFEJLyK2QziClZC9FLSZDg8iNiZauQZaicluuALzIIrytCFFKNTuxFMVNidygQbKcfdZGMbVfB5rNOUfxJLJrnIY1457XI6wvJWofua7rjTBKovWSyhJ5aJZjkheRRPFI1/TSeOLGzvZw3d9OBNXRCl3e7yF+cIjLZesVslHhUFZZXLJqNsSVwHoJ71MH3eV7q22upHZPIpbAoZK1I1anVQE5SXfCsBhTPrG0tvLXWLhaMcygCiGOyN6R1A74NVWoZdCtbgXvhElwWCeOzozNjcm49JyNjIW4fM4gh5uqaA4aH4zNKRQqVhRjdOTJvbXe6OvK0a6rTdcqQ5bcBH1NikcKNqai5TQqcqPgfNDjoSx5YxyQzKE5urOcbA+KWH3ImnilWssoqFUO6Tf7soF7k1qpd9rDXIrnj9W9TA/L/HSMj04UIDfTU6BE5tdLTjuevZqmG0QkOqy4HMyWaiQWGOeqmZ2x1SdPM3t6IHkupOWycW/V4b5pYM4a1xuOOkjnlOyEIhuRytjsECyfwpKAdsO5dxLnMKCnwKlCo5f9czIt5WJJasKSsFS7MZbSnTuC9m295vos52EO4SmtiBXuHrcsxZyYbqntjgBdTbpd6w5Kpe6oLU8EWmU8y18Rrt0c7zu/i2OS3tXFyQtNklQ2vsLT6+Q8LI9Reh+PpO3sx7sKYwp3cGDPOYSWtUci7ny8jqY0Bskgg5jENPWa7+QDBZGxdjJ2rFWckf11f9ec8ES4Jm7FV4zbGBk9rTFQIvj1tQfp4MHyuEHSXSdNGRx2fNwe5FM6EZx5Gw6YlJakJS6XTg7fSiHc2vtynazyWznG9bJQzTTOPB1sQ0hm25tJT4Lt2G1LlcO11PWtkyHxPuTuYmTsM+5+U3YRfLp3MMMON0czL3puIrv9ITypwiCrm8rfoHGPTJvCZoWLHexMLj0ytA/tl+VgNOfNpcI4f+2GScx3FFPrJ0k/d3czZ/bH3TRZPNu4fdhyaOR0VpDyg8sieq6d+ns6hVK4he2c5A6QsSncQsqc4WLQmGjzN2qvhxcrI9CY0CcntRP2Ena+jXSTaaQOwuisj4umfJSgriQDUzWaDZSGd6+yZGeCaJ3IDGlXdMBNkZ1X65MuoZElG/GRhzhyv7HWxORTyP501EaFJjfxdLPSVQZTyd6gFUaNCwFG193ImDTrukbUaffDCl1ibE5lO2F0MTzDMiLnlq0lb/yiousL3cedyVx3hwNprSTfclZny+qNO3nVmbT2O1i9I0MrmLhnmRSXTnSyhilklXJbAWf3oeU0iCIfW3MtXdWrHBocsqMUheuM+FqZeK1f9IpR7DLdu1mbCWuxg9Sc6W6VfIW2jV4QpCOi/dqISpY6VwQu9/Z0troldFvhFbY6yNmGUZwjh/rpVWOmMlNvR4G5aiulYhPRX7aatd9GJaEmWWtoCoxsGKY1QuLo9jd374CwPhMDMxxNa32VT5bcChTYwjC+tncs5cJ568AD0b6Ee3bauinEO73UHlJVHQ+uDRu8LuHawU3yzRAfcdbi0DSEGd6waP/WjOi9h1fkqNMylEpHl7hdT2I1hZv78abLx52d3SvQ91OZGZIQ3a0Uq2XFoqTvzMrPg26KnQ122zXri0KvzdjaMZZd3BgoW67TwQr38vV0JYgtZjDhkr9yW+sQCBYAFVpWVn4i9sIhiFEaxEmNSmcTJOc+ITKkpWhi6WHOCVVWgWhLOrRPBnZzxAuZYufWMfaiNWZvuJFUml7ex8J9u0Ex726u+GVz20Z79XiRaWLrG/cQg2/OuCnK01Z0jvsECsNCKZWQx5jmAsVL0rctY1WYUGSL1hhIVsG3blWgx8iiBRgjSFH1sjTkcWbHrJoKMQh8q3iHNWtpQnA1jqIQd5DTrJgCcY1CPy4nPs30wYo1NcX3q6tBpJiV4UWz8ip6GhCUIUpRFEuJrfGWmRtCnKmS2rpjmJi0WHw8GwMmLYdEQfSOs9ENtSegjLvKgWsrvO3J1w2GX1X9jtyvW68n7gJxUHDE10SyjhFmQkS7dtxNFqTiZd3vrakOatZSrYkTZSEdURKJnOk4gmuaAy1htOW77Brtb52bJzefKI+erCV9q7fnYcvS9Dra6ttttstQiQrHSg3HSG6D5J7ZkhQccTdtRaTcgmYBvWFlZ5EdFYjBcMc83pMJXCfdpVmKRLI/timCkvfLKb7U0tFyvJsSaxKSwvwhPe40MTPyjd7kPqKe132eODFSbaTT1naE5Ya7nygKYk8Uw9i06eYs7EmtUjmubrCc4DJLYtfFZbVqoet00JedOEkNTHGwG4DdWImggajt9sm+lc69ZXluLdnFckIdFZTGFd/ZTCITu4FL+93J99GwqvZr/3ZNkI1NslJiXfC1ZqnnlYb4Fc5v1Q269dAVaTkttSPMhvH23N5szpC2r6pViprexVleTxU/6UsIM6E1pZpRwddyXCPSgb26K3mbrC3H39UUQ0+dekEYF5Hq5f1Qo8F97Na3/LiVrKvVn7wRh31Y9/a6Q0MA0IXyiE1eNUHcuMGh/kLAOkGTlMbv7fCIwmfXOzD07Z7EIr8cINTkxcTQrZNQc9DlziO8g7HbOgnplbBqhZxuUJceD2S/WsIbFndkycrpHTtyw3U7lkNrLKsjgRFrO2GkqiEIuzOHsLniK8s5BFWTyTUkREYuZiEfEpfWpeSrhIdnD06P8tSUMWjRyhvG7MaTOxzLK1okR1XNBcGEtr5a7lsXZsY12ThLzGr1Q1conG1Ldd7ISbmtTnhdyVqz3HeJMSlI2rcKkXvBqTFySXCd9YGD4vutPqArKo7pGsXz+NDh5FJBW0qx6vZ6JSBB1W9a0p49lMJuuEJRJ0MvaF9QuVN9v3ZQrDnJrc5HrzgfLaWxKYpO1NJsG9S59TfZrqD9SRrFA0q5d0oeQmGq7wf0flbsW3qWaRJbWQfJO+HXBvbQza2CT+ngY/v0pl58DDr0qMgyoykGxxgMbc+rECLzcsqAuyMjUks/YvrCYAobWIi8QuvzFmq2EO7Wo40ZA6hqODNe6zoit31GNSvliiaus89Xt5WBTIGpoFYNOiNccFaUmyASDI8rGo4E7LZWN6qDOjAk9gS6u8kiub/U/jnl9iivbNgigrmdf2NunspfukHcbi+7EKL4CxIgEsmbsWfGznkZxtYR1CcWd8fgsDeOsIiPZE5V8qqRc6SN71eKdPbFpcdvegmpagZhh4Q62dym1Kog6mXWFScyNnerYSkIkIoUXOuTRy+RXKq8yOKu1cVg0pAV2GmvIq5QW0vBGeZcOGC7F7N3TDXGbKOKWiuf9xNf8TBV0RVJ2pN1Pgt6yweavreSvtPLAGJC6HxGSwKO7DiEQ0tnQEOwRjDItU8e5hfk1lybMJaVDrt2Tng81Ktm3KOII91o8rAypxps4nt0G6tFm0LJis5Wq4TfHWQYtbvzPa2XoOFvhA3fuYZopfHhZOv7GrkKGYkfIo60yfWOX6vHoe8KgVNcjjvcA0NZnmRBz7eyV7OgKUuM8oAt7fV4EScWH5XK0AfaTFbD9mbCyVlRDzJ28Htg+85MiaN29oKjELdSHcsKPkqBC+XT5mJf7of9/RaDyi1LwXagqnrfjDBCcU3U3TdqosFDkfrIDlF6fHtMAoynY5o1skHQG3I9LM+IyfuoHVXZSp+y9STcGdU56fk5z9z45lBU0qZTZ0E9b+oR6JqDqTG1tSYmDCYdknpPbOhhaapDg9/zYnWtAKpW9mnsSpq9bwtPvCpU3G3tVEi4m6C4MWZDN/suHY/qgUBp7UAK3IRu6+Ei3JWB321KEIsY5ojDhUu3EKVRLigE6S7Ze0lHDplElefYjS6i3OnwQUVpRshBzBeMK9ATWvfU2j01nb3FyO5seYFR3tTAT3oI6ehi2yPn+BST2bkvzT1e7Yv10KNlcJtKlUA13r6hqxOxIiMO79EBTYgdtzMrijiOK4H2pGRqUyttNIuw4Khd6eZGKDdZvT8zDFLUqWplR/gCin195jPeYxVsuW7J232s6uS+6cMyqUFlMwl4OjXspVKPunXYGlY5/+R3ryuELVf7IM8KvC+TGGxuzjwj1IcuvwSCut91mEMWxOEeL10TlE14zacIJxT1sJO58z7tcB86HfdXMZBv3BLvhzUnINUqas7CCU4tkjJt/eyjRqI4a7n1dNAdJdg1kbXVjc55f+xNBWGpNRTR7tGb9I0dtYzXBmF0v1nMnccKgkYkTbVCb6/ZKL2VIEhub7gs4cp+izj22NEGvVVaaXArmao4SwqqVjd6h7xhmWXL5AU7tTkuo0kFm5fRsMJrjcvyoMNO1og5KiYn5ZqUHhaFoMKmk+PaFQ0n7a4qatAiSizOe+fVAc/iWOaTHbkplg4muUqggfogeAdp5yDZkIdh5QiVulmm6lo/xp2FJfQONI6lbbDLEHdV9YLRGO+kstk4OFS5ihDU1IUtl6QEiWVAEUi/POWI1p2DvuaF5IwqeZt6qM4btsUou9V9JwSsJJUCu3a1gFSWZEDxFAO3tniuPS9cVhw13CIPuuenCqMrpcOxe6KhtrWW+4Rq2lvnTwoKwJISutSPC1QBIZHk21vk8MGl48F+ZF3roxcTWCXCduC4p9aWMO3OVAqO31QLxVHYNWFGSJuDX5XC5ipnPIoXnHuEHJ4GWy3lPPKCoUUs12GXFSNySZEzsa3QN3wzMCp+vS2pSmmxBiP7yr5ehVEfSHcUHCo3lugVhRCegcsRUbhGPh1WcbOUbkXQLNXmRrWd6JDTeQV2Rl1XNX3S0QccajEYowOt0MjWhg89bIegE18zF1xblzg9ysPdF8WWvkpSJN+S2y1vnUhtYHhXOg0M4ewRbeHtfVVdKrRQ+FI4pyR66s8q7tpocNZ2NKvxjn0KHZCkDKauIJRQIrLZD7ww7AwKGup+2jYFtNyfp6geNaJvN0bJbI/1ebDbIaeYmzSc1qe1k479Ziwr2qbiOip6q94cQh/Evra/bpWSrxikVOsKPibEZlf1V/+6deXT/VjeAzfnUaGTKlih71eGKVdjEuDJtveIlLdHUttLV0NFi3h7HQsvS6SehTirRfdlXEXYujUzREhONdZ3GQ7Dii+ZsTKtmzsAfKNH9Isvs83ybnQqDF0b1zebwbPQ4aaGMIIRlBAgPaUqYyWt57OQv719ePt+gPb2379oNR/B/D877Xke2nx9o+JxJOjb3qcHr0//hix///BWuzGQ5HmG1WRd+DoU+ocTrI9/edw3L5uebyt9Pdd9HhG3dji/r/sWF17XtPX0pSmzxxsUYIXTNfObfs38MqgLvv9wivkSez4ae5zufmnLL8/D1rf5Pbz5xQjfi4EIr9vwdZT34c17ndd+wSnyi19Xs36vk3igFv6OvONvv/1f6jTjwFotAAA= -->
