---
name: "rar-cowork-cookbook-d365-service-to-deliver-develop-service-strategy"
description: "Scopes the conversation to Dynamics 365 F&SCM 'Develop service strategy' (10 L3 processes under Service to deliver), answering using that area's entities, USMF legal-entity conventions, and documented honest-degrade opti"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_service_to_deliver_develop_service_strategy", "rar_sha256": "16777628a83848f4384c6bb662adda4594aa078df168fec009c009cced73d08a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_service_to_deliver_develop_service_strategy`. The original RAPP
agent is preserved byte-for-byte in `d365_service_to_deliver_develop_service_strategy_agent.py` and in the RCI capsule.

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

D365 Develop service strategy Expert — Scopes the conversation to Dynamics 365 F&SCM 'Develop service strategy' (10 L3 processes under Service to deliver), answering using that area's entities, USMF legal-entity conventions, and documented honest-degrade opti

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver-develop-service-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_service_to_deliver_develop_service_strategy_agent.py` and embedded as the fenced Python below (sha256 16777628a83848f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_service_to_deliver_develop_service_strategy_agent.py` first:

```bash
python3 d365_service_to_deliver_develop_service_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_service_to_deliver_develop_service_strategy_agent.py   # or on stdin
python3 d365_service_to_deliver_develop_service_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Develop service strategy Expert — Scopes the conversation to Dynamics 365 F&SCM 'Develop service strategy' (10 L3 processes under Service to deliver), answering using that area's entities, USMF legal-entity conventions, and documented honest-degrade opti

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver-develop-service-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_service_to_deliver_develop_service_strategy',
    "version": '3.0.3',
    "display_name": 'D365 Develop service strategy Expert',
    "description": "Scopes the conversation to Dynamics 365 F&SCM 'Develop service strategy' (10 L3 processes under Service to deliver), answering using that area's entities, USMF legal-entity conventions, and documented honest-degrade opti",
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
        "upstream_slug": 'd365-service-to-deliver-develop-service-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-service-to-deliver-develop-service-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a7e17010c613b1d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'service-to-deliver/d365-service-to-deliver-develop-service-strategy', 'uses_skills': {'custom': ['d365-service-to-deliver-develop-service-strategy'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Develop service strategy Expert** skill for this conversation. From now on, scope your help to the service to deliver domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Scopes the conversation to Dynamics 365 F&SCM 'Develop service strategy' (10 L3 processes under Service to deliver), answering using that area's entities, USMF legal-entity conventions, and documented honest-degrade opti", 'example_request': 'Act as the D365 Develop service strategy expert and help me set up our service strategy processes in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants D365 F&SCM guidance limited to the Develop service strategy subdomain of Service to deliver, working against the USMF tenant.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ServiceToDeliverDevelopServiceStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ServiceToDeliverDevelopServiceStrategy'
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
    print(D365ServiceToDeliverDevelopServiceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
