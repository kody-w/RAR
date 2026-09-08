---
name: "rar-cowork-cookbook-d365-source-to-pay-manage-supplier-relationships"
description: "Scopes the conversation to Dynamics 365 F&SCM Source-to-pay, Manage supplier relationships (8 L3 processes), answering with that area's entities and USMF legal-entity conventions and prefacing D365 replies with the requi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_source_to_pay_manage_supplier_relationships", "rar_sha256": "bdbd78b6e693b13182f8c5d956073f4c5222e969e5462dbc5ddc2f67ae73ac2c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_source_to_pay_manage_supplier_relationships`. The original RAPP
agent is preserved byte-for-byte in `d365_source_to_pay_manage_supplier_relationships_agent.py` and in the RCI capsule.

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

D365 Manage supplier relationships Expert — Scopes the conversation to Dynamics 365 F&SCM Source-to-pay, Manage supplier relationships (8 L3 processes), answering with that area's entities and USMF legal-entity conventions and prefacing D365 replies with the requi

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-source-to-pay-manage-supplier-relationships
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_source_to_pay_manage_supplier_relationships_agent.py` and embedded as the fenced Python below (sha256 bdbd78b6e693b131…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_source_to_pay_manage_supplier_relationships_agent.py` first:

```bash
python3 d365_source_to_pay_manage_supplier_relationships_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_source_to_pay_manage_supplier_relationships_agent.py   # or on stdin
python3 d365_source_to_pay_manage_supplier_relationships_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage supplier relationships Expert — Scopes the conversation to Dynamics 365 F&SCM Source-to-pay, Manage supplier relationships (8 L3 processes), answering with that area's entities and USMF legal-entity conventions and prefacing D365 replies with the requi

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-source-to-pay-manage-supplier-relationships
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_source_to_pay_manage_supplier_relationships',
    "version": '3.0.3',
    "display_name": 'D365 Manage supplier relationships Expert',
    "description": "Scopes the conversation to Dynamics 365 F&SCM Source-to-pay, Manage supplier relationships (8 L3 processes), answering with that area's entities and USMF legal-entity conventions and prefacing D365 replies with the requi",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-source-to-pay-manage-supplier-relationships',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-source-to-pay-manage-supplier-relationships',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9812b535089f2fe7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'source-to-pay/d365-source-to-pay-manage-supplier-relationships', 'uses_skills': {'custom': ['d365-source-to-pay-manage-supplier-relationships'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Manage supplier relationships Expert** skill for this conversation. From now on, scope your help to the source to pay domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Scopes the conversation to Dynamics 365 F&SCM Source-to-pay, Manage supplier relationships (8 L3 processes), answering with that area's entities and USMF legal-entity conventions and prefacing D365 replies with the requi", 'example_request': 'Act as the D365 Manage supplier relationships expert and help me with vendor setup in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs Dynamics 365 F&SCM help specific to managing supplier relationships within Source to pay, against the USMF legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365SourceToPayManageSupplierRelationships(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365SourceToPayManageSupplierRelationships'
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
    print(D365SourceToPayManageSupplierRelationships().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
