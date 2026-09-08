---
name: "rar-cowork-cookbook-scheduled-brief-contract-suppliers-for-services"
description: "Builds a morning brief on contract suppliers for services from Dynamics 365 F&SCM (legal entity USMF) \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves an email draft to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_contract_suppliers_for_services", "rar_sha256": "fb63ae0e151c45cf293b131f8cc6c47a384adb83d1a98f14dbc106bde9ab5263", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_contract_suppliers_for_services`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_contract_suppliers_for_services_agent.py` and in the RCI capsule.

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

Contract suppliers for services Scheduled Email Brief — Builds a morning brief on contract suppliers for services from Dynamics 365 F&SCM (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-contract-suppliers-for-services
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
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_contract_suppliers_for_services_agent.py` and embedded as the fenced Python below (sha256 fb63ae0e151c45cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_contract_suppliers_for_services_agent.py` first:

```bash
python3 scheduled_brief_contract_suppliers_for_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_contract_suppliers_for_services_agent.py   # or on stdin
python3 scheduled_brief_contract_suppliers_for_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for services Scheduled Email Brief — Builds a morning brief on contract suppliers for services from Dynamics 365 F&SCM (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-contract-suppliers-for-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_contract_suppliers_for_services',
    "version": '3.0.3',
    "display_name": 'Contract suppliers for services Scheduled Email Brief',
    "description": 'Builds a morning brief on contract suppliers for services from Dynamics 365 F&SCM (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft to the o',
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
        "upstream_slug": 'scheduled-brief-contract-suppliers-for-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-contract-suppliers-for-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '549856618f0394fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-services'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-contract-suppliers-for-services', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where contract suppliers for services stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on contract suppliers for services for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads contract suppliers for services, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on contract suppliers for services from Dynamics 365 F&SCM (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft to the o', 'example_request': 'Send me the morning brief on contract suppliers for services in USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly contract-supplier brief for the responsible owner, drafted as an email and a Teams channel post rather than sent.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefContractSuppliersForServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefContractSuppliersForServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefContractSuppliersForServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
