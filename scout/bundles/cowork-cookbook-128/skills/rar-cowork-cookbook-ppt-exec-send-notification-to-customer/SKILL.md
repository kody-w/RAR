---
name: "rar-cowork-cookbook-ppt-exec-send-notification-to-customer"
description: "Builds a read-only executive PowerPoint deck on send-notification-to-customer status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_send_notification_to_customer", "rar_sha256": "d8046136538b1ab5a1fd921f3e0c992b078f301865ac10510a16df1f8464818b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_send_notification_to_customer`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_send_notification_to_customer_agent.py` and in the RCI capsule.

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

Send notification to customer Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on send-notification-to-customer status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-send-notification-to-customer
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-send-notification-to-customer-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for the trend comparison (e.g. monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_send_notification_to_customer_agent.py` and embedded as the fenced Python below (sha256 d8046136538b1ab5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_send_notification_to_customer_agent.py` first:

```bash
python3 ppt_exec_send_notification_to_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_send_notification_to_customer_agent.py   # or on stdin
python3 ppt_exec_send_notification_to_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send notification to customer Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on send-notification-to-customer status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-send-notification-to-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_send_notification_to_customer',
    "version": '3.0.3',
    "display_name": 'Send notification to customer Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on send-notification-to-customer status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-send-notification-to-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-send-notification-to-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'da9b7f8c081afb9e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/send-notification-to-customer'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-send-notification-to-customer', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-send-notification-to-customer-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for the trend comparison (e.g. monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for send notification to customer reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on send notification to customer for a 15-minute monthly review. Produce 'ppt-exec-send-notification-to-customer-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads send notification to customer data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on send-notification-to-customer status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': "Build the exec PowerPoint on send notification to customer for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-send-notification-to-customer-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on send-notification-to-customer status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecSendNotificationToCustomer(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecSendNotificationToCustomer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-send-notification-to-customer-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review).', 'type': 'string'}},
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
    print(PptExecSendNotificationToCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
