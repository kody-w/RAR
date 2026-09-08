---
name: "rar-cat-agent-skills-knowledge-source-router"
description: "Route country-specific SharePoint questions through Country metadata first, then search only the complete set of matching documents."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_source_router", "rar_sha256": "b8e2822507b13775fff2410fd66bb59f29f9c622a8d8e45b844f4fa235f54569", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "4.0.2", "author": "Adi Leibowitz", "tags": ["knowledge", "routing", "sharepoint", "metadata", "grounding"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/knowledge_source_router`. The original RAPP
agent is preserved byte-for-byte in `knowledge_source_router_agent.py` and in the RCI capsule.

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

Knowledge Source Router — Route country-specific SharePoint questions through Country metadata first, then search only the complete set of matching documents.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-source-router
  Upstream author: Adi Leibowitz
  Upstream version: 2.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `knowledge_source_router_agent.py` and embedded as the fenced Python below (sha256 b8e2822507b13775…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `knowledge_source_router_agent.py` first:

```bash
python3 knowledge_source_router_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 knowledge_source_router_agent.py   # or on stdin
python3 knowledge_source_router_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Knowledge Source Router — Route country-specific SharePoint questions through Country metadata first, then search only the complete set of matching documents.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-source-router
  Upstream author: Adi Leibowitz
  Upstream version: 2.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/knowledge_source_router',
    "version": '4.0.2',
    "display_name": 'Knowledge Source Router',
    "description": 'Route country-specific SharePoint questions through Country metadata first, then search only the complete set of matching documents.',
    "author": 'Adi Leibowitz',
    "tags": ['knowledge', 'routing', 'sharepoint', 'metadata', 'grounding'],
    "category": 'integrations',
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
        "upstream_slug": 'knowledge-source-router',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#knowledge-source-router',
        "upstream_version": '2.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '222db16ad4565ae2',
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class KnowledgeSourceRouter(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'KnowledgeSourceRouter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(KnowledgeSourceRouter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
