---
name: "rar-cowork-cookbook-teams-update-define-quality-procedures-and-tools"
description: "Summarizes the current state of quality procedures and tools from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_quality_procedures_and_tools", "rar_sha256": "6e4a4bd555a6a3071f1c6e66d0981aeaf399cd35c9950e5fc5ab57e878819d96", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_quality_procedures_and_tools`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_quality_procedures_and_tools_agent.py` and in the RCI capsule.

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

Define quality procedures and tools Teams Channel Update — Summarizes the current state of quality procedures and tools from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-quality-procedures-and-tools
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
      "description": "Filename for the generated Adaptive Card JSON artifact.",
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
      "description": "Subject of the update, e.g. define quality procedures and tools.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_quality_procedures_and_tools_agent.py` and embedded as the fenced Python below (sha256 6e4a4bd555a6a307…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_quality_procedures_and_tools_agent.py` first:

```bash
python3 teams_update_define_quality_procedures_and_tools_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_quality_procedures_and_tools_agent.py   # or on stdin
python3 teams_update_define_quality_procedures_and_tools_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define quality procedures and tools Teams Channel Update — Summarizes the current state of quality procedures and tools from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-quality-procedures-and-tools
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_quality_procedures_and_tools',
    "version": '3.0.3',
    "display_name": 'Define quality procedures and tools Teams Channel Update',
    "description": 'Summarizes the current state of quality procedures and tools from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-quality-procedures-and-tools',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-quality-procedures-and-tools',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4512659c1ced970',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/define-quality-procedures-and-tools'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-define-quality-procedures-and-tools', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'topic': 'Subject of the update, e.g. define quality procedures and tools.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define quality procedures and tools. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-quality-procedures-and-tools-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define quality procedures and tools, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of quality procedures and tools from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.', 'example_request': 'Draft a Teams update on quality procedures and tools for USMF and save the Adaptive Card for me to review.', 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the update, e.g. define quality procedures and tools.', 'name': 'topic'}, {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on quality procedures and tools status from D365 ERP data, with an Adaptive Card artifact saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineQualityProceduresAndTools(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineQualityProceduresAndTools'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'Subject of the update, e.g. define quality procedures and tools.', 'type': 'string'}},
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
    print(TeamsUpdateDefineQualityProceduresAndTools().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
