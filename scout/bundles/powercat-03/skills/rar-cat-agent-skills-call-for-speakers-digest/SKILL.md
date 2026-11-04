---
name: "rar-cat-agent-skills-call-for-speakers-digest"
description: "Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/call_for_speakers_digest", "rar_sha256": "5ea0d443f429476b193cd018fdf370d484de2bd510263c087c133d8dc0146951", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Michael Heath", "tags": ["productivity", "speaking", "conference", "automation"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `call_for_speakers_digest_agent.py` and embedded as the fenced Python below (sha256 5ea0d443f429476b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `call_for_speakers_digest_agent.py` first:

```bash
python3 call_for_speakers_digest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 call_for_speakers_digest_agent.py   # or on stdin
python3 call_for_speakers_digest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/call_for_speakers_digest_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/call_for_speakers_digest_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/call_for_speakers_digest/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
