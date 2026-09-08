---
name: "rar-cowork-cookbook-d365-acquire-to-dispose"
description: "Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Acquire to dispose process (6 L2 areas, 43 L3 processes), using the D365 ERP plugin against legal entity USMF."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_acquire_to_dispose", "rar_sha256": "60a84f1ab4eb989902dfff8b7fedc829758c7803b07d8d5e6dbf7db92d7756d9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_acquire_to_dispose`. The original RAPP
agent is preserved byte-for-byte in `d365_acquire_to_dispose_agent.py` and in the RCI capsule.

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

D365 Acquire to dispose Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Acquire to dispose process (6 L2 areas, 43 L3 processes), using the D365 ERP plugin against legal entity USMF.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_acquire_to_dispose_agent.py` and embedded as the fenced Python below (sha256 60a84f1ab4eb9899…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_acquire_to_dispose_agent.py` first:

```bash
python3 d365_acquire_to_dispose_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_acquire_to_dispose_agent.py   # or on stdin
python3 d365_acquire_to_dispose_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Acquire to dispose Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Acquire to dispose process (6 L2 areas, 43 L3 processes), using the D365 ERP plugin against legal entity USMF.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_acquire_to_dispose',
    "version": '3.0.3',
    "display_name": 'D365 Acquire to dispose Expert',
    "description": 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Acquire to dispose process (6 L2 areas, 43 L3 processes), using the D365 ERP plugin against legal entity USMF.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-acquire-to-dispose',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-acquire-to-dispose',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '79d4cca7c8aece60',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'acquire-to-dispose/d365-acquire-to-dispose', 'uses_skills': {'custom': ['d365-acquire-to-dispose'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Acquire to dispose Expert** skill for this conversation. From now on, scope your help to the acquire to dispose domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Acquire to dispose process (6 L2 areas, 43 L3 processes), using the D365 ERP plugin against legal entity USMF.', 'example_request': 'Walk me through the acquire to dispose process for fixed asset acquisition in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs guidance on D365 F&SCM acquire-to-dispose processes, entities, or USMF conventions via the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365AcquireToDispose(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AcquireToDispose'
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
    print(D365AcquireToDispose().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
