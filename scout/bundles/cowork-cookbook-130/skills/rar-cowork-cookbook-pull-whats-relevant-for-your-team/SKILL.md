---
name: "rar-cowork-cookbook-pull-whats-relevant-for-your-team"
description: "Get your team only the parts of a long document that actually apply to them - without sending them the whole thing and asking them to find their section."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pull_whats_relevant_for_your_team", "rar_sha256": "6f764939aa523b0822bc58cb35ea3eff7dd2548066690c8c000a3006d379722d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pull_whats_relevant_for_your_team_agent.py` and embedded as the fenced Python below (sha256 6f764939aa523b08…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pull_whats_relevant_for_your_team_agent.py` first:

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
    "version": '2.0.0',
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
