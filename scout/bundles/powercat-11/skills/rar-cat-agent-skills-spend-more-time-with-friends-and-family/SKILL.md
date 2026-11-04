---
name: "rar-cat-agent-skills-spend-more-time-with-friends-and-family"
description: "While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/spend_more_time_with_friends_and_family", "rar_sha256": "4743e9c8b7ee1fa73e987d108f61e04136cdc16eea4ee7d16d01fd4db0d6984d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["automation", "teams", "out_of_office", "knowledge"]}
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
