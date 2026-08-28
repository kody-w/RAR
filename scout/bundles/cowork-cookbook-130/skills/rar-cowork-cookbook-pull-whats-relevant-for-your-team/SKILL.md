---
name: "rar-cowork-cookbook-pull-whats-relevant-for-your-team"
description: "Get your team only the parts of a long document that actually apply to them - without sending them the whole thing and asking them to find their section."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pull_whats_relevant_for_your_team", "rar_sha256": "16a83f1f0a4e11f6021200ded812a0d12a46204d1173679350fead46dd4ef03e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/pull_whats_relevant_for_your_team`. The original RAPP
agent is preserved byte-for-byte in `pull_whats_relevant_for_your_team_agent.py` and in the RCI capsule.

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

Pull what's relevant for your team from a source doc — Get your team only the parts of a long document that actually apply to them - without sending them the whole thing and asking them to find their section.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/pull-whats-relevant-for-your-team
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pull_whats_relevant_for_your_team_agent.py` and embedded as the fenced Python below (sha256 16a83f1f0a4e11f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pull_whats_relevant_for_your_team_agent.py` first:

```bash
python3 pull_whats_relevant_for_your_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pull_whats_relevant_for_your_team_agent.py   # or on stdin
python3 pull_whats_relevant_for_your_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pull what's relevant for your team from a source doc — Get your team only the parts of a long document that actually apply to them - without sending them the whole thing and asking them to find their section.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/pull-whats-relevant-for-your-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/pull_whats_relevant_for_your_team',
    "version": '2.0.1',
    "display_name": "Pull what's relevant for your team from a source doc",
    "description": 'Get your team only the parts of a long document that actually apply to them - without sending them the whole thing and asking them to find their section.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'intermediate', 'read_only'],
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
        "upstream_slug": 'pull-whats-relevant-for-your-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/pull-whats-relevant-for-your-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd4eab744a786086b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/tailor-content-for-an-audience'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/pull-whats-relevant-for-your-team', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PullWhatsRelevantForYourTeam(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PullWhatsRelevantForYourTeam'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(PullWhatsRelevantForYourTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
