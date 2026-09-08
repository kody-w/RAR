---
name: "rar-cowork-cookbook-scheduled-brief-return-goods-to-suppliers"
description: "Builds a return-goods-to-suppliers morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_return_goods_to_suppliers", "rar_sha256": "afa9713b34e37a39ffc3950e9a6fd2a30fedcf49034b59612daea8edfe57ead9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_return_goods_to_suppliers`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_return_goods_to_suppliers_agent.py` and in the RCI capsule.

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

Return goods to suppliers Scheduled Email Brief — Builds a return-goods-to-suppliers morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-return-goods-to-suppliers
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_return_goods_to_suppliers_agent.py` and embedded as the fenced Python below (sha256 afa9713b34e37a39…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_return_goods_to_suppliers_agent.py` first:

```bash
python3 scheduled_brief_return_goods_to_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_return_goods_to_suppliers_agent.py   # or on stdin
python3 scheduled_brief_return_goods_to_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to suppliers Scheduled Email Brief — Builds a return-goods-to-suppliers morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-return-goods-to-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_return_goods_to_suppliers',
    "version": '3.0.3',
    "display_name": 'Return goods to suppliers Scheduled Email Brief',
    "description": 'Builds a return-goods-to-suppliers morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-return-goods-to-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-return-goods-to-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ba8af8d22b4da3f9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/return-goods-to-suppliers'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-return-goods-to-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where return goods to suppliers stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on return goods to suppliers for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads return goods to suppliers, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a return-goods-to-suppliers morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a', 'example_request': "Draft my return-to-supplier morning brief for USMF and send it to the owner's drafts plus a Teams summary.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly return-to-supplier brief for the responsible owner, drafted as email (not sent) and as a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefReturnGoodsToSuppliers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReturnGoodsToSuppliers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefReturnGoodsToSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
