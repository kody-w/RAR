---
name: "rar-cowork-cookbook-d365-administer-to-operate"
description: "Scopes the conversation to Dynamics 365 F&SCM 'Administer to operate' (13 L2 areas, 132 L3 processes), answering using that domain's entities and USMF legal-entity conventions; call it for administer-to-operate questions"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_administer_to_operate", "rar_sha256": "ea3bad01087385afcb86a0a477aab19f62fe059348a8e7dfe9e1b2a4c5c62d8c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
