---
name: "rar-cowork-cookbook-bulk-update-implement-a-business-continuity-plan"
description: "Runs a bulk field update on business continuity plan records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies and confirms."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_implement_a_business_continuity_plan", "rar_sha256": "e2e826a5b60b45e682fe2e81a541f6c34a5b425ce7aa97ddb1eaf9f2894643b0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_implement_a_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_implement_a_business_continuity_plan_agent.py` and in the RCI capsule.

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

Implement a business continuity plan Bulk Field Update — Runs a bulk field update on business continuity plan records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies and confirms.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-implement-a-business-continuity-plan
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
    "approval": {
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF (sandbox first).",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
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
    "record_ids": {
      "description": "List of record IDs for the business continuity plan records to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_implement_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 e2e826a5b60b45e6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_implement_a_business_continuity_plan_agent.py` first:

```bash
python3 bulk_update_implement_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_implement_a_business_continuity_plan_agent.py   # or on stdin
python3 bulk_update_implement_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement a business continuity plan Bulk Field Update — Runs a bulk field update on business continuity plan records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies and confirms.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-implement-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_implement_a_business_continuity_plan',
    "version": '3.0.3',
    "display_name": 'Implement a business continuity plan Bulk Field Update',
    "description": 'Runs a bulk field update on business continuity plan records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies and confirms.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-implement-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-implement-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c04668f4a4f2700',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-a-business-continuity-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-implement-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of record IDs for the business continuity plan records to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when implement a business continuity plan records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to implement a business continuity plan records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on business continuity plan records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies and confirms.', 'example_request': 'Bulk update these business continuity plan records in USMF sandbox to the new owner — show me a dry run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'List of record IDs for the business continuity plan records to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of D365 record IDs in a sandbox legal entity, with a preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateImplementABusinessContinuityPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateImplementABusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs for the business continuity plan records to update.', 'type': 'string'}},
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
    print(BulkUpdateImplementABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916aZObWJfmX9FkR0y5WrYRO7jjjRgEAgkhQGIRolzhYgexbwJUXf99LlKm7erX1T3VM59GDmeKy71nP885J+H3F6fv4rJ5+fSiBU6xEJwsS+KgWTiFv2DLoWxS8KtMXfB/4ZVF1yRu35VN+/L+xQ9ar0mqLikLcPzUF+3CWbh9li7CJMj8RV/5ThcsygIstkkRtO2DQlL0STctqgywawKvbPx2kRQLbiqcPPHaBUrgC/5/auxhcUucRRcHb3Jw853NSQVH+ygpPoHTXd88uPrN9KHpi0XVBLckGBbz/lnk94vBSbp2EZZAo6pqypuTvZ9pFvNllgTtQ1EgVpg0efsRaBWMTl5lQfvy6Zdf378k4PvLp99fvMxpwdLLGqhnPPTazbvyoOiY9at27FflVKAbIAV+RuBMNQELz9dV0ABBcrDkB+Hi9epdG2Th+8W//ms6OE3U/vzpc7F4/Xx+mf8Bwz6s0JVO2wVAWKdy3CQDbD4umGxwpvY7Q7TAQUX08XnyG6WyWvxjvvfuyeRjFHTvPr+UQARndt/nl58XwEKfX4ANwfePM5Xq3c8fs3IImnc/f6PT9u418LqZGJD645fX61eyYOO3rUm4+KKpG/aVF/B0UgWA+Hf6zZ+n6K/kXk3y5bn5XVm9X/yY8qzPP4C8zxB0Ad0fkwU2ACdfPl7LpHj3ygMEQVA4hRe8+/mvyHpx4KVZ0nb/R3R/eRKOA8cH1no1yc/vH+77dbF81e0rzb9mO6fE39EEbH9j99VQf0X74dn/QDqbw/arL39I7kcHlv9Y/PKXuv1nB94vws8vXJAlNxB3bhZ8Wvz+CJFffvK/Lf706x+A9H9JRiv7xntQ+JI7RRIGbfflyy8/tY/ln3795ae+AlEcOPmXvsl+RPNHdn3w+ZMFX3e9+/NZwN8o0qIcisXXHFr8Xlb/o/nj48J0ssT/tt5+WnyfifNnuZiVeGP6NMF32dgCWb+z488vfwAcKoA2vfe4DfDjX/5lcUi8pmzLsFtoXtl3C+DgLsmDWXg9TgCktg/UAIAYNG0CDPu6D8T/7OFZ4jJc/Pa/vAe4fvBeQR6aAfzLE7q/JG8Y98X58obhX75h+CNkfvu40AGfskkAJjvZ4sSo6ufCicCpWQaAyG3Q3ABuuVMXfADp/WH+MiP+b3+X1ZcH1Y/V9NsDtZMnLp7Y3YyJbZ8FH2ftzzO6P3X1QIkJxsDrAcOs9IB0YQKg/T2wSltmN4Cps6XaNMmyhZ8A1AGVbXrQBtb8NBP77bffXKeNPxdPEEcXz5LXQmDDV3EWHz4ANcMsieLucxF4cbn46fc/flr8++I/O/UgPvNQQWl59RWQUNQUeQFyr5+NMVdGAPqO//DV73+8GhuQKUCNBp5NwrmGzYdB7KaB/2Z5bct8QHBi4QbA4sDaeVU2wJTRIuk+Lnbh4qu8gOl8a64dcdl2Cz+ogsIPCm8CVB2gzldLFmW3aEGAtuH0ftG3wYPrb27jPETMAQg43W+LA6uCSlVm4Mcs5mMTOFwWCTD/17h4rgMizU/tYv1G4uNCnqN1UTmNU8WN88ojdJ5+mWv463FA3FkUwfC5+Bo3j9R5mgdsApbxXl36YfY5KPE5wIlnq9G97XHmeqo/6mrzuWhf08JpgkdjAkSZFlGf+HOx+LfXkGrjsge9zWw/IOlM6dUL/qtXHjH4tTl4dER/0fzMvcSCf7RKz5Zi8blHVjC2+P+ilZrNwAjCaSMw+oZbbGT9dHm6Z5b8YZpH5zkrMNN8pOK33uYNv95g/HORJSDWmunfnjsfTn3d84TGvgE+ODGnB30QUcA9M91HwM8B3DQPGT8Xb/XiPdD2AY7ArAAdQPbMQfvGcL77JmkMIGC+/tY7vJp7VhkE9aLq3QwEXBgEvut4KZCqmZP21Z8g+oM5gYc48eI/abUA1EGQAfqzb2fzgpry8SuGP+++if6ng88WaT7yaB97kLPNgwCQI5gFnJ0xJB2ALqd7du1Az08PIkCNvOpm3V2QNfn718WgCeo+aZNuRsinXYMKoPWH+fdT03k1GCuQKMBYIB2qHlj3kUAztuSgAQIyAAwB+ZQnBWgIgFFejfAg6OQzGgC0fY23J8XH8qtCwSPr5kr2dvARVeDM3BwsQiA6WJm+Bw39R2EC6OXzjgff/xhpX7nNtGfgbAH4AY5vd59dxMdnI/DsNBZvdD/901j07u9NTo/Sbvw5AD4t4q6r2k8Q9CzHb9X4I4At6Clr+6jMH55I8OEr7H1wPrxBwodvkPDh0Up+z+dpgk+Lvyfrn0i85sqnBfxx9XE135JeY+31A0zDflhfPmDz3c/FKfgGsoB9mYNgmx05gVbga0V82wLKYtQE0bz5WSHbubAOAF4eJQF45XPxffDPyQcqThHNwdqW34HCozUAifB04tfKBW4VHeDtz41mFMyj3iNV2uDlU9Fn2fsXAJrB3x3x5lKVz+HezlMiSCzQxHVJ8Lh6Q8n5+59n5c0IANMDmRKVH5x5blg4IaCxeELunEpzFP4VEs+id1M1y/oc9+YG8QFVY/fPvJTHFyf7uOACAItZ+338v1azuZp/l6ZP8wKzekCd94vZFO1cfYF5Z03nFHfa9FEKfihLBvyYfQF2A3b6Z4EeteexZfHc8tYqONEjpd8vgo/Rx4WhHfjFuxZ40y1HwLppu59/yA20AV+Alfun0f/Ma4aGRwV91/78CAywefHYPC/MXQQoXQ8BAgdA81PxH3L52p3/M5MzaHxmEn75adbj/Su+vn/U5feLr8MRsOTruPr4O0PR5y+ffpkHszmOHkfmL8+4+nro699Z3ODl1x/I9RT5S+L/QHsJnJ/rzmu67Lj2K8L9l23EoxLOnv+BNR5sQakABXfW4JtpvglYPsbIWUBAtXv+1eP3F5ApDqDpvObK6xwCtgNk/dDO/RUEsAUwBNdPFAD3/q8nlFd6beyAjhgQDJCAQggHd4mVi+EBQSHhvAQ7OAaHhIdi4BaG4F5AOg5N+r4LB05IhwhFYwSGurN8T2z5MjeVySwjTpPhiqaREIORle8HIYL5PkVQhIeTyMqhXUASpx3329E0KfxXxZ+Kzlb9Oiw94OOp/+8vLoGBnVus3THPDwstYRc6k+6pcSFrRY3TcO6r/bix/a4nMXPy4O3WO+44/VRixMnhTYQpveQk6/amVpe7XVzydLJF2dCW6EI/3HGRTVzW70ga9lF2zbgH8pDraoGh3tLuRRzt11S/uqVm7WTs4Tzts2OdrMTN2azrjpcyq5+0w9pS6/60v/HMlHgW2t+jtgqvpAVRuVTXK4w3LpbKR9UxuNNcUlkb297GPlsFEq5GCLpPmk0GQ5Dm3rErGRQNddzyl2raUWblV2hmLnf41R7922GrOTWqKaZjmR5BjrdsmWdBhSjWFOGSFfWXW7sc612Nc+bJBrBvJKiCTuRGuei7ONcaKtdycRRi2d3j5o1FqUHZFjjVSy3u5WS7DBNSPZPJSNPUEfM2MtVmTuPZXD7qoy5dvf1pyBDMZDJ6QKCN2xjNlE0CshKSrMgvJA6VidabGtfyG6Lc3Q/dxRJH76Cmx01b2w1b0Z5JsJ6I3SNM7vJ9bUqHUtRv1Rovz6wmHtq+lepD3aMlvJXw6dLKtyNZmEl+OVXiDikJMuLCGjknu0bQDhkhrE4mxpTnC23H+d7SkE3nufwZBPQoRIWyFOU+N0YRmHHkbOVe+9vmQHW4HdvkWe82TF5jebnKrvltPbSasJfNLdtN7SqSDp0nOa22xoc7F7IQapsrQjAvQLRNKGo4JGVarFXZQd9OmXSrvOsyC6F8R/P8Ej3kZSyyU92N5kapSYkdozDvR+6sJidKmzI1O1fHOtzdMXoz9Ohqm1xE2WXWN9PyxqMY3y4sJxS6PaostGVEzoGYQ0O2o3vw9pHJnRGYtZyWaTRYxliE9DPrdtof9czEzEslx/K9c2zeCDQApYkUUiW5NnDadvV8u8QZMaF5l13BBKuS5zW2yxJ/qG3u2C4nrB2dLRnCt9hzD9VkUmPRYpF1At3tFrHc/OyscnF71UlL0vEzn55TrHMxyLVGSGvIm1srqjoG4Vhn0uBeeUu9n8LlAI1tgo6Ne9hi18xXm3ZcZpawHr1JOm9azEwFOiIQao9oW5ps/UnatY3ZJGPup+Wx6QLckuUU2kV3PsR7bglswV0y9zh62uSFyd2O+8TVJU7a0kGK2arp+Hf2Ih/gvXFmSsnl4Waz7jkbJgaFX2/4pOAGaTTl4UCs18HmDEeyDBCPKyKHatr7dp24hLSNHEYrKfnWiURuZkJbbJhGJBJzg2lr0yCPe9aL8OMgHzX5XN7SbK32GXQiGqZTkchHB2opCroB16Xd+1CyShIdceV8RcC1Z3cwHMZ9y9bTcrsvV00up8u9tN9srB228WQnBJg1NNBKPyv5tkZgvVkK7eVC5Ec/4/MjKeeUY7DFutwBF0GtEyGOjhyieyQf2TxYCiwlu7FaNJIM6YQ9wHJAQea05UdnbaSJwfRyfN675IU93q+9NrC5RUTHCa8jOhZPu3QVZdeqhzwZCbtWOF3qVUqCDjaHeASqN0og0ZO7XLsCC+HW7aLjw7idrIi8cSVzIgNvr3CStxolJxq1LZ/4Ph6N7uWi1zy3sq3dGqlPsuyZUYmwvXLwSKMOA5AkihlZTQ96ZcPRQo62TFLUdCXHB6+GS7HuA2jwRBy+7TCR9qaWKo85Wm4jEiBBQbCMTbOEjlmwlUsoBbG44ZxQZQhgZT1h6f1a7CW9dTd6KWiew/acXk5pyjknwujR4z1ytGnio6Uhbl27FwarUnTqfN8OBrJx5GSzvBDc7jQm+0kwYjKuuPEaTcyY00hDocFSj3BZT0wOF2RHb1XW3ji6exU3rL0WypREjKV/XNO9c2DPJ23a0WW13nGJO039Md8IWUIXK/a8gq6jwPhH/pbQYn+IstIm81tBXZEojg3Z5+iVL0EC2Z01H0DeRvYEDgkKye4vki23iqNSjup2y6CwCdIv1hsNRwUDE0euoIhIu+oSBQDSpss1e12hLHtQ7CKAIJNhZHdckY5wkAX/aK0C5Xa7kcQNtsPYXHa321Udaae/s/vbqVgHS5dP2UEyjq6zYQMuP9mRkcZrqwHQWMe7CA+HYxErZe26KsPf5fHcpuTpapuJlfMMP6pXTUgwjjlesPKsaSHT5mD7kbB4LmXV3SGIR60SimSU9EN1tRVJnHBe1BQdR/lNEzVXqGnJjaDcziyf0gYvt9gBQaOVKzjGckTxYlRJ58pd4uAsxLfKhiyNYoKU3SVEb4r740YghI2rOe7F827U8XjJpsk9YMvTVTpdmsO+lwY7joWtae6EbH1iDE5ILCqL0wgfOxLvxeWeiTdFkzPxgF2xPUszF6fvRYUftpSMTPsiRrY1vneWGoSTOz6eiBOFTNIt2w+cKIy7hBfMyrNwXWPtc1UupYyNDD1bMTpcMUg/DSXGZ4qwvhqmV5OcpOKBS4maKO1XgSSfcfYSmfxwNSARE5R8Uta+eN5bp7FjOQvRdiHXm7sdvQQlcJxa/SBmxp3SLywVCaLP8g3bQ41uX4bqILjrkxeDfD9daYmo4nU4NVwqicchx83ung7ihdGXCZGanC1IMhiLYUhKKgUxy7qwQb/jweq+PjvHFVFcBmHHlYUc1lMmWMKGqHcIa51NYm9DehVL2EHcDBITnEw+C8RQREzpLjFUlgclZidaVp7uFxG/mtWgnzYbj9ENXpP9K3yoDyfePXHGVKGbewaRR16k85JJ4nDAtqQBGgYOSgy5wtzNqQqSo76yT8FecpY9GAag8ESM0U6h1ZO3pVtLpKRNur6mrmLSLt7H10K5DlBSGxmzRxsMV0h0RW9PICxO+64c1XbUzPO2VWOFif17VcKJI+nHlZKujhS6So+VcBFpJb+GonVYVS6863ctk98Ml2CyroJYsafUnOlrcmfH1/KuMVUikuj6pF8P8NTg4+U2UQ05iADSsq2f44XB8GwjBvuqmgTufnJGtZKw0+BvJSdXbKiiDwJ8cKNKvFoxaK5yt9QjbQK4q50zk+G1ZbcdT1cnorxVX9tpX3Jk1d8hEqcLwzB3Zzzaqb4sTv1AXy3CmnoPd9T0UGTjydBghko3xGkpjMi52cW+Bam5t6HXI9vLWCxqfOhkfihn07CLZUbofM1Syl7XI5lC2eaCRd0+SCl7pE/6yql5BdSOnCilwTfWiV4lld4mFxxt+HWGppNw9LUlRpaEvr2PFhv0btGKk9nxtGXExJKwpHI68psLhm1OR3e3xfHpWBx4/ohMQ9s00RGvV5rJaSJ7FlZbvDXCUSd2kFEmPj/cQ2RIbG6JxGF4Q1GYSdJxlMiDWu4wrA0uhGNNSslE+zY9JSa7CQbuuN14Z45pgypaRvrBQF1kq1/u3C2nBkYl9tHl2oTHG5nWe5vzIIKqFTRFqwtLw7HIXUneWoKhkDN6srGW56VB16TX36ssxHopPRJ20lyY3b4hkiyxIEaAz5RdO0lyIOw9sd8vxXMVsFW5P2bX0L4aRLusZDM5G1SGh4fLmFO1bd2su5aO9rlABHOfqibetmcai0/L86YWE57uJc7X1XtjFXfQTiLxxYlCx4BWitpJgnWWojvV7EOlMPQ9xNy90AhEfrXKdxxBqTe2z+lGRgKfsvfIGjKwaQkJG0QlQ3s15cpUILv0ds8ObDCKwflA8ssTs98ZDEsJIu71EQUXsedDWsWPsgXLDJSkxEZhxrgvTQVLj/WZv2WTfHXuGy7QlWuaCck25kVP9Q44yl08cucVBd7eVmktQMYdvRSmeGOtob2uiLHHBLk1VHEMbnd4CclCXjFGsvGS+s62m+qenS5bk00OgpDkEMNtT9c8Vdcm2+YmizD96OfTrbutwWjrKxuUVZYIQ3VmezOw1Mfdslf7dqr4ifd157KVoSOdaRNFlZE13UJIQCmr93eXoK3WoobBhnVOhFWz3eCrST3eLnloHOhyuQtKwdincXfaXnG8os8Rno5NVfYHIh4o0bLNgy7q9XF0oZUmIzEuOb52rvsI2rVeZsXojOow4kccWdgSxMhZXSg54+147Cxe2eFu7dRhbbCVcQ9F5kqsmam1Wks3FTARq7wEd1eH3guoX/ecPOqHU7vVMLyf9lNz3otUs2uqAnPhg1rYhhjefa0jlwqkT4lz5IZMZVrxULsWR1qTJA/RBWBBcUmSu5WdcvkSRcPlouyZNI43bN8cISY/HriipsjVndOPWahtzS2ENQMHH9GTExh3S6BR+VabRpQV2uSbhH8bKPQQAVfqBmR2FNumxdYplHJJiwa1Ddo6hZFVmTlgOBEY4mqDcVjrC3nF4IVrRQp7KWEpuF1PLMbsAt7am0YuF9jIulG9s1jnDDdNDsaxtbJSo5YDWeIHxBVAXrRmG1OA8mkKGUyiJhe0xRwzqC6UbKkNdenq5UmeRpYRM+oS+FtU64MV4p3XVbqVd+hpq08Rdya4G7es3REXs7HrVAemSQY2bBmmlNXheld7hLkMe19E7d0AQ1rS22olSz51K8OOtFNMPe1R9S5Sihhyg7sJphRpBkS8+UrXiT0a369IGyAdhZxwz+cDhMwGksWRkbzW/Rn0dCdZIBCi2dY2v+bpo+2AJnx7IKJiA+WVSzoOfF7eBmNAPGdPttqg3kOe8gThhp5H9CDLFUou4UB27rjTbW6dxXEefaZNOW0IP6yZXuivG8QeFVlI+y5gkg28QfXEZbsUXkmVeEYouutDbUCE0oB27unW3GD3Qt9y5jbm7JJ26Awu/LUd+C2jXayqJLfhMall4YwchSN9gKEbyKW2gcpa1rd2WkONFWI5xCWEuxJEAjFDa88M+zVOiybsTzpRMBMn3w17xIvNVePIWsPE5VRcakq/LV3yRAzc/izL2024WnmRol0gmpxGHWq8q+d09rnOTApTzf1d9+4rgtiO7fo0scoUGwXVDeSV25b28bKaDgelw6EKz7FViHZ6O/qouF8b210IYZCFWmGGGIYXngKUYuTAB1Bhg+Kc749jxsp4wJY9j6KaDMMoGkor/qb0vXB1VkSQwJ0Q47vJmnz6rELlRb2uleq22aXRpkojX71BlmD5RQXGiwvLbJ1z357MVGKOrpjciRF2XY1S1lpd5L55USK5UNQyD9A7waPLSFhRh9tav4GhSTKZziIwChT4YZc5mrg2q015W6eBeSPUHdoUO4AY8D0XCYL2QLcE4qLpdrdNFRGG2N3v+GZce8SZOaPJlSLW3klc8o6XecGAxRRnp0jS3rjAUOJK0yFaUy2SGk/Bkly2IStOVtJ0lySjdUKSx3AtBxwpEIFVHIZwUDis72udg5pUtfeyKe9blNKWVFoW7TJsiKbBDh5qIvvYTcSrOFxHylrpwnL0dsgUJic4PXD5xpuaIlza3aqXjujB7wRzWsEl6q9l5VjdTzGFbag7s70sFaWVyn24jVkkyzEqJdw1nVHHe3CTfdfrdhu8IeUW5ocVfOy9nvCQCYPL/HYbu/hox9Xdveyc64Q7MYwdaDvH1pNyUDZXuHUN7MBOa4jeQnuTq+vkct9GaOvh5trAkbRV8SrRFHpg0J5x9EC9b7khQqwOp7b3oCpItL8pfujQzfJ6iSF82Uu61BvhrYyPd2ucqKH3AaB0EB/eU7ODPLUX2sZB0WUnXHqVtruiGKXk2lR9SPqqVfjLbMQNGmTvGWFFYGhqZxCZw5r5Nojv3a3f9h0RMyNR6HJ/jC2fhVxv8JbeiTz4OIFtKQR0LYqrD9AkR8p49Krc5uB1HYfnftxaeimeCBvyavV2vCr7UAIiMp3LT1fQi5XHhAw9MZ5Yz0Jrh823VGpMcUnhYcZxRg4MgSgMmelr0ebJbdmndOBpJ0rwL/4aL0PebvsUIAveHsoBvuBxbd7dczee9WVFIlLgmrS3s3tG1m9qECZFut6RR2lHRi5lqEt4jRzUARcC2yQZQ72OdwuCc3kpdTW6k9DDnlu5ztgTE6qFjhXhmp1pUisVyIrfU71ldnu6G6V82XYCfO06F9eQ2lhdxQs2EoLi7m5XCmllL4XzUMBcRE0xngCElGBZueEk7nG0VhBpbaDLs3lvLnd2ErfiKtStyULd5EwvRaXo+EsbQ1bK1rwqXWBp0PmlhfSoofNiJpPn1V4fCnIY8Ht5xpP7mNtL2S18j0Gtmlgj52CFUlhJk9BWgkxkpfboxeNbdRsauYPo6Glji/UlXUXhiSFBc+6sPTIbISiz0IhekSuB3hWlHhwPdUagTXqRrz3cwWRv9WhOZgVoRz3YSij4TFuhj5AU1tEn1GPGE6mnkJdi+o2gCpBL/NXeRQ5RiKUloMqNTLoOs+Dd9QIdhAJVzxVOBh7CjSpVJNoYn/PoIOb3lWUEpH4/4remZc84vAVj/YbjdtKROiWM3mxPyjqAs2U3cNFqj4rJSpmaDqFWvi+XIxwe1U1mYMGNMsc7XJxJK2Ug0EVg0sUhThBfldtG5ZplWzaEuzxUJNqMjVNXCk1aiRpWze0yYXc8hFweP8ByDsk9hxBYE3AXKMHTA7OahsA/96QpQzycwo1nq11Y+ZyPUspmNEDS8QVp3rfN2ZEH8SaitWT3fo/BPb3y4dhKiqUdN5Y4roaE7q+n46nKm+QmoX2o07zeK91g3ZNWDW2U6fDzec3wxw4SRzeWV2tDH8y1vw4r0V8t0XWEtQQPyqejbYprrwbZgd6stjZL1FoSYd4W12SxWvd+QKX+hLUKoRqo3bU7GAJV8Bo2k7FXwbhHYysC7cUwp5z1tCbOV9kkb+ejjcbetN3J90SPKnjjK0oklZ6QYAqB19vRpyGuGJyU6wZ+H0JdBNMrjTeF6CQ44QAZRhBSYhWT/I2pVZ+qMxhV1WjbZLqSSDzHMMw/Xt6/zI+eXx8g/7dfa5ufDv0/e0j1fJ709r7K40lj4PifHrw+/fdF/PX9S+MlQMDng7o266PXx1j/4THdh7/7usJMbXq+Sfb2LPv5XL5zovlt7JekAH1H10xf2jJ7vM0CTnwVGKjqgd/fP0r9Tklw5fjPN1KC5ktXfnk+s5zXk2J+WSXwk2+X0evjzPcv/uubVF9QAv8SNNWs/utrEEBr9OPqI/ryx/8GYBjLQ0QvAAA= -->
