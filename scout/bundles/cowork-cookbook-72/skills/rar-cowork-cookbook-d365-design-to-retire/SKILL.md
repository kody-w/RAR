---
name: "rar-cowork-cookbook-d365-design-to-retire"
description: "Scopes the conversation to a Dynamics 365 F&SCM Design-to-retire expert (5 L2 areas, 31 L3 processes), answering against legal entity USMF via the D365 ERP plugin; call when working in that domain."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_design_to_retire", "rar_sha256": "d05110d88176f452aea41a461a5ad553cd897aa7f0e2f88e55f5568938f6c061", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_design_to_retire`. The original RAPP
agent is preserved byte-for-byte in `d365_design_to_retire_agent.py` and in the RCI capsule.

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

D365 Design to retire Expert — Scopes the conversation to a Dynamics 365 F&SCM Design-to-retire expert (5 L2 areas, 31 L3 processes), answering against legal entity USMF via the D365 ERP plugin; call when working in that domain.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-design-to-retire
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_design_to_retire_agent.py` and embedded as the fenced Python below (sha256 d05110d88176f452…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_design_to_retire_agent.py` first:

```bash
python3 d365_design_to_retire_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_design_to_retire_agent.py   # or on stdin
python3 d365_design_to_retire_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Design to retire Expert — Scopes the conversation to a Dynamics 365 F&SCM Design-to-retire expert (5 L2 areas, 31 L3 processes), answering against legal entity USMF via the D365 ERP plugin; call when working in that domain.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-design-to-retire
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_design_to_retire',
    "version": '3.0.3',
    "display_name": 'D365 Design to retire Expert',
    "description": 'Scopes the conversation to a Dynamics 365 F&SCM Design-to-retire expert (5 L2 areas, 31 L3 processes), answering against legal entity USMF via the D365 ERP plugin; call when working in that domain.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-design-to-retire',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-design-to-retire',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f3c97077ebed1576',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'design-to-retire/d365-design-to-retire', 'uses_skills': {'custom': ['d365-design-to-retire'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Design to retire Expert** skill for this conversation. From now on, scope your help to the design to retire domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to a Dynamics 365 F&SCM Design-to-retire expert (5 L2 areas, 31 L3 processes), answering against legal entity USMF via the D365 ERP plugin; call when working in that domain.', 'example_request': 'Act as the D365 Design to retire expert and walk me through the product lifecycle processes in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when asking Dynamics 365 Finance & Supply Chain questions within the Design to retire end-to-end process and its L2/L3 areas.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365DesignToRetire(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365DesignToRetire'
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
    print(D365DesignToRetire().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
