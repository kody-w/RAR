---
name: "rar-cowork-cookbook-d365-source-to-pay-manage-supplier-relationships"
description: "Scopes the conversation to Dynamics 365 F&SCM Source-to-pay, Manage supplier relationships (8 L3 processes), answering with that area's entities and USMF legal-entity conventions and prefacing D365 replies with the requi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_source_to_pay_manage_supplier_relationships", "rar_sha256": "bdbd78b6e693b13182f8c5d956073f4c5222e969e5462dbc5ddc2f67ae73ac2c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
