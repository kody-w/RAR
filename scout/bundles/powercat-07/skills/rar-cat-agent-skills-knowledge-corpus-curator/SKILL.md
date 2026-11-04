---
name: "rar-cat-agent-skills-knowledge-corpus-curator"
description: "Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_corpus_curator", "rar_sha256": "10ffef6ab60d115b4c4de25df5f583e6259ff262bdee6283a7524c223c70ebf1", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.8.2", "author": "Doug Bellingeri", "tags": ["knowledge", "sharepoint", "governance", "deduplication", "documents", "uploads", "excel"]}
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
