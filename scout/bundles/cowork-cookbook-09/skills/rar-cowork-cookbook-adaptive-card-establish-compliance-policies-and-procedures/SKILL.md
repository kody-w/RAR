---
name: "rar-cowork-cookbook-adaptive-card-establish-compliance-policies-and-procedures"
description: "Generates a read-only Adaptive Card JSON file summarizing compliance policy and procedure status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures", "rar_sha256": "970f977f243aaa56754ae9194b737ece9db4dae62fc4e77d935d9077c3cfb2f5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_establish_compliance_policies_and_procedures_agent.py` and in the RCI capsule.

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

Establish compliance policies and procedures Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing compliance policy and procedure status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-compliance-policies-and-procedures
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
    "as_of_date": {
      "description": "Date used for the card timestamp and file name.",
      "type": "string"
    },
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-establish-compliance-policies-and-procedures-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_establish_compliance_policies_and_procedures_agent.py` and embedded as the fenced Python below (sha256 970f977f243aaa56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_establish_compliance_policies_and_procedures_agent.py` first:

```bash
python3 adaptive_card_establish_compliance_policies_and_procedures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_establish_compliance_policies_and_procedures_agent.py   # or on stdin
python3 adaptive_card_establish_compliance_policies_and_procedures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish compliance policies and procedures Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing compliance policy and procedure status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-establish-compliance-policies-and-procedures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_establish_compliance_policies_and_procedures',
    "version": '3.0.2',
    "display_name": 'Establish compliance policies and procedures Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing compliance policy and procedure status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-establish-compliance-policies-and-procedures',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-establish-compliance-policies-and-procedures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af3168c1d861d214',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/establish-compliance-policies-and-procedures'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-establish-compliance-policies-and-procedures', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-establish-compliance-policies-and-procedures-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical establish compliance policies and procedures status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-establish-compliance-policies-and-procedures-2026-05-24-card.json' that visualizes the current state of establish compliance policies and procedures. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current establish compliance policies and procedures KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing compliance policy and procedure status from Dynamics 365 F&SCM for a legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing compliance policy status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-establish-compliance-policies-and-procedures-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of compliance policy/procedure status to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardEstablishCompliancePoliciesAndProcedures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEstablishCompliancePoliciesAndProcedures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-establish-compliance-policies-and-procedures-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardEstablishCompliancePoliciesAndProcedures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6aZOjWJblX9F4m01mtSKCHYloa7NBgITEKhYJVFEWyQ5i30E59d/nIXlEZFZl9UyX1ZdRLu6C9+5+z7nP4dc3p+/isnn7/KYHTrE6OFmWxEGzcgp/xZRj2aTgR5m64L+VVxZdk7h9Vzbt24c3P2i9Jqm6pCzA9kNQBI3TBe3KWTWB438si2xe0b4DFgzBinEaf3XSFXkVJlmwavs8d5rkkRQREJtXWeIUXrCqyizx5qfyqim9wO8bsLZzur5dhU2Zr9i5cPLEa1cYSaz2/1NnpFVYAmtXWRA52SoouqSbP6zGpItXgnpcdUBZ+2Gl0YdVU44fnpIdbzF5BfzoyqL9BDwJJgeYELRvn//8lw9vCfj97fOvb17mtODS2zcfFhc4YIybJW3MfDdaXWxOgpYufPWbzUt4MqeIwO5qBvEtwPcqaICpObjkB+Hq/dvPbZCFH1b//u/p6DRR+6fPX4rV++fL2/KP1herLg5WXem0XeCvPKdy3CQDXn5a0dnozC2Idtc3xRL3FqSniD69dv6QVFar/1zu/fxS8ikKup+/vJXVki8QiS9vf1qBGH55a/rl90+LlOrnP33KyjFofv7TDzlt794Dr1uEAas/fX3//i4WLPyxNAlXX3WVY951NYGXVAEQ/hv/ls/L9Hdx7yH5+lr8c1l9WP2x5MWf/wT2vgrQBXL/WCyIAdj59uleJsXP7zqacgiKJW0//+kfifXiwEtBjrv/J7l/fgmOQcmDaL2H5E8fnun7y2r97tt3mf9YbQUK5r/jCVj+Td33QP0j2c/M/o3oLClAs37L5R+K+6MN6/9c/fkf+vZfbfiwCr+8sUEGOqkBPRR8Xv36LJE//+T/uPjTX/4KRP9fxehl33hPCV9zp0jCoO2+fv3zT+3z8k9/+fNPfQWqOHDyr32T/ZHMP4rrU8/vIvi+6uff7wX6zSItyrFYfe+h1a9l9T+av35aXZws8X9cbz+vftuJy2e9Wpz4pvQVgt90Ywts/U0c//T2V4BIBfCmf8LWAkj/9m8rKfGasi3DbqV7Zd+tQIK7JA8W4404aVfg3wU1mgDEtU1AYN/XgfpfMrxYXIarX/6X94T4j947xEPOO9Z99QDYfQ2+od3XHxj9tXrHu68AS79+R+n2l08rA2gsmyRKCgDFGq2qXwonApC8WFOBJUEzAARz5y74CBr94/LLKilWv/zzSr8+5X+q5l+eyJ68sFJjjgtOtn0WfFoico2D4t1/D3BcMAVeD1RnpQfsDF8MAYSVGeCpbolemyZZtvITgESA6158BCL8eRH2yy+/uE4bfylewI6tXiTYQmDBd3NWHz8Ch8MsieLuSxF4cbn66de//rT636v/atdT+KJDBcTznj9g4ZM1QT/2OVgGUguKAYDNM3+//vU97EAMoN8VyHYSgjA9N4N6TgP/Ww50nv6IEuTKDUDsQdzzqmy6hX6T7tPqGK6+2wuULrcWPonLtlv5QRUUflAAXu5iB7jzPZJF2a1aULRtCCi3b4On1l/cxnmamANgcLpfVhKjAvYqM/C/xcznIrC5LBIQ/u8V8roOhDQ/tavdNxGfVvJSwavKaZwqbpx3HaHzysvC/O/bgXBnVQTjl2Kh72AJ1bOdXuGJluEk8d5T+vE5goDqAtjht990R+8DjL8ynlzbfCna91ZxmiUVHqAOoDTqE3+pyf94L6k2LvvMf8YPWLpIes+C/56VZw1+Hxz+btxZ0vW7gadd6a+J5/fD05cehRF89f/tnLVEgT4cNO5AGxy74mRDs1/ZWebKJYuvURQIfup6duKPcecbpH1D9i9FloBSa+b/eK18uvu+5oWWwCcfWKQ95YOCAtlZ5D7rfanfpnmG/kvxjUKA2asnXgKrATiA5llq9pvC5e43S2OAAMv3H+PEsz5A6IHjoKZXVQ+S7a3CIPBdx0uBVUuuvuUQFH+w9O8YJ178O6+WyIIaA/JXwIgEdCGgmU/fYf1195vpv9v4mpqWLc+Jsgct2zwFADuCxcAlJUu+gHnda4wHfn5+CgFu5FW3+O6CpgGevi4GTVD3SZt0S2pfcQ0qANsfl58vT5erwVSBPgHBAt1Q9SC6z/5ZKi4HMxGwAUAIaKc8KcCMAILyHoSnQCdfwACA7fsQ+5L4vPzuUPBsuoXcvm1cHFn2LPPCq1qdYv4tZhh/VCZAXr6seOr920r7rm2RveBmC7APaPx29zVYfHrNBq/hY/VN7ue/Oyf9/N87Sj3Z3vx9AXxexV1XtZ8h6MXQ3wj6E2hi6GVr+52sPy68+fE7b3780egfvyHMR2DExx8I8zuNr2B8Xv33rP6diPeu+bxCPsGf4OWW+F517x8QJObjzv6IL3e/FFrwA22B+jIHZbekdAbTwXdq/LYE8GPUANgBi19U2S4MOwJSf3IDyM+X4rdtsLQhoJ4iWsq2LX8DD88ZAbTEK53fKQzcKjqg21+m0ChYToTPpmmDt89Fn2Uf3gAYBv/8SXBhr3xpgXY5VoIsgFmvS4LnN6f9WoZffeDc8u33R2oWXF0o0f9eh0uin70AlOfPFnw5tti3mN3N1WLn6xy4TI5PwJq6v5etPH9xsk8rNgDgmLW/7YJ3Slso/TfN+gotCKkHHPiw8p8kBAwDFiy+LY3utKBzgLF/aMuTOr6+qOMPnF2Y5rfssmBv3YPm/7AKPkWfVqYu7f9Q7vfR+e+FXsEEssjxy88LGX94RzrwExx3Pqy+n1yAN+9nyeefA4oeHNP/vJyaluw9tyy/gD3gx/dN3/8E4gZvf/kju55w+HVJ0Kt+/tY6eYE5QANLcP8RgQPjgQF+7wXvYfjnm/4jCqPkR5j4iOLPzZ/uLZiP/j6iwPQn8AP6XKLwI7w/nCyf58TFSRCU7vVnjV/fQI0D6zrnvcrfDxpgOcDJj+0yLEEAH4BC8P3VyeDev/AI8i65jR0w6ALR1AYOqc0mRHHMcRyC3BC4E1AIhbsbbBN4AeW7uO8EJBp6eLDZ+BRG+BS82XiYF7poSAB5L6RYdOfJYi1BbUKYotAQR1DY9wMg2/e35Jb0iA0KO5TrEC5BOe6PrWlS+O8heLm8xPf7aegJAa9I/PrmkjhYyePtkX59GIhCwMWNO4v8uiHDchx3vJk5SShn/o4/bVtFnXYmkQRrdjplsbQ7lcl1OmHCSRRPd+S6i9T0GApccDttLz6c5tMZkVFf9XNFkjTxZl0QHyHXdTA9+IM7nWN3LR03pnZ2GxlvY5VO8lk+kozONPGJ5I/bu362b8WdRIt4T5q6Rh7Cvc8Vgr2h1J0BQWoLTUx/m+VxcI7usdIoBZ6NwPdcCg8N/7o5CHaSmb2PkUGoY8K+GBq3apo5N61CuFTIMIWnEEfn+IwPBwzDEwvCOhLinBaOJ3EqxG6Cj7l2MdpTf0yEu5vc52DQbH6PcPpWxcpsO2jJWBlUebzrGvMQyzQyiDN+0EgqGCxoIvs7m6zDZPJbdYNR42QH8m7fnWirYUS8k/NSahtEa4+JyaiQYpnmQ90KGI2zJ2NnORTvGZo0hA9Mk6hU9es439EHzbBNOkaxu0youCjlh8nslRNCeyfiATLgqnB6TbNLdLAmQLOCctwY+G5+JBstuHfENTwQ287hB04ei9ylcW/KU45tUdVjH1xaKhPXCJ6S8sSaOSGSTurUiUuKcybeb1p7ADPTrDsbPEFpWtaiy9ZiTAONLKfAEHPbkbeY0BND5vhDjadlirC5uoNb/SDIe27vHIZ4n5rheWfY+G1qopBoL52SZxZs2GWBlx6UGQcnL488UgceOFV3k0wa/pBqG+FBpBITRZVo9228p6FKxOtZqtEwvW+TPX2VOuqg2wZPB+sgCTPXkWfVxmiF1y+1yW6RK7GPHNrfjLHiaOrDCPhEQQS3Oj2GSTz6wujvrjnCWkK6a/RRxmeH8BG91UgjFh6VZVd7MJzWgy5F2/TGQJxgbc29fyUUDh/gYfQGSnycQlKEnQLmwG2IM13mhJd+GZxRl41gZJbPobrpWrewM8nMb416i/YqK43bPYWTMD7X+XW9DcbSZYRgThLVmGqluGjzLSr9ioPDdueaEdGfelVuzftRlSZTxaKwpV2ISBvpsY1wRqm21DrnSTnDVczLEeZixmKFdPbhms0nwt6U9nE7RyVS4zccKmr/uNEiiSUYWWpkf6CNQXKS6hTs3FBNXY8/GNQtrZgaiaJdF6+n0JkOeTpr1VHTgtP5emUTfh/SWKdE9yO9XTeYDD2mvTwpzk5WmMYe+dnrrd2sbvv8IeGSgtn5+g4n5dZwcct3bEoWbu7VUfeCcSGHk0MZ6eXazKMQWvUhK/Vdu+Mgi+fUw50sUrvWHygAEoTaBUVa1SNyKscEIuoU7hEedEV3um6uVooMEGsxjarGGadnDYMVTqjnRzX3GOEwI8c4nZNMdjxT9eU4Y0kEEbYhqUaFR1LHwdDusC+IgsDbgqQe183moG9kyVGM+9kgg4eoxmNBW7Y6kg8rgFW0Ux4holYmdILBKWY2BFoxr40uA5DuaCWFdum2zNDeSbrjST3ydHZjHwg2JKpYzAi1P1sOr8EPig2TiiM2zRCXXn20tIHl8ESV6IS83R65jcKU6cllsZFPo8nJLYPU3q0eveLuT/TcSRXEHkCvp5B+v8onP9sfA/OUqm1TMDK8EaAIK0BHlTZZJQwxQbOZko6P1aD+Do3tBVoMDXehDRt0z6ozK6hOQCOmjwYXqeBN7EBURYGx0JW6HaCcaLuHoUDMJTHutwOn2vmcdOzchDL/wOpB8hFqQ+/8lK2N3jZMx7vgCucaIbmegtG42Ih6mALVYUfmlFTsbd1UErdBQv5At87dsCKdk9DJCAZ1EznarmlPFhbJCTqVxvHodMe9cdZNf8f2pXB2nDXcOYRg7xSbuwsCp5t4se1O0eEYwXLfrqMQLuzrg1EFAZsUHBOc63bsoAvbeyTD6BfnQO/P21ZAsoSyRBHdO2KKRsYJtXhRyV1R2WMKw4UyNBjkWrJcePLMHBNulR8VUcdS9U4ALLT2Tn2G3mFB9e3bGvfW9TYgVSbi57kRWH+YYghJqXC4dxtc4PFgvQ61aB0MCdLq7WN2ClZpoa0l0vtjOIFmOxejhIgq4uhRwcDX9LI7aMEGt0bIbv2ziaIh39yZnPNUvoA3oc2E8UMDnOyYOos5kWmiEUHxqjgL20zm1nq2D26IJAgUHpzrPZukqmxk6bU2DKH02kY8mG2Eq/H5aBxk2dyco/5K4dueUEQRuSM3ngoyWz9g1whxJdvs8WkLm7XiX9kjdBDuFXSb1vNFY45tyexnX8P2EgdOk7tuh/QxMlexzM68cYryJj64KHZNkCKDJVm8xHv4hPIFbY8TEXObdUeKF0KeWDNl1Loq1oLrMBM9XY0h2ivbCuINmNvUF+QiVPHxuBVpOpHremiEeXvcE7RT7Oc5tiZDp6mgGbcX5WSXnVCPWQ3PZSXCA6fUbBnTgpcWil8M+0cbcqIt6kmSFk2yH0+xfN4fTy7bjAd8urbaGjV1lx6pNUcK91O2l24s7lwOB1Ov8r1Wu4kv0bDGa3oc7qsygVDhPMUPBFd39pixUW3m/HmvXkRSC7hL5ZkIUiC3ds0JtDo2pHNxjrHXsnu8vNlWuYExDoxOl/HCwmVlPXQhbshhZ9NM4hFkUyM7v9pHoPoNV5RgcWuPAe8fjCgcPZ3RbzKa2dNw6q7NJHFuFRJsXkuCk+79vZTLAZjEzg1uZSO3P+dHBHO5Ub8lDDzzVGH2u0yE0OSoA6qaOmaAbuFFo+dSzU8GWiR1I6vwdXYSwSfOTYFgRelsSO8q7YJHhbtF0CW9Ekvp4+jFl0s4y6Ldknt8g3oYY0anExYMYrKWHtpIYHtuTgg7m61TACOp4PAYe43NWwvLqrk1dkdCJaRIP8IWKct7Wp9vlY41mq1VtOyUicBVl+v6YPi4L+188zBuKJ5LYCYfD/R2Jx5um5rmpwS3d4RFWPfdpE9+6BZIej6wo+zEVayhniY1INSBlD3KgU8guzifz7J7IsMsUTvlPHYmst5xj2CQ8/CmYL5Jc/W+pNteqM9OvtYlJB7cSLLRnrHPTX+AGGiApkCrzevjBKfbS3Fo75Laia6PZ9uiVK7zxJlikwv10Y7WZ3Y2z1WXxdWshS4gzXwfmnhnMY6WlkyF5qZ7TPe6MImnOIbqvoirZdxZI71vWo+s0geBdOc7QZ7x0wkdsWjOxCsRHC/E0F/QnJyaWQ/cA06TDmRvRPdOoZMlybc1lu+ZnZ/oJT8pQ5DrZEzvTNY9pMm53hitjl8j1qudpiHIbNTEzWheKCn3HgfsxmloYsK+0eI0N/N+p/drFcMeZtlLtyDViO0ZNyxCbM9moB1Hj4wCmpfOTlZy8E5Zhw/HcwwefoThGTFQtySQ09xcZrXz+MvQ3ZqaIorOty7rxIPEIjWaLRiTIztBBFYQw3Qb7hlJTeiRdgs2Q4/RAy/OI80lFxDGpL9o+yg6X7ehZ5ql4eTnU3Dz8ruSQS0P0+SkkPFpe3fIaLagFIyg0bCw9XTZwo0vpBhDxoDZhIuJ4Nc7Bp1vQZ0mweQdsPrGBQ8wj10RFmbxEY09mcNlu6E3cOYaQo3kd0u1MEnsA/hM0AdjLpN4LJVcHUYsh27niqzU1DleHx0lPaKHYMntMdPENLS8SbkEW6MUwMi/38udUHgj12F1NLr+kTQ4jMPXKWY4vnwnh+ut9zRrTFOXrB2PQnc4ansmg+3MKfax220j85jnelh1nkg0mDAj2TH42WBYAZGNfVeVCrrjNywTGwQHC+txf6TN5kJxjlYidB4LSuWdg8ZyW5I+W/3Ozevq0W0QGMx79UTmZZifh3HLVs3xkjhNz0MYHyUq1We3M5FWzl0cTWI610xJ2CjHPaBaXOMoJCS7ltnqzNnnKwUYiWWNKiCTIUs9fEAFfjqIvjTxgeSnB686V9TMrAt6zzQnlZb4NNnKJ3Mi8Kllq7XmbDxbwkVTxq6brumRMdsq+M617SogC58xNu1OR9j+IuGxyFe3Gd6Y2ZXTtgeO10fCPXPpiMfa8Xar1y06himqOXXSUJt6r4YT0m3oapIk315n2nTSHB+Ftt7MXop8xyWOEG7sSpO48+7ujYfWkU4KuekVT+UygcAVQLPqhSlhjhMdYD/G8MSM0+q+9f1EVnmKxSLLtMB4n1kEQACdFfvueqvBvQlgWkxtfVhuK9mr1letY1FuJsbeUk8VSfsSfN/e1Qo6yWAAJO7dVV9zIs1V44BGyrRvR9bKYZc4pv5VZS0tJ9jLUIrydKGJA4Rb0+VmiTxxiAc5Dg/9pdrKOKGzNy3DKnGEglKs41vJDBs9U9JabY6bJr7CZTphtZSqQib7lA7T8CxvHpEyK7UyknqPeMitP0SKYlQ+TwSqwvcuc3EfgDI9VoHYDbYbawkZ0WvFXKQgp2zBoPpB4RyfkvnhGjZF+chn37bs/Nqvye0maUukFeri0l7EdXGtKCW6KCidB7OKn+i6HcXw2lyF8wYCfJeSd7ekImNjIxK0SbDRowJD9SdYb8dhZs4UwDZmsKHZGqM+QhL70ef2TT56U80E5/Pe2oeSYd6sWWkPSSlWw4Fk1MlFmPUtcNdu01qQaXdsGrFDeu5PNwjBlDa/BDJFeLYa15vGZO68C/sHz2bhLUYRD2h9j7fmCdsfiNqBoKRaN+Ku9kqjgm9EuFYz5xocLpaKeF6ZPrx2si+MpJQzRJb74QHReeatd/C6qcl1UQkZVR3yJhFxXTnzJ6VR2o19spC8xPbNtTF0ae1vhM61msFwz4EfCwhU5h3fztiulzyPSLW74T7iXhEp1SwO1Xrj+ISY48dI2W28ZoSIR98nfZG3Gkggt5fXp+ryuLGn4eindy0gvHtobK1bmUJkVfXtFSsUu8Mv+xHZrDPDVLra4gU4PDnWNgiv927NkwcfOx44bj5y1owre+vRRI3ywAIuBm3gutegPF9MVJFu0jW4BoPj8PkkImeqyYRdaQRjV8t8NwT3C5QK8yNOccknqW66JeA0jXqlhsfHjZ1cTmbFAbMjL98TLBuz5cFT4TLpLGt31GXrfA+1RkV2oOJDUr4z6Whzl5Ib1x17lYpwT0n6Wjz7g83exi15ZdMipjm5dnxI1LbbQDWO/gWjoqu4lvrTWqv19lhJWiPLbKNsKt46jt1WZcu8rR8i1Jn7a06iJwZUoaScmxI6Ng0DyMAOit5gHtwNKOD3UV+lHpngly5Tr1lpYNv87I3N41ZKmE/shyFX8rtIiEfERZO7dizxEl77dHDTmY6Ula1YCwOLCuLx4QXgCEgE13WgVVbet4rJMR5MFGgdEWchLa4Hr3ZvtgsbRjHkcOXF4Dh6Twn+hCKsiKzRq5pfzkwyl0p/ktYd70nMvIN8npLKg3/hpl7dsTY5i2Rj6XoE5Uh1aDD6FOC7CujtW/VAOQHcdKpM5gXWkH5FICZiwy6nQtYEOZX/iNc4p3nzFm366tEjMNmfRpGAh3JdGmAokWi/I5uZkpJbP4hV5+K2QAaFsVcDsXdKL9hTWzhDcZTBtqeBVGw6H2gY0W8KZVzVwA9qqlYP7MVrRwI/PqphwxZucUms+T5YIw0ltVLNs48a4fFC14l2ObpCcJJNF2naWzeVXEkBLBemzRU2pnkr7bWWIXE2TTFiTnR18EDhHwk0UKr0OEHRTgdT/yMZd+xde1SnUujztWwTYFzOO5I+jmSqbpXED/nIaopKqfa+uxe2rn3KmhrApeu09l2EnJpKmjs/bJyDS6sXf9qAXtT2+nSGbpZ9DMlCRSf5TvmCxue31s94wtuuvfN26u+uPjxm4qFHxAFt3RbuSbUj9F2G5aUm5x59LWvrsrl1lZbdg6uSuVrfOBUKnVK7Em0J2eQH+wh1MypNToTOxsGGNvvIPvhQJeUYXwv+Vj1ZCnW+ItUx2TzatQPv7at2uinsVg6ZIceifNrSg4skkmMMJ5x2rjGpR4MsRal/si5Ejc0M5jv7bBdwt4FXj61Hahsvvl/uzhox0nRDuYZ64XMlRLR9YXkEFF/FcU34W8i1AwmqtnNtddIuvWbJvmKDeXqMjA6zJHyPiQEdChE6O2eVarXBp9yWy1z1WnpG0PVopkT+FZnXmFduzN7m5oCfApHyKKqpUN1CRv887IfabTBrD0AfhGGe2oOWz1pxRmUBR4mZQgmU0ALt4PJE0oLjbhkEWHNqPAM64mlrX6qSZW4ttUfEGvPg3iU3dNb7RnTA9FOc7odem2m94eXjTrXj7WAyEadgO3AUnP0K9ciTGnL2rRjByG2u+Qbaex51Q3qKpMMohlEGPfSpP3XkjhzHKrxk+9DAHpl6WPfrh3apMBiM4S7V6biJKYYYPmyLvTZwM6J4qOexvz2wXiihtC9LfHFp+vV5WwZC6Wa1OD+MTTHN5HojhRrKP3h+c53uFSpfWw6LJnTfYgLmOchQrB37gsfh3ZQdXOXZHbvZXCHMPkWEq09kM1oGawjr6uqugypUqjDFo/PWFaajGYn15Y5dnZJpIyalEC4wDuT56vPdTNaierfOLUBe2qPg4zqFeTeSdaYsVfe0NtmjLCqPBkvZ/pCoVkPd/QyNDwPpQ6hIOez5jE2Px+ZuiAGZBUZSWZxa2UfM6olw5+vFQ473vaej+76Mqxu889kIttaYJW9CcRBnac16ka8cB4N/aKy1MU6Cym3Lh7Getw9tcPDsLsO1L+uNSl0UdbfZMogcoskjOEc0/fbh7ccjtbd/wbtjy7Oaf9kjo9fTnW9vhTyfIgaO//mp6/O/wti/fHhrvASY+nqU1mZ99P546W8epH38558ULnLn1ytc354fv56Dd060vCT9lhR+33bN/LUts+d7JGCH27fLC5Tty+q2/e2j0985/vz+ehskaL525dfXE8bgbXnRcXlRJPCTH1+j94ePH97893eSvmIk8TVoqiUU7y8egAhgn+BP6Ntf/w/q2Q+20S4AAA== -->
