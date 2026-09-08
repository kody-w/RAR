---
name: "rar-cowork-cookbook-teams-update-engage-in-conversations-with-customers"
description: "Summarizes customer-conversation engagement status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_engage_in_conversations_with_customers", "rar_sha256": "b7afa20c3753e18105b5b294ff8934aa3f5f09ceb7e5c18bfb5fc60b2f5d7ecd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_engage_in_conversations_with_customers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_engage_in_conversations_with_customers_agent.py` and in the RCI capsule.

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

Engage in conversations with customers Teams Channel Update — Summarizes customer-conversation engagement status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-engage-in-conversations-with-customers
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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
    "topic": {
      "description": "The status area to summarize, e.g. engage in conversations with customers.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_engage_in_conversations_with_customers_agent.py` and embedded as the fenced Python below (sha256 b7afa20c3753e181…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_engage_in_conversations_with_customers_agent.py` first:

```bash
python3 teams_update_engage_in_conversations_with_customers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_engage_in_conversations_with_customers_agent.py   # or on stdin
python3 teams_update_engage_in_conversations_with_customers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Engage in conversations with customers Teams Channel Update — Summarizes customer-conversation engagement status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-engage-in-conversations-with-customers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_engage_in_conversations_with_customers',
    "version": '3.0.3',
    "display_name": 'Engage in conversations with customers Teams Channel Update',
    "description": 'Summarizes customer-conversation engagement status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-engage-in-conversations-with-customers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-engage-in-conversations-with-customers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1565a06c5c8459b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/engage-in-conversations-with-customers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-engage-in-conversations-with-customers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'topic': 'The status area to summarize, e.g. engage in conversations with customers.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of engage in conversations with customers. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-engage-in-conversations-with-customers-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads engage in conversations with customers, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes customer-conversation engagement status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.', 'example_request': "Draft a Teams update on customer conversation engagement for USMF with an Adaptive Card - don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The status area to summarize, e.g. engage in conversations with customers.', 'name': 'topic'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams channel update plus Adaptive Card on engage-in-conversations-with-customers status from D365 F&SCM; it does not post anything.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateEngageInConversationsWithCustomers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEngageInConversationsWithCustomers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-...-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The status area to summarize, e.g. engage in conversations with customers.', 'type': 'string'}},
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
    print(TeamsUpdateEngageInConversationsWithCustomers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
