---
name: "rar-cowork-cookbook-d365-order-to-cash"
description: "Scopes the conversation to Dynamics 365 Finance & Supply Chain Order to Cash (5 L2 areas, 42 L3 processes), answering using D365 entities and USMF legal entity conventions via the ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_order_to_cash", "rar_sha256": "eeee1d0ebf32b052bdd76a4f63089ac736864953e2490392681365f092515f27", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_order_to_cash`. The original RAPP
agent is preserved byte-for-byte in `d365_order_to_cash_agent.py` and in the RCI capsule.

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

D365 Order to cash Expert — Scopes the conversation to Dynamics 365 Finance & Supply Chain Order to Cash (5 L2 areas, 42 L3 processes), answering using D365 entities and USMF legal entity conventions via the ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-order-to-cash
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_order_to_cash_agent.py` and embedded as the fenced Python below (sha256 eeee1d0ebf32b052…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_order_to_cash_agent.py` first:

```bash
python3 d365_order_to_cash_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_order_to_cash_agent.py   # or on stdin
python3 d365_order_to_cash_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Order to cash Expert — Scopes the conversation to Dynamics 365 Finance & Supply Chain Order to Cash (5 L2 areas, 42 L3 processes), answering using D365 entities and USMF legal entity conventions via the ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-order-to-cash
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_order_to_cash',
    "version": '3.0.3',
    "display_name": 'D365 Order to cash Expert',
    "description": 'Scopes the conversation to Dynamics 365 Finance & Supply Chain Order to Cash (5 L2 areas, 42 L3 processes), answering using D365 entities and USMF legal entity conventions via the ERP plugin.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-order-to-cash',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-order-to-cash',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4463babd043c52a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'order-to-cash/d365-order-to-cash', 'uses_skills': {'custom': ['d365-order-to-cash'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Order to cash Expert** skill for this conversation. From now on, scope your help to the order to cash domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 Finance & Supply Chain Order to Cash (5 L2 areas, 42 L3 processes), answering using D365 entities and USMF legal entity conventions via the ERP plugin.', 'example_request': 'Act as the D365 Order to Cash expert and walk me through the sales order to invoice flow in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs D365 F&SCM help on order to cash topics — sales orders, invoicing, collections — using the ERP plugin against USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365OrderToCash(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365OrderToCash'
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
    print(D365OrderToCash().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
