---
name: "rar-cowork-cookbook-d365-source-to-pay"
description: "Scopes the assistant to Dynamics 365 F&SCM source-to-pay work (6 L2 areas, 42 L3 processes) using the D365 ERP plugin against legal entity USMF; call it for procurement, vendor, and payables questions in D365."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_source_to_pay", "rar_sha256": "b3f9b1bf4376da2358ec875be03292f75b993eccd154b02f290c95556b87f831", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
