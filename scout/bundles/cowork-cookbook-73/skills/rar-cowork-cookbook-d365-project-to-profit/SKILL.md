---
name: "rar-cowork-cookbook-d365-project-to-profit"
description: "Scopes the conversation to Dynamics 365 F&SCM Project to profit (6 L2 areas, 37 L3 processes), answering using documented entities and USMF legal entity conventions; call it for project-to-profit questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_project_to_profit", "rar_sha256": "b2e82cd24e38dce3d0c0869a8a98d8689f8735414b0333a075da03886e7df728", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_project_to_profit`. The original RAPP
agent is preserved byte-for-byte in `d365_project_to_profit_agent.py` and in the RCI capsule.

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

D365 Project to profit Expert — Scopes the conversation to Dynamics 365 F&SCM Project to profit (6 L2 areas, 37 L3 processes), answering using documented entities and USMF legal entity conventions; call it for project-to-profit questions.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit
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
      "description": "Legal entity context for the D365 ERP plugin; defaults to USMF.",
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
    "project_to_profit_question": {
      "description": "The specific project-to-profit task, process, or entity you need help with.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_project_to_profit_agent.py` and embedded as the fenced Python below (sha256 b2e82cd24e38dce3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_project_to_profit_agent.py` first:

```bash
python3 d365_project_to_profit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_project_to_profit_agent.py   # or on stdin
python3 d365_project_to_profit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Project to profit Expert — Scopes the conversation to Dynamics 365 F&SCM Project to profit (6 L2 areas, 37 L3 processes), answering using documented entities and USMF legal entity conventions; call it for project-to-profit questions.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_project_to_profit',
    "version": '3.0.3',
    "display_name": 'D365 Project to profit Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM Project to profit (6 L2 areas, 37 L3 processes), answering using documented entities and USMF legal entity conventions; call it for project-to-profit questions.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-project-to-profit',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-project-to-profit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '72ba6fe8ce851d19',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'project-to-profit/d365-project-to-profit', 'uses_skills': {'custom': ['d365-project-to-profit'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Legal entity context for the D365 ERP plugin; defaults to USMF.', 'project_to_profit_question': 'The specific project-to-profit task, process, or entity you need help with.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Project to profit Expert** skill for this conversation. From now on, scope your help to the project to profit domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM Project to profit (6 L2 areas, 37 L3 processes), answering using documented entities and USMF legal entity conventions; call it for project-to-profit questions.', 'example_request': 'Act as the D365 Project to profit expert — walk me through project invoicing in USMF.', 'inputs': [{'description': 'The specific project-to-profit task, process, or entity you need help with.', 'name': 'project to profit question'}, {'description': 'Legal entity context for the D365 ERP plugin; defaults to USMF.', 'name': 'legal entity'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when working in Dynamics 365 Finance & Supply Chain Management on project to profit processes and you want answers scoped to that domain against USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ProjectToProfit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProjectToProfit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Legal entity context for the D365 ERP plugin; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'project_to_profit_question': {'description': 'The specific project-to-profit task, process, or entity you need help with.', 'type': 'string'}},
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
    print(D365ProjectToProfit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
