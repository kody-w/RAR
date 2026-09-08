---
name: "rar-cowork-cookbook-teams-update-update-product-assortments"
description: "Summarizes product assortment status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post any"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_update_product_assortments", "rar_sha256": "80718435c8d1944668576e1d5165fe02dec43c538beb976247de16ab34613e6e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_update_product_assortments`. The original RAPP
agent is preserved byte-for-byte in `teams_update_update_product_assortments_agent.py` and in the RCI capsule.

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

Update product assortments Teams Channel Update — Summarizes product assortment status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post any

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-product-assortments
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
    "card_filename": {
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-update-product-assortments-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_update_product_assortments_agent.py` and embedded as the fenced Python below (sha256 80718435c8d19446…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_update_product_assortments_agent.py` first:

```bash
python3 teams_update_update_product_assortments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_update_product_assortments_agent.py   # or on stdin
python3 teams_update_update_product_assortments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update product assortments Teams Channel Update — Summarizes product assortment status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post any

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-product-assortments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_update_product_assortments',
    "version": '3.0.3',
    "display_name": 'Update product assortments Teams Channel Update',
    "description": 'Summarizes product assortment status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post any',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-update-product-assortments',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-update-product-assortments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44a3f22cf4a8d8bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/update-product-assortments'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-update-product-assortments', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-update-product-assortments-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of update product assortments. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-update-product-assortments-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads update product assortments, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes product assortment status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post any', 'example_request': "Draft a Teams post and Adaptive Card on product assortment status in USMF — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-update-product-assortments-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on product assortment status from D365 ERP, with an Adaptive Card saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateUpdateProductAssortments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateUpdateProductAssortments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-update-product-assortments-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateUpdateProductAssortments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebPiWLLfV8H3Rbi7H1VXaId6MRHWgoRACNAK6pqo1r7vC5La8919BNTSMz32jMN/map7Aemc3POXmffo9zera8Oifvv0pnhWvuCtNI1Cr15YubtgintRJ+CtSGzws3CKvK0ju2uLunn78OZ6jVNHZRsV+by9yzKrjiavWZR14XZOu7CapqjbzMvbRdNabdcs/LrIFuyYW1nkNAuUwBfcf1eY48IvAMdFEPVevki9wEoXYFPUjg8xGqsHRNt7sbDqNvItp20+gdWAW+IW93yhelbWLJzQynMvXZRF0z62AW0o1wLi9d6CsWp3sVdO0uIeteHicBaax5qqi5zkI6AIdFgAxdoib/5r4RaAX160X2mNQFlvsLIy9Zq3T7/+9cNbBD6/ffr9zUmBjkD5hwha6Vqt9/x9fpqA+maB2WCplQdgcTkCi+fge+nVQPEMXHI9f/H69nPjpf6HxX/+Z3K36qD55dPnfPF6fX6b/8ldvmhDb9EWVtN67sKxSsuOUmCt9wWV3q2xWdRe29U5UBHYvY7y4P258zulolz8Zb7385PJe+C1P39+K4AI1myKz2+/LIBHPr/V3fz5faZS/vzLe1rcvfrnX77TaTo79oCnATEg9fuX1/cXWbDw+9LIX3xRzlvmxav2nKj0APEf9JtfT9Ff5F4m+fJc/HNRflj8OeVZn78AeZ8haQO6f04W2ADsfHuPiyj/+cWjLkDUWbnj/fzLPyPrhJ6TpFHT/kt0f30SDj3LBdZ6meSXDw/3/XWxfOn2jeY/Z1uCgPl3NAHLv7L7Zqh/Rvvh2b8jnUY5CPyvvvxTcn+2YfmXxa//VLf/3YYPC//zG+ulIENry069T4vfHyHy60/u94s//fVvgPT/kYxSdLXzoPAls/LI95r2y5dff2oel3/6668/dSWIYpCmX7o6/TOaf2bXB58/WPC16uc/7gX8tTzJZzD6lkOL34vyv9V/e1/oVhq5368D7PoxE+fXcjEr8ZXp0wQ/ZGMDZP3Bjr+8/Q0AUA606R64NePPf/zH4hg5ddEUfrtQnKJrF8DBbZR5s/BqGDUL8H9GjdoDdm0iYNjXOhD/s4dniQt/8dv/cB6g/9F5gT7UztD2pXug2te3F8B/+Q7wzW/vCxWQL+ooiHKA3zJ1Pn/OrWAG/2guCV7j1T2AK3tsvY8gqz/OHxZRvvjtX+Tw5UHsvRx/e0B39ERBmRFmBGy61HufdTVCUEKemjmgAniD53SAT1o4QCg/Agj+AdigKVJQFdrZLk0SpenCjQDGgLr2rDjAdp9mYr/99pttNeHn/AnZ6OJZ8BoILPgmzuLjR6Cdn0ZB2H7OPScsFj/9/refFv9z8b/b9SA+8zgDFV+eARI+ahTItO6h8mJ2M4CRh2d+/9vLxoBMDio08GPkR95zM4jUxHO/GlzZUR8RnFjYHjA0MHJWAiOCOrCI2veF4C++yQuYzrfmShHOtc71Si93vdwZAVULqPPNknM5bEA4Nv74YdE13oPrb3ZtPUTMQMpb7W+LI3MGdalIwa9ZzMcisLnII2D+b+HwvA6I1D81C/orifeFNMfmorRqqwxr68VjrvezX+YO4bUdELcWuXf/nM912JtN9UiUp3nAImAZ5+XSj7PPQecCmpPcbb7yfqyx5uqpPqpo/TlvXklg1bMrHFAUANOgi9y5NPzXK6SasOhS92E/IOlM6eUF9+WVRww+W4A/aYOaV6/CvHqV18LPHbKCscX/zx3UbBaK5+UtT6lbdrGVVPn2dNfcVM76PfvQWeJZlUdqfu9svqLXVxD/nKcRiL16/K/nyoeTX2uewNjVwCcyJT/ogwgD7prpPhJgDui6nlPH+px/rRYfgEEe0Aj0AGgBsmkO4q8M57tfJQ0BJMzfv3cOj4CpZ4PNKbgoOzsFAeh7nmtbTgKkquckfrkZZIM3J/Q9jJzwD1rNLgNBB+gvgBARCBfgnPdvCP68+1X0P2x8Nkjzlkfz2IEcrh8EgBzeLODsqtlxQLz22cMDPT89iAA1srKddbdBFgFNnxe92gO+baJ2RsynXb0SgPbH+f2p6XzVG0qQOMBYID3KDlj3kVAz1mSg/QEyAEwB+ZVFOWgHgFFeRngQtLIZHQD6vvrVJ8XH5ZdC3iML5zr2deOsyLxnbg2eyQCi60cQUf8sTAC9bF7x4Pv3kfaN20x7BtIGgCHg+PXus4d4f7YBzz5j8ZXup38Ykn7+9+aoR2HX/hgAnxZh25bNJwh6FuOvtfgdwBj0lLV51uWPz3L59e0FGx9/QJw/kH9q/mnx74n4BxKvFPm0gN9X76v5lvgKsdcLWIT5SN8+YvPdz7nsfcdawL7IQIzN/htBI/CtMH5dAqpjUAPwAoufhbKZ6+sdlPRHZQDO+Jz/GPNzzs2oFcwx2hQ/YMGjQwDx//TdtwIGbuUt4O3O3WXgvc9D2Sx+4719yrs0/fAGgNX7lwe6uVRlc3g38zAIrA9atjbyHt9AnrpfZlmeFH//u3GZe935FmXfzfSPmPth4b0H74t/0eUfkRVCfFzhHxHs4yzFe9yA2gjEbcdy1u05E85d5APRhvYfpTs9Pljp+4L1AHqmzY9p8iqCcxPwQzY/3QHc4AArfFjMwjVz0QYmmA00I4HVgNQC+v6pLI+i9eVZtP5RIHaudH+oawCcqw6gw8s2mnLk/pTutzb6H4kaoGeZ6bjFp7l8f3hBIXgHo8+HxbcpBmjzmitnDl7egZH913mCmkPgsWX+APaAt2+bvv2BxPbe/voPcgHBHvgKqtRM67uQ35cWj8lrVgGQbp9/KPj9DYSbBWxrvQLu1bqD5QCOPjZzkwKBzATMwfdnDoF7/7dN/YtME1qgmwR01isSXmMo7qxdeINhBLHGScKDXRwmcN9bIa7nYKiDo2vbszckgWCk68GEZaMYAaMe4QF6z4T8Mjdk0SzaLBewyEeQ0z/cBpfcl05PHWaDfZshZt1fqv3+ZhMYWLnDGoF6vhhoA9ukQdqjdF3WRHdrGqquTKOQjokRuoKWbeK9kCGq5E0NF7RXbWsnyr6A5auI3zQHZs+XyCuMTRKT+UQNnFaqjSlyfTuA+NXUU86m07ncTGY34NduaUt7hdtmmRHy+oXZ57mim43OTQlWI0oGj07Na061im+BDy1xEtrKdm6O2wm6LDV3vZK98SAeB3UvSt1+xa87ic3FAT+7fiT5kIvuRj0aVXUbDavWqbiSs0YtDJKIQC6NFY4nDY7oGxqZtFmYzgj6slLOTnA1MXikwGJgAOn9A1Ou01tPhalRMMVpz5mHM75e+xrpWCex9WMRMTtngIYL0dEVKxRE5BiRKBTJVC73xyNHOLqAGW3rkWv9esURaNnV3BL2cqw1yM3S95eeuDGKJIguvZUro+iagtyTinyrUDpOpvSS+CtWWh9YhlT7Y0xZEaREqyFDEDfDuP1uDFCaOkbtxF2KKV06RzQrb7g2GDqKYcmKvqdZdjehxjaUJh2LXg5ZvnXKEUlOGs15t6ui6k6vGms7M5Zmtbys+Esr3Nm9Kuh7OtkfllPo2ZngMoyhFJrI6yO9hynBsOFhG3WyeLxKRuDXQ44LupsZFtXcC34ba0LtEySSo2aKxp3PS4ex0VaaqosXJ1KFk+7Y6v0mRHAS0uWB8EShPF6m/obt5TI4bySjZTKOFC/IYY8Dw3KhZxHaORfG9JRiax1R2Q0eQfLF1wZd29KComfJ/qYS55LDC++oi0yR+IlSMKXeuodpOJ1Y9zjxeOCYKSdwE8HEJ2+jq92gcWF9Y1g6OwtnvOy5gbojE35krsOxkA53l+UzjrUPCV1f7hI22qarK41MaPFOJ9PbHo6l3kHUY9BoJgNt6etai7tSy5kLqlwtbrfOdaqHtthWpC8kxvhoId3lM7cJqZEfzHXS6ezqPGaVz5cG7XJZss4TjMrp3PJ2o2JHxnaVD2qSn04KhqnkzTuzHW1eiVaV6soHoRA1Gsl6R9qA1gOExxCb1RsrIemNgCHqel33g0ZOTW51elBs9scgaXJjCLRKQWo9bGQZT04ROkZyM6ZEq4cBw939UMjPfcklBA3DkZZKTM1PEc4FRsbpaZK3l3Vem+yQ4Rodd/uDxyYerV0NttzCx9LQDsbOkUZ7wpF+WvpRZ8ftSrHWZy5m9Xos1+zBLDMpMzHB9cbztEs5AzNQSCFOXuOezisndw7H86ZhKxNGVaVFlUYScm27jqfo2nhEPEr4zu7gPt/WHC9rmi24Reo7IT4Y082Y6n6zp1t0fe/wMd6RTQXFjaDAtufi25xbk8Jm68O7TKFLXI0Lab0/edkt3OfL+lAu15ceJrn1eDAFYirjPVRm1CFgas29bDbX425JXviAO2N+gI+luJzOoo6xQzWq9qrBK2eslv4YpKYj44V87XcFF2lrE8MC804dN9o59QfJgO96mwpVSflYQJvhHievuLhXh9sIY7vhsl6fIFvDKvxgixN5m1jnLOnjfUmxfjBuMsuy94e2LxmJJOLdysyzbG9rjJisklZDPDIQtvqQnbDbleJW6X4XdlYEc5wwquxxI4r32vbGApNwjER5tiqDoPP7Bj5Ibgcdl2Jyii3K2rWTv1t6TsNry51yFsXDgZaRPeqbB3WaxvMYXiUPoSmSkAdoc/Az9kboRM4dMBLaaPxRvArxwXSYU4uprI1q12tBnxiaS0aRtGN5fT1rcrjeSG5u3hnSHJ1o7/mRd48A6ll4ZnbMusz3gaAVR+RyP96SWdsTAqojRgfyjTxccsd0VHUaVwxf6zR737pbnLMOB59R8l5E6jEJ6IQOxmCXgBitxcuNZg4SKdbnm5QOPJNNVHVA7h15ZQxjuGRYrUPCZqCCnK+i9RU+40zVXRnYhOOWQZuS6x0AjKGTREp4U+8Jr/Ykhnv+tcNCg8u1exhn9fbuobnmXYv9tM4cWzSLDR1GNYWfrrsY8jbTIBJkFq5Wwr0xYemUr5t8XHtSsNTVpeBPrFDTiKm4uG5NWSavxTaitlITGULAYJ6CxFeOW8NOl7JNIThXnthh97g6ZOM0ZVhWlCh1crFmzOSdvF1H/tHqZMWrkPTG2fGOkYaYae/ZEWaUjHf2nJTlJS+M9zoUhvgWT3zNHs76Ki4OxK0MTvv1rh7TfBrlXZ7bnDLaYibm55Ux8Fk/tIrNSWOTFlU13ZepY1ibjZ8RDhfSR3lUGAJapdx2SfYtDdNG06XTNtxvGN6nkQkbDkp7jzR0xS9Zyj5UyvKktyhGMXiAV5lypMPrkVWa8RRHfWFHyimR2O06gGRflbNCElAuO2N52NwG6zh1yujc/KWlDAeqC/aUVUpoes04mrlzRGj0rnm7YnfWIBjqEoXrytVuW08ZcfmW32iLsjUASLB7SbR+3BhOwzAH+H40rHRUdeogrmm2FzFJZQaPOUaGY9NIe2DFURVsKzsFh6KLYlGLzAAb2YvM3floZx3OB33faldkUiPhdIPoQOSp0jEvMSlidRO6hyBcl1yo5IgsNnmQ6nRHQbupl7diGtiqRO6VJW/ya5jVEIN2JGUg2jC5saCkQFdqsy2nSdcLK4mtjOaJ7eqADJeecLei1+7V3f3Eleet0YagQwXV45RsC7/U08NeuSXpbms3h1WUKqFR1PhO0sBY6tGVre1FYdrSZXZk+QrjVy1kCeFZgOlyJUCbFMEiuo7OyP4y7EqXc3vknLixrhNR0dfD4d6hmNkITF72YeZmiAhjQja5TLKT9I29akOmQlnfnKoCp60rPmy6OlnFZ7Z3k+nSI8b6ulWKzVDVBb9Clk5HF7C1J/i2RnhlPPEllXBVuGX8c1ZqgzK0BrOhIIq7FTDGqFd+s41NvF+7DugRjHRI7gXW5lLls7KcClkXEnrT1ysCP8j3mxYnKwSHTZoJ1mxdaQdRONNbcpVtvSYtV2oM+5l5pLesMXo5a+Rr+H6rCori91C2QsqhbWHZpSNKZCLjXgOY0/cFNAr+ZRcPWYl0zDjljoTYEIQyFs1oOwPv9P3duqkseUGITeyaFZ02ULgdCRwWVERRCcrhxlTf9nBnTAS09I5NwlTXrc4qwZ63WtOIKHkonUAQnJVhHMKemyxpDO7mqFxupdDgjbY/yWVL2OrmimzSoeeWVFyoo07i2E0Q7DNKrpZnP5bh5XE3rd0VWRxNNBS5Yros083EKlh8xe9WzPX9idrlIDyqhDHqsIzKTKB8ah2mez5svS3MY4Uu4ht5n0CprrZ9WNpB0JLZGc4k0ebUkjkRjtxNWV+n2HJT5dwpXIdHOQNTexxsbXg6H1qr3dS8qRnJ6livaaPmjCaHJf8Irwrd13ukRGmLWOFKzQjVjkx7eSOM633AsJWWmPypI29UT2W1HjNbYdx3Tl5W2Q2PdZ5rskvM3Ld70H9E03Z7d226cU75cSmV/uoqunUKUCy0TmZ0IiCdjyYIwJG4WSkR4hB5IW56Bxg0MapGL5tc3wyybRYKcsGPq8lQsy19Mcu0FvLt1E3TrfEPZXxjdtG+YSOnPEq7nZ+dhhzZaANfh8iqpczVUhrqKtSYvZwOqBLnAeXIGk3dKvhK3GMo6keTZ0aehkoJkqGYuMIjOnSKgBqNXBEiHQ57HhPQ+IIjjaNQV3prLXWr5hH+cF1j+sHW97fUjHaQiWXdnbgqQ42FQyKlfVDVxjHtKdVqKLNA2Y1E2hNrbfmTtIX1jEUxpjLY2wC6KjOqMimhG6a/LU2qYTZmrYgcsTkyCAHaW24Y18kJWcZHZneBUWGYkPt1GqTldkdNShqJu5xK+KOJr6aQQAX72NbaxoRivKbD7fm2jaxaAyNkKV+1RCkveHpnzf1h2iitMJVw0gJZcontd6BKLQt/Re5HBpa5eOdmO30fgMCQjSmDUPZ2l1qtx8U+irCAuTIYaVH7Mq2O5t4AjaYI1bqFHBJ7rK2qRG1obaDOmGnjamVVasrJjVZttkRZUkIuWVt15VmVch22u5qOIjA/WdpZWClEGeHb+767OZF3XC6x8XS7WfhBTe1DHgZ5AHqX1cXKzFJc0fYeupea497hwD26newHLVYQtXm2Old16JwJN6O78hunvSbpjQ5Dd0inVeaz4KZfO1sHNpXpKleMzPppy4wSnCn7SFhKCp9JW4m1QQlfgbkr3Y5qmHdgboN7Bwv7O3NH9p5YY7ttWe6cbAebS7ogyEmlm4ajVyfKrqpQdXZiFou54plQQloiN3Us342HW9qXXontDpXd7VJNryYk5Owu8w89ivmSeeXd/VUBwLnUJ+i+azbXbmd1vS131zbuj9WyOmfExiyvZ1RYiyLutJaHqBFlrZCmN/ozBld83NTTUKX8xsQOV7ZyVeBONAshesuxqXzNNN6DhL7EQxq+lnjP5CmM6JPaNn6ocvDWRUUVaLCWoakT9FEHkGZAmrbeDsd9ogQOX2yQgd5WcmLFh9tpErmGX8dCLU6eY6z4lUFO9XEssSjMB8XgkcC2l3B2dcjdeB98ll3xG7xFD2iZr0+erajLJQxBA7cc9JQ7LOO9D40+2HAwY+eEnK8hLJCSfi3aEufxq5V0mHlizeZCubvieFpmDHHv73vTOAetXh2uwj0uEq6kVmdngChaoUgwKsI9sT8uV2v+ftRW/eRMZV7UEitPU9u6BELFirWUp4OkNiO6924YObExl6E1G3vX5XGLcrVRWC3NGqRwl/YCwiJnNG9d0/OytVJa+W0XLrnSRQ3ePgXYns/WY0nFOdaLhumvbOWsunt+jdiXVgxrBBKzwhUv/Ukv/YG4Epavx23Hx0vOHU4CnVyEOrk7577nOdvNzLWq3QGGlRYx0IZ8WHlJqJNmpdfV8mr2KSudDg6jEKD+YJiJuOPZ8AzUON5ialoPDeF77OGq4a6gYuGNvEVaqZXb8AgmvmwHLIqEYaYkF4KO2c1ZcUUE25N6RiDh1BxzY6s2OEYhzYGlChlp1N4Ke9CAB0hi7raFhzb0mjjtRHQ1BWFu6OIZgrGl16tY40EkHhw5CDNOl805UVvUow/StsakG+ysCZynlxHmmgis3CCyZDtdlelsj0CHKypUTLwlydZi60ZyYRdUQoy1Rge0qGJm7jybu6FjV2ajTBbj/XDTh+P8xyW/QeGJVPXUabsbDOq9dCuwYNkb1K6DKG/JiwYPc354FyXP6s7yye3d69KlYyNLGxcNaLyejPbIdy68kSrxOoHuvpfFI+lkwyFxpAt5Y6T7hkvvG6ZOBzgDA9/lfkWIXK1aUg6My5ksfBwqPI6S+QtObqb40FexNxx2hEU1QrMWWpICPbzdga4V7VWj98pyMFbLCjVv5MmBnER2GjDanjeVgZ7OdukVZY77J0g51p5S2VIo9qysa/rEn63jzWhVcnN1eXQHibpJXvTwcsfa7gSfrmMGqdj9cMVbIdXH7XVUrzuOC9g8svBew+0OEi1Lv5Jb68RYpDHJGry7yuguqs4W5IlG7DHs6Vi7Zh+v9qf1Jdq2Clty8P6QnxowEXY8domP5brKfDccD4d8WHcNJSCccwyXxk2TzXLXgxHkJPYrljYO64t3uSSde74Xd/0YyWzDSeE0HnTOTot+uzmd9tSyPjZwQ6zPY4Pu5LM5qWAog5H7tB20NnAHMbKneHmrNmVdoyFpMS7tZHh38AYhTJ3xgiooVph4ImOTq67cLBVh7XLK55E6LiGXR1Z2Bgb0lB7b1kLd/bLIkBTjNd9otx1wOz/mHtrq7WGVmCPc1LZb3Sr0utylXSpRk9EVbhp3k3ibJDCwVfa0Y2+tSt07yU2RYlBFKKoEM6/PRinect6+eviJT7c32JDH7Zk0AEyqS/62u/DL3GCmElRxAFCrs+JwZOUwALewaqMuL8imvqwSDqO7teNkZV6dr8IN9pC+1QiBJ6+rAZbxUl6eMcdCYGld4dYOldp8stkhh/dZnabThVd4gwLQiWinpaDIFwuefAgCLSfpV4f03EPuFl4P3cUzxpXf+whqbir3Fk79Lk1bQoSOJcOr47IqzXp319yre3DgaaAaAwIhSWma7F3Iyx2MG2Bk0yR/UyG16qdirzmoA5NbPHAy1C52orXBA28fBu1S2YMmgpUvmTZZBBwbR3pTOumE0vWF3BWUk7A7UYQu4TbotVNk0UtoVzrUji2GjjXPbUag5mhquE6PndP4e1vBsgaTgKdQC5sKes3sfM24bIx4KSqB16wPZ4KIzgm+Jky0q+u6qRqSoG2a3EgOZpHQOSWXsAlR+jJ2eJQdexKe7jdpWCtHZpXc/RaJiGVUAaeUtYHF5t4HvN0NdFAEj8QhZtq3VqmTkoGJPY1mI+rU7WBb2LIsw2t0XpphfeXAoCxA3g31Jva467d6rroK4dta7E4ZGTp4KKvZSeDOS/q+ZxK2HSsXyTKqEqjyrMu7RF4nUi5j6+4Q1QPZ8CKvBqfTuPVZi5UCrmRvNbIrCY3FWMHL7W6/cwRuicoEQh6l6OzUOXTt9WDHxOhWgryjsUEjtax2ybqQlcCt+yOx2QhEOgnutpNSmUk1ebUeqTKcqgmy66zwUxTf7PxTJZ9QyijhDRraeJFMlTcRqLKUfJQO1vgyhAgx3WvRtELPcd9AF++sFxJOaPMRx1/+8vbh7fvZ4tu/+wTVfNDy/+xM53k08/VRiMfJmGe5nx68Pv3bkv31w1vtRECu5ylWk3bB6yDo786wPv6Lp6EzkfH5iNLX087nSW9rBfPTvG9R7nZNW49fmiJ9PBYBdthdMz/618yyOuD9x4O+H1V6HvJFQf6lLb7UXhvV86Uon5948NzouWL+GryO98D617M7X1AC/+LV5azx61AdKIq+r97Rt7/9LxjOzEKXLQAA -->
