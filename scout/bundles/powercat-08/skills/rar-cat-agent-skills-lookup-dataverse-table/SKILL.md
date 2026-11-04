---
name: "rar-cat-agent-skills-lookup-dataverse-table"
description: "Search any Microsoft Dataverse table, browse matching records, and drill into full record details \u2014 sourced live via the Dataverse MCP Server."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/lookup_dataverse_table", "rar_sha256": "8b0277b43675440ff607ba85c746d410d864d62ddc5682363f111737c00be4c4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Chris Garty", "tags": ["dataverse", "mcp", "data_lookup", "power_platform", "crm"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/lookup_dataverse_table`. The original RAPP
agent is preserved byte-for-byte in `lookup_dataverse_table_agent.py` and in the RCI capsule.

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

Dataverse Table Lookup — Search any Microsoft Dataverse table, browse matching records, and drill into full record details — sourced live via the Dataverse MCP Server.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#lookup-dataverse-table
  Upstream author: Chris Garty
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lookup_dataverse_table_agent.py` and embedded as the fenced Python below (sha256 8b0277b43675440f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lookup_dataverse_table_agent.py` first:

```bash
python3 lookup_dataverse_table_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lookup_dataverse_table_agent.py   # or on stdin
python3 lookup_dataverse_table_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/lookup_dataverse_table_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/lookup_dataverse_table_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/lookup_dataverse_table/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Dataverse Table Lookup — Search any Microsoft Dataverse table, browse matching records, and drill into full record details — sourced live via the Dataverse MCP Server.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#lookup-dataverse-table
  Upstream author: Chris Garty
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/lookup_dataverse_table',
    "version": '3.0.2',
    "display_name": 'Dataverse Table Lookup',
    "description": 'Search any Microsoft Dataverse table, browse matching records, and drill into full record details — sourced live via the Dataverse MCP Server.',
    "author": 'Chris Garty',
    "tags": ['dataverse', 'mcp', 'data_lookup', 'power_platform', 'crm'],
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
        "upstream_slug": 'lookup-dataverse-table',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#lookup-dataverse-table',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '9a79dc859cb36791',
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:mcp'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class LookupDataverseTable(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LookupDataverseTable'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(LookupDataverseTable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
