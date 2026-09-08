---
name: "rar-cowork-cookbook-d365-hire-to-retire"
description: "Scopes the conversation to Dynamics 365 F&SCM Hire to retire (8 L2 areas, 55 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for HR/employee lifecycle questions in D365."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_hire_to_retire", "rar_sha256": "9ade9c36cc39bd690bef3af78f0b0547cdad1ba01bfa1caff90ecd4ae75134a1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
