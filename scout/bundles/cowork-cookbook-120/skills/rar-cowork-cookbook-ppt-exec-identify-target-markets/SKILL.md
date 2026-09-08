---
name: "rar-cowork-cookbook-ppt-exec-identify-target-markets"
description: "Builds a read-only executive PowerPoint deck on target-market identification from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_target_markets", "rar_sha256": "1d3db7ad7ca83952e6f0e4b38de42f226e662c0c2256623090e33443fe21f190", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_target_markets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_target_markets_agent.py` and in the RCI capsule.

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

Identify target markets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on target-market identification from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-target-markets
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
    "comparison_period": {
      "description": "Prior period to chart the trend against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-identify-target-markets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_target_markets_agent.py` and embedded as the fenced Python below (sha256 1d3db7ad7ca83952…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_target_markets_agent.py` first:

```bash
python3 ppt_exec_identify_target_markets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_target_markets_agent.py   # or on stdin
python3 ppt_exec_identify_target_markets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify target markets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on target-market identification from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-target-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_target_markets',
    "version": '3.0.3',
    "display_name": 'Identify target markets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on target-market identification from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-identify-target-markets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-target-markets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3eb1be1d98915577',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/identify-target-markets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-identify-target-markets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-target-markets-2026-05-24.pptx.', 'review_length': 'Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for identify target markets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on identify target markets for a 15-minute monthly review. Produce 'ppt-exec-identify-target-markets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify target markets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on target-market identification from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on identify target markets from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-target-markets-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready .pptx on identify-target-markets status for a short monthly review, sourced from D365 ERP without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIdentifyTargetMarkets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyTargetMarkets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-target-markets-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the meeting the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecIdentifyTargetMarkets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPiRrbmX2HeGzG2L1Uv2oXqRkcMCC0ItCEkJLk6ytr3fQHh6/8+KaDKdnf17e6I+TRU2SAp8+RZn+dkpX59c4Y+rtq3T29a4JQLzsnzJA7ahVP6C7q6Vm0GvqrMBf8tvKrs28Qd+qrt3j68+UHntUndJ1UJpm+HJPe7hbNoA8f/WJX5tAhugTf0yRgslOoatEqVlP3CD7xsUZWL3mmjoP9YOG0W9IvED8o+CRPPmcUtwrYqFrupdIrE6xYogS/Y/63R4sJ3emcRVkC9RR5ETr6YZ/XTh8U16eMF+JkHHxYHZf9h0bdB6X8Ayvgfw9yJPiwcb5bcfXhY5tQ1eJzcFl0OVu4WdT50i64OnAyYXlZ90L0DA4ObU9R50L19+vmvH94S8Pvt069vXu504NabUvcMMHD/1Hw6P+wRH+bM3smdMgKj6gm4twTXddACxQtwyw/Cxevqxy7Iww+L//zP7Aqmdz99+lwuXp/Pb/Of0wA8FQeLvnK6PvAXnlM7bpIDm98Xm/zqTB0wsR/acvZ8B6JTRu/Pmb9LqurFX+ZnPz4XeQdq/vj5rQIqPJz9+e2nBfDo57d2mH+/z1LqH396z+eY/fjT73K6wU0Dr5+FAa3fv7yuX2LBwN+HJuHii6Yw9GutNvCSOgDC/2Df/Hmq/hL3csmX5+Afq/rD4vuSZ3v+AvR95p8L5H5fLPABmPn2noK8+/G1RluNQemUXvDjT/9IrBeDDM2Trv+X5P78FByDpAfeernkpw+P8P11sXzZ9k3mP162Bgnz71gChn9d7puj/pHsR2T/RnSelCDxv8byu+K+N2H5l8XP/9C2/2nCh0X4+W0X5AAOWsfNg0+LXx8p8vMP/u83f/jrb0D0PxWjVUPrPSR8KZwyCYOu//Ll5x+6x+0f/vrzD0MNsjhwii9Dm39P5vf8+ljnTx58jfrxz3PB+nqZldW1XHyrocWvVf2/2t/eF4YDAOX3+92nxR8rcf4sF7MRXxd9uuAP1dgBXf/gx5/efgPIUwJrhid+Afz4j/9YiInXVl0V9gvNq4Z+AQLcJ0UwK3+Ok24B/s6o0QbAr10CHPsaB/J/jvCscRUufvk/3gPhP3ovhF/Vdf9lRu0vLzyevjxh+ssTprtf3hdnILdqkygpAfyeNoryuXQiMHhes26DLmhHgFPu1AcfQTl/nH8sknLxyz8T/eUh5b2efnkgdPLEvRO9nzGvG/LgfbbuEgflyxYP0NWTYYJFXnlAmzABYD1jflflgHT62RNdluT5wk8AqgDamh6ygbc+zcJ++eUX1+niz+UTpNHFk8+6FRjwTZ3Fx4/ArDBPorj/XAZeXC1++PW3Hxb/vfifZj2Ez2sogCxesQAaCposLYDZQwGGgTCBwALgeMTi199ezgViSsBCIHKAD4PnZJCbWeB/9bTGbz4iOLFwA+Bh4N2irtoeIP8i6d8X+3DxTV+w6Pxo5oa46mbunWkvKL0JSHWAOd88CThv0YEE7EJApkMXPFb9xW2dh4oFKHKn/2Uh0gpgoioH/5vVfAwCk6sS8Hb+LQ+e94GQ9odusf0q4n0hzdm4qJ3WqePWea0ROs+4zJz+mg6EO4syuH4uZ8oNZlc9SuPpHjAIeMZ7hfTjHHPQmBQAB/zu69qPMc7Ml+cHb7afy+6V9k47h8IDNAAWjYbEn8ngv14p1cXVkPsP/wFNZ0mvKPivqDxy8Cvjv1qYxSuBF8z32p3d3O58HhAIxhb/v7VIszM2HHdiuM2Z2S0Y6XyynkGaO8U5mM/mEiz/0OhRkL93MF9R6itYfy7zBGRcO/3Xc+QjtK8xTwAcgK4Ac04P+SCvgCaz3Efaz2nctnPBOJ/Lr6wATFk8IBA4DGAEqKE5db8uOD/9qmkMgGC+/r1DeKRJ68/OAKm9qAc3B2kXBoHvOiA+fTxH8WtoQQ0Ecxlf48SL/2TV7H+QakD+HNIE5AlgjvdvSP18+lX1P018NkLzlEeTOIDKbR8CgB7BrOAcpjmqQL3+2ZgDOz89hAAzirqfbXdBugBLnzeDNmiGpEv6GSeffg1qgNEf5++npfPd4FaDcgHOAkVRD8C7jzKaEaYAbQ7QAaQoqKoiKQHtA6e8nPAQ6BQzJgDMffWlT4mP2y+DgkftzXz1deJsyDxnbgGeie2U0x+h4/y9NAHyinnEY92/zbRvq82yZ/jsAASCFb8+ffYK70+6f/YTi69yP/3dzufHf29z9CBw/c8J8GkR933dfVqtnqT7lXPfAXitnrp2M/9+nCHh41eS/PgnDOj+JPdp8qfFv6fbn0S8auPTAn6H3qH50fGVW68PcAX9cWt9xOann8tT8Du0guWrAiTXHLgJEP43Hvw6BJBh1AIIAoOfvNjNdHoFDP4gAhCFz+Ufk30uNsAzZTQnZ1f9AQQeDQFI/GfQvvEVeFT2YG1/bh+jYN6yPUqjC94+lUOef3gD6Bj8863aTEnFnNDdvL8DpQOasT4JHlcgOuBx0lXlvEFJKn+++eedrwJut4vn0xlegA1t/9y1zQgLeO2Rx7N6/VTP+jw3anNr94CfW//3QuXHDyd/BwwCoC7v/pjTL56aefoPpfd0IXCdBwz4MBMBQBSgGXDhbNtctk4H6gCUwHd1edDFlydd/L1Cf6KaPzLLbHI9zE3Wg3lA9X5YBO/R+0LXRPa7C31rdv9+lQvoM2aBfvVpptwPLyAD32CD8mHxba8BzHvt/h4b9XIAG+uf533OHM7HlPkHmAO+vk369m8WbvD21+/p9UC7L3PKPRPnb7WTZhQDKD97+x3U6u2ZnrMD2sofvOBl+T8r448IhBAfIfwjgj3EfNdLoHlPgusXoEvUx3+vy/FxfzVvmYHLXkoVQfCA6fn3o4soBtD2hUn/UgzGPwLQnjvmAiRenM8YOq/yHQUeGgCyAJQ7u/b3mP3uueqxXZx1BZ7un/+68esbqCRnToVXLb32G2A4wNaP3dxnrQDagAXB9RMXwLN/eyfymt/FDuiEgQDYR32XdHzSc9YohSMBEUIB5qJrP8CQEEGIgCAQD/IQMJxAUIiCAhTFMDQMEDiEqVmfJ7p8mZvJZNYJp8gQoigkxGAE8v0gRDDfXxNrwsNJBHIo18FdnHLc36dmSem/DH0aNnvx26ZodsjL3l/fXAIDI3ms22+eH3pFweAm6d5ic9kSgdVlm7w/CbmM8s5U6qeAhORUdOVraTtbdtjWXXK60TdWjO+ag3A3dbtMzlRUEmYo35VNoeUVefZb7sKJuTe4YmEq+L0wCt7z7HET53qmtaWWrkMaOnaheT/AWeWF+HZb6KfRDpN9i1yWuu4IloEJldiuHWq1YsX10RExQ9ybQ3jeOXbLyBNPCpUK7XVIXDtZcUwOlB2fsZOlmc397gOeJ28SxUWnQxiGrKooK6kgZXM/qkeTuGu8ODLegPJRYRkDVmBp1UhX0bfO3Sk85rh4EvijIEybwqSJZEThkxJtdcPFsv2Zvt8P6zTF9uxFygX3gBmMkEPtUhv0VFOTGhX5dIKNYLyTFLEe3XVxjldU6MI+gWMDziSaINLNtVkdd3addhe7RPbnw4nHCncpWmXDuVedy/GM3q9whGHCIypSaLo6b4zT6Shf1d3UbKqrE2OrQIWzVZBuuauKOPH1ZnV0rIjrTT0uLbkrIb1pNn2nkshl0Nj4xuW32K/Zy0Sx7rQMOeM2EuVg1gFeYpoGgkPvJPV2ZDbi6mifrqyVGPmgaHFRCDu60AyhyJKTW2kw3lXI8Yyo6FHxIc01tuVWlo7tlhZIjRzP5HRX2ktuyV6Vne3dzUmOB0FQ8fPVO2Z5lOL2Ztii+AmXuEkQUKlQXQxFLNY1K4FbMxdKl+3ptjpojKEi3nmvI+4Zv+CHES2OFLtdTtxJVZm4vlzUPFYqhDL0k3DpLB9K11f6eiwuy1QQj2nEh8pNufaSTPLiOeHTeA83AuG0enTdMkthvVcLJlxDaE7RV+TOhu3+fEblit3c+l7N4VY9QH2qbfLl3TFcXcssIsWZRjhbrUGyg5GXWbQ3uxgdt7zllPLNyIkysM2lYATHkA1TCd8rNzaMXKrarJnzLcBUMe4uodC04iVeIpSLmdx02OfKHdHuUWJxNn51a7+xbMMVuwPhZktYSWG3rycqNzLiHpD5bc1zvkR3loQPh2WwXlLx3Q85uJtWE811y/JMEk6ILc2oN25HWfCVvqJzaIK7JNRgZj34OsMEtnVxEI0LRpgso20m3jK/O7mlveuJDQwner2jqkvq4sZxd8vuF7vKKrfNSHevjeZQHbaCuLGqcNMc3C1E7xMmlKbtZqX6gYDDXrc+p2tTinZu3HCb3R7li2uXbc1cKmzM8uWbQvH5pl6bLlb77hGmGy6XuZOYTu2OWbfXu3LgthV9qm4Mdhf361Qhlf1NZ8eOvE/kFfK5eJ9ocChCyUieMMsNalBKyJJnCjfwzFVex9SgX7Vur91a825sq/suwkqrjTrWOuz0mIxEcTsGjXPKzmvb9KUS2mDZGAc1dFapmKG3XnoQLUlBlvcWPYamqkn0brtDbHsts5ZaJ2BfCqEUh3Cl2NTlugrVmjRjVkDTVrXYrgi4PS8ybamX2RToS/ICnzjVOrDDJOgQr5Ta/TgivmDqzpa6p+wunKChiVLAk14x8nm85b0W7XgF4308r2RyZUe7O3pnwqgbJVFDKlEH7uHk9a3yOlGA6No7ttnOSRFB8qAM0daWhfdc4+3hssvlXRAgNRJFDSbu7j2a1cJKJ5UTOTQb01j3brxK09a/oS5xym08ZSRlc1Tven5RauIw3U1JxkxntCWlRUuzkrbHMWIPqUxKqn2dDjTk0qsNRWIZFx0EhcFSvGZrDfVpWSi8YFMYIUFs226KrRtV2IHS+FdaSEDQlm3O+zsUygTrWqTWLW8VeSNx2j0YywRQ/13GRU07rWoAtEddKBm7P0q2Fq90fSoz8qYf/F3QJW6jHTR64rDqWjO7xL1CjWowXN3D/Jq7ZHf6EkT6BqTlIE0l24jH0PDIVM427OHWVkGfqtSpaXNovHTqUWtVVL17uCOlW/c25NNpKCVS7kx7GYxofT1DsjppJKvsxabUNd2Jw3V89o89X+kBR6hX8aikaLA2IJlALNXvjzKzPwghmq+E5VL0ViuFX16xYLUikdvhrgiNQ9s2ilXIfr+x7U2/PE9YEJC8Fh+SU9IxzXnPMR2JYueAK5KWpMSdYR5v9L2CUIQ8bjhZP+FXeEp2Y5vsbUPfQazBrAWgXVQJaYRrmS47qmVVx03PJFJx5U8EyujO2PDXSxevznfrzDEBdNvV5/pWQKgGb5oVgFRIXoY07esdh/eFKl5um4ncLs3gOk3OssFYHQ8DyyyWrEfxW5jLpM0pYzsiaQ4W1br3M72p+2OfcbLMMftJo/CpvPBqrYhKZE2we5iYI7Lk5MiIHF2U+EwQCTlj1FZamTSHMijHnJiTt4pp0OYxm9zhEEZAm0DZKVWuruXRN+OzmZmolEf61KvH5m6YqAH2TobXgd6CDVlpv4OdMFxVugq4zTzG/N5WEcBAzaD2icXoTCv7TsrcVyZ3xLcSe7LPcMzhmyiqNVbFVtvKbssotlpKjCok3kJFmbC4zdIKHBqybtnaofCQvT0I0oZXd8gQOxB15gBHQnaf0Ddkv1Wx/JSejyCV7EBrl5HJC8Ig3g8SOhQovd6skLo56UoG5AuofVnLskRwPq/6rHHdFjkOazftUKokt7ltfBG/+yZXNpjADckhcW23iM34kOKkmmH8WuWszmzsmPN60wmZ9TbUAvxeHvjGyViDVQo23LNiY6x3V73WIvbU1lldnqJ96+xNwKsYWnUrR4yPFbxBddAe5isnOcWRgghnpIw7+JC63FY6GdBQpSSx1jrFp/iW24wutGZvI3IzlHifnfdeamNjnAkEfbAdhQJ4DmBMo4ZztBrQM+Rx4Y1mGiQVhqRyde46TGpxYyCnlrk6mzhNEwr7tmcaG5jgNpVMX+49d6GS3Ua6bht4yyUH1yyuk9vt8Opw6DSwQnuO7Mses/1BPxTVdbykzNrMQz3Y8/GRKLYH7qBgMr83ZbZgdDmafMLVjpyGY6c0VEwW2qfb1pbP8agtOQpyqu3E1lMVuDoO3S91EZl7YRMfLDa7sTYEhcSZg7bYuu4tWPDUA1kP1xVJkXnk5nl0908yZ5+zU0Eu017C8jVwwGVabYQcvp7kjZfxxKljN8e2tmyPDdF1ueWvNnW8HA9qhjOaD0UZdIBMLtppQ0zGmalXPhfePRRvrCjPl3zEGYpAS3rVYjqwaAzSEd5fjxmtXuQYSZEYoKoORfDtVOa7UO25JbYf7ZRdG5Nu6M4tRdSsvlTydnduakc/FoFKRKYFVWpjbiKGhsRpzdjsqN1CU8u0I71ifWctXMhTME20ezrzt1K4gDoinL1dCJlMOqy/XAZh7k04zRI4I9MsskeSjubISPcCK1H4lXo7aadpYM3orELnzBwISyJ3JGGhZYeF4QbPUBZuxs0y673AyMc2lbftKlXT297mC+SC6uW+TO/4vUPoY7JZI3SrQCsrPLu2poMmg9CLW+K03sm0vaTnjRhqmgE9GlTP1ahRUkbgrlAMP6JhbiX4SB805TqhqpI1GzpXAU1HBm4ShjtELiHYlUsfokzesG3hp74wGMikxUq/b1v0uiOGztmphIlvNsyV7vALXd9N2ERVlIMTIXakOLeRqx4mV2q3PknMaoMfBCTYnjB0qlq8t5vULDnL72W1w66iBW0KMT3lvR7nwcDBDEfWjMUPHlln7b2VdPlyhyeRrCjYg0b3zmgiX93Z01jHu61chHHYgN6+tK6SyDVpoE+Gs79FXLjHto4Fei2osq7WjbAwgbDuZxyzk61zHHIygy1p3XMmdm/tPtcBXg3nZazrUJhLDGnKcLDW9gdsdzD6mkHwTHdo7HqwL2fvQC3FFsptDst0ejlN+UnQEwkqTHmYIGYbtObOuTMmtDsW9wyWdUyNlWlEQM9EXu+mQ6WTAQVQL8p3WoL1XuMscVhWh6kEjWe2HlYQi3ru2Mt2m6y1YHbryVSCDmnwSwGDzogwR+80JqFu5Rs+LOQpZm/wmUYqwrhEFd8oR8HznDw1ttJk2ckA36eSourNGCclycQu2MOYKpNnqx6Av7Nu4hFPl1cvWVr+oUk3NVVnHIKQZ1Kqk+S6YRUNw6CJG2L0Ujj5pSU8NqGEaGMT1QF3okgJcUayVCEL8ZGFEmmdwbVwxij6dud1jEZPRpTsgq2UFVi441Y+al22B4MUfS9c7hVxw61gu7kGxmBjSCjthqvJa/csxblVJwsqosB+RWr9yuXx/eVClAQd6P1+I9Jnz6Fa3ZTdy4ju2V0GV5p0dMuUzHf3IqWDxjaNsweoTtfHHblrEpZsQ4u/cstLHPiiehPVTSglk74X9DXdtqcTss/stV3dosxobf5WZJPHkFu8tDKX4fhqeb0kg9aY6CQJa0RYOaZWOxgve85qu6SNVN5XBpGiFUA41ui3dnFH+GA9NkFTwJLTkPTBgrFdJNdDz90ctVl7qNAfUuVwbqV9HSj7sieZPRKopBKClpWD0e0VbGZv0LI+IZwiJiOdrdz6zknZ+tDC3QjfIJu0Zf7enbnlkliTaVOR3bYpTVonkdKIaH9qnM64BJOCHSdDyMxlRbcj6q51O46LG0cEa35p2IEZ4KcVUR7uMd7L27AJU0alGvjChj2lhYQkM4eEI+xJPmkujKl9U+6LKimpDhbOS7maUmYc9T5jwgTtYUpcu7LZW0TtOgokgmoSbshSJPE+wvCDEmut5AsIKo4HZFt3Z7C3iXvLDrl8Z+1TNSja1TSGK2ynEMkZdLfdBV1R4yqu96AbPhK2G/K65MAb6XawIm8yUOOwVPideLFtZZdoAgXJ7q6E6WoLEeV1fZd26w2S71ztxkIij/FZwe62nmcNxFl0U2M8V/UlkH3q3Lm4WfugFYkod2+lB2OKdXLdX9GClq9Tdqv79fW0y1daLtyq+7gv3YQcaH03XQRd5ylkAB9+Nwj71S5hR3IDIYS72xaqop3qUaxOy3h5nKBLSDFweLl7Ruld1ocJc6gxuTW8Bh3vucOvsTyEW4rgEGzoMVs976NTeIwwN5QHuiMVF4uF7Ljve5uIGYOibcsIECd3CCW/ubhKnZN2k0kjJCUy35dBCpO5D6fcXhVXEKmU9+y4PufTwNPs0NHSJUtUwzkdjleLr1lUO3C1g2/3XCDq13EoTXanXW5xQWT31cWWi/3BxrDUujYecT06NwXl4pY5j0lTCCZbyatxg9jyvhWuRy1eS43nr47LlR+sdhvfQKlIPx7FTGiuFy8ofMTF5LNJaOzFP20U2U5d7MKfpJNZjMtclSobgaDrfdULONNvBa6nYlj1hp0P+0l1wWhr8iLMAenAy1bPQNNQNZCBH4qrd21Re+lwJHZUXMn36cukwy3a0na2PSaphKPbOm2PZoSSUdI2a5oUiMlPtLFsj4Rx5/xoDdUpZWSXghcJCHJhXcfgyuQICHFwNoOpTY9c9p2kYuRkYEEy2UFqTDfs3l+3zE2dYFoOJN4T6Wm78sHGpeIMg7kNypbWQ5ulLkeBUafa69LR20vkhitMY8VeOxetW3OcRKJ1PNjVs7BE9OFaFWK4HMslTJPlroeGpAYVaoLcsUcU3pvJPUVDlTJ8hAm8ngQ8nCMU04SjUPctiu0bxm135x66gakKgTqOBgdm7C4Z9MYVOicee0HFxUvu2TIBNyXKNNIBvuXs/UQHoeKEYrZ2+rWHgX2uhOdHlF2P7BYtrEjKUjs9XEtNMekgDRMkY66HEak50xyLnF+TS509dTSR76oMxW9qzUM7a7tk1lDP6xMnKvim9qUzXt1Ag1rKmXxj16vB5Ttvai87lcp0z6P5JXfzLCNhloez5zN+Cwtr1+ImeEq7tMR6IRVHqmlBFygF6Fhtsy3loHvQbp9oJ8E3fhpG8b0plFNC8hgJHXiFj8WD4qxIsIPDNNcYTubS0vlqglIfyRE9dEywc8Qb6GKZCFQ5BuZRA9Sez6kp4Zbjj5x7QO/UWgWQcbneUkj0kFO4q3vbgXdnG8DJWF1O0b2n6g7GiXhYOnpbBJnQO5owrLuRcLcBq+tisaWU8DSQ7rm83zcQaPjgSCT09VkVDIevD/Qa1ugTlElWUYl714Z1aHCvpTLd691ZPhrDvqJsJIwvOJQsL9AKrcTrfdl0LdGjytqBHb48juVA7m4ldSj8bIAj7uRcDtKJr0av25T95urEN7mkSGpaZW7JjmfT5c/temPrx3zkOXR0AbwZsrkhx/5+CJzDcKab3Q3sAL0eTgdCOhKpjMhTimwNSE8RpcnJg28FHJdpbHMS/B2G1HP9dlcN6ViSxyO9IMmMPzowZQ32GPmTJhz16y72Ci918DsZXGSp98szSrfXWwzF2HbrtoWi0icLxzeAccL4dtU3MYJJ5jCdXb+V4jPWcYWxDsUTf9oiy1upSBc/7IOIp3TpeHJ3rK5YjbKh9PNhNWHJWGFr27y3R9wz2MC/h8NGWJ3NYcyvUx2unAJnDKlYScMOIa0y2KqrBM+hDcCiwL8MJE43MdbEzaUaXEnpjV2PUrC1TDsekxVkLOUObuAoWfPDtSPqC5leeorB3XHap6sCc+DJ88U9cC26JHIrsDbdMqEq5o7CDkmVrrAqs56H+cm7yoGZR+pWP4aTY18LYtPssUPWRP1ktYUKAQquq4YQfAKBsq3Ce5fVwZ6ESp7Yvj4cQBcV5iCvMvHeolk66OwSPRHISuxjbiD7FXyknHN8IpMCHbnygt+Oa3SnBvq+tkTYHKhg2/k0sFt1S05Xc5PpaTk6VgGXrBACL8gbha535dXNdvGdJS5Lu9JWji2csDJnQHmhBSEnUtyy7d4RHNxlEXjkI3R9MVh8GtRos3n78Pb76d/bv/zK2nwC9P/sIOp5ZvT1LZTHsWbg+J8ea33611X664e31ktmhR6HbV0+RK+jqb85avv4z04r59nT8y2wr6fVz9P13onmd6PfktIfur6dvnRV/ngHBcxwh25+n7KbX7n1wPefzmVfRrw9zr+9AFz21cuCt/l1x/ndksBPnD54XUavs8cPb/7rGPoLSuBfgrae7Xy9xQDMQ9+hd/Ttt/8L4kBBcdYuAAA= -->
