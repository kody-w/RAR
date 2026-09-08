---
name: "rar-cat-agent-skills-copilot-agents-news-scout"
description: "A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agents_news_scout", "rar_sha256": "9d45dca1f4eeae058b0f07c698721c49a4bc3bb408dbbc74401899aef8225a40", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Elliot Margot", "tags": ["news", "copilot", "agent", "digest", "automation", "weekly", "teams"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_agents_news_scout`. The original RAPP
agent is preserved byte-for-byte in `copilot_agents_news_scout_agent.py` and in the RCI capsule.

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

Copilot & Agents News Scout — A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-agents-news-scout
  Upstream author: Elliot Margot
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_agents_news_scout_agent.py` and embedded as the fenced Python below (sha256 9d45dca1f4eeae05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_agents_news_scout_agent.py` first:

```bash
python3 copilot_agents_news_scout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_agents_news_scout_agent.py   # or on stdin
python3 copilot_agents_news_scout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot & Agents News Scout — A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-agents-news-scout
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_agents_news_scout',
    "version": '3.0.2',
    "display_name": 'Copilot & Agents News Scout',
    "description": "A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams.",
    "author": 'Elliot Margot',
    "tags": ['news', 'copilot', 'agent', 'digest', 'automation', 'weekly', 'teams'],
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
        "upstream_slug": 'copilot-agents-news-scout',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-agents-news-scout',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'fc3502443ed8b977',
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


class CopilotAgentsNewsScout(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotAgentsNewsScout'
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
    print(CopilotAgentsNewsScout().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
