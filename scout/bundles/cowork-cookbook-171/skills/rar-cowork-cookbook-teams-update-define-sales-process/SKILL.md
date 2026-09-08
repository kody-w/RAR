---
name: "rar-cowork-cookbook-teams-update-define-sales-process"
description: "Summarizes the current state of the define sales process from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_sales_process", "rar_sha256": "71ebf620caad2e7abc31736c24f676de2176771dca8f1067b8247ea9cd9f3972", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_sales_process`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_sales_process_agent.py` and in the RCI capsule.

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

Define sales process Teams Channel Update — Summarizes the current state of the define sales process from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-sales-process
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-define-sales-process-2026-05-24-card.json.",
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
    "process_scope": {
      "description": "The business process to summarize, e.g. define sales process.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_sales_process_agent.py` and embedded as the fenced Python below (sha256 71ebf620caad2e7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_sales_process_agent.py` first:

```bash
python3 teams_update_define_sales_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_sales_process_agent.py   # or on stdin
python3 teams_update_define_sales_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales process Teams Channel Update — Summarizes the current state of the define sales process from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-sales-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_sales_process',
    "version": '3.0.3',
    "display_name": 'Define sales process Teams Channel Update',
    "description": 'Summarizes the current state of the define sales process from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-sales-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-sales-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8645a5c3a3ac7192',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-process'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/teams-update-define-sales-process', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-define-sales-process-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'process_scope': 'The business process to summarize, e.g. define sales process.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define sales process. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-sales-process-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define sales process, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of the define sales process from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b', 'example_request': 'Draft a Teams update on define sales process for USMF from D365 ERP, with an Adaptive Card JSON I can review before posting.', 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The business process to summarize, e.g. define sales process.', 'name': 'process_scope'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-define-sales-process-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on define sales process status from D365 ERP, with an Adaptive Card saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineSalesProcess(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineSalesProcess'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-define-sales-process-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'process_scope': {'description': 'The business process to summarize, e.g. define sales process.', 'type': 'string'}},
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
    print(TeamsUpdateDefineSalesProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
