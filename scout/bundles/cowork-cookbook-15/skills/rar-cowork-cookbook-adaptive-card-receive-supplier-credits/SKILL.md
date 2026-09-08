---
name: "rar-cowork-cookbook-adaptive-card-receive-supplier-credits"
description: "Generates a read-only Adaptive Card JSON file visualizing receive supplier credits status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_receive_supplier_credits", "rar_sha256": "6235404a057406264f3c01ac0ed3df19adc7d1cb56459270c8c4eb7281e18c80", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_receive_supplier_credits`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_receive_supplier_credits_agent.py` and in the RCI capsule.

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

Receive supplier credits Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing receive supplier credits status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-receive-supplier-credits
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
    "as_of_date": {
      "description": "Date the snapshot represents, used in the card timestamp and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
    },
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-receive-supplier-credits-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_receive_supplier_credits_agent.py` and embedded as the fenced Python below (sha256 6235404a05740626…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_receive_supplier_credits_agent.py` first:

```bash
python3 adaptive_card_receive_supplier_credits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_receive_supplier_credits_agent.py   # or on stdin
python3 adaptive_card_receive_supplier_credits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive supplier credits Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing receive supplier credits status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-receive-supplier-credits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_receive_supplier_credits',
    "version": '3.0.2',
    "display_name": 'Receive supplier credits Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing receive supplier credits status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-receive-supplier-credits',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-receive-supplier-credits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f6f28d6190af570',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/receive-supplier-credits'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-receive-supplier-credits', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the snapshot represents, used in the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-receive-supplier-credits-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical receive supplier credits status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-receive-supplier-credits-2026-05-24-card.json' that visualizes the current state of receive supplier credits. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current receive supplier credits KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing receive supplier credits status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card showing receive supplier credits status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the card timestamp and filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-receive-supplier-credits-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of receive supplier credits status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardReceiveSupplierCredits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReceiveSupplierCredits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the snapshot represents, used in the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-receive-supplier-credits-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardReceiveSupplierCredits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOj1pLnV9HcjmiXW1VXCIEQ1fEiRmwSAiEWsbocZfZ9EZsAt797H6R7q+z37J73JuavUZUtAefknr/MrMOvL3bXRmX98vlF8e1icbCzLI78emEX3oIs72Wdgq8ydcB/C7cs2jp2urasm5ePL57fuHVctXFZgO0Hv/Bru/Wbhb2ofdv7VBbZuNh7NljQ+wvSrr3FSbkIiyDO/EUfN52dxVNchGC1689Lmq6qshjwdmvfi9tm0bR22zWLoC7zBTUWdh67zWKzRRfMvyvkefEh80M7W/hFG7fjQlXOzI8fF/e4jRYR4O/XHxebT+iCE9lFC1g2H4Fg8v6wqMv7x4d68KfNwnZn8RdAp7YsmleglT/YeQWWv3z+6eePLzH4/fL51xc3sxtw6+Vdn1kd+Sm38iY2+ZQakMjsIgRrqxFYtgDXlV8HZZ2DW54fLN6uPjR+Fnxc/Md/pHe7DpsfP38pFm+fLy/zH7krFm3kL9rSblrfW7h2ZTtxBnR9Xeyzuz02wHJtVxezxRvgmCJ8fe78TqmsFn+bn314MnkN/fbDl5eymj0F9P7y8uOirAG/upt/v85Uqg8/vmbl3a8//PidTtM5ie+2MzEg9evXt+s3smDh96VxsPiqiDT5xgs4N658QPx3+s2fp+hv5N5M8vW5+ENZfVz8OeVZn78BeZ+h5wC6f04W2ADsfHlNyrj48MajLnu/sAvX//DjX5F1I99Ns7hp/ym6Pz0JP4Ptw5tJQAjOLvh5sXzT7RvNv2ZbgYD5VzQBy9/ZfTPUX9F+ePbvSGdxAdL03Zd/Su7PNiz/tvjpL3X7nzZ8XARfXig/A8lS207mf178+giRn37wvt/84effAOn/Ixml7Gr3QeFrbhdx4Dft168//dA8bv/w808/dBWIYt/Ov3Z19mc0/8yuDz5/sODbqg9/3Av4q0ValPdi8S2HFr+W1f+qf3tdaADPvO/3m8+L32fi/FkuZiXemT5N8LtsbICsv7Pjjy+/AfwpgDbdA6Rm+Pm3f1ucY7cumzJoF4pbdu0COLiNc38W/hrFzQL8nVGj9oFdmxgY9m0diP/Zw7PEZbD45X+7D3D/5L6B+8p+Q7avLoC2r2+Y/PUdk7++YfIvr4sroF7WcRgXAHzlvSh+KewQgPDMuar9xq97gFbO2PqfQFJ/mn8s4mLxyz/H4OuD1ms1/vLA6PiJgTLJzvjXdJn/OmuqR37xppcLqpY/+G4H2GSlC2QKnmgPRCkzUFba2SpNGmfZwosBW1C9xgdtYLnPM7FffvnFsZvoS/EE7M3iWdaaFVjwTZzFp09AuSCLw6j9UvhuVC5++PW3Hxb/tfifdj2IzzxEUD7e/AIkfNRBkGddDpYBlwEnAxB5+OXX395MDMiAgroAXoyD2H9uBnGa+t67vZXj/hOMbheOD+wMbJxXZd3OBTVuXxdssPgmL2A6P5rrRFQ27cLzK7/w/MIdAVUbqPPNkkXZLhoQjE0wflx0jf/g+otT2w8Rc5DwdvvL4kyKoCqVGfjfLOZjEdhcFjEw/7doeN4HROofmgXxTuJ1IcyRuajs2q6i2n7jEdhPv4Bq9L4dELcXhX//UsxF2J9N9UiTp3nCud2I3TeXfno0FW6ZA0zwmnfe4VtL4i2ujxpafymatxSw69kVLigJgGnYxd5cGP7zLaSaqOwy72E/IOlM6c0L3ptXHjEo/1Xbojzblj+2Pl86GFoji/8vuqRZ+/3hINOH/ZWmFrRwlc2nV+YOcfbes6mcGYLQfGbg9/blHaLekfpLkcUgxOrxP58rH6q/rXmiXwdUBVLJD/ogkID2M91HnM9xW9dzhthfiveSMGvxwD8gNQAFkDRzrL4znJ++SxqBzJ+vv7cHj7gAbgDKg1heVJ2TgTgLfN9zbDcFUs1+e/cnCHp/ztt7FLvRH7SaLQ5iC9BfACFmR4Gy8foNpp9P30X/w8ZnFzRveXSIHUjV+kEAyOHPAs5umT0IxGufDTnQ8/ODCFAjr9pZdwckC9D0edOv/VsXN3E7O/hpV78C0Pxp/n5qOt/1hwrkBzAWyIKqA9Z95M0cfTkIFSADgA6QRnlcgJoPjPJmhAdBO59BAIDsW1P6pPi4/aaQ/0i2uVi9b5wVmffM9f8ZwHYx/h4rrn8WJoBePq948P37SPvGbaY942UDMA9wfH/6bBRen7X+2Uws3ul+/oeJ58O/NhQ9qrf6xwD4vIjatmo+r1bPivtecF8BWq2esjbfiu+nuTZ+ekv1T++p/ukt1f9A/an458W/JuEfSLxlyOfF+hV6heZH/FuEvX2AQchPhPkJmZ/OiPcdUQH7MgchNrtvBNX+W/l7XwJqYFgD6AGLn+WwmavoHRTuB/4DX3wpfh/yc8qB8lKEc4g25e+g4NEHzED39NZ7mQKPihbw9uYOMvTn2e2RII3/8rnosuzjC8BC/5+d2eZ6lM/B3czjHkgj0JW1sf+4spuvZfDVA6rMV38ceylw9xlYBehPovJRbOcuCCj8KKHfepjZtY/oB4CdP5Luod4s5Cx7O1azsM9Bbm79Hgg1tP/I8vL4YWevC8oHaJg1vw/7t9o11+7fZefTvsCuLtDr48J7VCCQEUCAWeU5s+0GpArIkj+V5VFDvj5ryJ/YYK42fygzAGxvHcj2jwv/NXx9VJ0/pfut9/1HojpoNWY6Xvl5rrof36ANfIN55ePi2+gBtHkbBh/Te9GBOfuneeyZnfrYMv8Ae8DXt03f/vXC8V9+/jO5Hvj39d0//yidMOMawP3ZuH9VvYHwQACvc/03M/xzWf4JhuDtJwj9BCOPha9JA5qef7QeEPOB6mDXrPF3U35XqHwMdbNCwADt898gfn0BYQ4kae23QH+bCsByAIKfmrkDWgFAAAzB9TN1wbP/y3nhjUoT2aBTBWS28AZFIMSGUAyBtvAWCTYutLZdyPc2XrDGbc/FvLXroFsExWEMcncu4jsYvFv76527m6V6wsDXudmLZ8lQHAsgHIcDZA1DnucHMOJ5u+1u66IYDNm4Y6MOitvO961pXHhv6j7Vm235bXR5ZPxT619fnC0CVh6Rht0/P+QKXzvbDe+MJ2M5bYNStm+6xZq0aGFmjlN17dAZvNSagCz4FFfUe8k50gmMenvpbp/3o7bVbyKt+Gd6OW6mwqMkNuTOoLv1h9Q4cieCr8Ri2hrYetyiRuEjJ4jTgkEmtU3my1wtlQoTdyclxgQlq1T9OnJWNl1DmbDl5TkIVjHq3xhJazLZVhi6PKjwJAjZeug3A3Ze141ZXk9X7NBVp9OKwoeucUoWBhUKt28j78TeKeAcebjt3A1FLHm0R5deT3CJzK0zFtAcOu0SHAN422cIG2OJG59hndlp9Ooo4OwRwTC3l800wyXl3Bv9KEVX63Td5qkTrlaqwzbsOGnkWDfNoGDS7nBdb3e+GDSDJW4mCGMaPOg3m00fr1zn5LIN7xwuKaOjowT6x0rVynai9VIas12DlHqAaPnpDvpWhW7DS1pE1njgN+N+SgOviQ4MyVimhoc3bXNlsENKLK+J2gY9ORAdGcV054UcLiCVIZ8uq7gkU8g9rTMk9LJMi/GjM8DBYZtucArqm3J3y/S8VM6lpbGkQK3InR5bA8dYnKw2llHuCzUq6rO7Vk4Op3XCRCO2vT6iJ6hRRHsfjlJY8zxDnrAr1kzYMIm1npkXF9GuGnWyY+7G8HW01QmC1ruUEngQN1ZGq2cDvpCubVIrR8OUqvLHhGeY3XqvbRv3ti6Yk54YoyZmUGf1ioMjsagpgRvpOg0eZUbKlA4mViR2QmrzTm32IZvpNzPqirO8PfbHJj/VgdTRd8XdI15lVJKIaY6qEyWx7UkareiVICCdqRxgrcq6SBDJbahSB1ggDb3d1wossKSBCZXWy5x87XhIKlshag1XR9eaDPoAfzxelpxwB5ETn/j+HIf9boy3+pLEDxZ0y5HQQOLJlUTm2FDxYTJdpojkLYUWXpu4K6aKgbGslSBViAkX2TI/rIsoo/EUd64VRhL2ocL9rtr5eYV3aeE6x7ITy+XqFBo1dRSH1liJPeJuAozVrQAnDmRwrXBcDBDfCHllHdkxmzVbuCETBU6RxoO4o2yNht/ZB+LI4Xy47w/sKNKsCO+G9W5/Ww7cJQshXu53t+HO4uf1wb5eDiEqwjDdnOGSs6wqrzwCySzLvJScFCcqtJUYiICOoUFB7HAQBsEmBJ+q3Tuj7Lpgz+W+d7Vy/3A0mutuwPY3kYCX3EaeWuD2tXWSyPJU0yVZofz+lsvlqEURfdN69oxhWJGq22mUu92+3a3zqFTsOGGvwD9LzrwcYasbzbbX0Kyb8mzDteeg3R04Tyas3iauFX/YK0d6YlwtusmS3+x1IomFCZoaOg70+JYTO+cSJizv1nlCbBjusHctyZu65XAb26WUcNtyX4aVmko7I7s1EoJ7VmMLuOA7qiHiLBdnG0lKM4iIwrtjcTtXEkz23mV7VF1WB7jdRgKruexez1mJPoq9vjrVB4+/+aK0PFVFtEIPPbdJsnG3hC97XaaObi3e9zBCrhgjJbAQSahkGumgqfvzToERVh+Q9nAmMbhk9yByL4hehASUnC7UeZ0xiisPTlfGjJ85E6xE0pQnpmtz25DY71YBg+o2JuBW5SoyrV15BfGPCDoWnjkWFixrJ+p6J4qouxb8SBqyUuuFv7mSWLa7ttwG981L5FV75pSIlCBZ951NngtixeIYkh16tsZali+vcJkLEubZLDkdwlO1QYv7dsVW+rk+xUay7d19bN6kTZNQ7FQ001ngWcM1c3YXxkLNGDy+wk5NN43WQVG48eyxjl0l8dXJLCo3h/xSQVCVbg9UZa9T1Y04VfGl9eFS0KmaqdDICjxd9w3rVetDfGXr/anUvHp1Atw6Ow1GUSFp+g5BYj6UAbvRbqNW66EIryNnbcVuq6Bhm8J3tITkAr/5xmmH+8UEJRCZqUV+CKST25dQCSl9WimY2O5N1VeQIeV0r+vFJUX0J09YjmGitKm6xw1qHWyCYYevxFLEl9fb3dghHcZde+JW+GDOSWOIbfaOlfZLKl+6I2TWkqBtW6QmuJCtJ2mMQKo5thgKd0H2+9TYJJNj3rhreRiOOWXst6sEYC7ltde7aKum0NKEVEqSxRCpeua4vZlVuQpXOnm32THKj2eEYCvOvMrXg2lZhKZkFnpVpxLdYia3VhRT69g9yFSed6llvrkYqVFCe61vt3zTCL1eTh4T3PckLfh+zl/orDTXAUWTNdem54t4YNlUGdB+C7n3FREoK2Nn5xEp0qBKhzvJvPF7dD8ecLTTXAqSBZRkY5cOUrwteZrIbO4eo6e9kwvKQR68UbvWyUraGIybCEolMTq+Nm6oqoyKNmorescXEkrpzABq+KpmKCI9lAUnRm7IDPqd9NPbmBNpZk30WA8ulsuVGqlbg0iPloiGKLmUT1iy09u07bhMOSgAfVqeWtk+a9SZa3Iqvh2bMgmvZ9RVAJxbCXen71XEQWvnkKFNY9oxmcEsoSC5nFD8PbD1ncZzKX4Eheo8bNtNlx/ilF5hhM8NIDVhtME4LBuUAugRH6xbp6iQcbzBB1m9Heu7vt+XxcW3oRJTQZxCkSo7q0vDnbWr3yt0EU5qtd5HZ37iyriSa0wcL9698jNT5Y4+6FKOAC64nXwT2FqVpJKUGfK6H4nrJdsPl0F2pDgc6n7A2dWh46+kIPH4pb9XFvC6jyRCDqSGdC6QhYTtLY3ubrEzLkeb8vECIOp+uuzOQg8PshCZ0Jl2bwjU16qonv0e0o9uwggS2WC+mDQovhvuzopmlcI+59Mt6iWL3KKEQ1/lWwrpsMJaJzbFCjJUqvzO4MtbCDHOBbIcmOX2PXHIVE04q2tRSNKVxEySapgq4bBktB5hJxSYpaZCJlXCkNMUvacd74RactsTzEw9utrfLQ6RztDtHF3ydayF/UVR7Qnf4oxkDs1RG/XSUYXR9CQi5a+9sttUU5t7SrvPJZEg9XvNKtzVKldQLpTUsJ3Wk5oNRN3lGL8KpkS45xUf5UiC7e7pETuLuGgJtxThIZG1xO6g3NBk9C1WhBKJ81ddFmV3fRWcUXY3iWB4sYA32RC/rWl0H9aybu0FDjl2J9Kzs7N1IpnNqbqzhS7VSujvEPSiGIddtL7mGZUQHXFcCgG9pqWImchGKPmEKRRuvzxZmIrdIzfTcuhmSrIoCdnOHXeuXo3q6CTKvlFvtLT38+0V1m/Hg4yzhrml5aMBoft2exZOwlVHKh6TTgfcj+M2POzWCA3LTu2wpnuGCVPh1H5lo0piKxZBH5PiYK9OZUggKJMQYw1D9AUqtzeVyUkP6XNo1W+wZOluiubeBzvs2IQWuEmsjTTgEKV2bqKttRshv3U1Wu7Gm5VEzDriXPh8YdtAy9q778TRAUMYQSVql1OP5IWgc9fcI7huW6aRpbs7T6/DbONgnJqn9qaNGRNTkyMnHWh9FNgtV5mjBUQH5exaCSTwYDvUV5u/0VNWW/xyf07wHj9SG24A8zRy1rjRmIwbgzscs+RD3o03sNjctzWIFEo432rNNlHUdYdWP4ry6tQgiCnLx6uRIDQ0wDbHSds1ZrlEpEcOfRx76hQiWyuNcb/KGUWWwkOVatkg20Z7W5sldCs82Dh0hmHuXdnYJweTbB3SA1W6M41zxpzOB0EQHAWd9mcediiSJYmDc5BN9mamJ87xvRspXPKzc9SFVKNCgrpvqnXP2sO+D0cldSsRTIPHa1PLBtRJWBpadbtNt706qN4V1PI963bYKJVlt5v03eHYoRa1whiiYOmjsj4QobnB+U7d8OOYeEuYXC6FHkB6VlRqqB2JgB1r0d95FgK3WDSPC5dQWu3p3VkOL5ezljFcwsnN9qprZUFuFWHUA24wrQ3q4p1FeS5ejRImMaZp+YM/yc7NDYRWd0/yxPJZzt1CS77akoLcDjw5oaeYGAhVv7gboNsuoC69QZAepd4NI/CwqN4GIqjlZxFqVYkgi4Q5+aPZ+FuSMPtBXJ3pY5zkd5LlqSOF7yBbp1dwpYC6cPRF/YapAswt12PspcWygNXJabJD2yobhNqtfD25r9N1XjepFl7D2/aq3bcxc70M67gU3cIjMTbQtVMa0uWIXmuVdgCkGHtOzrA1TtRbD9mDyjq1MZFTRLTLJwCP2d0VeE6ki4kbOBstSF7A4bzzdOJQMLsovlS3pSSSKuhkKk8PRzvETttU12/pSTiOR6Xcc/76wlxGXU66yVpXhTaWmTzmUXAT+hu8Ou9o6oCHdObJXpcYGL0iuwQyN/cl6jftbmizwLmkRxy7bAziXgvjyk5UakNl0dXAlKCFUBTufNnaboxxuz2vu6OPwqcEWNvXBh+SDzsngrP1ZVmhIIEn5L7GaOgiryn4xtZKQcrruFYC2rfc846AKDxk8I3h3p1y5a03xh2Ci7XYnCRbOfrM2sDXxyW51XcsYWXuVKH5ZRKFNbEq+WhsA4vu6NoZGFeVGNyuAhAwDHlfJadYPQXadtg6befntLUU1jXfXVI8QXvV35Pl+YhscKZmTQNegvyIwsO2Xy1FgEqs6HLn4tSeJyNA8oAoMZs+UE4l+0aTJTVRoQrLR5LB2WeRanTGNI6KbOFnZj2uSmUUemnLa9ZVusK5sm4SCZ+OO4JhkyZtRX3VpBM2QU645rWtlQdnirHaWvadthQvYFQizmNeb6xr1p/PbpQM4eQMYdKL+Pm8YcBkG3swHyNelx1wBvc9HNbQ0RoyZnDvsIbAhX5lzXYcRkXQ7ga5g4Wh7+Jrn2+a/La1WzTaDKpBHedOx0QuJzWoBzjPggzD88MGOd98nowFlrjJ7DGZdnDUbiw9OAg7mc4FQ9fL5Z3OKym1J/MMt54+Qj1VarchSTX9eKOGwjmPorWcyCow5VykxImeTihGrg7ahcFRKRvA6HtPZaUcT4RNsWBMhXom0giVI4714cxvEDjyjOwQ2V1No9PBuUnH4oKljs5QYUA4yqkeGmdIMSSpFHngj+1xfyquCHfftagS595JDNDa81f+KuiWGNqI0WXF58dGOcsrOseg0zUj8WN+WvdL2AxXqXeMLE+Fj8v8jmVlVm5I55pMGFSwMpTtZO3iLnkJEmBUZ+MaOpeow8fmwU9bJoWT+rJSjiQYtqRksjuvxcuaR1rCJWDYMngjp6zuxMbHy/YgFCG/uYZGkCQ1uSXrAWPb3OrE0wWvvHEpE6WRt02AhhRaT5dWOC557uJDVOLb/GXH7DZLkjdb2bSjoaSTO86gI07V2bTOsZBklRDeuknbY0SoSyJWrlCK2dphfo4Q0SkOKpiL8CsprkfZ7K1SrWH2gh0uFORTZBuoGmSkeG1E5Na1tthKSbcgGPwjhLWgDMiZdTNzzz0K2AFdq5BwWKLT7q6d3SlBYvGCty1WLyEnxm8dirf2VJ4R1/APl04V7dL114ILZznWknzHbCIyvxPJJLQ8lGz45AjDrRYhkVzBndDgtpn06DbJ0iJR+2uh9xd5dS49FEQrctmNEOGmR9bS1aW0LY2108jrECZUNDtPYEpal6skQyVNv3M2clGcIMzINJDkJXnmmU73S/psBqMsbbf9cCLVi3fxuGzPnOMTkt62WQj1ii5eCH7Js51wuRMBc2o7ui2yUyM6ohbqRGW0O/tIWSKmGY3mb6eNKU3uHvQqpLtheJa7gq6dw/bJSqW7DQGfhbtFO5YymGpQDNjGwJccfoPZenfjqMG0NVBjV7wIbEFWl8FhdyfQkeLszgeJqrXWVOe71uPgxMlsdLusNLXmwViG6ReH7ZM7DOwVVk1+HjYQz96DzTIdnR0uTX2GntDixsP1STUIo1iigsTQppDLgxAMHepM/cCbSNo767ixldV1T6ztIjuTLXolZEQTjEOlmaK5TqHWkGpxvLbUtbucWyTdeblR6yhEYQcE35jnsVrJRxmXtWIpOP11SjcJxEfIZlVQpymw1YRNRBqMYZDkK/vrEFoCiwhOu1qNfcMXSiIdN6LcOk2tUll/vN5dh+9Q7eI1287JtBa5BjpzPVzH5e0U1EVBeR0noQV2o8xspWB+mJammcFDqjtRaJWptRNrpRM6t58UzLsXqZwPS9O7NH7rTHBrLjHSQI9pm5ACQ5qTUJSXyjtieTQFgUm30+0iGS57uCh6dI/osNcvsU2g12Kc9hdKqt0DL2EnodtkNVXIBxCcw45iLtF2NWyOlO45rS9RS92jZIc66iLSC3vcMrUgq5jgKg6Z4W975DbV081hlqcOAmOq2hBt3w+Fv87Dqd8Ke8ftmV7qfELaYHfO9Hqu1PEuY8ZUkzfGVc+GbOnsNIBHgSWfjstlcG82dgdth7x2qU2IbZig0zoEr1zChYZ6uK7O4brOkZUlX8ZNP63Z+3IazDbDJNTrvBUtnPveuBkSnpi76/J4lVNlv99m5jLxzrR6p2VR0Jj0hKfZRt66Fz+uy2xTO4pE77zB2VUFC4cYq8NpWV4wYqkmii5Nl95XLigojB5VO7sRpnUs6JdtUJMuL7qge0Tu2MY/+XnjU2MIq0lrIb3RWBtCGjHkdI+HplrT2vkCktnNY+TCDTUWWatgKBCBJDYIGV2CncQHHp0jk8TWAo9Qg3UE7d76LJqeKsi1eDW7y4Dt+I0rRi6XStJ+//Lx5fux18u/+NLWfMby/+yo53kq8/5axuNUz7e9zw9en/9VwX7++FK7MRDrebTVZF34dgT0dwdbn/65U7qZxvh8J+r9nPZ56Nza4fzu8EtceF3T1uPXpsweL2iAHU7XzG8aNvPLqC74/v0R5R8U+n5W1ZZfK3u2a1zMb14A3vMx9PMyfDvw+/jivb3383WzRb/6dTWr+3a6D7TcvEKv8Mtv/w3EyKag7C0AAA== -->
