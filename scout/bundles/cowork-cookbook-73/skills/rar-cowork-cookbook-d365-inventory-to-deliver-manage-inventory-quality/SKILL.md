---
name: "rar-cowork-cookbook-d365-inventory-to-deliver-manage-inventory-quality"
description: "Scopes the conversation to Dynamics 365 F&SCM inventory quality management (a subdomain of Inventory to deliver, covering 8 L3 processes) against legal entity USMF via the D365 ERP plugin; call it for inventory quality q"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality", "rar_sha256": "671cc6d2800942d3a62771d65e42687cbf82814b6159bdfed3b318c5270ca4c1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality`. The original RAPP
agent is preserved byte-for-byte in `d365_inventory_to_deliver_manage_inventory_quality_agent.py` and in the RCI capsule.

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

D365 Manage inventory quality Expert — Scopes the conversation to Dynamics 365 F&SCM inventory quality management (a subdomain of Inventory to deliver, covering 8 L3 processes) against legal entity USMF via the D365 ERP plugin; call it for inventory quality q

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_inventory_to_deliver_manage_inventory_quality_agent.py` and embedded as the fenced Python below (sha256 671cc6d2800942d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_inventory_to_deliver_manage_inventory_quality_agent.py` first:

```bash
python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py   # or on stdin
python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage inventory quality Expert — Scopes the conversation to Dynamics 365 F&SCM inventory quality management (a subdomain of Inventory to deliver, covering 8 L3 processes) against legal entity USMF via the D365 ERP plugin; call it for inventory quality q

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality',
    "version": '3.0.3',
    "display_name": 'D365 Manage inventory quality Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM inventory quality management (a subdomain of Inventory to deliver, covering 8 L3 processes) against legal entity USMF via the D365 ERP plugin; call it for inventory quality q',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-inventory-to-deliver-manage-inventory-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '437bcb2dce05c37f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'inventory-to-deliver/d365-inventory-to-deliver-manage-inventory-quality', 'uses_skills': {'custom': ['d365-inventory-to-deliver-manage-inventory-quality'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Manage inventory quality Expert** skill for this conversation. From now on, scope your help to the inventory to deliver domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM inventory quality management (a subdomain of Inventory to deliver, covering 8 L3 processes) against legal entity USMF via the D365 ERP plugin; call it for inventory quality q', 'example_request': 'Act as the D365 inventory quality expert and help me work through a quality order in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use when working on Dynamics 365 F&SCM inventory quality processes in the inventory to deliver domain, with the Cowork D365 ERP plugin and USMF conventions.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365InventoryToDeliverManageInventoryQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365InventoryToDeliverManageInventoryQuality'
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
    print(D365InventoryToDeliverManageInventoryQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPixpbmX2HejhjbrarSvlA3bsQIhARaEAiBFpejrH1B+4rw+L9PCqjF9/p2t6P701BRAZIyT571eU6+qd/enL6Ly+bt49spcIqF4GRZEgfNwin8xbocy+YKvsqrC/4vvLLomsTtu7Jp3969+UHrNUnVJWUxT/fKKmgXXRzM44agaZ35yaIrF9xUOHnitQucIhf8/z6tlUUCRhRAzrSoeydLummRO4UTBTm4u/jRWbS965e5kxSLMlzsvg4GwvwgS4D0d2AV8JUU0YJZyPiiakovaNug/WnhRGBe2y2yIHKyBZg5iz+fFH4xJM5DQW5WZKMdFlXWR0nxt4UHzF4k3SIsmz9RrQbGBjcnr7Kgffv48y/v3hLw++3jb29e5rTg1tss8KuWesk9dVQeJn29f3yKA8Iyp4jArGoCri/AdRU0YOUc3PKDcPG6+rENsvDd4t///To6TdT+9PFTsXh9Pr3N/7S+eFjTlU7bBT4wonLcZF7iw4LNRmdqF03Q9U3RLoBDu9lXH54zv0kqq8Xf52c/Phf5EAXdj5/eQCSbR/Q+vf20AC759Nb08+8Ps5Tqx58+ZOUYND/+9E0OiFcaeN0sDGj94fPr+iUWDPw2NAkXn0+Hzfq1VhN4SRUA4d/ZN3+eqr/EvVzy+Tn4x7J6t/hzybM9fwf6PnPTBXL/XCzwAZj59iEtk+LH1xoNSKjCKbzgx5/+lVgvDrxrlrTdf0nuz0/BceD4wFsvl/z07hG+XxbQy7avMv/1shVImL9iCRj+ZbmvjvpXsh+R/QfRWVKAUv4Syz8V92cToL8vfv6Xtv1HE94twk9vr6Jx3Cz4uPjtkSI//+B/u/nDL78D0f+pmFPZN95DwmcAKUkYtN3nzz//0D5u//DLzz/0FcjiwMk/9032ZzL/zK+Pdf7gwdeoH/84F6x/Lq5FOQLc+lJDi9/K6n81v39YXED5+9/utx8X31fi/IEWsxFfFn264LtqbIGu3/nxp7ffARIBpGt67/EY4Me//dtCSbymbMuwWwBI7rsFCHCX5MGsvB4n7SJ5gnQTzBidAMe+xoH8nyM8awww99f/4z3Q/733Qn/YBxj3+Ss4fu7Kz6/gfH5C93fPXsD564eFDlYqmwSALIBijT0cPs1DAcYDLaomaINmAMjlTl3wHhT4+/kHAODFr399sc8PuR+q6dcHdyVPbNTWuxkX2z4LPsweMOKgeNnrAboLboHXgyWzEjDAIkwAwL8DnmnLbAC4OnurvSaAGvwEIM+DE2bZwKMfZ2G//vqr67Txp+IJ5PjiyYctDAZ8VWfx/j0wNMySKO4+FYEXl4sffvv9h8X/XfxHsx7C5zUOgGBe8QIaiid1vwD11888CUIJgg/A5RGv335/uRuIKQCBz+QYJi9GBvl7Dfwvvj9t2fcYSS3cAPgc+DuvyqabmTTpPix24eKrvmDR+dHMH3EJGNUPqqDwg8IDTBw7wJyvnizKbjETfhtO7xZ9GzxW/dVtHkwc5AAInO7XhbI+ALYqs5nHmxd7gcllkQD3f82M530gpPmhXay+iPiw2M8Zu6icxqnixnmtETrPuACW+jIdCHcWRTB+KmaafrQUj/J5ugcMAp7xXiF9P8cctBI5SCu//bL2Y4wzc6r+4NbmU9G+SsNp5lA8eo9pEfWJPxPG314p1cZln/kP/wFNZ0mvKPivqDxy8NF9PHuDP2k2NjdQ7t3iU48hKLH4/7mrmn3BCoK2EVh9wy02e12znjGaG81Z5WdvOg+eRTzq8VuT8wXIvuD5pyJLQMI109+eIx+RfY15YmTfgEBorPaQD6wBMXqoNmf9nMVNM9eL86n4QhzvQCI9UBJ4HEAEKKHZV18WnJ9+0TQGODBff2siHlnS+DNggMxeVL2bgawLg8B3He8KtGrmyn2FGZRAMMdkjBMv/oNVs6eB04D8BVAiAbUIyOXDVzB/Pv2i+h8mPnulecqjj+xB4TYPAUCPYFZwhrIx6QB+Od2zrwd2fnwIAWbkVTfb7oJ8A5Y+bwZNUPdJm3QzTD79GlQAtN/P309L57sBSGFvrh5QE1UPvPuoojmpctAJzRnhB6Co8qQAnQFwyssJD4FOHjzz5tW6PiU+br8MCh6lN1Pal4mzIfOcuUtYhEB1cGf6Hjn0P0sTIG8uhafX/jHTvq42y57RswUICFb88vTZTnx4dgTPlmPxRe7Hf9o4/fjX9lYPjj//MQE+LuKuq9qPMPzk5S+0/AFgF/zUtX1Q9Puvlfa+K9+/6vr9Ewe+e/aqwj+s9HTCx8Vf0/YPIl7V8nGBfkA+IPMj+ZVtrw9wzvr9ynpPzE8/FVrwDWvB8gCcupkLsgn0BF+J8csQwI5RA+AHDH4SZTvz6wgo/cEMIC6fiu/Tfy4/QDxFNKdrW34HC48OAZTCM4xfCQw8Kjqwtj/7LAo+zFu1Wf02ePtY9Fn27g1AbvDX93szZ+VzyrfzphEU1wzxSfC4eiDIrZt//nFDrT5+ONmHBRcAtMra79PyxTQz035XPU+bga0za7xb+MBT7cyMwOZ58bnynBakMsji2bZuqmZjnlvDuZn82mn+szYGIPAHUZQfZy5794II8A12B4A2vjT6YNXX1mteISh6sKv9ed5kzG54TJl/gDng6+ukr39McIO3X/5JL6DYA3cAes+yvin5bWj52JzMJgDR3XMv/dsbcLkDfOC8nP7qbsFwUKbv25mxYZCmYHFw/Uwo8Ox/oO99SWxjB3RZQCRFo55H+RiDIEsC83GHwmga9SkyIDCKoT03ZDAGJVwKJZeuHwY+7uIo45EYjXgO4aFA3jNRP8+NSjJrSS7pEFkusZBAMcT3gxAjfJ+hGMojaQxxlq5DuuTScb9NvSaF/zL9aers168t+Oyilwd+e3MpAozcEu2OfX7W8BJ1YYx2J9mETIS52damkU6D5riyy7fVvrWKVGZFELEc6xhzzfuRptpirtsbJVxGN47dLxOOjAtIg0hmOm556Uw7mmXtBzY6mepdvN5JyMfv3TogCTw4HODlHpKWuqoJaxv1akdTmNtwa23pJufwZnJ8hXRMAr3DkOTR6z2v8pLsS/H6mpPlufXteqfEl8GNJRLBNnGyd134fqXDdMk6rU/Th9VZl45lnRlnutZUTS4NmmzE3cqpjN2B4uQhyhACI0o4gSAvmZb7I2+d6+oq9q1ElJozYkpsW6dAgw/bAb5kt2o63qfyTKoHImqb1KKCE78WPH+dYZJPRmobatPeLHAcDwrRp2BVX1K76w184/B0c6+ks7kqE9V4VZrtxaOcXeIgypX8Qvamc5JMKUlF00sDaXmqTchDZAUXOgu9HEbrWMtS52mBjKCnXL+h/NkdojoMhX6lbhj0tka2Gz4JakzyEue62+Z6pyrIoGj1JBVBerWbQxNM2F7E12xXZJu81CTg0x200aWdVmRBY+xAu3w5Idd+kwWsxCd7w61218S83AbfTbti5105QVh1Ecv17WmgmGOYenTlC05LNvmd44ZG32/WvLMsymuZZOF+aqX1bh+y16YwyK2XT/eDUe+KvaOw+DgwnaQOR0krrTQvvfpyYxoziE+8rjQ6ae4vd/8Otei22nnSPu6NDS862eXKlzZVtMBR16017QoysmpT8u+NFqzuE2XnFr7OUknO12klJig3oRrKR2vOqRnraGxCBjEpKiL0i3WrFJfRq4JCj7SFiMt6ZDulaNOaJv293mrUJSoywrQAOnbbBD9JEXOx1/BGMJnz3jd4dUMNCDyehqUs8yElT3Z+SsJIhdVrt9owZwg97Fw+HZ0LqRzDw7ZpLdPKesNwN4QaVaRlpCZkCJR6lxT+6mmmgAf9/sToamhEQSgQNnIDINJrVwsUJ08OcnluBKW9qTBTwaSebm9D4w1QhK1VklrCeQHtR1+osCQh8klvxr21O3IsS2/L9JIGyXqr+pl30Q4n45gjmLrZHURoF935LYmxMMwqnJWF1s0zJm9Y096E2asbXxcpvD16bdGnBztWrvUpk7j1OdtH1C7PupI/HwgzOq9k010RPCGBMPtsMqxlbxQwJh74W47Zd1v1JHGwr7YG3y7CCoWd+xFtUJOnoqvDH7VMyFJ0tbGW9yq+3JfJqdvtsrplYqwPUQaJTON0G6KikW/T6WjXyHRsbAQmO/1UoFcL4hmshSbGrJaS7vGXDFJ8Tby0suOWmzjlKjPNtWSoI5ksp2gd3GzKLsXizN9rVXIHyU8PlKceBTsteJa8VMK2Xob+Xu7b5a7upWhzE0k/I5zLVVZMhvOKIwgNzvXVhT8LDc8mnN3QhkQVgko215qtLh6iCWZqX67r9pqsbf5EyQUua8USOZeGmp4Cap9Xw+0c5td7kdCwu1/FG+FKWnCMBysMVhQsYXBluWf2nkkr6LFMDIydcFXe0M6964+RhufePU4Ctjid20Ag6+bknU+24snVqYMpiW6pnAshZ5ri9cknwoo0AUmqeZivqpq/3YlwC8H7GodaG1E4RSqXFZFiK5xHz9PklZZ6QuhBTaFpTcZ0QTDFceqljT5w0dCLihXGmhAWl1pYRQenOPjozR1ZKg9Rru/tSb3W923CUJlIcOckGs/+lhjMw5i1u8TlL72Vb5l4x/bsEYo3KlRdHV3kBXfbDDiJ0yuw3w6k87UUcw2Vk3EnFMYNMTbxsc6Rcb/m7LuDLd1cIi7W2tE2vS14unq6xKfr0THueHjkaZ0SrVxDjnftog4IUvWkOVXFZsSRQ1RvzhxtMT5tQGNAX5JG83aJ1robC1JV1L51u0ZHNYFnqMOA37AQ3q6wY7MpL2gueehOgSap1iT1XCx3VzwAI2VOOonuVIv0AKNjtNsTpN+t93tMO5p3GB6nyjtY3XoZnlzmcA3RzunptTQkgcAw2UHkS21cLbOTybK4i108ia2poMENSzO5IQ7pjV4LedzQnMJeyPRGQ/0dZ6gwvIvLpa7vsYuVk9qZLTwlcciNqQN4g0QiSGuBmFaToe02UIzIvKgOfZAc0lCvTcTfcjlyFkLT3fWTs16rZXs8I1jd5odMP9uqfTk4FwSVHHhkrpBprIU4Wk6QKDrs/iisT+INb/34tragXL3DEb9S8+iq2vX9UOzPHscDtwqFIIqCvzpFwnhZHW0q3x3ChoLo3E22sWRz4W4ETdxmw9u9eUTogPUnolHTq+vWUE0qHaof2DA5R3eKsOqYl9cnVi7W94BqxpKcti3KnqT0dq5FqtbtJEIo/ETXMXdhd4i+zg3eqNJNQsJNczqWl87VbOogOud12bP2xBSRJfE1s6GF9lqsGsrj5XOvr3UlYFHMz/ggO2/354giIkfgDbEXjrXJ95qJwXrOKl64al1jU3rwmHbdzaRO12LcMYa0SxM3viN3wmWO8Cq8G6m2kbubI+65XYJsvQBBdQQ3xV52c9Rd7Xq16verekXtZDOv5NNlRajQiqcy6kJKF1ov0RCxJVAmx6Yit4hzcbfU7oSHVZSeRDxXkbKshLOBrG82WGE4G9GxZFNdSq1rhbKZd1eOqmqRrdM1amUyyM3x7HqDlyhMRoPG6lTJEBknBGoDIQClbWfdTqjAhWbtavfwTiXs2cvVnFRdazCj3D2fpGONDNMKbg+677i04LuFtTp5BzcmD+laWapL8gi6UcNmisQqEbmid2vh0B8v65a2K3vX3fP1aQoom73KZYlIwaHOrNvpPhgJkZ420k2DzrxMXS05p0fYSqiSWA3ydpXc02LEMGYvC2biGIdhNYWJXF5EMY5Pnm7TxeGqCNyoqHEV81ypFEGGJOi1oy5HStWvhOtpCSdTIzqaYsJJidRWRzG8n7atsiQRho3W+rbcbZM1QgTSThdTbkdounaLqx0L+hjCp7Yju82R2EIkS1+V9m0XCaboj4qbncQYFk2VbEfOITNHx+2JQO1gkvejM/U6YoyiJU0r/Dbk11Xu7lhvF0kIme+k3VmiWMAh6jSWW/HAVx5PeVDB8lMT0xYa2wR5lMKzBVPOsUelW3xpltdbIAF6IgaaTYsOq+RrnU0bXORcKinvfH11pHSz6kZ3dcpdqj0Yjb6lpakzzLE4JEt9LzYBNi0x20nuEZVHnpW51yt/WReW41yTnjlGzPmod0lOyNW2OO/HVeZYLcLK2oZva8/eG+hK424WJnHaZFx35KGv89jG1m2kkM3Si6UKgvH4KhtDtG8MpwodNTkoAto4OhdfkKS80Cen5lCSqdIc9GHFPoaQwRCK3OK9k7DxjJhVOiWfTgJFYlJJlBABmO+4xWIDFdKrcPcztXdxW9qvLtscstutpDARUXKpUJalI07u4J0nPQjDzXJviWKacft0NO2t6S1NcUOP6WDJ5FXE4XBLqn1unMv1il/XY4Jp+62YZ5A33c7H+3oQe4wM79BmXSo7Q2ePgsLqTb8W64K61o2DkvWJpJw7QoYq7/ERd2nnvjD0HXgDOkZqZUyhgLUgNJimpiTXhrfxnnS7AjYxgTEDbV+wvlhlsmynOeax3JGrAe6bkp5KmXzfS70E6WFqVymipNbl6Cu5AMNmx1xLQ4l9vu5ZnEdAf6XsS782iIGUhHFro0qubTahffc60OxbLnnIcjHZUaY+Xu9SPAjZNKaOJJBKqkoxeV7jxrbmPQG99XdjSnVFkvYn7n4cHeWMbJJx2WQ0vsWNVaNwkdWrd07Ewz15LRFxuKq3lutNpRPie81dVt3gh1l4WO22sGCsODnzL6DuelTYJeNWQYjVmY1q4TbKx7xUAv2+3GFaRRTOPTzACl0DpuSsXTYcGIRTCfVmRyjX+RZZ5rizNNqwcAckirdW1I69eSNhjsRjZM3roZ+scDzMhn1VoTE++MHgY4Szo3t1GuiDXgdj77chQWm5iIwXG8EqeK+uebdv450RDIG7ZYTK5IiuL6C+iHv5LkPlkKhMKfLE0cFagkHPW2NX0NDJIldyNQ510eLONgaVoYrAdOjWHY1hlSAZGpByZEDhzW1XkV8JAaPvl6rFhh5CStDSoah2DHUZVUe75yS0yX1Va2wcXnpLmNgFnFIW5/CAHaDt1sM862rc+NBMFIMvSfeMnagL553vSRAUx+5I4HxSHpk8OOwKdj8cKdTUTFZnM0pAktO2t+ByI0r+Na0IfHnOQ8zQHcNxTbu/JDpj5reuVtKiPKg4X6/JaBvb1d3wCJ9MI2GD7fN4i3PQkrnybpCfeoKnoLMvnCODnczlFAxDD7u1pk1YhvujwJMYCTb6Q9gfK044s2PCaFIZXBuqw884Sk6IGZpbrRO9QXPUNPQKDU7rCl1DzRZXlC1kiKd6J4rs/iSyUBD2/h6id3fmhtzOJ650cpQ1OOGSr4/Nsr0JKOrKE47FeZGja7CDv5qKp9B7etsc5MsyFXajArrc1sQzkRFPtFHEa1xdbZrEWquiu/G2lxSK3BXoEs/SinVzhUOXJNG5YzIZTerg283ol/bB1W77Zh3dus2+2dDkyBGTxpAGcfWCiIAI/r7j+m44Qhv1NFUZDjVFSi6X0YimcMaOJpT1pmvEHr/0OZuSd2f8KI2sDDapFLLZMnjLyIc+H4eJ5jKjSFICpLkynNX9qSO5kEvFvXj2cR7bVe5Vacjl6qboB92YSL/EQBHA/qjf6PUg19HoU6I8hHvfP10mAy1wP+YlTbuJWbBch87EYQe9aDhqXYxM0l87czts6bALcNUHe5CqgfBLdO/bLqc1v8WcFYKkTdtNUtVjk0+ZO8tLK8lUiL6PrCBVCEu1UXYtb07Y8i7boz6OMih7LDyTqCIksk4F0UoDUUHd9nqumDZOLRpXdoG1bzpSP6tDE7QQ7GplVuR4Ioc9RUL5OUVoRWFwsE0kl1Pao+7+vvJpGS5sMcMV39RXNKxacM/IWmX7g+6ZSCDHHU23AMfWp+RCqSQn9zq1PKB7OPXd0wnj100dXxIxXq+0quRDF1Ug79KCDRxWMhZ3ud2xvmBxq4/1oVECDRqWo+sftdsFh/llWEnD5pyASq42+2p9XbV76gAdjCu2OpOV6voaJEtbctkrrITxRyWGTu75pld4IbcraMuM6f4sgW3TkS2Xfki6kcSv0k6vyY4yUkG97OmshKO1qoocJO8Gde8xJgnaK23rgB5/66zawdOEC81euK19oC+4Z0Br2sbjgljvVegoK0cusde10aY9P9yPdrhi0z160DDHGM5BulQP7h65mhziunpvm6pz3koY2vhYgeWuY0bk0QcV10LUSkgaH29yLBOMPelQF1+guqZwmeySXP2INnvLvqYQLFt3rtZNUbX10sNWkQv4fnK9oLQH3OfIoWaxTtzgqmXSF2S3TgCrRmHcEPtlz7D4YVxRK+aSnEzIZldVGZwjCe8HzEySgVIw6tCc2p0+cf5IkPcEOwh40d47BweYLsJmRe2UminD0K4vPT3Kfh4wyTK8n3kBZjL7YuHOSO3uq9U9OmgBWa4OwupK4EGyvdMwBl9r3xlKmjXrOxHbZzltlrSMgjwbUHWQcZcOMTM2TL5tIsYw7qYLDSEEGVUSwmvFgMplmBNV5PjGrcD20U3Jj/tQF7CmcSMZqO5mGb2x2zCX7vjBiEncGtzbWEBxcrpFWB4pfD4iodGHt2XlIQdsJXvUdqcEV53byaGXbtjCUKfjeom4TRht2VLv9QzurqY7kJZEeGKchceB2x8JaKA8cUSLgB6tFbTengjZcnIN5sljaKy2IbVMhgoi8mHQw97QLh3a18vgIK3he4/nR5pmeHxoQJnDFsP5wlJecUdYuHveRpc7AqnhblNUcOQzg7JBG8/u8oHJ456Gd8Ym7Dw4tnmoJ1BnvATcYBu0RS9vg0nmWMipncRosN7KNnFnpZuIwJglJkvyVG5NRp5uzkAYHXFeagy0PhWKD1pxrztfJZYDTS5c7Fv+fFydgjyRd+ly3/QpSvj8trg1rSoLeqSusE3IOZwfCRWLXLYpAksrZP7DMLKdNHytmQMSx2CjfEzNZQ8J+1vHllZIkBV5a9CWOR3247nJt0i7cVyYbUu4O5G5kuAHMVhfEQ1hMLaKR0eGwyZvwwxHl9twVWsqzhoVzYgRTZdXrhTZukXgqDcnw/cjBF6q+RHpaQK5p60P60zlYTbJ30eWZf/+97d3b/O51Ot06b/x8sv89/7/sWOH5wnBlwPtxzlO4PgfH2t9/O8o+cu7t8ZLgIrP45c266PX0cQ/HL68/+snmrO86fnOyZeTtefRXedE89ubb0nhAxYDarVl9jjyBjNAoze/4dV+fr3w8PWw6vPj/R9wWXZx0LzN71v9s8WP2/OBduAnThe8LqPXKdW7N//1psbn2WVBU832vw5Kgdn4B+QD/vb7/wMLDZQ3iisAAA== -->
