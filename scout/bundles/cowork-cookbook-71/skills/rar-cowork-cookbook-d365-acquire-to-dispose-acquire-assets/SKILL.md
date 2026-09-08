---
name: "rar-cowork-cookbook-d365-acquire-to-dispose-acquire-assets"
description: "Answers Dynamics 365 F&SCM questions scoped to the Acquire assets subdomain of acquire to dispose (12 L3 processes), using documented entities, USMF legal entity conventions, and honest-degrade options; call it for fixed"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_acquire_to_dispose_acquire_assets", "rar_sha256": "33e19674ea73aefa8bab762a60634bbae14d9e9e6de0a4f0c117d256e2ad2c36", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_acquire_to_dispose_acquire_assets`. The original RAPP
agent is preserved byte-for-byte in `d365_acquire_to_dispose_acquire_assets_agent.py` and in the RCI capsule.

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

D365 Acquire assets Expert — Answers Dynamics 365 F&SCM questions scoped to the Acquire assets subdomain of acquire to dispose (12 L3 processes), using documented entities, USMF legal entity conventions, and honest-degrade options; call it for fixed

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_acquire_to_dispose_acquire_assets_agent.py` and embedded as the fenced Python below (sha256 33e19674ea73aefa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_acquire_to_dispose_acquire_assets_agent.py` first:

```bash
python3 d365_acquire_to_dispose_acquire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_acquire_to_dispose_acquire_assets_agent.py   # or on stdin
python3 d365_acquire_to_dispose_acquire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Acquire assets Expert — Answers Dynamics 365 F&SCM questions scoped to the Acquire assets subdomain of acquire to dispose (12 L3 processes), using documented entities, USMF legal entity conventions, and honest-degrade options; call it for fixed

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_acquire_to_dispose_acquire_assets',
    "version": '3.0.3',
    "display_name": 'D365 Acquire assets Expert',
    "description": 'Answers Dynamics 365 F&SCM questions scoped to the Acquire assets subdomain of acquire to dispose (12 L3 processes), using documented entities, USMF legal entity conventions, and honest-degrade options; call it for fixed',
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
        "upstream_slug": 'd365-acquire-to-dispose-acquire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '63374b5cb6933e93',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'acquire-to-dispose/d365-acquire-to-dispose-acquire-assets', 'uses_skills': {'custom': ['d365-acquire-to-dispose-acquire-assets'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Acquire assets Expert** skill for this conversation. From now on, scope your help to the acquire to dispose domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 F&SCM questions scoped to the Acquire assets subdomain of acquire to dispose (12 L3 processes), using documented entities, USMF legal entity conventions, and honest-degrade options; call it for fixed', 'example_request': 'Act as the D365 Acquire assets expert and walk me through acquiring a fixed asset in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user needs D365 F&SCM guidance on acquiring assets within the acquire to dispose domain, against the USMF legal entity via the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365AcquireToDisposeAcquireAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AcquireToDisposeAcquireAssets'
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
    print(D365AcquireToDisposeAcquireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
