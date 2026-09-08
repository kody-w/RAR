---
name: "rar-cat-agent-skills-call-for-speakers-digest"
description: "Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/call_for_speakers_digest", "rar_sha256": "d0d10eab87e4ada8b21db20e33224b2e3b97d5c23eac20300aa8864d64ea5d98", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Michael Heath", "tags": ["productivity", "speaking", "conference", "automation"]}
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
