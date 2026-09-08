---
name: "rar-cowork-cookbook-demo-data-consolidate-and-eliminate-financials"
description: "Generates 25 realistic demo records for consolidate-and-eliminate financials in a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_consolidate_and_eliminate_financials", "rar_sha256": "08869653fbdd34907f4bf6fd4fd37ef3a35647190e27bac1ec90f4b5e21ceb90", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_consolidate_and_eliminate_financials`. The original RAPP
agent is preserved byte-for-byte in `demo_data_consolidate_and_eliminate_financials_agent.py` and in the RCI capsule.

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

Consolidate and eliminate financials Demo Data Generator — Generates 25 realistic demo records for consolidate-and-eliminate financials in a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials
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
      "description": "Sandbox D365 legal entity to create records in (default USMF).",
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
    "record_count": {
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-consolidate-and-eliminate-financials-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_consolidate_and_eliminate_financials_agent.py` and embedded as the fenced Python below (sha256 08869653fbdd3490…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_consolidate_and_eliminate_financials_agent.py` first:

```bash
python3 demo_data_consolidate_and_eliminate_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_consolidate_and_eliminate_financials_agent.py   # or on stdin
python3 demo_data_consolidate_and_eliminate_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate and eliminate financials Demo Data Generator — Generates 25 realistic demo records for consolidate-and-eliminate financials in a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_consolidate_and_eliminate_financials',
    "version": '3.0.3',
    "display_name": 'Consolidate and eliminate financials Demo Data Generator',
    "description": "Generates 25 realistic demo records for consolidate-and-eliminate financials in a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-consolidate-and-eliminate-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1463d78116e7fe7b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/consolidate-and-eliminate-financials'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-consolidate-and-eliminate-financials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-consolidate-and-eliminate-financials-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic consolidate and eliminate financials data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for consolidate and eliminate financials. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-consolidate-and-eliminate-financials-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic consolidate and eliminate financials records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for consolidate-and-eliminate financials in a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each record's primary key.", 'example_request': 'Generate 25 demo consolidate-and-eliminate financial records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-consolidate-and-eliminate-financials-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for consolidate-and-eliminate financials in a sandbox D365 F&SCM legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataConsolidateAndEliminateFinancials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConsolidateAndEliminateFinancials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-consolidate-and-eliminate-financials-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataConsolidateAndEliminateFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abebVpfmX1Hf+pCksC9ISCBc612rQQIxSEjMQnGWwzzPIIZU/nsfpHtt532T6k51f2p52RJwzp73s/f24bcXq2vDon759KJ4Vr44WGkahV69sHJ3sSv6ok7AV5HY4O/CKfK2juyuLerm5cOL6zVOHZVtVORg+8HLvdpqvWax2ixqz0qjpo2chetlBbh0itptFn5Rz0SaIo1csPQjYPLRS6MsysHVwgdfuRNZabOI8oW1aMBjuxgWexTbLFIvsNKFl7dRO35YNK0VAE5t6GWPtfmCHhwvXczyzqJ+WDhAhPa7JTORDw+taq/t6rxZeJYTvkn2Q7Mo6yiz6nGReOMr0M0brKxMvebl08+/fHiJwO+XT7+9OKnVgFsve6DU3mqt3TddyNyl3zVhvioCKKVWHoAt5QjMnIPr0quBGTJwy/X8xdvVj42X+h8W//7vSW/VQfPTp8/54u3z+WX+I3f5rMqiLaym9dyFY5WWHaXAGK8LMu2tsfmqFzAc8FIevD53fqNUlIt/zM9+fDJ5Dbz2x88vRTm7Dfjw88tPC+Cfzy91N/9+namUP/70mha9V//40zc6TWfHntPOxIDUr1/ert/IgoXflkb+4otyoXdvvIC1o9IDxL/Tb/48RX8j92aSL8/FPxblh8WfU571+QeQ9xmHNqD752SBDcDOl9e4iPIf33jUxd2bneT9+NNfkXVCz0nmKP4/ovvzk3DoWS6w1ptJfvrwcN8vC+hNt680/5ptCQLm72gClr+z+2qov6L98Ow/kU6jHKTJuy//lNyfbYD+sfj5L3X7rzZ8WPifQQKl0R3EnZ16nxa/PULk5x/cbzd/+OV3QPp/S0Yputp5UPiSWXnke0375cvPPzSP2z/88vMPXQmi2LOyL12d/hnNP7Prg88fLPi26sc/7gX8tTzJiz5ffM2hxW9F+T/q318XOsA/99v95tPi+0ycP9BiVuKd6dME32VjA2T9zo4/vfwOYCgH2nTO4zHAj3/7t8UpcuqiKfx2oThF1y6Ag9so82bh1TACOPoAQKAAsGsTAcO+rQPxP3t4lrjwF7/+T+eB9B+dN6SHZ9T+AmDN+vIdXH8B6PnlK1x/+QbXv74uVMClqKMA3EsXMnm5fM4BQuftLEFZe41X3wFq2SMAfZDcH+cfMyr/+vcYfXnQfC3HXx9IHj0xUd5xMx42Xeq9zpoboZe/6emAyuANntMBdmnhANn8CKD6B2ARwOwO8HS2UpNEabpwI4A4oLSNzyrR5Z9mYr/++qttNeHn/Ang6OJZ8xoYLPgqzuLjR6Ckn0ZB2H7OPScsFj/89vsPi/9c/Fe7HsRnHhdQVd78BCTklbO4AHnXZWDZXAoB4Fvuw0+//f5makAGVNsF8GrkR88qN+dH4rnvdldY8uNqgy1sD9gb2Dori7oFVWERta8Lzl98lRcwnR/NdSMsmhYU7NLLXS93RkDVAup8tWRetKAmt1HjgwrcNd6D6692bT1EzAAAWO2vi9PuAqpUkYJ/ZjEfi8DmIo+A+b9GxfM+IFKD2ku9k3hdiHOkLkqrtsqwtt54+NbTL6A6vW8HxK1F7vWf87k2e7OpHmnzNE8w9yJz8/Fw6cfZ56DvyABGuM077+CtX3EX6qOm1p/z5i0lrNp7NAZAlHERdCAmQaH4j7eQasKiS92H/YCkM6U3L7hvXnnE4HedwSOc/rTLmduIxdxHLN6ap7n8ditkuV78f9RNzeYgDweZPpAqvV/QoiqbTzfN/eTszmcLCkR5qPRIyW/9zTuGvUP55zyNQMzV4388Vz6c+7bmCY9dDXwhk/KDPogs4KaZ7iPw50Cu6zllrM/5e80AmiweAAl8D1ACZNEcvO8M56fvkoYACubrb/3Dm86zLUBwL8rOToGffM9zbctJgFT1nLxvXgVZ4M2J3IcRsNb3Ws2+APYC9BdAiAikI6grr19x/Pn0XfQ/bHy2SfOWRwvZgdytHwSAHN4s4OylPmoBhFnts30Hen56EAFqZGU7626D7AGaPm96tVd1URO1M1I+7eqVALM/zt9PTee73lCChAHGAmlRdsC6j0SaMSYDTRCQAYQryCsQj8/gfTPCg6CVzagAUPctfp4UH7ffFPIe2TdXs/eNsyLznrlBWPhAdHBn/B481D8LE0Avm1c8+P5zpH3lNtOeAbQBIAg4vj99dhKvz2bg2W0s3ul++pf56Me/N0I9yrv2xwD4tAjbtmw+wfCzJL9X5FcAX/BT1uZRnT/ORfPjX6b/x2/p/wcuTwN8Wvw9Sf9A4i1TPi2Wr8grMj86vkXa2wcYZveRMj+u56efc9n7BrWAfZGBUJvdOIJ24GtdfF8CimNQA3ACi591spnLaw8q+qMwAJ98zr8P/Tn1QN3JgzlUm+I7SHg0CCANni78Wr/Ao7wFvN251Qy8edZ7JErjvXzKuzT98JKDIPybM95cr7I51pt5SgRZBbq4NvIeVw/oGNr55x8H5vPjh5W+gjoAYCptvo/HtyozV9nv0uapMFDUARw+LNwHJoNQBQrPzOeUs5rkURlmxdqxnDV5joNzA/mA/S9P2P9XgZS/qhAzGj4rwNfaA2rAj2B+tbq0XWjKifnpT/l97Wb/lZkBmoWZrlt8muvmhzcsAt9gAgEF532YAFq+jXePsTzvwOT88zzIzGZ/bJl/gD3g6+umr/85YXsvv/yJXE8tQMsJ2uV/FU3sMhvEGsDpP5RbIOx7lH7TfbX5c83fS+eXZzT9M4tnfZ3r7gyXj3idF35YeK/B6+Lv5ffHFbLCPiKbj6v165A2w5/I81AZQDoojLP1vrnlm3GKx8g3iw6M2T7/h+K3FxDU1izIW1i/zQxgOUDAj83cD8EABQBDcP3MV/Ds/3KaeKPWhBboXwE5ZLvFCGyD+rbromsCwf217WO+u/ZdFPd81EI32BpfEoi3wkHNXXoOgYAlG2+1dDybmKV7YsCXuQWMZgk3BO4jBLHy18sV4gJfrtauu8W2mLPBV4hF2NbG3hCW/W1rEuXum9pPNWebfh1sZvO8af/bi42twUp23XDk87ODoaUNG7g9Hq/wFdkOaa8Lgm0UNmtNxhigDHQ31XAXOBKHryB0x8iKwNKpo43KlUVNukdIH5jR5KH8nvNJGA5yeiayrB0Ri+Ipeir7jTNtoM3qcoi70yluhUQ5nwqCbkp4J2mnYr3SNAFO7yEXNNFlh9KNiCVrImn9Oy/w0wUZJ+fqw3f+ukUaY92kaqI1cFwU4y6RuR493Uo2NaPd9UA1SGSO/YinSKIU0n1XD15JwczW9f1LaAzXSzYkdHJL3Wav3VRoF3W6hedhYyZrSI45gxlzyNMiVdleZJI0lKzhaDUPrp4x1hchoUXusiyLqR2oG5uhW3/XdBvXtPfkxr+rBe5dr2u4k82cH6ELEJiG4GuSBvfeZPsKFdxNtqPFpdIVCEf7nXkvysiT7bGojkJEkZAtyX3rpBRUBmZXLCOLk0OJMqhD2B2bLTfx0HBIxoMSI+H5rgz787aP8S3p2Jd1ZjRRNADbpduRF+jhkPeKnqWrjGCPyNIXcMJMVnAzjUQSyXblu0cnjAPPNrjCEtL0zO72I07RY0TXJyRRLZlLIR5jNUYg8g1HbUjVIpue5q/rjl4Hzd1DzvD1vBVHKyyNWBU5+jDbjDfoU+eXJk0rFqbYGBY6e3gcJ0FkdEPYa5hJwbF7U26tBx0M+mhV7Kn0YJ2hZclBWKNcj4cRWplwnRxdfg+pB1WSkrDUjZsu7yuIUNibYtaNz+zXgQOULhyxCk5pbl+GSy+KZ5xt1IMp+UvNRoxdYSGktOFy2t8iaEqQPdL18c61tyCElYaV5DKVlmNJWshp752y7upqNe0layVaHxsNG7I8tUtG85RT6EXsBRKCSa/UUBhlv09sfh+dD5uQ97ZkDsuHgsujFglve7OB9tJdrvYbaXmPNZzuRmw01cik1H5CLjuCE4cLY+3p0B3gfQujwzXe+iK66Y4Yt7oMhj9Uriipd0Znp/Tim956i/jt4Vr6w15A/JhRIfG+ZfmeTx2roXnr3KJkk4S4gbNmFB25AusbPrM5kLytE5AS1Z3qgWHWK9mCAtc1U1YamvPKuewGE9pmwv4ockfQZ+C3vShsUerKc8lRMygdyfjSOXEbxpYq8oSwzZQP3TV3YMZByaGgkbVMisz2NlYOeoLGk32aehNzSViDAvMa1X5HIO3RrLhUP42+Pu1QfTqx8p2xxTtzEKttWhbykalH1qi36HTaVeNKhM/TVfAPU1t5KcdfLTSFSZehsZN588ikQraTAxxyYtKAKDQbhBxjEvdzcxUPiu+SHddV0jkoojgnTw2ZX/TzWnGJCnVPl8EzturZ20yi4FCIxJsWeeJWkwozG4q8lVjHGV6B7UyTIKbM8Dt1f9LNS19NtoccjfY8+dI91QjK0TeHpHbOtRhquxtmkuYUdsqUncA8gTrLytsGiRRIiMDm1+nuJnh5Zq6IQm0Tht3DK9FjfFZEiC1yYu5sYkuWn1H4gWTiXOzboZM5zs3xk98rybIhl4WjYkOQq24QyNeDiYeBQ+aKH0p1VjRVlJyFcEV7R629eGOBn2/hNa+6U0GayoWFfB0WAs8C5sREaWfV6d3Du+5kT0Ztqyf8KJhDuabQyU7Ww3aT6E5txF65YrAjluNnP9qSooBnpH5jybyRbkPD0GXHhzFy3zkWoh4rZBBGSufwytWWRc9GSKBXoHHsbZ+7GydcTq7xkGzJyAS9D6wPYTHAmHJwiuXAGHUsKgdNspomI0Cx9LRlFqqVeeoPJEWF4YibYsckyk3F2L7doKvlKVenmsOkBHyc6ChQleKssy2SJHxgER4x5M2FTONKN8lrcm/8cqlcdnfC9pamtB/kqLcsd0TFGqew1tiJDLKnUsmmRp09cpF1PDPLk7A/WPCZXSJOXkJmvquVibkU9CpHPN3iVWiYZF6cGs2LRiVmqQiwhAGdnbEFGRXH++Fui+0SYlEYhSoMglJ3226uztHWXSxJL3uxgbfGkWNIzwyMLbd3LieFiRDeti7pKaiqwy7YoOY1OxyqCr+eznVlR4yYYGg2VkklaGReth0X7JzzmZNbrbgElhD3OaObY+Ds2YsGxXLp7yKTZZwyO7lsZhsnstzdrVMm3XojzbrzCd2ZYXNNJGO91VY0L8YmSjvGMnHcFi19O2YncZdhy/XKhTrrdj3jAyFUEXkL6A1TujIriiub6MkqadBj4BRrjTd2G3O36VNBom2BmbyORfdOSS77rrny/Wac9tdo9HD3bGceehD2yAEl+9w542NVB4idwUcOucGFWe8yOeRVIVRd5lreNAhJ0qSC+DSl/PTM7Vvh7BOldmyl8iqQGmgj4MJgbmRWXvpDH6GJTuoUfCQ8aNTHsuWCPioiqbfCdVjw8el8T5xOWI7HVTXKpoVWPUrJg2C2EX/M85usH6pbZF4PTjQFYkDj1G55izC+3njldNjv7724W4VCTGeaMznLbcDvBh2ng3Sni9YVnQ5JCO3ggxzL9DGN64qZjhF6LsWBFtWblxZHVdoKpVnu1NyNSTM4R9oGqyK1u8J6xEVFsLxl15CKe7wctf3uGOwHmxB60KaURr05kbc+98z1LhyTUlYltYyNLmS5cpOftAKJsRArtTKhYG5vceeVfC5WZgNbp5AtlmSokX43wqJM9v0Vp8ub2h+2m/tqMJkCi3hNagm/7JiVv1+GpAPrW2ZoV8OZlSpxu2OFTDhiKLmk2KJjOorrFY2v/PvUbLp8rzkHf7Wni1XMwSp10BWvR2jl5tn0Xq5y08Iu3I3nOj6jA6WMe4bwqqDl7TNi2ivuRKLkodZ2FleWrr3nvf6SBaCxXW4hGR9yE5Fp89iUfEEe9+7S1PKijHGXb7SIgD0UR+R7QBWWJ9z1qbzBZL8RZK06S70nHK98JRCh0OkJLqJSRB/aZHM+EMd1O1Z9gZIMvzUQtJzArCSLZCdR1M7oaz4WlE0BH2lbYuMxQ1Qj7YKrI65YGEZ3DtUahz2DsgiXCtxo+tgZtWUKz4uzNmwbOk0HJsUiyeeZwbFb+djp0x2+nDbcRj2XQno4H3hdsZuCDLmkVYSyZxSdbo1wh6Uk6sBELK1JIYtVt92MqVezbFffmmhNtawWs1gp7SIKWvJIwpgYSOdrgNE7+kqnO6oNzFzIAqaU/SvLESM6TI5V7yjNp7boShfgK6Gzu9JaHTmTDLjtjd5GFHxG8d7xdJuh8EH0SC9fGia143S/Jcsq2YuRjQVbzyqL7CCYWL+OwFSbVCV6C7BQ05Igvd+0/ALyLi63W/9+bKELq25v4v3OEcPWZSYb6rgJ4q+DLSo3od3eYlQfPEhnwSwU3SBTvskjupP0mGNNLoNuF5HWdxDmV/mmzq6iI8mceOa2aSYHdrwmwXBRMJlFCvR+FzG35CAZinEL9WgXZKGlSySIvEG1yRUsFR4SDiFckfBdyElx5ct80fnCeIF9VMroyeJDtdvzdWfqN6Uf47VKd1uq1/N4SvebfW+UAR0t9fqSQcq9GxTByynIY2tiDWHeSsQ1t+wzer8iKFw3Oh5dF2fG2Bc6j2fnpabqrnsTkQMnXfkDA6YiF4lXQWtTSoEEtHTCx0tgXFKe2YUgs3Edbmy9JOzuqrrIYHZquoIvaqgK0nFyBnp9wvZqoJdRdjgP7U7fqzQWYcuLludI0RToGOdcRVdX9eIaSFTDnX2DjmyPX9Ql5t3dHVZJroWsl8HaxEodQJW6tk6OBDrB1gBh6ohmH5XSnoms29KPkTITCWN1OBq1qo3a5oRiuaWzq6zaGI0ndfQ5XWZLc0PXu50Rso3kbQt3VW2OlaGyhHSxBxHSLtk4bbmClpn1ssy2URegZax79kEV7qbia7eqWHFcHzTJmO6Yi++rRShJ+ao2unF/L+Qzh8XbUCExw7sLtL9pmyFSeXXCBzYm4r2SVW1qxcc6okCphtA6gdasg+9EByoZPojdfqkS+YhinliRy1Df00hUaaK0XoKSmaSxI/S3blzijJ8KsoHqGUPu6IxCe5nWsaujj/GB7IYAdr37NeSUrmrq+lareE5Yp7LaR9pasWnoxpV2eWVadWhDrGfc+1LxMDq7Xw9uw/C4wfOuFeXnpu/XGqdPh+UG7k8KW57jluHK1Yk9ayWk7uQ8qq2xiuHoOt3IRm2rzUpZbo5aAaDVt861gVd+dmH4q6et9tE+DsiIYPaKwyfySdr00Hg/sSTA7I4TkPUtC9Juv+/RtTA4bREakQxfUcUO4FrlUVuDT8ieYPAc5VhXPl43ByiOLrBprCj9SrscdhVvG1XeNoS0YeiLBOuFsJ/OcdU1PY7uy3M/VUt/mRS+WCEn9Eb07Nk7pWbLUqjhSzJ0jCDTLMXzsL3HSYM7shlrEC5YLLQiM9Q5QPcmFKtVG8XpvtYl3Kqnls1hc8C1K76xerxBr9zqlhZ3735eT5VmR4lWu+cEipElD8WaeNCJc+/h3BihaZ6V+/bSWLnJtscN4hqNJQCKfYl7wjWCpf1UGDZI9LvSQrvzElRJQxU8WpN80ZNagUfkAJlY0s8NOOA9eTwUECiFUr8SwFQJsZQAeTe70mF1C8e5ceu6uWSewq3B9LU9dtUymOyhReuJ2p4vvOUI3LbrEaZYs50Iw22NwpSPHwxHM1c1i0MGPKI9c9nfoXV0XeI4ZFW9xCs7UI12RBiyMaJjGOgr5RTW1hIDS+vEP/Po+UR4PUlvC9uKOG8IIOqUyJANg45zUm6T6bTWjVEmfeoqMUrtVdWuL+d+edMMuoFD+qjfYzVn8pODF8FAmKDnveQ+T2loVV+cyOwmYwJQQ5vLLUqcXWKVmuNtCPnJ7WPQBlaomHC26t+Oh2roKbjO1tlF56+wh+v2Rc60Fb6u+HDaQEcj8fCkuiwLTFGuSxO2wsZzQuEW0iJHVTLHxtN2GabLG5hJjBUHqvJQ15prnq7XUWHsBrSrXXu75R3C6+t1L4jHFdXKyLKpwQzs1PeGG/ZUjiW3BHIzP3I7JsCkdghkrIClsVT4g7W/uBcfAe2WcdYUiq0PpyNaLMMTmgpl1ZU0Vht+taOa0xIR2105yWRb0zphHRr5DIGJKGmMLd5t97ekXzc5SDk0S5UJJpzLFd9uuDz3vOJI3SgmJEfdGLHb6nYPGNEvOd1G2buzyUQ/NF1zyXi270aBCmrMLR828FruD+7peHCXIOzNMe36ZqAnj0pzMehugYU5Q9amrJGu3VXT9NuAzZbNJBPlyltZGLZvk6Ez7qJzHpFkoFLPlexCGdu1CBVchd3JEIBdbqbHDRZtSgc0T4RomVvkxmzC6dyeD5PMXC4OjRFGNqFclJ1vaadsmHDcV+xNjTCLSjHYPrITiZDadUm5m12+LDYh6SkXtCHKlBxqrrrIa2rDruSrjo2KxqJXpkitdaCiZMvfjzoRr6daXeVuWl6cFbS7XvMLexL1XG2kCfVzt05RgcYloPkVGhzV81b3KXeFS5BVcTH5jlX6zP1OmFrl+IR7uyLilSHDHGui+32HEccAK/EUSfV8vYMjd0wN2apgVUohq43WKwLY9pgdNexWLikKlSMjvmD+mXLNbutABG4Pm/RY3bZeSaIHM+C1yIyxPlXu9t6L7TCjuUHw7XOMJ6cpyiHiTpNHg9GPEATwfl0hdm83AWgE1kpQhRcGP4EoO+eE3qdUHueSpJxvB30bptfGi7bqcjPweF8uM6RObls9GzFlpV6xQb4f8P2JUeraWVr70Z/ka6L7JoHfpMkhq7qTNJS5cIIEEFNGSRQrQrfaN/Y9VDhUcZFtAbMxhg9QRmB8K8DHYw4m17S2Vt2k4rJ4P0paBesK30yhoDEHorPdVjht8bS9GSvbmTQg87lleIuq7q40iSzRGX1ma4eVYk6Hu9bG1ORgqthO6eUC+esi8xrCShrVuYm+KPg7geubzBtEH0MdMJuvN3mnoCk2WOAhvyax1u1z0Hui1yrxp8g73lRvKe6SLQ9tT2f3tmnXyNbLrq2xQffwYU2g5mkcYPlqiAoo5/z1rk4JWiNXkrrDScxNsVUQXHqha1rGePRI8hvpVJ/OLAR7sMtiSdDnGDZZWHwN9kLotet15wKdj66JbfB002EymH2nSu+9y9Gr8850M1fBiqmWnIKINddvnMHV7NtU7/qboXCH9sBUy2U7xnATt9PJow42uwkQDMKW94tNZJzD+0mnrE4kovHhaeUFWLvqPYsVCSJQ0FVBUPs+MDe8he9oZef6Ft/vMfOeNqRzjo21mHSG23ZolcSFwR5CRN6CKTG0JlnP2atbh75EjJrrFl2Ip8z2UMVesxXuFRbfwTyKxGVbKxqqW+5WvdMuXOsNR8D5yMLXNtzXuN7bzr3JpQ6iPJTtOfNc8/1q06bLPtOpSVeNdkhWNpwgIurDaiwcRq/fwlZnbtzJqChxfXYNWxxb9NDaTZhljCf4m+7QOjjr7o4rTGTOh8q+MKc7CPQWQSDUQgd7yUuhX51P9CXlEJ6MyK40Lu6tCoRotyvxAhTHI5Il6wubTtrqGl+VoNk48rQs8x4LalPVokZn1X4rnAkwM6IFSrfddYkhEgbBJ7c9dMINXuKEqQ7A1yu4O1w9bLARhOg9/TzGbe0zGDEJa2ElQdSZydylUESbcEUxaprs73YNOlgmh2HRp0rpjJPabYIygC5FsjyM17FLnRtcqOkW4lb7xPD7IsXHzj86iLe/L3OP2p6WO5Ik//Hy4WU+Gns7kP1vvio2n+H8PztKep76vL/78TiJ9Cz304PXp/+ugL98eKmdCIj3PEprwCz8dtT0TwdpH//eweBMa3y+mfV+Bv084W6tYH6x+SXK3a5p6/ELIPV4KwTssLtmfv+xmV+RdcD398esXxV8+XqE2hZfnu+PvcyvJ85ve3huBMR4uwzezhnB3hG4MXKaLyi2+eLV5az125sEQFn0FXlFX37/X1qIrH+OLgAA -->
