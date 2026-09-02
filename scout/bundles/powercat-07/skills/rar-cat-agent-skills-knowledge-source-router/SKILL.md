---
name: "rar-cat-agent-skills-knowledge-source-router"
description: "Route Copilot Studio knowledge searches to the right region-specific source (Americas, EMEA, APAC, or Global) based on where the user is, so answers stay locally accurate."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_source_router", "rar_sha256": "a6d2ac6a36c781505665b517953328f2dd809e91140dd40f56588569f87edeb6", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "knowledge_source_router_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/knowledge-source-router:76983aef509c9560166b4ccf73db557efdf8c0e0f4710a7b7f412d5bc7c1baf1", "kind": "skill"}, "version": "2.0.0", "author": "Adi Leibowitz", "tags": ["knowledge", "routing", "localization", "location", "grounding"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/knowledge_source_router`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `knowledge_source_router_agent.py` is
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

Knowledge Source Router — Route Copilot Studio knowledge searches to the right region-specific source (Americas, EMEA, APAC, or Global) based on where the user is, so answers stay locally accurate.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-source-router
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `knowledge_source_router_agent.py` and embedded as the fenced Python below (sha256 a6d2ac6a36c78150…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `knowledge_source_router_agent.py` first:

```bash
python3 knowledge_source_router_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 knowledge_source_router_agent.py   # or on stdin
python3 knowledge_source_router_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Knowledge Source Router — Route Copilot Studio knowledge searches to the right region-specific source (Americas, EMEA, APAC, or Global) based on where the user is, so answers stay locally accurate.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-source-router
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/knowledge_source_router',
    "version": '2.0.0',
    "display_name": 'Knowledge Source Router',
    "description": 'Route Copilot Studio knowledge searches to the right region-specific source (Americas, EMEA, APAC, or Global) based on where the user is, so answers stay locally accurate.',
    "author": 'Adi Leibowitz',
    "tags": ['knowledge', 'routing', 'localization', 'location', 'grounding'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'knowledge-source-router',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#knowledge-source-router',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'bcc9646e4cda8666',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class KnowledgeSourceRouter(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'KnowledgeSourceRouter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(KnowledgeSourceRouter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
