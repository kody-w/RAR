---
name: "rar-cowork-cookbook-adaptive-card-maintain-contacts-and-accounts"
description: "Generates a read-only Adaptive Card JSON file summarizing contacts and accounts maintenance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts", "rar_sha256": "17c2b2ff8a02f58f9cbd706ff9d4cfbfa73d9bef61489c0d3855b79bdb33bec4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_maintain_contacts_and_accounts_agent.py` and in the RCI capsule.

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

Maintain contacts and accounts Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing contacts and accounts maintenance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts
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
    "action_buttons": {
      "description": "Which 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date used in the card header timestamp and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-maintain-contacts-and-accounts-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_maintain_contacts_and_accounts_agent.py` and embedded as the fenced Python below (sha256 17c2b2ff8a02f58f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_maintain_contacts_and_accounts_agent.py` first:

```bash
python3 adaptive_card_maintain_contacts_and_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_maintain_contacts_and_accounts_agent.py   # or on stdin
python3 adaptive_card_maintain_contacts_and_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain contacts and accounts Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing contacts and accounts maintenance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts',
    "version": '3.0.2',
    "display_name": 'Maintain contacts and accounts Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing contacts and accounts maintenance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-maintain-contacts-and-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b480651abbfdeb92',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-maintain-contacts-and-accounts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'Which 2-3 action buttons to place on the card.', 'as_of_date': 'Date used in the card header timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-maintain-contacts-and-accounts-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical maintain contacts and accounts status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-maintain-contacts-and-accounts-2026-05-24-card.json' that visualizes the current state of maintain contacts and accounts. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current maintain contacts and accounts KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing contacts and accounts maintenance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing maintain contacts and accounts status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-maintain-contacts-and-accounts-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used in the card header timestamp and filename.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'Which 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of maintain contacts and accounts status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMaintainContactsAndAccounts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMaintainContactsAndAccounts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'Which 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used in the card header timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-maintain-contacts-and-accounts-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardMaintainContactsAndAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
