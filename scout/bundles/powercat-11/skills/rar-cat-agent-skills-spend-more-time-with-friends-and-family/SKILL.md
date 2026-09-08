---
name: "rar-cat-agent-skills-spend-more-time-with-friends-and-family"
description: "While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/spend_more_time_with_friends_and_family", "rar_sha256": "ae5c4e43c1e54091d9c0fba127f9b7f077a61289feb638570df2aaab146c313c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["automation", "teams", "out_of_office", "knowledge"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `spend_more_time_with_friends_and_family_agent.py` and embedded as the fenced Python below (sha256 ae5c4e43c1e54091…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `spend_more_time_with_friends_and_family_agent.py` first:

```bash
python3 spend_more_time_with_friends_and_family_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 spend_more_time_with_friends_and_family_agent.py   # or on stdin
python3 spend_more_time_with_friends_and_family_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
