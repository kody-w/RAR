---
name: "rar-cowork-cookbook-adaptive-card-audit-financial-results"
description: "Generates a read-only Adaptive Card JSON file summarizing audit financial results for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_audit_financial_results", "rar_sha256": "52968585e7d1c262a565b251528550ebdfed45f33dfb2296e66c7a08fb6d73c5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_audit_financial_results`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_audit_financial_results_agent.py` and in the RCI capsule.

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

Audit financial results Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing audit financial results for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-audit-financial-results
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
    "action_buttons": {
      "description": "The 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-audit-financial-results-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_audit_financial_results_agent.py` and embedded as the fenced Python below (sha256 52968585e7d1c262…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_audit_financial_results_agent.py` first:

```bash
python3 adaptive_card_audit_financial_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_audit_financial_results_agent.py   # or on stdin
python3 adaptive_card_audit_financial_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial results Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing audit financial results for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-audit-financial-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_audit_financial_results',
    "version": '3.0.2',
    "display_name": 'Audit financial results Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing audit financial results for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-audit-financial-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-audit-financial-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c3e5940f543e4195',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-results'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-audit-financial-results', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-audit-financial-results-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical audit financial results status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-audit-financial-results-2026-05-24-card.json' that visualizes the current state of audit financial results. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current audit financial results KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing audit financial results for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.', 'example_request': 'Make an Adaptive Card JSON of audit financial results status for USMF I can drop into Teams.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-audit-financial-results-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of audit financial results status from D365 ERP to embed in a dashboard, email, or Teams message.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardAuditFinancialResults(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAuditFinancialResults'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-audit-financial-results-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardAuditFinancialResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjxrblX1GfF9G2n6oOiJnquBGNACEGSQgkIeRylJnnGcTg9n/vRDqnyvYtv763oz+1apAEmTv3uNZOJb+9WF0bFvXLpxfds/KFYKVpFHr1wsrdBVv0RZ2AtyKxwb+FU+RtHdldW9TNy4cX12ucOirbqMjBdMHLvdpqvWZhLWrPcj8WeTouGNcCA+7egrVqdyHph/3Cj1Jv0XRZZtXRFOXBwurcqAWXcyt3IisFs5subZuFXwA1FtyYW1nkNAuUwBeb/66zu0XqBWCYl7dRO35Y9FEbLkKwold/WMiquGjBAs2HhcYIi7roPzxMsZxZzQXQvS3yp+iTZ2UNdOjadLbNy2zPdYE6r8Ayb7CyEgh5+fTzLx9eIvD55dNvL05qNeDSy7tNs0nMrPvmXXXtqTmQkFp5AIaWI3BuDr6XXg3WzMAl1/MXb99+bLzU/7D4z/9MeqsOmp8+fc4Xb6/PL/MfrcsXbegt2sJqWs9dOFZp2VEKzH5dMGlvjQ1wVtvV+ez0BsQGqP+c+U1SUS7+Md/78bnIa+C1P35+Kco5WMAln19+WgBnfH6pu/nz6yyl/PGn17TovfrHn77JaTo79px2Fga0fv3y9v1NLBj4bWjkL77oKs++rVV7TlR6QPgf7JtfT9XfxL255Mtz8I9F+WHxfcmzPf8A+j6zzwZyvy8W+ADMfHmNiyj/8W2Nurh7c6i8H3/6O7FO6DlJGjXtvyT356fgZ/b9+OaSnz48wvfLYvlm21eZf79sCRLm37EEDH9f7quj/k72I7J/EZ1GOajU91h+V9z3Jiz/sfj5b237ryZ8WPifXzgvBWVTW3bqfVr89kiRn39wv1384Zffgej/oxi96GrnIeFLZuWR7zXtly8//9A8Lv/wy88/dCXIYlDdX7o6/Z7M7/n1sc6fPPg26sc/zwXrn/MkL/p88bWGFr8V5X+rf39dXKw0cr9dbz4t/liJ82u5mI14X/Tpgj9UYwN0/YMff3r5HcBPDqzpHvg1o89//MdiFzl10RR+u9CdomsXIMBtlHmz8qcwahbg74watQf82kTAsW/jQP7PEZ41LvzFr//TeeD7R+cN3yHrDdi+OADZvjxg+ctXWP7yBsu/vi5OQHhRRwG4lQKYVdXPuRUAOJ4XLsEwr74DsLLH1vsIavrj/GER5Ytf/yX5Xx6iXsvx1wdwR08E1FhxRj8wwnud7TRCL3+zygG05Q2e04FV0sIBKvlPAgACixRQTzv7pEmiNF24EcAXQF/jQzbw26dZ2K+//mpbTfg5f8I1unjyWgOBAV/VWXz8CGzz0ygI28+554TF4offfv9h8b8W/9Wsh/B5DRVwx1tUgIYPIgRV1mVgGAgYCDGAkEdUfvv9zcNADGDUBYhh5EfeczLI0sRz392tb5mPCE4sbA+4Gbg4K4u6nRk1al8Xor/4qi9YdL41s0RYNO3C9Uovd73cGYFUC5jz1ZN50S4akIqND5i1a7zHqr/atfVQMQPlbrW/LnasCjipSMF/s5qPQWBykUfA/V+T4XkdCKl/aBbrdxGvi/2cl4vSqq0yrK23NXzrGZeZ89+mA+HWIvf6z/nMwN7sqkeRPN0TzP1G5LyF9OOjq3AK0FXkbvO+dvDWk7iL04NB689581YAVj2HwgGEABYNusidaeF/vKVUExZd6j78BzSdJb1FwX2LyiMHmb/pW3SgZtf8pfX53CHwClv8f9MlPRwgCBovMCeeW/D7k2Y+AzN3iXMAn40lWPwh51GE3/qXd4x6h+rPeRqBLKvH//Ec+TD/bcwT/roaeF9jtId8kEsgMLPcR6rPqVvXc5FYn/N3TgAmLR4ACCwCuADqZk7X9wXnu++ahqD45+/f+oNHaoBQAKeAdF6UnZ2CVPM9z7UtJwFazbF7jynIe28u3T6MnPBPVs3eB+kF5C+AEhGIFuCN1684/bz7rvqfJj7boHnKo0XsQLXWDwFAD29WcA7XHFOgXvtsyoGdnx5CgBlZ2c6226BegKXPi17tVV3URO0c9qdfvRKA88f5/WnpfNUbSlAiwFmgEMoOePdROnMGZiB5gA4APUAlZVEOSB845c0JD4FWNuNAmr53pU+Jj8tvBnmPepvZ6n3ibMg8Z24AFj5QHVwZ/wgXp++lCZCXzSMe6/41076uNsueIbMBsAdWfL/77BRen2T/7CYW73I//dOu58d/b2P0oO/znxPg0yJs27L5BEFPyn1n3FcAWNBT1+Yr+36c2fHjo9w/fi33j2/l/ifhT7s/Lf49Bf8k4q1APi1Wr/ArPN9S3hLs7QX8wX5cmx+x+e7nXPO+YSpYvshAhs3RGwHdfyXA9yGABYMaoBAY/CTEZubRHlD3gwFAKD7nf8z4ueIAweTBnKFN8QckeHQCIPufkftKVOBW3oK13bmDDLx56/aoj8Z7+ZR3afrhBaCi9y9u2WZCyubUbubNHigi0JS1kff49gTGL2/AOF/58+Z3zlHkI/pXAAV4E+VO2oG6Kd5ZsnZnNduxnPV67tnmLu+BRUP7z6IPjw9W+rrgPIB7afPHBH8jqpmo/1CHT1cCFzrAhg8L98E3IPeBK2fz5hq2muSB79/VJSmjL4AH8+9osy16gAOgQL9SyB+N/BH9iIPdj2cBHHwQjtPV9YywdyvtnlEEwZ6Jpgac8921H6z15cla/7w89316e/QhjxYH+Bms/xq8Ls76bvPdFb422/8s3gDdzSzLLT7NRP/hDUrBO9ggfVh83esAn77tPh+/FuQd2Nj/PO+z5jR6TJk/gDng7eukr7+Y2N7LL9/T64G3X+Z8f2btX7XbzzgKeGYO8d91DEB5oIDbOd6bG/4lVPmIwAjxEcY/Ithj3GvcgDbrn50HtHyQCKDi2eBvnvxmT/HYRM72APvb528ev72AugKKtNZbZb3tQsBwgLkfm7nnggAAgQXB9ydUgHv/d/uTNyFNaIHWGEjBEZqgcAr3SHflIARi4QRuI/gKRygchz3b9T0Xw30UdX0bAWM9gnBIC6Z8m3BJ1MGBvCfqfJm7y2hWbNYK+OMjyGXv221wyX2z6GnB7K6v26EHijwN++3FJrC5lrBGZJ4vFqJXNmSQ9qhcoStMDWlvdKWM8zd/rxV8OTVm5pZKhurHnkQQJWSDYRNX2u086tcjXWtCYBP8FmXVJIVwaurP+KktlY5Gepg1WCmfyh7PSXq6dUds6tY4b5VOvTk1A7YdRXwjXc86vsk8PB9cS2Uger/xrudwwg09XlK2B0W0M6Zl5uvjiuJUm7M0adtRBAZNKxLqMVgcU7hxUSLzS20w7uF2FVapoQcusAiyYLndxnA3+tHquvS3NnxJLkOcicOUelSGJXUqkNt1FMt2pFKkp+9HRWZy7H7CLZxPL4MaDsS2D1Z92lwCw7uRfHg/bgkDWpFbRNPgdBQ9DZGd3ZFUIq731WsN0/49J5eYZwyemnf9MkXre9QnuiRi4VAH7YpKEM3MqjwRiMsGk/3lObnC3J4eORbX8/NORmAhmW0mb4QV2AN66I9cFDH3XZixq8suI8e7mOyyCl1f7k7IHXbJOdoaE23ISDLVvOvoyXSyOynpGBa00IlRkF6aD52vICGJZMaVr/Ta1JKg16qAZwRvAxJiMMT0dgrhgOr69aGMr+ebRPLn8Vw69kXvLQ/ZlhLZRorJMH1p6RUeRYeeIx2CktG0OzmqLJdn+HgG+wY9jCyxy4P+ItWSoOvSjlMpalqfVmGAHjLGJ1DrTNjXe4X3ob0/4rm07av0ciaI/V0+E1cdz2jJRyORTiVaF7zj8ZwqiXUUQj8JqfymXmyD7zGe5Xelf7s0ZznuVU/V1KmlWWyL86tj4g3bVFPJi5kI+3q9urO8FG6h/R73j82ubsQ+P0B8FMD1Gt5b5nnvVEehVRg0lup0dZGHbanvzlcj6/V6Yy1X50xba/K4Wco7Fat0Iu0d6eJKbsFDo2Po9baFpfvKvDM3yArUNU9dO54T7U0+6sRpU/jt3VhuhoaKpwtFJw0mZmuwmRfG6y0T9ucJRWtyw5nHU5vdS/zin4iVv0cyW3WgDU5ur6Wwpk2dWLrhEuMgLjvRVkBykIhlMYHV99IkeyffVav4IobKbdWYFzZppZVJFsfDrrxmXmoeKH9aHZJD0htrKlzrcLYkAz6P9to52QTEDU+Q3UaYaC+Z0Ko8bO/tGh5da9cbfOJIZH701tfc4Cq+V8TV5pAEJINRNaTB06Cqg2ow+25bmMxecTybHf0ezk8iuVtOZnaLUVbidRvzfeFw2enAm8J9I4oDXg9yA2NptudY+CLDTUQzse5vgiWHXw4iCuUAy6lTRhQWH8RX+A5d8F073uGbTgCQv2FtCu0nn4CHJToWWM0yFw+m8vPRWZvOaXfpDaFK11YPrXe7tQ82kZGYryr5lnjCVoWp4GidysNuTWQmVva7jaV5fkpz66u1gZn6ECwZKrOuXGicm14NV0m3KiwMxjfeDtpwWKpG9DWpPdVTmNaM+3KNsk5YmpRwgXQu9C6addSt49pKlWHCh24k3VxfjUXPdb5Z2JQmrc4Hh7pssyVLnXfbK1XQCYu0fS4KJGT13OE0pCV2VoxMsuGD7MDnWDQ0+NbsJJjNKUVJOOuCC2GnD+fNRjmw02E1ArhJu0kz9wRWnQRezupgaXpNIqlEruX3ymXEqjOqHloNpU2vSNnNb9Jms1dZg98jzmVXb+GVMJR5jkZtR28OuLdU9uNxSVmxzfFHG8Ojg8DtU7HC0En1CDm8VKUqUTFUCpqO1YwT+0ET9hFSjuY6xQKwggRLG5ySSFYUDtk+x/NgSpspsYz1tTEFfjyGAh3b+4F2AmjXqJK4LKSzNqVrO+HUEgtrdlfWpSuud2vTR9L6Kmm9aDBdeiyi/ZVP09A83nihTVc5JVfYxOq34MrfsNy1B0m+2BlU0ZPoaoyvtxsGcw5C37rm/RKNRXyN0LYS7m6qjcM6G8fwNgVxNakkjHdx2pGHq5RUKetbEqJK6UUElJHTMpbppEZstzy/g2jETz3VJWM7RGGS5YCocI3CSQ5NS8pULwnlqfjhcPchiEdKw8U3+jrL3OXYZiy/PwYGJC0dVZVjUk8QuTTk4crcc59bXjGgCZuNMUY73PlKYixEGTcbl46R6snUUSc2IJ+sS3BtZVNBUlFG9GN3Fu2+CXR5m242u400ZaOrZQF8iYWD4aIpP6mQFaPmcsQsvZwkRm4HXbhhjgOKQueISZEnddus2zC8G6YveWCQoRveFalu9J3Yn5cm5CkSy6biaaALSxbbPKA5mb3fuHuyZXUh2S11l8bZrWFuUzNWa8wROIXFiqPLnohNDounEMqtPcpPvKIfzzs/5Ny1t19bwS42Ez7fwvR0YRUN8ZdyRLXLk+vcArbBrWOBXjwCP5GMVLONJ5/H/ExxmQQN0EDJG04735PhCOEG7qRJYDDCcgj1sJVGuxZz6DI00Jo8ySPBjpfuqIiyfg+2heMHSCLThDiyUGQKatn7wUlSQAKaHHObUjjFwht7W2dYNDAef8B2ppErN/2+T3LeOTZd1J8b6YjX4S6u+zwpoVvP4DeR3S3vLlkmzJXhlrR9PHM3XtnH1v4CSRGj3gzYXSfp6SAo22SlrEFZhsluHTEETmYZHKuX4/GAs8o5PQ9n4PfN5MXyMe9lSVF5hDVb8Z7cx0ufRiTVNEco51Kxj4ggn+RY3zgRcMxwrvRC1qobJQnnid9UmcIJpRMTF2i/01PeCnxiBy1HVIzW5dFv9DRWhatVbRuLX22uJys63WsgtUVhqzFZupn6SZjsjbPcnLRjOErGhSpXbaBXt9i3TpVYrsdTQ3rXFCbLOJw6sUw3/WhH1ZYOa7GB1e60Z4uTplhZmGSRpbt6yCZ4YMOEpYzpbtLT+znqoyNjrbQclvQRoviM7AmTHWs5zDEh2MSCUt55zJJ3QgJjqpEkVJ76hiduN1t6v+zsUcWMLeNo7MSGvFjZVymTaVwKizvX07x+i8zDPWnXwxkd2iZQRCM/hHh7yu1jlRBrjNE3fBkYGn/JJw0qd/5xG48ZINbQ7FE0dnNIHbD8aPPpkXRLT7CO46GP71fYH5e7XbvpDznKSakuFSdIXN+qnWOw1AoEskQp6jb4wzntzgpO9pGdunrEaEPpBKJorhRxxN2UlpJ1THOiE5cDr62mlSW17H3MMf+k0SjB6xsVoP2ZYfJI9pDTLnSmm8JzpyupDjbvd55iHvdSxvVRX/McHZiD0Vrh7hqcHJZk6+gY4VlhOqLWY6Vse2lF3bttnZY6rq+tUB+UydziuzrjM6qC74FUerFG73IMy9aVMAbH2ybd7M0ONDl9tvaXOhVcKa+Tq+vhYvu7SLlyzhXjTnJk7VlMruAUIbG2m1piuXPTsN1m2RULAdGe3ZDb4bIwkeftcS1ZHNMwWSKhQROc1tTSUyOSMHc5jAF+1fr4WPqj6+XHWth1BIasWqYk94VVKYKH88ry3lhTtgopuMKa1h0n/SKOmD8xWlvwPX+0FNDbEQ089qpcbBhDqaN1y+vnga7MA82VKo2YhUhqh2Uq9/7VONbqyByKqIVKKm3qrlze0qFJSWaX5pfbCQ0FQl2qappmV7AnWrWTkrdFEa+C8jqENxKL0mgqqoKZqDQ8ceWmqveejVtLcmoTxCVBa5lFtwarmDVHQo4pOll9gauTgZhbZLVUXORCiicXx5iw8+Q95Ue4baa3Amw4W0Cr9yMcIegx4tei1VtiLufTJWZSmOKZdq+v3aDqQYde4W1IBaSfyAZ5kBz4KKIsx/SaV+rH4tZOSCHCvTlUhu4WBm3Km7BbVa1pFWId5GuDqlGrvsSn8XzuT+fuQrfNxaNPws3HV+kJMEbIxLZ/Y+Tt5cbAWzw2Nc+hOvkkMkqCuuxkr3hKkhWNipdqrPlbAcXOHhejsKaTQVvEvnrojJayTxZq9HavHP174vS7a8KI2vJ000MuwdKJKOtU3p27wESlHrtdJGfT2ifbpuIMGEoVO3gyu1u5RxpVQEiZP/a8EmYHOZZue4JTHDOQMeOqRAxDCMczcWr33Emi1GoPevbCyvoKtkdq71902Qq4jaeUvDOcwoq+q+c71xiHHsVdKQitmBCPVcxWwxmsYezDSdRqpGF6EYEr1MSL+6hvUjQj10cPW3fYESKdnA5u0/U2aQNNq1zJyYPRmKvab/BRFZMM28YucaTB59GKr5UVxKfO4RjpBENFeDjUqUKGqqCtyb66Zcsb6hB0qlb8ntzSUQRf/OQiIOtTCXPdigi2YtuzRILzhBYUiKIJipFEDHVpVKImzv06pYaqRkhubXr4VVDSVeP3XucsFUi+Xgo9uRwqn9uX+ElCWizKZaELD1l6WVdxeNpKqHXXU8MVEmRPZBZH6gwWBzurLIHUU7GmY81esY6d3wh9HL3r3UJkLesi5GaaaJM7zpYtTHTrEpl31nDqQp9z0vX8pskzymvxZefFBxvsVdzIRND8mjsm6LL6EiYQtvASumWmWjpdImjKNNDIby6Zd82u8phP914qEvvWTdyeyy2kC09uAdFTSpg0yun16kZBB9XpYTYtfFxpEGW/W922hbHc3cPDar3jp8wVmakyl9JZ8MIwGsnNeq/REehDeDakiSsdnzCDpurxCh8REpUIeLmX6K7HcVD9equ5KYLu7nLOnYptWJBbm82crK81Ds7D4EAr0FK9+9R6ae74Whp36BXCYij21i2Mke1uRTtLN7X2mIhJN0oZ/as5Kpv4fCpwjlVL0CR7GL8s0OCQwzhQ/x7tlHq557b8tYed4GCZDHYK4xTSb3FjtZZRpreGRC/C2N3wDA0okruk5njeo92IKp4pkieF22RozsLOHTtKS8WiJYxcXsPh2Fu6VkUR1PhlXbfjmABDNAel1pHntvtk3Nn2EVeEqh+PmJRgV0iTUNTmT6e7bjgjiVVSOOGEpCc+mVTq6nKZwFbLgW5h1+W0lMYDnzArMeEGfIlhI9nEaiwgcpTsr4ZRLHsxq7nEmszd2LrGCN/p4lIN5blq1KMQe4iZeCidbYxlH4sHwY+07LRCN51YOzY+hkosxGkoJamW6GwvrAnLh5m0MYSjvt4CxuBWKwwra6b2jDqWrkwZEEHcx2PJr9aOzbACGhGUJTQA/23BTBwjIJeYMK1xq8nXBza92eeGpAxuwCj/EBH1PWWwK1J2ahYtuYpDbm1wPkwwL9+tqHCc6YD2zSGy2Lvqu3IwVldDK4cVRMa9SjDjoaZkq8ArgWzIzTHtt5cGX/fUdacL3mCty9TV6JJbXjLGGWtQWu3e2m7udXJAYhm3G9jed3ypAVy5GR5z1zLOXR4OjVLId46myPPgHM7+CjfMpXprr0LVqr3DOjDY3VfBcl0F2d4heGQkLwVRq3UbHnGOuxysOHFy29ndr/XNBGzHyAoRVlg3DQ0ZBsZRJWtfGgvvcj4JGMW7cS3eq9gdZA66RU3WOMyKDIT8SpNZT9mrkrQ6hEJKi8LtS+2rskXqkTlA2dInz0rnHK7nQZ+Uyevo7WF7XVU6ypM5shyzVL2U/YQieXW3M0TqCApD6HscpNXRXV88RwfgikG1dyuVPcFu7tjJP5/H9d5bl0W3cgnqRhMbokYKytxchnq7EetDrLaH29Lbs4TvEoSypTQN1xBzgqFROoplstKlcVvpF4E2ScR2nJDdjflQ3VqUFIvS30ZEz8TWatK3+C3UNkjubOli37sdZsrhKeZGdhPHNSQ566N49oiTIVRUFOnGzVDK3A9As19OpGJ23DRodl7uy41razJVm/v0Vsmjqh9bc1Igy6IjG/bvpCXYzA7ZjGSGicNGz3tQ0L0JrfhTG9lbknCiXVO7J1lFMDpzTtTUxbZ+n7Kp7S9tbZClAu8Q+M6MObkqol7tjv25HpeWWxpJLBvtyrbaWhhX97S2pau+S+N6W5p4Ey23k9WvKiEZMXTr9w0XnEq63MEYjcFddZNxtGIRabhekGsIYUW8rsbDMYCEVYBOdj8dCQZNicHYS75UMLIREnpw37NB4kqxoVYrlkVda5OyHn+7b1XR0oZ0Px7Uq5sTl85z7mmr0rB+M6F62NyvIw6FhnJc4i4GUaa3A73YJLetuE60NOJ0lk6nPOBhU4idg9xBHuTccRYfYriYQI2iwV7uvBbDCNo+eVeinBjUJp0xzzplHM+9d1CsOu8OLtHqeHHqtk1BB6i7M6nIKpExN7ZhWPKhRcRTcTVWhytd7rvEKDVvWJpbyWkRLm29JboVod6jRT7tzHVQnQ5aC/q2eqcaSDfhZHAp3BjmYH1dg01KcIz6U7XV9gzFK7TLbLli1XEbtc0y9DaaR0LTxsaV/e3pjBkNtceHFWphaLGm2K0DG0faiJfKGHiNI0OrcuOf7kN63TvoFFUVRWYnRyTpvUdAV/aqQNANBS0orFADppr7qMU2HGXvl722O6D5ufbQKMIjuSDKUrGIE61QI3EgVb86scs4p2pxtcpao9lcAxrZ5GcZdezV0jzYZol3fqRal9BWBWuNCDTU9T5HSinglW6V6cRAnc/4cmz9rjhthz6lyk2mFwx3rq+9VfZZxlRKf1lf1napObCXr+9mR9zqoe7PohB3e28UnMlad8d9xRWYikvLIyvagg06A3nr7Hnv7pOCzd3ZlY+QUHMhzocgBPvUHD0kBk2LVL7RuuKq90N3d8cli6TbzGcVD0vP0mVQjlPBZoCs73TX3ZZL37vyN0rAGcIZvPwK75mrfVE2eeZdhhgitvsVDSPbJs2FyAAlQLnxgEnLsI8rkUzmY5R//OPlw8u3w7OXf+9hs/kY5//ZidHz4Of9WZLH0aBnuZ8ea336N/X65cNL7URAq+f5WJN2wdsh019Oxz7+Syd9s4jx+STX+4Hz86C8tYL5ceeXKHe7pq3HL02RPp4pATPsrpmfjmzmB2gd8P7HU84/mTOfvT3Onr+0xZfngezL/ADj/LyI50ZW6719Dd7ODT+8uG8PLn1BCfyLV5ezwW8PJQA70Vf4FXn5/X8DDOVrC6YuAAA= -->
