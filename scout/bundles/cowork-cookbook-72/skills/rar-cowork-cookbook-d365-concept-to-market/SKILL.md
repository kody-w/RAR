---
name: "rar-cowork-cookbook-d365-concept-to-market"
description: "Scopes the assistant to Dynamics 365 F&SCM Concept to market (6 L2 areas, 31 L3 processes), answering using that domain's entities and USMF legal entity conventions; call it for concept-to-market questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_concept_to_market", "rar_sha256": "5896dae390879521e8df07910a4c7f033257cec2d680a64f4f7837a360084a5e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
