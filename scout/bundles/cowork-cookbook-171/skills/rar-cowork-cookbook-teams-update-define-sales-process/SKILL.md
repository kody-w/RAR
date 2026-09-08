---
name: "rar-cowork-cookbook-teams-update-define-sales-process"
description: "Summarizes the current state of the define sales process from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_sales_process", "rar_sha256": "71ebf620caad2e7abc31736c24f676de2176771dca8f1067b8247ea9cd9f3972", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
