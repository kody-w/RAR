---
name: "rar-cowork-cookbook-d365-hire-to-retire-manage-performance-and-growth"
description: "Scopes the conversation to Dynamics 365 F&SCM Hire-to-retire, Manage performance and growth (10 L3 processes), answering against legal entity USMF via the ERP plugin; call for guidance in that area."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth", "rar_sha256": "72278fcf35453f51085e2e055ef45cadb7d292299a598ddcc4bc24d71e91a778", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth`. The original RAPP
agent is preserved byte-for-byte in `d365_hire_to_retire_manage_performance_and_growth_agent.py` and in the RCI capsule.

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

D365 Manage performance and growth Expert — Scopes the conversation to Dynamics 365 F&SCM Hire-to-retire, Manage performance and growth (10 L3 processes), answering against legal entity USMF via the ERP plugin; call for guidance in that area.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire-manage-performance-and-growth
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_hire_to_retire_manage_performance_and_growth_agent.py` and embedded as the fenced Python below (sha256 72278fcf35453f51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_hire_to_retire_manage_performance_and_growth_agent.py` first:

```bash
python3 d365_hire_to_retire_manage_performance_and_growth_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_hire_to_retire_manage_performance_and_growth_agent.py   # or on stdin
python3 d365_hire_to_retire_manage_performance_and_growth_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage performance and growth Expert — Scopes the conversation to Dynamics 365 F&SCM Hire-to-retire, Manage performance and growth (10 L3 processes), answering against legal entity USMF via the ERP plugin; call for guidance in that area.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire-manage-performance-and-growth
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth',
    "version": '3.0.3',
    "display_name": 'D365 Manage performance and growth Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM Hire-to-retire, Manage performance and growth (10 L3 processes), answering against legal entity USMF via the ERP plugin; call for guidance in that area.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-hire-to-retire-manage-performance-and-growth',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-hire-to-retire-manage-performance-and-growth',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e1be97f64b5ce82c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'hire-to-retire/d365-hire-to-retire-manage-performance-and-growth', 'uses_skills': {'custom': ['d365-hire-to-retire-manage-performance-and-growth'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Manage performance and growth Expert** skill for this conversation. From now on, scope your help to the hire to retire domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM Hire-to-retire, Manage performance and growth (10 L3 processes), answering against legal entity USMF via the ERP plugin; call for guidance in that area.', 'example_request': 'Act as the D365 Manage performance and growth expert and walk me through this process in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'When a user needs D365 F&SCM help on performance management and growth processes within Hire to retire, using the ERP plugin against USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365HireToRetireManagePerformanceAndGrowth(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365HireToRetireManagePerformanceAndGrowth'
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
    print(D365HireToRetireManagePerformanceAndGrowth().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
