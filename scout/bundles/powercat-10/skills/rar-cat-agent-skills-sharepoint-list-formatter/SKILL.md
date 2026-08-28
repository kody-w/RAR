---
name: "rar-cat-agent-skills-sharepoint-list-formatter"
description: "Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_formatter", "rar_sha256": "8ce15990887997b95ee23d598dab87d7f22a644e38e5dd49d089571a201564f2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Mathias Salomonsen", "tags": ["sharepoint", "microsoft_365", "productivity", "tables", "data"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/sharepoint_list_formatter`. The original RAPP
agent is preserved byte-for-byte in `sharepoint_list_formatter_agent.py` and in the RCI capsule.

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
