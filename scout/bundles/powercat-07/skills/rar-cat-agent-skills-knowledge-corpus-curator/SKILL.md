---
name: "rar-cat-agent-skills-knowledge-corpus-curator"
description: "Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_corpus_curator", "rar_sha256": "0c3aead2f0ab4312a0b116210443d47034268810152022a21ef72612b84c7fa6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.8.2", "author": "Doug Bellingeri", "tags": ["knowledge", "sharepoint", "governance", "deduplication", "documents", "uploads", "excel"]}
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
