---
name: "rar-cowork-cookbook-d365-plan-to-produce"
description: "Scopes the conversation to Dynamics 365 F&SCM Plan to produce (5 L2 areas, 30 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_plan_to_produce", "rar_sha256": "62fd7b4d6731679d1ad1aab84483b19b210170b33832937703fb0b42895b718d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_plan_to_produce`. The original RAPP
agent is preserved byte-for-byte in `d365_plan_to_produce_agent.py` and in the RCI capsule.

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

D365 Plan to produce Expert — Scopes the conversation to Dynamics 365 F&SCM Plan to produce (5 L2 areas, 30 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_plan_to_produce_agent.py` and embedded as the fenced Python below (sha256 62fd7b4d6731679d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_plan_to_produce_agent.py` first:

```bash
python3 d365_plan_to_produce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_plan_to_produce_agent.py   # or on stdin
python3 d365_plan_to_produce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Plan to produce Expert — Scopes the conversation to Dynamics 365 F&SCM Plan to produce (5 L2 areas, 30 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_plan_to_produce',
    "version": '3.0.3',
    "display_name": 'D365 Plan to produce Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM Plan to produce (5 L2 areas, 30 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-plan-to-produce',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-plan-to-produce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '286961260ee3ad34',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'plan-to-produce/d365-plan-to-produce', 'uses_skills': {'custom': ['d365-plan-to-produce'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Plan to produce Expert** skill for this conversation. From now on, scope your help to the plan to produce domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM Plan to produce (5 L2 areas, 30 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.', 'example_request': 'Act as the D365 Plan to produce expert and walk me through production order scheduling in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants D365 Finance & Supply Chain help limited to the Plan to produce end-to-end process, working against the USMF legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365PlanToProduce(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365PlanToProduce'
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
    print(D365PlanToProduce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
