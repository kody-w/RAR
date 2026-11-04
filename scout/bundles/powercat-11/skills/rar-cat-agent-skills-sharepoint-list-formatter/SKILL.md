---
name: "rar-cat-agent-skills-sharepoint-list-formatter"
description: "Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_formatter", "rar_sha256": "8d46667639bcef5592415180941620139a0b843fe27c8f605456fb68a5316ced", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["sharepoint", "microsoft_365", "productivity", "tables", "data"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/sharepoint_list_formatter`. The original RAPP
agent is preserved byte-for-byte in `sharepoint_list_formatter_agent.py` and in the RCI capsule.

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

SharePoint List Formatter — Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter
  Upstream author: Mathias Salomonsen
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_list_formatter_agent.py` and embedded as the fenced Python below (sha256 8d46667639bcef55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_list_formatter_agent.py` first:

```bash
python3 sharepoint_list_formatter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_list_formatter_agent.py   # or on stdin
python3 sharepoint_list_formatter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/sharepoint_list_formatter_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/sharepoint_list_formatter_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/sharepoint_list_formatter/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
SharePoint List Formatter — Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter
  Upstream author: Mathias Salomonsen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/sharepoint_list_formatter',
    "version": '3.0.2',
    "display_name": 'SharePoint List Formatter',
    "description": 'Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.',
    "author": 'Mathias Salomonsen',
    "tags": ['sharepoint', 'microsoft_365', 'productivity', 'tables', 'data'],
    "category": 'pipeline',
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
        "upstream_slug": 'sharepoint-list-formatter',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '081ee2e4c6d01a36',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.667, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:data'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class SharepointListFormatter(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SharepointListFormatter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(SharepointListFormatter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
