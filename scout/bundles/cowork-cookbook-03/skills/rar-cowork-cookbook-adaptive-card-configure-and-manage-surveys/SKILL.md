---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-surveys"
description: "Generates a read-only Adaptive Card JSON file visualizing configure-and-manage-surveys status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_surveys", "rar_sha256": "4f0c46e7b43383e5913bac153c2a24d98f3a9976a25a839ccfbe918f7bbf1865", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_and_manage_surveys`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_and_manage_surveys_agent.py` and in the RCI capsule.

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

Configure and manage surveys Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing configure-and-manage-surveys status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys
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
      "description": "Date used for the card timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-surveys-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_surveys_agent.py` and embedded as the fenced Python below (sha256 4f0c46e7b43383e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_surveys_agent.py` first:

```bash
python3 adaptive_card_configure_and_manage_surveys_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_manage_surveys_agent.py   # or on stdin
python3 adaptive_card_configure_and_manage_surveys_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage surveys Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing configure-and-manage-surveys status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_manage_surveys',
    "version": '3.0.2',
    "display_name": 'Configure and manage surveys Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing configure-and-manage-surveys status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-configure-and-manage-surveys',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a61968433387527c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-surveys'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-manage-surveys', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-surveys-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical configure and manage surveys status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-configure-and-manage-surveys-2026-05-24-card.json' that visualizes the current state of configure and manage surveys. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current configure and manage surveys KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing configure-and-manage-surveys status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON for configure and manage surveys status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-surveys-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of configure and manage surveys status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConfigureAndManageSurveys(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndManageSurveys'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-surveys-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardConfigureAndManageSurveys().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6ebPiVpbnV2FeR4ztJvNpRUjZURGDVhAIhBYQclY8a98XtEtuf/e5gvcy7SpXT1XP/DNk2iDp3rOf3zknr359sdomLKqXLy+qZ+ULwUrTKPSqhZW7C6boiyoBX0Vig/8WTpE3VWS3TVHVL59eXK92qqhsoiIH2wUv9yqr8eqFtag8y/1c5Om42LgWWNB5C8aq3IWono4LP0q9RRfVrZVGU5QHM1k/CtrK+wyYfs6s3Aq8z3Vbdd5YL+rGatp64VdFtmDH3Moip15gxGrB/0+VkRY/pl5gpQsvb6JmXOiqxP/0adFHTbjYy7tFA1jVnxbKRlhURf/poZTlzAIvgBZNkdevQA9vsLISLHz58vNfP71E4PfLl19fnNSqwa2XDw1mBZgPSTe5Kz3kVJ9iAiqplQdgeTkCc+bguvQqv6gycMv1/MX71Y+1l/qfFv/+70lvVUH905ev+eL98/Vl/qO0+aIJvUVTWHXjuQvHKi07SoFyr4tN2lvAIpXXtFU+m7kG3siD1+fO75SKcvGX+dmPTyavgdf8+PWlKGf3ANW/vvy0KCrAr2rn368zlfLHn17ToveqH3/6Tqdu7dhzmpkYkPr17f36nSxY+H1p5C/eVJlj3nlVnhOVHiD+O/3mz1P0d3LvJnl7Lv6xKD8t/pzyrM9fgLzPeLMB3T8nC2wAdr68xkWU//jOoyo6L7dyx/vxp39E1gk9J0mjuvmn6P78JByCCAfWejcJiLnZBX9dLN91+0bzH7MtQcD8K5qA5R/svhnqH9F+ePZvSKdRDnLzw5d/Su7PNiz/svj5H+r2X234tPC/vrBeClKnsuzU+7L49REiP//gfr/5w19/A6T/j2TUoq2cB4U3AA+R79XN29vPP9SP2z/89ecf2hJEsWdlb22V/hnNP7Prg88fLPi+6sc/7gX89TzJiz5ffMuhxa9F+T+q314XFwBi7vf79ZfF7zNx/iwXsxIfTJ8m+F021kDW39nxp5ffAATlQJv2gVMzAv3bvy2kyKmKuvCbheoUbbMADm6izJuF18KoXoC/M2pUHrBrHQHDvq8D8T97eJa48Be//C/ngeifnXdEh6x3cHtzALq9fQPiNwCUb08gfnsH4l9eFxrgUFRREOUAcZWNLH+dF+TNzL2svNoDC92FPTbeZ5DYn+cfiyhf/PLPM3l70Hstx18eUB09sVBhdjMO1m3qvc4aX0Mvf9fPASXLGzynBazSwgFy+U/IB+IUKSg7zWydOonSdOFGAGlA6RoftIEFv8zEfvnlF9uqw6/5E7ixxbOm1RBY8E2cxefPQEE/jYKw+Zp7Tlgsfvj1tx8W/7n4r3Y9iM88ZFBJ3v0DJHwUQZBvbQaWAdcBZwMwefjn19/ezQzIgGq6AN6M/Mh7bgbxmnjuh83V7eYzuiIWtgdsDeyclUXVzNU0al4XO3/xTV7AdH4014uwqJuF65Ve7nq5MwKqFlDnmyXzolnUIChrf/y0aGvvwfUXu7IeImYg8a3ml4XEyKA6FSn43yzmYxHYXOQRMP+3iHjeB0SqH+oF/UHidXGcI3RRWpVVhpX1zsO3nn4BVeljOyBuLXKv/5rP9dibTfVIl6d5grnXiJx3l35+dBROkYFgcusP3sF7P+IutEctrb7m9XsqWNXsCgeUBsA0aCN3LhD/8R5SdVi0qfuwH5B0pvTuBffdK48Y/NYJPILpGcWLj55FffYsf+x9vrYojOCL/0/bpFnnjSAonLDROHbBHTXl9vTF3BTOPnv2kTN5EJDPvPvevHwA1AdOf83TCARWNf7Hc+VD2fc1T+wDerpAIuVBH4QP8MVM9xHdc7RW1ZwX1tf8oyAAsRcP9ANSAygAqTJH6AfD+emHpCHI9/n6e3PwiAZgeKA4iOBF2dopiC7f81zbchIg1eypDw+CUPfmbO3DyAn/oNVsXxBRgP4CCBGBnANF4/UbSD+ffoj+h43PHmje8ugPW5Cg1YMAkMObBZxdMvsLiNc8e3Cg55cHEaBGVjaz7jZIEaDp86ZXefc2qqNmdu3Trl4JQPnz/P3UdL7rDSXICmAsEPtlC6z7yJY53jLQ4QAZAGCA5MmiHFR8YJR3IzwIWtmc+gBa31vSJ8XH7XeFvEeKzaXqY+OsyLxnrv7PcLXy8fcIof1ZmAB62bziwfdvI+0bt5n2jJI1QDrA8ePps014fVb6Zyux+KD75e+GnB//tTnoUbv1PwbAl0XYNGX9BYKe9faj3L4CjIKestbfSu/nuSp+/q+S+w8cnsp/WfxrUv6BxHuWfFkgr/ArPD86vEfZ+wcYhflM3z7j89OvueJ9x1LAvshAmM0uHEGt/1b4PpaA6hdUAGzA4mchrOf62YOS/UB+4I+v+e/Dfk47UFjyYA7TuvgdHDw6AJACT/d9K1DgUd4A3u7cQwbePMA9kqT2Xr7kbZp+egHo5/0Lg9tcjLI5xut57APZBFqzJvIeV1b9VvhvLtBmvvrjwMuCu3OFc78F2uzJR7ADNM4eOfbUZBZolrMZy1mw59g2N3oPRBqav6d9evyw0tcF6wH0S+vfh/l7hZor9O+y8WlLYEMHKPBp4T5qDBAMSDDrNmeyVYPUAML+qSyPCvH2rBB/ouxcS/5QRObyP6PinMOfFt5r8PqoK39K+1u3+/eEr6CpmGm5xZe5vn56hzPwDSaUT4tvwwbQ6H38e4zseQsm65/nQWf24GPL/APsAV/fNn37Rwrbe/nrn8n1wLy32UnPoPlb6Y4zlgGsnw38j2o0EB4I4LaO926Gfz6zP6MwSnyGV59R/LH4Na5Bi/P3FgSiPtAc1MRZ6+/m/K5U8RjlZqWAEZrnvzz8+gLiGkjTWO+R/T4LgOUA/D7Xc78DARAADMH1M13Bs/+LKeGdUh1aoDcFpHAfdnDCW9s4hpGYt6IQDFRUZIU5qIXiLkX6mEVRawIst0iMchzf9iiE9Ne27SMksQL0nun/Nrd30SzdLBowymeAIN73x+CW+67WU43ZZt+GkkcqP7X79cUmcLByi9e7zfPDQBRiQ9jBVsrDMofJISRqIglr1T31eAt7fjWKh6Zu1hZSpye7vcCVGHB0pEbcZtOfGdVTy8tal2tuSWjY0aE26GYTlIfaEAjNIZOUK+OS8BLfgJa3xJPwYCnBV92opNJnNHg/UMoROtz0Ozm2K325J8ldo0aWfJ7wqlCLMpZ7iJehNepCvCXGB4whMu6AHcqQkuDI8FzHIEkfok7VXrxF92aXGrgDGZ5ecZdzpfm8l54orFIsbZkjlzwjeNVbD0dKCBRR7nL4bnSYvfR5W7pVKVoseW13L9Bd3k3UcikkEOdelHrYLt0u5Pg03WmOYcPXViupm4bhvcunjBldFZPPohCT2JCA/KpeeW3MjpQ8SA22JVdLR7puY1XNmHRz8dO0hstxV1Giw4vNLnJYGRJ0HZ6O5H5i8IlXaflKbh1bkyBjwrQNlORmEQr8RqC1mxmU8CS21DahIy0+l0YHiJ4kMubazeZchFc9vATXyyQa9HbrKKVzyy0FqTsFxSs5tkiUYrEDPLbmkkuC4qYHocsMxFnwUrLGmVrZjzlb0is/iEyNy5JOVXYlLFo4ptt0ub75SdYud02wYfUb7yN9ylEFj5YUdZEPXnbz9CKZFHq4t+JePJ5Xce8euDCKFYW+hhUOzLSFNzp6EhwL3y5t3tbK8kJx6F5c7rfySh+y8s7QFKh2e/tQOZqXYPaK88ZkabKbYrdX0UO1U84yoS73dSw0+WoH7cIzHx98Jcm4od92oENdXdHYidFjz4ZwaqUb6HhplZsQbD1yp2WJRsJYCDFndLL9StSqaVdcdn1z1DPkoO/hY6VueGK0EB9RkzMRl+JB1G7l5d5590qTNn1uMtj2tIUvvKsSJ3hZwx2pdtR2L0KoCB86hOs2JgSfLUbEK3d3PaMHOYAvqHyGDkRD2vmN567ZqjqaPS2xEkke4RaRJKLMum7b7K99kB/X6eDfGK89TqSRkGioSmdy4pElHlPD1oOk9Jb6yTZQBtmA+h463zoadUf7tinLvaEdrHF/PDjauELOZ2WVhmZ5OU8D1Dk4vacjKR4Y3qkkF9rsu1qNy9uVtU/b1KhlQTsqWapGaF4u0XN3bZv+oqoig3L9vU364y4sRasrdHjrsF3fSZUr6yTJTw6LFmocBJg0mMlBhLzJlqp6OtCxSRz8TV+kWEBA8HC3LtH9jnh75VoN1kFZ4STITXl/uhYqn9JcpecJk8REl98sdUSP1Aq57P2tEt7PqXhAo2kUeviCXAmYdo+CXC+FO5TxHWLdfE2Qkorhjh5Mps5NCpyTKDCrQ2hHQbpxElZm7DxLzyVHNiuv2Ao1kqzDa5mit/q6LRTxpsBSMdZrtCWPUsspycajT5oo03XLbh0Q05Dmc/66Xto6JlPcGIWoEfJiGgiSiJR83dyQDaa3qeppe6pKi8qiNWZ3EjdCRGsI1kWndR4hFH82LFTpJ4oHgKZgnCFvFYUNuvhE54Pu3GilbycMxONAobh4kFFhG/qFfeOrM27xgXK6UueN2kglxCDAmwmkxtej6Kb8ztEp7lBXOXNU1zsswPKmaIqbVWsbsqdWe9U/nibMi5bxpT6dsh5ChthsEXsf5qaYb4/y5hQfbvnFPwwXfmwtd80GdmtMMlr5GMERPBAquoIRvj6bg7gfiYZZrtaYkV29JVUCSdi7mOunO8VvLC3hVuK6vPJ9elkzNxyVBzzwaMVRdrbRA7o9FKv8dRfLV0LnrPqeUb4v04ia+aOpJvE4HFQ0KrQDPhHWDU+Pt6JsZNHyKskSKJPDd4mUnBNZ0dpxn3JGeZc2IOQnu5JvR0oUuJbaVLR56zy7ETYS5uqnlVZsoqSAYbk6w11h3VfuAaluDHPHj4xEALPe+itpl05imtNykG185XdxA6lupI3jxMsBNxqwdQFeXZaTIjZYrXv3fqA2DXQpEMxHzpue7w5sU+F9tx7Wrg9BLex3eT6upMT3OwgmPZK9IW6WpDJ7rCHyctjwGxcPruSOdmR5H6/0JNkh1/sYFDi6w/ITGTtBjyC+XQZqK3n+VJC2rylQvMoSsx7xA1NyzrqWwow8nXYh4hRycN1rfc67NhO0IKn3ypko2VgbQOomOlEJB6EfUnF3igfYjJHLCS77cuxKfRJiM3cI6ra/aIqdX658ikpX/6adMlQwEv9i4XeCC0i8PYLZSsbI40An54uyL9piijLZJaUNGkzYGV9diiQsD2ai29rI2ahx7TbGET6528NGLWhY1tUcdgUipDAByzM8xwNc5bQtrmO9H5+vRSYHtiOyqLsp4EaSR1u56HdVoU+gCS+a6N7F+44UBW3X6peKAHXUlTbUPaHxu6MO5+XlFMp6lF5uhmluJFRdMbpwS3LJvcn81PncgXPa6FwiiCLhzLktLNU8sNWKO0eTE1F1naB0SJA7XJfU5eGWafsVrJvKPbtd/FzXxH7bs1CQqCtVu/BUp6cxHdv4kb71KR1j+y3fRW2fTuJ1nFQ9PBKdtxbz/b1nyTuapEK0M2xu4qqlwS/dyo52VnbH99NYlMakHlJt7bH9meZW02Bc8CsRHRh1S/NNPZ27YdMQLqfIdCdqO5oXsLsZCk6DWT53p7UImrZHXdVBchJ7U9ovh/3qXOFG2jP8+bRDkEofdgN36bhjtS8d7XSFGu6cwlYw7Wl/OS6rSAnPvqNmjczrjmWUPjxwOjKGuVy1UoBgoNaZDBVrPXai7IvjMMpRPJdMdW/L9bUPkYbuGoVKio1qdJCspeTtGodTezARehzsoN1TZbWjN3J7a+hiMkvrVFYZo0ZeZNIJXYTw3jtsUn1Uke4a9bG22Q8Kp4vaPcXFbN2vbwxRuGFHnIyDyNShlO48wyn25c639ajTpi458Gwfaa4x5ZeEE1j4tGRAXB+LzDTKdkeaO63otuOaVwpYYq/jNTFvLlStNtvLYQoVEiunskFUd8jO1sBY/UGM7ilfQkl0LDQE1/agObhLF4x1Qwii8CSw0zSY3OGUmVp6ybbLvFnCqrfas6lU7MZjKl3OskjriUvXaXofWeMCTUhOy7WjVvF5B+LDQgvDSBim5M2E5eJ4V1QVer+KpbFubezCkebVqKLwTuKrk7rldqdMoIRzqWFczxjZcuVboNWFRHFVmwkfa2vZ9I8+QEVuhfZoDUeiAKdEeD5XWGO2QchIYRiog6Q4JXp0bW7T8bzCkYOR4iWOW1d8H1tKtE7SHXq/jDWdrkNdLRKUc49OeyEpy2YGOV4H+arINydyZ3g0NzhElNFwtjtGPWudg6W8E2X3VsGuXOHCsJYYEzls7Mt4pG4bZBlaKQHf88vlglCh4af9CBPLoWl32bYxryvTJrdbPFdCcqPU8RbXyIGsMxGWEmbYF+g4aIcdlRi7g3VqnVYTG8WxmkL3b7AKE2YgwKygxUnk05myOR+vfkLXw9FZsu6YIDCylqIMU5eRDKaWCy3iV2iCFNsCIatOjqCszczq1XAyptCjMZbqG6F2+b3vUNbNFZuLNa26tLKbdt/563PJiupdFoL9mYLKNjm5flS2aZ+xgZlWGcowATuWVSON4aVLok17hlWGVfrL8oZfDUS9XbLz8ajIgynfYcLwS8e9WOvNFO1xbqMdLk3VNQFGi6yZFKVYjHe7wKk8XpfHOob7c243zi3dBUq74cJeu5bkuSmbcHnf8ao58no29SGx2fPREDWgthV0qFZJQXtu0VzlbWmyMq92xpQN/no6mReJV5Dl+bxL92RLjLReNzBrQBkVQCtYxRsHVbZRXii2rObpMYK7HTJ2N4iI1vVRXpYJEnpiuJFY28ivwnV5LKfrycRLAtMnnHOjyFHqc+wkY7rnQPNxQfq+0PWLuzOl3AhLCUjhSRtXng6GHdM5b4Utgbq1i+p6IrY7T5L0yWSWSLsWuMoe8n3ubwScEi9nsmkvO+O8B8WFNEWWVURbYNB7y4vHvF9XCH4mzwiiISgW49flytbHDet5h1L3cXF9zbDubtCYwEflbhvS9G0P8ewQ7DlLYnkwAniCaKvNtdwmImng9xbHkkJvt+smkbGc3hKHHsVHuPYTflRi3kiq+7pOy15Dx0NsxKAmaR6CV5zcxcs0ScxOlSP46Mk37ZA4JoM6AnP3ksDCqTupyXf2iBl9WFzXAn0U0DzZFcvS2ztlIO7dxGH0iUQFlcw1SMrw6bocu3iCBlq92DnJ6VsxglAA54dTq3Vzl1bcVR2WuaNyZq/LQx1Uiil4RHkailEhR7xYIVhhHq/X9d3R3aHnXEzJbgh7RU66dJ0MnimnLiZTPrQpvuP9FA00iuR2MttbWwIi7MvWik/Csr6ILWbk9pFZwtNUdMgIm5h5CqdaO2ie67lDpxvbpVUiu/QElePeiRNKQyppQhWKzixDYjA4QKzcgmJvU6AFSxxw2kMGDT3BDcnVhhdjjgs6/XxICi+0ivuyWBL5Muxoh+sx5VQOqraKei48B/fKqtS8iO5TYw28aJxTyi58dWovNgPlNXs1fQ8d8PjoXbudSdyR7tB5txolQasCuj5WQQU0jAy7PYZ3iSYsBLCCoB6G7uwhirlB8iHkCPHxzTJZ/8j1XQUhZKX2kuh7y5Qfq5juJz4DnW+fXHyXppyO4ITY7U8JcjX0G1UOjb+DMWfwN4q6W4uyguRrcbesKQE/qohFmPkkK0Z1gnNibbFTTeu6K/M5lel4s4pjlfMkQvMk3llB4j7DYR3TtSR0MHFPmyx3j2UKbsEnFwqVJn3+4I5CSWEWS2fwaVTKTiqU1FweIvjqUxxSXSD/kktXcj/iFtWNq/v2Ch+m1JLhcr90uruCQiylnQicZRiTY/YracvaK2S4YCbRMXrW31EUye8cf5G3UabxeZpXaBauapXSZWulBhaH1QcrVtY2ViD+iqlr3DyxW6+znest6gbJ2HPeTjihu1S97BWx4m5bMVyqtXfYXTYyva0E6QC2hjqW8qTVltwSEuz7eVueiMQWeDY40rYqVgR8vI0u2erlAW9olCqESRyPt5Pl6aiSqhNEWXJewcvDtmq7gr35/YjXJjdsfMzLlgyJ7PMQiV2f7ZKbQGxD2DAuYgihhHAfj+YRkiacWTpFIUlJ14ERYOhr7ILuQjsQY7FnR9KAVcEb6h06dsVpSlEt2zhjlVuReZ+Eg29IbiNcRnhVYA17ZM9giLhcPVAUToy7PJ3qQwEG3ThDxQx3CsIW1gjJsmp3dG/OCt+syunYIOKQIfSp3uA4OuJIkSXyrQnPZnjvYwW34mhlhchIradDz+yYoiMO6xY7FsNhx5IwaOZiU1S065ncNlO8l9vIK08cWUrlVT7vj+vNNtuaU9gnNrbqrl1KEhXhmyletWCacIVBd5cUK1OEi54Mv2CSNTftW8qiJocibgKredTSszI5XJFDnPrXJYRAqjJAa8Rz0Iulb1swAFNbjLEb+HRSsxbg6gUKD0seC5msp+PhmNppYPMws66ud9CHFvBkVA0LWsH10gsoS3S9E+HAPnGjVxfMm3CIoX1TpS/JHgzuJR4g567CbqHN3kSF0CkU2SKF0m2rsQft6/ZKO3C0PFn8bjnQJGgsJgZ2td2thxImhRE5m7jiRjiEUm3s8hpnJxNZ84WXkJ6jsqSgWM21p31e7FquyRGxNmw6GqbYqTL5sGVMeX0xasNhmrV9npwNASqQg/Hybn++b9f79UaD9KGdaFRG+pLzTGu46X46TU1/mDxKQAG+plq7pdVjB+aWkipbLN0JhmeFHDoZcDOYjY2ubTXeHlc34tIIRHPPbTJToqQJJqO9mUG8xA63ib+ztiiZMVRflWDdUmKCrog892lUm2Tda6yr2IIQzrKjwnPWVdsQWYfYLQqvSLI/ijaYANlT0nEw415DQg26IxMkrthdmjsyMqh7kQ/7wshXIhwOU9U35hZk6EDesZOFWWjuIWwWyqsoUqq7g41VivtOC8a6WuZ9PTMv9jLbjOwZzCZbD5ivZ1SYJUgtgDq0yw/Q+XY+UKISut0BNJ+37po5ste0aHrKXMUdl5hTrPVST1NSjkbjvloXuZEnXVETgbD39RN29043oXRrE4lvUixysRdGFj80UwrVWoNGZLRD5Yk2K6MDrUOFnWk8W9KIeAs67Sxwo0nIFcaYq0LCEFSRHSLeCLJKBwnftbthIyJxkmy6Gl4KON3veTsA7ZMpoOuTa+Sn/UnSMBun9jaLYFF78lrCUJfBFi6INUBnzJJxmWcoE7/6F2Tra8aU5qyGOeX9Dq9x1cWh5TV22HUnp/KqtjeYgVagwfDtNnBJgW3l5NyzqqYAPD9UqXRno3tG2ZFYY0vx5rdQO211NyDD1RJxBnSdxTpj97d1hNopqGiW0dtHaU+eu1UmNE6+1ZgD2lJQU163mXrYFp11PFzWGH4q8xUMSlFF2lvGGKOryAWbE4CJxiyDO7FhxPV9V0dHGK0J2Qh7/erHhlo3K0kZMLEbs3NsaUnUXLZaT+5pcrfL4AKTulY/rmCFoKDarIWlYEEpBt1ixCQYYdlefZB6NgbHvXM5EYF7YAWCwg74njgvFYa7UoNYqKsIDXkws8rsYKxccs3iy2W3KXthtYHdYdk2PrGrQY909cyVJvjLAPeaMA3WvH3TrxS2lZvGk2mop9cJJnBowm02m7/85eXTy/djsJf/xitb81nM/7Njn+fpzcfrGY+TPs9yvzx4ffnvCPfXTy+VEwHRnsddddoG78dFf3PY9fmfP72b6YzPN6M+znGfB9CNFcwvE79EudvWTTW+1UX6eGED7LDben7vsJ5fTXXA9++PL/+g2OP6+dqFV701xdvz1G8+84ry+Y0Mz42+XwbvB4KfXtz3t3/eMGL15lXlrPr7iT/QGHuFX9GX3/43rEls/PctAAA= -->
