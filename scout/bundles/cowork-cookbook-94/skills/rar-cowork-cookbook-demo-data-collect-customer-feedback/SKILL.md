---
name: "rar-cowork-cookbook-demo-data-collect-customer-feedback"
description: "Generates 25 realistic customer-feedback demo records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_collect_customer_feedback", "rar_sha256": "b95b716385bc39d7eae26bb4cc7bfcdab7387baf935c05837d2f148daa619b84", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_collect_customer_feedback`. The original RAPP
agent is preserved byte-for-byte in `demo_data_collect_customer_feedback_agent.py` and in the RCI capsule.

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

Collect customer feedback Demo Data Generator — Generates 25 realistic customer-feedback demo records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-collect-customer-feedback
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
    "record_count": {
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-collect-customer-feedback-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_collect_customer_feedback_agent.py` and embedded as the fenced Python below (sha256 b95b716385bc39d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_collect_customer_feedback_agent.py` first:

```bash
python3 demo_data_collect_customer_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_collect_customer_feedback_agent.py   # or on stdin
python3 demo_data_collect_customer_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect customer feedback Demo Data Generator — Generates 25 realistic customer-feedback demo records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-collect-customer-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_collect_customer_feedback',
    "version": '3.0.3',
    "display_name": 'Collect customer feedback Demo Data Generator',
    "description": "Generates 25 realistic customer-feedback demo records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-collect-customer-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-collect-customer-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f7dcb0487ee102a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collect-customer-feedback'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-collect-customer-feedback', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-collect-customer-feedback-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic collect customer feedback data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for collect customer feedback. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-collect-customer-feedback-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic collect customer feedback records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic customer-feedback demo records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo customer feedback records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-collect-customer-feedback-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training or pilot customer feedback data created in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataCollectCustomerFeedback(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCollectCustomerFeedback'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-collect-customer-feedback-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataCollectCustomerFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916aZOjVrrmX9Hk/WD7qiqRhNjqRkcMQggkAWIVCFdHmR3Evi+e/u9zkJRlu9t9p3tiPk06XCnBOe/+Ps97En59s9omzKu3L2+KZ2ULxkqSKPSqhZW5Cyrv8yoGv/LYBv8vnDxrqshum7yq3z69uV7tVFHRRHkGtjNe5lVW49WLDbKoPCuJ6iZyFk5bN3nqVZ99z3Nty4kXrpfmYIGTV269sAIryupmYS1qoNHOh8UeRpFF4gVWsvCyJmrGxY+u51tt0iw0hT/89GlRN1YA1DShly6iDGx1gVp3QQ+Olyxmi2djPy0cYETzWvfp4U/lNW2V1QvPcsJF5vUvK36oF0UVpVY1LmJvfAeeeYOVFolXv335+a+f3iLw+e3Lr29OYtXg0tseOLC3GovKk8RzGurl4eHlINifWFkAFhYjCG0Gvhde5edVCi4BVxavbz/WXuJ/Wvznf8a9VQX1T1++ZovXz9e3+T+5zWbjF01u1bODjlVYdpSAkLwvyKS3xvq7RyB8IDNZ8P7c+ZukvFj8Zb7341PJe+A1P359y4s5VSBvX99+WuQV0Fe18+f3WUrx40/vSd571Y8//Sanbu078HUWBqx+//b6/hILFv62NPIX3xSRpl66QIyjwgPCf+ff/PM0/SXuFZJvz8U/5sWnxZ9Lnv35C7D3WXs2kPvnYkEMwM6393seZT++dFR552VW5ng//vTPxDqh58Rz5f5Lcn9+Cg49ywXReoUEFOicgr8uli/fvsv852oLUDD/jidg+Ye674H6Z7Ifmf070UmUgcb4yOWfivuzDcu/LH7+p779dxs+LfyvoG2SqAN1Zyfel8WvjxL5+Qf3t4s//PVvQPT/UYySt5XzkPAttbLI9+rm27eff6gfl3/4688/tAWoYs9Kv7VV8mcy/yyuDz1/iOBr1Y9/3Av0a1mc5X22+N5Di1/z4n9Uf3tfXAHmub9dr78sft+J889yMTvxofQZgt91Yw1s/V0cf3r7GwAfgI5V6zxuA/z4j/9Y8JFT5XXuNwvFydtmARLcRKk3G6+GUb2IHpAHHABxrSMQ2Nc6UP9zhmeLc3/xy/90Huj+2XmhOzTj8jcApdY35wls3z6w+9sHdv/yvlCB6LyKgigDAC2Tovg1A2icNbPaovJqr+oAVNlj430GHf15/jCD9C//gvRvD0HvxfjLA62jJ/rJ1HFGvrpNvPfZRz30spdHDiAsb/CcFuhIcgcY5EcAtT8B3+s86QByzvGo4yhJFm4EsAUQ1/hkgjb7Mgv75ZdfbKsOv2ZPqIYXT0arIbDguzmLz5+BZ34SBWHzNfOcMF/88Ovfflj8r8V/t+shfNYhAtZ4ZQRYeFIuwgJ0WJuCZSBZIL0APh4Z+fVvr/gCMYBLFyB/kR89GWzuhNhzP4KtsOTnDYIubA8EGQQ4LfKqAfi/iJr3xdFffLcXKJ1vzQwR5oBnXa/wMtfLnBFItYA73yOZ5Q3g4Caq/fHToq29h9Zf7OrBz14KWt1qflnwlAj4KE/AP7OZj0Vgc55FIPzfS+F5HQipALfuPkS8L4S5JheFVVlFWFkvHb71zAvgoY/tQLg1E/TXbOZebw7Vo0Ge4QnmSQOMFs+Ufp5zDkaTFKCBW3/oDl7TiLtQH+xZfc3qV/FblfcgfmDKuAjayJ0p4b9eJVWHeZu4j/gBS2dJryy4r6w8avDF/N+Hm8X34WaeDRbzcLB4zUMzu7ab1Xq7+P9mQJojQDKMTDOkSu8XtKDKt2dm5gFxzuBzppxNA+X57MLfhpcPgPrA6a9ZEoEyq8b/eq585PO15ol9bQWsl0n5IR+EYw44kPuo9bl2q2ruEutr9kEIwJvFA/1AugEwgMaZ6/VD4Xz3w9IQdP/8/bfh4OXzHA9Qz4uitROQpe/JacJq7tdXTkHhe3Pv9mEEIvZ7r+bcgHgB+QtgRAQ6EJDG+3eQft79MP0PG58z0LzlMR+2oF2rhwBghzcbOGeqjxqAWlbznMeBn18eQoAbadHMvtugYYCnz4te5ZVtVEfNDI7PuHoFwObP8++np/NVbyhAVYNggU4oWhDdR+/MsJKCCQfYAEoTtFIaZc/SfQXhIdBKZyAAQPuqoafEx+WXQ96j4Waq+tg4OzLvmdl/4QPTwZXx93ih/lmZAHnpvOKh9+8r7bu2WfaMmTXAPaDx4+5zTHh/Mv1zlFh8yP3yDweeH/+9M9GDu7U/FsCXRdg0Rf0Fgp58+0G37wCxoKet9YN6P8/k+PlFjp//ARX+IPrp9ZfFv2feH0S82uPLYv2+el/Nt7hXeb1+QDSoz7vb5+1892sme79BKlCfp6C+5tyNgOu/89/HEkCCQQUQCix+8mE902gPmPtBACARX7Pf1/vcb4BfsmCuzzr/HQ48BgFQ+8+8fecpcCtrgG53Hh4Dbz6zPbqj9t6+ZG2SfHrLQOX9S2e1mY3Suazr+YwHGghMY03kPb49UGJo5o9/POxeHh+s5B0APkCkpP596b04ZObQ33XI003gngM0fHpAcj1zHnBzVj53l1WDcgWVOrvTjMVs//NYNw+CD8T/9kT8fzRI+afkAICvBw0yHyP/jij+a5GCcCzmgNoP6HCfc+afqv8+pP6jbh1MBrN0N/8yk+SnFwqB3+BgAWjm44wAnH6d2h5n7KwFB+Kf5/PJnIXHlvkD2AN+fd/0/e8Mtvf21z+x6xlWMFSCKfgfTRPa1AYFBxD6D6QKjP0o1d9iskF++lPPPwjz27Ok/l7Fk1Vnyp2B8lG088JPC+89eF/8C539ebPaoJ9XyOfN9n1I6uFPjHj4CRAc8OAcst9y8VtE8sfxbbYXRLB5/rXh1zdQ2Nas/VXar/kfLAeA97meJx4I9D9QCL4/OxXc+785GbxE1KEFxlIgwyYQG1ujMI7YDky4mGd5G9S2t46D2b7jWjYG45ht+QSMOCsEhzF346+3uGtZ6Jqw8S2Q92z5b/NkF81mzTaBaHwGqOH9dhtccl/+PO2fg/X9IDL7/XLr1zcb3YKV7LY+ks8fClqubW8D2SNnQAZCRFzQOEqZ0KZ9sbHbdXQw5oJJ0i4N/NoWndagmXA8sbSgXceLJbm9upf2xEHc0JACT/HUI06+WaU2XFlbsO2E8KPJL/3hssXNy3Y7XWjsrpPWgaKLa3FozQjRta17FLlaP8FnOxooAse1POU7jxN2LrR0Lz6mLIvhdMmOhbtkz3FERTkVbwtSIeWRsWSkPCoQUQr0wTkaYwxRpl+cMnbCoCsvj5jmU0isaTat9muqhfbHdjhCmb1GL0N8vEJhxR12LXK4MlSpMPreMYpitWe290rgELfw7rFOmkE+cdFAslqtFzKS5+oq2K6PCGeEfaJFI3ppsiVEF+6ABDgrl2s3K9DlRSxGLxIuMIsjS6JW2Lss79JQDRQxTGotmW7peKhkz1aOGTlBQ3IQLlO0czTTup0rDncHgR53y2vmtWQZlZobBIeEPNrksslkxrywHH3Xjrv6mmWBgPsNwqa0CKX76kQczmVwxOirM17XjBXtA4G7M5hy7hL0DCfO8lLtffiCd/L5lG0VhRP8uNbICW+SPXm9elG8yXfUyBX8KlZObuQ1wo6O18SKRwNzIPUttSv5PetKZ9m39i5qeDpC3FbVbkjiyD56e003Ze6cnb39Tkvr2EDbfHOc8GMd3REzCST4kpL2Ft7cDrZRFYeB2ZQ76GyIiCVHJRXVLpPdzzbHOuqylZpVLCLnG29Kq7DQdSkJxTwkdMYYr0UNmfttoMY63xBMpJrG5r5SccyX2h3ErtOAWV8v00FKGTc48oqJ0JAgbP0+FiqcHLN2oiNkEvQNuqYMvSErZSMcKQMTimsjn+V7KcZaHgviOUFL4jjuRznmcAnxB11H494plhK7pO8m46i9IZYnjzSWebCi1UHBJDysdXFXVLEVLHXBBpU/nG8FP1m2GlAOYxZboxDawkxkYbS1DKdNiE7veHoZER+5jHB34P0dMqlSxdAbO2KWy4EYws5PIX70x/3puM04GPX8o2cE0wURwuC6ari5pehz054QDc2Px+UoxXATH3XIaF3yKE3MFQ9Jz40v+5w19JOk8UxgCVhyrUVGFa7pXQk7T23qUCL8MshB+q/5Mby6p8Ay9tRF1bUzv1/vVvWhscVD3w2G0PPW7nKhgl3Y3XlVbZFsc1PNVOfYKYkgdUPp3qVb5gdtqu0i9JXhyPbt/b41rgPOlf2kre6Ucpo4T0Jsf+PJUcGJJkxhHWP2OhPld23baNxFxDe5cyylXT1Gnj+pQnberfty4pA+HxWaFjlXKrVBQkns0KLj9RhwSrQhQ5JeombMyH6ho2a4PJ8Sv5d4fSdjp5QeuSy+nSSz54+bSYESZE/ezGV7FMZ8RTZHHj1MewG2m+DMs6iL3DtLZ4TL4FtdoeGDvT7Q8d0Rz0KkUyZ2I6VJbq8Sl14nGWqtq6hLCq2QJ5ry89bn94xvrlCrzlcClqZnBqK9ZYVf9NN9tDacczxa0WrZ12LgqIlGdpBDTXdpPYkbXYz8o307cNLWuF8jZ41R5EG5qZdD01PuaXlgWmuczmepL+CbjDZUDW1PXD2lgrMs600QBD0OIZThJCO0WvKGZgWHtX9SXZhwMH3boMvY1L3bsLf7fWa2asX2+jnCDOGC72JhhUEQkogjnxNnwASUzBDLWzCFpZYU5GF5wmCZEizZgFFJCLKdyVOGWls9Nbhb4WLeq3oT384Cu1tyhwnnOOrMWK2YMY1BrGjXk+KUsyipOSKrc0HR9hrpDHYaXbhI64g8HKKtvQuFYQvT6+x8vMrq2VO7tWyuBHQ8tcXRPApHh7pTsdyeur1q7hym1n3H5Pb56YYmBrk/cRiLqlrel9ABTqSYhLVbzKDZzUYT5E4Y3MlKTLLjtF13SYaxH9NxCl01yvapjy0Jny02kKAGReOYUbahrhPClwWdQyRUaCkKW6J025qxd+UxuGsOpC+0DGxLciiN5YUwur7dI57YQW0Daxk2LY9Jh/EF70TlESlSn6puAbkrYgXZinaCobV5pkviUB4k/SjfG7gJIIp3ZW3jOZTBw7SOqq7H8Q21LRimUYStxA1bm5TvVtV7wRnPwp2HwiGZ64xcENRdQVk6PJ5OpOdMub73GDoIEZzaln7qpAe39JpwQNBBqsvycJfNll4bzjLbDCMeYUzJVE5n8Nxkr8rCM3YoySpUfFQPa8bRRqzN2PXx5N7vGRkm1LVLgguU5PwVwXUB7R0HnDi6qdC2zDrslYAxXA/XoRbGD8FldQwul3vfbrUrXbIFjJU4Z202y+0uJjdXhTrAaLlsy6qPpTpay1KXr4ewnEgFs3QoKYNNyd1u+RRNK30wyeREKWkfaOM1u5RYCEEGwyHk7eDa6/VwMDkyKqyNlOwrgjmC40lEBF282d1R/kBrW8XijqWcm1vDlKPkluZqeo63+35HkeTVPZh5SWSlOuR961B9faOCYXnYU8bBWyt9cPWGAxfEkJ4I8bRW+d3y4KjnIY8Om4HPz3A8SJmSbiOmKBtKuyCZ52q11iDjZQh4iVUZB9bMohBhOd2CU/pGR/LrVrotLyifkH2EkogOKfVxSjaYvE2lY6hCvLOWEnWVl/kJ70uSZqmzfOOSI3TcHD20PRs3UTbt3S4YizVNgGqT6SPwm9tkd2hjuNGR2ZyhW7K/edQSWfcbukbLI2M6vZhs0m26HkTdITlRnQwwFtKxuuvZ/OxwuthVblrFe9HZw1eZjEsOh7xsGLwL22J8tmJPSXc4peWesazlzrqE42a7Y2yXkwBw9QCudPV4DFwZDdR+ech1RW/K3qCt204/i1Fm2TckUOxu7wZcGaZOt3LO5nBgBqHcWmdnvcl4j8CPzSQMt2S0VK9KfGTrd8NhKVFUEYyTgYQxvmfidKCGkdlPsjXwg1Efk9HLTA+lZXJdZ0W/LqB97fbXwzoI+XU5mdkybK76bUmqazLak5wCnWlLAp2bHioj4VZly0AU1EHDiYTPnJyilGmqmULwIsHZ7jbGR43lbktlr6DbSKmQk1hHdXu08iQ7I5GYsc7qlmdaYt9AmcZcuToPq0C6Hos4LRjDRyTLTjWmUQlYWFrkmbrzGzhjZc/z2zGUqU1ZCchNGM4+3cTENvavS4JJyOFckrtRaHWF7jxrxauRmpeWXI3b63gzECQotLCvL37rsONaJFFYuzgo3WFXbp26QXQLmQ05hiecYU+SE0+kLPFHj85pApM28BnbnTlKveYHPg8tzlW1bOpdXlrbGEizpMmrvdYf+HutHTTeas8KTNTSvm+xePT4DF7hnois8KWDYYdzI2ZZY++MRg8s9NyoJ9tV2aosi7KCxi3CqZhwRDeafuQcj05LnXQGDtlmS0WoknBcrwVYubXOra9HM96hHJ/xmyNJ78+sxOEB75oUqQluzAaKqpvlNaLaFY5VEHkgVatwA9tDGJYZVvyB7437zg6S7BJvNl7X7MFQBOWyanp00MBy3G0qzTZ7o0KlaMR3EJw2MrGfJryM761slbCeHjzYq1ERLlDgoAe5sIucy6ZrTMHq6sNpiBjBa0/scItN9cRZzWaUvRxr8SJf7tLkMMQUc97k5EoCZH7YbUn5FF12/m4QCjGP9zZreD7amuqqjTHRum+xrDTPa9TpsgF2ywK7hmTsIjd1hZ/K7QkcLbQ4rM/91eEbPqcreX064VdAsHgJbxj5bK87kDkFGlYEa24ItzOQZLVaUrltMYNMmZpLcGiTCKx1o/RIR/11ULa5hSY3+FZyuWhyApFszseBT9YevxRgJqST8pKgrNa1sEmO7iY1j7irjAFXeatS1GPkzHgCCzmiHYbEWmnHiSdLUqxxNF47MuRYq02ybFQu7nCyCS83R5TJgk9Kmve88i6POBhMDxeXvi4l3qEv0T3nU4mPrvaqh3v4eD2kyyKD0R2LaTEt1NLxuh50WgUxvkbasUEbsxVviOnXXHF2w/GOtetmbdz6fRXHh+PpcL1Zvhzv0VOwNm+Jq6posTyWeHX1Nl3Zb3X6MJBbQ9miGjgrcRq9JYe0GtfntUcTFNKWY7us7bZb+34K5hh1OlQS6KXGNj3BoPgG3t1QcEPnrjaTeb18v6B5dFb2uGctuf3aJfEbUhYryK11nMAhH6MLeWzk4G7Uld8n0W2VwHGpLPMQCm9KVhs91mE5gCDjemwFj0e9VBCNPDYMZbnhUXMpM4JMnbc3zkyNEyrhPdXCai4WFG9ddGaTACJwbU1fVvecWOnQ/XaVPbQAI7VimgLEY3sR7SZ7SW3vK5HY4/0hv7bGeJiKPII2iWZvW3lfsm1g9aXSJVnJSrmNHuw7J/Fy6eZFum/Syx03XWbrXFBKp1Fqi92DI9c627Ha5zQShPY61ZRsvVSHQBc6ChXlOo02Z2LAdJZnQyi/CeiqDadNVzGRuEFxwHSYwBMMR9QN4m7sKuPoqfaZ9rKFKrnK2fyQs5fmilmRLfW6cW4zg1mC+fRkmkjuLKe0MTI2GAhMrzThjqyKrUK0ySXwM5jElkx4bjGMEaNTeyc0pNSmMZxYwo6PVETR+rXrb1Cbwhc3Oe1BKjerK8Htb2dbhLiGKUwkaU/+VqQS2VVTBKuEu34x+lTfpDU6okJqe+sRcW4iGKs4ZS/DzYYJCJYkjncIbx1oa0O3cR/cL8QNgkZjKWz2as/BBXRAvCWUWIJHqdIOP7G9kea6yBy7ZLqIbcRhVTgRhJRJ7qVYd3yiBOSBBq3cHr0wIHZODMZQIPcOKeZem//mdThPyNSU13tWQFWTi5f+IOGbVbAMNW7V9XC6v0hIN5zCZb/dxxDrKVHYuXsPo3s/bhgt0PNpQljUw7C6HOIpiKYUCulpapo6lQCR7+PaqliSJVo7uhGrzCfO4TogKHPCqihPWTHbNmdwEFJySL8XJ9m/TgTKDMhIg5OXtAqYgg48UZzASf6aFLgDD7R6XBOmdcd2EVqNciUE03m9sjkHgkOgSpe1m5eLjNupRyLDVucKOvDB1lxyjCcaYrqt/OjWakfnxruosuVKLVJTEr+oLCHuEDdMtVpCd9meOJ9slRgkK61yucvzzIrv1/uO2W9XhUPeOGsn+sLe4jN/33DU5iQRnbnDUS9h9kl3dldTsUOh2h9xwHXqNImrNZ5bUX83z6oj4VkNB0rW0FuxtorG4++7jtyKOIoWYGAQQuw81GY3pT5tTMmBLDYnHAx0fnaXV+7IglHx1jvB1uJKk710ArIao+oyDdhS17yem6zULBH9Duwj3J0+3mAwobT8pMXDLvFcybox43UrLPNjiXZkiHqX7BZXCBYtKXzKdFs43yAdOZzC6dJcGMI+8IJ1GLRGSFvZFHyzcpKI22sXsU4ubJ6nRr52ao/HHEBV2gH2FVcwbjw17iCCRU75Rr7Rcirsurnb0dyIvBBi5PJgw9Te63dFAvuBwzEEaq1t1L6UaSa0AOKmSoTV2GDFTp0gK3GncIOudvyAb6qOvIcwdlkX4eVcZVDp4EOa4ZsNccU8dxBXcFCvE2vFHDwUVW3vukYNeq1mYtFX+z6BSCyzyKgj0HhMBsFOeh+r9NJ3lHxVGUxtHOgCCYgTbt+HBG6mFi4DONU6TRyXGuuZEblRhJSvKPdIOCdUWHKWpJIlZK1MV15amg8aQroyPVcAblL97EDFvllCe5xDQutS0PzNH3cSinajTee30kGV/WU6wm3FN/iY66qHnY49Sou4EG2nan/A9bRdyZtOy4YmsDnjfBkvsrdOeWD31eB970yIhrTPOTS/7ER4R5/Kk7bbCEuKZcoZIWv/3km5s17SfU5kUF0EbgRZTXSGJirGGSa221U7TZhCsGeV10eYWhYDqUBs2qSJbTkW0nGs0uSwqbeeGF0P53FDCd5wT0du6wiVqOdn+3SnTYIaedaFCj6FRA2MdY7imeidqBRZmOIDpO+4oLyHcX8pKjAocJ67vNzYuEG8Wr4rxgjG2krDT6TBgqNtAeNrNtQ0uLGlQqT8br9PhXyZp3gRXe86sZ5aBiMMSRyLSYKnQsbBOGMQxhizHazs8A10vyZm1ai7lZJGqqagNnwkTUji08jhmhGCEGOihxW+EpbSSoIpZk0h1mktYswGDApqRl+6Frnal9jOV6XUe8ba5twbRGHJoLDrnpA4pkNVCbuXMTZmFhPKDROWgWzYd2at23hOpEy6rrtbx+9j2HYDxDa6Ghp5nu2U3clOyds5HmLb8Fx9IoWmqpfe9mCxvBfsyJvoOOFyp3D7y1GmVypSdYeAdNr7ddvFy42l+h0hsxJ/EfZHFduiPrlO0+zSpphBLSM2zpE0QtlSM3qvFNCpbwgdDHKCf9Gd9d47o2U5ebbfsd1mXYWGg+ANxAuOULaDz8B7zIq5LgjcAR8Z0lJuYotdXadIJOcqrSvnKqTdmt03MNHflvea3V7ETZdd6nW5DiKcbSceRXTsrjdEORn7jubwcVJqVUVSujqwd8hWePZi6aLsCaUJBmB/qSaGwbJjeB/ELS8wypHcA0pChVUvu6RM41dNlw6ob7hs1W/P5zYyvKY5keqwPnRj6kTWvg5tS4mCrcMiknAy9zxKIEcs2fnNymu6ibvJVYv5hALp8VbztkWDDcW6dRRI6Fdsso9z1sImr5OmlipiUbLvSCYr5bG8uaShIQiPwShSsoNLQPust+J90x/ODsRuraV1EuQ6CW6FT/tKgHXthu7xaDhfyZpYQ1uU6forn9tdshsokiT/8vbpbX749Xru+u+87jU/zPl/9tzo+fjn42WOxwNGz3K/PHR9+bes+uunt8qJgE3PJ2R10gavB01/93zs87/wkG8WMD7fo/p4pvx8Tt1Ywfya8VuUuWBPNX6r8+TxQgfYYbf1/F5iPb+66oDfv39O+t2VWbJXdZHjfWvAlef7lG/zi4PzqxqeG1mN9/oavJ4agt2gswFe1N9A+r95VTE7+3ojAPgIv6/e4be//W95nCz7HC4AAA== -->
