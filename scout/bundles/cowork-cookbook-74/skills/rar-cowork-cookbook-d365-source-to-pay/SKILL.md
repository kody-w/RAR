---
name: "rar-cowork-cookbook-d365-source-to-pay"
description: "Scopes the assistant to Dynamics 365 F&SCM source-to-pay work (6 L2 areas, 42 L3 processes) using the D365 ERP plugin against legal entity USMF; call it for procurement, vendor, and payables questions in D365."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_source_to_pay", "rar_sha256": "b3f9b1bf4376da2358ec875be03292f75b993eccd154b02f290c95556b87f831", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_source_to_pay`. The original RAPP
agent is preserved byte-for-byte in `d365_source_to_pay_agent.py` and in the RCI capsule.

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

D365 Source to pay Expert — Scopes the assistant to Dynamics 365 F&SCM source-to-pay work (6 L2 areas, 42 L3 processes) using the D365 ERP plugin against legal entity USMF; call it for procurement, vendor, and payables questions in D365.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-source-to-pay
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_source_to_pay_agent.py` and embedded as the fenced Python below (sha256 b3f9b1bf4376da23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_source_to_pay_agent.py` first:

```bash
python3 d365_source_to_pay_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_source_to_pay_agent.py   # or on stdin
python3 d365_source_to_pay_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Source to pay Expert — Scopes the assistant to Dynamics 365 F&SCM source-to-pay work (6 L2 areas, 42 L3 processes) using the D365 ERP plugin against legal entity USMF; call it for procurement, vendor, and payables questions in D365.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-source-to-pay
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_source_to_pay',
    "version": '3.0.3',
    "display_name": 'D365 Source to pay Expert',
    "description": 'Scopes the assistant to Dynamics 365 F&SCM source-to-pay work (6 L2 areas, 42 L3 processes) using the D365 ERP plugin against legal entity USMF; call it for procurement, vendor, and payables questions in D365.',
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
        "upstream_slug": 'd365-source-to-pay',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-source-to-pay',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '63f13e34b79b0347',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'source-to-pay/d365-source-to-pay', 'uses_skills': {'custom': ['d365-source-to-pay'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Source to pay Expert** skill for this conversation. From now on, scope your help to the source to pay domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the assistant to Dynamics 365 F&SCM source-to-pay work (6 L2 areas, 42 L3 processes) using the D365 ERP plugin against legal entity USMF; call it for procurement, vendor, and payables questions in D365.', 'example_request': 'Act as the D365 source to pay expert and walk me through the purchase requisition to payment process in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when working in Dynamics 365 Finance & Supply Chain Management on source-to-pay topics such as sourcing, purchasing, vendors, invoices, and payables.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365SourceToPay(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365SourceToPay'
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
    print(D365SourceToPay().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
