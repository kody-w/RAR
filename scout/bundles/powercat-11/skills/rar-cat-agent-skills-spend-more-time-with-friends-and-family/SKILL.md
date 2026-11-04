---
name: "rar-cat-agent-skills-spend-more-time-with-friends-and-family"
description: "While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/spend_more_time_with_friends_and_family", "rar_sha256": "4743e9c8b7ee1fa73e987d108f61e04136cdc16eea4ee7d16d01fd4db0d6984d", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["automation", "teams", "out_of_office", "knowledge"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/spend_more_time_with_friends_and_family`. The original RAPP
agent is preserved byte-for-byte in `spend_more_time_with_friends_and_family_agent.py` and in the RCI capsule.

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

Spend More Time With Friends & Family — While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family
  Upstream author: Adi Leibowitz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `spend_more_time_with_friends_and_family_agent.py` and embedded as the fenced Python below (sha256 4743e9c8b7ee1fa7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `spend_more_time_with_friends_and_family_agent.py` first:

```bash
python3 spend_more_time_with_friends_and_family_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 spend_more_time_with_friends_and_family_agent.py   # or on stdin
python3 spend_more_time_with_friends_and_family_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/spend_more_time_with_friends_and_family_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/spend_more_time_with_friends_and_family_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/spend_more_time_with_friends_and_family/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Spend More Time With Friends & Family — While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/spend_more_time_with_friends_and_family',
    "version": '3.0.2',
    "display_name": 'Spend More Time With Friends & Family',
    "description": "While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.",
    "author": 'Adi Leibowitz',
    "tags": ['automation', 'teams', 'out_of_office', 'knowledge'],
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
        "upstream_slug": 'spend-more-time-with-friends-and-family',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'bd12abb4ba09a5e5',
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class SpendMoreTimeWithFriendsAndFamily(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SpendMoreTimeWithFriendsAndFamily'
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
    print(SpendMoreTimeWithFriendsAndFamily().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
