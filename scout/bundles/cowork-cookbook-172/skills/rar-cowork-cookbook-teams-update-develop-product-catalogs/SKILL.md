---
name: "rar-cowork-cookbook-teams-update-develop-product-catalogs"
description: "Summarizes product catalog development status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; doe"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_catalogs", "rar_sha256": "0b10a65613042e335d4bb0a35624b51361d73eaf69d2c0bdeeddc778b9f501c1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_product_catalogs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_product_catalogs_agent.py` and in the RCI capsule.

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

Develop product catalogs Teams Channel Update — Summarizes product catalog development status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; doe

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-catalogs
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-catalogs-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_catalogs_agent.py` and embedded as the fenced Python below (sha256 0b10a65613042e33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_catalogs_agent.py` first:

```bash
python3 teams_update_develop_product_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_product_catalogs_agent.py   # or on stdin
python3 teams_update_develop_product_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product catalogs Teams Channel Update — Summarizes product catalog development status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; doe

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_product_catalogs',
    "version": '3.0.3',
    "display_name": 'Develop product catalogs Teams Channel Update',
    "description": 'Summarizes product catalog development status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; doe',
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
        "upstream_slug": 'teams-update-develop-product-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-product-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1feb311f9f4814b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-catalogs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-develop-product-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-catalogs-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop product catalogs. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-product-catalogs-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop product catalogs, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes product catalog development status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; doe', 'example_request': "Draft a Teams update on develop product catalogs for USMF with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-catalogs-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on develop product catalogs status from D365 F&SCM, saved as artifacts for review rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopProductCatalogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProductCatalogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-catalogs-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDevelopProductCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObSLbmX9G890NVXeyXTWy+0REjCSQ2IQRCIJUrXOz7DgJUU/99Ekm2q7qr73RPzKeRw5aAzJNnfZ6TTn57s/suKpu3T2+6bxeLnZ1lceQ3C7vwFptyKJsUfJWpA/4u3LLomtjpu7Jp3z68eX7rNnHVxWUxT+/z3G7iu98uqqb0erdbuHZnZ2W48Pybn5VV7hfdou3srm8XQVPmC3Yq7Dx22wVOEgtOUxdBCRZeZH5oZwswOO6mhx6N3/VN0YJHYIXUK4dicfLtvF24kV0UfraoyrZbVFk/D2ntm+8tVp4NFLv5i43deAtRPyiLIe6ihaQK7YevSsSFFwMdgTUfHuvUfeymH213tmgBzOzKov2vhVf6wFh/tPMq89u3Tz//8uEtBr/fPv325mZ2C269PdQxKs/ufPZprPr0webpgtldmV2EYGg1AX8X4LryG2BvDm55frB4Xf3Y+lnwYfGf/5kOdhO2P336XCxen89v8x+tLxZd5C+60m47YKhrV7YTZ8BV74tVNthT+wd3tSBcRfj+nPldUlkt/jY/+/G5yHvodz9+fiuBCvZs+ue3nxYgEJ/fmn7+/T5LqX786T0rB7/58afvctreSXwQZyAMaP3+5XX9EgsGfh8aB4svusptXms1vhtXPhD+B/vmz1P1l7iXS748B/9YVh8Wfy15tudvQN9nQjpA7l+LBT4AM9/ekzIufnyt0ZQ3v7AL1//xp38m1o18N83itvuX5P78FBz5tge89XLJTx8e4ftlAb1s+ybzny9bgYT5dywBw78u981R/0z2I7J/JzqLC1C7X2P5l+L+agL0t8XP/9S2/27Ch0Xw+Y31M1Clje1k/qfFb48U+fkH7/vNH375HYj+P4rRy75xHxK+5HYRB37bffny8w/t4/YPv/z8Q1+BLAZF+qVvsr+S+Vd+fazzJw++Rv3457lgfaNIixmWvtXQ4rey+h/N7++Ls53F3vf77afFHytx/kCL2Yiviz5d8IdqbIGuf/DjT2+/A/gpgDX9A6dm9PmP/1jsY7cp2zLoFrpb9t0CBLiLc39W/hTFAOraB2o0AJyaNgaOfY0D+T9HeNa4DBa//k/3Afkf3Rfkw90MbF/6B7J9eeH4lxe+f3nhe/vr++IEhJdNHMYFgG5tpaqfCzuc8T6e6cBv/WZGZWfq/I+gpj/OPwD8Ln79l+R/eYh6r6ZfHzAdPxFQ2wgz+rV95r/PdpqRX7yscgGT+aPv9mCVrHSBSkEMsPsDsL8tM8AK3eyTNo2zbOHFAF8AB7yopi8+zcJ+/fVXx26jz8UTrvHFk+paGAz4ps7i40dgW5DFYdR9Lnw3Khc//Pb7D4v/tfjvZj2Ez2uogDteUQEaPjgKVFk/0+TMTQDebe8Rld9+f3kYiCkAN4MYxkHsPyeDLE1976u7dX71ESPIheMDNwMX51XZdIADFnH3vhCCxTd9waLzo5klopk9Pb/yC88v3AlItYE53zxZlIC1QSq2wfRh0bf+Y9VfncZ+qJiDcre7Xxf7jQo4qczAP7Oaj0FgclkAhs2+JcPzPhDS/NAu1l9FvC+UOS8Xld3YVdTYrzUC+xmXuSl4TQfC7UXhD5+LmYH92VWPInm6BwwCnnFfIf04xxz0LKAtKbz269qPMfbMnKcHgzafi/ZVAHYzh8IFhAAWDfvYm2nhv14p1UZln3kP/wFNZ0mvKHivqDxy8EX+f98Bta9+ZfPqV56dwuJzjyHocvH/c+c0O2W122ncbnXi2AWnnLTLM1hzMzmb9ew/Z4VnGx6F+b2n+YpbX+H7c5HFIPOa6b+eIx8hfo15QmLfABu0lfaQD/ILBGuW+0j/2a9NMxeO/bn4yhPAgMUDFIHmACtALc0p/HXB+elXTSMACPP1957hkS7AS8AFIMUXVe9kIP0C3/cc202BVs1cwq8wg1rw53IeotiN/mTVHDGQckD+AigRg6IEgXr/ht3Pp19V/9PEZ2s0T3m0jT2o4OYhAOjhzwrOwZnDB9Trnr07sPPTQwgwI6+62XYH1BCw9HnTb3wQzTbuZrx8+tWvAGB/nL+fls53/bECZQOcBYqj6oF3H+U0I00OGh+gA8hdUF15XIBGADjl5YSHQDufsQFg7ys9nxIft18G+Y8anBns68TZkHnO3BQ8a8Aupj9CyOmv0gTIy+cRj3X/PtO+rTbLnmG0BVAIVvz69Nk9vD8bgGeHsfgq99M/bI5+/Pf2Tw9KN/6cAJ8WUddV7ScYftLwVxZ+ByAGP3Vtn4z88cmYH1/48PGFGx+/4s2fhD/t/rT49xT8k4hXgXxaoO/IOzI/kl8J9voAf2w+ri8fl/PTz4Xmf8dZsHyZgwybozeBFuAbKX4dApgxbABygcFPkmxnbh0AnT9YAYTic/HHjJ8rbsavcM7QtvwDEjy6A5D9z8h9Iy/wqOjA2t7cVYb++7wZm9Vv/bdPRZ9lH94Amvr/4jZuJql8Tu123gACx4NGrYv9xxWoUe/LrMlT3m9/t0U+PEpl8XXAt0T7R8j9sPDfw/fFvxTrjxiCkR8R4iO2/Dgr8J60gBCBpt1UzUY9N4Fz2/gAsrH7C8UeP+zsfcH6ADSz9o/V8WK+mfn/UMTPOAD/u8ABHxazhu3M1MC42TczANgtqChg41/q8qCqL0+q+keF2JnX/sRmAJPrHoDCyzOGvt/+pdxvffM/CjVBozLL8cpPM2d/eCEg+AZ7nQ+Lb9sWYM1rIzmv4Bc92KP/PG+Z5ug/psw/wBzw9W3St/8Pcfy3X/5BL6DYA1YBOc2yviv5fWj52GrNJgDR3fN/Bn57A5lmA9/ar1x79epgOEChj+3cmcCgJMHi4PpZPODZ/10X/xLSRjZoIIEUxEERmyRIFEeWmI/jhLd0HMTGCRJbOgSKk6hH4b4dkIyHuYjjAdbzXIqiHSYgENRFgbxnHX6Ze7B4VoxgqABhGCxYohjieX6ALT2PJmnSJSgMsRnHJhyCsZ3vU1PQabysfVo3u/LbhmL2ysvo394ccglG8stWWD0/G5hBHdiknEm2YAuhx+uFa+qrWQaHwezoSmkvuScrAobp7MFptsPavHJJrV2NScN1pdLYo8LELBEV0Am6V2mknSWDMvUR9pJVqJ8nop2uNJxSV9r2iQE9oLYpIciYiiUutetNJO90tynU0WqzTk6X2D7NDFmmFCFLS9qFYBg5uJnXd4pa3aSeOXAVl3XZWRQCcbPNjf4cO17cKZ7QuOR9byU4jlRWM1ISalfcWebsGE1Cd0diq/yq7aWyTDQxybzLUhelZpR5rU8ukyLR3DZzkWrtWnUlqEKXnvtIFg0yjd1jcKcIQiAJpNW2sH9r6wLV9uTmpC9ZDvW5UwNvk5reCfWASEV8jk3tyuWQttcqsxx81UFRiPEDFW/hS3eifVmB8CCAIJnRynQ4HRs720zyyawFy6vWrbcNT+Z1qk2FjHJ6u668qxXFg3pJUCQFDTAm8E2ht3XMXVZyfl5H3ZKBBi8lXNK4OCLZClaDxOWYh4J5JLF9xzWZ5oVWNtTpqFquVvkX3tbQ9qZhy0ZN3AFn1ojUZ7p44oQtdrlUonDqWHhDW/sLud30WVkbe5lenSROb/FYUzIuspZ5nQwI2qjksWon1V6F93LVQD1X0IPPQVQL0XWR3U6tLB+2HHqkzTKeYk2Pap9dG2abGpVgH5XrlruyPJOExS5fwRhqIpJttR17KQusTARBclEM5KKc1o5cuYmf4dS49esQusZlK0g6IsuCfiywYGrux0lrzK3Gwa3ibXIbPShrkr/xbS42wbEX7skULXnmfMC315BQwn7XcO4Rvmu+XG8jpYiv1F67rwhzU9oIWtrEOVRsc33b6JbT1+dJ1ltj2bvNVmzPDaqkjMxNjWCV4R2Ow7oulDHNyIwIJRgp2wwub1p+lURo3dDkEeFOo04d6ag1VXZI2W0ZdDcT2o5tHMsyQSnXaa2wCk2rCITv91WjbgrZsN1svPTlZvCO23iXns/XGqGuVLHs1IuNisMtWVksjPBweKAhZ3+XVFdtk/iq3hgICs8+25FVd5F4/SQIsoj2l/Mm7UT0QqVHf1chZ8gebK5NUCxekZfTCjqGNVFAeMgVsaIZ6TYkr0SKKVq8rU+qf60GhqkO2Kk+57shjTWR026jFOeDJ5yEq3c9VoJ3VFfxZuoO7JEdzuig2pHo8zs0lpTR99Nzil2ta47JHN76tGZGls820DRVmYk1nL2xx92q9rVhl6Y1e5y8re7KQnG8IMndDQwaKVJzQtFjE4giZAt5WU8r/CjBxGrUHS+zFQjGUmii8gwWvAt1JZBDa+1l3Ut3/hgN12jcj5Z4IZDU9NN7xcLStVAyR69IJyZPN65hPNGQjutR2isqsxej0/Jsn/zdrWYiKCfX0z6lQnlgr44cDTduK9gRahc20tK2m/d0oCM5sd/EyLJDEm13l9ccVK+0iUzcks3Od30d+WhiHqVc58T0BJd94J7zoGsla++ZEYzgyjqIKQ81b+p2TQT3ME1Y+FKqNHtbgl3Xvme7vaayhgjdeZqreGfV2QV3sQ9e04bD2cw5Kgp7bqtzrWcSjWy0oNpdXiC3VnRAmEwcgjtaHDre09frPRzkqKgwPdxC3Jo/Z6uOGhE/qTu33e0hVVdkjlFXJiliLipkxbRRp7ul9KhbUuR5YGgpyDaA+bCIk0qKuhu7vcQLTaU3CEMNxa6oMwg/bnRuLYmxcagZTsAAxkHq7UD0R+m63x5OKcXREL3dRrsk2ByUJPD1VVkrwhFd7anLIFzwy7AlYb9nHPLgHlNCXJnoZTkw96hIU4uMNvR0zQ5r5mZsDlloXn11K67iYQVnaiFkF6Pm1Q2rYxJOrbe2p8m7SZrWsQSNUIrKmNTrvRerwRGfSm112LIjCAWmom6bS/eIx9CYqu8GYUfJ2hn7bNL6qGB6zxIn2C9kLEx3e+PSKDtWGRk+Mw+BKiZ5fXJWQ8lEYcKmlFLfVIZNmghHqA3rZVp0QfuK8A88i/qwhePjbYBgU6V87Go6hHIe89yDZCXecMoxNGERclVFH8EWEZMqSxoxc2/KMcyujiO6PjlXet2Ltaws2dSX9116aY8HobivkzRtKTO/WNaxiMXyNGUlRo6rjS4MknYkKkGLW3qH6JLb76bBHqakYwTS9izE8Mmz0Yqt53nLrUQYrUTG09isTtbFoQTX6IXJayqZt5d35erwEWxdqX5naCupDFw6bL2R0ikS44SzbTmC7Qb7i1Zmzb3iiL4d4jqLTU7mlbBDAwG6jYS92m/oi2Osat2V5HU9QlTmqSf35B5b8aTf4Z3CbC8DVx+x9pb18OoYXXzH1+t6fydRdNqt9sN54CjnJkGINJ1WkrzpfSlT2LDYbIs976HsYPDp/WihF9ElwJ4m3Ppid+z3zRmXrkd4O3bX1bY8Z0ftWuPi3liVt0HY0LcQTeX1UjTFq9jzO+SyL6p9VOeX5Tp1IWnfSVW+PYe27hyO7ZEc14STy9UGAgkwRnduKTMgd/l4x/lCcGYuMvDlRgWzjPouOiHDEUBzi4YaQ2OJvaRMUI7e1vH+5l0QZYucE27fWDEmr8Vtvy734AlBNDXCOYF1DNntxqFUY3sQCNWqdqfBqS9kfNxnFOvuVFSMUb8KE05ejmvf1Y1mI2McdEULoTH08LiWsthgN4pjjco+F8KOjsIryodwdqM0TmR2pUyG1tK91cv0YvA4V9X38cxmKQ4fLjGPnqNTU9fLFsFS7HaN7+GwWuJe10P+5uqiZbQCT1MKGxxUzDpPjDTvKEqDVzjbKSiKCO/l6/LIFP7+xOw57XylWP3kCZbb28oxT86jwl4Vbt3SxmYr31dwgxjXtL7mheyHO5KlOZs5MqXeGcHlquJrethuTZS1LyuzxpJ8n1RuttmliY3edmjG4DHRWTdKxdysEYy9NCa25eJtGC7dNXIW5HvLhvEZEIB60BGypNuIY83JLxIzoZXxUpaHYSvCOY1XY9N6urf2V9ImNodGjCWDKOGpDY58MuYN1m6mpHAVjIdhfGNHsXV25EKeToCAsEtAHhA8PpVoeTjfIUGTm+QUBaKgrtZ3S4TP+nEiL/DNdA3NEc5bS05FaZUq1Xmri2sjbictje6VZtQYeZbLTgh5JuVC/Khxm1t6lY+VCFO14WDNAFV3odJhpjUZt7shyEXhb0QLQbxMkkJbyW66jIogMVbh7X4x8YRHR7vddi3NcaAy4jTdbRq1C7p02LirIUrLNFz34EcR8woUGAdRJTSDcJaSudzwXpUw10TAxjNRJk3B8S7aLBkfxvUKGq3+6In3tbM/3+wurbKtOfp0dhd6Xov5Y7/KTzF/0KRYyU3IkEq7p1o4BN3Sqdom/JlVpnxJpleLG0etkbQ04SxltTaFk5ET2YZbrzDodEN1yR/qTY6dBC00R27ZLdFLvHFFbzlJEnr0zY1KKWN1zxxbiM79aVt1yxIkPGQxuS6XyWaDY1R4YoJrf7oKhXE0Yf5+VRqn3mCnS9auyStobTaX4za0jbu573nX481Mh7wjMaz33F3cckfdscMdI4FuuLHHWKlzSu9ZKdMYxTUuxlFq/T11opl1XEsrC+e0msb3wdICe4TRzOQRZbxyV5BQNsCiZzNCVMFuvRYSN1XK5b3vGpDtPpttr8rR0s/x+sgksW1U5R2pV4Qx0iE9Yut7jKYBJ6mpwCi79lh1q6bZK+PKyc+FQpY6eV817S6TxtZqIHE/Xh1OX0Ury/Gvq3rHeDJ22NqMuoHuOhJuBuKgs466vW3MHrEEPESHgBo9ZsdPE5Rt5HURttxepNAkKVLb6m/u3UQb/wwfpSw8TruYj+1G5wwsHS0jrMUDCWpGPBV2yzkxzl5zksTANiFUQkWKMx7ZbyblyJ8sI7a6TRdEndbWNeRjkevsNKbOoU3TlnuaTdJ+jyI741qbuZ0FBTJhPJOHsoKs7dELPAwSbjc8E44Z07bnkN9qe0NiOLJKWknPoqJprkOTJBZrW7QBmnqElGp+nyOcfWoCJDSpmCNCz0k7mW2nG+ZJ6ysnOZSu7yPf5q8ybKdrfe9dd1oSpPqetaSeRLVDYxgdbdPCyS+YTcTz3k3UOTPkASBuLT4yKf7ck1FV2QraZP0yHWSqWx7sxHY3R11kNXpztKFUXZY8sbWMQtyMxyW9dw5XijlEbhKqPEBCk+itaY1sAkG8yhVSy+r9VuQ6sZGTdLPK16ebOckmYwP+PE8aMmBnzS1OWZ4EQQE2mY1KIyx77uJTn1xRgmRiHE9uHpvRan5rACY7oyXdjTXlT944uNK0u+XEGVPOkWWgDFJQ3gGEmA9jv0Ppvk8UR8MmL76gOG5lbsusRl9Zkh2ZBMa0BeLoimR8hxeWIS9F+8uF6di4DwL8FtZGNZpUf68gUi4RtQ/6a1wDWj/dcIRbijAL78i6xxJ47dX+cn3J9lSl7TaTinur6cRpnm3KgZOCzZan6U7B4OuamCBRSRCTEGhJSAa+YS1N6e6glHsGEi+2OhaU3NhY0Z3Ru8pvmKGAoSUELzmtPV/J4w10YfCydrVxe196Gr6Kp65CizTJxZ1s2aF3CXqNoC8b14r3h0PMOsF9EgmdL72g2hWylpirXXVBQMcNs9q0IsTsht/krQq1427JXJCbI9yJwa27lFVvEYrwjR3TwzXcDjUK4ZKrEEnicYc9dgpaX6Fg0c6XXYavTxlh4+JmDXbJA6RBNNWUTUM03M6sxtUyiOyTp0TZvTxsrtWNFYXEgLeQLapQTVi21m3xXPa3mqv4cGWgbElm66lrCEWHnTvZerfB8PVGXFfrfbze0j0bKQy5lO4tdYu5fBNqXRMYgkTaJgt6YtVRzc5Tp2W2Kb1sylapd0OU+MB7hZ+geNahyU4Y9nDrqAUeSlsELiQOEuwDJmTSWdJEh7vwYgFlISUBDiu5Q3gd4BOS6FC/8Y9E39U+zopoxBG7c6wUm3LYcl7DDbS9a7UDJObHzDUHKlru7uIdu91kl2vGqapwuuPv45LZJ3gQ9OvwRuvole8uWHDGQ509khBvKhh+6K9hUPq85nlGrkL5ETWrsrytcDW6U2gmVJNCxx6HIVpPHkZXdjWEPFxcZUvtk5trxvb1hHZXju123ibfuo7iFCC/O9YdMeRqyV6eeO2Q6NJBUuV7uMbDI38bIzTytPMyGBMrd5LpdHMs45a5F5RoHJ6GVr5N35uTdkvQ4IRFCKW0LYWYdxU9tzrBs8Zhv09cVfPd25EkXOaaLbfCXia8Q4bgXTjKAksjAR2hbl6KieCzEDFknKLdjDJmvO2ZLWwA6yF74juYOl4clUjMW3wkGtJFZVp1DzVErjYpyeS7gEeozu0pDdZ45X5weY/YEVdjZNjD0qJHlPMZCo1228aEYJTQqpGBzoYHMZbBH2Q52Z5OdHND+gOZ9Y6On40og9IMkPdlRZB577QZRiUilnfnaNwlUd4rS0RRKjRlxKV/GhsruqdWUN7juq+pgTRy6Bivz2ldHk0D0skQb/DL6LAXUcMMWGn4LtDUXRANvRvu8K3LTVBUiwKEnvD9KnZcmtFLLYLXmwxB1fy04g4Kf8hdDHfYJRpfD5GnUPRK0xgpuFDbsVHRa++nWHpGO6O5e2ukS0pKoFypA005UzeQ3Ldrqi2v7YpysGXvgAb7LIusknnhyNS66nDYXkGunE/4w8EIihFfWih0pbTuahGZxCJL+9SD3ZGidizCGj3Zbf0dZJhk5vP4qZNAqzbdARBr3QU1O5oBZG6fs3a/ZHheSa2RdEyzOyLYabekyG3o7hi1U/KCb3beUIjWgTmaRC3Y+AFS0S138UBLeeaXGL2BHH/dJCXrWw23RCq6CNeVzVeHDYNOaw0xlPOhggXZQ0vT2C61nHbpqCpEAxOWjIMFmUlMm6WJwLgmZieo2Tt2jqu0jfp8Id+KuGDHgjnkZ0vJ4z3YVx7to1qGLr0qmtVg34KeYih4glOxC4LqLjaV6IVITZB4D9M7LEcAauRjb2FUprrtjRdP6+WyI3ufWoMdnoy1B9ufEmx7RrZJrtarRvIu/m6X6tuGVAE5UgYRYAVGru3zluKJ0M1q3AZMRS1L9wSvKSTUTSLcbao9sUPxom8NxrEptejX5oipR1UTdr1/jtagp/Fbj0PYsb6dkZV7SMzl3ogw2/FusslL9mEPSnS5kSwWxaP+4PekZTIrdbiQYHe+69NgtA0eTaIzZKZn5gDvzh5Vw0gj3Q5Vh98O1NGCOhfWiQBuSa9jghIfqwHCJsijdwnYKUMrT1H44tz0IPNLXyqdrJbJ+4nKLnx/qw5jcnPUpel1jXJorxW+YpYHZrSozOlVG8+p/V6ij/DdUOxlwPNrlrqb9OEihhQ2daRM4Lpsp03vtg4zWK17FALqbKTSao1KBLyzL1IXbkIaNcwjT3qWx1cDRUr9zmfsFvDPkgotukn3WGinrB6SPc/oaijEOQO6cWYYLV5bNRRoRJfEAMGEB2MCI6nHC84Md6rQZR9L/dNU4wZb2UvY6q/W2pmaUY22N1evuf7SlVdEvLIDDfoN6wDDoC3grvSOWJHu6Bc3U+JuWK0dwnZVJQGNOfgJjwP4AnpZ7uZpJ5LikyGg2fWeFZVmnM82/vb24e37QePbv/ca1Xy88v/slOd5IPP1jYjHSZlve58ea336N/X65cNb48ZAq+eZVpv14evw5+9OtD7+Syejs4jp+Y7S15PP53FvZ4fzi7xvceH1bddMX9oye7wZAWY4fTu/99fOarrg+4+Hfn8053ngF4fFl6780vhd3My34mJ+6cH34ueI+TJ8HfWB8a+3dr7gJPHFb6rZ3tfJOjATf0fe8bff/zcT4YlDki0AAA== -->
