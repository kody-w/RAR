---
name: "rar-cat-agent-skills-copilot-agents-news-scout"
description: "A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agents_news_scout", "rar_sha256": "9d45dca1f4eeae058b0f07c698721c49a4bc3bb408dbbc74401899aef8225a40", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Elliot Margot", "tags": ["news", "copilot", "agent", "digest", "automation", "weekly", "teams"]}
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
