---
name: "rar-cowork-cookbook-d365-order-to-cash"
description: "Scopes the conversation to Dynamics 365 Finance & Supply Chain Order to Cash (5 L2 areas, 42 L3 processes), answering using D365 entities and USMF legal entity conventions via the ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_order_to_cash", "rar_sha256": "eeee1d0ebf32b052bdd76a4f63089ac736864953e2490392681365f092515f27", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
