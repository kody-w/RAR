---
name: "rar-cowork-cookbook-d365-service-to-deliver"
description: "Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Service to deliver process (5 L2 areas, 37 L3 processes), using the D365 ERP plugin against legal entity USMF."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_service_to_deliver", "rar_sha256": "c57a2364c2dbfdc68a1cdeb4d9576ab1be4ac63b666876fade8a719c4c65ada5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_service_to_deliver`. The original RAPP
agent is preserved byte-for-byte in `d365_service_to_deliver_agent.py` and in the RCI capsule.

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

D365 Service to deliver Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Service to deliver process (5 L2 areas, 37 L3 processes), using the D365 ERP plugin against legal entity USMF.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_service_to_deliver_agent.py` and embedded as the fenced Python below (sha256 c57a2364c2dbfdc6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_service_to_deliver_agent.py` first:

```bash
python3 d365_service_to_deliver_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_service_to_deliver_agent.py   # or on stdin
python3 d365_service_to_deliver_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Service to deliver Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Service to deliver process (5 L2 areas, 37 L3 processes), using the D365 ERP plugin against legal entity USMF.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_service_to_deliver',
    "version": '3.0.3',
    "display_name": 'D365 Service to deliver Expert',
    "description": 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Service to deliver process (5 L2 areas, 37 L3 processes), using the D365 ERP plugin against legal entity USMF.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-service-to-deliver',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-service-to-deliver',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d64e3b12bcd55b5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'service-to-deliver/d365-service-to-deliver', 'uses_skills': {'custom': ['d365-service-to-deliver'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Service to deliver Expert** skill for this conversation. From now on, scope your help to the service to deliver domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Service to deliver process (5 L2 areas, 37 L3 processes), using the D365 ERP plugin against legal entity USMF.', 'example_request': 'Act as the D365 Service to deliver expert and walk me through this service order process in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs D365 F&SCM guidance limited to the Service to deliver end-to-end process, with USMF tenant conventions and honest-degrade options.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ServiceToDeliver(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ServiceToDeliver'
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
    print(D365ServiceToDeliver().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
