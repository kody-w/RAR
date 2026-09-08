---
name: "rar-cowork-cookbook-competitive-move-response-kit"
description: "Builds a same-day competitive response kit in Microsoft 365 Copilot Cowork: exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update, plus draft email and Teams message hel"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/competitive_move_response_kit", "rar_sha256": "9aff2f12ffadb1a35cb4b70f6eb6996f88f4aedda714291cc5f5eabcd90a6935", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/competitive_move_response_kit`. The original RAPP
agent is preserved byte-for-byte in `competitive_move_response_kit_agent.py` and in the RCI capsule.

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

Competitive move response kit — Builds a same-day competitive response kit in Microsoft 365 Copilot Cowork: exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update, plus draft email and Teams message hel

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
  Upstream entry : https://coworkcookbook.com/recipes/competitive-move-response-kit
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
    "competitor_and_move": {
      "description": "Competitor name, the announcement/move, and its URL.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "marketing_channel": {
      "description": "Marketing channel where the Teams update should be posted.",
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
    "owners": {
      "description": "PR owner, Sales Enablement owner, and Field Marketing owner to address the draft email to.",
      "type": "string"
    },
    "product_category_and_messaging": {
      "description": "Product or category to position, plus the messaging doc and battlecard folder to pull from.",
      "type": "string"
    },
    "team_channel": {
      "description": "Teams channel holding prior competitor discussions.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `competitive_move_response_kit_agent.py` and embedded as the fenced Python below (sha256 9aff2f12ffadb1a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `competitive_move_response_kit_agent.py` first:

```bash
python3 competitive_move_response_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 competitive_move_response_kit_agent.py   # or on stdin
python3 competitive_move_response_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Competitive move response kit — Builds a same-day competitive response kit in Microsoft 365 Copilot Cowork: exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update, plus draft email and Teams message hel

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
  Upstream entry : https://coworkcookbook.com/recipes/competitive-move-response-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/competitive_move_response_kit',
    "version": '3.0.3',
    "display_name": 'Competitive move response kit',
    "description": 'Builds a same-day competitive response kit in Microsoft 365 Copilot Cowork: exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update, plus draft email and Teams message hel',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'competitive-move-response-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/competitive-move-response-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '737840e32bc4ef19',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/conduct-competitive-analysis'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/competitive-move-response-kit', 'uses_skills': {'custom': [], 'ootb': ['Word', 'PowerPoint', 'Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Fabric IQ plugin enabled in your Cowork session', 'Output matches: A response kit - exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update - substantiated with Fabric IQ data and routed to PR, sales enablement, and field marketing.'], 'confidence': 1.0, 'deliverable': 'A response kit - exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update - substantiated with Fabric IQ data and routed to PR, sales enablement, and field marketing.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'competitor_and_move': 'Competitor name, the announcement/move, and its URL.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'marketing_channel': 'Marketing channel where the Teams update should be posted.', 'owners': 'PR owner, Sales Enablement owner, and Field Marketing owner to address the draft email to.', 'product_category_and_messaging': 'Product or category to position, plus the messaging doc and battlecard folder to pull from.', 'team_channel': 'Teams channel holding prior competitor discussions.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Get a coordinated response to [Competitor]'s move on the table by end of day - one story across PR, sales, and field - backed by our own performance proof. A response kit - exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update - substantiated with Fabric IQ data and routed to PR, sales enablement, and field marketing.", 'expected_output': 'A response kit - exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update - substantiated with Fabric IQ data and routed to PR, sales enablement, and field marketing.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Fabric IQ plugin enabled in your Cowork session'], 'prompt': "[Competitor] just announced [Competitor move] - [URL] - and we need the coordinated response on the table by end of day.\n\nRead the announcement and the surrounding press. Pull our [Product/Category] positioning out of [Messaging doc] and the latest [Battlecard folder] and bring forward any prior competitor discussions from [Team channel].\n\nPull our live performance data from Fabric - share movement, growth, customer momentum, win rates - to ground the response in our own proof.\n\nBuild the kit:\n\nExec overview deck - five to seven slides on what changed, our posture, the response plan, and exec talking points (PowerPoint)\n\nInternal guidance memo - what changed, what didn't, recommended posture (Word)\n\nCustomer-facing talking points (Word)\n\nSales objection-handling sheet (Word)\n\nTeams update for [Marketing channel]\n\nDraft an email to [PR owner], [Sales Enablement owner], and [Field Marketing owner] for my review.\n\nDraft a Teams message I can use to update my immediate teammates on the work underway.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A response kit - exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update - substantiated with Fabric IQ data and routed to PR, sales enablement, and field marketing.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a same-day competitive response kit in Microsoft 365 Copilot Cowork: exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update, plus draft email and Teams message hel', 'example_request': 'Acme just announced their new analytics tier — build me the coordinated competitive response kit by end of day.', 'inputs': [{'description': 'Competitor name, the announcement/move, and its URL.', 'name': 'competitor_and_move'}, {'description': 'Product or category to position, plus the messaging doc and battlecard folder to pull from.', 'name': 'product_category_and_messaging'}, {'description': 'Teams channel holding prior competitor discussions.', 'name': 'team_channel'}, {'description': 'Marketing channel where the Teams update should be posted.', 'name': 'marketing_channel'}, {'description': 'PR owner, Sales Enablement owner, and Field Marketing owner to address the draft email to.', 'name': 'owners'}], 'model': 'claude-opus-5', 'when_to_use': 'When a competitor announces a move and you need one coordinated PR, sales, and field response grounded in Fabric IQ performance data by end of day.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CompetitiveMoveResponseKit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CompetitiveMoveResponseKit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'competitor_and_move': {'description': 'Competitor name, the announcement/move, and its URL.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'marketing_channel': {'description': 'Marketing channel where the Teams update should be posted.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owners': {'description': 'PR owner, Sales Enablement owner, and Field Marketing owner to address the draft email to.', 'type': 'string'}, 'product_category_and_messaging': {'description': 'Product or category to position, plus the messaging doc and battlecard folder to pull from.', 'type': 'string'}, 'team_channel': {'description': 'Teams channel holding prior competitor discussions.', 'type': 'string'}},
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
    print(CompetitiveMoveResponseKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916aZOjWJblX9F4f8jMJsLFKkS0ldkgARIgkAQICTLSItn3HcSSk/99HpJ7RGRVVHWX2XwaxeISvHf3e859Lv54sbo2LOqXTy+qZ+WLnZWmUejVCyt3F9uiL+oE/CgSG/xbOEXe1pHdtUXdvHx4cb3GqaOyjYocbN90Ueo2C2vRWJn30bVGsDwrvTZqo7u3qL2mLPLGWyRRu4jyhRQ5ddEUfrvAVgTQUEZp0b4p/LTwBs9ZFHevvkdev3A9J/kANrVenVvpIugi18odb5F5WfFh4XRNW2TA4tZKkygPFmUBljYfgB2p1ywKO/ac2cRFE3pe+2GheVbWLLrStVrvw6JMu2bh1hYwxMusKH34/VySeU1jBd4i9FLgrDdYWQkEvnz69bcPLxF4//LpjxcntRpw6WX7zVUJ2K28eStGLdiaWnkA1pQjCHQOPpde7Rd1Bi65nr94+/Rz46X+h8V//mfSW3XQ/PLpc754e31+mf8oXb5oQ2/RFlbTeu7CsUrLjtKoHV8XdNpbYwOC3HZ1/sgByFMevD53fpNUlIu/zfd+fip5Dbz2588vBTDBmkP0+eWXRVEDfXU3v3+dpZQ///KaFr1X//zLNzlN94jqLAxY/frl7fObWLDw29LIX3xRT+z2TVftOVHpAeHf+Te/nqa/iXsLyZfn4p+L8sPix5Jnf/4G7H1Wog3k/lgsiAHY+fIag9L4+U1HDfKUz3X08y//TKwTgspLo6b9H8n99Sk49CwXROstJL98eKTvtwX05ttXmf9cbQkK5t/xBCx/V/c1UP9M9iOzfyc6jXLQKO+5/KG4H22A/rb49Z/69q82fFj4n18YLwXNUlt26n1a/PEokV9/cr9d/Om3P4Ho/1aMWnS185DwJbPyyPea9suXX39qHpd/+u3Xn7oSVDHo5y9dnf5I5o/i+tDzlwi+rfr5r3uB/kue5EWfL7720OKPovxf9Z+vC91KI/fb9ebT4vtOnF/QYnbiXekzBN91YwNs/S6Ov7z8CXAnB950DzybYec//uM7IFWdomsXIMFtlHmz8VoYNQvwd0aN2gNxbSIQ2Ld1oP7fgbHwF7//b+cBvR+dN6xffgfeXzLQKl/eEfwLQPDfXxcaEFrUURDNkKzQp9PnHIBl3s4KS7AWYDcAKXtsvY+glz/Ob2bc//1fyv3yEPFajr8/cDh6Ip6y5We0a7rUe539uoZe/uaFAyhrJosOSE8LB5jiRwCkP8x8U6SAd9o5Bk0SpenCjQCeAOoaH7JBnD7Nwn7//XfbasLP+ROescWT05olWPDVnMXHj8AnP42CsP2ce05YLH7648+fFv9n8a92PYTPOk6AJN6yACwU1KO8AF3VZWAZSBBIKYCMRxb++PMtskBMDigN5CzyI++5GVRl4rnvYVb39EeUWC1sD4QXhDYri7qd6S9qXxe8v/hqL1A635pZISyaFrBp6eWulzsjkGoBd75GMgcM3IDSa/zxw6JrvIfW3+3aepiYgfa22t8X0vYEOKhIwX+zmY9FYHORRyD8X4vgeR0IqX9qFpt3Ea8Lea7DRWnVVhnW1psO33rmBXDP+3Yg3FrkXv85n6nWm0P1aIpneMAiEBnnLaUf55zP0wZAALd51/1YY81MqT0Ys/4MiuxZ8FY9p8KZB4zx6zjxX28l1YRFl7qP+M1DBZD0lgX3LSuPGvyO8BdzGf91wPncoTCCL/5/HonmINC7ncLuaI1lFqysKcYzOfOUOCfxOViC+WQBKvTZiN9mlndceofnz3kagUqrx/96rnyk9G3NE/K6GmRAoZWHfFBPwL1Z7qPc5/Kt67lRrM/5Ow98AIF/gB5wFGAD6J25ZN8VznffLQ0BAMyfv80Ej/Ko3dl1UNKLsrNTUG6+57m25STAqnpu2bc0g9r35vbtw8gJ/+LVAkgHJQbkL4AREWhCwBWvX7H5effd9L9sfI4+85bHWNiBjq0fAoAd3mzgnJQ+agFwWe1zKAd+fnoIAW5kZTv7boOeAZ4+L3q1V3VRE7UzPj7j6pUAmD/OP5+ezle9oQTVAYIFmqHsQHQf7TNXUQYGG2ADKD5QdlmUA6IHQXkLwkMgKHPgDsDat0n0KfFx+c0h79FzM0O9b5wdmffMpL/wgengyvg9ZGg/KhMgL5tXPPT+faV91TbLnmGzAdAHNL7ffU4Hr0+Cf04Qi3e5n/7h1PPzv3cwelD25a8F8GkRtm3ZfFounzT7zrKvAA+WT1ub7xn34wwpH98B4iMAiL8Iffr7afHvGfYXEW+N8WmBvMKv8Hzr8FZYby8Qh+3HjfERn+9+zhXvG54C9UUGKmvO2ggo/iv5vS8BDBjUXjAvfpJhM3NoD2j7gf4gBZ/z7yt97jRALnkwV2ZTfIcAjykAVP0zY19JCtzKW6DbnafFwHudD1mz+Y338inv0vTDSw5q7r87l80slM213MxHOdA1YPJqI+/x6T0ZRf0F2PCYVObLfz3ybr8uWsz6nl01m9iBQM6UtZz3ffjqxUU5zKa2Yznb9jyjzVPdA4eG9h8VHB9vrPR1wXgA89Lm++J+I6qZqL/rwWc4QRgd4M6HxQzpzUysIJyzp3P/Wg1oCNALP7Qls+rEm9t9pntAd+k/WiW9L1m8LZlTWz+p/HsqebfQBuhTzGfWHyr8Ou/+o6IrGDhmzHaLTzP3fnhDtpmiLPDp63EDuPl2AJw1eHkHzta/zkedOcmPLfMbsAf8+Lrp6y8wbO/ltx/Z1edvlfFXo07K4nHrw0J9sCmbz8g1Z/v9+pxuLvKA598i9bg1+2K5LujrZyK/J9m2+GF0gPkuIL8vDohnAGakZzU+aHhe8Y/WPdfPGX/fMmsF8Y/mFW/sPiv/KgSE13nYDNiiTT1ARy6ojtR92luCdnrA8g/Na+eT1T8tlGcxvBdJCGQ+hpE6mq371jtu1ICJZYaj5gdKgJYHcQH6n7P6rVy+Je050DzClVrt83crf7yA1rZAGVpvzf0284DlAOc/NvOstwTgBxSCz0+YAvf+vXPQ2+YmtMAoDnZTlu+jPoL6vuXaiIURjo3bJOyvPHtFUSt/vfZxy3Ndi0RwlEIch/AJz7Idl4KtFYURQN4T6b7M02w0G0RQpA9TFOrjCAq7ruejuOuuV+uVQ5AobFG2RdgEZdnftoKJz33z8unVn486ejuSzdF4c/aPF3uFg5V7vOHp52u7hBBnRRxsubSheuXTTr4qUGJvqOZkoubtdiH3dooJcn5S0ZMpi6JacXzECpZRJVtXaDXdvU2Xk8SuVxq5d440XSXVcYWyKyerEyQto4t6ZAI8hSiH3l74oOHKe5QmpVojelHK8X1dlyo5amw7FGo91NhyfZnGTjfLgj0nru2d8cg2Iqqz4LBqpTunDCDR66uRk8tlunfM4iY2cL08YNKId0JypJLDYSNCui2oxJ6HdiKrmpemGQO9Qor0olgMQ+aCMoqda+p3c5tV4gE5o5ficjTsivVDvlRsAs8cUx/rU8gRh6uBsdaQtq0YHQSxTtSNUtYXXVWyDWtHoh5F4YEUtjLClJZq766rK9OvTvm0XvmnPYlAUHJeL30bgc5Q6B3QK7rdGWNUKIh7WR2QK8I5jROLo87l3EWhOx2O5XU1bfFDrujBnQ90oxnF2jlN0jZVq4sdBBxyk6+pJmlEgUnZfpVI3ngcq6Dmor5iR0QIDYoLWFSvRO2GcnTOq62UwdMI9ce+sgkrbnHy5FrajTrABe+OUqjH4nG71tC7QU9Qy1WZOKSMYConlvNokQvlq02YyQXSBadOr2u7Q/bBXiQEt9gyYiD642pymA2u2c1EDtOpvqbGVbmqQhPCR0VA0iZSS1ziVGtUxIjQW4Vgdf1aKRfEyhlaXh/WpdjWMF8VlzYLvDEVocrUr6l7jkWYMuONb0s+lh5cgYGsFa1cNrynw7psaKtjQcGKaU2Rcog2vbG/UF2hHblhOrS5UW9qcqvIvZbC6THdrCmlUwwxrM8bJokcZTmdoWvCMCq5lQTkPnS8IvYus8s45iYmm/rcy/hoEa6sNspKV1IOqRrDv8tXAruZKuDBkfPWFz+s2FVjQ9zJr/f0cq0pIHopHuf4BW34PArRkGDM5shMlxBiiHRp70qId/WL7uXCyN5PLCrhB9wP8jDlKLzY0xm/iUlhEzBbrbfMitIajWw8XWsYvGd1iM1xz8fXMIaUTHMimM3KjwcGOt7Xe6E/pI6ah1eFvzKlT8sMn+ntcOVrlxurouVzuwnW1woRO+uwgfjYXZGM0Ye3HqqQBD5T62a09lHrKm3Ek8ghzwny7Er5LgZVsE+DPSpzRMqZ5pEX9XFzvuwCedr4R3ztM/iNWd/0gDGU1T6Qt32S8VEUF2EwHUffcDR6JCfJEGT8eJ9Mcad1LSRURjLamRbKk7UTChNpTLbYk8lRoKhpULokikl3UO4T68nCMWGtcwpt0/324KbG+gqjS28yJm8ZpYbVrFwmVfWgo6aja+LjOkD2BiAf2RE3SC7RBj8uKWkI+BsmGoaT+mcmvG5s/S6V4dm7gk53lXVpJkm7yZP2LIYZJhwqmas8kfDio3PVzMjeo3qK3K2I8XDDl+W9zhUZ4orrzApHFnVxI7F7NpBSh0ip0kYltJWKkqahaNgdRSbvXTcZVO+g8tKm7W40c0eZ466L9G0INRHXgFrBdf+iYXTe6YqRWjf+Xjf0Zk9uyG1jGHxi7sZ0v9mSecoEx77PA2nCi/t5U1pyfL6ZB/aCmIJ6sO7nY8SQhzLAmCy/YB3N5PW6s6bcumunmBiLIcgKgrhtlphEMtfWViWS7y5DidN9TCbEsCbiqtURMw+JHeFCdrulcIG6taW3Zpj1ET7hhULvVgm+OVKENmmXy/1W0pudm7KluCNr5czhxIYfvYxgKifSjMED1HoamX57iFQRiuFmg6aswh/VwGd1HHKyMfKFVX+2kfVaK+DMbGVvp7KmlPCmFbZofKjMqLrk1yiD4VTOAiW3kcTWo7N68s4dJx1496KY6Pq84ROs7QIqGPR0e2admhbo1K2XR/Ec6sFumwcMTbNMrJxljtEotq45/H6VWKs6WGOxN0c0FukEvloHGC88LSeI5lbCKOWfVL0Rr1fFIJZ0EkCxGqvVikM9wmyobQzvttJ41NoJX+8cOTjcUVLcynymnH2yXpbL5WqVy8Ry3XJLQXf8+95HKrIpxe3GMEmizvgDXYSgLrQWP5pmuqvY6LoDbNnoyJj0jizs0OFcWdkwMQWe4WmbwFg0VWp7hm+nCI2OXHKQVVnqo/UQ87aw9c57yiNaxkt4kd345QCapoUlaO0oygEqPFehIw0lqQM06Odjgx8sjfWM5prhaN0cJ+4Es/VEN1ZPRATPirJMHvb3KkM2U6dz5drWolVoMaMXhavWvtASLPNqekBUC26sLoyskZkyKOC99fW+ge69D8HL7bTkxKs5aKBdWy1qSRh3z2xFRbtWSO5rcKjbpZAMCJs+umNSZRnFX53NVJKAuxIyqXgR9d0dReisbigJU2eRJ5oic8u3LN/f7lWqiNzGlFjBJdTDpQjMRBC01XkXWloyNn0N3VarQK2s0bFW68tVPfPWdThtTr2VWQrOu2IxdSJSGm5LwJhHiVXFEtcDS3hszoc36ULvtGwtHtOOvlXklMqgigqJO2wvO25d4m5/K8+JoZc3/hAk/jWS4SlVxUt3zAa2R5WIclCPsUc80vIyHE9Oua/7Kw3SfvRA5RUJhpCQIZyzkb+Ly52xj9FI6E9EHAyHuzRqx/LmE+112tMx3m4H5RbTaYHHbsgmDMunTnRPnFShVDKStRTh1/tor1fjYYS7k3s9VfuwOMP0PSGWbrpcqWYUnDpeU/LY8bbUarhKg4hXZwUbqcvVsyXvJoxT0CngvJOhe7zc9Y6A0rnY0vaIYhmxGdvNUtRpU1wjbq7BUB4oiTdtCHo0yMExV6G6y+7BNcAIvvKVCpsG2YokNmOnRNzyzEUupPU5NZEkja2GI/aJpEexL4xZd8C3GdbjxnZVrDbpTnD5cTM6aMqJR5XMrMB2pgMxHJn2LNeVG8ghrJ2CEmUmA+mL4ppcPamDDtyyrxhGDuBObUlisM0Uk2IctJHqK5iQqXEcKLUXHJB2W1nrK3VtMrq8qRB9TbMUFTb4RDZuo13UbXmhaVmqj3GLpRIMyRQzRJITmFuWsRuBHXeBsOOCSu0EQVjHV/FUC+muvGXJsALzH6bBuywy5cZbRziaXAx6S9QkI3GXgDKP6Zk/rFRB1lnBT7B1E7D3EJHzre6n5xWEh2ljUEfOuwjGZsiEjMSVXVyWXZ8uT/c+bbGLQ2zLPR5X906kMY4lTiuoheNyv0bkwizQWMU0mWXPjmbgfMwqAt9VurpNYgUZVIEqnFT3rHQn7uXK3anqmhRvZLXrmVWyE3FMawkl2elB4HcWG7DWmMI0FNdyTuDiMpbONdLcNSVadkcPW++ubd6O1pIv9J2qi6OPyuYd297XLVNFrWgLOTwUnavuMwX3teOW6tY7VkeOJgMwFlDPmchsJYt3N5pzqkETjEvKZ1trV6yEnS9q+HAeLimtE0Z8jBxVYDYsaazYlltBlMTrrJUnXF+sT6FrylWj7sy2kIZRt+NARTtL6daxK1oWQeZNJ6LSXu2ku6UN6XJD5grghCN9XLoYvgPnOIyeHJhT+C2XlCN5vHKb+5U7Hhk0StHDchJdSBkK0RoBxrGGqcI8jV20msaCJUdI957t9aNYUY6nORjhojljnjsYlYNum58Mwoe33SHEnalHohi65xzZNnLn8fqdgoR8e3A2mKNh25vF785nfOMz6m1aFclW1IStA3FdPVRr6cidVsbSjFwY5g4c5JlS7KMWqt7VHS9LPENchF4p2+21DK1OS/BWb2Cr3AmGwolb1zLuvhVZsqlo53spahsKc5xGutoBS2qHCJxM2tgOE+d+LlEzZ5ohv9fZ7toU6hUmj+5aU+uOZPuT4qhNvet1M/X17H7CGIe4WwEmcqsAIYQYMQPJcPRtE+zlMYTjXb0Jgy0HdZubjEMbhMXq0ZWW9/NeEDBe7NJsnd63IQc3x/1NtBM8wJdGZCnlFF7TybzIaKtJ8XbMFfRsk115lGu9XPtsX7Se3Ds26d3w60pUbToGiyfPFqM0iwNv2Oz1OzwNCFs2d36IrnV8ODOnXleafkiDWr0mCY87WENfQnDIOFH4AYolg8Lt6HA+KtvDeroo+Q3HDudl3UBSLVpUcsN2AAaLgB8u3L6qXbkeDmRg1QncNKshygvRYRt+dQaDkDHxDk6o0vbW094ZnKjFOMvDPoZvDqfvKDAht0V1LMvpPGSXiM23CXKgFTAqpmjsXwlK6Ffb6qB2IzyMPJU5TrsiKSLHm4mxLjfoRkEryl3fNhVBKCcv8KMD7y+vKhQK90Qg+RO6Zep9vTqsgsI/c9tl5eQcF904Ywi2OJRfu3Oab83ydty5ZjbqwYjjQk1v4mDZX9mkUhBhCBQ17c5KJVxO5CGQ2HLHmEANN1XhebcjbtdygyqVuImty31HWDpqEOeL41iIoTa9kGy9O2THMrbNBOsYA9KojrEFWg5qYyaWmLLLmHIZrM9Z48EkJLP+JofOjjeRerLrxyG6qD3wBxcIN2dNhG9c4uLdhz3uy9aKH+QddiTuYQdJiY8hHMplqJjyBIetmbV2M642esZYgxEqU6RyrAPHhTLM6LpJnMyiV0cZYxuGKaoqP2dGP+VJWPSUN9Y4LInnTQBR/AAtsUJxSRGbknMTDGu8TfXANwdKFbGkbpPqfrpXy5pXkBEabgOJqMsqTOvuxKXt7RbynX1i2JQgyBpG2TJXnNhqDyQJ5Y184tNVNUo0Tx/OHS/zjpzc9TMNdbZ3XQJmzZaqvDnZ90N8m84FWScsXbYXUctc+4BMkJZbLYe33Z7eQyeMXOadhPXRdgPFo8y1pqddvdrpMVHJLytqk3kIlZ3joJVsCiLzO68OedkdvPW9imur9ZH2MK15OulRoe/iMnLvJNoJmJNCBHbOCaZZ3Q1nh0W7jQ/T/UmadGfPFPBxW7mWFth3BzZZv0UIpD7ecbnIcpKwerLB9Fs5nRSP8tyBQqQuAkU3OVF29y+d5R/UyJQ2qxPFXlWpqSYpNDfMyeX8g6Kukl6ZKGkbNFlnkxU2Nm5XnNwJdnVzSWiM3qC1hnSETd666rjhhiQfthDDWLerFkC1WYLBh2lbgD/rqMHyoUjI8aS4jr8sYMY6r+uWtM4+1ElV4e+10ieQdZV04ABMYREcrTbr3uqGekvAHnO8u8vNzVjGiuPG2wsuw/Y1WO9BBa9uS2o9LPGUOOBBPEn+CXGXx5ZjhntPCvtpuOqXuj7fFDVubk7Qhv4q7nlcVvIzWXr0tJQYRz5uTtVBi4q9LE1KsgmC7OJmKh8OIbQRDntT4DbOZlRPRRfjlAG32nkSsKaSYy+Y3HZDoGx9EIl0wx8RiBQdbz2A7vZ306bbjd1m2aSDk11PhRYZfTcajKgLl/Vtfey6pqMnT3Dwgykbo1ciGMlwWX8alfK+LWLGWGXNRJboWh4c/HybtqbruLs+7CmuWMnU6O5XYnVPB+p6Qi8Wn9JDiShsQiN8wgwEtFcGzLz6Ow/lo3BH1PXFNUQTrhJrMqShda8jdqIKvRriRL/uC8ae2szcN0sAR6eGHehNTlRmAm0zP5Q0wduwnG+wYNDKSHQ37IbeOBXmzSDEVSpuz9LaKCuvO2McxxlqWq1792RZx0yyMQlfNeJtG9LXQLthgT0kJH6rPWUQ9y1Jy7mGVTAj4UVhX5P9nTD8JUmkCLQzrgF02SqGuCMIkSR862TvLheYPTkKHLhDGl0OacIfub1CZDddDpc5unfi3Tpb1tbaPQWXy3Rz7KiTSAc9yYg8XAZn0O1j47mRmZ37bJnuUL3nsaSbxiHOEIewSA1zUXtFMG0xdtda3i3LUor2R9i9H+l9q3MedDyuD5V4ZzrrpuR4zOOYj0DRdqlqm0omVZINDlkgQUjhTl6ceRsXQaPpvjnJZFjaV7yQztQqPRhWbAGSzwiHMjucjuiisWrzdN9gDN0Efk9QU6rAiMKvThvSwcd6VdwqOvNR9yDXpy3n9ZuyRskLj8okjNRLokzhZJrq6e4fpSVlJDpMStIaI5YWoY0BODqJmeuSp6GOu+K2SkxtZ0VEONHXekOAYfZ+826idG2XkDieCFpF6EO+J9qhTN10AMOoH+KX3eXGp3VChL2EFNu8s8EYtBQgp1Vq3e942FJqLAc2217qVasqtiffxXQouV36GOOxC7VejodGGuhLmRJ7ZCOm3vVI7W6MwyvZBYL0PVaHOXdHKM+g9UatU2YdwYLi1rftyd10Qr8LgzJc8pxUWKfjjTj3spDElHIlTgqUVupoXxkVEow1zp7wJqJwagwgUdM8gdyLLg7BxwPbMePdPsZrOVm2sjf4uGFd1yfsvCn8gB1Y22HPMRmgfFGv2VNLblYSdqb2ZqlSFVuHAqkuNQEAKIDscUetesS2kI4c8Rhp6/5cQpTFO3s/MMGZ1vUwW0+J/pBBbbtD4rq1CcmWRUvJGve8POzl9Nbv7OuuU+3pxA3Y+sD3hgTBkLGmlNvSKjSJUiyEMDNcrDwSmgIACqO5Z4fl3R2x3I+uG+Lg3WrOgMN1Fmwt5LRVOfzAlSdXIhQu12oSXVWWfsC1lDDX8WCHNTHu5Ftbk3pn5XptueTlaAh7Y38WnYLFiDrlfb8r1aUBSd4l87por2xN3jNSOO8UeiJC80i7WxeFluiNVmATxg0B6nKaE9vTtXAPXntH02Pi3eURwpgNWW6Ju4ifOK5BJow++TvBgcvVAF/AUAFRwjVDDm56XJ+2ecmGVhWX8KG2wsMS923LXI88epqYEomRwvNQMssdbSkYSWNwZcFszUbmEDufPNizVySddq4SMWRI9+MWA3NHwAKYUoPbOsRRY9OLnB2gPmnuUfKoHfeXi8Pl5H0gUWnlb5ATs3PdFmo4ipWFkKIia19cyN6r2tXUj2NdZXhyD0aP7JYjWbXHJb6HDsu0wmyUnAh7aV6nVKaytdTtUabE/E1AhgS33sIJDq1aHUETnRsQRm0HXfeWrCNgPtyq6XX0enxpQc7Kj/V6Y+P2XhpQEXNsBLJzeQ9Gbn/odq2B7smjgB4Q0kMz46SrrZcvU44v96vrFUY8fFmyHBbdAzxwqMv+nGyLHZniBJxldMXjYlIGjQgQU1nxHooWDbnvENMa+Tx2rkvRHOXiOO6RS7vfYMZpDFRNjdcriqDJVLndYSjsJtvQbMpbrjjoLpyD5TBpWKzVHp5CdljseaY0JOTWUd4m9rjp0ATYcdhtE1iB8RVdhr013e06q+8chq1P/qY6HzEABMtlvz0pXIZopr9b6cN9qYeWZJNp4IQ9HmTxxdulDrW/977WEPsgIUSapv/28uFlfnDh7fGD/9nDjvNXd//PvkF8ftn3/hzT43twz3I/PXR9+h/a89uHl9qJgDXP70ebtAvevlD8u29HP/7LZ1bmrePzycH3BxyeD2e0VjA/R/8S5W7XtPX4pSnSx/NLYIfdNfPTt838gLYDfn7/FX7Rhl798nhewvHK9ktbfHk+rgCuWe59dth9mR+Sbb3g7UtikA7LriPnS1TNbr099gK8wV7hV+zlz/8LgRcY0AAxAAA= -->
