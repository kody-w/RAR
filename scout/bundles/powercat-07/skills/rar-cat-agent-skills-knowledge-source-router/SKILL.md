---
name: "rar-cat-agent-skills-knowledge-source-router"
description: "Route country-specific SharePoint questions through Country metadata first, then search only the complete set of matching documents."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_source_router", "rar_sha256": "28de060ce9e856846c1ed608ec2cee0367fb8584d3b8b16ad583db18d97fe305", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "4.0.2", "author": "Adi Leibowitz", "tags": ["knowledge", "routing", "sharepoint", "metadata", "grounding"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `knowledge_source_router_agent.py` and embedded as the fenced Python below (sha256 28de060ce9e85684…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `knowledge_source_router_agent.py` first:

```bash
python3 knowledge_source_router_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 knowledge_source_router_agent.py   # or on stdin
python3 knowledge_source_router_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/knowledge_source_router_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/knowledge_source_router_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/knowledge_source_router/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
