---
name: "rar-cowork-cookbook-adaptive-card-process-customer-refunds"
description: "Generates a read-only Adaptive Card JSON file visualizing process customer refunds status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_process_customer_refunds", "rar_sha256": "4d65203c89a0d6049c25283f4084206be8cceab217c47b709702c38c1516d55f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_process_customer_refunds`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_process_customer_refunds_agent.py` and in the RCI capsule.

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

Process customer refunds Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing process customer refunds status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-process-customer-refunds
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
      "description": "Date the card snapshot represents, used in the output filename and timestamp.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-process-customer-refunds-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_process_customer_refunds_agent.py` and embedded as the fenced Python below (sha256 4d65203c89a0d604…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_process_customer_refunds_agent.py` first:

```bash
python3 adaptive_card_process_customer_refunds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_process_customer_refunds_agent.py   # or on stdin
python3 adaptive_card_process_customer_refunds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer refunds Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing process customer refunds status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-process-customer-refunds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_process_customer_refunds',
    "version": '3.0.2',
    "display_name": 'Process customer refunds Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing process customer refunds status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-process-customer-refunds',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-process-customer-refunds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6dfa7476d5fe1855',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-refunds'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-process-customer-refunds', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the card snapshot represents, used in the output filename and timestamp.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-process-customer-refunds-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical process customer refunds status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-process-customer-refunds-2026-05-24-card.json' that visualizes the current state of process customer refunds. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current process customer refunds KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing process customer refunds status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make me an Adaptive Card showing process customer refunds status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the card snapshot represents, used in the output filename and timestamp.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-process-customer-refunds-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of customer refund processing status for Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardProcessCustomerRefunds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardProcessCustomerRefunds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the card snapshot represents, used in the output filename and timestamp.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-process-customer-refunds-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardProcessCustomerRefunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjSJblX9G8NpvMbEU8VoEUbW02YhECAWITEmSURbKD2Fchsuu/jyPpRWZWZfVUjc2nUSxPgPv1u55z/Tm/vjl9F5fN25c3PXCKBedkWRIHzcIp/AVd3somBT/K1AX/Fl5ZdE3i9l3ZtG+f3vyg9Zqk6pKyANO5oAgapwvahbNoAsf/XBbZfbH1HTBgCBa00/gLQT/KizDJgsWQtL2TJVNSRIuqKb2gbRde33ZlDtZugrAv/HbRdk7Xt4uwKfMFcy+cPPHaBUasFrv/qdPS4scsiJxsERRd0t0XJ13a/fRpcUu6eBGD9YPm0wL7vFocFH7RgSXbT0AxbcstmvL26WEe+hlbON6s/gLY1JVF+w6sCkYnr8Dwty8//+XTWwK+v3359c3LnBbcevuwZzZHeepNv9TWnloDEZlTRGBsdQeeLcB1FTRh2eTglh+Ei9fVj22QhZ8W//7v6c1povanL1+Lxevz9W3+o/XFoouDRVc6bRf4C8+pHDfJgK3vi212c+4tcFTXN8Xs8RYEpojenzN/k1RWi/+cn/34XOQ9Crofv76V1RwpYPfXt58WZQPWa/r5+/sspfrxp/esvAXNjz/9Jqft3WvgdbMwoPX7t9f1SywY+NvQJFx80xWWfq3VBF5SBUD47+ybP0/VX+JeLvn2HPxjWX1a/Lnk2Z7/BPo+U88Fcv9cLPABmPn2fi2T4sfXGk05BIVTeMGPP/0jsV4ceGmWtN0/Jffnp+Bnsv34cglIwTkEf1ksX7Z9l/mPl61AwvwrloDhH8t9d9Q/kv2I7N+IzpIClOlHLP9U3J9NWP7n4ud/aNt/N+HTIvz6xgQZqJvGcbPgy+LXR4r8/IP/280f/vJXIPr/KEYv+8Z7SPiWO0USBm337dvPP7SP2z/85ecf+gpkceDk3/om+zOZf+bXxzp/8OBr1I9/nAvWPxVpUd6KxfcaWvxaVv+j+ev7wgR45v92v/2y+H0lzp/lYjbiY9GnC35XjS3Q9Xd+/OntrwB/CmBN/wCpGX7+7d8WUuI1ZVuG3UL3yr5bgAB3SR7Myhtx0i7A3xk1mgD4tU2AY1/jQP7PEZ41LsPFL//Le4D7Z+8F7pDzQrZvHoC2by9M/vaByd9emPzL+8IA0ssmiZICgK+2VZSvhRMBEJ5XrpqgDZoBoJV774LPoKg/z18WSbH45Z9b4NtD1nt1/+WB0ckTAzWan/Gv7bPgfbb0HAfFyy4PsFYwBl4PlslKD+gUPtEeqFJmgHm62SttmmTZwk8AwgD2uj9kA899mYX98ssvrtPGX4snYGOLJ621EBjwXZ3F58/AuDBLorj7WgReXC5++PWvPyz+a/HfzXoIn9dQAH284gI0fPAgqLM+B8NAyECQAYg84vLrX18uBmIAoS5AFJMwCZ6TQZ6mgf/hb32//YyuiIUbAD8DH+dV2XQzoSbd+4IPF9/1BYvOj2aeiMu2W/hBFRR+UHh3INUB5nz3ZFF2ixYkYxvePy36Nnis+ovbOA8Vc1DwTvfLQqIVwEplBv6b1XwMApPLIgHu/54Nz/tASPNDu6A+RLwv5DkzF5XTOFXcOK81QucZF8BGH9OBcGdRBLevxUzCweyqR5k83RPN7UbivUL6+dFUeGUOMMFvP9aOXi2JvzAeHNp8LdpXCTjNHAoPUAJYNOoTfyaG/3ilVBuXfeY//Ac0nSW9ouC/ovLIQeUftS36s235Y+vztUdhBF/8f9ElzdZvOU5jua3BMgtWNjTrGZW5Q5yj92wq5wVBaj4r8Lf25QOiPpD6a5ElIMWa+388Rz5Mf415ol/fANdrW+0hHyQSsH6W+8jzOW+bZq4Q52vxQQmzFQ/8A1oDUABFM+fqx4Lz0w9NY1D58/Vv7cEjL0AYgPEglxdV72Ygz8Ig8F3HS4FWc9w+4gmSPpjr9hYnXvwHq2aPg9wC8hdAiQRUH6CN9+8w/Xz6ofofJj67oHnKo0MEQQ6ahwCgRzArOIdljiBQr3s25MDOLw8hwIy86mbbXVAswNLnzaAJ6j5pk24O8NOvQQWg+fP882npfDcYK1AfwFmgCqoeePdRN3P25SBVgA4AOkAZ5UkBOB845eWEh0Ann0EAgOyrKX1KfNx+GRQ8im0mq4+JsyHznJn/nwnsFPffY4XxZ2kC5OXziMe6f5tp31ebZc942QLMAyt+PH02Cu9Prn82E4sPuV/+bsfz47+2KXqw9+mPCfBlEXdd1X6BoCfjfhDuO0Ar6Klr+518P8/c+PlV6p8/Sv3zq9T/IP1p+JfFv6bhH0S8KuTLAnmH3+H5kfjKsNcHOIT+TFmf8fnp10ILfkNUsHyZgxSbw3cHbP+d/j6GAA6MGgA9YPCTDtuZRW+AuB/4D2Lxtfh9ys8lB+iliOYUbcvfQcGjDwDp/wzdd5oCj4oOrO3PHWQUzHu3R4G0wduXos+yT28AC4N/ds8281E+J3c7b/dABEBX1iXB48ppv5XhNx+YMl/9cdvLgLsvAgQGtAVoUuLywbhzKwSsfvDo90bmWVgPu2btHrbNFQFAPK9mE7p7Nev83M/NHeADqMbu71c+Pr442fuCCQAoZu3vs/9FYTOF/65In24G7vWAeZ8W/oOIQGEAdWbL5wJ3WlAxoFj+VJcHlXx7UsmfuGImnT+wDcDcugdF/2kRvEfvD/L5U7nfW+C/F3oGHccsxy+/zOT76YVw4CfYtnxafN+BAGtee8LHJr7owXb753n3M8f2MWX+AuaAH98nff8lhhu8/eXP9HpE69tHtP5eO3mOIYD/2bn/iMSB8kABv/eClxv+uWL/jMIo8RlefUbxx8D3awt6n7/3HlDzAe6AImeLf3PlbwaVj73dbBBwQPf8VcSvbyDbgSad88r31+YADAdY+LmdGyEI4AJYEFw/Kxg8+7/cNryktLEDGlYgBveJFQpj3nrjwD4B4xsPXaFrLMThNY7ChBusPS9wXBQhPZx0SXhDwqiHrT1khRD+ahUCeU80+Db3fMms2awWcMhnACjBb4/BLf9l0tOE2V/fdymP4n5a9uubS+Bg5B5v+e3zQ0MbxIUuojs2F6iAl6N29g9twsYjXhhHSEME0k6DzeiG+JR2gqwdDZUXpVxWtwy1rYSVbDeVCqnC8m5g/prs8bKPBKbFXK1WFPpAYa5cTMtwKHbIqrj6eEYEMbKr2Uon9cYbd2LmZ2yejWak7WrvYhyk6ODrxc6zqT1ebSAI9/GDdrQp/HLiWybihTrX3am5KoOB+i1m1WZy0AlTLGULcjYHJOHJTrBQh8DuPt0d/TS/mQ57vmDYpIsTjvnF6EzcYWXUfHy6HcxgYn00GC74rcDT0uTIPbW8HsLksMyvawMa9m1GJ/dKQJl2c8zE1PEvSyFm8X4PH0aOjU+l0ep3kU9RWBmjdRgW941SiNVyGRb4tXA3RBj2S3EzttXtqlYtj/P3/GCsGsM7tMiuNffRsU3oymoqzsVNbjfmfbllO2CPGEoRNsHoFitCP4q4jNtpqytP64QvKRmt7leyGeubYKfT3gpv2KMfcYlZCRd/exTzc58EEs7o61sPJ80qSDockwxii2xiNBpsjU9LS1Nvo1rfJGsf7PDeGs+HzDY0KYqGG3WsrsrZqvj0RJwqzzV13AnQvSBgQyJa2y3RbBuiZfmiU/pJGfbSsnPM2LZtPr/vI4Q16W7ap8RZYFguyZkNY/FJIlzg7Qk9cpKD75fuzjUq29yWrsyuM7FYt6bm7BzN5OGlbdgBeQixXPQFZmlwhqWycXU+a5nG1MvJUCmz8Ha9RTGpmtKrbDAd8XY8Gr5E7iIah/eeOh1LR2YZoi78pNWZIxKZl5hO8Rji4nVbnjkUSRg7OXsrc1tzXeuwfWZR56x1bmyHkqCVT07X/aEpVCtSLrVM1p00MrSfip5nhbEjEew6rEy7CvGdT7SeBklGbai6EETXJRIFtGAVHp+rsKi0GMIxOuSg3Vq42rs0KGzY3PMsLJHTDTJIexeb1HqHdMei5XelUyAEUYyEU6CE7o9tkFjLq7vOqaCVJIjLoDUFRYwPdbGdQTBrjRu5wOAlNLYDVZuTy1IXDe7T8y41HRQvMqOPbiaSx9fNXdVcKljdooHj7wrLK2g7IuttvRwPxyyCRW1Y1+ONvWuNlCa+HN+DLj2i7lXlJDjXO2rrNCuQf3CgnkWCE64wi3m7BDfHTatRyqict3K/r7ytbKzPLn3HpTafeFLbJKM87QdWizIsIiDZr+3jYJ4OWa7qsX0W1L4ApWeCgtVbj0/1bEMVW8hfw9dK3K5QmgwlgThzSRnBbGOJEF3rsd+77VlxkNq326oLKa6X0cBnspNhme7KJRgj55nES47cHZEiCRYG/2jAk2Wzy87UJAalhROHani5D+Dt0TzxdyO1DjgWeojNQYKG2Ccaj2s+lNuj6HuxlkDGIPmk047VUiQAMgqt2Z70QQxYtUdtiy/ciNkTu6kGuNI7l2G6x+o90XQ1ZqPTRp7IrJ0Ih8rKnVaF6+WkYniFmSF5H9XAxShHiyqABujWXYve+r7e+2HrUHuKmIa1SIoi2zl7bunQxnXY4oczxxKx0+92961fy1f1Ilj1NbmGmps5O5dE9L2dS9x6jexiamcwN2iPBPe02EzlGNZSxNf9ObtByDh1EjF20tS245UrYjHgVkdvEGxCjD2YnMgxGAMWtLMQlwvlJdC09JrQ8tobjxTFTfmKl6GpyJMyCxqDbniotovTca9fWXvKWGGPIgctjAk/OnjhHu8KbFv2fOrjbG8V7cB4hhY3ln2+qapWj4mLLDc+jh2kJc2P6fZMFRUjnndHQerrhE3LVXak1vbJ4uLhbHcrgd3G3hbcvPB5antnm6XT1sQwKbgRyVmozJQqs+66ERIYvx7xWoP4jbaNCi6P16jM4FzdX3TAzloXuygRY758v8cHOStoQqGPkQeFhbkOJcxeryviqN51cqdoQqiUcAknPXXNa8NV1HKTxdFOuzDpOIBdDqsvc9zyu6N04HwVg/UGv218aEnbRCcIIdQFV23j9CStD0knrdeoQu1K/UZ1uQ7hR3cHc61wMi+dWQOuuGm7c0iWRsLlSUNeeLrJLxGz4WEMJQ8RKUbRFA+pBCSV+c5EBTxx2XXlCn1726ZLg9jzvH46GZFr8BVyl6oIGzPmiGprWtNPtzxP1TjPhXrbFMzhTAi7kfRlalwRo9rW9e4+Foyb32wkPx4uJytA2jjO3K5QXS42UTQg4xYCsMzYSkWPxr4jL1U5RrfVBqfqczKu7nfUssJkoPbdUjE0uyhPEqEvVds57CIV5TabAfEYSetWlDoeaWVtwvCq3t5l3tK8zva5vcGUkByZxpWEdPSyK6mC0mumCfAGwcvtkhJvpjuqvU7kvDUdAwVVBKu0Tj3MyjYkpl6r82rNyw6HV8eLZLPD+sKhtAoI2zvs0saLGKB/uA0qHKKayGxuumduc9xz9WidFzpH20m5Iya8vJ/qFPfqa6kLEzVFJcuZcov2Iu5UCrc/YFG9u25PvRBpCb0WK+ciJRGv6ni1F5WAtInK2DbUsMIJWKNXHqcY/v00aBk67FRENm/nq+YFoBD2KiwhkbRlNM5bI4gNVzRV85oTd1nv7ALWUYruYEThzdJ7nUPQ7DQOgnxu7lsNvijr8WYyiHRP6qiYDvV2J+XmmR7VzOEPnJA7ucZQGnfXWqDcOJjWMvWZkKqptNwtSXcDs9N+G3p6flU43N7tMUl3ErHSVK5AyPTkkIR/0mgsjuPez1FyhR/ykUhY5mh6PtZFh3rHuI6xguutc9mh7lCMyyDgAlLew4pwLXbGoTEu6t7yvWtAazmm32VXkNg8JdI7zTMnuASEOjp2mjVOuxu5jDeT66085L2A73PyBlk0UTJxyx0tOk6QG+p78o7TUeeo1H3qropQPfFW0pigm43FIZ0C6ro9rHXpkMh5kMMJknbHRHInGAtpbTu2hX0/q8vKjW4AqC3eUJwWtTdtbrredssLNK3fmqqojVUJwZxcM+NGJ4T03uIuLiyh5T6d1LZDjVIe0oALx3HD74MhxVJdXTlK6Sv9UTuwjlosVbo6BU6TjdXdDnWQBmMSJraPnoTDNtbqDF7yFGiC71QUX09t0mTnC6Bbjt8uUaGC2aDi+gN9ma7pivdcda+nHS3AO267Lc9MnESJmwsqs0pALZ+o8xKQsm2iUYukFGN1YzE5LcvCF1KML7y6XIqsJWu5fruKGR0LqjjVZyEjQEcxjLxV8L144BKRcwbKNBy0V3ebkr22w+ieb8a5Xu+mw2iWnFRL2MrSD+kAOavL1aJXZ7jFGLtcx4PDDHeRA0x8syQvpgizdFWWXIWn6rYOFWXMlz2jbY77iyLQYw6vV8g1jQn80riEEpvR5UjXU71at5FYFXGGxBcPb498F2ZZcwuxJObIEbQCjI2b6lQeRXZDlbHhrqwqi4J+d6fRa5Mr6d09KU098ee9xI8nlgr2/p06E9POp3R6Ys317pjCh4Fo7espJy4wlYkovIdibU8OG067SGW6y1dyfhyD6wn0h+HBxkP6uGWS4aKlJooFKae75rmGRxGJJxVxW9/i8+kax7utLwdKZBh7u0yrfWNt8pYTnFWrhvSy16gYnoQdsdQlGr+utobRiEJygi8ereu+WFn2amPH1EiF9EFLDhkywZshkQHTHZKdzMlyx+ibaSeJqMvxKqvyGM2sbhpaFSpohIRlzbOEPdaO5lv6JnJ2yWDmrXW4CaFeg2UazSH92D6E2aR6dSb5g4nCt1xMUSeNuxXNMYOctFEq5D3uKR5oJCDUMTOmuqe1f9mOA3HkWVK8365IaFAhxGHwzWMclVb1aznw90Y+Bud23VwsnINsuVlu94R8YR1euxqCo13ZGy06V8F0qGUf6amgrV0zOm1lgrE9GZluXSlGklTaIWhrMknJUUhkI5ITd8nxAOpKq3f+nT3FW8w5F8xxe0E5DZ7UZhMaWruvZPyslUTP1TjomjYXbX3QXWZCD6uS2hZXUwio0dtmDKZFd5EMXWvb3o3lnS5Vqi95vOo5UR/5fFPD/MYgVyh6aXa9XaCDKbYF5CLXq5kTUUWuEAg6lWW7c3ebi5ey62QjJTiyOVTN6db5UQJgEjJOOofl0VFnHGFK95R/LxBaiY0258/GYXBdSc2KQ64iU4NrZdPwFL+kObCdwFPsgNsczcG+pFncLhRc2tEodyP1qmM618tyUPf8bhmfdma2bsNUsM6eS8PJVeV7TOGcVOo2lsNV90itZRwb3cLgkkIuitI/Y2ef6yQHCc+k6JWb6SZp8P1gmdIZUTT1vNF3VAVj1zWUhS50CWvFcbOQvLk9wUWw7EfH7nxd0z6/c1NhiV0KTdmukiILwiEbmH7yg+mS+zGOrLC9qXn+1A9n/jQgRVqNx5iSz54S2Ps1W55ye7d0pNo8klA4UhN5OhjcklJctich5wyRhThoq/4YXyJjHbWKpzd10yvrbC3QlmxlElk6nKDvcToS2b280psxuVBIz+ZkzbfLDncHC+OG64Bk9kHt68nbVDmsmIm0VA5IioXneGzv7jEiThyDO0sC3lrIfbnXFW676VAo8CCoxEP1YOH8RrpfoPU1jJsY4Swahe+bftvcuzPBml65360OTbbagR2bqK6peAWroaEufaXe20yzOW5l62KyZGPKhsiG6i2MAt3CZHEar2Qljb183iine3v3SKewMAYodQv8mIDXlk23mB1mg8R69rRKJnGKueN+468OB2cjR6Rj8EsVtnXKYpRw0giCINfdLTUqd+LISDLIrpJy/YrROwFHzkdRQdhCgsiKg9yhdotVixSXy15raV/RDudr6BXaMimrlbds9qQkK+trKbQSn0ZslUaeMkB77uLn9lqFx5MHIIZA9mdmjzSn+EwKudnU6HkFdbQcHD06uW/Us0TauUYqAEBEkpa0m710OVcZxAJXq/ug0Fzf6vI5TVST08TpZu0rhtUTqfIimDlyhJO6F+RmYI0GZ0bR2X3Nr6PprnXWiROspOPTgRsHzhgiPbP3bBlgLbXGg0Jk7li811tCD6ADsl4fmVjdQNikBgcSHnaNWmeMoReDWnC1iSutU8r++kpBW1xZE0QlKRs5xgS7sdodGcYTiWY8BSPrcXP0tEmD/TuZ49ca9iLcFXObCwZ5Bd+T5j7ZZM9IimWuuiXnDjdpwqbLRc3aDHE2xC3RvAovb/3xprSVulxzWMAi5iWCwl1qL8XDkVgNZMhrsDPp5z122i6d9dRoWugLmnGOvLDR7CY1jf2GRisvjus9692DfTlwlxLx2kDCPCqhy2NfSaSzvFm7lFkSylKtc+3EarlCYR5+b4jykpw1iIsbTlRArG5UlSGh2YrchnAQcsUc67yQOVjHpkK5qPBlr7TTBDmZP11RwiOOVuAimGm3JC4bezy0MGyzhTU8ULhgiWzMla9TAriHIgjB7+RgKq9NmIx5vt9XoSULQb8pq4h2l9d8KzQ3WT6h8MBerX45mA6yn9i6ly08MU1YkuOJZroKOzQ9xkvL5KB4srVRDIg/Rm6UrjTKNlZizQSDfz223M25ShXqngd9mSyPl3ibdGDjffPSfHM8OdpGFfEwVuRpQuiY26+3h4txWtrSVsVPHuHV24NzuZ6PtilWTRDp0rFiINHqj9yNC7Oq61i/MYW1ax2zJhfug32CPTOFOjMYfZLE/I6Rb5zT4+rknbykOpZB27ScslEj0srH5bLgr6JwkejrZqm4w/ZsY1rXnVeVt6pUr3HPHeaEjtCVYYI0MMLXo0Lxt1ODLp2uMvPr8dxlrt1N8okI4b49ZSXnbDBGSkN05XJ2p1qIcbbWZNZanDw1Eopx9dlfQytR2qgEUlk5PrVQs0X4kxah9p7XISaYXKohV1ufcQ+jLS4B0JzYvagi4q1Ii9vhkF90AnZWwAvdXlWLliXj1cTB5/W07hKzOW8Ad51JwLNKxuTxANfJfmgljGgyPgx71sha6BiccuCJvUbbvG9t4aK3t9MqtuUtrokxCd2HocHApnAPdZod3pt0nw37k9S6YbfKDj5PDG6GdCsDOu9iQ8DDHdshE4b3hSl4aIww6/Oy7AfDO91knbQmUb7dpFyVfYOAm6t7Fddwj/njirXbMN8bzb7R15scVZe3bKkBw25XTc2lySKYCtN7EA0MQynRAztnpU8NhhdD78pui/PxrtOrYT+S6mGrkh43QaEg91heGMWFO5truD0WRw1djleFOfthF0QKwfuM5jK7k2JVCk1UWKMwxqFv3MRZrlOo5owMQeQaEjGHg5AMpXpsWomQdVSty/Kqchg5DrBYRDe3wwtLboQSXXUZcktNajSNM+jszw50dzhyuOlj0jfFWpRQJM/OLeJGmzM1XGrIc827mxC8vYoviULYsRtyFnU+QBAEB4x4LK7sZYBMlNhIp8t9eQ+bjSDI1LpY09yVh1mq3g0rmcUNY2uyuJPW0XDDB0c0Iqy9+B6CI/hhx1DTfrAZxe62KM8hW9jbb1IIbGnkQpoaLGV6LlEuzebqZ2h8GEgfQsWNw6gqNk4TeTXEgMgCI6kwFnS/PHbpVyHl6sWkxLs+TPpdXcaVDVMGE2EFaDlkKBQH8S4tGS/yj/xgXKCMvpCakOm3s5kX6x2OXgPktuSUtj/ttEYx2P44kuv90q1sF9up6nb79unttyOvt3/xva357OX/2THP87Tm482Mx4le4PhfHmt9+VcV+8unt8ZLgFrPY60266PX0dDfHGp9/udO6GYZ9+drUR9ntM9z586J5teH35LCB1Oa+7e2zB7vaIAZbt/OLxu2H/r+/njyDwaB67LxgR1dCa7b+G1+GXB++SLwk/kk+nkZvQ77Pr35r1d/vmHE6lvQVLO5rwN+YCX2Dr+jb3/93+ggLtvvLQAA -->
