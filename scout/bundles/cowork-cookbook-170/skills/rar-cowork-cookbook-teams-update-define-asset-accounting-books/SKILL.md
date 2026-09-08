---
name: "rar-cowork-cookbook-teams-update-define-asset-accounting-books"
description: "Summarizes the current state of asset accounting books from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON file."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_asset_accounting_books", "rar_sha256": "4b8789499a42ba6d53da51ac248195056b376afaf7c20abb2c6c407b11ccc4d9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_asset_accounting_books`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_asset_accounting_books_agent.py` and in the RCI capsule.

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

Define asset accounting books Teams Channel Update — Summarizes the current state of asset accounting books from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON file.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-define-asset-accounting-books-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_asset_accounting_books_agent.py` and embedded as the fenced Python below (sha256 4b8789499a42ba6d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_asset_accounting_books_agent.py` first:

```bash
python3 teams_update_define_asset_accounting_books_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_asset_accounting_books_agent.py   # or on stdin
python3 teams_update_define_asset_accounting_books_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define asset accounting books Teams Channel Update — Summarizes the current state of asset accounting books from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON file.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_asset_accounting_books',
    "version": '3.0.3',
    "display_name": 'Define asset accounting books Teams Channel Update',
    "description": 'Summarizes the current state of asset accounting books from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON file.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-asset-accounting-books',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd9e29b6160427b2f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-asset-accounting-books'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-define-asset-accounting-books', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-define-asset-accounting-books-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define asset accounting books. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-asset-accounting-books-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads define asset accounting books, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of asset accounting books from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON file.', 'example_request': "Draft a Teams update on define asset accounting books for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-define-asset-accounting-books-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update on asset accounting books status, with an Adaptive Card for triage, saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineAssetAccountingBooks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineAssetAccountingBooks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-define-asset-accounting-books-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDefineAssetAccountingBooks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
