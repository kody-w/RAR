---
name: "rar-cowork-cookbook-adaptive-card-maintain-contacts-and-accounts"
description: "Generates a read-only Adaptive Card JSON file summarizing contacts and accounts maintenance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts", "rar_sha256": "17c2b2ff8a02f58f9cbd706ff9d4cfbfa73d9bef61489c0d3855b79bdb33bec4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
