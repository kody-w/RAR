---
name: "rar-cowork-cookbook-post-launch-readout-and-optimization"
description: "Builds a post-launch readout package from live Fabric IQ launch performance data plus campaign files, leadership threads, and customer signals: a Word exec summary, an 8-12 slide PowerPoint readout deck, and an owner-rou"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/post_launch_readout_and_optimization", "rar_sha256": "65569ebba1aa00e40cab133c971569cd9c38bddb59faf8217efe7a8f3748adc7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/post_launch_readout_and_optimization`. The original RAPP
agent is preserved byte-for-byte in `post_launch_readout_and_optimization_agent.py` and in the RCI capsule.

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

Post-launch readout and optimization routing — Builds a post-launch readout package from live Fabric IQ launch performance data plus campaign files, leadership threads, and customer signals: a Word exec summary, an 8-12 slide PowerPoint readout deck, and an owner-rou

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
  Upstream entry : https://coworkcookbook.com/recipes/post-launch-readout-and-optimization
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
    "campaign_folder": {
      "description": "Folder holding campaign records and creative variants.",
      "type": "string"
    },
    "channels": {
      "description": "Leadership channel and marketing channel to pull exec context and reception signals from.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "launch_date_and_window": {
      "description": "Launch date and number of post-launch weeks to analyze.",
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
    "product_name": {
      "description": "Name of the launched product.",
      "type": "string"
    },
    "recipients": {
      "description": "Exec audience for the readout, plus demand gen, content, and channel owners for the action plan.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `post_launch_readout_and_optimization_agent.py` and embedded as the fenced Python below (sha256 65569ebba1aa00e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `post_launch_readout_and_optimization_agent.py` first:

```bash
python3 post_launch_readout_and_optimization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 post_launch_readout_and_optimization_agent.py   # or on stdin
python3 post_launch_readout_and_optimization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Post-launch readout and optimization routing — Builds a post-launch readout package from live Fabric IQ launch performance data plus campaign files, leadership threads, and customer signals: a Word exec summary, an 8-12 slide PowerPoint readout deck, and an owner-rou

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
  Upstream entry : https://coworkcookbook.com/recipes/post-launch-readout-and-optimization
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/post_launch_readout_and_optimization',
    "version": '3.0.3',
    "display_name": 'Post-launch readout and optimization routing',
    "description": 'Builds a post-launch readout package from live Fabric IQ launch performance data plus campaign files, leadership threads, and customer signals: a Word exec summary, an 8-12 slide PowerPoint readout deck, and an owner-rou',
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
        "upstream_slug": 'post-launch-readout-and-optimization',
        "upstream_url": 'https://coworkcookbook.com/recipes/post-launch-readout-and-optimization',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f17d9d1bfa30fe27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-campaign-performance'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/post-launch-readout-and-optimization', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'PowerPoint', 'Email'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Fabric IQ plugin enabled in your Cowork session', 'Output matches: A Word executive summary as the cover, a PowerPoint readout deck for exec review, and an owner-routed Excel optimization action plan - all built directly from Fabric IQ launch performance data.'], 'confidence': 1.0, 'deliverable': 'A Word executive summary as the cover, a PowerPoint readout deck for exec review, and an owner-routed Excel optimization action plan - all built directly from Fabric IQ launch performance data.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'campaign_folder': 'Folder holding campaign records and creative variants.', 'channels': 'Leadership channel and marketing channel to pull exec context and reception signals from.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'launch_date_and_window': 'Launch date and number of post-launch weeks to analyze.', 'product_name': 'Name of the launched product.', 'recipients': 'Exec audience for the readout, plus demand gen, content, and channel owners for the action plan.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Close the [Product name] launch loop - what worked, what didn't, and what comes next - grounded in live launch data, not exported snapshots. A Word executive summary as the cover, a PowerPoint readout deck for exec review, and an owner-routed Excel optimization action plan - all built directly from Fabric IQ launch performance data.", 'expected_output': 'A Word executive summary as the cover, a PowerPoint readout deck for exec review, and an owner-routed Excel optimization action plan - all built directly from Fabric IQ launch performance data.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Fabric IQ plugin enabled in your Cowork session'], 'prompt': "[Product name] launched on [Launch Date] and it's time to close the loop. Pull live launch performance from Fabric across [X weeks] post-launch - campaign results, channel performance, KPI movement, conversion patterns.\n\nCross-reference with campaign records and creative variants in [Campaign folder], prior [Leadership channel] threads for exec context, and customer reception signals from email and [Marketing channel].\n\nDeliver the readout package:\n\nExecutive summary (Word) - the cover artifact: results headline, the story behind the numbers, and recommended next moves\n\nExec readout deck (PowerPoint) - 8 to 12 slides covering results, the top three drivers, underperforming areas, plan delta, and recommended next moves\n\nOptimization action plan (Excel) - owner-routed and ready for the next cycle\n\nSend the readout to [Exec Audience] for review and route the action plan to [Demand Gen owner], [Content owner], and [channel owner].", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Word executive summary as the cover, a PowerPoint readout deck for exec review, and an owner-routed Excel optimization action plan - all built directly from Fabric IQ launch performance data.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a post-launch readout package from live Fabric IQ launch performance data plus campaign files, leadership threads, and customer signals: a Word exec summary, an 8-12 slide PowerPoint readout deck, and an owner-rou', 'example_request': 'Do a post-launch readout for Contoso Sync, launched March 3, covering 6 weeks - deck, exec summary, and action plan.', 'inputs': [{'description': 'Name of the launched product.', 'name': 'product_name'}, {'description': 'Launch date and number of post-launch weeks to analyze.', 'name': 'launch_date_and_window'}, {'description': 'Folder holding campaign records and creative variants.', 'name': 'campaign_folder'}, {'description': 'Leadership channel and marketing channel to pull exec context and reception signals from.', 'name': 'channels'}, {'description': 'Exec audience for the readout, plus demand gen, content, and channel owners for the action plan.', 'name': 'recipients'}], 'model': 'claude-opus-5', 'when_to_use': 'Call after a product launch when you need to close the loop on results and route optimization actions to owners, using live Fabric data rather than exported snapshots.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PostLaunchReadoutAndOptimization(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PostLaunchReadoutAndOptimization'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'campaign_folder': {'description': 'Folder holding campaign records and creative variants.', 'type': 'string'}, 'channels': {'description': 'Leadership channel and marketing channel to pull exec context and reception signals from.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'launch_date_and_window': {'description': 'Launch date and number of post-launch weeks to analyze.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'product_name': {'description': 'Name of the launched product.', 'type': 'string'}, 'recipients': {'description': 'Exec audience for the readout, plus demand gen, content, and channel owners for the action plan.', 'type': 'string'}},
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
    print(PostLaunchReadoutAndOptimization().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
