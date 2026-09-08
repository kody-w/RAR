---
name: "rar-cowork-cookbook-post-launch-readout-and-optimization"
description: "Builds a post-launch readout package from live Fabric IQ launch performance data plus campaign files, leadership threads, and customer signals: a Word exec summary, an 8-12 slide PowerPoint readout deck, and an owner-rou"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/post_launch_readout_and_optimization", "rar_sha256": "65569ebba1aa00e40cab133c971569cd9c38bddb59faf8217efe7a8f3748adc7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
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
