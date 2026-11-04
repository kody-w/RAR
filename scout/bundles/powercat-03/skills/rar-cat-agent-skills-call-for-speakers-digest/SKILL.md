---
name: "rar-cat-agent-skills-call-for-speakers-digest"
description: "Weekly HTML email digest of open conference Call for Speakers (CFP) opportunities matching your topics of interest. Pulls from confs.tech, Papercall, AdatoSystems' CFP tracker, CFP Radar, Sessionize's public user-groups directory, community-specific hubs (like communitydays.org for the Microsoft ecosystem), targeted search of standalone Sessionize conferences and run.events, and general web searc\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/call_for_speakers_digest", "rar_sha256": "5ea0d443f429476b193cd018fdf370d484de2bd510263c087c133d8dc0146951", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Michael Heath", "tags": ["productivity", "speaking", "conference", "automation"]}
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
