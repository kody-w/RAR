---
name: "rar-cowork-cookbook-ppt-exec-perform-service-tasks"
description: "Builds a read-only executive PowerPoint deck on perform service tasks status from Dynamics 365 F&SCM data, with KPI, trend, issues, actions and appendix slides plus speaker notes. Call for a monthly review deck."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_service_tasks", "rar_sha256": "efcb197c028b832b895ac107b8c4edff168470647e7f34973ee89848db92796d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_perform_service_tasks`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_perform_service_tasks_agent.py` and in the RCI capsule.

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

Perform service tasks Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on perform service tasks status from Dynamics 365 F&SCM data, with KPI, trend, issues, actions and appendix slides plus speaker notes. Call for a monthly review deck.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-service-tasks
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-perform-service-tasks-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison basis for the trend chart (current period vs prior period).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_perform_service_tasks_agent.py` and embedded as the fenced Python below (sha256 efcb197c028b832b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_perform_service_tasks_agent.py` first:

```bash
python3 ppt_exec_perform_service_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_perform_service_tasks_agent.py   # or on stdin
python3 ppt_exec_perform_service_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform service tasks Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on perform service tasks status from Dynamics 365 F&SCM data, with KPI, trend, issues, actions and appendix slides plus speaker notes. Call for a monthly review deck.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-service-tasks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_perform_service_tasks',
    "version": '3.0.3',
    "display_name": 'Perform service tasks Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on perform service tasks status from Dynamics 365 F&SCM data, with KPI, trend, issues, actions and appendix slides plus speaker notes. Call for a monthly review deck.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-perform-service-tasks',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-perform-service-tasks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47598ba14f88f413',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/perform-service-tasks'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-perform-service-tasks', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-service-tasks-2026-05-24.pptx.', 'review_period': 'Reporting period and comparison basis for the trend chart (current period vs prior period).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for perform service tasks reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on perform service tasks for a 15-minute monthly review. Produce 'ppt-exec-perform-service-tasks-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads perform service tasks data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on perform service tasks status from Dynamics 365 F&SCM data, with KPI, trend, issues, actions and appendix slides plus speaker notes. Call for a monthly review deck.', 'example_request': "Build the executive PowerPoint deck on perform service tasks for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-service-tasks-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and comparison basis for the trend chart (current period vs prior period).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user needs a 15-minute monthly executive review deck on perform service tasks from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPerformServiceTasks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPerformServiceTasks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-service-tasks-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison basis for the trend chart (current period vs prior period).', 'type': 'string'}},
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
    print(PptExecPerformServiceTasks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916a9ObWJLmX9G+E7FVNdgvIBAIT3TEIiQQAiFxESDKHS6u4g7iDjX13/cgya6qbndPd8R+WjlsCTgn7/lkpg+/vtltExbV26c31bfzBWenaRT61cLOvQVT9EWVgK8iccDfhVvkTRU5bVNU9duHN8+v3Soqm6jIwfZNG6VevbAXlW97H4s8HRf+4LttE3X+4lz0fnUuorxZeL6bLIp8UfpVUFTZovarLnL9RWPXSb2oG7tp60VQFdliO+Z2Frn1AiNWC/Z/q8xx4dmN/WHRR024EM78h0VT+bn3YRHVdevXHxa2OwtTP4S3yxI8i4ZFnUZA0kWZArp16dsJ0C4vGr9+XzBA2wWQAkidAd1CIHPld5HfP6R8Bzr6g52VqV+/ffr5rx/eIvD77dOvb25q1+DW27lsdkDH81MV9amJNisCtqZ2fgNryhHYNwfXL4XBLc8Pvqr/Y+2nwYfFf/5n0tvVrf7p0+d88fp8fpv/KG2+aEJgnsKuG99buHZpO1EaNeP7gk57e6yByE1bzVoD61VRfnt/7vydUlEu/jI/+/HJ5P3mNz9+fiuACPZsr89vPy2ADT6/Ve38+32mUv7403s6O+3Hn36nU7dO7LvNTAxI/f7ldf0iCxb+vjQKFl/U84558ap8Nyp9QPwP+s2fp+gvci+TfHku/rEoPyy+T3nW5y9A3mcAOoDu98kCG4Cdb+8xCLwfXzyqovNzO3f9H3/6R2TdEDg/jermX6L785NwCKIeWOtlkp8+PNz31wX00u0bzX/MtgQB8+9oApZ/ZffNUP+I9sOzf0M6jXKQFl99+V1y39sA/WXx8z/U7Z9t+LAIPr9t/RTgQWU7qf9p8esjRH7+wfv95g9//Q2Q/h/JqEVbuQ8KXzI7jwK/br58+fmH+nH7h7/+/ENbgij27exLW6Xfo/k9uz74/MmCr1U//nkv4H/Jk7zo88W3HFr8WpT/q/rtfaHbAG5+v19/WvwxE+cPtJiV+Mr0aYI/ZGMNZP2DHX96+w3gTg60aZ/gBvDjP/5jcYzcqqiLoFmobtE2C+DgJsr8WXgtjGqAiA/UAGjmV3UEDPtaB+J/9vAscREsfvk/7gPiP7oviIfLsvkyw/a3ZHzB85cHPP/yvtAA1aKKblFupwuFPp8/5/bNB7gOOJaVPy8HKOWMjf8R7P84/1hE+eKXf074y4PGezn+8sDu6Il5CsPPeFe3qf8+a2aEfv7SwwW16lle/EVauECWIErnEgBEKFJQcZrZCnUSAYD3IoAooGaND9rAUp9mYr/88otj1+Hn/AnQ2OJZzGoYLPgmzuLjR6BUkEa3sPmc+25YLH749bcfFv+9+Ge7HsRnHmdQJl5+ABIe1JO0AHnVZmAZcBFwKgCNhx9+/e1lWkAmB/UJeC0KIv+5GcRl4ntf7azu6Y/LFbFwfGBGYNusLKoGoP4iat4XfLD4Ji9gOj+a60JY1HPhnQuin7sjoGoDdb5ZElTDRQ2Crw7GD4u29h9cf3Eq+yFiBhLcbn5ZHJkzqEJFCv6ZxXwsApuLPALm/xYFz/uASPVDvdh8JfG+kOZIXJR2ZZdhZb94BPbTL3MFfm0HxO1F7vef87nY+rOpHmnxNA9YBCzjvlz6cfY56EoygAFe/ZX3Y40910rtUTOrz3n9Cnm7ml3hghIAmN7ayJsLwX+9QqoOizb1HvYDks6UXl7wXl55xOD5u23L7nudznbudD63SwTFF/8fdkezNWiOU3Ycre22i52kKdenl+Y+cfbms7UErcqDyiMjf29fvkLUV6T+nKcRCLlq/K/nyodvX2ue6NdWwBUKrTzog8ACks50H3E/x3FVzRljf86/lgSg8uKBf8CgACRAEs2x+5Xh/PSrpCFAgvn69/bgESeVNxsLxPaibJ0UxF3g+55jAxc14ezIr94FSeDPedyHkRv+SasFoA5iDdCfvRqBbARl4/0bTD+ffhX9TxufXdC85dEhtiB1qwcBIIc/Czi7cfY1EK95tuVAz08PIkCNrGxm3R2QPEDT502/8u9tVEfNHA1Pu/olgOiP8/dT0/muP5QgX4CxQFaULbDuI49miMlAjwNkAP4HaZVFOaj5wCgvIzwI2tkMCiBuXk3pk+Lj9ksh/5F8c7H6unFWZN4z1/9nbNv5+Efs0L4XJoBeNq948P3bSPvGbaY942cNMBBw/Pr02Si8P2v9s5lYfKX76e/mnh//vdHoUb0vfw6AT4uwacr6Eww/K+7XgvsO0At+ylrPxffjjAofX9n/8ZX9Hx/Z/yeqT4U/Lf49yf5E4pUZnxboO/KOzI/EV2S9PsAQzMfN9SM+P/2cK/7vyArYFxkIrdltI6j238rg1yWgFt4q/zYvfpbFeq6mPSjgjzoAfPA5/2Ooz6kGykx+m0OzLv4AAY9+AIT902XfyhV4lDeAtzd3jjd/ntUeiVH7b5/yNk0/vAF49P+nGW2uR9kczPU81oG0AZZvIv9x9cCGoZl//nnSPT1+2Ok7QHiAQ2n9x4B7VZG5iv4hL54aAs1cwOHDDNQg3UEsAg1n5nNOPQAeiDhr0ozlLPpznJsbwBSYMv0CNAYh/vcC/akUPJYunksfpfrRBQD0+bDw32/vi4t6ZL/L41sH+vcMDNAAzLS84tNcCz+8AAZ8g6nhw+LbAAA0e41kj9k5b8G0+/M8fMymfmyZf4A94Ovbpm//k+D4b3/9nlwPFPoyB8PTpX8rnTSjC0Df2dDvIIeGZ+AAeQFPr3X9l+b/PL0+LpEl8RFZfVziDyLftdGz/s09bFR4fy+J4n9txp4rntAG9LarqAb4DxrOqP4GQo/yPEc9cM+PbltVcyV6bezmbjoCC5/XP31Hmoc4AM9BVZyt/Lv7fjdi8RjnZsGB0Zvn/z78+gYC3p5bhVfIv+YBsBzA38d67oVgAAmAIbh+Ji949m9OCq/ddWiDXhVs9wPXQSnSRZZrZ40tnTW1sl0UIZ21i/teEKDEGicRAid9MsBwisR8f02t8bXnUEuSIjxA7wkAX+Z2L5olmsUBhvgIzOj//hjc8l6qPEWf7fRtMJlVfmn065tD4GDlHq95+vlhYAp14CXpjKIJmch6sK6sYEcXYlQtkhoLbFDtZd2HbTKZtcO3rDDRl5N1yDSLdbdZuj/SE8IH911giWSunbc5wdeHJbZs0qa+WvXkQs4RCjLvOJz3rmzlx7TOlheryPRlJfOVi6KgI90TF9niKnvMT0nYWrl6uU+1cdgK5O4Mk0sP5u4XlitCdT0S10A78MRS7q4Nw6WbXdEiXg95EJaFg3YQpfaQcHDtsEY8oF5wHk5dYCojzNpcAA3SUMACCknQJA0nxZr40wE5lOblRu1MQr6PMrfDdgW81djsXBSeoDD3y8W+2atTaa7T47DLW09tT2c7VnladEX0gOe9lMfSqvJlyYWS0yaCYAgi15TYmiRCAf4ZSUEu3LYiZRQF7Y7GCQ+D1alOL112sSG9LHdBVHYorQSuFJzUq3mXbRPOrvL9YmYW1eVWe1AVR3Bvt5RNNr61PZqrETtmJFFfnc3BSp0u0mSSMWyr3+6hfm2c0HRb7V3XQKetchIFPmmP4v0sZMuC4tSJNDoUVrAsMs1jZ8XqttVkS2APwm3Thb6o0nokGAa+Fjgv2CGEJWCcqg5sHcqYPRi1AblKcRiaSLPKC2TiriJtrRNcepxdr8QM3W7bSpd4hlORvCjCbRawY80wB0nnfduMbyssy9ibUXrHK9Kf19nk5zIzUeZJEFfC9rxyCQ4Z62QXb4f0lKJ1CatajNyCletdNnG2SzfKykiYghykYAXSProiwS6GZV8lpvha6Oebt/YjJ3OIzXAslaOc+MM+VQJS3yWcVAhHRlntAva8hhFWOo4cefSctXrfqvVeHspQRseStpGj5h/b1tQv5M5P+SFgNO8qemPKeSyb3HizDsUuNC+64EX+OTnUWbtmTiuj3cLXXA5hPVxvYPLCFXweNUhpba81xGjaldquCxsbMj3OfbvMFcTdiP1Un2KPlxKfu5jLSwkCA9tTd8wcwN9JcBo8sW84uVvBnL46Md5VsPxTD7khFa52sJG0E8zzWkzYdVCCHD5tI1Poc3NdJ0AlY7yphtJUVlQrIK9Z1SYIaYxav9PL1EUMbR21UiVRGMNOzFG75MsbYXkJ4rL2RPmJur+Xp33hbcbRtY9ltvOPDCMjYcu7Bu7ziZcIXC7LAe37OnnHV3hi4rlFh9gGqXn7cNqeQ3DVXJZOzjDe8pBd3Vo/RN4ZWMW9Izrdln0k6T571fPUYAeiuC5b3Yh2Wijg8XCHD+R9L4M8abvDGTrc7V3E42hNKjbcZ4qSN9r1OGAjMo6EeYBJAcf0FDnqYa/XNtSVhxN/Ox1GHrdFeaQH28cjljZJVRqOBqSB+tHdKSQXo1DjI5o4dTumjHK61x2xWvu9rjWQshWQy/nSKUl6I/P0XtNr1Ds0d32SPOtinikXOmhIxw6Hc9xEvW3za9tw++2OSKi7ttYunoPi1iZJfLIod7IHgWDL1vEAVCr2w8n1TrCN4HdYMIWJvK5ONsu0hBHgTND70CjREtYOyT7vMhdWLN/m00bmu0lRj5aF6X1Pk5qg921LAxxDDG5ViHV668dJkkePQPM6PW19/1QOt/u95/cdSUqM1hbDkaK0QmEvI9ruW1gSJqi+amv4yBdNgcdY2DpZkfJQXiwPLAER56WDilsIBpVDk1WyV5I4GqXRHQxpw4mZ3pNDknPZvYQqlXZ21P3gXKSRyhPiIu2W+5PmJN16c6zxc2h3QahdFX5CljV1VM7edo8xOxrpt3e8l+gkZKR7hjkUQW4a3QK5StFMEqc2t0w4R1U0bmfuhoSoGYPpptrh6mmb8TGuVILTymsejP53fsPzZNe5VDjsd45K8lta3O8JzzpMioQacXskIjpKbWFbXi9nTYAGX2TjLZexrWWfXcTci3SBGxeHx/lsM1GCiw1E0IkJXo6cPGrm5qQczucCKRC3o+Jd5Dt7uaDYJCxxIXJJmEh2oBXkckeOIym57GCYoFI4IM/9fqK8oDtL6zaPj6FpKxdcT7E8HVY9qGe7Yx3p8GbyO/gSitHdure6stmpO2HKra3Ty6geOOXNbi2f9pHYYqWbq3KXXeZK61so2MhFszuG2iihn5ThMpM36i3004RRZKS4pVc3RSZ+O21qTfD2dWZ6SbCyTkwXNJRXrOwVQMOo1gaRVlTeQV1xJR1kSm/tclxT2hmdtEu/tsOC3t25XFT18S4QzIj1PXNXNWurxZuIYXc1xN/QUtiw5bDeckpqpYxAdRvEPh+3Uej11OpwlEe1yqud42IEtGnxDA9xORJz6LRtuOttXcnZTqMh7zLteC+3YHwURwxr0GFHH+L0sHE8fRWn55BOaaHBK6CN1p+uGbzH8r69CKjqanRsGXtBpOvdgdsaWSRo6XRSWHjvT1R+VEanP/JRwzY3iuFCXt/e1tupKDC+E8QTGzp+uUFuqarfbzecGvlOLg2+GER4z2cifdodcde4pM712KVJvnPdsmVuy/og4/FmX1d1F4WBMtHFWmRqtQ72TSZn7gaSAu0SKzsxjR2FxQ4RvNcNRNeSpXlKxH2COhu+PXntcQOgiJ/MLK5OKU1LDiNeDslyNMUx0ka4HJEt0x5oHYuscOemmBrghGz31KSJl9NuOgjCwT8KDXNRI7PvJDnoRSxGBlQTU5iPLV43FBnHiha+Qlm7lbeKLFJLANfs8sBAan2yrmOubSR0WPIR0fD84DGYjmR47uFufaWp44RMA+aw6nKnyX04Wgq6rk9RlzReIS2zO3dQ1xF51nCk22v7IJv6tDLWVpN6W5vGUnTcI/us0k9yWiv9qColezzcGpW4bVdeevBVw7v3ZqJeNxyAgpyyL/kVW540jzalTeoF8tTTm5EK02Sy3HTPhYy1ymNXpgiiYWCeiapLbprSmK+3W1rnQ8vabvCicbNrhSUhF7l5uT7sJrb39qKdnCzYIWnaTr2+yAIdN8ZteSpEelvKwma3zBuRSJTV1oeZq9H4uyA2XWnpwDDGqJujwW2BwpgKqhyPQ8gpxmptOsggKtZ0ZppMwZCjHFy3muAHuiETxCbI85NwZvI6GmR1l9CyhTKMJlfK5crb+rR2+SWRMNcJOmRwreXsap8QU+e5fXBXIohfVkTB2NSSvtDGnSbU5J6niXqj6LqnXc2+RYOZ3OihP053tSTWqi6eNCbY+QWnCo5nRHAaY0OxZbboqYj3vHmVqc25jRoT3m8HqrqszteO5aFUMZkNkD089puMFxSvpOxT6V9oVr5loswWQITAJSxpr5GEfwZVIgiES+Tcsh49KpqEsKmyJTgLn0xIcVZlx/ZDy+ssW5RwVAro+XYvJ/sQx4LARGN8FO6mGUo0m4ZFl5IkGEHEYCnr3Elw7HOiV7l0uo/CyqhhIb0dh/6ibiZXpyVPRchzjNCkLiuIPCAOu1HT0jadhtDu1zV6yA50Em3Cq6tAt9p1WKtmy/gKGRlIx9Zu+pU00FSxCYU66pTO8C5UBxdHQ28BxrTTdaoVHI1CA7Tj5r6TBdVBJ0Is2n5vXu+rRm/i3IGjfdY5F/dWHSqrD3F2rZTdgdr3/nlV20soRAJ0uKsrer9X77d2jU+WlB+HUzxwvH1VKMs/ZCJiMZOB3NYxx1BoldLnuMLtZhhTfIiu642sJY28bHCmJ7aHkJP30RWarIw+K1Zy8tJqUwfc/kZgew+yyrFbD0uBRlVpl6CRJepoqHd4RN/lNF0OtuOy6il0L3uxYpsUonb6CUQb28XTgeFc9ZqaohO4DOFLrRgnx9KViH0DLH6FdiMhGzZzgChFqresVaniYa/kKhI6RxnL7OXNqlHD3Rlp1SpHEuqDKXRq/ry5xwRfXrGKQ33PIG2/UmsqGpxg1RLw6F841S54bBXXV8XVLtXxfuH0YhiJTXJLraE0kgPhjNwYrkyPmQbyZpZRv1+y8ZlSyOrAoDLZObcdQkOnrpRQZ9waZyN0KwmTz5YDGs3K3ds8X903m745Hdd0uhMwZJQb6qxZ9eaeIdsdsjIwvQsxyGhajOUxSlPKQ4wLjsUgq4A9hGSxhgRsI0NC1m2wNJelK5GxkXeSRjG8suUFH5ab82p1EjZHOEIv/VW/h3BvKrSbblH0iAAPpb182uqOfTsZp27jbNSLTcXJRrpC95CmTAWiKTuLiVGbbt2VCszOy0ICs/cOb1AFP/SNj+SKkhCqutIpTg7QrGBFMBaLxSkyZHSortJ0ORf6kKaeuMcZ78xHwXKHWuiGWK2ri9Ks2Wzw7zRT3TVZh9LWQuyl2dUjcTyCjBETCwVNfeXU3lBL8QVene5uZWEtIbaU6RFHZhWsYAMIg6pdmnNb2JskZaoFCO0MXId9hb0m1hIJp9r0a0wc6m6JiyNZ58YeRfMrd2pbHBUEsrFQAicS7h4QGbizo+ziSGWe7IaKVWUrPisMa1uD2aY2be7S9Vv5vKRrUvJaWNg7oPLIemMuSZg3iH1EXw/x+Q5d4HvWXy70ICmsU+DFCLoVt9yOgbA6mHwQTa2+GiHLxoorEdp5h2knwjkg6PLsUVmBrE7dWa1TT1re605otvJ1Xxbk3okijCOoJrzGY096Cgyf0Q6iYVSxVDWwahgez5CNKCoHD00Ca/ehpow2ZBUVSOgmNUoCoHd7rt/T1pXiuzIOpE7g8G1JSdeVed3QUXuRYnFnXvrg5qvXa3GOYxZTramwm5VdlnqyWqLc4Gtpotx8LyaQi2xcAparTpaWdsdjcIjD28QPY5GD+WiHsRV3971qG8F8Lx14VPYDTCWgkfDccJ8PcOLl/MnEtItV39llTshDyuyGbmDM9USWS8xuCfuyWqOpaW61ZpAbhTBC061k2D2AkbIrhgHbSJzGMdaOEVZHUAJWw6BjVhYk0pFlJsdoa4VtzElkuuW0q0y97ibgSNu3L4Iooht8CjOrq9dW6cLXTbvfnqdrdcBXLrzbu06KhGLMRnp4SFIlUY/93l/ZAWLoocHJ6mZfZUeQUCu8dG5lZFSxiKFI7xFXfcDcyKYjSQm3ztDu2VvOqwHQ7kBuu5PTbuubXIorfKJz1UTBwMUWiHfOq6i1MSIURUl2jUioHXmdLTcF0cnynSxbaJiOZED35KoQ1hSF3LeC52XcLTfhsqOngi7SwLZKMiycVqx1F6MtY0pAMXWHozWtOi4zUZO77kH3sZmEVsJPfZV2WdvKpH2s0qZS6iWvSmwusaiFH6ih4Ab34l1N+QLt2cOSjQgPhytP1GFqYu4Sqrv49UiW4qbTpSHWb7WdgnqTGrGGDkbjROHIcY1/3PN4a+CWvw3sq69k9F2Kbmhzr13jcKXPWQyhpwhPWdba9v5+z1xMnaOiy/kmpCco26DtVV73ZHBf7WQCqomJYnLFEI0W2jglZga5fMG0usemwPSqFBNYU+LvFjq158rJQ81FHDJ3QEHrtM6cTq2wbCjofki0eA01V8jZOJfmLpnLRpncqkNa4Z41gQwQ5CZCG4xl2du2ixwbi3dI3lZLo9HbQYhvRnvidI9jzTWcEncwplTVlORJF0dV4OQDkURrRT1kiZpoRkIoRI8VGL6ytSurZc3SMQI1iqBzsN3oDl3eK/tAQcciiUk8rzGG8834zjJHEz9f2qhYr9YMWDiWgksHXJAqq/3xnvbI+UrH1F2Gx6UYrzpochuJ4qvGOgxRc1vqWVEJlBAN8bGjCnJ5CMiWcAurpsFIR2daJDNCztJS7t1C6u51zm4poYjFOVY5gKROJ7LIqeVRui+PFUURBppcIaRVNVihYkGu7xIXno30dthHpI5pTSlcamdEkcqWUsc8mctTlR6cjdH5/XRgqZMxZNUllZIhO0PTldvkAaEdmoG4GfCdUaazTS/R84gtDZ3a4xVzZzitCxjsZmJOvw0cGivJwTgcghVOC1m00vrqJPSJf3D07n7xd5hks2lk7Cx4e+Jtb0Co9njeWzmBtp4NDe3ZQzTrQhbYoCs8tuQ6omr4IGhjLazhXSdU3FCQCmfx3pVG4taip1VoSQwubMM1fDcnlix3xR7qlCvcOMk+rXMAJftzvUptzycqskFrQoQBMGgiHrB6g5JY0+ae6E4BSh8NqJAD5XJRvAt5nRyp74+ZLHlahlSxE59XFdXu81IxBugqiq5HwGljUfh5N/XGStxt7vamzzROabyVcD7QGdROBzLW4TBGbryycarEuV2ifopxRWIghRxcei8WqO+sxCZLMAu63q2VNq7kVYDvNZyr10cLXWJzUEIIGBLXukypN0i0b/7yxAV3Iu4O5ArR2mJ/Mk19afach2zgSnG3ITatJviaylcTimUOMwcMcaob5sR4cpUqtliuGhaFWX0z6JrRDBmhwqPNkGe4VZi269bicYlmqVGjzo0ylNxsYdfRR2dDbNdNoq2HSa1FhZjk04R1FLS5BjZz9CkqRZqu48h1pZIwbVd96KQn/NyxyQ1MAByZImQoHTcXObT9O7PnY7+OZZXL9lFVZh3XbeSbfcJRkrcmqeBW9LI4xTf8kq62eFhbree7XdMjMkHBtVWf1gDhHJBQZikTWwJqDTBfKA6GNGOgn4iwEQOOmDARF4kLZNG8REKmnJq7Znu6CVefW1NLYpXtVxS1js83jN9rkYiQsBk6ZJEw1fIs1Agc+4cC63wOn7xjsrn4ZN9XceHDG4oQKiiNkR1N03/5y9uHt9+P3t7+xde45vOY/2dHP88TnK8vZjxOFH3b+/Tg9elfFeivH94qNwLiPI+26rS9vY6J/uZg6+M/Pyac947Pt6K+ng8/j5sb+za/JfwW5V5bN9X4pS7SxysZYIfT1vO7hfX8+qkLvv90HPpSYCb8VfTiy+uVyLf53b/5XQvfi+zGf13eXgd9H96818nvF4xYffGrclbzda4PtMPekXfs7bf/C1Y/OaDkLQAA -->
