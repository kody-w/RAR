---
name: "rar-cowork-cookbook-teams-update-process-customer-prepayments"
description: "Summarizes the current state of customer prepayments from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_customer_prepayments", "rar_sha256": "8265de005a08607e817b14a29f4d0744a1c563ed3d62d501d9182e9cc6408bcf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_customer_prepayments`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_customer_prepayments_agent.py` and in the RCI capsule.

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

Process customer prepayments Teams Channel Update — Summarizes the current state of customer prepayments from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments
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
    "as_of_date": {
      "description": "Date used for the status snapshot and the card filename.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON artifact.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_customer_prepayments_agent.py` and embedded as the fenced Python below (sha256 8265de005a08607e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_customer_prepayments_agent.py` first:

```bash
python3 teams_update_process_customer_prepayments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_customer_prepayments_agent.py   # or on stdin
python3 teams_update_process_customer_prepayments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer prepayments Teams Channel Update — Summarizes the current state of customer prepayments from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_customer_prepayments',
    "version": '3.0.3',
    "display_name": 'Process customer prepayments Teams Channel Update',
    "description": 'Summarizes the current state of customer prepayments from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-process-customer-prepayments',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b94ad658e40eeccd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-prepayments'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-process-customer-prepayments', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the status snapshot and the card filename.', 'card_filename': 'Output filename for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of process customer prepayments. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-process-customer-prepayments-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads process customer prepayments, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of customer prepayments from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams update on process customer prepayments for USMF as of 2026-05-24, with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to report on (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Date used for the status snapshot and the card filename.', 'name': 'as_of_date'}, {'description': 'Output filename for the Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on process customer prepayments status, with an Adaptive Card for triage, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateProcessCustomerPrepayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessCustomerPrepayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the status snapshot and the card filename.', 'type': 'string'}, 'card_filename': {'description': 'Output filename for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateProcessCustomerPrepayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
