---
name: "rar-cowork-cookbook-d365-project-to-profit-manage-project-delivery"
description: "Scopes the conversation to a Dynamics 365 F&SCM Manage project delivery expert (11 L3 processes under Project to profit), answering against legal entity USMF via the D365 ERP plugin. Call for project delivery questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_project_to_profit_manage_project_delivery", "rar_sha256": "c377831220674567bd495927bcad481e5d6f0a9d153c64a08ad1ec37492e1141", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_project_to_profit_manage_project_delivery`. The original RAPP
agent is preserved byte-for-byte in `d365_project_to_profit_manage_project_delivery_agent.py` and in the RCI capsule.

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

D365 Manage project delivery Expert — Scopes the conversation to a Dynamics 365 F&SCM Manage project delivery expert (11 L3 processes under Project to profit), answering against legal entity USMF via the D365 ERP plugin. Call for project delivery questions.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit-manage-project-delivery
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_project_to_profit_manage_project_delivery_agent.py` and embedded as the fenced Python below (sha256 c377831220674567…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_project_to_profit_manage_project_delivery_agent.py` first:

```bash
python3 d365_project_to_profit_manage_project_delivery_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_project_to_profit_manage_project_delivery_agent.py   # or on stdin
python3 d365_project_to_profit_manage_project_delivery_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage project delivery Expert — Scopes the conversation to a Dynamics 365 F&SCM Manage project delivery expert (11 L3 processes under Project to profit), answering against legal entity USMF via the D365 ERP plugin. Call for project delivery questions.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit-manage-project-delivery
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_project_to_profit_manage_project_delivery',
    "version": '3.0.3',
    "display_name": 'D365 Manage project delivery Expert',
    "description": 'Scopes the conversation to a Dynamics 365 F&SCM Manage project delivery expert (11 L3 processes under Project to profit), answering against legal entity USMF via the D365 ERP plugin. Call for project delivery questions.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-project-to-profit-manage-project-delivery',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-project-to-profit-manage-project-delivery',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '021d741b0818292c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'project-to-profit/d365-project-to-profit-manage-project-delivery', 'uses_skills': {'custom': ['d365-project-to-profit-manage-project-delivery'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Manage project delivery Expert** skill for this conversation. From now on, scope your help to the project to profit domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to a Dynamics 365 F&SCM Manage project delivery expert (11 L3 processes under Project to profit), answering against legal entity USMF via the D365 ERP plugin. Call for project delivery questions.', 'example_request': 'Act as the D365 Manage project delivery expert and help me with project delivery in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when the user needs Dynamics 365 F&SCM guidance limited to the Manage project delivery subdomain of Project to profit, using USMF conventions.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ProjectToProfitManageProjectDelivery(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProjectToProfitManageProjectDelivery'
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
    print(D365ProjectToProfitManageProjectDelivery().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
