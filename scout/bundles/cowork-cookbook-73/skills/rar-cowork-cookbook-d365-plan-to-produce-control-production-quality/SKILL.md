---
name: "rar-cowork-cookbook-d365-plan-to-produce-control-production-quality"
description: "Scopes the conversation to Dynamics 365 F&SCM Control production quality (a level-2 subdomain of Plan to produce, 8 L3 processes), answering using documented entities, USMF conventions, and honest-degrade options. Call w"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_plan_to_produce_control_production_quality", "rar_sha256": "c715cf0a4df3613ee8aecedf1bcc25a06add1263598865e68f705e57f83ef1a3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_plan_to_produce_control_production_quality`. The original RAPP
agent is preserved byte-for-byte in `d365_plan_to_produce_control_production_quality_agent.py` and in the RCI capsule.

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

D365 Control production quality Expert — Scopes the conversation to Dynamics 365 F&SCM Control production quality (a level-2 subdomain of Plan to produce, 8 L3 processes), answering using documented entities, USMF conventions, and honest-degrade options. Call w

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce-control-production-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_plan_to_produce_control_production_quality_agent.py` and embedded as the fenced Python below (sha256 c715cf0a4df3613e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_plan_to_produce_control_production_quality_agent.py` first:

```bash
python3 d365_plan_to_produce_control_production_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_plan_to_produce_control_production_quality_agent.py   # or on stdin
python3 d365_plan_to_produce_control_production_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Control production quality Expert — Scopes the conversation to Dynamics 365 F&SCM Control production quality (a level-2 subdomain of Plan to produce, 8 L3 processes), answering using documented entities, USMF conventions, and honest-degrade options. Call w

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce-control-production-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_plan_to_produce_control_production_quality',
    "version": '3.0.3',
    "display_name": 'D365 Control production quality Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM Control production quality (a level-2 subdomain of Plan to produce, 8 L3 processes), answering using documented entities, USMF conventions, and honest-degrade options. Call w',
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
        "upstream_slug": 'd365-plan-to-produce-control-production-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-plan-to-produce-control-production-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a7f7d756b7fa015',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'plan-to-produce/d365-plan-to-produce-control-production-quality', 'uses_skills': {'custom': ['d365-plan-to-produce-control-production-quality'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Control production quality Expert** skill for this conversation. From now on, scope your help to the plan to produce domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM Control production quality (a level-2 subdomain of Plan to produce, 8 L3 processes), answering using documented entities, USMF conventions, and honest-degrade options. Call w', 'example_request': 'Act as the D365 Control production quality expert and help me with quality orders in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user needs D365 F&SCM guidance limited to Control production quality within Plan to produce, against the USMF legal entity via the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365PlanToProduceControlProductionQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365PlanToProduceControlProductionQuality'
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
    print(D365PlanToProduceControlProductionQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
