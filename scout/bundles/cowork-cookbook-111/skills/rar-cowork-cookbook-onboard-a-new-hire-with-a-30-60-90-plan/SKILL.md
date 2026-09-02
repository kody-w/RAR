---
name: "rar-cowork-cookbook-onboard-a-new-hire-with-a-30-60-90-plan"
description: "Set a new hire up to succeed from day one - without building the plan from scratch."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan", "rar_sha256": "96132de281cbd1920cd14db062100b705919cc271dcf5be58dfd0cded2c772fa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "onboard_a_new_hire_with_a_30_60_90_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/onboard-a-new-hire-with-a-30-60-90-plan:f123a85f5ad61e3c555fada4c5ef26faea18cc285b40e17c064fa0987b04ad12", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "hire_to_retire", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` is
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

Onboard a new hire with a complete 30-60-90-plan — Set a new hire up to succeed from day one - without building the plan from scratch.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/onboard-a-new-hire-with-a-30-60-90-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` and embedded as the fenced Python below (sha256 96132de281cbd192…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` first:

```bash
python3 onboard_a_new_hire_with_a_30_60_90_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 onboard_a_new_hire_with_a_30_60_90_plan_agent.py   # or on stdin
python3 onboard_a_new_hire_with_a_30_60_90_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard a new hire with a complete 30-60-90-plan — Set a new hire up to succeed from day one - without building the plan from scratch.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/onboard-a-new-hire-with-a-30-60-90-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan',
    "version": '2.0.0',
    "display_name": 'Onboard a new hire with a complete 30-60-90-plan',
    "description": 'Set a new hire up to succeed from day one - without building the plan from scratch.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'hire_to_retire', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'onboard-a-new-hire-with-a-30-60-90-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/onboard-a-new-hire-with-a-30-60-90-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ccab66f4acb9cee8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-employees'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/onboard-a-new-hire-with-a-30-60-90-plan', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Calendar Management', 'Scheduling', 'Communications', 'Enterprise Search'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 1.0, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class OnboardANewHireWithA306090Plan(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OnboardANewHireWithA306090Plan'
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
    print(OnboardANewHireWithA306090Plan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
