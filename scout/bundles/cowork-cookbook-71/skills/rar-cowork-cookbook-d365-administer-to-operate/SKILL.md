---
name: "rar-cowork-cookbook-d365-administer-to-operate"
description: "Scopes the conversation to Dynamics 365 F&SCM 'Administer to operate' (13 L2 areas, 132 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for administer-to-operate questions"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_administer_to_operate", "rar_sha256": "ea3bad01087385afcb86a0a477aab19f62fe059348a8e7dfe9e1b2a4c5c62d8c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_administer_to_operate`. The original RAPP
agent is preserved byte-for-byte in `d365_administer_to_operate_agent.py` and in the RCI capsule.

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

D365 Administer to operate Expert — Scopes the conversation to Dynamics 365 F&SCM 'Administer to operate' (13 L2 areas, 132 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for administer-to-operate questions

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_administer_to_operate_agent.py` and embedded as the fenced Python below (sha256 ea3bad01087385af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_administer_to_operate_agent.py` first:

```bash
python3 d365_administer_to_operate_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_administer_to_operate_agent.py   # or on stdin
python3 d365_administer_to_operate_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Administer to operate Expert — Scopes the conversation to Dynamics 365 F&SCM 'Administer to operate' (13 L2 areas, 132 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for administer-to-operate questions

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_administer_to_operate',
    "version": '3.0.3',
    "display_name": 'D365 Administer to operate Expert',
    "description": "Scopes the conversation to Dynamics 365 F&SCM 'Administer to operate' (13 L2 areas, 132 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for administer-to-operate questions",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-administer-to-operate',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-administer-to-operate',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f9b266fd9ee417c3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-administer-to-operate', 'uses_skills': {'custom': ['d365-administer-to-operate'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Administer to operate Expert** skill for this conversation. From now on, scope your help to the administer to operate domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Scopes the conversation to Dynamics 365 F&SCM 'Administer to operate' (13 L2 areas, 132 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for administer-to-operate questions", 'example_request': 'Act as the D365 Administer to operate expert and help me with an administer-to-operate process in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when working in Dynamics 365 Finance & Supply Chain Management on administer-to-operate processes via the Cowork D365 ERP plugin against USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365AdministerToOperate(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AdministerToOperate'
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
    print(D365AdministerToOperate().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
