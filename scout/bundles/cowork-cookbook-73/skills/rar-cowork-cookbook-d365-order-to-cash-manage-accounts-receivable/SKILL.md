---
name: "rar-cowork-cookbook-d365-order-to-cash-manage-accounts-receivable"
description: "Answers Dynamics 365 F&SCM questions scoped to the Manage accounts receivable subdomain of order to cash (13 L3 processes), using D365 ERP plugin conventions against legal entity USMF."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_order_to_cash_manage_accounts_receivable", "rar_sha256": "85fac6e1303caeabd141c3f142e0171b4db42e59a7925f0f6216a84d9f409a74", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
