---
name: "rar-cowork-cookbook-d365-prospect-to-quote"
description: "Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Prospect to Quote process (6 L2 areas, 22 L3 processes), using USMF legal entity conventions via the D365 ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_prospect_to_quote", "rar_sha256": "03294391effeefcd53ae10f6fec57d917d71eda37b5c1b73eccf44e8b26b3d5b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
