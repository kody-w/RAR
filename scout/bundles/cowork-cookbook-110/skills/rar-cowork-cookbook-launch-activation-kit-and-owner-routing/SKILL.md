---
name: "rar-cowork-cookbook-launch-activation-kit-and-owner-routing"
description: "Build the full launch kit across customer, field, partner, exec, and creator audiences - grounded in real performance baselines and proof points - and get every asset to the right owner with a review deadline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/launch_activation_kit_and_owner_routing", "rar_sha256": "79fc2933161838fb0e1a2e3851fc7868bdcaff5931c3e69b12bbd6ab95094f78", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `launch_activation_kit_and_owner_routing_agent.py` and embedded as the fenced Python below (sha256 79fc2933161838fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `launch_activation_kit_and_owner_routing_agent.py` first:

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
    "version": '2.0.0',
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
