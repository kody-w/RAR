---
name: "rar-cat-agent-skills-vacation-urgent-forwarder"
description: "A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vacation_urgent_forwarder", "rar_sha256": "c4a04ec663c7617f56de6dfe01f5dff6d5ee25a69d631c6e6d25f66d513f1024", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Giorgio Ughini", "tags": ["automation", "email", "teams", "out_of_office"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/vacation_urgent_forwarder`. The original RAPP
agent is preserved byte-for-byte in `vacation_urgent_forwarder_agent.py` and in the RCI capsule.

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

Vacation Urgent Forwarder — A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder
  Upstream author: Giorgio Ughini
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vacation_urgent_forwarder_agent.py` and embedded as the fenced Python below (sha256 c4a04ec663c7617f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vacation_urgent_forwarder_agent.py` first:

```bash
python3 vacation_urgent_forwarder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vacation_urgent_forwarder_agent.py   # or on stdin
python3 vacation_urgent_forwarder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/vacation_urgent_forwarder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/vacation_urgent_forwarder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/vacation_urgent_forwarder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Vacation Urgent Forwarder — A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder
  Upstream author: Giorgio Ughini
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/vacation_urgent_forwarder',
    "version": '3.0.2',
    "display_name": 'Vacation Urgent Forwarder',
    "description": 'A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.',
    "author": 'Giorgio Ughini',
    "tags": ['automation', 'email', 'teams', 'out_of_office'],
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
        "upstream_slug": 'vacation-urgent-forwarder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'e2fd9f42fce2d9e9',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.636, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class VacationUrgentForwarder(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VacationUrgentForwarder'
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
    print(VacationUrgentForwarder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
