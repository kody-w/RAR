---
name: "rar-cowork-cookbook-blueprint-position-and-onboarding-readiness"
description: "Paste this recruit-and-onboard workflow blueprint into Cowork and it reports which positions are vacant, how long they have been open, and which new hires lack onboarding records."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_position_and_onboarding_readiness", "rar_sha256": "b86f56064705bcb4742c8e97a7e61bb3e8f81191be9525c7a60a74eeb07fc3e0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "hire_to_retire", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/blueprint_position_and_onboarding_readiness`. The original RAPP
agent is preserved byte-for-byte in `blueprint_position_and_onboarding_readiness_agent.py` and in the RCI capsule.

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

Open Position & Onboarding Readiness Blueprint — Paste this recruit-and-onboard workflow blueprint into Cowork and it reports which positions are vacant, how long they have been open, and which new hires lack onboarding records.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-position-and-onboarding-readiness
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
      "type": "string"
    },
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_position_and_onboarding_readiness_agent.py` and embedded as the fenced Python below (sha256 b86f56064705bcb4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_position_and_onboarding_readiness_agent.py` first:

```bash
python3 blueprint_position_and_onboarding_readiness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_position_and_onboarding_readiness_agent.py   # or on stdin
python3 blueprint_position_and_onboarding_readiness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Open Position & Onboarding Readiness Blueprint — Paste this recruit-and-onboard workflow blueprint into Cowork and it reports which positions are vacant, how long they have been open, and which new hires lack onboarding records.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-position-and-onboarding-readiness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_position_and_onboarding_readiness',
    "version": '2.0.0',
    "display_name": 'Open Position & Onboarding Readiness Blueprint',
    "description": 'Paste this recruit-and-onboard workflow blueprint into Cowork and it reports which positions are vacant, how long they have been open, and which new hires lack onboarding records.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'hire_to_retire', 'advanced', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'blueprint-position-and-onboarding-readiness',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-position-and-onboarding-readiness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '12750246048c8972',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'hire-to-retire/blueprint-position-and-onboarding-readiness', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.529, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'word:blueprint', 'kind:blueprint'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class BlueprintPositionAndOnboardingReadiness(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintPositionAndOnboardingReadiness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(BlueprintPositionAndOnboardingReadiness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
