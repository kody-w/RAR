---
name: "rar-cowork-cookbook-scheduled-brief-quarantine-received-goods"
description: "Builds a morning brief on quarantine received goods from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_quarantine_received_goods", "rar_sha256": "b70ec406b632634381cda78ab91782384933b0e6349f3a9da33ee1d8a78a23b8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_quarantine_received_goods`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_quarantine_received_goods_agent.py` and in the RCI capsule.

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

Quarantine received goods Scheduled Email Brief — Builds a morning brief on quarantine received goods from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-quarantine-received-goods
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
      "description": "When to run it, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_quarantine_received_goods_agent.py` and embedded as the fenced Python below (sha256 b70ec406b6326343…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_quarantine_received_goods_agent.py` first:

```bash
python3 scheduled_brief_quarantine_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_quarantine_received_goods_agent.py   # or on stdin
python3 scheduled_brief_quarantine_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine received goods Scheduled Email Brief — Builds a morning brief on quarantine received goods from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-quarantine-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_quarantine_received_goods',
    "version": '3.0.3',
    "display_name": 'Quarantine received goods Scheduled Email Brief',
    "description": 'Builds a morning brief on quarantine received goods from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-quarantine-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-quarantine-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f872f97c53a6ce6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/quarantine-received-goods'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-quarantine-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run it, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where quarantine received goods stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on quarantine received goods for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads quarantine received goods, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on quarantine received goods from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner a', 'example_request': 'Give me the quarantine received goods morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run it, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly quarantine received goods brief for the responsible owner, drafted as an email plus a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefQuarantineReceivedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefQuarantineReceivedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run it, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefQuarantineReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
