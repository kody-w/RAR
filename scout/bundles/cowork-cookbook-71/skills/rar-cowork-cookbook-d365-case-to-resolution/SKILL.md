---
name: "rar-cowork-cookbook-d365-case-to-resolution"
description: "Scopes the conversation to Dynamics 365 F&SCM Case to resolution (5 L2 areas, 37 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_case_to_resolution", "rar_sha256": "dda3a961023f6dcfb506a3a20d115aad81ae660976a24d67c95786840036f072", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_case_to_resolution`. The original RAPP
agent is preserved byte-for-byte in `d365_case_to_resolution_agent.py` and in the RCI capsule.

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

D365 Case to resolution Expert — Scopes the conversation to Dynamics 365 F&SCM Case to resolution (5 L2 areas, 37 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_case_to_resolution_agent.py` and embedded as the fenced Python below (sha256 dda3a961023f6dcf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_case_to_resolution_agent.py` first:

```bash
python3 d365_case_to_resolution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_case_to_resolution_agent.py   # or on stdin
python3 d365_case_to_resolution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Case to resolution Expert — Scopes the conversation to Dynamics 365 F&SCM Case to resolution (5 L2 areas, 37 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_case_to_resolution',
    "version": '3.0.3',
    "display_name": 'D365 Case to resolution Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM Case to resolution (5 L2 areas, 37 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-case-to-resolution',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-case-to-resolution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16cca54576658a8e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'case-to-resolution/d365-case-to-resolution', 'uses_skills': {'custom': ['d365-case-to-resolution'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Case to resolution Expert** skill for this conversation. From now on, scope your help to the case to resolution domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM Case to resolution (5 L2 areas, 37 L3 processes), answering using documented entities, USMF legal entity conventions, and honest-degrade options.', 'example_request': 'Act as the D365 Case to resolution expert and walk me through resolving a case in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants D365 Finance & Supply Chain help scoped to the Case to resolution end-to-end process against the USMF tenant.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365CaseToResolution(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365CaseToResolution'
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
    print(D365CaseToResolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6ebOb1pbvV9E7XdVxGtsgZtx1qx4IgUAgMUkIxSkHMUtMYoZ0vntvJNlO7k369q16/zy5fA7D3mtev7XW2fr1zW2buKjePr2ZgZsvRDdNkzioFm7uL1ZFX1Q38Ku4XcD/hVfkTZVc2qao6rf3b35Qe1VSNkmRz9u9ogzqRRMH87ouqGp3frNoigU/5m6WePUCI4mF8O/mSl2s3DqYX1VBXaTtY+E7YqGgC7cK3Pr9AqMWCrYoq8IL6jqof3wPBKr7oEryaNHW80+/8NosyJvAX4CfSZMEYNvBVIVFGkRu+nw4PmXJZwb1+4dScZEHdfPBD6LK9YNF8ZC//gj0CQY3K9Ogfvv008/v3xJw/fbp1zcvdWvw6I0Hws9SW4XxTWawKXXzCLwtR2DF+b4MqrCoMvDID8LF6+5dHaTh+8V//Metd6uo/vHT53zx+nx+m/8Zbf6wXFO49ayR55buJUmBAh8XbNq7Yw0s1bRVXi/cRd3MZvj43PmdUlEu/ja/e/dk8jEKmnef34BTqocjPr/9uCgqwK9q5+uPM5Xy3Y8f0wKY9d2P3+nU7eUaeM1MDEj98cvr/kUWLPy+NAkXX0xtvXrxqgIvKQNA/Hf6zZ+n6C9yL5N8eS5+V5TvF39Oedbnb0DeZ5hdAN0/JwtsAHa+fbwWSf7uxaMqgNPd3Ave/fhXZL048G5pUjf/K7o/PQnHAYiZ6t3LJCAqZxf8vIBeun2j+ddsSxAw/4omYPlXdt8M9Ve0H579O9JpAsL9my//lNyfbYD+tvjpL3X7nza8X4Sf3/ggTQACuJc0+LT49REiP/3gf3/4w8+/AdL/lIxZtJX3oPAlc/MkBHn75ctPP9SPxz/8/NMPbQmiOHCzL22V/hnNP7Prg88fLPha9e6PewH/Q37Liz5ffMuhxa9F+X+q3z4ujm6a+N+f158Wv8/E+QMtZiW+Mn2a4HfZWANZf2fHH99+A4iTA21a7/Ea4Me//dtCTbyqqIuwWQB0bZsFcHCTZMEsvBUn9SJ54m0VzHCbAMO+1oH4nz08S1yEi1/+r/cA8g/eC8hhH2DZFw+A2Zem+PIdgn/5uLAAuaJKoiQHEGqwmvY5dyOAnzOrEqwMqg7A02Vsgg8giz/MF4skX/zyFxS/PDZ/LMdfHtibPFHOWEkzwtVtGnycdbHjIH9J7oEaFAyB1wK6aeEBIcIknZH9QbMDCDnrXd+SNF34CcAQUIvGB21gm08zsV9++eXi1vHn/AnJ2OJZpGoYLPgmzuLDB6BNmCZR3HzOAy8uFj/8+tsPi/9a/E+7HsRnHhooCS/LAwllc78DdSt6lCPgFOBGABMPy//628umgEwOqirwUxImrzIJIvEW+F8NbG7YDyhBLi4BMCwwalYWVTMXuqT5uJDCxTd5AdP51VwJ4qJuFn5QBrkf5N4IqLpAnW+WzItmMVfhOhzfg6oZPLj+cqnch4gZSGm3+WWhrjRQd4r0UY5fdQhsLvIEmP+b+5/PAZHqh3rBfSXxcbGbY29RupVbxpX74hG6T7+AevN1OyDuLvKg/5zPhTWYTfVIhKd5wCJgGe/l0g+zz0HlzkDW+/VX3o817lwdrUeVrD7n9SvIQdMArOIB0AdMozbxZ+j/z1dI1XHRpv7DfkDSmdLLC/7LK48YnMv7n3Ul6wGkbLP43KLIEl/8f97kzIqyomisRdZa84v1zjKcpwPm1m521LMbnGmCKHwm2/de5CvefIXdz3magGiqxv98rny47bXmCWVtBSQ3WONBH8QMcMBM9xHSc4hW1ZwM7uf8K74D8RcPMAO2AvkP8mM24FeG89uvksYgyef777X+EQKVPxsAhO2ibC8pCKkwCPyL692AVNWcli9PgvgO5hTt48SL/6DVbFQQRoD+AgiRgEQDNeDjN8x9vv0q+h82Pluaecuj3WtBVlYPAkCOYBZwdk2fNACc3ObZSQM9Pz2IADWyspl1v4CQApo+HwZVcG+TOmlmxz/tGpQAdj/Mv5+azk8DEKXeHCUg4MsWWPeRInMEZbP/kxklQMZkSQ4KODDKywgPgm425zvA01eH+aT4ePxSKHjk1Vx5vm6cFZn3zMV8EQLRwZPx97Bg/VmYAHrZvOLB9+8j7Ru3mfYMjTWIYsDx69tn1f/4LNzPzmDxle6nfxhV3v1r08yjFB/+GACfFnHTlPUnGH6Wz6/V8yMAJvgpa/2opB/muvehKT58z/M/kHtq+mnxr4n0BxKvlPi0WH5EPiLzK+UVUq8PsMDqA+d8wOe3n3Mj+I6WgH2RgZia/TWC0v2ttH1dAupbVAE4AYufpa6eK2QPivID24HxP+e/j/E5x0DpyKM5Juvid7n/qPEg3p+++laCwKu8Abz9uf+LgnnWemREHbx9yts0ff8GoDP46xlrri7ZHL/1PJCBTJkhOQkedw84GJr58o/z6P5x4aYfF3wAoCetfx9jr5ow18TfpcJTN6DTjPLvFz6wSD3XMKDbzHxOI7cGcQlCctahGctZ6Oc4Njdw37q7f5TGBqV2RjK/+DRXnfevfAe/QUf+fvGtuQZcX+POYyLNWzBJ/jQ39rMZHlvmC7AH/Pq26dssfgnefv4HuYBgDxABUDzT+i7k96XFYyCYVQCkm+f8+usbMLkLbOC+jP7qKMFykHMf6rm2wiAcAXNw/wwc8O5/22u+ttWxC5qeeVr2XcxlyCWCYiHpe+GFQEjwBEX85ZJwXZ9eugFJIgxFuijuk5THEBRN0jiCYGSIUCig94y6L3PfkMyiEAwVIgyDhvgSkAHjONjogz2kR1Ao4jIXl7gQjHv5vvWW5P5Lv6c+s/G+tb2zHV5q/vp2IXGwcoPXEvv8rGBmeYFt6mLECnxCoGHod/tDUhmur9xW7XF09xKuO6ubwFxbwTlUtHC5mZks3PQepthEjE6tFNAydeu6HSXL3qG0mnJ11U8l76xzH/NzBwonTQFkpkA74aSxG5SNmiY347a9QUkdJZYtD7SZHu1EgyFogpNpzZip0ySVY4aD7N3H8aj1jnxql3GrT/TJ2J+WJ5rcY3BoiFfEoAZczszsbNHWtcNL7IrYrnyhth5hazKiiND5tO3zKB3LAeKKNLykR+++5qPzMlmv6gbabzrYvhl32dQYb+sTiZ3xuRitnRJbbxMoi45lqqZsYp5ydaMPQbdJp6BTsiHM5S22GeEwLy0SBw7zylqgpDqNcvEoeHKc7sXgskrJ1Iu5NbOCT9w46V2vMehashVLdKkzViVqMRx2+sEyK7pQKY6B2u1h9Or+GGcWrzenbrVk92rTb1brjT1kG5NilWVky+leP8ghLt5HkXavtVuFsTdiww4b12QudGJXbFXY1BVSY3ltRZ8OQaKUR4XTu+JCs/qWtes+zox1HRsnkuHChib4vh5QQ2jZ6MKzFVk70rXNESgbkja01bb3yqKw72JErO2Dd5fGU9QfhUoWVlUtJ9qZE27OQdkV+hnpeRilzEgfmciYkiS8RyNzWas0BUjbDXHPTRJdY+VugIxNcnfKA2TfzoZg37YFgefqitq6SnCjlbUZrcpj00/XtUMw2kRbNyG+nw66tS9cFd8whjYd1wdxV8jq1sDXoaDR0GElpuTqbE3n5Oydj+xdbJr7uk0dzk5btxcalALdbHKIN85lkp3LxqmManeblEmw9W7gUljgTsfMivdVKdfREpbPhQA7OQiy1RRECtPz3toaAvygxrUdykrqMDxduNiQHaOTca60a0HQpza5+C4ZXiQaKeDUYJUggHK+cM+CKuIBeg9Sa6qtXLUNS9058HoJUTyDbsRNmlvqle6DTCtHBs5yku89sbSTHE9XutXvLrKQnNduc5eHA3ULYzczTsTBCjc3tzzEZ5EdtVbx2nPX4qzuDHfnxkhCg+yNLZxW4pZSWE1Z07lE8MN9eeSUVsJJXd87l4RN643kJU3BFxv2dIqC87ELCAJX7vjGZ6OcYYKet70sX48ZebbOe28r584tMIbhKHJLqGQOQxVa3L7jJG5JGoGE7GPQzt0MvAn1idBcMuBQMTByJT+ejO4Ka8vt/Zi6qyvUmzvYN8umwMZoohTTzZH4OKX2qZ/4/SqOlantEEdylCLGcjWaZHKX7+szAZmuKnX3QJf0cxjEVslyfpLe7itRvC9Pnlcaxf667Rk1so+ltyccb9rAgm1SQVwsy7tLO1BarqxMP3N0KEb9SXLud9UhCEk6WrR98lWOuOhuqd9MLTQTNr924c1fB4qtB1Bztza8tpwgmc8dwqNNyLpTfRRz6hHGFayX21FYFS0TqxK8R87BuKPHgb9EsbsJxxY7F5ji4GEpSNTtgnBuXIpZa1757ZZHhIBDYrujr0fkOIkdjGBnPe5VWqOZ7c7ORWbTd+VWiIc+2ECwem+gu2PRsKoWTYEnmLFMCYAjoVJgskD25Brf4UsfZZYGynelXQqiROlMYu2ZKrMNzr4FtMuMHY8SDoFYTnEzdLRC9aR1i1gK3Go66zbrsN1mgJTU6reXRBAhI41jgXA5TsajerWua35jb61eRqVr0E1LbGf2k7s+y9Jq3VwzoVXV7LZCVCloDbXEVcrtzLEhMXnD6RJ76AuTEKlk2yN3lk2u3ghN6IrwDLbsdHVV0Uq57PM0Oyitm/rDxjFZ82rotM+ZtH6n0r6xLw6lN9etQQUJXob3q3HW62uUnDfKkgqwaYT9m2ycj2qp5/sk5Ifz0ZSNZA3LJ3HEXE13sDun7A1j58OM7ARL7BijiIR7F3HQwiMNQcFFPhE0FIbbBhacczttFZDSNk2XGnesdTb2b+aA7y8ppWwF76DVWqp2lnLfRbsz3A67Yuu6XYf03CnTNhVO7nMEP2tlgTLFUDm1yocYyeo2auiB2CnI9kpoo1sXWlurupqz4yAV/voqF3ToE815bV632OSrKL48xDnsNjVenLeYU0IOJmspfERdHyWOuu0S976jT3Ei8am5c8jUEPkloobeDUKnfRsfPb3nK9zx0u1w3hwH7axD1igSussGh5sVkZ7Z8tiKckU6w2PHlE4bUr3clSEeDhavIHt7R9JKkpR7dbkPt9mYr9aMJKariF9efOKkGQeTZOHoUPV7FRSfzeimYVhek/N9tS0i2azY+zAut9yKj8Zzklh3Its3XUwxR1eIWNIwDsUx2ZybXpD7Voj1NTwcb+Z41dBloQe8Va5Y5Mqu5CtSjQmnDoIouDhZBAmtxBznQ0TqMvbdN7hRwaWL0wt8clgf9DmQBOS+2ow3WxCnM1eP57tdDf2JhqqDwQPrL80LtOy4COt0BjT1Ui2ulnYnFvbKmzyedfi1jA12uqzdS9xKOm5cGvW2pQ0l6MxVHk0HeUnHdMVo0VU2sTEEuWgNzMpSDhLdyy4qnWux5q8BZ0eVphNr6cpTpmwOKSPljhSjhuWglzY0N2UVISy+CsIW0Y5RPRThXdLR/Ho/yhyydJ1k66p6sBkx05H9Zl9Jg9uXpJ9DTdIGKwGYnWFBc29T5KSSvb5Eb5Dq6MMWa7INuFQMhMGIGooIqRpcY3u9Z3kX+T1B7B12OhZ5ZKYXB6TysL2t9KDodJluzdtGUMTlWemte29UXLAszcbkHWKHcB4iHJGUy9jN+cjxeznT2amwEF/kGWc85fYR56R83JZWnXqRG/aqxGmJkN7UTZIsQRB0kqkUhGbxiLThjdHPAWyq7Dm0JXcdO7eBXXHb7eqeJAWcrdc9USENdYv5K4tI5l5BO1H2xs2edQ6eZ1htAeb2irVajzey+M4N2OosTIq0lhBc3LImZQpInfLnXK6KSt5Ho8mEGM9I4+7U7ZRibHGIFcVDpNYSmR8nQ9wNEufdmdFJCrHPi1Udebs4tlLkmNnMiJSMwl5ik0fRyh0bJhLOyyGcjo0vptd1ZVNyRh+VSulvp2VaNedSuY23iTjRbtffikm4r91tqnH5FMU66bq3vV35e0sceWO72ovyFgYwSaiFt1+OzYpsvVL0PVD5D40BYu582RYSUspZugoRUXalqEn9KJUvtuJcpw2P5wyNL5X2nurFPWgilagYNd6WEITFN8XuiiNru2Xo7q+YKi6vrsXHApIUKWW6d36Je5t2wtU1f+szN7znx82atUuW3UN6I/YgXGVFUCvBPqxvQitDvbWDqivK71IIMsUTVWuObKBTT7LYkZUagx4JksANcmncYuZARxq2yZJetkvF3SjC5cKgAq7gmX49+U54w6mSMSWJBx0nsztvDnR2PBFIuTKm9ZbKnWuq7TALv+qNs9zD5UTZKC5l9/Cupgbwo3GQDTusDnhpsFO9YtrdLWlPjEsKq1VMJMEQiPZtF+mIEVSU4B172KwrFvPPKNpfNoOcbXYcmBC3BL8eaHY8cPfeYo8uCMslb8gjNpFnIdJuS1IUK+tkuWEMI5qVBFsW27oGXSdWajipxk4usjyjvdKo/l7bt06Pmop16BF4uzxWGl6xRRN07FZKhSMWKAD86aipJDAN3wWrXdr3K8btALLZ2j3ONSoOBd7KnOx+gHkYQDFjnPgTbZwz99yPgboMzJBStQY5KOmIIXkSscUK3hY3bJJ3I7FbanXOC/72ODpbz0bPO+FqiQMYoFpse+2EiY6u6+4W1Vf6QARuyqoFGFw8pzhYKHeSlqq5W+edxmfN2fLv+LbiCom6OnIKaKiuSRTVyt8gDV8eE6/bkQD9XFy4iEy0h+DozEcUh+1re7XFXZQ/ceapxREcQjNIP1GeQPioXcnM8uxKy+VyWqNF3Ubd7iBUqie7SwnWsnWzLzVGPBsH/CySK7u4VgrqMOc6UYrK4WK/klQEOuDaRssJSF7vN1pvyVeh1G7kheMOYJax7GjYOaLV3nHhHF4U3E5AE98FkXGHaoRjCAsEgb48kyjtumM3aJaBisi5vrpIk9l7DiQoHDAwXKAwCFmp1KpqA2074uJkQxm5/mkvoPL5Qt1a43zfoSlLiNfyprR7oTfvrLaPr6OMcDsMyg+NPim41+joLbL8SWA4Wb6qt3AjXtrbhOnIJUGUFKvSyxoWoPx8vPY4yS+7wWURlitOd2/I90rg4GUsX4PCYHo4veRSXJ0uPhq1MB1H/e3qcCHcEgizRMilKe17WL3s2b5rqfVZbQjG3EnOWK7gfNRk5paHx92e3ORaVpMk7u6qiSAVGwHauBoNQvjY3QeG4TlPYAllWskStz1LG4tihiHFzmSY2dkq0hvlZEvkKCVX0hROTVbZ7ZUIM+ig2bQZ2SJWs+S1pM5aAQeECdoYYsVtoO6ool7bxdLJRALJJUYp9QzcPO8dvsdrGOFY2Ywm0DoyHhEHwX6/dWkpijOyqPrE2d+kfIcZ4hDrzj1ZIYkLNSw0W3Nfy6dNsddaUO49SjkjWrxaq/fAg9OeDrUcoO/NgIv9Cl4pmcuf1F3fxjUjRNsS9x2+jHnKX/F8e0YDOcYs50Q0A3o346M/iZvsRPL3UsP9Hpl8ohIQf9xkOJhqvM5pBEad8jD3dnVF8rmkYagOTdt6J9bTEd9M4Yn1m+w4Ysto2aRryThj1jmzuXa8sigVAQCgeaogrvv+fpwwZbwMMorZLjqUhSoS5bSv0401kMXJ3qLNrm53rnyH/GW73UhurSTQpsBbu/ADXrPPAWdyq6azMsTrSdUcWXi3YWQ9vx4Oy5vGUR5uXqkiLy4cdLfA5E/GaOewyEi1nib0YWA3PnTI/JNCbTrbZvwjRZvSNccKAm6UlugpXwDx1GkEFjVlmSG2F6IejdZlm2jUVRZSG4KXikviUI+kNLw9FbvtBsusq1udFWqAyrsRlpzpxAID2ntkjKOoRbxuf0+1A3kgmSN1CFTxTpx5m4qoNA0vWJN0VmcHfldJEnm/1DSk0elptTW2h/iQkEhqdrbIZJhYmRZ7h71833a+ICg0fBLZdbVqRR1WdlvpjlADhkYYh+J2dBf2qiZJ9n6f00dnmxjSZIe+TY9JatggF8qNdU10rZgUoTgpS2ATFLdQ/0D2dmQpvOqnh6XSgaYC3rZMgt1it6VVTDeLE71yEqs2paO9vO2QJbTdVOgZd1oC2jOrYaqRUzlMx07zqPaquM20pUczYkS0BmDQ6dPFpPmttb8bfoxslcOhQpkaRUpz6BQRpBB6bA6kRvvi1gTVNyDibKVRXnNV7XJX34ZMgyZH5PKQtORmIOMMbtZKFhShe0tj7zyEO0rXtxJSZxwkdvEJu/S8R7GbkhpsWQqJG+tmMWGy1X6E3ExOupK7qG2z7SNN2mH8Nbc7p/YDb9oPlUfupskPqiIfQXfuk1A5WRXfYCU1grnM1vULPC7T4/VY8UWsrqk9ywhUFq2ZQjzGDKF0WocZEMGdJ71DOoh3gaF1Ejl1m6YK77ud3GEoVXYq8FhdRbR7Caqm3XfYUcEOKByjSohcm/xwMHf7ypkuYn8WL7IY8Gukul6uChj8LilBrM91mG0nVLNjAgymB6hPIYNQnB7MmJk6OSRfnOouQFqLoKK09q+3DWZy11va1UbCWtWG23Kh7yNtz0fIFpNpDB2bZkkjgicVhN4JYZQVnnYKtg5BUqV/QViY46tauGl+ASd0sak2fAW1RUX60E4mlpcJQwTTZ+pa96Gk8wMGT0cYRphhs2zjUMR4iqpkrMd3Az3hHDL2gW+3VLbDC5xrYOyi20skJ8t+JCEyUPs7R/BXpnIGlMquh9VldCgaveQXABMdBllOisTwld25oFbyHEfRIqvFZX6ptgrWmPGpk5KWWJEdXO73t7UcyjCXHm/2ik1XGF0J7RrTBWMvlkqheFslS1B8RwnYETTiHadH7h5fUtJ5kguR4NzDxuhh0qDZteWil+yErQSvWQddN20u15zbwSQB1wN+CIq4o+IUa2ub2bF0nh7rYuNOQ1DTY7taplgSriYbSg+cN1D6WIzkJg4VqG2PMASfsHXZiwSL+gN0Z+aJxFeLnpnGBNDXNnfNdwNosAtXzADwU+Tp2mtItl46e2kfsezb+7f5gOh1zPPPviwy/0H+/9m5wPNP+F/PiB+nKYHrf3rw+vRPJfn5/VvlJUCO50lHnbbR64Dg7845PvzFSeC8aXx+2+LrSdXzyKtxo/mbhm9J7rd1U41ffrfjMp/+B3X95fXdgG+HP18e33wBt0UTB9V8BvRnBytJPp/1Bn7iNsHrNnqd+bx/81/fU/gyqx5U5azi63gRaIZ9RD5ib7/9NwCBdDsXKgAA -->
