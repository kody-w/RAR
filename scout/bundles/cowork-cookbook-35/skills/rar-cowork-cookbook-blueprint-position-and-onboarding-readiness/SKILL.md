---
name: "rar-cowork-cookbook-blueprint-position-and-onboarding-readiness"
description: "Paste this recruit-and-onboard workflow blueprint into Cowork and it reports which positions are vacant, how long they have been open, and which new hires lack onboarding records."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_position_and_onboarding_readiness", "rar_sha256": "b86f56064705bcb4742c8e97a7e61bb3e8f81191be9525c7a60a74eeb07fc3e0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "blueprint_position_and_onboarding_readiness_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/blueprint-position-and-onboarding-readiness:3dd84718535d38575daf9bac3fe06c5c7cfe66f16a0cc135762442d21d9415a6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "hire_to_retire", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/blueprint_position_and_onboarding_readiness`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `blueprint_position_and_onboarding_readiness_agent.py` is
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
