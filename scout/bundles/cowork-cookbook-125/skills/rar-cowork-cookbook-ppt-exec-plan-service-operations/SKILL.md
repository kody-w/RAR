---
name: "rar-cowork-cookbook-ppt-exec-plan-service-operations"
description: "Builds a read-only executive PowerPoint deck on plan service operations from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_service_operations", "rar_sha256": "c2d789719ef63e8271b7505ae43f6a2e188c03dfdeb029c06875e3f40e76aa4b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_service_operations`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_service_operations_agent.py` and in the RCI capsule.

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

Plan service operations Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan service operations from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-operations
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
    "comparison_period": {
      "description": "Prior period to compare trends against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-plan-service-operations-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_service_operations_agent.py` and embedded as the fenced Python below (sha256 c2d789719ef63e82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_service_operations_agent.py` first:

```bash
python3 ppt_exec_plan_service_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_service_operations_agent.py   # or on stdin
python3 ppt_exec_plan_service_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service operations Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan service operations from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_service_operations',
    "version": '3.0.3',
    "display_name": 'Plan service operations Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on plan service operations from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-plan-service-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-service-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '97145fc1efdce144',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-service-operations'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-plan-service-operations', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare trends against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-service-operations-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for plan service operations reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on plan service operations for a 15-minute monthly review. Produce 'ppt-exec-plan-service-operations-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan service operations data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on plan service operations from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on plan service operations for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-service-operations-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare trends against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX summarizing plan service operations status from D365 ERP for a monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPlanServiceOperations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanServiceOperations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare trends against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-service-operations-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecPlanServiceOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObSLrmX9GcGzFVdbEPO0ie6IiRBEIgECBWqdzhYgexbwJU0/99Ekl2ubrdt29HzKdRRVkCMt981+d58yS/vzl9F5fN26c3LXCKBedkWRIHzcIp/MW2HMomBV9l6oL/F15ZdE3i9l3ZtG8f3vyg9Zqk6pKyANM3fZL57cJZNIHjfyyLbFoEY+D1XXILFko5BI1SJkW38AMvXZTFosrAcm3Q3BIvWJRV0DizoHYRNmW+YKbCyROvXeAUudj9T20rLXyncxZhCTRbREBksciCyMkWQdEl3fRhMSRdvDgo/IdF1wSF/2GRtG0ftB8WjveUOxvkVBV4loyLNkuA9kCHvl20VeCkwOKi7IL2HdgVjE5eZUH79unXv354S8Dvt0+/v3mZ04Jbb0rVscAuBaivPbWXvykPJoPbERhVTcCrBbgGz4DSObjlB+HidfVzG2Thh8V//mc6OE3U/vLpc7F4fT6/zf+d+mLRxcGiK522C/yF51SOm2TA0vfFOhucqQVu7vpmtmvRgqAU0ftz5h+Symrxl/nZz89F3qOg+/nz2zdPf377ZQG8+fmt6eff77OU6udf3rM5VD//8oectnevgdfNwoDW719e1y+xYOAfQ5Nw8UVT2O1rrSbwkioAwr+zb/48VX+Je7nky3Pwz2X1YfFjybM9fwH6PtPOBXJ/LBb4AMx8e7+CdPv5tUZTgoxxCi/4+Zd/JtaLQWJmSdv9t+T++hQcg1wH3nq55JcPj/D9dQG9bPsm858vO5fBv2MJGP51uW+O+meyH5H9O9FZUoDE/xrLH4r70QToL4tf/6lt/9WED4vw8xsTZKBkG8fNgk+L3x8p8utP/h83f/rr34DofylGK/vGe0j4kjtFEgZt9+XLrz+1j9s//fXXn/oKZHHg5F/6JvuRzB/59bHOnzz4GvXzn+eC9Y0iLcqh+AOtFr+X1f9o/va+MB0AKN+h2KfF95U4f6DFbMTXRZ8u+K4aW6Drd3785e1vAHkKYE3/hC+AH//xHwsp8ZqyLcNuoXll3y1AgLskD2bl9ThpAeY9UKMJgF/bBDj2NQ7k/xzhWeMyXPz2v70HsH/0XsAOV1X3ZQbrRz58eYHylz+U++19oQO5ZZNESQFA97RWlM+FEwHwndesmmCeA3DKnbrgIyjnj/OPRVIsfvtXor88pLxX028PhE6euHfa8jPmtX0WvM/WWTEA/KctHqCNJ7EEi6z0gDZhks1AD5QoM8A13eyJNk2ybOEnAFUAW00P2cBbn2Zhv/32m+u08efiCdL44kljLQwGfFNn8fEjMCvMkijuPheBF5eLn37/20+L/7P4r2Y9hM9rKIAsXrEAGgqafFyA2upzMAyECQQWAMcjFr//7eVcIKYALAQil4RJ8JwMcjMN/K+e1vbrjxhJLdwAeBh4N6/KpgPIv0i69wUfLr7pCxadH83cEJftTLkz7QWFNwGpDjDnmycB5y1aEIg2BBTat8Fj1d/cxnmomIMid7rfFtJWAUxUZuCfWc3HIDC5LBLg/m958LwPhDQ/tYvNVxHvi+OcjYvKaZwqbpzXGqHzjMvM56/pQLizKILhczFTbjC76pEiT/eAQcAz3iukH+eYg34kBzjgt1/XfoxxZr7UH7zZfC7aV9o7zRwKD9AAWDTqE38mg//1Sqk2LvvMf/gPaDpLekXBf0XlkYPKP2lY2B91Oczc5XzuMQQlFv+fdEazD9Ycd2K5tc4yC/aon87P2Mx94RzDZysJFn1o86jDPxqXr+D0FaM/F1kCEq2Z/tdz5COirzFP3OsbEIDT+vSQD9IJaDLLfWT7nL1NM9eJ87n4SgbApMUD+YATATSA0pkz9uuC89Ovmsag/ufrPxqDR3Y0/uwMkNGLqnczkG1hEPiuA8LSxXPwvkYUpH4wV+8QJ178J6tmr4MMA/LnSCagBgFhvH8D6OfTr6r/aeKz/5mnPHrDHhRs8xAA9AhmBecwzbEE6nXPNhzY+ekhBJiRV91suwtyBVj6vBk0Qd0nbdLN0X76NagANH+cv5+WzneDsQJVApwFaqHqgXcf1TMDSw66G6ADyExQTHlSALYHTnk54SHQyWcoAFD7akefEh+3XwYFj5KbaerrxNmQec7M/M+kdorpe8TQf5QmQF4+j3is+/eZ9m21WfaMmi1APrDi16fPFuH9yfLPNmLxVe6nf9jn/PzvbYUevG38OQE+LeKuq9pPMPzk2q9U+w4wC37q2s60+3FGgo9zxX98VfzH73qC7+U+Tf60+Pd0+5OIV218WqDvyDsyPxJfufX6AFdsP27OH4n56efiFPyBqGD5MgdqzYGbAM9/o7+vQwAHRg0AHjD4SYftzKIDIO4H/oMofC6+T/a52AC9FNGcnG35HQg8+gCQ+M+gfaMp8KjowNr+3DVGwbxTe5RGG7x9Kvos+/AGkDH41zu0mYnyOaHbeVsHSgc87JLgcQWiAx4nbVnM+5Kk9Oebf97nKuB2s3g+neHlOSV4giuAo+iRxrN23VTN6jy3Z3ND90CfsftHmfLjh5O9A94ASJe136f0i51mdv6u8p4eBJ7zgP4fZg4AgAIUAx6cTZur1mlBGYAK+KEuD4748uSIf1SImdnlexp5UP+jqwC49mERvEfvC0OTdj+U/S2D/1GwBRqKWZZffpq59cMLuj48SO/D4tumAlj02uY9duRFD3bQv84bmjmAjynzDzAHfH2b9O1vEm7w9tcf6fXAty9zkj1T5e+1O864BXB9dvA7qM7xmZBAX7Cm33vBy/J/VbgfMQSjPiLkR4x4iPmhl0CXngTDF6BL1MX/qIv4uA/Pe2PgspdSzzmPn49uIe9Bexcm3UsvlPwIUHrujHOQanE2vSb8YP2HAoAdAMfOnv0jZH84rnxsC2dVgZnd868Yv7+B0nHmjuNVPK99BRgOwPRjO/dTMIAXsCC4fgIBePZv7zhe89vYAR0vEOBhPr1c0egqCCk8WGI06tIkQjoBgYeUgwXocukhuB/6gYtgKw+hljQZ4CGBBDTlOIQL5D3h5MvcNCazTuSKDpHVCgsJFEN8PwgxwveX1JLySBpDnJXrkC65cr6bmiaF/zL0adjsxW+bn9khL3t/f3MpAozcEy2/fn628Ap1YYx2J9GGbGQ5ZoNR1xerFATA+KTlJgjiXcYdko7x2DWIaGLr0ktOo37ZeUyc7Y/qHeHDmg0vAkQuJ3W/Oxikpbl4cWY2pMvn+rG4l/ANFpKRuCdMu4qVWBDJeEpUvkVTOvZPeRKPUMZyl9Nulcp8e7uIpHUqs9iO+gi5jSsahnR9aMp7bADkJlfSscpblebDNo8ZNdaNE3YWTLPI6d0SxROXOq4TB4LC5BTASrMkBYOHPd6u7/p+m/eqzqotihPtZSewo0UkTS0kPEwOq4JPkmzICePEapWp6Wc1dMQKYqMSnuB1DyWxsedNLTr72vZiCjAq5nyairV/3xByjuM0sYJDt+pXSkHcdLSnPbiXRf9UlpGu1q0QThN2UMksPwVJiqUneVPA18OBOuXQ7hR7l6jyoGO32W/Ru7JartDoaBva1PCnWN2k1mVCt8swrK0p7E7rq8O7O40gcmMzgO1YZKBwq1i6szXNKMB45i7YmMDxCLTWWqJH7JIOzGLsQ9GKaTQP1CyG1sm+kNLrPV2r46AcJ84INhabXsQCLatjouJZomuXas1P3did861utbAgo8sTfRIilNvYqCecFEf26zA09Qmv8n12ECREBZ1koiW6IZ+Xe23kzyVmqGPpQax1Oi17zWQuBddv4Hy0EEozpM3uZjCY0YdTed2drPScoEpuYHY/FSsywTUVTscUYTe8Y2bpxVCp5maYiGU0km0xRBpanBQvMcw47SNvKVOXXIR24w0hNn2oGg7PrUz5vlNzzo94SbuQLHw8EuGQHtvBpieDWE7UTpNE3RQ6Dd12jINEm6DNO3tlVKxcUpo2GdjBdBq8rpH7WhIwtRvv8Wp3so1e7w7NUYTZBj5NSbhK/C0dOytoe8MiZjgpOzpeT9x4WeZ1Ozp7OkRvsefyZWLAykWUt0J0KYpNn2FVnJntNDRVr08GLna1ve+cQHGOWb7C3YI4SmS7bc9Hsj9AwRJaxfcw5MAMeNpyKZTf99RZWdriYNZkphb39a7ZIH1k7qsD5FsyxW5vfHlYaS3XiySFG7In7aKQV9eZcOuINUpcDVOAIsVt27yISixspNQwrZqUc2zf7O7NNnK0NSezQ92nw5GPz9sxVAlPVvdhFFwsPSBJgq+JfbfO9ptTe050ydYjesivPC1B93MeXPGIzYVuebx1OyrPLIHnTkQ1TMcsYM8Xu5alUttFIwsqvuSjG1UHMbnf3gXUFkNGUB0wWTSXd+0Ap8zmRBu0K1l4i0wTmWcw4RD2ZbeUyq1xO6MSqTvefTiSE0+4gpGss0NgMJu1CFe5emHh/GToAjSex3SN0UNyOeO6REQnbOsyW+Hiheaqgfy9jayvSgSvl7kVMnHAVoMSo3m/Ks2V4+V9EGoVtC1Mn00LT2aOibW9kMZ6TFyPSpe5PUV3Da2NaUsOaXri5YRcDshlZd2rerqqRe+cS3epXXDb81qTZlfaUuIP+i6AYzvcYop02+A2lUb6EroAeKDHLLFWTCJz7I5wp83mMAyFJ56itFdX9fGMoJNWXXghLnLkkN2vV+h+OO9ouqKdDZfQA7xDgykt7noJ42W2Fuveug4wOmauj+oHv7gIxf6orC1LPBdmKI7mbuodnxgbmfLD/f3YE87WvvHWjuFyjJAIw9w4x9hqV/RQcB1bU53E8lesyjIVb1hHFwdo01grtD6gk4Be99M5I1alsubzQ3osqL71ByV01ITZ7qziKlqIvjxizhjc7HtBlXdZYEXtNB4yUhcMocIuPiOdp6xEVsVJy67NiJk3a9zUwmazgXScO+7Za1oZackfxXOjtOeumtjWV5s1T2R+sxIOOm/CNYntO29zyLQkcqh9VtO2JaJeWxJmxJGdx5EY0hw2mC7I2f14cHI3vOkDGdoopKVbfZruO6VkywIJTGejQ+P9JHR4awT5BLhsC2oLhmp+gx3Js9+JHMvINRziIUjOo+ntoH5ImSCEryomWBfyqPN3RoJ3+biJGH5rS5GPi/fhPBmC4SjmIWoOHBsROBGGubwl23Sp2BK+czDdCUSp2xLjaV/s+tRQzpbhIQ3v1gdnQ2nZtiOG7W6zXSmlF8XxZV1v0knMFESOjoRUIowuY3U+UJB3iJeWVFo7a09QMqTB29W54S6+HZ/7eKPdGLKwxmnS4Lo/WnS4vdjYvURPpDhCLGNu1LRKqKt8uKxsdckctoXPXAsv2XJsC1DxmKQ7XW9WAJrPE2VodGujhuRDu6uKEFuOigVS5hgd76BbckmEnj+xp+wO70YsalXOKq+aEil2NdwdwVCYBjcRMxtoODEiYTpoW7QJyuY+lKGlWZp5Y5Mp2Rtr3imUECrY1BAzLdKnnJd6yxBy9hDk8Ro76IVtnHjYHHtYVS6Gud9O1zYSVTbelK0Yo0hcjUZ7gjBDc9fDSmOqHSHVCScWfWBynKFVuakRCAt5m2iNrkuiE41hDF3/cGbVm5xEhiSoZ0RrMJcoogo+H7RxMjdScgtpIZ1uEbOssTTjEt522fu56e1d7wOu5J28JsT7WFb2XRMyVQ+YQd2w5H20TVymGHE97U67rr2rt5E5UitBC5itJm3hfWyeaqu1J3+XrLRSJquiVuSzUTmsh7GBih5KcxDuiGQm3QhXXJdOkZqfyz46qWfUbV1NGZsEiSJjezs1MGagrCrX11ViHCuiPjOnVUJk5ZRIxum48qp+1wdX87q2Oyo4UDh9rouh1HhW1mrnFpeUCe1bfwdB/KAZiijfEVIR42GF79JlXPHNmGImsisZ1nZ5HDQJnZExxgjAfcP10pBvUWm7VjLMyAXhgjVCALoM7syj1JrRMqrghsltGbI81A3FhfzEta3Usy4dlRcidTQJalmGvh0QexkJG3uDEf1SPxKcIFjJrkilfZKg0yW5ySqJ6PEqmM7IOWcaUlTjqw1d20E0GmjD3oPbMdcvAn5C12y6U9dtf6i9OoU0CY1vbiSdsf5w8i3vCLFwCK+Wd7XsML0UIkbx18QUIKsbPulToJKO2EqFDRpGkDfKMuWwU8fdLKvhV/4WLq4gfMmFT4WDyhTWQcgkr9WEq7qpbTWbrmJtycye7l0ElQZtgK/E5rBvY+6gmnS9vQMsPuFUQ1eqydvZelscdX+Vb3Jd8rftER02EM2JRJOUznC/7o0rp3Wqs+UydIuUNuj5pnU/lmpudCS/Q/lTRJSUGGTOst95uZlB/IQiameVq246kKvEtA8jv7lkzHjwIewAtjzhzd9oZ3xHCXt7y07ikPfrnZ7qUr++8nvczjbbUr1kEYd0a2JX9wUDEStoX1H0ao8MhpQTUOMRrJQ296ntunM17MOlY5xByi2xCapOsLB312bPBqCbyAX7ppBVXw5atUUH+qC74z0dh4N2spW0q1HWoo5lbOUeTTXlrWVw0lt2F0WL1Isd7wS7duhwM3Dl1uH3iahStIgw+Lk8MiCvkaxXpUkzzj6WkroraO2I6FSMDfcWPTbklsSdDaERwgGqDzfgvRsRwk5/qCR929iccfOI2suuVEHk2gnfjIgdgQ1FcTM1O0fzxlJkOXFDL7LJ5FzGywPsTvlOCXymK7OjbvMeQdk4ihWcKyzJXEDCYbyLnHCVRmkMrmuLg/K9ZExnKKtLwfDDq25Yhulp+I3a1C3BtVcm4lUnza1sxWvBVSViUKD8hh6pI2fXmAU1RrwzQWMDQfurv2qdrG+hzIolovNPsUzg2soDjaPAX0Vjd161U4Hf2Xiw18OdQtw4LEYBayv+BnC8oAIjNw/lNTvTdL3XQZ6evbKQTjeVs3dabFRhkLAmD3GkLmuWQ9mlr0F0mQokdt4QlHk8TWephcq7VpCmmC57GN3hnnvrgqrRltqQaGtxuaIwbGOA3W/ud94qGpdCd7pykZ+cxe3O3huq6BRr83BYQ/wByeKxsU7qFi+67FBDgeHiHc9KshGqqQhRLOXwebtHmzBijOxurpQQW6UuCXqk+rgt0Fql/QrDh4tuMnoEurpxc07bbt3dRd9GEBf0Fup6QiVzxEPehyvBuZU6A1/BrtAIBqEx+6LL+bMFF1uWUPHbet+2ClOe73R3XeeVcTOveQSLXmWXLmYecIbEkj19so7waBg4CcVXUoDcXZaI3Sirt9qAeQ9rEpkqknuYkun6zoUhxdhWBeBAGXn4zlyrkZQoVKfTqI7lkOsmAKq0EONuQst3H17u0A5t29Xocchatqqm5cfCqPWjBiGVI68qGWmkrZ0cXWIak6i82pNJHi0P51F3JdTrcS059Gpd7dxsmXop6CFbkUBq33JD2RlQSETTkHUzQHOsHVrhRbX87MhWWFNYSNU5miPngsXUoeSP0g7F99oFvVm0nBnmHe+YChbjZXq8uoa4drZ7937eR669VDblxd36gESMDbpFS7Wg/cAvEZ0uFTmBbfFU+CnoUUapO5IoibPCaQrpujA1g4aKvqJlc6dY9VW57BGWrKVBDE3GtIcrtJe0kot6il3ue9TXDgGhwb6MnwcEKwplukSOX0Sn+grVVzg5lSS/SXLv3qg5o++FhtETJ2586H40ZdAj1XIPdVN9I+DdzREJe2zLAL3WaIuGSr7BcvdaeafLHY9vU25Rq9ohbet6vHG5Wkn2gPhZF1UGl1715hoF6QGG0Vu4NJSkIggeeMmGl9cwGcvjbc+u9uWtgcdlo018VcfTwfaNkF960nhGU0m+AJBVRZuG4kNJe0yzOgcgWw5B3AlsTucisd3q+3gtyxIOOvtVVuJCaTWhLkEX6rDSjRK2XTXwk4NsaqJa7yibuNyTey4XS+0ctnJEKqOSllUD2tduc2x2zCnjd7XkQRnwN0Qfau0yTqB4hw1KYCV+TPm9qZIiV4/TCJc5YSknAce1zDduquVNNFELsU5SvJWGdForKGHeJ4Dze3epmKY38GnEVmnkKTd8z9l+US0vznkrhI7Vt6fd1bhYO7fNXau/Xs42hIgmMZUmty8Z595Rl30LB5UdnuN8zygjeycJegvvXM/dTbF45a5ZLKSZlmrawG0oJ0TCrLDks7bZN5wk4uUY23YmGk5fsVDKhfV2m3uHkpIO9mbaYpG+opDjefKXLdKJRLfBViV3F+DjWbYCQxwrTYdJD29uOMHvm/5WMqfLJYs5zQQbhsnJoW0L8D1Gr6A/vqdnjtrHiG2bQgxjFFezx+Z4WOLEFvIrVfajUDaNPemf+6YFqMb6HJPus/JWpR4gkFOXhapfikR4XJOxLU8sYuKSBUFnypFuaX81bw4XRDGTXBkS2ZAZccBLhB76sl7KxMXJw2S6ZpUY7++g2JZoFt/ZyM4LiUIMW1INBBruueuITJA4HqVgqJByoiBrYy6LWc3ZDdxKoXSIDjFV2nSIH8tR5JklEiLj9SKcdEtd7uNxzPbo6WaMW3J3oPYd39iSFJyBnXutakNu5UBI09wEMrcxiPJNEr2gAMFYCcZJ2CH9KXYQ9iRRMOaW5F0gSUpbTWBn1l/72qZyRca6jm5kVEmgnZl4SOcaMroxl0SF2xq9EmO1ojMEQa+g0iP/rNbt2ljplzMBN/vb/mY66HWM0T4/+zvWR9wuu5+u0ygWGd7kRng/yPVhSsJ9rzXMQT0YmcmhsZwGObficK5R9XUNe7ncF+HxoNCrZcRfzztU2F+Em56AXUsDhxtovxy6nbGVJeWyLn0/pNr4sJf3csatRyiHbLZd3ktLP8Mpq4bbAtuf+pYZLHdfHaud75qHpesB3qHiVr+yjS5fQtq0pUugrRRbZUqR7uWNv18nHMpOW9qBNwzj88H1iCgnvDZ6bbclPA8NSWJQiBprvOjmDaVy6hqO7sSWxZDbZiruZtkPshOqRjNBrYU0dz2xj6jrgGE1esvu50rXpOx63Zdnsk2g/R3g/8Q4l6Ub386BHunVqvJAfO6Zz07mpNRb9DjuTQg53Y3yup0ue36AXXPCATfl44oPitvunMZwETE1qhzUnTAWaU8cjDQ4Q+mBd33caNMmlu2smEROLjk8lbTWxaHaA0DUUCfKCAwSFlhrBV1zCPU6hu6wa9BdiYw8XVBPpXhGON7ZOl1N/D5kRXFgakkWaTgLpUKug0i5gz0rodjlXjzJLX3GaGdlyt6ZDt3MbEndtzKN0yeoEcJm37p+X6vQSeyZcwZrTACSLCIqbEytrhwkQ5MpblPZOSzZwJN4LU78XV1JZt8GnXjH6ItMb21yn3bX7XG3Pd+PRSkX/pnO57/endnuXkuq7fEcaJagIWajwpATbw1hLumv90yJ9sxOyQrXbWmE8sF2E5YSJVbqJWMFzpKi3M4TKT7QmOa2MxSvVCLUuFL3YTk1NUbkt0IOj7rD5VRzui1H/GRDLdgO7EK4lkk82xTwql5jqBcHsbdMhA5fG8M98LWOvohizNfXPk+7plPaGy6WdAnad962tKBeptDtjDrDKWCUs6WrjT/ebCgmGhuPTvCdPTqkrOSG3h5p+KItFSmx7FNAY2exWvmQ3pmwbnVL3oD0fs1MRMmuzS2+bHYyi6u7k7Ixdsiu10Wva4QN1hyS+9KhzF0hJrJMHiFjYF0tSM2kpPp9pyrVhsU6jsxWU3zjEsUuVteuRAc9hPqQ5gJRUVV8NdzpQhMDLA2YpMYNpgJoYPcXe+OCrYs4JGhfmWtbChC+lvqYsA5w02QurOD4cPA2vXrce2Gjn6FEPMZpVuSBMRarUnYbdNsq50bbJnZvCX7njsQG6iPQnJnsfMTyl7+8fXj742Dv7b/92tl8uvP/7JDpeR709ZWSx4ll4PifHmt9+u+r9NcPb42XAIWeB2lt1kevY6e/O0b7+K8OIufZ0/NNrq9nz8+j8s6J5veb35LC79uumb60ZfZ4oQTMcPt2fieynV+b9cD3n45cX0bM3i6bwHPa7ktXfnmdxCbF/J4I6HacLnhdRq9jxQ9v/uvNpS84RX4Jmmo28/VGArAOf0fe8be//V/Nh34zkC4AAA== -->
