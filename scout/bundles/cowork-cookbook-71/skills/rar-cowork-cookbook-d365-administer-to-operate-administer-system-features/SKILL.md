---
name: "rar-cowork-cookbook-d365-administer-to-operate-administer-system-features"
description: "Answers Dynamics 365 F&SCM questions scoped to the Administer system features subdomain (20 L3 processes) against legal entity USMF, using documented entities, USMF conventions, and honest-degrade options."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_administer_to_operate_administer_system_features", "rar_sha256": "d2dc7e3043760406249e78635b724059c3c48f12c70249477e825c5ce30a5cee", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_administer_to_operate_administer_system_features`. The original RAPP
agent is preserved byte-for-byte in `d365_administer_to_operate_administer_system_features_agent.py` and in the RCI capsule.

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

D365 Administer system features Expert — Answers Dynamics 365 F&SCM questions scoped to the Administer system features subdomain (20 L3 processes) against legal entity USMF, using documented entities, USMF conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_administer_to_operate_administer_system_features_agent.py` and embedded as the fenced Python below (sha256 d2dc7e3043760406…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_administer_to_operate_administer_system_features_agent.py` first:

```bash
python3 d365_administer_to_operate_administer_system_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_administer_to_operate_administer_system_features_agent.py   # or on stdin
python3 d365_administer_to_operate_administer_system_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Administer system features Expert — Answers Dynamics 365 F&SCM questions scoped to the Administer system features subdomain (20 L3 processes) against legal entity USMF, using documented entities, USMF conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_administer_to_operate_administer_system_features',
    "version": '3.0.3',
    "display_name": 'D365 Administer system features Expert',
    "description": 'Answers Dynamics 365 F&SCM questions scoped to the Administer system features subdomain (20 L3 processes) against legal entity USMF, using documented entities, USMF conventions, and honest-degrade options.',
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
        "upstream_slug": 'd365-administer-to-operate-administer-system-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dcd4441c68528abb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-administer-to-operate-administer-system-features', 'uses_skills': {'custom': ['d365-administer-to-operate-administer-system-features'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Administer system features Expert** skill for this conversation. From now on, scope your help to the administer to operate domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 F&SCM questions scoped to the Administer system features subdomain (20 L3 processes) against legal entity USMF, using documented entities, USMF conventions, and honest-degrade options.', 'example_request': 'Act as the D365 Administer system features expert and walk me through this in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs D365 F&SCM guidance limited to the administer to operate domain, specifically administering system features against USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365AdministerToOperateAdministerSystemFeatures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AdministerToOperateAdministerSystemFeatures'
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
    print(D365AdministerToOperateAdministerSystemFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
