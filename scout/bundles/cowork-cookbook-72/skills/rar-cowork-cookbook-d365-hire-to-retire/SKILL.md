---
name: "rar-cowork-cookbook-d365-hire-to-retire"
description: "Scopes the conversation to Dynamics 365 F&SCM Hire to retire (8 L2 areas, 55 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for HR/employee lifecycle questions in D365."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_hire_to_retire", "rar_sha256": "9ade9c36cc39bd690bef3af78f0b0547cdad1ba01bfa1caff90ecd4ae75134a1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_hire_to_retire`. The original RAPP
agent is preserved byte-for-byte in `d365_hire_to_retire_agent.py` and in the RCI capsule.

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

D365 Hire to retire Expert — Scopes the conversation to Dynamics 365 F&SCM Hire to retire (8 L2 areas, 55 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for HR/employee lifecycle questions in D365.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_hire_to_retire_agent.py` and embedded as the fenced Python below (sha256 9ade9c36cc39bd69…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_hire_to_retire_agent.py` first:

```bash
python3 d365_hire_to_retire_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_hire_to_retire_agent.py   # or on stdin
python3 d365_hire_to_retire_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Hire to retire Expert — Scopes the conversation to Dynamics 365 F&SCM Hire to retire (8 L2 areas, 55 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for HR/employee lifecycle questions in D365.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_hire_to_retire',
    "version": '3.0.3',
    "display_name": 'D365 Hire to retire Expert',
    "description": "Scopes the conversation to Dynamics 365 F&SCM Hire to retire (8 L2 areas, 55 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for HR/employee lifecycle questions in D365.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-hire-to-retire',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-hire-to-retire',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea4ca0f4482fc3a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'hire-to-retire/d365-hire-to-retire', 'uses_skills': {'custom': ['d365-hire-to-retire'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Hire to retire Expert** skill for this conversation. From now on, scope your help to the hire to retire domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Scopes the conversation to Dynamics 365 F&SCM Hire to retire (8 L2 areas, 55 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for HR/employee lifecycle questions in D365.", 'example_request': 'Act as the D365 Hire to retire expert and walk me through onboarding a new worker in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when working in Dynamics 365 F&SCM on hire-to-retire topics and you want answers scoped to that process area against the USMF legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365HireToRetire(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365HireToRetire'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(D365HireToRetire().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
