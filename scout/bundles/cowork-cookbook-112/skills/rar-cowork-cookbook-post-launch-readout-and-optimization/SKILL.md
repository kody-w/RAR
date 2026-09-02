---
name: "rar-cowork-cookbook-post-launch-readout-and-optimization"
description: "Close the [Product name] launch loop - what worked, what didn't, and what comes next - grounded in live launch data, not exported snapshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/post_launch_readout_and_optimization", "rar_sha256": "2014529f4b23606dc04e303068e6dc0ac3ada61aedbf504962090208f4534eef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "post_launch_readout_and_optimization_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/post-launch-readout-and-optimization:8d723b8d4b66cc540c46de18befcb887fd342fd64f72378d7cef16706a599ce1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/post_launch_readout_and_optimization`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `post_launch_readout_and_optimization_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `post_launch_readout_and_optimization_agent.py` and embedded as the fenced Python below (sha256 2014529f4b23606d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `post_launch_readout_and_optimization_agent.py` first:

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
    "version": '2.0.0',
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
