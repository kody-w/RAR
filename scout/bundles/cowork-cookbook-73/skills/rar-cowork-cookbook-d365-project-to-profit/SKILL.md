---
name: "rar-cowork-cookbook-d365-project-to-profit"
description: "Scopes the conversation to Dynamics 365 F&SCM Project to profit (6 L2 areas, 37 L3 processes), answering using documented entities and USMF legal entity conventions; call it for project-to-profit questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_project_to_profit", "rar_sha256": "b2e82cd24e38dce3d0c0869a8a98d8689f8735414b0333a075da03886e7df728", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
