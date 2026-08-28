---
name: "rar-cowork-cookbook-post-launch-readout-and-optimization"
description: "Close the [Product name] launch loop - what worked, what didn't, and what comes next - grounded in live launch data, not exported snapshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/post_launch_readout_and_optimization", "rar_sha256": "3a0357561dd93cd079e2f422a38334357f476650c6d3252c5af671be6405e4d7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
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

Post-launch readout and optimization routing — Close the [Product name] launch loop - what worked, what didn't, and what comes next - grounded in live launch data, not exported snapshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `post_launch_readout_and_optimization_agent.py` and embedded as the fenced Python below (sha256 3a0357561dd93cd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `post_launch_readout_and_optimization_agent.py` first:

```bash
python3 post_launch_readout_and_optimization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 post_launch_readout_and_optimization_agent.py   # or on stdin
python3 post_launch_readout_and_optimization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Post-launch readout and optimization routing — Close the [Product name] launch loop - what worked, what didn't, and what comes next - grounded in live launch data, not exported snapshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.1',
    "display_name": 'Post-launch readout and optimization routing',
    "description": "Close the [Product name] launch loop - what worked, what didn't, and what comes next - grounded in live launch data, not exported snapshots.",
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd9b7da7b16292559',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PostLaunchReadoutAndOptimization(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PostLaunchReadoutAndOptimization'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
