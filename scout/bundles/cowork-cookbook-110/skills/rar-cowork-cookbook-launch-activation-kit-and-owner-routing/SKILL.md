---
name: "rar-cowork-cookbook-launch-activation-kit-and-owner-routing"
description: "Build the full launch kit across customer, field, partner, exec, and creator audiences - grounded in real performance baselines and proof points - and get every asset to the right owner with a review deadline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/launch_activation_kit_and_owner_routing", "rar_sha256": "b1b43c163c5cf26b946d3ded3d9cfb13396aa3dbd0c25dc7d0de3a49dc86d893", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/launch_activation_kit_and_owner_routing`. The original RAPP
agent is preserved byte-for-byte in `launch_activation_kit_and_owner_routing_agent.py` and in the RCI capsule.

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

Launch activation kit and owner routing — Build the full launch kit across customer, field, partner, exec, and creator audiences - grounded in real performance baselines and proof points - and get every asset to the right owner with a review deadline.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/launch-activation-kit-and-owner-routing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `launch_activation_kit_and_owner_routing_agent.py` and embedded as the fenced Python below (sha256 b1b43c163c5cf26b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `launch_activation_kit_and_owner_routing_agent.py` first:

```bash
python3 launch_activation_kit_and_owner_routing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 launch_activation_kit_and_owner_routing_agent.py   # or on stdin
python3 launch_activation_kit_and_owner_routing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Launch activation kit and owner routing — Build the full launch kit across customer, field, partner, exec, and creator audiences - grounded in real performance baselines and proof points - and get every asset to the right owner with a review deadline.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/launch-activation-kit-and-owner-routing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/launch_activation_kit_and_owner_routing',
    "version": '2.0.1',
    "display_name": 'Launch activation kit and owner routing',
    "description": 'Build the full launch kit across customer, field, partner, exec, and creator audiences - grounded in real performance baselines and proof points - and get every asset to the right owner with a review deadline.',
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
        "upstream_slug": 'launch-activation-kit-and-owner-routing',
        "upstream_url": 'https://coworkcookbook.com/recipes/launch-activation-kit-and-owner-routing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '49c0d6204b4fab80',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/launch-activation-kit-and-owner-routing', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'PowerPoint', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class LaunchActivationKitAndOwnerRouting(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LaunchActivationKitAndOwnerRouting'
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
    print(LaunchActivationKitAndOwnerRouting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
