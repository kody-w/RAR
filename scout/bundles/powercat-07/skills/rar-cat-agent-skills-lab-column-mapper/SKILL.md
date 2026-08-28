---
name: "rar-cat-agent-skills-lab-column-mapper"
description: "When a health system's lab results ingestion pipeline hits an unknown column header, this skill semantically matches the source column against the canonical clinical schema (LOINC-anchored), scoped by lab and clinical domain, and writes a suggested mapping to a Dataverse review queue for a clinical informatics steward to approve."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lab_column_mapper", "rar_sha256": "5589a92823bbb860000ebb088852972236b3df0668bbe743601f90be85ce0aa1", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Rafsan Huseynov", "tags": ["healthcare", "clinical_data", "lab_results", "schema_drift", "column_mapping", "data_ingestion", "loinc", "azure_ai_search"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/lab_column_mapper`. The original RAPP
agent is preserved byte-for-byte in `lab_column_mapper_agent.py` and in the RCI capsule.

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

Lab Column Mapper — When a health system's lab results ingestion pipeline hits an unknown column header, this skill semantically matches the source column against the canonical clinical schema (LOINC-anchored), scoped by lab and clinical domain, and writes a suggested mapping to a Dataverse review queue for a clinical informatics steward to approve.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#lab-column-mapper
  Upstream author: Rafsan Huseynov
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lab_column_mapper_agent.py` and embedded as the fenced Python below (sha256 5589a92823bbb860…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lab_column_mapper_agent.py` first:

```bash
python3 lab_column_mapper_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lab_column_mapper_agent.py   # or on stdin
python3 lab_column_mapper_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lab Column Mapper — When a health system's lab results ingestion pipeline hits an unknown column header, this skill semantically matches the source column against the canonical clinical schema (LOINC-anchored), scoped by lab and clinical domain, and writes a suggested mapping to a Dataverse review queue for a clinical informatics steward to approve.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#lab-column-mapper
  Upstream author: Rafsan Huseynov
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/lab_column_mapper',
    "version": '2.0.0',
    "display_name": 'Lab Column Mapper',
    "description": "When a health system's lab results ingestion pipeline hits an unknown column header, this skill semantically matches the source column against the canonical clinical schema (LOINC-anchored), scoped by lab and clinical domain, and writes a suggested mapping to a Dataverse review queue for a clinical informatics steward to approve.",
    "author": 'Rafsan Huseynov',
    "tags": ['healthcare', 'clinical_data', 'lab_results', 'schema_drift', 'column_mapping', 'data_ingestion', 'loinc', 'azure_ai_search'],
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
        "upstream_slug": 'lab-column-mapper',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#lab-column-mapper',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'a5d0633999e8c453',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.667, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['word:against', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class LabColumnMapper(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LabColumnMapper'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(LabColumnMapper().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
