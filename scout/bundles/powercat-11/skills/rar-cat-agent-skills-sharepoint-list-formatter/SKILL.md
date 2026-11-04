---
name: "rar-cat-agent-skills-sharepoint-list-formatter"
description: "Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_formatter", "rar_sha256": "8d46667639bcef5592415180941620139a0b843fe27c8f605456fb68a5316ced", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["sharepoint", "microsoft_365", "productivity", "tables", "data"]}
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
