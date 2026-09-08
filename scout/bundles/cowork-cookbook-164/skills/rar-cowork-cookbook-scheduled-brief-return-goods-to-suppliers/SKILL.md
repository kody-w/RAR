---
name: "rar-cowork-cookbook-scheduled-brief-return-goods-to-suppliers"
description: "Builds a return-goods-to-suppliers morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_return_goods_to_suppliers", "rar_sha256": "afa9713b34e37a39ffc3950e9a6fd2a30fedcf49034b59612daea8edfe57ead9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
