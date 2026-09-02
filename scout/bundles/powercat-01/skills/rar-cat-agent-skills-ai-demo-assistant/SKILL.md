---
name: "rar-cat-agent-skills-ai-demo-assistant"
description: "Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo \u2014 fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_demo_assistant", "rar_sha256": "91fdd28e1096d53816d4397debef31b39e5539d37b57a29783db543dc51482d1", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ai_demo_assistant_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/ai-demo-assistant:0f816977b1c864ae3c648327c1aaa4dcc6a90c2b4c1c30d5207417f35ad68cd6", "kind": "skill"}, "version": "2.0.0", "author": "Doak Moore", "tags": ["demo", "copilot", "microsoft_365", "sales_enablement", "content", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/ai_demo_assistant`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ai_demo_assistant_agent.py` is
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

AI Demo Assistant — Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant
  Upstream author: Doak Moore
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_demo_assistant_agent.py` and embedded as the fenced Python below (sha256 91fdd28e1096d538…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_demo_assistant_agent.py` first:

```bash
python3 ai_demo_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_demo_assistant_agent.py   # or on stdin
python3 ai_demo_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AI Demo Assistant — Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant
  Upstream author: Doak Moore
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/ai_demo_assistant',
    "version": '2.0.0',
    "display_name": 'AI Demo Assistant',
    "description": 'Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.',
    "author": 'Doak Moore',
    "tags": ['demo', 'copilot', 'microsoft_365', 'sales_enablement', 'content', 'productivity'],
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
        "upstream_slug": 'ai-demo-assistant',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'c768346e949547d4',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AiDemoAssistant(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AiDemoAssistant'
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
    print(AiDemoAssistant().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
