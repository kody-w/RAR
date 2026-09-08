---
name: "rar-cat-agent-skills-lab-column-mapper"
description: "When a health system's lab results ingestion pipeline hits an unknown column header, this skill semantically matches the source column against the canonical clinical schema (LOINC-anchored), scoped by lab and clinical domain, and writes a suggested mapping to a Dataverse review queue for a clinical informatics steward to approve."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lab_column_mapper", "rar_sha256": "914d0b5db16447f3e2a56c419e77f313284b3b6100129f4ee95beafda594537c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Rafsan Huseynov", "tags": ["healthcare", "clinical_data", "lab_results", "schema_drift", "column_mapping", "data_ingestion", "loinc", "azure_ai_search"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lab_column_mapper_agent.py` and embedded as the fenced Python below (sha256 914d0b5db16447f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lab_column_mapper_agent.py` first:

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
    "version": '3.0.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
