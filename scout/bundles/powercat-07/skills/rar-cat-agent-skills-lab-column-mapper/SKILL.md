---
name: "rar-cat-agent-skills-lab-column-mapper"
description: "When a health system's lab results ingestion pipeline hits an unknown column header, this skill semantically matches the source column against the canonical clinical schema (LOINC-anchored), scoped by lab and clinical domain, and writes a suggested mapping to a Dataverse review queue for a clinical informatics steward to approve."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lab_column_mapper", "rar_sha256": "5589a92823bbb860000ebb088852972236b3df0668bbe743601f90be85ce0aa1", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "lab_column_mapper_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/lab-column-mapper:b32169e5735f3ec5e0740dabdd4e7555b265c00cb6b07ac0a5ebbcc9514824ef", "kind": "skill"}, "version": "2.0.0", "author": "Rafsan Huseynov", "tags": ["healthcare", "clinical_data", "lab_results", "schema_drift", "column_mapping", "data_ingestion", "loinc", "azure_ai_search"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/lab_column_mapper`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `lab_column_mapper_agent.py` is
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
