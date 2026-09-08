---
name: "rar-cat-agent-skills-lab-column-mapper"
description: "When a health system's lab results ingestion pipeline hits an unknown column header, this skill semantically matches the source column against the canonical clinical schema (LOINC-anchored), scoped by lab and clinical domain, and writes a suggested mapping to a Dataverse review queue for a clinical informatics steward to approve."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lab_column_mapper", "rar_sha256": "914d0b5db16447f3e2a56c419e77f313284b3b6100129f4ee95beafda594537c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Rafsan Huseynov", "tags": ["healthcare", "clinical_data", "lab_results", "schema_drift", "column_mapping", "data_ingestion", "loinc", "azure_ai_search"]}
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
