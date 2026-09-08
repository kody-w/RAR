---
name: "rar-cowork-cookbook-adaptive-card-mitigate-and-update-the-disaster-recovery-plan"
description: "Generates a read-only Adaptive Card JSON file summarizing disaster recovery plan mitigation status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan", "rar_sha256": "eabecd921f5c0d473240e775ba8586d021bbca96c899e0a5f79bfac4e28faff1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Mitigate and update the disaster recovery plan Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing disaster recovery plan mitigation status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-mitigate-and-update-the-disaster-recovery-plan
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-mitigate-and-update-the-disaster-recovery-plan-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date the status snapshot represents, used in the card header timestamp and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 eabecd921f5c0d47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` first:

```bash
python3 adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py   # or on stdin
python3 adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Mitigate and update the disaster recovery plan Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing disaster recovery plan mitigation status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-mitigate-and-update-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan',
    "version": '3.0.2',
    "display_name": 'Mitigate and update the disaster recovery plan Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing disaster recovery plan mitigation status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-mitigate-and-update-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-mitigate-and-update-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dbb2d94f7f88dea6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/mitigate-and-update-the-disaster-recovery-plan'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-mitigate-and-update-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-mitigate-and-update-the-disaster-recovery-plan-2026-05-24-card.json.', 'snapshot_date': 'Date the status snapshot represents, used in the card header timestamp and filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical mitigate and update the disaster recovery plan status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-mitigate-and-update-the-disaster-recovery-plan-2026-05-24-card.json' that visualizes the current state of mitigate and update the disaster recovery plan. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current mitigate and update the disaster recovery plan KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing disaster recovery plan mitigation status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON of disaster recovery plan status from D365 USMF for 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-mitigate-and-update-the-disaster-recovery-plan-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card snapshot of disaster recovery plan status pulled from D365 ERP without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMitigateAndUpdateTheDisasterRecoveryPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMitigateAndUpdateTheDisasterRecoveryPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-mitigate-and-update-the-disaster-recovery-plan-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'type': 'string'}},
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
    print(AdaptiveCardMitigateAndUpdateTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6eZOjWJLnV9HGmG1VjTJC3EeOjdkiIRAIEIcQEpVtWdwg7ksIauq770OKyKzqrp7d3u5/VpmK4HjPb/+5e8CvL07fxWXz8vnFCJxiwTtZlsRBs3AKf7Eph7JJwa8ydcF34ZVF1yRu35VN+/LpxQ9ar0mqLikLsJ0PiqBxuqBdOIsmcPzXssjGBeM7YMEtWGycxl+IxkFZhEkWLNo+z50mmZIiWvhJ67Qd4NkEXnkLmnFRZUCUPOmSyJmpL9rO6fp2ETZlvmDHwskTr12gBL7g/qexkT8thqSLFzFgGjSfFugrvtirwqIDfNpPQBqd4RdNOXx66OR4D4pAia4s2jegRnB38gosffn8818+vSTg+OXzry9e5rTg0suHArP88lOigCl8s/LBwTEO2Hfh9XfZVSA6IAp+RmB3NQLjzudV0IRlk4NLfhAu3s9+bIMs/LT4939PB6eJ2p8+fykW758vL/M/vS8WXRwsunLm4S88p3LcJEu68W3BZIMztsBmXd8Us9Fb4Jsienvu/E6prBb/Od/78cnkLQq6H7+8lNXsLGCJLy8/LcoG8Gv6+fhtplL9+NNbVg5B8+NP3+m0vXsNvG4mBqR++/p+/k4WLPy+NAkXXw11u3nnBdyaVAEg/jv95s9T9Hdy7yb5+lz8Y1l9Wvw55Vmf/wTyPqPPBXT/nCywAdj58nYtk+LHdx4NcFHhFF7w409/j6wXB16aJW33f0X35yfhZ+j9+G6Snz493PeXxfJdt280/z7bOeL/EU3A8g923wz192g/PPtXpLOkAJn64cs/JfdnG5b/ufj57+r23234tAi/vLBBBjKpcdws+Lz49REiP//gf7/4w19+A6T/j2SMsm+8B4WvuVMkYdB2X7/+/EP7uPzDX37+oa9AFAdO/rVvsj+j+Wd2ffD5gwXfV/34x72Av1mkRTkUi285tPi1rP5H89vb4uRkif/9evt58ftMnD/LxazEB9OnCX6XjS2Q9Xd2/OnlN4BIBdCmf8DWDEj/9m8LOfGasi3DbmF4Zd8tgIO7JA9m4Y9x0i7A/xk1mgDYtU2AYd/XgfifPTxLXIaLX/6X98D3V+8d31fOO9Z99QDYfX3H3+ArgM2v/QPvvgKyXz/g+usHXD/C55e3BUBDACVJlBROBkBXVb8UThQU3SxP1QRt0NwAhrljF7yCVH+dDxZJsfjln2H79cHhrRp/eaB78sRLfSPMWNn2WfA2W8WKg+LdBh6oLME98HrAPCs9IGn4rBNAwDIDhaqbLdimSZaBwgR4gWI3PmgDK3+eif3yyy+u08Zfiie4o4tnFWxXYME3cRavr0DlMEuiuPtSBF5cLn749bcfFv+1+O92PYjPPFRQfN59CCR8lE2Qk30OlgH3goAAgPPw4a+/vRsekAH1dwEMk4RJ8NwMYjoN/A8vGDvmFcGJhRsA6wPL51XZdHP9Tbq3hRAuvskLmM635poSl2238IMqKPyg8EZA1QHqfLNkUXaLFgRuG46fFn0bPLj+4jbOQ8QcgIPT/bKQNyqoYGUGfsxiPhaBzWWRAPN/i5HndUCk+aFdrD9IvC2UOYoXldM4Vdw47zxC5+kXULk+tgPizqIIhi/FXMKD2VSPlHqaJ5q7k8R7d+nrowfxStCDFH77wTt672D8xfFRb5svRfueLk4TfO9Ooj7x5yLyH+8h1cZln/kP+wFJZ0rvXvDfvfKIwY/m4RFLz7h+rP073Y/xbHn+2D996REIxhb/f7ZasxEYnte3PHPcsoutctQvT+fMfeXsxGcrCrqbBYjQZyJ+73g+UO0D3L8UWQIirRn/47nyoev7midg9g3wgM7oD/ognoDaM91HuM/h2zRzojhfio8qMmvwgEwgNcAGkDtzyH4wnO9+SBoDAJjPv3cUD4sCuwPFQUgvqt7NQLiFQeC7jpcCqWZHfTgQxH4wp+8QJ178B60WgDrwCqC/AEIkIAlBpXn7huzPux+i/2Hjs3Gatzyayh5kbPMgAOQIZgFnl8zeA+J1zzYe6Pn5QQSokVfdrLsLogBo+rwYNEHdJ23Szc592jWoAG6/zr+fms5Xg3sF0gQYCyRD1QPrPtJnDrcchAmQASAIiLk8KUCbAIzyboQHQSefsQBg7Xsf+6T4uPyuUPAI07m+fWycFZn3zC3DM1CdYvw9ZBz/LEwAvXxe8eD715H2jdtMe4bNFkAf4Phx99lbvD3bg2f/sfig+/lv5qQf/7FR6lHwzT8GwOdF3HVV+3m1ehbpjxr9BkBr9ZS1/VavX+fC+fpROF8Bv9cnwLwC2V8/cv71I+dfH83m73k+zfF58Y/J/QcS73nzeQG/QW/QfEt6j7v3DzDT5nV9ecXmu18KPfgOt4B9mYPAm506ggbhW238WAIKZNQEs3L+s1a2c4kdQFV/FAeg5Zfi94kwJyKoPUU0B25b/g4gHk0CSIqnQ7/VMHCr6ABvf25Fo2AeCx9p0wYvn4s+yz69ACQM/t/Hwbl85XMStPNsCdINNHxdEjzOHphy7+bDP07Uh8eBk70t2ADgV9b+PlDfi85cdH+XT0/dgc4e4PBp4T+KBIhhoPvMfM5FpwXBDeJ61rEbq1mp5+Q495oZMHL2FdgCpMbfCsTOdeCxZPFcMsNj3QM1Py2Ct+htYRoy96d0vzW4f0vUAj3CTMcvP8/l8tM7GH16VKZPi2/zBdDmfeJ7DO1FD4bpn+fZZjbvY8t88DT3t03f/krhBi9/+TO5Hoj1dQ6Np4P/WjplRiKA1LNx/16BBcIDAfzeC97N8M/k5SsCIcQrhL8i2GP727UFPcyf2bQtQIcbl93XmeKfOOujwXiv6B/L5+5ubsZBEj16tm9N88ztvbI/4Bbsyx8ov/gwz5+IAeR4FAlQamd3fPfzd2uXj7Fylhjo1z3/CvLrC8gGYKbOec+H97kELAeY+trOfdUKIAlgCM6fOQ/u/UsnlnfabeyArhgQDxw38HwagUPcg3yMRBEMCkgSdx0KpwgfQmDX9Rya8CiaDiAHD0naBX0oFiBU6IQhDOg9UeXr3Fgms7w4TYYQTSMhBiOQ7wchgvk+RVCEh5MI5NCug7s47bjft6ZJ4b8b4an0bOFvw9NsrHdb/PriEhhYucNagXl+NisadglUckfxvJyIsNSd0joJl61qk5J40wkHmUS/SNEuswyRSKtYs1hNBCMoow2OzIwlLJ52iajmm9Am8am/l0gkKu2E2Bk8GqZBsDi9zMalt8wtbEquJ3RrN5hiJMlG0cFWWtp5xnrH7bNNJm21eFiO4NIlOWKiWYj+2jKKu8g0o1xgt/uZ0/TDPgxXy12w4Y6WtRm3EZ+vlS1k4Irv0vdVQdK4dLLvQmnVXddHiUpZ1bJj9wDvLihvbWrzfNbP9qmaWihn3BiqKOAaFLvlq+K+XOVl0vTKKLC6c7qbOqWEML+SV5UBc8nuaK4VxFfPZZT0eDOw5UHbG0TTtncDv8D8ESaow+6GYG3h2mOYIEGP2hONYQmM7BC72vuKseYsfLzUGCpkp1PK9K0uxikTSoc9Vyy3TlIX4unS3lxTF24JwV5UX2ADR8k3jG1eTulJjgTShoZlstkOYtyfiyK2o2Kt3zfGCjraAoafTPG8VSPjmhzkYmNQQ9+iJR7kNxxl9FqjVxMTi3I0Gaa0RYWd2AbYOYePB1Fr9oacpRy2sXFBJ0ZM2fbZyLmJEx92OYUv15uY5QmmG7ZrD+v806bi6cpHKx93i+lqtLtDYIhtnCo6d9o06OBLTJQcT8b6kLWcqGdbUz4jh43nXNiVeyKNqvI11XXKHVVtVtmR2ye4WMJ1IFdU78MqMZ36NF6JrNTKhtbWtVxTESx5Nit0ssvcjgzjJWmzmVx74oP1NJJVdmmFMx+N2hqn13qdurBJyqfRuohxoqvCDa9CabONu7SOUG02nbbXr44Tq7U1nErXShmJztEaLTOhQreEYxr5MDaI69U1Vmnazd4UqrK7OMUBxCKS6dZ5KZ586caFV5nK0IPHLYUW3bJ3nWSouEV2axszCaZFb/29DhMItvG8XOaYScnH43RjWRfY7erElwuMk5t1va+o0wW/n8UjayhHmSXg6YqAL5ThCHarTfPO3Vc73+43ns3jS0UkMRZl8omyD5O6EvbSlfDlsMpWVzyI5SaCDd3Voa60/NTA0UuTHvdgqLtx2nSgNBXuuw3UYEko6EMmhjdsk2FX8yTKxAGB7cMqttvobB/suh44htR8Ktp0+j1WwWyYmbvklGUREcWjpITHhhG53S2n1oMachd0S5cphO27iYnEEfeEMgLYIk/RQPqJS6jWWsdqlCx814Y3dXeqdDW57cHENw4433FLP9m593NmQWe82lzPW9ZLxFsVal6kkmdVHpqN797DFe+I4vFU1a4dZyF+u98tnOenosOWqozK2C0izxsSGP9Yy/t1E04n+zK4TXnEDKyJrU2SMSuMVXm3yNO0Mil/FbQ7PtrHJCtNLT5lRrJKssNa14tdsyRLgWT3+vYCqVCYjKOCcJhBbpe7k0Xy8ao5pjA90SfGO0k3bMjGYb1PuODecGeF4HAB926QGsCjaXeMFG8pKGbiuAIVA99VE+6sk1TtrhhmL6/d3Uq95ZEcpovO8ezJa1Fqm2Oiwp3LDb46RVyDoiDBIVXxDKSULb2Kz3wyXLBWFqFN4ckStCWStaJ4cMEBCNblVuqNlsakY0vlCqjVAhKvY5MK4c70uj0FLVU65whcNWmEpnz7trzZkMwKdRqX2AZl0ApP8eDQVFxzvMn0egntNv5KnbzBcAbn5F7ki15OiGDejcy2avberoFezXCLHP2Cr8VUrvzDvYokGIpoPD1QVxuEpunvsL5Qh6gVWrve3jXnsCt2fHFyeH+vT9d+TGT0Dns9WrRYdtTKnCH0m5U7vVwWZiVSpOkSab7FbpZTHZsGzo6Gxl4zGdFP/HG3pczMzDJBkbaN2gpqteYTX2sYCcv8ZiXuD8RpcHDk0FLrnLvqA0N6WYy07bmGbRVqhMPZYQ7ntuflsEUsQ7IC89iiS1qVMCS4TTamq7E3TORaYWg+MxPzYofy1XClbnfxmOXl3KwngUTDTGNGu7d2Z+2eMENtJVioFysquJlhPa0owZbWHeX008Yo4sIJlg6XbgZhqzXOlgvYPLCZ0jAZr4Htu7U5Z1OF3kr0slH8M0Jc5Oa6KzDswKPQEGJLW+TdfW8IdaYekESfgl0ja0vUYCkOSimROJ+Y0r8m3D01iUxonV4CSDrmSom1Vi5X7hoKDmWbRlx2cMPEgVr32m335eUQ+KFj3CQ64sf1mubxnacWBj7Z8ZjhyrFLxOyqr3GTJyF4wyPqsNRaYdyQyikrNlpa8C0aK/XUeP36SEYaiYsZ3GZdJjoN7LNc57QT618s+BCzabxLbCq7Z4WN9JB4E3vB2l639yWnjBwGcbUYR7tC2tKomeOufV0JiAJxmqlpWuZUdccnJTQODC5zYksdh/7EpsrFixzjTNQCi9Vd4pSnHJHPmcOo1vG0t3g/LWS/Cbmp07J96l2NoZMJsaY2wtnirvIthqErczd7fc2ZjhsNdM/xPCM2u81Rmihyv8fSSXZ3ArJdenG0lpjK61KTtkPX3W+3OnuQyKQVzFJOOa1U+PPSjC6Z7eBSVMTWzU8n7hzFS84/7u9lwiG4vMxYKcEPq9O0VabTJROJwDpRUCJaMlrSW0E/eNSJDrI+jyvbHBK0t0FzUBf0IRJVvRBZgtvedvlJP5nJGQkzahjKVT2UpmjeRQcR7HZPra8p1qprumeiOnP5nk7Sa36JuihhbZjbTtmN1LcCzZf7MT6v2htpanK7Xt73FkQpEQPv7ER0hBLP+FV4tlzdLUr4MuzIoEjibomIIrXfFsw1dTl4Zd8PV7a8XVdnxqsINi1wankg8YHerQtKiwHwT822tsh1skdGFDL55iwKmRoPo6avClmMOmMfHTGakw3C7+rxnBomwG9lE9fOpWlhV5WCRMojq9sqm8TIua6SDxFzw6376bLiqj1oAFhaI2t+K9x2ZjLIyH63JnhczPe9JvDHlUHowngu1hvFRoJCK2W+S/HDiF9JPffsWnLXid2c80lWCrJRQTRtIcawstNaOarqjoiuTkR5UF873lnmaHPlrvzRty0eFaEtzBRLQOTmHNAGF3EzXVsxdt1z95E7KaIWims6DfWOK/a4JnVnirKHI7bjCAJwyYSGrE4FAwWNHG1T+XLi/VAw7goUjdIF9KqJPFydKe77UlC329EjZAtGc3zjnZzY3opsbVdRn4gsFAfrUkiEvje2rMtMh2qfSFwdS/pZjG+xYsplKqqSFiADs+LUMu6MwR42/ibIOzXcrZZEUwTy5bYRsVTnOjaFB03xmHWCc+uKRfeakRkcFLNUsWMo+FLoCn3YnVcKdOwPlwNAhkNg9dlGu7tjgGQIT6zPF0YULubR5g1xBJPAdVQEtM4datNp1OR6jWIgG5jkBAe4Qgp8sWMsUN1Mj9k37Y2iIc6QTerW8ig3mX555k6uFvlYfU9W6wuYKM6xHxU6LBTGnrGQejoK7JmIsrWQdNslztlGDg/8fYdLpMKP8g5N7P16W+0jLRfkfVmfUk64bk7nwST07ATBV9+BkASPjc09tbAjhsTukqVRdZ3VoHtO0JjLkDGzlbvbEPp6QzPT5cxqm8i/jQEtW+mh7mE8OjVuukZvl5XnWgK9rkqa4MJ+WuK7JsJbElG4lQ1mEC1yT6WFbOtqPSrpauoHijoKSjpWG5jll5VpehnhKlbTAQC1ijtdnJDLecsN0rqIml67hkMvBjtJvBqWHgeofyIPKlKjdHG8Q3q7vFfbRN9gzLnenJGm1hLFV5ajuMtdSK3sPD6iW5NcQ5xDx8iW7a+qGBjRMYEvpF/4giTVB7zkPTcEEQMzdoIaMVNtZSKwb5y5rt3mst2gkpec6S47XTj5CNqYeI1es91Ro8zrfk+vKokGZbT2jji0SbcpcYDkzTQVcaPu4fuxUypojRx2GCcc2igq8s145Y1UQ3XRdQdD9O+kKKPpdUmke8OnLssjFAo3P+B542TzaHNCEGuZGW1PXQ8YNNKdjnCrfBBRTcYNZb0NnNzBnYNo5BLNHW/6jTBA+htOFd3rttofwSBJ0MH2RGA96An5Xm1dt2SOYyu722V6dLZ112fhWtQlV0OjrSmBtiaP+cTkNwoI3XXJUKhb87WR+fvQ2wYhJd+dS1bo426/9ILxROtoLuJk7p81ZFoJSaYkmN+zxYmdIkhOqTyiT/IO9D3Xdk3QKuFO1oHcryltc2Fxob/o+VGEbEOEa/hgsciejAgS9Rzzjmc6wyhXm2O2qcXedzU23Q/1ONVt4h3lKBAN38RDvEVrt7p7gzOtsBBr9k12xeIhjIX2alRw52/J8eqURxdq6WE6saxZ+JtwvS8byGYouSCOOo1M0GbfFnoGg29fmIqDOcflpSil62GzaQ738dhf/ejYK5xHuQYxiXgoawQi3UvFuDlXrUHNVQzrWOjwXeBXpUd3NXQudnpID/gFgUKWo5FzsiLl6ZZVLiI15zMVZDgHHSERPtZoTdO6WwKwuu7BDBSMarnVz1xtLju+PZdoy9Db9lyRF4BmbUFKOQ16rqlsZYZya2FHSKApqnnNmPZ4oRNyXhwcnrntFa69HCm9q6czpMscRATIWrAv6L4nQgrVXZ5hV55Ene/uadlMHismy4OXH5aSQXSls7ySpxy9aphp7bClfG00cc/HG4LfCbBcrPJwtYrIsF3jaaXeCWK5As2OxYhdeWmaXQb76/Z06YS9c/GSHM/XJWknU70rw+mwqiN2QLHt0MDQARh9Z/k0HvWYAMGetmLv4xrXZTY+bL2AOMrhDrXyO2j6PZIoLgXMHSXKp3UcEcoW2UvybUBz6XAhgrsYL4fxmq/4wElAN2IGBId4psKbSQBCnpCIYEW29T2drpGUkxF3nLqqRbQh4Ni0dRqm2i1bN76w2yKkpQxOac6e1FtS5ry6wzpHX/WGTPgkVYWnK03w3FKHfEuTxwtjjpfDDp3iXegXFWVA962xhrvjJWoEzfEMraHbuwNDrpSgSEwUnLW+uEEtmb7q7skdie45+MoLmryCG7WYUpESDNy6xuwZWW8bw97vFaHgCJmFzKk2r061iVqW4feXM4pek7wQLW0KLTAEXA69oIlYdb0MtYdEknMXg4615CKUFMVYSpp/c9beuFEtNi+yDeSY5WplXWGMUjcxjhYEA1mR7Y1+iie3wzKhNx4OFxoHxo3wngoKruqYFZ6UeNW1BztQehVtIWxceuLI+43KwecdxEC05MenRCBoVjhYI/A9WUlruyuJ+01ZwlmdmgK1rHN/6RqQJYXnre/npzsYs4ouFAXNXo1LhWK9QubJEieGZVRTIUnaORmP16qV4GLIlZqC4ereRce8UBDU2x1QcwvXhXpCLJ7eQiIt+vujIHceHvIXrD+UdnC7D4M3dMxpr2qg5cQdKhgYVdyRlNceWw9OncMV0sEYlSzrbIyXKp7UOkEP7LlnnGOADiR7v1mFT5DkFGQN6XVORy1H/+zzE7uCqRCpQw/zeqk9yzelJk/eSgmQ8uIFQdBQaN3S4q7YwzB9IkMiFtEzKSMKHXG0tqoOBSmH/hCoBnl0DNIfYne9LfBdDprzQVHkPLwFYGK1I9iBr/cY7jsQ8CVZibtjBO8Ko4/YsCfFpSwsRw6mlmp7dVlZ4/d2r7OaUWmn602HB3KzdTKVtK5kAU1JRofnnNk2cn/TVkK32VqEMkiI5iaYx2onMPSyuSmqhb08yYphCzSiQ8xJTdskuabn42G1F5jlTm2VhNjewJASpEh6gju5uXeDJGk1Px4MA8opYtXve2dJ+1iwjDjtTCVeMrUbITRDQeoaaqvQMMPLqEbvgsrAPUiK75Oy6q/8aotAZHqiLG5NyJ2A+naY7ZAMW5u903E5N8H1Jgt26BHgbYvDU2Dxxfmejx1Fh+Z+f7q28oVmd0p6HgjXsnwNQYzDtbxYekT2rJgiOFEUoZCfJtU8dJZV9RuszxvF57aXLtfvcgj3uDuFd0nD0ttFSWRHWx21NewUmbBp8eNGxzL6cqjyy/ECp1Tnao06Hjv22N/MvoQoOz9fLRK6Ls8YrV6YUVxpO1sxqmKpuLfjlKLXlR9j6Cq97qfCoVihU7dWWUDn3mCOSGR3ApaQHbkab6lUnCRtt3R1ydMbUyrKHe+CYt7TpwPdkqqbnVrs6FuZwR/HZSOGTUGyfl9rS77pd5dsZexCLS3tS42Ats+NU7tMbQrTq3O+Opz9ROkvLiJMGi0jhalaGYkG7Y1eSxRovO6gIYhlPL9DN7MdadLAhXO/se4oX+7aLbuTpFDTkuFY73SFWTYN7jM7tpx6llO7HEFtULMJ7j7VPhduJBNbdmVzLZqehqJyTe8PXdnFTbWjznwUtN6+gH0dhXAKtwcow3qnbhRaXTGH1dnqpW7KRpRCTvemJjnK9dQQAMRms0Z3k1quK7Fckd0JJvKTeD+xQXc/W9YKbtdoCOHGYV8GGrYilheCtBprIw02uRmdLOwVB4UmpQ0o83bP+e6S76aDiBzo1Q0P+Pysit6N3cgdfMam7o4nS4XQy2A3hkPraJmmsWaD3p1qyAkmEbG6bCOJyntCPUZoevL5JTUPQMU1Ddi9vRRLBdl2orW/9liYMVSaBmipbq+9yREAfpaY7Hdcv7dXCjldtLVNJPyq58OAuF9kiB2CkzVGAGu3PD3tCck6Buvl1urgfQla+h5McVkq3S4Ncus5lF7twggSijDab/FVEME0ZLhXWA0U6BarhhyEvrCLR0nVTGe1tNjbHQriFXNMQ2VzELWBYV4+vXx/OvjyL3lVbX7a8y976PR8PvTxFsrjkWjg+J8fvD7/a8T9y6eXxkuAsM8Hcm3WR++PqP7qcdzrP/Pgc6Y8Pt8a+3gg/nzy3jnR/G72S1L4fdsB6doye7y7Ana4fTu/t9nOr/Z64PfvnwX/QfnH+fMNFKBoV359PqkMXub3K+eXUwI/+X4avT/E/PTiv78C9RUl8K9BU83GeH/VAdgAfYPekJff/jcNMMwkRS8AAA== -->
