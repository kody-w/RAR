---
name: "rar-cowork-cookbook-d365-design-to-retire"
description: "Scopes the conversation to a Dynamics 365 F&SCM Design-to-retire expert (5 L2 areas, 31 L3 processes), answering against legal entity USMF via the D365 ERP plugin; call when working in that domain."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_design_to_retire", "rar_sha256": "d05110d88176f452aea41a461a5ad553cd897aa7f0e2f88e55f5568938f6c061", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
