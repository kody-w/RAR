---
name: "rar-cowork-cookbook-d365-concept-to-market"
description: "Scopes the assistant to Dynamics 365 F&SCM Concept to market (6 L2 areas, 31 L3 processes), answering using that domain's entities and USMF legal entity conventions; call it for concept-to-market questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_concept_to_market", "rar_sha256": "5896dae390879521e8df07910a4c7f033257cec2d680a64f4f7837a360084a5e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_concept_to_market`. The original RAPP
agent is preserved byte-for-byte in `d365_concept_to_market_agent.py` and in the RCI capsule.

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

D365 Concept to market Expert — Scopes the assistant to Dynamics 365 F&SCM Concept to market (6 L2 areas, 31 L3 processes), answering using that domain's entities and USMF legal entity conventions; call it for concept-to-market questions.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-concept-to-market
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_concept_to_market_agent.py` and embedded as the fenced Python below (sha256 5896dae390879521…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_concept_to_market_agent.py` first:

```bash
python3 d365_concept_to_market_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_concept_to_market_agent.py   # or on stdin
python3 d365_concept_to_market_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Concept to market Expert — Scopes the assistant to Dynamics 365 F&SCM Concept to market (6 L2 areas, 31 L3 processes), answering using that domain's entities and USMF legal entity conventions; call it for concept-to-market questions.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-concept-to-market
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_concept_to_market',
    "version": '3.0.3',
    "display_name": 'D365 Concept to market Expert',
    "description": "Scopes the assistant to Dynamics 365 F&SCM Concept to market (6 L2 areas, 31 L3 processes), answering using that domain's entities and USMF legal entity conventions; call it for concept-to-market questions.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-concept-to-market',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-concept-to-market',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '95cf7741c3a09d6f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'concept-to-market/d365-concept-to-market', 'uses_skills': {'custom': ['d365-concept-to-market'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Concept to market Expert** skill for this conversation. From now on, scope your help to the concept to market domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Scopes the assistant to Dynamics 365 F&SCM Concept to market (6 L2 areas, 31 L3 processes), answering using that domain's entities and USMF legal entity conventions; call it for concept-to-market questions.", 'example_request': 'Act as the D365 Concept to market expert and help me with product introduction in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when working in Dynamics 365 Finance & Supply Chain Management on Concept to market processes and you want answers scoped to that domain against USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ConceptToMarket(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ConceptToMarket'
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
    print(D365ConceptToMarket().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
