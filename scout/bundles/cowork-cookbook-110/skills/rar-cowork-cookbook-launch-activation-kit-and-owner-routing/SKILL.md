---
name: "rar-cowork-cookbook-launch-activation-kit-and-owner-routing"
description: "Build the full launch kit across customer, field, partner, exec, and creator audiences - grounded in real performance baselines and proof points - and get every asset to the right owner with a review deadline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/launch_activation_kit_and_owner_routing", "rar_sha256": "79fc2933161838fb0e1a2e3851fc7868bdcaff5931c3e69b12bbd6ab95094f78", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "launch_activation_kit_and_owner_routing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/launch-activation-kit-and-owner-routing:49e11364f8177d35943244dfa2bb5530cb289bed4dfbc68d84b21ba803340bcf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/launch_activation_kit_and_owner_routing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `launch_activation_kit_and_owner_routing_agent.py` is
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
