---
name: "rar-cowork-cookbook-scheduled-brief-quarantine-received-goods"
description: "Builds a morning brief on quarantine received goods from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_quarantine_received_goods", "rar_sha256": "b70ec406b632634381cda78ab91782384933b0e6349f3a9da33ee1d8a78a23b8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
