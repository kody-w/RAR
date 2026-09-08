---
name: "rar-cat-agent-skills-knowledge-source-router"
description: "Route country-specific SharePoint questions through Country metadata first, then search only the complete set of matching documents."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_source_router", "rar_sha256": "b8e2822507b13775fff2410fd66bb59f29f9c622a8d8e45b844f4fa235f54569", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "4.0.2", "author": "Adi Leibowitz", "tags": ["knowledge", "routing", "sharepoint", "metadata", "grounding"]}
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
