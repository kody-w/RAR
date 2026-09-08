---
name: "rar-cowork-cookbook-competitive-move-response-kit"
description: "Builds a same-day competitive response kit in Microsoft 365 Copilot Cowork: exec overview deck, internal guidance memo, customer talking points, sales objection sheet, Teams update, plus draft email and Teams message hel"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/competitive_move_response_kit", "rar_sha256": "9aff2f12ffadb1a35cb4b70f6eb6996f88f4aedda714291cc5f5eabcd90a6935", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
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

<!-- rci-capsule:v1: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 -->
