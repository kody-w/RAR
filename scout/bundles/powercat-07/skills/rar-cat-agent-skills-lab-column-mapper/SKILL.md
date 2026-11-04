---
name: "rar-cat-agent-skills-lab-column-mapper"
description: "When a health system's lab results ingestion pipeline hits an unknown column header, this skill semantically matches the source column against the canonical clinical schema (LOINC-anchored), scoped by lab and clinical domain, and writes a suggested mapping to a Dataverse review queue for a clinical informatics steward to approve."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lab_column_mapper", "rar_sha256": "0287bd0110c25b87219dd922e473ed65e8c5fec0e6ef39071b21a2d0aa8239d7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Rafsan Huseynov", "tags": ["healthcare", "clinical_data", "lab_results", "schema_drift", "column_mapping", "data_ingestion", "loinc", "azure_ai_search"]}
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
