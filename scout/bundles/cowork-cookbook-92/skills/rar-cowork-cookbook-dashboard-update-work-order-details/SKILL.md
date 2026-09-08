---
name: "rar-cowork-cookbook-dashboard-update-work-order-details"
description: "Pulls update work order details data from Dynamics 365 F&SCM for a legal entity and recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_update_work_order_details", "rar_sha256": "2c73607757293de6217b0f9e92fe67930a0564e2c8aa6062a056a0e382893799", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_update_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `dashboard_update_work_order_details_agent.py` and in the RCI capsule.

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

Update work order details Interactive HTML Dashboard — Pulls update work order details data from Dynamics 365 F&SCM for a legal entity and recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-update-work-order-details
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
    "fiscal_period": {
      "description": "Fiscal period to pull; defaults to the most recent available.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-update-work-order-details-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_update_work_order_details_agent.py` and embedded as the fenced Python below (sha256 2c73607757293de6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_update_work_order_details_agent.py` first:

```bash
python3 dashboard_update_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_update_work_order_details_agent.py   # or on stdin
python3 dashboard_update_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update work order details Interactive HTML Dashboard — Pulls update work order details data from Dynamics 365 F&SCM for a legal entity and recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-update-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_update_work_order_details',
    "version": '3.0.3',
    "display_name": 'Update work order details Interactive HTML Dashboard',
    "description": 'Pulls update work order details data from Dynamics 365 F&SCM for a legal entity and recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-update-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-update-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0fa2a30a9b4796e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-work-order-details'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-update-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-update-work-order-details-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of update work order details with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull update work order details data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-update-work-order-details-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing update work order details.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls update work order details data from Dynamics 365 F&SCM for a legal entity and recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde', 'example_request': 'Build an interactive HTML dashboard of update work order details for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-update-work-order-details-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants work order detail data from D365 rendered as a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardUpdateWorkOrderDetails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardUpdateWorkOrderDetails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-update-work-order-details-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardUpdateWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916Z7PbVrblX+HcVzW2H6RL5KCurhqSAIjIABAECatLRs6ByKCf//sckJRsd6vfdE/Np6Fkkwhn573WPgJ+fbO7Nirrt09vum8Xi62dZXHk1wu78BabcijrFHyVqQP+W7hl0dax07Vl3bx9ePP8xq3jqo3LAiw/dFnWLLrKs1t/8VhX1h4Q5PmtHYMr4Ly9COoyX7BTYeex2ywwkljw/1PfqIugBBoXmR/a2cIv2ridHgbUvguOFkHcuOBC5ddx6X1YtJFfLBq79xuwpmnBjXZWFv4iLlq/tt027v2FcFIVoLKJnNKuvcWP+nm7cCO7bpsPi6asW9vJ/MXj/x8W2moL1nqxawPHflq05axhUXZt1QHdZeb5wFl/tPMq85u3Tz//7cNbDH6/ffr1zc3sBpx6Y79qMh7+m8D9/ew9+3QerM/sIgQ3VhOIdgGOgTPA6Ryc8vxg8Tr6sfGz4MPiP/8zHew6bH769LlYvD6f3+Y/Wlc8jGtLu2l9b+Hale3EGYjX+2KVDfbUgJi1XV08Q1PHRfj+XPm7pLJa/HW+9uNTyXvotz9+fiuBCfacys9vP4HMAX11N/9+n6VUP/70npWDX//40+9yms5JfLedhQGr37+8jl9iwY2/3xoHiy/6gdu8dIG0xpUPhP/Bv/nzNP0l7hWSL8+bfyyrD4vvS579+Suw91mODpD7fbEgBmDl23tSxsWPLx112fuFXbj+jz/9M7Fu5LtpFjftvyT356fgyLdB9n98heSnD4/0/W0BvXz7JvOfq61Awfw7noDbv6r7Fqh/JvuR2b8TncUF6KevufyuuO8tgP66+Pmf+vbfLfiwCD6/sX4GmrWe2/DT4tdHifz8g/f7yR/+9hsQ/X8Uo5dd7T4kfMntIg78pv3y5ecfmsfpH/728w9dBarYt/MvXZ19T+b34vrQ86cIvu768c9rgX6jSItyKBbfemjxa1n9j/q398XZzmLv9/PNp8UfO3H+QIvZia9KnyH4Qzc2wNY/xPGnt98A+BTAm859XAb48R//sVBjty6bMmgXugtwawES3Ma5Pxt/iuJmAf7OqFH7IK5NPEPf8z5Q/3OGZ4vLYPHL/3IfgP/RfQH+8huAfnni+pf58pcHrn954fov74vTjJZ1HMYFAGltdTh8Luxwxm2gtqr9xq97AFXO1PofQUd/nH8AvF388i9I//IQ9F5Nvzz4IH6in7YRZ+Rrusx/n300Z0J4euQCDvNH3+2AjqycWSOIAWp/AL43ZQaIoZ3j0aRxli28GGALgPwX13TFp1nYL7/84gDDPhdPqMYWT5JrluCGb+YsPn4EngVZHEbt58J3o3Lxw6+//bD4r8V/t+ohfNZxAKzxygiwUNL3uwXosC4Ht4FkgfQC+Hhk5NffXvEFYgpApiB/cRD7z8WgQlPf+xpsXVh9RAly4fggyCDAeQVoDuD/Im7fF2Kw+GYvUDpfmhkiKpsWEHTlF55fuBOQagN3vkWyKFvAs23cBNOHRdf4D62/OLX9MDEHrW63vyzUzQHwUZnNxFm/+AksLgtAqNm3UnieB0LqH5rF+quI98VurslFZdd2FdX2S0dgP/MyTwWv5UC4vSj84XMxc68/h+rRIM/wgJtAZNxXSj/OOQfTSg7QwGu+6n7cY8+seXqwZ/25aF7Fb9dzKlxABkBp2MXeTAl/eZVUE5Vd5j3iByydJb2y4L2y8qhB458OPuLfjyXfhoXF5w6FEXzx//PoNMdmtd1q3HZ14tgFtztp12fO5mlyNvE5gM52z648+vP3seYrdH1F8M9FFoMCrKe/PO98ZPp1zxMVuxokRltpD/mgzEAcZ7mPLpiruq7n/rE/F1+p4gMIxQMXQSEAyAAtNfvxVeF89aulEQjKfPz72PCoGhAkEEhQ6YuqczJQhYHve47tpsCqeu7kV5qLOdKgq4codqM/eTUnDlQekL8ARsSgNwGdvH+D7+fVr6b/aeFzOpqXPCbHrpjrZhYA7PBnA+daGOIW4JndPod34OenhxDgRl61s+8OaKX8w+ukX/u3Lm7idobNZ1z9CqD2x/n76el81h8r0D0gWM9svz+7agacHMw+wIa5fP06jwswC4CgvILwEGjnM0QACH4Nq0+Jj9Mvh/xHK84k9nXh7Mi85lF+j2awi+mPSHL6XpkAefl8x0Pv31faN22z7BlNG4CIQOPXq88B4v05AzyHjMVXuZ/+YXf047+3gXqwuvHnAvi0iNq2aj4tl08m/krE7wDLlk9bm99J+eMTMT4+OPuBGB9fiPEn0U+vPy3+PfP+JOLVHp8WyDv8Ds+XlFd5vT4gGpuP6+tHfL76udD838EWqC9zUF9z7iYwBXxjxq+3AHoMawBf4OYnUzYzwQ4AqR7UABLxufhjvc/9BvCoCP0HIP0BBx4jAqj9Z96+MRi4VLRAtzePlaH/Pu/GZvMb/+1TAaD3wxsAVf9f2sXNPJXPZd3Muz/QQABY29h/HD1QYmznn3/eGe8fP+zsffES9MfSe7HLzK5/6JCnm8A9F2j4MBMAaHxQlcDNWfncXXYDyhVU6uxOO1Wz/c8N3zwiPmH/yxP2/9Ei/o+sMKNdBcLwF9Cwgd1lIIAvHM/n8eBFJHYPLJ9777v6HvTz5Uk//6iOndnqTwwFFNw60OEfFv57+L4wdJX/rtxvc/A/CjXB8DHL8cpPMw9/eMEZ+AZ7lw+Lb9sQEL3XxnDW4Bcd2HP/PG+B5nQ+lsw/wBrw9W3Rt3/dcPy3v33PrgfmfZmr7lk7f2/dbsYygPVzGB+E+ihQYO4A8Md/uf0vdPJHFEbJjzDxEcXfozbPvh+llzUz39bfyfbj/NxRtf93Bs2zMJgGvJdBbOk+h9DlExqWT8nL72gFah88Adh2jufvifo9XOVj+zgbCMLbPv+149c30D72PNC8Gui1/wC3A1j92MwT1xKgDFAIjp94AK793+xMXiKayAZjMZCBuhRGwhRFUCiDeT6JIpQDB4zPoIFPUgwG2zBB4j7q0rZNwiQ6H9qwj9EozWAUwwB5T2D5Mk+W8WwWwVABzAABOILCHmgfFPc8mqRJFyiBbcaxCYdgbOf3pSmYll6+Pn2bA/ltkzTH5OXyr28OiYM7BbwRV8/PZskgDokpjlY50J0MyvF8bCct8w+Crde2cDEpLkOh/Q3iZTRFNHnApXXJpfGq5cXdtLFuiHI+qEcaP92loPNgHK6OaYWNFDe6enrcYLZ3KOgWU1psOmyXQ6Bd+U7TL3pFK5W+rzT9dBc5UvUlITdCLxIyRqT9AFMo+lThglVneiguBaxfErt+k+rs5rY/NcH9KE8IWhanQKsbvN2Ia4ahFYtiCKo7ZajctquIExNvLea6PS4zf71N03Z1H0/2mHCQxEuF2ZRlIbZ38SzV8XFd7NSk5NdlJlZ4TLKGewnJHXy4wybOXrROasSyOPq1tqqhJazTQTC4LqnirCBn4yRdWlE6ahZ+NvkmS7VBFRJmueydiqaDviBIuSKXfr9EKqklkpMcD9I6VONiqncCv9vSOdZofJSuzHov8wXEXbmYvqdmaFNHTe49mcVYCFt5x3GPrVeqrMo0zIobA4WsYL0puI2sJcHe8qUt2+yuo3NBhw0j4YoBQ6EWdhVrj3pqxkNxUMeIkgk/aiffNVc3oc/P14saYrohyWKp+zoTsocYMfQIFVvLOcpgzbBeVWavZ5IpYzxxuu5bEmNSVYGLPFTUNVtAgmndQ5tlqCMFkVTanYydTPtWtUon02C41JIRWNAHUUyRpmSV/Y7eh8n9Qtu12LgcDw/sspum4mRDm8OO2GHcviJ0hnf2kpuX+amip/y2RI2gV03SFuhcTYeI2DTRjZd4K6RPiRfzMNgKEHmDKA2eBBxO7OB7Y66E5OhJq4aMSuao3m5eJ4+iSh2Na5pMEiQHo7NtG8jYkjxMw+fVbeu1Ntdl17WZNPbAtSgFtg2xERbupepG3oraQG6Nq7GXzGM/sj0kc7fbBtvG6CY7ZGwV4CcIj1ajTmt3ejw3YhFHaESwVrPfnHf54bhUyJa+Xq5EkeV8vyOm9Y7dobR5azFXzes8OzJ75aSptq8bpSncSpmXUJ/AxRO56/QrTwypQruB1Xsp0x+KfW4dqDWcuydpSe8OsKwMXk8YzqYfxGk9Ta2XrAqjzfz64Gwitt67idpHy2Rt3dS1ocVqQmzWuXmm9ivNvyK8PsjrCttrZiiNsDhm921L7NGJZ1votklsvZrKy/p2PwlwxK1O27m8GPxwYBm4YZjLfdDPw8GOtsFG8e+cOUSHNZKi1sXJUYXDGh9aN2upjxjGRoxRwbwTScswFAhgI3gn6AqHohLiUt08+kfpepg6T3MUMUUPfbat6JMaVzac1lYd7Bw2VrLshkowii/vbqJAl3xQrYjZNdq0dseWGruzyoZ7CZVxORziCHS9yiqcg1U5bomQ5lzoEcBDcBQCWlD5u+6l3kE31s7mZByHc7ajMVVghAMmTczEYxeoajpBa67+biqXur9r7atBCYw+8sfd4XQ3D0q+0mRKbMyTG27YlnC2GZTylMlYANhyTut1br3liqIP0qY4nPGtdIQ6oYh6cr/c5pt8uNMuzx9OkIxfFWKNhKuA54ttO3hRrFxR4wDiGOcidWWVI54metzaNLvatGqFsSt6jebo6SYTciemZbq6kpfYuxMT1tz2rO93DBION1UV7gx1O6bLmyf4SyHVzsaE74UI2skaNF5P9FI8xi5MrxzXSfEb4e+dapcce7Zb+f6SRomAiQRW62CRvY0JluMqXtzX5jG+wAw1FNueI6l2L5hEauw3o7CilIw7JBSSOqnamJvEmtx44y43+hBroVVeAw6KV1KqSKd9zF1JlbKksKyvHU9CPgvdY2upZKi+uqidbOWRiySHSkpuBraOc5jOmlt/L698ekmGtZ8dqiO1UTGurgb/6HF5HSECLcfwFGteaK5a99S1+C0+j1Qjj77tu5utkWhHhtpEVIiYCmI3Vnjg0HuyygkIvm83kN5qt1NdHJZKc5FgJugvrezKu6yq1wdcrQtDN2w/WGuVWWFHWRDYTQ7d1X5sCHqn7iHyevRabbNl0z4whwALBwcLT2TXL7v2gBHHkJosgjdO97tIE+a4WrGOmN0HF7vjCqerytlX0P0wiWshxvfHU7zO45piVOF8rEeQdtm5WHySHLYSPdgEu8YdmFrJjeyuqE26bkNY5NctXdusKLqGzg9d3lk3szFZa8uFI0HHeBc0jGcv1aWSFEqWJxZvQVud3MYwYbjd8h4YTodcIy+zmeLokNkZQ2lsZUBHtVpduyut1eIoiShnSIrNnooy3my5plN2fZIx1u183PSHxk7jKnTkTeRqzCidxJbOt1aQ5eiZOYwrOL12yi2Djug2bY/bc5Vs2GILFSzfg5o2w6DulZOFYVs+PA+tht5gFUPO5oiHMHyMZYLi0e504kQrPwToZVWb6slEV55Iubdw1YgXb7e5dupll1xjaak41iqh6UqBdglnHYzQ2pAaeknobZ53/marl1zC1rYqqIgrnpHcFQ8Mk42eVqs6fRKVHM9gUVztB1SqT4gbX0zCGI4NRzTXTTKu1lvyEnkqyaQpv5vaSQRWmdThvPe3orRUJ4Q/QqdNfezNzBnw6VJaMLJB7kmhKUKOKLzSuXf4ynJreLjs2tT0lBC2ILGTvKjQtIPMCwlUSEcBVyVfWeujcY4vU0bnriwfWsNmgHQ1vZUVOdy4VZnmfQRN0d44Qqqzz1T6Qsdeve7VWzQeLAeCrZWVGOx4VOj9hbieVJulYw6x8ClltR22z8WYtDhZY/YoEffOabqnCqoEbOth6IkdTCXWOJF3zcnx0LV8G3anUs0wTtZ7ktrBzOGeDBTGN1AkScp4c2/a8XK+hKrmudFuo92Qs8XVGbrVNypkrTnhZsObQCUACGeF3ZwJruLkQbvB6zyT0UObpNZwyMP4Nl3tjbau7BXhishF0u7HoXOcsYx8hr90wzHC7WGH8HfCWq6GSq6MNZpeDzu+5jAe7MNKuKgJRpzG+Lrv01ac0hqFAdeVZiFFfHsqLgc7t9dpaG84EEVkax/uUmKvaN+AOlvNV4DoMGt5h9xbzV5Te0uFbIft3YBeUQhTuNWJPZf3KIVwgr3la4lKQ2hSywxlEGmllBcasoYTnOuTwvOiDlcM2h6Pqb5pealcwUq5wa8ZIm3HdCP4owvoSitq5553vSVKuWQgPrbLSkyXcPm8CsXj+VxM1jXQ1WrjsnokRgEVHqdBPcWn0rKMq4rvpuuFaEHbO3Brmf3aaig7Q5MdKwTosdxIKy0XZLvQixNPmgPN8dvNfq2mRpdnsCviUnO2EXkbH3GJm7hii+R4D2Z5grG2jjQEnrguj+0uSM/hivBjyck5ohOl9QZHlJ2rddw+LVpy6S0hh3TQvlr6yzzH7hdPspOput0vfXFCdNL2MosrCZm/UGmWjPmWVeWJvAQAOtrIJHdlBqYxmqw3fRPrq9qnBdeA1rpOc8ctrp4bHJ7wOw8dcQM/EZLPiZE/9puTJGyZQV2xYnIXm9tqFx0pYXdqwiO5Qa/8LW4NiLiaCVztFSIireM53EIY0y9LEzUMSbO6RBYa94puotsFyo9g4pyunQ0xWzywGRGk7eZZt+RSrKOsQxzDDScCGkIGsytMjp268m5Df3Y55XbhjvzOQZ27ndiZ6Ae4zrBb6Ah7Bg3nZ7nuzhesNeJ0c+dkQ5xk5dwNKaXIhgHm+Iucb9KqVlzUJJszPQlIRyu1IuUyPGSTzpHyctrQZz6tQ5GUunzLi+WKb+UYOQ6ATmMZHqvShp3dedcg3Xg6nVN3k03dBt5qpgqNRmSUtmcoRtAGUbPZLSea6Umfqpp8SXpGlksUGFPvCkGgo2XUCLNufJu+55Y9Ip6Tb3hK5LbQxNGVipj2Sd9SdLqrsev6JGX21l8rPbulb4pZEOLNFwUINdH4Tl0vbHiUtVW8Zup7rfg6d93niE5VXm46m4Rmt+jdPYrJyloVFgrCaYx0oxEIAgoWcBlZ30qBQtC7TVx2MiwgaSbx8XocoFLHTQ92IhHP3SZEUPTGNyJlxgSzZY3WvTQ2n2NLSA9GDEk1CTECclWMpiCYOqPpeiHHvcrs24ixyqOFhjVBVs7hcN95eCPdfd6Lg6MkyOczH3c5Sd+8zKRVVdHasF7JAMnlXVI6RVtsFSIc265uNweqI42txVFHnZXJzX7Slt6xOtWttk/6mwndFEJ3s+1uWt6wQF2KwqUyPTnXWpdbNSsyDzSSr03yFuwPB+nkF8yGkGp/uYKr3XDWVpdAZFdoTfLrfM3quMF54V3e5yMsY2fJ2la1JSWcy1mjrtzWerRBEzm5miI68m2oHrjt1tGUO5siJqNLnaHuxroIREF3rr1xh5MwGDsUttBOucf5sMJOgNWxoCzs6Fye2i1yEpyDVVKpJxKsUcGWkZTUrcelki86fx3miHeSbzFGIFa8vJVlq0J5z0mWyVzKdsvbwjWMan/YRYNrw4jbauWFOPKFdun1oIWJEh18wGfIZSIpFWmKtEKl5BJ4/nmQ4cZYw/e6uHnEKcDZvT1eaqRq3OS2ps9d7QqFimzoksUPib42HWui2B27dASnwYhkCIYiNSjLz/uYU5lR7oHRyynBNVNc29VaQ5XTvmZ5RttwCI+sN2sVGaCBOXs2xZJYxrACnvLj0qV3VuIP550TXKZb6Vk+RBXc1UNFl7azoXLJzrpb+aUNSiNncZsd66sFJtbEmZKV3w3LO9Yv4fNhio9pObpjQTHtMqpERVcUmegDAbdIEalE9sJn2J4A7kOEko+ySNOn8FKFd7jDOajE030Po32ehPGwTUvH9MU7u4bWhJSEY3/YqoxU7KIbVjXneo/txnIrUTB9g4TL0W9T+VCfe6+P7gXrX/E0khImRJJiGQQ3Tbq0VeBunEKx7/JR4bbAdcb3GBQ5w1SMKx0dRYeh3Tf5cSCZBE7t+q7Hy3gHan869V07oEs7bpERHo0LKySwnl3xvWQE9YimYOczQhRr5UfDuuw4+8hysXYQErw9Bd3UkHsHj6Wrsm1bjYiMayE1uXKohVPbKgPNy6V3JusVrDVwm++EtveS8zJls14QB27ZUKKJ8QINerg9xDNxSGfOs+ik0QY3D8jtKSWTY9ocyXXBgh13nTtxvNxdtMRHokO2E8T9NnV9TQ29nXuUevyKHlh0VQSCstf3iu0dIbaZTpSJRb0srNFKw+iKalEqwGg0Z9IDz69NmU9a0vBMKkUGrOsRTu7tmHZdZ+dEVy9FeN9ekud1hu+nPEMpOg9cvGJVpG/PtwTB7S5pTjrGnfdJDnZd/l2ksKzJcwPR0ThENDO6b3ovU0qldxuWRhBYcqSz2fuNlPNcJ6tKUrKYBAPab7Fodz7jO/SOqBTXXjwdQw45TK35yhHI86pXfQupymV1rIj6uN97VYNMSpWQipN22tWOAPpWg7e7Tsy+yhIiv6w4jWd3yOaSaCi7asKAuDP1XoLPa85KBh/bg0HzxpMhcsDKKZapIbo0K9vyMFrZjCGUt+Zyp9yq6g62SDsarylal5MCuxK4d+qIkfJko7Q6Zzf4oNIAbWV4elcd0rRTRhIwZUJai/I8RsYEwkHPMAd6Na/4vvXUASUZJQFYQRnCVi4LNFOi6HRdIfitnKhdi+JoO9bnqy8a9rlOjEORq8TKp0lHwhGKkFAHg4P77SDqE+kK0Elk5evOyC0BWcuZb+6ZLSaIx0StIDt1vA69GkusIkJtP9QWtJ/O7imuT/0qmjYNS92V9WUDbfbWMfW9fqqiGysJXYSsidTBJtvsrq0AZ8k91g/RXWGv3REbTUepJEvynMhxEXN7U6YOh1tVS5ft2R89pDy0EbsbWPtGiIprNGEl47wluHxwi2q03I8RJIhJIWMnPaHvuzE4bsZO81oTzEb2UO5Pba1S2QWNKTM/ujnUbvZtwm56/gZ1uWPnqotlRWXCjox2Xk9qe1lHWc+nohyQGd0mqlnubSlRfWZCVWF3r1UU2xvMcmTO4oQgvVFl0li5y1uI0IYWopbAIcstlfX7pXDWCMW/1BwOV3QRbm7IYXPlKTzlEkIiB+a4O+b3uqqsbNMspT282+NwTMWnsbN8zymCA+kk2MxwhbcfuSQo+T67KEeI8kpseYUk3zC9nNzH4qSTk6avGY4FCJ8ZQiLtFQBFECOASS7sSSjx8eBSCrLpNw2OsmA2M8g1WmIKFaBC1d4zug7pS45cDt6Vaq4ZpRe2oJ2oMCcFaUiRa1vsG4FlpzUorHofuZTBB2iBYpad8ZRAhG42YfbeRCiKd5NgTcGpvifC7aZS+S2CFUozeI5NHYpubY53oWTDLYsdxGNoxAOWcNpuBTHOeF0JSon4Qia2eYo50EDAepKkkwoJfj3szsQVRKtDhr4cCXlvlV1EZjy9vSXAK0BqZNRLNYWeus7RsMsZdQbLF3vITAAG9YdMYO67aKqpdnDcPr5oHbTWMGVQrkotlSjRZgRZnNfj+WS2Y+UoS3jHeizM6dryfIf4FMxfmdnAVMiY6960l65zvjt7irOI7hJjpBVRgThmeMIse1ewrZDq1JGqp/pkOY5y3S7lA5Nk3djChcoWWWxIq9u6IzwVPzmrM6fyp/PxtOOKswSQB1O6m+3vPHlzz0bh4OfBhty00UHX4pLshPZ4qCRud9vdFSpLfI9b9wG1ddZ9RPaEt0RFxvQBFdZZge1Tk2FEWsi0rhR0eOx6b4I2eSqkl4jvfV3mbte21GDJYgfoHF0ueww6dH1o0Kwb+nu814u7t7o4J2kfeHSVBIzhYifHujpjzemSfeMFJFsK4ZJmU1ve7nfSZrVa/fVtfoD69cne27/zmtr8oOf/2fOm56Ohr6+aPJ5a+rb36aHr079l1d8+vNVuDGx6Pllrsi58PYT6u+dqH/+FR5KzgOn5/tfXJ97Pp+itHc6vR7/Fhdc1bT19acrs8boJWOF0zfw+ZTO/cuuC7z8+fP2mc5bs133s+l/a8svrPdC3+YXH+UUS34uBQa/D8PW0Eax+vRL1BSOJL35dzc6+3lcAPmLv8Dv29tv/Bk7yWXznLgAA -->
