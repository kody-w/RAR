---
name: "rar-cat-agent-skills-knowledge-corpus-curator"
description: "Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_corpus_curator", "rar_sha256": "0c3aead2f0ab4312a0b116210443d47034268810152022a21ef72612b84c7fa6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.8.2", "author": "Doug Bellingeri", "tags": ["knowledge", "sharepoint", "governance", "deduplication", "documents", "uploads", "excel"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/knowledge_corpus_curator`. The original RAPP
agent is preserved byte-for-byte in `knowledge_corpus_curator_agent.py` and in the RCI capsule.

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

Knowledge Corpus Curator — Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-corpus-curator
  Upstream author: Doug Bellingeri
  Upstream version: 0.8.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `knowledge_corpus_curator_agent.py` and embedded as the fenced Python below (sha256 0c3aead2f0ab4312…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `knowledge_corpus_curator_agent.py` first:

```bash
python3 knowledge_corpus_curator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 knowledge_corpus_curator_agent.py   # or on stdin
python3 knowledge_corpus_curator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Knowledge Corpus Curator — Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-corpus-curator
  Upstream author: Doug Bellingeri
  Upstream version: 0.8.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/knowledge_corpus_curator',
    "version": '2.8.2',
    "display_name": 'Knowledge Corpus Curator',
    "description": 'Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog.',
    "author": 'Doug Bellingeri',
    "tags": ['knowledge', 'sharepoint', 'governance', 'deduplication', 'documents', 'uploads', 'excel'],
    "category": 'productivity',
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
        "upstream_slug": 'knowledge-corpus-curator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#knowledge-corpus-curator',
        "upstream_version": '0.8.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '44b7b1e672580b5c',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class KnowledgeCorpusCurator(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'KnowledgeCorpusCurator'
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
    print(KnowledgeCorpusCurator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
