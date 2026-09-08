---
name: "rar-cowork-cookbook-teams-update-define-quality-procedures-and-tools"
description: "Summarizes the current state of quality procedures and tools from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_quality_procedures_and_tools", "rar_sha256": "6e4a4bd555a6a3071f1c6e66d0981aeaf399cd35c9950e5fc5ab57e878819d96", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
