---
name: "rar-cowork-cookbook-d365-prospect-to-quote"
description: "Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Prospect to Quote process (6 L2 areas, 22 L3 processes), using USMF legal entity conventions via the D365 ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_prospect_to_quote", "rar_sha256": "03294391effeefcd53ae10f6fec57d917d71eda37b5c1b73eccf44e8b26b3d5b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_prospect_to_quote`. The original RAPP
agent is preserved byte-for-byte in `d365_prospect_to_quote_agent.py` and in the RCI capsule.

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

D365 Prospect to quote Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Prospect to Quote process (6 L2 areas, 22 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-prospect-to-quote
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
      "description": "D365 legal entity context; defaults to USMF.",
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
    "question": {
      "description": "The prospect-to-quote question or task the user wants help with.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_prospect_to_quote_agent.py` and embedded as the fenced Python below (sha256 03294391effeefcd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_prospect_to_quote_agent.py` first:

```bash
python3 d365_prospect_to_quote_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_prospect_to_quote_agent.py   # or on stdin
python3 d365_prospect_to_quote_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Prospect to quote Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Prospect to Quote process (6 L2 areas, 22 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-prospect-to-quote
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_prospect_to_quote',
    "version": '3.0.3',
    "display_name": 'D365 Prospect to quote Expert',
    "description": 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Prospect to Quote process (6 L2 areas, 22 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-prospect-to-quote',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-prospect-to-quote',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd18f96e700847ad6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'prospect-to-quote/d365-prospect-to-quote', 'uses_skills': {'custom': ['d365-prospect-to-quote'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity context; defaults to USMF.', 'question': 'The prospect-to-quote question or task the user wants help with.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Prospect to quote Expert** skill for this conversation. From now on, scope your help to the prospect to quote domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Prospect to Quote process (6 L2 areas, 22 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.', 'example_request': 'Walk me through creating a sales quotation from an opportunity in D365 for USMF.', 'inputs': [{'description': 'The prospect-to-quote question or task the user wants help with.', 'name': 'question'}, {'description': 'D365 legal entity context; defaults to USMF.', 'name': 'legal_entity'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs D365 F&SCM guidance on prospect-to-quote work: leads, opportunities, quotations, customers, pricing, and related entities in USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ProspectToQuote(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProspectToQuote'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity context; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'question': {'description': 'The prospect-to-quote question or task the user wants help with.', 'type': 'string'}},
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
    print(D365ProspectToQuote().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
