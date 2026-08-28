---
name: "rar-cowork-cookbook-turn-source-content-into-campaign-storytelling"
description: "Move from raw inputs - a research debrief transcript, customer interview, or campaign brief - to a polished storytelling deck, with iteration built into the flow instead of bolted on after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_source_content_into_campaign_storytelling", "rar_sha256": "318091cac6ddecd9c2edec0b506684ff26b988ab29b2746aa7b6999738c29b19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "integration", "prezi"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/turn_source_content_into_campaign_storytelling`. The original RAPP
agent is preserved byte-for-byte in `turn_source_content_into_campaign_storytelling_agent.py` and in the RCI capsule.

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

Turn source content into a campaign storytelling deck — Move from raw inputs - a research debrief transcript, customer interview, or campaign brief - to a polished storytelling deck, with iteration built into the flow instead of bolted on after.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/turn-source-content-into-campaign-storytelling
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_source_content_into_campaign_storytelling_agent.py` and embedded as the fenced Python below (sha256 318091cac6ddecd9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_source_content_into_campaign_storytelling_agent.py` first:

```bash
python3 turn_source_content_into_campaign_storytelling_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_source_content_into_campaign_storytelling_agent.py   # or on stdin
python3 turn_source_content_into_campaign_storytelling_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn source content into a campaign storytelling deck — Move from raw inputs - a research debrief transcript, customer interview, or campaign brief - to a polished storytelling deck, with iteration built into the flow instead of bolted on after.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/turn-source-content-into-campaign-storytelling
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/turn_source_content_into_campaign_storytelling',
    "version": '2.0.0',
    "display_name": 'Turn source content into a campaign storytelling deck',
    "description": 'Move from raw inputs - a research debrief transcript, customer interview, or campaign brief - to a polished storytelling deck, with iteration built into the flow instead of bolted on after.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'beginner', 'integration', 'prezi'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'turn-source-content-into-campaign-storytelling',
        "upstream_url": 'https://coworkcookbook.com/recipes/turn-source-content-into-campaign-storytelling',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '62562f802e94aea9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'prezi', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/turn-source-content-into-campaign-storytelling', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.4, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TurnSourceContentIntoCampaignStorytelling(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnSourceContentIntoCampaignStorytelling'
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(TurnSourceContentIntoCampaignStorytelling().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
