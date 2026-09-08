---
name: "rar-cowork-cookbook-adaptive-card-define-warehouse-management-kpis"
description: "Generates a read-only Adaptive Card JSON file visualizing warehouse management KPI status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_warehouse_management_kpis", "rar_sha256": "a33e7a0f7adb8b989bce268d7377b969e5d804c3f778737568baf5fbfa99de05", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_warehouse_management_kpis`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_warehouse_management_kpis_agent.py` and in the RCI capsule.

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

Define warehouse management KPIs Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing warehouse management KPI status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis
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
    "legal_entity": {
      "description": "D365 F&SCM legal entity to read KPIs from (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-warehouse-management-kpis-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_warehouse_management_kpis_agent.py` and embedded as the fenced Python below (sha256 a33e7a0f7adb8b98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_warehouse_management_kpis_agent.py` first:

```bash
python3 adaptive_card_define_warehouse_management_kpis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_warehouse_management_kpis_agent.py   # or on stdin
python3 adaptive_card_define_warehouse_management_kpis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse management KPIs Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing warehouse management KPI status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_warehouse_management_kpis',
    "version": '3.0.2',
    "display_name": 'Define warehouse management KPIs Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing warehouse management KPI status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-warehouse-management-kpis',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea2dadab3875024f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/define-warehouse-management-kpis'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-define-warehouse-management-kpis', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to read KPIs from (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-warehouse-management-kpis-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define warehouse management KPIs status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-warehouse-management-kpis-2026-05-24-card.json' that visualizes the current state of define warehouse management KPIs. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define warehouse management KPIs KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing warehouse management KPI status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing warehouse management KPIs for USMF that I can drop into Teams.', 'inputs': [{'description': 'D365 F&SCM legal entity to read KPIs from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-warehouse-management-kpis-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of warehouse management KPIs from D365 F&SCM to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineWarehouseManagementKpis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineWarehouseManagementKpis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to read KPIs from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-warehouse-management-kpis-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineWarehouseManagementKpis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6ebOb1rbnV1GfV9VxHvYBSYDAr25VC4EYhJgRSHHKYQYxikEM6Xz33kjn2Mm9yevO6/6nZScSsPea12+t5c2vL07XxmX98vlFD5xiwTpZlsRBvXAKf7Er+7JOwVeZuuC/hVcWbZ24XVvWzcvHFz9ovDqp2qQswHY2KILaaYNm4SzqwPE/lUU2Lra+Axbcg8XOqf2FoMvSIkyyYHFPms7JkikpokXv1EFcdk2wyJ3CiYI8KNrFQeEXTeu0XbMI6zJf0GPh5InXLNY4ttj/d313XHzIgsjJFmB10o4LUz/uf/y46JM2XsSAf1B/fBBpAbvm40Lbsou67D8+FHO8WegF0KQti+YV6BIMTl6BhS+ff/r540sCfr98/vXFy5wG3Hp512JWgg7CpAisd5mP30Q+VMlslcwpIrClGoFZC3BdBXVY1jm45Qfh4u3qQxNk4cfFv/97CpSPmh8/fykWb58vL/MfrSsWbRws2tJp2sBfeE7luEkGFH1dbLPeGRtg5Lari9ncDfBKEb0+d36nVFaLf8zPPjyZvEZB++HLS1nNbgLqf3n5cVHWgF/dzb9fZyrVhx9fs7IP6g8/fqfTdO418NqZGJD69evb9RtZsPD70iRcfNUVZvfGqw68pAoA8d/pN3+eor+RezPJ1+fiD2X1cfHnlGd9/gHkfcadC+j+OVlgA7Dz5fVaJsWHNx51eQ8Kp/CCDz/+FVkvDrw0S5r2/4juT0/Cz0j78GYSEH+zC35eQG+6faP512wrEDB/RxOw/J3dN0P9Fe2HZ/+JdAait/nmyz8l92cboH8sfvpL3f6zDR8X4ZcXOshA+tSOmwWfF78+QuSnH/zvN3/4+TdA+n9LRi+72ntQ+AqgIgmDpv369acfmsftH37+6YeuAlEcOPnXrs7+jOaf2fXB5w8WfFv14Y97AX+zSIuyLxbfcmjxa1n9t/q318UJgJn//X7zefH7TJw/0GJW4p3p0wS/y8YGyPo7O/748huAoQJo0z2wakahf/u3xTHx6rIpw3ahe2XXLoCD2yQPZuGNOGkW4O+MGnUA7NokwLBv60D8zx6eJS7DxS//w3sg+yfvDdlh5w3gvnoA4b76D4j7+g2Xv37H5a8pQLlfXhcG4FLWSZQUAIG1raJ8mVcA3AYSVHXQBPUdoJY7tsEnkNyf5h+LpFj88vcYfX3QfK3GXx6wnTwxUdvxMx42XRa8zppbcVC86emBEhYMgdcBdlnpAdnCJ/wDkcoMlKF2tlKTJlm28BOAOKCUjQ/awJKfZ2K//PKL6zTxl+IJ4OvFs8Y1MFjwTZzFp09AyTBLorj9UgReXC5++PW3Hxb/c/Gf7XoQn3kooKq8+QlI+CiKIO+6WW3gQuB0ACoPP/3625upARlQXRfAq0mYBM/NIG7TwH+3u85tP60wfOEGwN7A1nlV1u1cXZP2dcGHi2/yAqbzo7luxGXTLvygCgo/KLwRUHWAOt8sWZTtogHB2YTjx8Vcnmeuv7i18xAxBwDgtL8sjjsFVKkyA/+bxXwsApvLIgHm/xYVz/uASP1Ds6DeSbwupDlSF5VTO1VcO288QufpF1Cd3rcD4s6iCPovxVybHxHySJuneaK590i8N5d+enQYXpmDaPKbd97RW3/iL4xHTa2/FM1bSoDwA1bxQIkATKMu8edC8R9vIdWAyMz8h/2ApDOlNy/4b155xOCzK/jLVqZZ6M9e5o/90JduhSzRxf/HrdOs+5ZlNYbdGgy9YCRDOz99MjeLszTP/nJmAwLzmX/fm5l3wHrH7S9FloAAq8f/eK58KPy25omFXQ0Mr221B30QRsAnM91HlM9RW9dzfjhfivcCAcRePNAQSA0gAaTMHKnvDOen75LGIO/n6+/NwiMqgPGB4iCSF1XnZiDKwiDwXcdLgVSzt969CEI+mLO2jxMv/oNWs51BZAH6CyBEAnIPFJHXb6D9fPou+h82PnuiecujX+xAotYPAkCOYBZwdsnsNyBe++zNgZ6fH0SAGnnVzrq7IFWAps+bQR3cuqRJ2tm1T7sGFQDoT/P3U9P5bjBUIDuAsUAOVB2w7iNr5pjLQYAAGQBwgCTKkwJ0AMAob0Z4EHTyGQIAxL61qE+Kj9tvCgWPVJtL1/vGWZF5z9wNPMPWKcbfI4XxZ2EC6OXzigfff460b9xm2jNaNgDxAMf3p8+24fVZ+Z+txeKd7ud/GX4+/L356FHLzT8GwOdF3LZV8xmGn/X3vfy+AqyCn7I230rxp7lCfnpWyE/f8vzT9zz/NFfIP3B5GuDz4u9J+gcSb5nyebF8RV6R+ZH4FmlvH2CY3Sfq/Amdn34ptOA7rgL2ZQ5CbXbjCGr/tyL4vgRUwqgGwAMWP4tiM9fSHpTvRxUAPvlS/D7059QDRaaI5lBtyt9BwqMbAGnwdOG3YgUeFS3g7c99ZRTMg90jUZrg5XPRZdnHF4CEwd8c6ObilM+x3swjIcgq0LK1SfC4ekDH0M4//zgNy48fTva6oAMAU1nz+3h8KykzbP8ubZ4KA0U9wOHjwn8UBBCqQOGZ+ZxyTgNiGITvrFg7VrMmz9lv7hYfkP71Cen/KhD9Hfz/gP1z1Z5B7FGkHnn3IXiNXp814U/5fGtZ/5WJBTqCmaJffp6L48c3DALfYMz4uPg2MQDt3ma4x+xddGA8/mmeVmZzP7bMP8Ae8PVt07d/cXCDl5//TK4HUH2d4+Pp5X+WTpoBCAD0bOy/Kq5AeCCA33nAAw87/L10/LRCVvgnBPu0Qh8bXq8N6FH+1YpA3AcMg2I2a/7dpN8VKx8z2awYMET7/CeEX19AIAKJWuctFN+aerAcoNanZm5YYJC5gCG4fuYYePZ/2e6/UWtiBzSYgJyzXgcbBwk3ju8SLkmQrhescMLfrDcbl8TJAPMJBPXW4WZDgHsYTrhOiIVu6JCkHyAYoPfM269zj5bMEmLkJkRIchWiyxXiA4FWqO8TOIF72GaFOKTrYC5GOu73rWlS+G9qP9Wcbfpt8pjN86b9ry8ujoKVHNrw2+dnB5NLF7Y27ijasI0QQ9ZbXbV3EjMPjX1TS4N+WTF13DKJIvv1vqfO50QjD83hIop8sCrjkoE0AeoNUgxlQyH2rLlx3NB3A8rXIeOYG0qBrj3o0vXo1FFMnanN4FrhaC51Z5evwm68YyeX7cIrvXJSC9vk4X5ZEjSMIKelr3NKezkoG2i5gYTldLDyCymK9qjpBuQJBYvg6LSBw3zTrg4Zn+RdttsQurLcD0FHJ33WLrMqG0+Ot2EF+NbzLXeH88S+Lu9QyLmEWqZ5AzNx0hLVGsXuk3SD94x9aAl+upzt1dkQKuEqG4i2wSB4D8Bc0fYQty3hcW/qycrSMCRv1h4XQcHd3iwhKLxvYuycoVDo0hBEeoTFXLULzcghl+zhNB+tRDtdDkJ4kJGdMpk2fuOLbu9em/3+VihNMHX8khanhlwaR4xaO6gfqRSXavqFbhQ5GMNO9ZtLegrwAzKMTIOMGrP11DirhOIsZZ5uToY2cLq9E1Z2poumf9cndH1vNyo5aWKdG82AsoxQ8kzUBDm1jgNxdzwlgmWiPq+IDWMczrflfgzVoOb15dCc3H294cMsl3G+7Xn6QAQNHjcRhMibY4eJxfKqN/VeEJiVjuRllMTpBZWzRB2osopqdUkoR8Ikt3vpGhdsR8E55CC4Y4WH1aQpgn6BD3vV6qzUGCUlN3G7GwsSS9a6CqdVZjIyr5/2RXxW8TJkllNxWWkXdqtizIGTL+7Jagj6Gq2N4xD2nQQtGWa6sVdrC92q9blmoqk9MySqVjIfDvVdxPdxmzHwukxt9qQe4tplY7GytqfKZRtK9LvVzSozXhtv0JI9GGcQbLWJH0Rhp941uoBBgJ/kMJHFTG7SO6EnuA0x0HG6mWFChpGxQqLgIJ45U8h7VFCOV4SdLNhhK0g0LngRXHGXMvqhURSPlwqZPkg4lt3houHZPi94nGZbjqscGTaQY2bh3fl6gfcDwVWktGvPFdaJ9iZR1oy/IZDTzYLVIOYYMgzpkNwlBLeBbGebabw++q5FXSp3DCwZZ2njYGFFdaIVDiKnaNux/Kige3yDqzgU+f4549TBkUosOCU9ERyXrHOR2RJTViPrStiN7jxtSKNOOq1ZuTIlXsxauuzxyIcorPLaTVFEuRs5yM70OBZLjsfBl7FbWGVSfjl7oTyIPScyN4Kzsbal1XZ50qshUU4Bc17aN9Opl46k4eXFKgTrxhjD0dPwE40qmYleQyg4jeulVh4SXteloSNpReZ0U55EyxDumMI1HQaFkJUrq+FE788qJ66KFE+0SI+H42BTZ6dvXWc78SzErBWaueoV5iT4mT1sQyi635WR4m/KeKyPXs9DrF7z3X2E4o5uDzf2lPYeFhiCGPd30ebpwcF2141h56fjBKtKzTeXmy5u+e0gOjzhqF5/3Pl6sBYgvlp1zrXhBYvfrdktznBK4cDCkPuijd+3soBdYxjbFfsTNWlm6HrGpEYAGyd4d5QpwrrcqA5GekrxibFBxdPGYNobvVcdVSvdo8O79M7f3uDdiFGrLAD30uZEaTqz7afWq3wc2zQriw66QzPEUUkSykCfmliAPfxIAnNS0mlcBRzUSaIvX13zuBF5Pq5QanVeC5g9ErZm1mwRYP0eE/FiA8J+vEnsxtrKBavgbjRdaYS5dBfVKAOTQJYM8KKaVttb7i/pstF6GcO0bQ9LGwanxSrqQHCgjb3u04ZPL3i0RM7lYUuy6VAJdHxNp3PKX+5eTh6VOk33rnrOQksLtbSi3VCOdCNclrbGHbGlXGdSZnB3cVVv09RIE9bhVf2IZk0j5HxMVRfJJ3fXTumRxNmfaYOp76FAGYxXkDZAjXpL7w+ISU896ubLZUJaoshKPtW73r7323FMpHTUq/M0lpc8nHoyvBcreGdR5s41KKVJCaVMbql6JSci81zRL0nqmjpsCG2k8a50JBWLgdSN0dWQUpAu8O7GOVighHDoCiUu30+t0212OsgaKID0rNj14lF1HYaC6DzTyEq3kvqUNKc9tVe9GlUmjTNPUl5Q+CZHk6Xui9Nlf833ekmgLkaJqBcc4szslcg6Gn3BGu4u6uR9ttNUTOI4dijjqkgnkRX3JX2weJ+jU5pCnU240X2pTDPj3EwytsS3Zp3fJumwAqWAb6l+XR3v6V0gAIEaPVDLI7HWCow0ODSf+F0X58ayOpfJ6n6Xjvx2TKGVqmLns1rE4j5Na8ng3FugwZ5xRGRVBN6qx4adyvxk0K586nx/KQ8Uku5pDlXXanhVrZLm1yR16E/TSmMUup5O66zCajg6RlZln9HbGb9v9Br2NBQ/7PcJYVaFXPX7BkFpmu7NA59UsHCLwpHc4SJPpSNXXaOEaLHR5dHOx1HIS9IiF2S23V8jYQfFNyFt5Huq70Rz4DBNGxqRXqIAcNAML/k8lDC7VG+Mexwr7CYQPX2mxn6MnaZtD8Ra9/SIKmB2W53184BmRGHH94sGGVlRpNnOJa3N2tid7K2yWbaUKqVqs5K6yia6g7c5r5LSS29YP06YZPU6U5ggwfqtxGDTZJ3KJL2xZS6bEqj0tjhEMUpWo0dDeq7udvt7Wu94TGrSEDO3+Z7MWQfMDLlqmiZ0Pm2ivTkEQdyXduYZ/FKCTJ2ZmH3BSjRbeVf8BEtHPWP0aINLITSu+YSq1LDRs6vCno43u0mYJWNbY3K/19ixb9dI0Jx3ZDP1Ezu5ew/aX3U+HgXrRNbLNtZr/RqerzVfUaPRwME6I9DLNQYtTZXt+9FtbiIZl3yfKp0r7UpDE508bvLknAR6vEux6Ar6AiHKvEnP7mbSJ+rWWepHRNDHkODzTY+fd3idxQXOhiLPHON7jDoH70LdPMVqGcjOQiTgOerY522hbHje4vgg2Od7NtSY8W6AmjKqYFBXCsigrkwvuYKjZfEaK5itb/ayxE1OIa+ok7TkKqpgBJXf4QgS4gaHUChRtedl5fPOJu4meE0Q+vmwQ/e2y9LI5Hh1w2+W5J7oDFrUvDiFUIypNMGkR9UUuK0rBE4TL5cuFB4JkTjcxgEg5dCemzvP7L2Dwe8qjsmG0G7NquZRACXL8mykg6H6LTaQQcvV12joLGeCUYm4IbtKtU/t6oKOvjqN3XbrGabBY4aQRvyayg1j2doDeTPTbqI9u6PdG8KBGV1bLZ0M2h4mj+qsS+FSleBDKydvYz5i7GuqqgKLXs8Wyh/krTr4t/hIrfb8Qe933rExlZFwDJQIuHCZQ91VIOWoLpodlpt3qgEtI3OLqg5dgh7KXOsb9JbjMHFjadZeSeRkI/iN4W1rLbidwJxDdbfiRYuVEY2n9XBHcThvWZC1u1y4dYJtXWo5MGMg3Gwv7e8tzotnUQ0HY5uiFUf2hru2tDoctxafd/AFyeMTbNtegq52eGxiFygPhI0WrWHVJMrzgA8eGzJnmCxPu7EpdJhp1o3q7rkNn9wmF4lBj3RbWrkc3CG3q6W4hpHhcEZPA0cbFerC25j38lulSSJ1D6KEn/yUxRS7sELHzZL2iCZ8qfIsgZ8y53iofV9bVUZElqvifOWQEQAd0R0PpH8dhh3MlEl7EoW8atZ7TifTQlDxvk5u6zbUSI5dwytb1v0Eoq2zxttbuuEPrlkShpkTmxMSEEfBrIUAOQToLuHVvF1eqWDLnnaO7oKItJ1GkwxJ9ncZ0yZtLa1v50nsWP/gqqp1Ycm1pZ6yq5c692btc+GhsE9CqnM90mrXM3QkyssqwziTyzRY2a/P59C4bG7J8rpLzxyjyA3poqtiqWKls7YNHo4CmT32XLiTRuNglueclw1r47UadyJibQwC9mS6im2lK0zhMcEDE0SN9Gfbr/1MVfK1IjLdZn+8o+HRR0Y6W+6ODSLfdZtjEz1vmMGMeStQ4syq0cJCJIM+he0a4qQ7PAi7nmgSXOMi3ZF1CUYzS64pphGxbrgW0BE5spcIxc5lSe16B1oJipeu7/vUSUEAXdIgsGO4HO91oFM4xsnIncCGw5aqQn+QdWu9dUv+IAU8rspH2mYazSEV3LkqHXqAMK3cmhTpxJv7bZxWJlTBnrrvLXbZOK4dNXYu8NSm60mIaa4OPCXjcTtwLHThpKORw7nvYdXd7OLShtWbYQyhsBm25Z2ofMvXL9KmGg/WfbzSAG8VX+hvt0ranfrbVdGy6WZBomYvq1Y0uBVllJvq3MYWGLKT6BLUg36yhVUreaYRjvKEaFkPN0F6b7W88MVDx9GryyjTsRn4EILfxRE7kM7FF6C1kYP+Fu3sWgvFupwswp+Kcw66qSVmy4WKulVXnH1zgxdEdVaOsWK3hnLhzC1fNmTvUZNdVwbCQDVXVxvBlDYmCa2SolJKG803yjmz/ZUb6u2guip9OWKtQRekWlDetTbd0WyDmMkEq0xOaimKOJJ0y6vnED3MFvtE34jthLAXhMjVCSNr1gjaAFQi6e7IfXPk0LWf3T1XWw2bTRFHLEbBMNmGxPno8UgtYMfJLoiTsoWaxmq7FZrYSNOepWmnHO+V7pEl4cnD+dI1CmjKkX5tGVAs8oNH31p9L2vKQd6YiUSvj3bPmIk8nhD/Ao260ipaR5+k2puO0AU/TBZI0LWrBn608y4KvrKXlym+Hz1bTYamd4doU8CQwKyF2DqPwVG0NoIq8fwY1rBMLpcnBMUSVXHQ2AGxI3V5P1xIukkddzowTB4m53ZfwFq7JTWkwKb9fdd07N1tcidG2h2BWRm8j8NhIC15hToiqkEmGuXaNukMql9BvnfyV5dioA1e811nvdztukSLaSG5riaktk9ELoQ39uLdVEF0SfoMxvbLuiQv2Mk/DwlDK5MzYQS6E0J3P8ZcQl3bRDAzPdXZgaXGc5ieC89iNV2jS9ZTkOUBqd0kKlpOP8kaluMptTEajV3GKuqrOpKciLVUjj4hmCmPZvSKTLmp2pR3W5QPVDdVwobsbNAbyFfeP62nyKagm3tlT+sRccNzLgs+EpQA/Z2BprvLKtjHiHG2MXeqTNZf4cml9EOIIWjoyscWKecNRqhrzz4n+26b3ItS3idghJssWpea+tY2lWdeIu54w5bmymzSZL2cOFfLvFZ2pNWQe2cVLfG7vOVacdvBLGftl/vw2osHYvIC01uu/RhyqdTO80a5q1sPwYrV7dpBJ89gG2/rXi414mtcZiHVMeqXdHc+XxPMiTOc3NDcxJS7kjvs3PqusNecoTAe7kg0P2iDpRF23F9xpUmgEqE7s7BWu/PewiJ6oluoPitSja5rG5m8JSY5SxzYTQoCP9N9eaIVCQpXne2VZnNLqsIOhiDqLqejqNEdD0uktpZ5sjKme+0Gt6Eh0DvqNqEzNg4l78mVd2qHYSPR12N1zZHydEF1OPZRtWq2Z8JwdTJvO1Rp2/oUdrzpnGow+wia6aeKF2gpcfExb9OipYSduAJGQ5kOhZzKGPY2HWM8ytR7zXlX95ryWm5CkqN06iQfiiUWnLenJqkGmmgQELEVN4RNVOwRNI6qGOb3x9JR5HCs4hstcPJ1KtCegZNcswZHrEB9ZqKQKixr9DKb1FyxEi9S4FIsWTfH/nho22sXHwzo5G/2dgv7OaGsVaoUW1gajBWVHipolFEW3tObJvKvJCFrrGXe+SUNRi6kheCcdKTuANOHK8HuMjdAOt2ADfJ6UJscknZyY3UVl0zW2mirg+mts7qyEPew6nyF8K2DvqLbAItzXQH18nq0StkRrseAHFdHTpqq42otmwSM9cnhgk/Lm74ShnS5NgUUKa9UOcqXKyQVYuh3B5czYzwgToluQ5ftoTaJamsCYNUVBgT1UhSpmm1z0JodwIC46XvsaiimcBfPmbO8+yrOd/AJoYmbh0gwbsr+5prDJ6KiNiTeX6Q7dh1vUyMOiJrrnKUfjDUf+UTfJBHi3+AQJmpseb9BrRKaEgfmnFbtrMinu6HtNpmJbYxi052sqZBI53S8KCLeZF0XgPzEKrq4BWcqMaAc8jRN4zGlpbfN+rodNHWJHGvnDiaXbgIdRXk/XyUaGS18wJG74i7B8CSEaaCvjjxiAsOtggjPJjVwOIkkI30tlwNF99EZE9zNjtF3QE+h5IouqL0tKu3a/tySTbrayAawIi6bxkpBh4NNL9dxJ8sdbutQxCElnicr9paGQ+BQ+NTXsM2cSAlmT95SCH0nr6fO3Tf2HVlOVXonIBteqcoaB93VEPcQvoN8gqU7JVV7UTc0cu2INX68Gcktb91ESAtYQJUO7jQOzAVhT8BOZ+JTXpu7uvc2ybrO3E5xbCE7HnXCVrCObb015+7E1biEu8riVjuavt+97NDiIRpXLlkudzjVuNzO7neWwEdbubKUcm1Q+yPFGMNJu4CJxAe4eaej8oYLPr5CUkrhPAs+XEaplMc9CNcDHfdhtkWy9DjV6/TamXtoreEr+NjGbLdp4aVIOkasbZJ8fWcLCxtEYk2rgSnrkV/fJZykZfSQqyTVHS1/fyiTKkYow0gRW55sSYXE+0RIIXVT5fXWrDbQJXaxMh3rlXJoELhStoh3vO9Aq80k0E24EJdpQBQ4YtCzs3J4htlut//4x8vHl+9HXS//xfeq5vOU/2fHOs8TmPd3Jx4neoHjf37w+vxfFfDnjy+1lwDxnsdaIH2it2OffzrU+vT3TupmWuPzNab3M9znCXHrRPNbwC9J4XdNW49fmzJ7vFUBdrhdM78s2Mzvk3rg+/fHlX9Q8GV+eQ8YYn6N6Wtbfn171fFxe35rIvATpw3eLqO3s7+PL/7bmzpf1zj2NairWfu3E3mg9PoVeV29/Pa/APNNr/WzLQAA -->
