---
name: "rar-cat-agent-skills-lab-column-mapper"
description: "When a health system's lab results ingestion pipeline hits an unknown column header, this skill semantically matches the source column against the canonical clinical schema (LOINC-anchored), scoped by lab and clinical domain, and writes a suggested mapping to a Dataverse review queue for a clinical informatics steward to approve."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lab_column_mapper", "rar_sha256": "0287bd0110c25b87219dd922e473ed65e8c5fec0e6ef39071b21a2d0aa8239d7", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Rafsan Huseynov", "tags": ["healthcare", "clinical_data", "lab_results", "schema_drift", "column_mapping", "data_ingestion", "loinc", "azure_ai_search"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lab_column_mapper_agent.py` and embedded as the fenced Python below (sha256 0287bd0110c25b87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lab_column_mapper_agent.py` first:

```bash
python3 lab_column_mapper_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lab_column_mapper_agent.py   # or on stdin
python3 lab_column_mapper_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/lab_column_mapper_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/lab_column_mapper_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/lab_column_mapper/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
