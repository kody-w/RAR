---
name: "rar-cowork-cookbook-ppt-exec-send-notification-to-customer"
description: "Builds a read-only executive PowerPoint deck on send-notification-to-customer status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_send_notification_to_customer", "rar_sha256": "d8046136538b1ab5a1fd921f3e0c992b078f301865ac10510a16df1f8464818b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
