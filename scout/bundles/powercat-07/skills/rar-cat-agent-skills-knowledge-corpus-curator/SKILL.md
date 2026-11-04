---
name: "rar-cat-agent-skills-knowledge-corpus-curator"
description: "Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_corpus_curator", "rar_sha256": "10ffef6ab60d115b4c4de25df5f583e6259ff262bdee6283a7524c223c70ebf1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.8.2", "author": "Doug Bellingeri", "tags": ["knowledge", "sharepoint", "governance", "deduplication", "documents", "uploads", "excel"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `knowledge_corpus_curator_agent.py` and embedded as the fenced Python below (sha256 10ffef6ab60d115b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `knowledge_corpus_curator_agent.py` first:

```bash
python3 knowledge_corpus_curator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 knowledge_corpus_curator_agent.py   # or on stdin
python3 knowledge_corpus_curator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/knowledge_corpus_curator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/knowledge_corpus_curator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/knowledge_corpus_curator/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
