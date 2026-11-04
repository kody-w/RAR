---
name: "rar-cat-agent-skills-copilot-agents-news-scout"
description: "A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agents_news_scout", "rar_sha256": "0121f58ca0194995eceb2c1c014371e45312be27668c438506c656cc63bd9d96", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Elliot Margot", "tags": ["news", "copilot", "agent", "digest", "automation", "weekly", "teams"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_agents_news_scout_agent.py` and embedded as the fenced Python below (sha256 0121f58ca0194995…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_agents_news_scout_agent.py` first:

```bash
python3 copilot_agents_news_scout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_agents_news_scout_agent.py   # or on stdin
python3 copilot_agents_news_scout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_agents_news_scout_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_agents_news_scout_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_agents_news_scout/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
