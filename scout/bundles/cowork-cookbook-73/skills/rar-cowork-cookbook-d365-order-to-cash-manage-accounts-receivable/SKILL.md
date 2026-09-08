---
name: "rar-cowork-cookbook-d365-order-to-cash-manage-accounts-receivable"
description: "Answers Dynamics 365 F&SCM questions scoped to the Manage accounts receivable subdomain of order to cash (13 L3 processes), using D365 ERP plugin conventions against legal entity USMF."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_order_to_cash_manage_accounts_receivable", "rar_sha256": "85fac6e1303caeabd141c3f142e0171b4db42e59a7925f0f6216a84d9f409a74", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_order_to_cash_manage_accounts_receivable`. The original RAPP
agent is preserved byte-for-byte in `d365_order_to_cash_manage_accounts_receivable_agent.py` and in the RCI capsule.

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

D365 Manage accounts receivable Expert — Answers Dynamics 365 F&SCM questions scoped to the Manage accounts receivable subdomain of order to cash (13 L3 processes), using D365 ERP plugin conventions against legal entity USMF.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-order-to-cash-manage-accounts-receivable
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_order_to_cash_manage_accounts_receivable_agent.py` and embedded as the fenced Python below (sha256 85fac6e1303caeab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_order_to_cash_manage_accounts_receivable_agent.py` first:

```bash
python3 d365_order_to_cash_manage_accounts_receivable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_order_to_cash_manage_accounts_receivable_agent.py   # or on stdin
python3 d365_order_to_cash_manage_accounts_receivable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage accounts receivable Expert — Answers Dynamics 365 F&SCM questions scoped to the Manage accounts receivable subdomain of order to cash (13 L3 processes), using D365 ERP plugin conventions against legal entity USMF.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-order-to-cash-manage-accounts-receivable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_order_to_cash_manage_accounts_receivable',
    "version": '3.0.3',
    "display_name": 'D365 Manage accounts receivable Expert',
    "description": 'Answers Dynamics 365 F&SCM questions scoped to the Manage accounts receivable subdomain of order to cash (13 L3 processes), using D365 ERP plugin conventions against legal entity USMF.',
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
        "upstream_slug": 'd365-order-to-cash-manage-accounts-receivable',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-order-to-cash-manage-accounts-receivable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '127123dfd4eb6815',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'order-to-cash/d365-order-to-cash-manage-accounts-receivable', 'uses_skills': {'custom': ['d365-order-to-cash-manage-accounts-receivable'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Manage accounts receivable Expert** skill for this conversation. From now on, scope your help to the order to cash domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 F&SCM questions scoped to the Manage accounts receivable subdomain of order to cash (13 L3 processes), using D365 ERP plugin conventions against legal entity USMF.', 'example_request': 'Act as the D365 Manage accounts receivable expert and walk me through customer invoicing in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs guidance on D365 F&SCM accounts receivable processes within order to cash, using the D365 ERP plugin on the USMF legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365OrderToCashManageAccountsReceivable(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365OrderToCashManageAccountsReceivable'
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
    print(D365OrderToCashManageAccountsReceivable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
