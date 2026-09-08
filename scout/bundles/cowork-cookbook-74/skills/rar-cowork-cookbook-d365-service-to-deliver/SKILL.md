---
name: "rar-cowork-cookbook-d365-service-to-deliver"
description: "Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Service to deliver process (5 L2 areas, 37 L3 processes), using the D365 ERP plugin against legal entity USMF."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_service_to_deliver", "rar_sha256": "c57a2364c2dbfdc68a1cdeb4d9576ab1be4ac63b666876fade8a719c4c65ada5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
