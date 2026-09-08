---
name: "rar-cowork-cookbook-scheduled-brief-contract-suppliers-for-services"
description: "Builds a morning brief on contract suppliers for services from Dynamics 365 F&SCM (legal entity USMF) \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves an email draft to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_contract_suppliers_for_services", "rar_sha256": "fb63ae0e151c45cf293b131f8cc6c47a384adb83d1a98f14dbc106bde9ab5263", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
