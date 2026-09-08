---
name: "rar-cowork-cookbook-adaptive-card-gather-work-order-details"
description: "Generates a read-only Adaptive Card JSON file visualizing gather work order details status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_gather_work_order_details", "rar_sha256": "842f9e6e42b90eab9f845b64f7f1fede76fd633e3fcc063db842247244d676cf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_gather_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_gather_work_order_details_agent.py` and in the RCI capsule.

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

Gather work order details Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing gather work order details status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-gather-work-order-details
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
      "description": "Date/timestamp the card snapshot represents.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-gather-work-order-details-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_gather_work_order_details_agent.py` and embedded as the fenced Python below (sha256 842f9e6e42b90eab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_gather_work_order_details_agent.py` first:

```bash
python3 adaptive_card_gather_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_gather_work_order_details_agent.py   # or on stdin
python3 adaptive_card_gather_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Gather work order details Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing gather work order details status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-gather-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_gather_work_order_details',
    "version": '3.0.2',
    "display_name": 'Gather work order details Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing gather work order details status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-gather-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-gather-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea770f9d4c3681b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/gather-work-order-details'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-gather-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date/timestamp the card snapshot represents.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-gather-work-order-details-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical gather work order details status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-gather-work-order-details-2026-05-24-card.json' that visualizes the current state of gather work order details. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current gather work order details KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing gather work order details status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing gather work order details status in USMF for today, ready to post in Teams.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-gather-work-order-details-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date/timestamp the card snapshot represents.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of gather work order details status for Teams, Outlook, or a dashboard, without changing D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardGatherWorkOrderDetails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardGatherWorkOrderDetails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date/timestamp the card snapshot represents.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-gather-work-order-details-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardGatherWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adOj1pLmX9G8HTG2W1UvO0jV0RGDJBYBAgESSLhulNlB7KsAt//7HCRVlX2v3XPvxHwZVdkScE7u+WRmHX59s7s2Kuq3T2+6b+cLzk7TOPLrhZ17i21xL+oEfBWJA/5buEXe1rHTtUXdvH148/zGreOyjYscbOf83K/t1m8W9qL2be9jkafjgvZssKD3F1u79haCrsiLIE79RR83nZ3GU5yHi9BuZ44PXkXtgZ+e39px2iya1m67ZhHURbbYjbmdxW6zwEhiwf5PfXtY/Jj6oZ0u/LyN23Fx1g/sTx8W97iNFhEQwK8/LMTjftECfs2HhUZzi7q4f3hoZruz1AugSlvkzTtQxh/srAQL3z79/LcPbzH4/fbp1zc3tRtw6+2rGrMW3ENcE0irzMLunrICEqmdh2BtOQKD5uC69OugqDNwy/ODxevqx8ZPgw+Lf//35G7XYfPTp8/54vX5/Db/0bp8ARgs2sJuWt9buHZpO3EKNHxf0OndHhtg3rar89nQDfBHHr4/d36nVJSL/5yf/fhk8h767Y+f34pydhDQ+/PbT8DQgF/dzb/fZyrljz+9p8Xdr3/86TudpnNuvtvOxIDU719e1y+yYOH3pXGw+KIfme2LV+27cekD4r/Tb/48RX+Re5nky3Pxj0X5YfHnlGd9/hPI+4w4B9D9c7LABmDn2/utiPMfXzzqovdzO3f9H3/6K7Ju5LtJGjftP0X35yfhZ4j9+DIJCLzZBX9bLF+6faP512xLEDD/iiZg+Vd23wz1V7Qfnv070mmcg+z86ss/JfdnG5b/ufj5L3X77zZ8WASf33Z+CvKmtp3U/7T49REiP//gfb/5w99+A6T/j2T0oqvdB4UvmZ3Hgd+0X778/EPzuP3D337+oStBFPt29qWr0z+j+Wd2ffD5gwVfq378417A/5wneXHPF99yaPFrUf6P+rf3hQFgzPt+v/m0+H0mzp/lYlbiK9OnCX6XjQ2Q9Xd2/OntN4A/OdCme4DUDD//9m+LQ+zWRVME7UJ3i65dAAe3cebPwp+iuFmAvzNq1D6waxMDw77WgfifPTxLXASLX/6X+8D0j+4L0yH7hWxfXABtX55Q/GVe8uUBxV9eUPzL++IEyBd1HMY5wFyNPh4/53YIsHdmXdZ+49c9gCtnbP2PIKs/zj8Wcb745Z/k8OVB7L0cf3kgdPxEQW27nxGw6VL/fdbVjPz8pZkLypU/+G4H+KSFC4QKnkgPZClSUHLa2S5NEqfpwosBxoCyNT5oA9t9mon98ssvjt1En/MnZGOLZz1rILDgmziLjx+BdkEah1H7OffdqFj88OtvPyz+a/Hf7XoQn3kcQQF5eQZI+CiAINO6DCwDTgNuBjDy8Myvv71sDMiASroAfoyD2H9uBpGa+N5Xg+s8/RElyIXjA0MDI2dlUbdzJY3b98U+WHyTFzCdH82VIiqaFtTV0s89P3dHQNUG6nyzZF60iwaEYxOMHxZd4z+4/uLU9kPEDKS83f6yOGyPoC4VKfjfLOZjEdhc5DEw/7dweN4HROofmsXmK4n3hTzH5qK0a7uMavvFI7CffgH16Ot2QNxe5P79cz6XYX821SNRnuYJ5z4jdl8u/fjoJtwiA6jgNV95h69exFucHlW0/pw3rySw69kVLigKgGnYxd5cGv7jFVJNVHSp97AfkHSm9PKC9/LKIwa5v+xX9Ge/8sem53OHwgi++P+5P5q1pjlOYzj6xOwWjHzSrk9vzC3h7LVnFzmzASH5zLzvjctXcPqK0Z/zNAahVY//8Vz50Pi15ol7XQ1MrtHagz4IIKDzTPcR33O81vWcGfbn/GsxAGIvHsgHpAZgAJJljtGvDOenXyWNQMbP198bg0c8AOsDxUEML8rOSUF8Bb7vObabAKlmd311Iwh2f87XexS70R+0mu0MYgrQXwAhYpB1oGC8fwPo59Ovov9h47P/mbc8esMun308EwBy+LOAs0tmvwHx2mcHDvT89CAC1MjKdtbdAUkCNH3e9Gu/6uImbmfXPu3qlwCTP87fT03nu/5QgrwAxgLRX3bAuo98mYMuAwECZJhDza+zOAfVHhjlZYQHQTubkx+A66sdfVJ83H4p5D+SbC5TXzfOisx75sr/DFs7H3+PEac/CxNAL5tXPPj+faR94zbTnnGyAVgHOH59+mwR3p9V/tlGLL7S/fQPI86P/9oU9Kjb5z8GwKdF1LZl8wmCnrX2a6l9BygFPWVtvpXdj3NR/PjM8I+PyvzI8I+vDP8D+afmnxb/moh/IPFKkU8L5B1+h+dH0ivEXh9gke3HzfUjPj/9nGv+dygF7IsMxNjsvxHU+W917+sSUPzCGiAOWPysg81cPu+gYj+AH6j4Of99zM85B+pKHs4x2hS/w4JHAwDi/+m7b/UJPMpbwNubm8fQn8e2R4Y0/tunvEvTD28AAv1/dlybC1E2R3czT3ogj0BD1sb+48puvhTBFw+oMl/9cdDdgbvQHNQAfbPyVQOBKk0O+pSoeBTduR2a9Qds2rGcRXpOanNv9wCiof1Hwsrjh52+L15C/j66X6VpLs2/S8KnFYH1XCD9h4X3qC8g8IEVZ8XmBLYbkBEgGf5UlkeB+PIsEH+i6VxK/lBDAKZWHUjqDwv/PXx/lJQ/pfutuf1HoiboJGY6XvFpLqofXggGvsFA8mHxbbYA2rymvcd4nndgkP55nmtm1z22zD/AHvD1bdO3f5Vw/Le//ZlcD5j7MgfZM1T+Xjp5hi8A77Nx/6o2A+GBAF7n+i8z/JPJ/BGFUfIjTHxE8cfK91sDmpp/NB+Q84HeoAbOKn+35XeNisfYNmsELNA+/5Xh1zcQzUCU1n7F86vvB8sB2H1s5g4HAnkPGILrZ4aCZ/+3E8GLTBPZoBUFdFY4Gqx90sdRZw37trMOVjjhkHhABUjgez5FBh6JYT4WuC5MYp4DNqA4heK4R1KkGwB6z3T/Mndz8SwasaYCeL1GAxxBYc/zAxT3vBW5Il2CQmF77diEQ6xt5/vWJM69l75P/WZjfhtOHpn9VPvXNyAaWMnjzZ5+frbQGgE3KUcrnWVN+gWh0rV9tmN+1wvT4VZr/oRuPNy7LDeoEEbkRiqZNNYzUXN2+7prnZN6303sUWGWIzalRsnEIplRzsiQY6jKgiWb5XkZjPm5NXwCx/wtJ93cmi1d6hi5+C3YI+e9f2RiWd6y1Vm7jYrFBhzLxO54W6kQBOHH1VlMxdJnD4koXg5pUbVyggw5diG9/lK0Rr6NBsZqdaHnoUFJ7Xq/6qxuiCtk6AdP9sTaG+yDvnOolTZB0Hqt6Aa3NSpJUyI43ndeJ1EwEhyHQR44zXUaldmJ5XIPYRR1jrTrBE9Mt3J7TcR7ARazxNpEjN+epUMXw2I+bPAjLyHkyoeceBW0+WllTsgSCiA/ltZDk6olbBZbIjHNAT4VXeNtSfFkDoy4U4jbRiajFLqG23A6o7sbCjO6hCkWNVB26ADp7+purOnCHcxNfvEOl+aqcoQib5HlSmJofEIVHc/oGsbi9ERz5nC9iLsL55JH2m3urSfBXi9OOAZnU+ERTr0lLqLMaqqmxhZcXXmfxbtkCs8iacalOh3vmlzGrXkhU1UACl+y6ea2R2u3ahBMYzs6dG70gJ7FxEFzzEsx1l22thESU6TJ50Na7ZvqLDP96X7dx0gSaqWIbqR9sYpi8n4/5Sf6CDm1uJEl9Kxd8R4t3NqYUKPBCwm2fXMeekeZNI5YvF8bm9XEalc1iUmp3msqhrbl9ibC0vW+5YUNUV3uTjkxfgSMJcQ2BkvRgclphbeN7LxbIybChjbtUfdIsbXjdPKljInalLOc4nTCxIKlh7ZWU6RWRbi96XS6nGzDgfXkTMVredzfXKtCjO42TsM5kWC1hAbDYE85nugTTSBF4FAMhApwlanVpdhCmTRKIm/ziZzdcd7ohmpHBEZ/cymmjJvpYFGKKuBWl0dQRbn30c4cXQnCsxxt5Fpvj3agny+XvLpIqYD5BCndSPmuX1nijkwry4AmasnL2HoQussynDSlTNbLnCflFJcxu0ND0RbTtXbNNLN2Yt9Qst322KykQxVzm4u4ngq64PCxT67HodmQAW2Pg6hHIbyzBhc83nsMbNqX0w5HE8pSBtNytidZNtkDHxtsGpJhcxtl41TSJsyrxo7wo+1eWwoViJT7SYo39SWacP88jqRzmMI7tY4d9BhsVNzH7grZ+bZtBmbsbkhdvythWugHmtxagxIVpJKMNui7NgRWLX2N4gWmTqQqPy8l/XY2BN1ojD5qh3tWxYhFk44XCIVgQAepO9nX4GQfYDJmDj68LQaF65cssxP8VD3f70JIi1EfJ9ZwVUmjlVroRFfH+xaJVmcuL+VRnArbuuuDmBRRFdcY2u8xG9YUPWETVgxX2Yi74shyEmQurziKENGpgfCpso/XzdlsTHpLhxlq4UmChFuGNEZLJdVL6xqco9pXlfb2qnsVfX+91M7u0oQbPVqfTsddgHo+2wHcWK9ciWljbo+bAbPxQrYfqYOLbWCOl2+sClnmUsBvbXhud5Evm8LU71WmPonevQU5XspgSlDs8SYo+3uKngey33oQta/DKasva/tM3iK6gQKCNG1KhqzVmXHNM4cEvIYrIjE2OM6ur/dmhascVuyU6ZwZAS2eUq6zPTjYU5UxLNdiwG0i0kCTEAD1yh02+W5liVUoEXnvMXuEYoNLOYjEIY7WRhFKB5vO8gANIkcw9HtqHU4rX+PD84UZuSFxSs6TUXcoBW514xCx2B7QJnV7DGrQ6XK0Ekva1+KAR42TKoLcmYlS3jiGzE8jQLGrkuampo1MrYnC7nylXN3X03Hah8C27XLYmvnZFpq4obONgfZrhr0u486LLwENW+ei4MXojho1xZKdqRkcCTxR8AElaum2ltOidKcx17IAS4lVNyHkSdnmxpByfcP0+d03bEEb9ysS8Zrd9oZm3CHdTlU9QMmKQ/nAa/ZAl3KzEYOcP64JBzrlpJJPd8paLs2caqlDKa+yCifKJNhS15DetIl+D2mnpKRhe9siWIzEzWGkdUrZrRg8tMpqeZ9oxBhXWl/J8robCzm8Mooru1Gykkkrki+bI+0NJzrDHX4bKRsp4/aFezaQ4ZBtLBJEKaOZh3CwVjfQqXTusvT3pwNJghxD4tgyjC17M5nLpXBA5J27/eDVgyTZ2KQ0qr0ml1Iy3fZbN/RPB9+6J63U1Vc1SkkfVUOCvqq3SMJytUaoLVUpBuXdTPhgrdOdfma2O0+7AgTpcMVBLsyaOflqvM83OXF07O1AW+at3S9Pd24dHiI4yN3UOFv9nZJunFpuzIKR7KxG77UgCwdL4mPfGp1rVG/X1TRByBhnIq9bV8mu75U5DsI+clVEuIQAW6md0BOek6kRA2jGkqiMGkuP7B3UaB6XL4K7MvZJk0y7m33gx7W/t9jM3R+TtQTaQiQTTOIcTq5WbFGcRtougrVASrXYPZj95iIpdHGwLU2q8T4rPZEtNU4KM8P01yBq1C7yd8Fp22uMlN5xkMCSDil3g2JlVu+3DX4VEbyNCdW8qCuOHrbeChkcwsvIQuDImI8d0rmrp+VNu2LFeN6sd5G2G/TES4uUqvE64VY7SnIHdXk6JNX1to4unayX7DXesluviMIr6lUg2BUBPUjn0d5xS4qH+Ts22KpabaACD9hUHva7Spys9Gb7IheA1ElODTkaZ11eeiQaYr01DiF9oI5S4Kwb44bbArPhBSO9DLVObhVLPO62myovNrrb5wjqdo6Fe1S8tzRgJKqOgqu9lYQdldRqtUeViwQfEvjETJG6P2eH3bLXNHcsM9ttScZilLtWGuykp2SO3seg2RGFJDY2f0h01lwq51hhxzMM21LJrZzzZfIN/LRPQLczZHgHnWSck4RrvMkRrZFgNNHddLqnXAP5vXY2D84GcdOCQ24uejhvNluYOvQy6doEdL6ox4RR1fSeMdWkLa2Do/K3dV5npXCjIQBVwQo6ykbU6cbOm1jcahUVVT1yOVrGCTuqqyhZ4pZYZ7xAJeFKl8OKXpImd9kGawyTuUxYllWOR4LO3OzIO6l7ETYydasrRzume7N0RE0FgW2vANrtWf9snjL+hLEEDtx13WWOa1OFGqanbTGNVRSSq1ACpZ2FD9X+HNr2srClq5XjeJXU103n8at7e74UYdqasmj0l/2hkRprKcRSREahGrF1HBdX0pQVnysPpeQ6eX2N7EmPnHNVMJsxnCCG5Fetu0ob63zZAmz1QUWEldNlsx3uPColpnBW3HJTGntHZJzhBguU32MBhC6zNQherF/aWi5KBMscagFVCJcyWtmLqxZJN55jrPaWoisXchOpKIbHG9D7UkK3ZNtrr/rMXj1wAHn3AOS2QhOoApE1oLHhu4yiJRa5d7CdG+KFPNpduDZJtjyN9wus7ZjRqlFtf9zqFzfz9qUVULtMtp0yULmmo/Qe9PVQBBW2dz5Y7LXbMXHTr2AxsswRDWJMh/ft+kaJcTVRcIKcxAoxM8W/8Mfc0EbYH23Dd/fVLaqHFdMdvOy2O3lm5+ZML/FyzQinczIcPFm3gp6ZduX+Ti+pa06o6oUlScPcHmVtN16DWu5NOR2Qs9TQy/2Rbjkzbk+uXIt4iZ/dVBCEjD16mFNAgbdrXTk97SiriGGZ2cp3OlS2GiLFTC63S2TDFDflEBsZydJr+o5KWwGZNpdQWGaDcIhdZ7IbZ60HSqAneBu21R3LzlWtc7Fk46pN8AcMVfk0uRSyvLwquzxXT6VLnGN2d1LP6Jryz4NzWt02IrWDbL7H4SV6GAwwbWy8K9cdlcZzcDSnDEwxfB8VIfq0P1xieUtbCWIm+6i5bdGyYPX4LJVbJCldmRzGwFwhTdcak165O4Jfalbo1XKCHjlsJzEFtWOTiWdDuq0m2qBE4Uqf1tIumvZnk9PPBGpYfS03PCHHOxEuTchDI2xJpB0VHZx7DavshqNEsVOMo7La7FQJVihGvo66DzqLWt9KYZLROM25dpkKRAK0bHd0ciV79Zbder4R605GRLoOKwqMPuz9hG5Ao3MSleMdXsuNXtu386nN0vtxKyr6Je+y041BppJt4aA5Kf10o2ou2dCjnerpJZMnHEeV5S1mz7k8MpRzlu/3mBTV0B8v8PaawJeiZnM90+Kav3FaYB3vCWl13GieyRNxLFtkatr7ClqpwCUERCeDyNwSuMpPZat7DaLw1fpUcw6xuycQ0o0oKq5RjewGCwlX6hj1enruGQ1qSWxzsfLO38RbjBAwc6BoghocisLQDEwXY4MgvSyTNWZ152UvoBTub67GBTKqPqvDFWdD4mnd5UqHTMPqyHXQhdfytqFGBRieouqp21exigUn5YaWGCKXJ993s9ulOakEfz6KxarZ+3xuVI2+4m5VNbYkTHu1tu4uFg1ZbodhFU4aGnwZaN8vbhftsg8IbVXUqjnoB6hUOW48UhZwFqNXceUK5L7KULjQrMsE8Bnj8Yb3/KwXhAHxHaw7GAi2B/lamW5LieRR5iyfgtDVcNxpKLfaxPyllEP7sCEJedmsIWiDQckRTjgvM6Egc5ayT+t4ANd9SgRxPrVmTgsdv+58QQcQRjR2aB8PZEDu+9YPDhgrLiMEza5oXJeMh3FcmsfHwj6qvHAIupS4EhCcXTGuNvNhbEiXJ29XLPJH5+57EQnjV0HW2xHi/euBuGUTk/HYbq/wa42s2dRE914ihXhZHASmVdXjmCMIghGGeVI2YVd3zHRUUHK0trvOVPShatxzEGsK28O6t0RsEz1ObH/olmJ8va782Cj5iBBva1+BDWnZBN0dDYRcY6+qJtCyLtArP+hQuaPECR/aeN9uKptEeJPOkeIcmZSQIXWJmizubVv/ULGniAxXFkodbiigVQUreuSjHI8teL0ersVytTbzaHNBN0ytW5wo7XMWP9zgFlNjDrRbYDz1D+d73/cOy/rm6ZYRzY7MLCXb+gkVa4e7oSh3tsWrnotq5tT3bSJc2EbBAxq1DnwtjVh6SIhzAS2NlqQ8aLmkoB7d3vnVobOX6urOU7zVh72s1rh3xYwzRWSbZYR7LILoV4i0dobJtdmyI1Zm4OMErUR91JU3GLKVW3faTozh3xJ+Z7nTnoLZosvOno1ZNDWOt5HxncvpgHmEdWGLulDQk0jYK9yRA4FWLeykcf6us7ud122Vpg6lPo/XqFCRK5CyrTlReua5NjpAcrjL+gOKwkciK4RJVcR10VCwOR2RTasTbFTx7GrkNzByk+BlZh4zw6W1zZnFbNOTsethO26gNQ/p7qmq4uvEh0jjEsbmLK3lfXBRkTjFom1/peE1FYDWgNuRNkJhlEKiuZxNK2yq2s67Vkrg3fIIUaicb2FDt4A3sA1rtp3NylNU91Yg8Trfn9fEXu/rICD5ksMhl2y7Fd5Ux5bzKPlGFQJK8qAyXo6lXpGqDoXeVa0a+rxEXMuDuMGDfRKrmB1feSIyuFF9Ug3qWPhZ4mod6WIQYW8I4+JS+Hq7CSx9YyRiMTYlHiJqX2PXyNldBQ01Ibni+8tNkS7p4OK011dEGa1cWNTWBY/u1VtuEWSqRhEksMeiOiqgzlxJl1RvQdqEAp6LJBLCvW4ewQC15PedzEDYMU5gLPaHsYBYdEfYhGYamJ5G0SFfwgbGYV4IoTCN0uuwDi/yXd+K2Spajt2dXiES1tzXN9pFDb4bQ53l15CHE1AQ13Y7iutxG64VtKE672gLbenvUr6tNefWU2lTXlIYc85tnh8aSkQxx2QvNbQFUZolVs0fjsMAGveVlyFRfZaFfOi4dUQoGz9H0ynPaxEZHeHCrbUMpljjQqLH5Zq5ero6ejzcEjzVRscAYm46OjamBtXTht3maeMn+A7RcJbVasIi5WvUYp4+6h1D+Gawt60pkUuer/1hVWHyAbPR3Ed2mRjACJgedQKKDOm+JDx4ubr6ClQexmpo91pipDGol+Sel2iBvB+4xGXb5RoiAoQu7zfYQEo49nHROBB2dId5FMU7BLTAXZ4RaRBcc6k9bwroSC5NskQSTMqyY96RISp4MDmlQsUdBa+wWQ62uWrDBTsLracg5RsYxSpp3E/q+mB0jd86E0pdSWp7IfikvW1ldnud5LxQco+hsmgCrJh2qhT14u45RTeje8SEvanEIADZfJxoZafWLieplCB3WFpPKMJx1jz5p3JEQgPGS6bntL66W5reTnN2vHnEW5leW1ejr8a4L3N8BIL32Haqp8pB1m0HG1CNH1foBSLrbtioFgSZodxdNlhxOe4rx7uzBxnLz7WP6StCFwuqLCWbgNfZivCO3iVzTxp0y1e1gNWy2FoCtFtfueVwoXKnk64XZToexJXWlxnfrm7cJT5iy/XdK7Ndy0p83aPrvQdm2JzoqSY9kM7yFG92A1MzoUZjbpW7VhmK43ZbUsV+Fclr3XZ5b6SqLL9d9LAhXG3CyvzehfX1BCcANOqIOu9IXdvZN3dcElcs12gHWw7Z3cHBGNlBFOvXknrFhmmibifJJ1P/NBYYsyvtPXbpiGBz0vlJCmOsE9jtxQVNOUm3EW5Ld6rOnJ7HEJw90tiev3USPFC5yqLweCqOtHjFIJZn4WjVsFdqtY3zqtXWVjrgR2hjg5G40RBVpem3D2/fD8Pe/tVXteaDl/9n5z/Po5qvL2U8Dvt82/v04PXpX5bsbx/eajcGcj1PvJq0C18HQ3933vXxnzy9m4mMz3ehvh7gPs+cWzuc3xp+i3Ova9p6/NIU6eMFDbDD6Zr5HcNmfg3VBd+/P7v8g0ozdb/uY9f/0hZfXu9Hvs0vAs6vX/hePB9FPy/D12nghzfv9crPF4wkvvh1OSv9OuEHumLv8Dv69tv/BjS4iz/iLQAA -->
