---
name: "rar-cowork-cookbook-ppt-exec-perform-service-tasks"
description: "Builds a read-only executive PowerPoint deck on perform service tasks status from Dynamics 365 F&SCM data, with KPI, trend, issues, actions and appendix slides plus speaker notes. Call for a monthly review deck."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_service_tasks", "rar_sha256": "efcb197c028b832b895ac107b8c4edff168470647e7f34973ee89848db92796d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObSLbmX9G8N2Kq6mK/gNiEb3TEICQQQkJiESDKHS5WsYPYoW7990kk2VXV7e7bHTGfRg5bAjJPnvV5Tjr59c1um7Co3j69qb6dL3g7TaPQrxZ27i3Yoi+qBHwViQP+Ltwib6rIaZuiqt8+vHl+7VZR2URFDqav2yj16oW9qHzb+1jk6bjwB99tm6jzF+ei96tzEeXNwvPdZFHki9KvgqLKFrVfdZHrLxq7TupF3dhNWy+CqsgWmzG3s8itFxhJLLj/rbLHhWc39odFHzXhQjwLHxZN5efeh0VU161ff1jY7qxM/VDeLkvwLBoWdRoBTRdlCuTWpW8nwLq8aPz6fcECaxdAC6B1BmwLgc6V30V+/9DyHdjoD3ZWpn799unnv354i8Dvt0+/vrmpXYNbb+ey2QIbz09T1Kcl2mwImJra+Q2MKUfg3xxcvwwGtzw/+Gr+j7WfBh8W//mfSW9Xt/qnT5/zxevz+W3+o7T5ogmBewq7bnxv4dql7URp1IzvCybt7bEGKjdtNVsNvFdF+e39OfN3SUW5+Mv87MfnIu83v/nx81sBVLBnf31++2kBfPD5rWrn3++zlPLHn97TOWg//vS7nLp1Yt9tZmFA6/cvr+uXWDDw96FRsPiinrfsa63Kd6PSB8L/YN/8ear+EvdyyZfn4B+L8sPi+5Jne/4C9H0moAPkfl8s8AGY+fYeg8T78bVGVXR+bueu/+NP/0isG4Lgp1Hd/Etyf34KDkHWA2+9XPLTh0f4/rqAXrZ9k/mPly1Bwvw7loDhX5f75qh/JPsR2b8RnUY5KIuvsfyuuO9NgP6y+Pkf2vbPJnxYBJ/fNn4K8KCyndT/tPj1kSI//+D9fvOHv/4GRP+PYtSirdyHhC+ZnUeBXzdfvvz8Q/24/cNff/6hLUEW+3b2pa3S78n8nl8f6/zJg69RP/55Llj/kid50eeLbzW0+LUo/1f12/tCtwHc/H6//rT4YyXOH2gxG/F10acL/lCNNdD1D3786e03gDs5sKZ9ghvAj//4j8UxcquiLoJmobpF2yxAgJso82fltTCqASI+UAOgmV/VEXDsaxzI/znCs8ZFsPjl/7gPiP/oviAeLsvmywzb34rxBc9fHvD8y/tCA1KLKrpFuZ0uFOZ8/pzbNx/gOlixrPx5OEApZ2z8j2D+x/nHIsoXv/xzwV8eMt7L8ZcHdkdPzFNYYca7uk3999kyI/Tzlx0u4KonvfiLtHCBLkGUzhQAVChSwDjN7IU6iQDAexFAFMBZ40M28NSnWdgvv/zi2HX4OX8CNLZ4klkNgwHf1Fl8/AiMCtLoFjafc98Ni8UPv/72w+K/F/9s1kP4vMYZ0MQrDkDDvXqSFqCu2gwMAyECQQWg8YjDr7+9XAvE5ICfQNSiIPKfk0FeJr731c/qjvm4JMiF4wM3At9mZVE1APUXUfO+EILFN33BovOjmRfCop6JdyZEP3dHINUG5nzzJGDDRQ2Srw7GD4u29h+r/uJU9kPFDBS43fyyOLJnwEJFCv6Z1XwMApOLPALu/5YFz/tASPVDvVh/FfG+kOZMXJR2ZZdhZb/WCOxnXGYGfk0Hwu1F7vef85ls/dlVj7J4ugcMAp5xXyH9OMccdCUZwACv/rr2Y4w9c6X24Mzqc16/Ut6u5lC4gALAorc28mYi+K9XStVh0abew39A01nSKwreKyqPHDx/t23Zfq/T2cydzud2iaD44v/D7mj2BsPzypZntO1msZU05fqM0twnztF8tpagVXlIeVTk7+3LV4j6itSf8zQCKVeN//Uc+Yjta8wT/doKhEJhlId8kFhA01nuI+/nPK6quWLsz/lXSgAmLx74BxwKQAIU0Zy7Xxecn37VNARIMF//3h488qTyZmeB3F6UrZOCvAt833NsEKImnAP5NbqgCPy5jvswcsM/WbUA0kGuAflzVCNQjYA23r/B9PPpV9X/NPHZBc1THh1iC0q3eggAevizgnMY51gD9ZpnWw7s/PQQAszIyma23QHFAyx93vQr/95GddTM2fD0q18CiP44fz8tne/6QwnqBTgLVEXZAu8+6miGmAz0OEAHEH9QVlmUA84HTnk54SHQzmZQAHnzakqfEh+3Xwb5j+KbyerrxNmQec7M/8/ctvPxj9ihfS9NgLxsHvFY928z7dtqs+wZP2uAgWDFr0+fjcL7k+ufzcTiq9xPf7fv+fHf2xo92Pvy5wT4tAibpqw/wfCTcb8S7jtAL/ipaz2T78cZFT6+qv/jq/o/Pqr/T1KfBn9a/Hua/UnEqzI+LdB35B2ZHx1emfX6AEewH9fXj/j89HOu+L8jK1i+yEBqzWEbAdt/o8GvQwAX3ir/Ng9+0mI9s2kPCPzBAyAGn/M/pvpcaoBm8tucmnXxBwh49AMg7Z8h+0ZX4FHegLW9uXO8+fNe7VEYtf/2KW/T9MMbgEf/f9qjzXyUzclcz9s6UDbA803kP64e2DA0888/73RPjx92+g4QHuBQWv8x4V4sMrPoH+riaSGwzAUrfJiBGpQ7yEVg4bz4XFMPgAcqzpY0Yzmr/tzOzQ1gClyZfgEWgxT/e4X+RAWPoYvn0AdVP7oAgD4fFv777X1xUY/cd9f41oH+/QIGaABmWV7xaebCDy+AAd9g1/Bh8W0DACx7bckee+e8Bbvdn+fNx+zqx5T5B5gDvr5N+vY/CY7/9tfv6fVAoS9zMjxD+rfaSTO6APSdHf0Oamh4Jg7QF6zpta7/svyfl9fHJbIkPyLExyX+EPJdHz35b+5ho8L7e00U/2sz9hzxhDZgt11FNcB/0HBG9TcQetDznPUgPD+6bVXNTPSa2M3ddAQGPq9/+o42D3UAngNWnL38e/h+d2Lx2M7NigOnN8//ffj1DSS8PbcKr5R/7QfAcAB/H+u5F4IBJIAFwfWzeMGzf3On8JpdhzboVcF0P3AdlKZcZLlyVtjSWdGE7aII5axc3PeCACVXOIWQOOVTAYbTFOb7K3qFrzyHXlI06QF5TwD4Mrd70awRQVMBQtPLAEeXiOf5wRL3vBW5Il2CWiI27diEQ9C28/vUJMq9l5lPs2Yfftu0zO54Wfvrm0PiYOQOrwXm+WFhGnXgJeWMBxMykdVgXTnRji7kqFoUPRbYoNrLug/bZDJrR2g5cWIuJ2ufaRbnbrJ0d2QmRAju28A6ULl23uSkUO+X2LJJm/pq1ZMLOUcoyLzjcN65spUf0zpbXqwi05eVLFQuioJudUdeZIuv7DE/JWFr5erlPtXGfiNS2zNMLT2Yv184vgjV1UheA20vkEu5uzYsn663RYt4PeRBWBYO2v4gtfuEh2uHM+IB9YLzcOoCUxlhzuYDaJCGAhZRSIImaTgp1iSc9si+NC83emuS8n2U+S22LeCNxmXnovBEhb1fLvbNJk6luUqPwzZvPbU9ne1YFZiDe0D3eN5LeSwRlS9LLpSc1hEEQxC1og+tSSE0WD+jaMiF2/ZAG0XBuKNxwsOAONXppcsuNqSX5TaIyg5llMCVgpN6Ne+ybcLZVb5fzMyiu9xq96riiO7tlnLJ2rc2R5MYsWNGkfXVWe+t1OkiTaZYw7b6zQ7qV8YJTTfVznUNdNoop4MoJO3xcD+L2bKgeXWijA6FFSyLTPPYWbG6aTXZErm9eFt3oX9QGT0SDQNfibwXbBHSEjFeVQeuDmXMHozagFyl2A9NpFnlBTJxV5E21gkuPd6uiUOGbjZtpUsCy6tIXhThJgu4sWbZvaQLvm3GNwLLMu5mlN7xivTnVTb5ucxOtHkSD4S4ORMuySNjnWzjzZCeUrQuYVWLkVtAuN5lHWfbdK0QRsIW1CAFBICE6IoE2xiWfZWc4muhn2/eyo+czCHXw7FUjnLiD7tUCSh9m/BSIR5ZhdgG3HkFI5x0HHnq6Dkr9b5R6508lKGMjiVjI0fNP7atqV+orZ8KQ8Bq3vXgjSnvcVxyE8w6PHShedFFL/LPyb7O2hV7Iox2A19zOYT1cLWGqQtfCHnUIKW1udYQq2lXerMqbGzI9Dj37TJXEHd96Kf6FHuClPj8xVxeSpAY2I6+Y+YA/k6i0+CJfcOpLQHzOnFivato+aceckM6JLawkbQTLAhaTNp1UIIaPm0iU+xzc1UnwCRjvKmG0lRWVCugrjnVJklpjFq/08vURQxtFbVSJdEYy03sUbvkyxtpeQnicvZE+4m6u5enXeGtx9G1j2W29Y8sKyNhK7gG7guJl4h8LssB4/s6dccJPDHx3GJCbI3Ugr0/bc4huGouSydnWW+5z65ure8j7wy84t4RnWnLPpJ0n7vqeWpwA1lcl61uRFstFPF4uMN76r6TQZ203f4M7e/2NhJwtKYUG+4zRckb7XocsBEZR9Lcw5SIY3qKHPWw12sb6sr9Sbid9qOA2wd5ZAbbxyOOMSlVGo4GpAFu6e40kh+iUBMihjx1W7aMcqbXnUO18ntdayBlIyKX86VTkvRG5em9Zlaot2/u+iR51sU80y6015COG/bnuIl62xZWtuH2my2Z0HdtpV08B8WtdZL4VFFuZQ8CyZat4gGYVOyGk+udYBvB77BoihN1JU42x7akEeBs0PvQKDES1g7JLu8yF1Ys3xbSRha6SVGPloXpfc9Qmqj3bcsAHEMMnigOdXrrx0mSR49E8zo9bXz/VA63+70Xdh1FSazWFsORprVC4S4j2u5aWBInqL5qK/goFE2Bx1jYOlmRClBeLPccCZHnpYMeNhAMmEOTVapXkjgapdEdDGnNHzK9p4Yk57N7CVUq42zp+965SCOdJ+RF2i53J81JutX6WOPn0O6CULsqwoQsa/qonL3NDmO3DNJv7ngvMUnISvcMc2iSWje6BWqVZtgkTm1+mfCOqmj81twOCVmzBttNtcPX0yYTYlypRKeVV0JU13dhLQhU17l0OOy2jkoJG+aw25GetZ8UCTXi9khGTJTa4qa8Xs6aCA3+gYs3fMa1ln12EXN3YArcuDgCLmTriRZdbCCD7pDg5cjLo2auT8r+fC6QAnE7Ot5GvrOTC5pLwhIXI5eCyWQL2kQ+d+Q4kpLLFoZJOoUD6tzvJtoLurO0avP4GJq2csH1FMvTgegBn22PdaTD68nv4Et4iO7WvdWV9VbdilNubZxeRvXAKW92a/mMj8QWJ91clb9sM1da3ULRRi6a3bH0Wgn9pAyXmbxWb6GfJqwiI8UtvbopMgmbaV1rorerM9NLAsI6sV3Q0F5B2ARAw6jWhgOjqIKDugdC2su03trluKK1Mzppl35lhwWzvfP5QdXHu0iyI9b37F3VrI0WryOW29aQcENLcc2Vw2rDK6mVsiLdrRH7fNxEodfTxP4oj2qVV1vHxUho3eIZHuJydMih06bhr7dVJWdbjYG8y7QVvNyC8fEwYliDDltmH6f7tePpRJyeQyZlxAavgDVaf7pm8A7L+/YioqqrMbFl7MQDU2/3/MbIIlFLp5PCwTt/ovOjMjr9UYgarrnRLB8K+ua22kxFgQmdeDhxoeOXa+SWqvr9dsPpUejk0hCK4QDvhOzAnLZH3DUuqXM9dmmSb123bNnbst7LeLze1VXdRWGgTEyxOrC1Wge7JpMzdw1JgXaJle0hjR2Fw/YRvNMNRNeSpXlKDrsEddZCe/La4xpAkTCZWVydUoaRHPZw2SfL0TyMkTbC5Yhs2HbP6FhkhVs3xdQAJ2W7pyftcDltp70o7v2j2LAXNTL7TpKD/oDFyIBqhxQWYkvQDUXGsaKFr1DWbuSNIh/oJYBrbrlnIbU+Wdcx19YSOiyFiGwEYfBYTEcyPPdwt74y9HFCpgFzOHW51eQ+HC0FXdWnqEsar5CW2Z3fq6uIOms40u20XZBNfVoZK6tJvY3NYCk67pBdVuknOa2VflSVkjvub41K3jaEl+591fDuvZmo1zUPoCCn7Ut+xZYnzWNMaZ16gTz1zHqkwzSZLDfd8SFrEXnsyjRJNiwssFF1yU1TGvPVZsPoQmhZmzVeNG52rbAk5CM3L1f77cT13u5gJycLdiiGsVOvL7JAx41xU56KA7MpZXG9XebNgUwUYuPD7NVo/G0Qm660dGAYY9X10eA3wGBMBSwn4BByirFam/YyyIoVk5kmW7DUKAfXjSb6gW7IJLkO8vwkntm8jgZZ3SaMbKEsq8mVcrkKtj6tXGFJJux1gvYZXGs5R+wScuo8tw/uSgQJy4osWJteMhfGuDOkmtzzNFFvNFP3jKvZt2gwkxsz9MfprpbkStUPJ40Ntn7Bq6LjGRGcxthQbNgNeirinWBeZXp9bqPGhHebga4uxPnacQKUKia7BrqHx36dCaLilbR9Kv0Lw8m37CBzBVAhcElL2mkU6Z8BSwSBeImcW9ajR0WTEC5VNiRv4ZMJKQ5Rdlw/tILOcUUJR6WInm/3crL3cSyKbDTGR/FumqHEcGlYdClFgS3IIVjKOn8SHfuc6FUune6jSBg1LKa349Bf1PXk6ozkqQh1jhGG0mUFkQfE4dZqWtqm05Da/bpC99meSaJ1eHUV6Fa7DmfVXBlfISMD5djaTU9IA0MX61Cso07pDO9Cd3BxNPQWYEw7XadawdEoNEA7bu46WVQddCIPRdvvzOudaPQmzh042mWdc3Fv1b6y+hDnVkrZ7eld75+J2l5CIRKgw10lmN1Ovd/aFT5ZUn4cTvHAC/ZVoS1/nx0Qi50M5LaKeZZGq5Q5xxVuN8OY4kN0Xa1lLWnkZYOzPbnZh7y8i67QZGXMWbGSk5dW6zrgdzcS23mQVY7daliKDKpK2wSNrIOOhnqHR8xdTtPlYDsup55C97I7VFyTQvRWP4Fs47p42rO8q15T8+AELkv6UnuIk2PpSuSuAR6/QtuRlA2b3UO0ItUbzqrUw36n5CoSOkcZy+zlzapRw90aadUqRwrqgyl0auG8vsekUF6xikd9z6Bsv1JrOhqcgGhJePQvvGoXAkbE9VVxtUt1vF94vRhGcp3cUmsojWRPOiM/hoTpsdNA3cwy6ndLLj7TClXtWVSmOue2RRjo1JUS6owb42yEbiVh8tlyQKNZuTtbEKr7et03p+OKSbcihoxyQ581q17fM2SzRQgD07sQg4ymxTgBozWl3Me46FgsQgTcPqSKFSRiaxkSs26NpbksXcmMi7yTNB7CK1de8GG5PhPESVwf4Qi99Ff9HsK9qTBuukHRIwIilPbyaaM79u1knLq1s1YvNh0na+kK3UOGNhWIoe0sJkdtunVXOjA7LwtJzN45gkEXwtA3PpIrSkKqKqHTvBygWcEdwLb4UJwiQ0aH6ipNl3OhD2nqHXY4652FKFhuUQtdk8SquijNissG/86w1V2TdShtLcReml09kscjqJhDYqGgqa+c2htqKb7AxOnuVhbWkoeWNj3yyBIBARtAGVTt0pzfwN4kKVMtQmhn4DrsK9w1sZZIONWmX2OHoe6W+GGk6tzYoWh+5U9ti6OiSDUWSuJkwt8DMgN3trRdHOnMk91QsaqMELLCsDY12NvUps1fun4jn5dMTUleC4s7BzCPrDfmkoIFg9xFzHUfn+/QBb5n/eXCDJLCOQVejKBbccvNGIjE3hSCaGp1YoQsGyuuZGjnHaadSGePoMuzR2cFQpy6s1qnnrS8153YbOTrriyonRNFGE/STXiNx57yFBg+ox3EwKhiqWpg1TA8niEbUVQeHpoE1u5DTRttyCkq0NBNapQCQO/2fL9jrCstdGUcSJ3I45uSlq6EeV0zUXuR4sPWvPTBzVev1+IcxxymWlNhN4RdlnpCLFF+8LU0UW6+F5PIRTYuAcdXJ0tLu+Mx2MfhbRKGscjB/miLcRV/971qE8FCL+0FVPYDTCWhkfTccJcPcOLlwsnEtItV37llTspDym6HbmDN1USVS8xuSftCrNDUNDdaM8iNQhqh6VYy7O7BlrIrhgFbS7zGs9aWFYkjoABiGHTMyoJEOnLs5BhtrXCNOR3YbjltK1OvuwkE0vbti3g4oGt8CjOrq1dW6cLXdbvbnKdrtccJF97uXCdFwkPMRXq4T1IlUY/9zifsADH00OBldb2rsiMoKAIvnVsZGVV8wFCk98irPmBuZDORpIQbZ2h33C0X1ABYt6c23clpN/VNLg8EPjG5aqJgw8UViHfOq6i1MTI8HCTZNSKxduRVtlwXZCfLd6psoWE6UgHTU0QhrmgauW9Ez8v4W27CZcdMBVOkgW2VVFg47aHWXYyxjCkBZOoOR2siOj4zUZO/7kD3sZ7EVsJPfZV2WdvKlH2s0qZS6qWgSlwucaiF7+mh4Af34l1N+QLtuP2Si0gPhyvvoMP0xN4lVHfx65EqD+tOl4ZYv9V2CvgmNWINHYzGicKR5xv/uBPw1sAtfxPYV1/JmLsU3dDmXrvG/sqcsxhCTxGecpy16f3djr2YOk9Hl/NNTE9Qtkbbq7zqqeBObGUSqsmJZnPFOBgttHZKzAxy+YJpdY9NgelVKSZypiTcLXRqz5WTh5qLOFTuAELrtM6cTq24bGjovk+0eAU1V8hZO5fmLpnLRpncqkNa8Z41gQwQ5HaA1hjHcbdNFzk2Fm+RvK2WRqO3gxjfjPbE6x7PmSs4Je9gm1JVU5InXRxVgZMPZBKtFHWfJWqiGQmpkD1WYDhha1dOy5qlYwRqFEHnYLPWHaa8V/aeho5FElN4XmMs75vxnWOPJn6+tFGxIlYsGDiWossEfJAqxO54T3vkfGVi+i7D4/IQEx00uY1EC1Vj7YeouS31rKhEWoyG+NjRBbXcB1RLuoVVM2BLx2RaJLNizjFS7t1C+u51znYpoYjFO1Y5gKJOJ6rI6eVRui+PFU2TBppcIaRVNVihY1Gu7xIfno30tt9FlI5pTSleamdEkcqWUsc8mctTle6dtdH5/bTn6JMxZNUllZIhO0PTlV/nAantm4G8GfCdVaazzSzR84gtDZ3e4RV7Z3mtC1jsZmJOvwkcBiupwdjvAwJnxCwitL46iX3i7x29u1/8LSbZXBoZWwvenATbGxC6PZ53Vk6irWdDQ3v2EM26UAU26IqALfmOrBohCNpYC2t424kVPxSUwluCd2WQuLWYiQgticXFTbiC7+bEUeW22EGdcoUbJ9mldQ6gZHeuidT2fLKiGrQmDzAABu2AB5zeoBTWtLl3cKcAZY4GVMiBcrko3oW6To7U98dMljwtQ6rYic9ERbe7vFSMAboeDq5Hwmlj0fh5O/UGcdiu7/a6zzReaTxCPO+ZDGqnPRXrcBgjN0FZO1Xi3C5RP8W4IrGQQg0uszsUqO8QhyZLMAu63i1CGwmZCPCdhvP16mihS2xOSggBm8SVLtPqDTrYN3954oM7GXd7ikC0ttidTFNfmj3vIWu4UtxNiE3EBF9T+WpCscxj5oAhTnXDnBhPrlLFFUui4VCY09eDrhnNkJEqPNosdYZbhW27bnU4LtEsNWrUudGGkpst7Dr66KzJzapJtNUwqfVBISf5NGEdDa2vgc0efZpOkabreGpVqRTM2FUfOukJP3dccgM7AJ5KESqUjuuLHNr+nd0JsV/Hsspnu6gqs47v1vLNPuEoJViTVPAEsyxO8Q2/pMQGD2ur9Xy3a3pEJmm4turTCiCcAwrKLGVyQ0KtAfYXioMhzRjoJzJsDgFPTtgBP5AXyGIEiYJMOTW3zeZ0E68+v6KXJJHtCJpexecbJuy06IBQsBk6VJGw1fIs1ggc+/sC63wen7xjsr74VN9XceHDa5oUKyiNkS3DMH/5y9uHt9+P5d7+xVe85vOY/2fHQs8TnK8vbTxOG33b+/RY69O/qtBfP7xVbgTUeR571Wl7ex0T/c2h18d/foQ4zx2fb0x9PTt+HkU39m1+g/gtyr22bqrxS12kj9c1wAynref3Duv51VQXfP/pqPRlwCz4q+rFl9frkm/ze4Hzexi+F9mN/7q8vQ4BP7x5r1PhLxhJfPGrcjbzdeYPrMPekXfs7bf/C/A0+TMALgAA -->
