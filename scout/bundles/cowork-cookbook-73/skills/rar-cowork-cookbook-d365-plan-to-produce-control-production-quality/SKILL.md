---
name: "rar-cowork-cookbook-d365-plan-to-produce-control-production-quality"
description: "Scopes the conversation to Dynamics 365 F&SCM Control production quality (a level-2 subdomain of Plan to produce, 8 L3 processes), answering using documented entities, USMF conventions, and honest-degrade options. Call w"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_plan_to_produce_control_production_quality", "rar_sha256": "c715cf0a4df3613ee8aecedf1bcc25a06add1263598865e68f705e57f83ef1a3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
