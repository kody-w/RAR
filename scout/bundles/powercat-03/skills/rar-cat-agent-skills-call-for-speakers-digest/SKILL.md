---
name: "rar-cat-agent-skills-call-for-speakers-digest"
description: "Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/call_for_speakers_digest", "rar_sha256": "d0d10eab87e4ada8b21db20e33224b2e3b97d5c23eac20300aa8864d64ea5d98", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Michael Heath", "tags": ["productivity", "speaking", "conference", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/call_for_speakers_digest`. The original RAPP
agent is preserved byte-for-byte in `call_for_speakers_digest_agent.py` and in the RCI capsule.

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

Call for Speakers Digest — Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#call-for-speakers-digest
  Upstream author: Michael Heath
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `call_for_speakers_digest_agent.py` and embedded as the fenced Python below (sha256 d0d10eab87e4ada8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `call_for_speakers_digest_agent.py` first:

```bash
python3 call_for_speakers_digest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 call_for_speakers_digest_agent.py   # or on stdin
python3 call_for_speakers_digest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Call for Speakers Digest — Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#call-for-speakers-digest
  Upstream author: Michael Heath
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/call_for_speakers_digest',
    "version": '3.0.2',
    "display_name": 'Call for Speakers Digest',
    "description": "Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc…",
    "author": 'Michael Heath',
    "tags": ['productivity', 'speaking', 'conference', 'automation'],
    "category": 'general',
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
        "upstream_slug": 'call-for-speakers-digest',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#call-for-speakers-digest',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd964e313b2ca6981',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Scout', 'Cowork'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class CallForSpeakersDigest(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CallForSpeakersDigest'
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
    print(CallForSpeakersDigest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
