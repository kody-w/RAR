---
name: "rar-cat-agent-skills-sharepoint-list-formatter"
description: "Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_formatter", "rar_sha256": "8ce15990887997b95ee23d598dab87d7f22a644e38e5dd49d089571a201564f2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "sharepoint_list_formatter_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/sharepoint-list-formatter:08cb0bad36d8f48d74f7c3c5fd651854f55a878317c1bafe17449803e39bfcb3", "kind": "skill"}, "version": "2.0.0", "author": "Mathias Salomonsen", "tags": ["sharepoint", "microsoft_365", "productivity", "tables", "data"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/sharepoint_list_formatter`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `sharepoint_list_formatter_agent.py` is
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

SharePoint List Formatter — Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter
  Upstream author: Mathias Salomonsen
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_list_formatter_agent.py` and embedded as the fenced Python below (sha256 8ce15990887997b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_list_formatter_agent.py` first:

```bash
python3 sharepoint_list_formatter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_list_formatter_agent.py   # or on stdin
python3 sharepoint_list_formatter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
SharePoint List Formatter — Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter
  Upstream author: Mathias Salomonsen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/sharepoint_list_formatter',
    "version": '2.0.0',
    "display_name": 'SharePoint List Formatter',
    "description": 'Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.',
    "author": 'Mathias Salomonsen',
    "tags": ['sharepoint', 'microsoft_365', 'productivity', 'tables', 'data'],
    "category": 'pipeline',
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
        "upstream_slug": 'sharepoint-list-formatter',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '081ee2e4c6d01a36',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.667, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:data'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class SharepointListFormatter(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SharepointListFormatter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(SharepointListFormatter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
