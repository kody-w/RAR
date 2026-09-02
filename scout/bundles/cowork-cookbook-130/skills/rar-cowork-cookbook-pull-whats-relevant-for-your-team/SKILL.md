---
name: "rar-cowork-cookbook-pull-whats-relevant-for-your-team"
description: "Get your team only the parts of a long document that actually apply to them - without sending them the whole thing and asking them to find their section."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pull_whats_relevant_for_your_team", "rar_sha256": "6f764939aa523b0822bc58cb35ea3eff7dd2548066690c8c000a3006d379722d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pull_whats_relevant_for_your_team_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/pull-whats-relevant-for-your-team:279da4bd72284cf59d3ed9db582c8292a0cf6c67976b2506cd2a33f6ac8cbefb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/pull_whats_relevant_for_your_team`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pull_whats_relevant_for_your_team_agent.py` is
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
