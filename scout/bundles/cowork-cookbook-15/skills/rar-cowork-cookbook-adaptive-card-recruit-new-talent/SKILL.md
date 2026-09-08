---
name: "rar-cowork-cookbook-adaptive-card-recruit-new-talent"
description: "Generates a read-only Adaptive Card JSON file visualizing recruit-new-talent status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_recruit_new_talent", "rar_sha256": "aa330b38e4534db096d5578b5cc0e34b04c25de30b195ea87565ccf9711a2b05", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_recruit_new_talent`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_recruit_new_talent_agent.py` and in the RCI capsule.

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

Recruit new talent Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing recruit-new-talent status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent
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
      "description": "Snapshot date used in the card timestamp and output filename.",
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_recruit_new_talent_agent.py` and embedded as the fenced Python below (sha256 aa330b38e4534db0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_recruit_new_talent_agent.py` first:

```bash
python3 adaptive_card_recruit_new_talent_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_recruit_new_talent_agent.py   # or on stdin
python3 adaptive_card_recruit_new_talent_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recruit new talent Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing recruit-new-talent status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_recruit_new_talent',
    "version": '3.0.2',
    "display_name": 'Recruit new talent Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing recruit-new-talent status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-recruit-new-talent',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '78f01c8a22043700',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/recruit-new-talent'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-recruit-new-talent', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical recruit new talent status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-recruit-new-talent-2026-05-24-card.json' that visualizes the current state of recruit new talent. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current recruit new talent KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing recruit-new-talent status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing recruit new talent status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of recruiting status pulled from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardRecruitNewTalent(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecruitNewTalent'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardRecruitNewTalent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abOjRrrmX9GcGzEuX1UdIRYBdaMjBgmxCxBIIORylNn3fZPw9X+fRDqnym67b3dHzJdRlS0BmW++6/O8WcmvL3bfRWXz8vlF9+1iwdpZFkd+s7ALb7Erx7JJwVeZOuC/hVsWXRM7fVc27cvHF89v3SauurgswHTWL/zG7vx2YS8a3/Y+lUV2X1CeDQYM/mJnN95C0BV5EcSZvxjitrezeIqLEIx2mz7uPhX++KmzM7/oFm1nd327CJoyX9D3ws5jt10gG2zB/G99d1h8yPzQzhZgZNzdF2f9wPz4cTHGXbSIwMp+83EhqvyiAwu1HxcaxS6acvz4MMl2Z3UXwIauLNpXYIV/s/MKDHz5/NPPH19i8Pvl868vbma34NbLu/6z+tpTT9kfTw8tweTMLkIwqroDHxbguvKboGxycMvzg8Xb1YfWz4KPi//8z3S0m7D98fOXYvH2+fIy/9H6YtFF/qIr7bbzvYVrV7YTZ8C21wWVjfa9BT7q+qaYfduCEBTh63Pmd0lltfjb/OzDc5HX0O8+fHkpqzkmwOIvLz8uygas1/Tz79dZSvXhx9esHP3mw4/f5bS9k/huNwsDWr9+fbt+EwsGfh8aB4uvurrfva0FwhhXPhD+O/vmz1P1N3FvLvn6HPyhrD4u/lrybM/fgL7PJHOA3L8WC3wAZr68JmVcfHhboykHv7AL1//w4z8S60a+m2Zx2/1Lcn96Cn4m14c3l4CUm0Pw82L5Zts3mf942QokzL9jCRj+vtw3R/0j2Y/I/p3oLC5AQb7H8i/F/dWE5d8WP/1D2/6nCR8XwZcX2s9AxTS2k/mfF78+UuSnH7zvN3/4+Tcg+p+K0cu+cR8SvuZ2EQd+2339+tMP7eP2Dz//9ENfgSz27fxr32R/JfOv/PpY5w8efBv14Y9zwfrnIi3KsVh8q6HFr2X1v5rfXhcGQC7v+/328+L3lTh/lovZiPdFny74XTW2QNff+fHHl98A8hTAmv4BTzPw/Md/LA6x25RtGXQL3S37bgEC3MW5Pyt/iuJ2Af7OqNH4wK9tDBz7Ng7k/xzhWeMyWPzyf9wHjH9y32B8Zb9h2lcXgNrXN/T9CtD36xN9f3ldnIDcsonDuAAwq1Gq+qWwwxmYwZpV47d+MwCccu6d/wmU86f5xyIuFr/8M9FfH1Jeq/svDzSOn7in7fgZ89o+819n68zIL95scQEn+Tff7cECWekCbYInqgMlygzwSjd7ok3jLFt4MVgQcNP9IRt46/Ms7JdffnHsNvpSPEEaWTxJq12BAd/UWXz6BMwKsjiMui+F70bl4odff/th8d+L/2nWQ/i8hgrI4i0WQMMHy4Ha6nMwDIQJBBYAxyMWv/725lwgBtDlAkQuDmL/ORnkZup7757WOeoTjG0Wjg88DLybV2XTzXQZd68LPlh80xcsOj+auSEq227h+ZVfeH7h3oFUG5jzzZNFCZgVJGAb3D8u+tZ/rPqL09gPFXNQ5Hb3y+KwUwETlRn436zmYxCYXBYxcP+3PHjeB0KaH9rF9l3E60Kes3FR2Y1dRY39tkZgP+MCGOh9OhBuL0BifClmyvVnVz1K4+mecG4mYvctpJ8eLYNb5gAHvPZ97fCt4fAWpwdvNl+K9i3t7WYOhQtoACwa9rE3k8F/vaVUG5V95j38BzSdJb1FwXuLyiMH38h+VnHx1pToz6bkjy3Nlx6G1uji/8vuZ7aTYlltz1KnPb3YyyfNevp/7vRmTZ7N4bwMSMJnrX1vTt4B6B2HvxRZDJKpuf/Xc+TD1LcxT2zrG+BkjdIe8kHKAP/Pch8ZPWdo08y1YH8p3gEfqL14oBvQGpQ/KI85K98XnJ++axqBGp+vv5P/IwOA24HhIGsXVe9kIKMC3/cc202BVnOc3uMH0tufK3SMYjf6g1Wzn0EWAfkLoEQM6gyQwus3EH4+fVf9DxOfPc485dH/9aAom4cAoIc/KziHZI4bUK97NtbAzs8PIcCMvOpm2x1QFsDS502/8es+buNuDu3Tr34F4PfT/P20dL7r3ypQCcBZIN+rHnj3USFztuUgQYAOACRAweRxARgdOOXNCQ+Bdj6XO4DTt5bzKfFx+80g/1FWMxW9T5wNmefM7P5MW7u4/x4VTn+VJkBePo94rPv3mfZttVn2jIwtQDew4vvTZxvw+mTyZ6uweJf7+U87lw//3ubmwc3nPybA50XUdVX7ebV68uk7nb4CXFo9dW2/Ueunmf8+/bm0/yD3afLnxb+n2x9EvNXG58X6FXqF5kfSW269fYArdp+21id0fjqj2nfUBMuXOUiuOXB3wOXfKO59COC5sAFQAwY/Ka+dmXIE5PzAeBCFL8Xvk30uNkAhRTgnZ1v+DgQeXA8S/xm0b1QUzy4Ba3tzZxj6827sURqt//K56LPs4wvAPv+f78JmtsnnhG7nrRsoHdBndbH/uLLbr2Xw1QNGzFd/3LLqBWg6IqDJ/Hjmsm8dyRy+R4YDKM4fhfVWSg97Zq1mZbt7NWv33JHNPdwDjG7dn1dSHj/s7HVB+wD4svb3Gf5GSDMh/64Qnw4FjnSBOR8fKrYzgQIFZkvnIrZbUBWgIP5SlwdJfH2SxJ8Vomc6+QOPAFyte1DYHxf+a/j6oJW/lPutif2zUBP0D7Mcr/w8U+nHNxQD32Dj8XHxbQ8BrHnb1T024EUPNsw/zfuXOZaPKfMPMAd8fZv07R8cHP/l57/S6xGfr+/x+bN28gxhAOJn5/4jYgbKAwW83v2r+IJFHvALSGzW97sjvqtTPvZWszpA/e75TwG/voDcBMDQ2W/Z+dacg+EArT61c1OyAvULFgTXz0oDz/7ttv1tfhvZoG0EAmwbQSAHIXwUQ1DPgciNh2E44WCuC/kI6kCoC2OeD8asScy3CRzbgEcBia/XNuxAGJD3rNevc+cVzzphJB5AJAkH6BqGPM8PYNTziA2xcTEchmzSsTEHI23n+9Q0Lrw3Q5+GzV78toN4FOjT3l9fnA0KRnJoy1PPz25Frp0NIjl34bKcNkGp2bV53Ys7rmhz3eOaxuEyfcoF53rJdLMSLXcfQjsN31K8Je9217Od1jS2LyZBbT0IQ8KR4vWGL1qsu2brMQ59/FQRq0zBvN6/ooi/WyZlJma6YhriQd5X9RkVCeUO9ULFKXbWV6dY2N1iwl2uVpBCpHXajplQ761qFw17SMdk70qOwdRtSEbvDZ1jK297zjc5UV/MA9RMEiNmCh4noF3gq1bE8AEqdg0fQ/4qsBwi4FcThPsxs4/X8D4+MKKhrDgPvvYXFM3Rc2+wjrS7SzsnTjb+oFk5Q+51IlhVIiMXhsZrlXQQS4NJ6ywzrte6gLeoUjTrDRmsuHpjuZeJMKXutvKD5VKib21VxmMXW8tRTLzr0erbNhXP7MZgGMWJzvEFomVSpEXsfjElDobYOEsNC99unNC5qcp4pOs6bndRTheBd1Az/chgslHppJ/dty7DN3uZjNnaqISLJWSunkonbSzMi76FTcOUIG/grkvnzK5Kf42l2cTLEBTrBq3wnND6KJevT8wxNTKJvU+7DbVfpnx3dfLa0K+77tYZnFY15yDNlzeeLHe0GOrDBtNjZaRxd0O40x2pcibLzr3NC6qhMcdKPkin0eLTdRpqlbjemoLNhPFmHE/FiVJXziBqskTIumUNealPaYJd9DrWSLYoxEBq3JOfIg629+/pEkv2JS/agzjwwlGF9Uhqi12XUKK728amW8X1WmRuN24oypwx4ZA4bYWRjuDMz6hVZ/SaxYacT/CnPD0R0Coad0d4SiynOiVjUzL82NHnfC2dRUhudIrZ3O11sNbT4+bs5wxTtYcazxGl7kV9L8HHarppS7acWkPwqrPBrGLjok+3CzopVyEWjeVWdfQtWnahd8wdOmwJUT06Mk6WdoF2sulfN2rVMSrN3onVWMIEeiiR0jTbpT+GTryx96pM5Dbu4gyGcGbF0p612yyJaIXSKzo/kbaJ00seNU8bXB2qNRIKMFM5B76qNuYomXeBxF3tLiDauZam82Fy050cNFSx241ByN8aM8CXlOzza0YParrKzdMJMp0DA59Ev25Rv4Y4R7iX99bShSo/0gIztrR+MDWjERmaJqjNjpIKbL8PizJpKBPZQeSe1XpJjgx/75+wzMsdqz25N3xk9/t8ySG3mjwJ69jOz/uKnygxVqhDKCaJuM+sg8HLW2ybUiuPWCeVSmVIaAxh0W6DE+axdeVA0sSfewmyzI3RBcJm3Q9Z1su2BQacbWPaOoW9nSKR7RVmTwu+se2xhjvSFT/c8+voQBtGlpJACwHQX7NtCpk9f1KNfXW8gtL3T81QE5Gzb1ddxIu8yFDMkI2Wl4sHbuMxp8E2WVmZAlutePnOYJpI9E606dr6ph2QcMeiKV0fN/qlc9Zco1YetaS1HSfSBdJ4aY/LWc0YKXeopyNCZKd+GDG+V+XCYlqLHzKNjGhuV/PxikJMhgq9lrzWPgCmLDZJOnblHd+5F5/AuZ1HVas4xigl04XSyVtjK5wUvpU6vSI3iNO2Ju334v4W3kqDUG/02S2EVQVduU1i7cQGsLtKu+6mUjrndMD5eh9V6G5VwsJUYFu6rtbJaZDSpC8uE5IPHrNi8DvtatGGRRW0uFEsmaKkgmGn6XTWB6OiQtYz9n3N4o12ZCBsy+tL+cYZ1Tkek+pwIvwbHp4ve51d7caUgnGiDLX44LHXNiwIozVy0g9WWxnNnYnT0tiYhDtr1k53vm/iY5kJWFN5tHhSGgIzZZtl+JSgN6kU6eSdZ5iznC8pfavgeK5ablQWUD1SK4CAK91OKEZne7LCAmpZovsjfTkSTp9hCWk2ArCf6huT6btMuI/X/H7XnCmOkDxAKtLNpQ52hx0birkZWMKNzu6bUE9OEpGJlytZbnfJiLCWVigIl6y2Iwz1cGEdtU66i9sluRqMcLOMEdRVuQlHlx03cEmMt5VCsNUNw2pfl47Rcdvl+oQqTgazsaCztVmvz8bOoMYhjVa76/EMwwHlxHaMe3ytMrmJnc9UqMbDft9HG6JmsytNatpR1c1SrlmqTIXjlaHTVOR5zdpW+XndbZkQ2mZsutHSycVQoYfo9GI6aeNe6eu0Vnp4m6XpmZFS69CvwzvCE5U3ZZhxl8u1vfGjpcmuvSjHYNyiKEjW/VTKdB0ql120VYwUvrMce2L3B8EmIMMSSwsaC3pSG9TNy0Zu+eBIUfpZObFCCEuYt6Ldk3tsBe04LXP5xljjvj7CB3V/DKxROQ6qVPLG5jzBa/KWWru0hnRlIA0yMtwrn5F7BXTxdSpeoDGGr9VE3sYm223PwX6tDVI09uKdOh263RndJ1J/zA9LqbAj0eCvSnq8isC6PcNf7mxHBOE6zS43M9ai7Gw5+rg0i5gxMb0RRDVvrMoUcrenrj3fUpW1NaHpah8Gt4Zg87BPtirOUpV7tLS0WA/9zbs3uxTntoJ4uG06pM/D2N2tkKbW9mpalrC8lkxCOcibEgaboLjEOEQn2MiqCCe90pQVKr2PVSk67S5oomhMncMeI15xrdwE0HVHrTSNj9AzZBpoRuTYeTiMdBdvBGrrKudkJ8H7pbWmW+MuWDxF6uZ9WbFVEBfoiTiarlUe7GYM9BVZxnsiOVPSsSGUixPzbM+vrIze+8xdhTkrF+CtuxQ5czm4SYwEWn0LeWVS6Z0jt5cTasq7hOP7U4NMtbhMsnsyonF1zihxSrGgEG74tYkRnxozhbjKrLf1KYhZ3zmIYZuLYGXDbYyPWnk5CGGn2yGNkQy/1E2vvl9S3dXMnRyHto025cVRpWUo5WGflwAkwy1nJteYgi6YezqWilfxcKMuofpw2Imo7LB2vHJdrrQIxhRY+bofh5Olbe4XFWy5JXIT7HjKhk8pLtlqowiUWJ4OrAA2kE47wse+B+FIt0eq7cSa26RL/UBGgxMeLp13XtUN6qAV6EI5bJ2dHbc4Ou4d0JuWkBXnD+mQEaMIBfxV7RVNPAdX0KyyOy1khoHUj/WGXgUuyhOIWomRpu8TMfTqdC/so0bTbUoWsWVPYR6cUFem58xIkI9bMhf5hruetSbPdqngx9TRr0IEjjRGZPGJknQEYaI7qw1dON3PvnPAKJLZ3CBjyNUk7s8ZkxOQCzrgCG4p0bNXQkYLPHEXWvfAu6M6SmW4Ctaynu4GkxESbjpnkwfHW3aDM0J3rvySPnEhmh9XXQMarZBPt6nKKQdoqUMRHdwFls7MxDq40fZ2EWXQnCX1xdKz+9WcIMiuZdO7ra+X9ipE54Ecm1R2Apant57jZhf01MUkxVLhMFoqYJABa/n9EsiVkMihLkI37m6eK3jZ7p5h5bqhT5qzb6z1yFQ0kt6vbHM/XrITI5a3kvCPNcJm+k02l+urZ8J3I50M4Z5fsvCmGitbpfpuu5e60YK9UmZLl9ss95LVh0rJFP3lCHFrzs/3umOYNjFKa3LcMUeXzK10EquEPnsK3iIbTy2mkZCC05YkDxyCy0do9KyDCDpF6dpvDUPzmUPEIkuIuxHEqZbTuGQvVWemGtjf5NDUjPYuvoTQynQCbZIShKpavOcRKmf1GvSypOCja+uUpo5AsQzteVyJBp7WqUJKb/FrFN68/U4eKfFAQd0RjWDHkbz9kXfx6AzV2IjKo83Ug8GGlpgeytLaHI91ZuFeCokTMyZucxG74dhngDst2xK18kbxhe1gcbqdZGc02U2fHlZtW1cUXSvVMndpdXMBOG9cM4EhZWZFOMGkVcI9Mq7sEmWKwTdbwvHJlKk0eRmgNHRQQ9GmTil8bq2b6up9uc70qJEqpk8zQt4sdTfH122joBjm7rf7xkUtzKvlhFVzeJL2RXncJdfkDNotxQy5RgcZcoj1VFtfBfN2y3vTKAp0ahji5FM32TUaxOT9FbJFG15HCbHab6lrCKEFcboMgHdQBg5JsCnfuRMPYzyO0Df11KBVchBZks0P/cjjK0xb8xfFiKZcbxiaiN2CMTeZVuN6R+DFbaBYzMRYd39YUnF81O0VeXZ8w29X1g6HVuXxcMfbHdvRcHi9RqBXCo6ypPLyznBwuY68RrqiE1Wt8/LW3MQdbcoEk9kH32Iil3R2uXWgxZXlUc1xbJ00qu7JFJhYyVntDVWJqFGyenk87I7Ybq9v2g3ovuAp4juY4YqrGvqbk2yMmyvkeWWEefGpaALQqqj4Oo+CNVnF6+BAnGg/IzbHHpD9rSIT5H4auh22UvsLwLbUMhBAmhEe3GRtdGu0H8y1OSl3pdmdV3YztcXFXU+9qsJ3yECufX+sJ+VG2CieLNujUiRmoynsMoGMCjmlGc6Yg1tEu0PjXBnWprCrIgfKsL0LF0kY6rxZd5cV5UqqNzEQRSKcVpfVksITZL/B6ylZCYEoH/btKXbOELls+xXBLxmO8+UasrIxs0PBt0N0aHQRN9VbKUm4AekCnvKIal3Ladwmau83gmeulwfnkOPIxYjCJTu0HU9TCjw4JeHuYDpYYQm+SrZ30BxVcpSLy1UsECzO5G3XIlS86UdTadnVlgE780Qh9r7PWV2KKKobnTYWl2xXx+hs+VeILeN0WXQ0WVb7CPSh6G534jBG9+XVVShWWYkIdW7kTr7a0wwWgtifhlJlp6h3CwKX0BYbkVyhLc1aWrIPHHGB07xJYbrdqnsm8VKey3eDel8N/mYjEqSMFju457ktgeuOkB7MEsUEtibEm7wv0GLSBARxuuRI8jBxw9FaipI1xuelx51rZZ15lXAh/dU16pZikp11XeG3+ZEvipHYdgMimB7rEcf9nVFMuCXHtC5TSLlb7bIF6Loe6PBcR0VhsHRFa41z0FVnObHNinIknz2BjagDI0wf5gkW+GfBtSC/FfZpfYiPZnhXT6dldpZEVNwdedLCYr8fOEY2zX1Wo/cI1w6clsi2l/B5yBdJScGEYSQjGQqXZXlLkxguzmqI8wXoPpZnN2GkTZsF9Qj67ASHAo8keE7zxRgvGI0YcxwSplgnuVxY+8vaClepx0VX7wxzy3zEMyvjkSuuJhMOF3sNPhPsmoYgctgomCsdAOgoZ1c2pkOiHs14c9XWg7ejB4nmSwHrrofOX68T14z7EL8emmyYohZpk2hbeHJ6tRSiRmUY5Tf3nuqXwepyzpvmfgKsq6m9aK1vjcOtTUqxiclxTsNadk9sC4il7XDIH1VW7vTrNqo50b1xAozQ0noJm2pOl7vyUNNOGahsku+3GL9a0lgmapOpEZdojDYHN+6rNdt2atdZo7ieaC6n7SXSrmE12XbqtbsVKdlcigzzrhje1PFGjjn/gqKd2wMw9BiGVgb6jsou7FtKTLtMbznh0ik3E1PYMEyuV155k2FEVyDmcgYba6fqGinGYJHjtBMtV+c+57Nph4/RyaLWaJ5neOEYN8w5XeoQ1UoIv7CxL8ThBvbBtYAi+HCFnP4cTCLn0Wig0MOhA53A9s4amZoqNUOa+N6z5NBQrqfDsvHljYqSRCs1/Fa2L8JhCM1IV3uKvO32MaKq5x17UDG+8uQTlt5EVimUlIfJE3a3BUmpLFmCkmQK9VV8lxIQEQmt5A4tWrtSQRqi7Q5VRbKaZOskreyajPFN6OPi3qEOkNFLOcrftrpzxK8X6xDYSQFbyi1SaDHBt+fdLlkuh2u6HG5yZ2JMwERHv5H0DjEv2JWsfMqQ4EbjoqHw+oqLSAhQjaR4LpJVFUxc3SZQL+tdnV0d2lT123RlCD9fZ81ZltNbryyjK0v7CJxPl6JmDcIROIU8wuurWG8kArAhf6yTKL0rVbOUEcn3ltsrl3aY3xqJfrnblNKcCSG8DPlRV9Om7tZstHWUPs/iDYMtdY+3vZsgV3uu6e+kjSi+uUSKHtvmfgCRE3cmMTwxcYjAZJRUSlteYePdXcMRf+en27YWyD2XhnvCYk9HkHfBECwvZHRpliTncZ5YtGx2UkzIpbdk10vdGcOljOyvF8RgVpZB2aDzb7I+9djujlVJgfSll1w8pUXAlt67czYbaR0b1XE0lYG59h2wYc0ScwoHazjQKYx7JeZchoi8qQQ36FvBySnQE02pc/F983Zad0279FHG4Q5+6FOW6hLRbqtLtH/Q9lCyjgZmpNw+MVD3HMP2yS+wXssyVb7SwhLx1NCexnVxcYJmG2iJfvanm0EjIo2qhkJaqO0Za8k9XZBCJSfvQmYGAPnmwgVVU9hBgLndquuD1guuAy1FpNAtcZTh3IEiQ7jNEyeHL5daO3OyIdsI62EBqR05sG2ODgaOreiJrLFTo9jdUQrolWUuMRMEo5ugE8cNjERYUWPK0XKKvXgIEPgYdcVplCRkFWde1POSsbJU0U995kYUBMuGPLSn1uKaYGtXqEI+9sVa4umV0PQJhMoYc9HUwczTSAB0j1QnVeu28LGreO0YIDRRcWkb5Z6CZt59HJSaviBY1PHkfRkAijH3hOmXtwGPMqRvTVLmCS4z2pKzkZs/uPd+t06RMIiYxtNrvre88Ahh3nZ0jeSC7FbLVTGAZo52AWWiK+9ckXvTMdj0aIqXG0cuZaeB/INqeZqsNyrNKUqEEzQ08QZETKD7o14+vnw/onr5l9+Xmk9U/p8d7DzPYN7fk3icvfm29/mx1ud/XaWfP740bgwUeh5etVkfvh31/N3R1ad/diw+z74/X0F6P0F9nv92dji/mPsSA1Rqu+b+tS2zx1sSYIbTt/PLfO38vqcLvn9/ePgHI8B1FDf+164E5nTg18v8tt38/oPvxfPB8PMyfDvN+/jivb1z8xXZYF/9ppotfTtpBwYir9Ar/PLb/wW4iuU8Oi0AAA== -->
