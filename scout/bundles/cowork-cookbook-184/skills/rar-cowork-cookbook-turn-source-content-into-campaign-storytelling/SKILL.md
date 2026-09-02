---
name: "rar-cowork-cookbook-turn-source-content-into-campaign-storytelling"
description: "Move from raw inputs - a research debrief transcript, customer interview, or campaign brief - to a polished storytelling deck, with iteration built into the flow instead of bolted on after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_source_content_into_campaign_storytelling", "rar_sha256": "318091cac6ddecd9c2edec0b506684ff26b988ab29b2746aa7b6999738c29b19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "turn_source_content_into_campaign_storytelling_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/turn-source-content-into-campaign-storytelling:7f1d11b146ea19a432d3f3e432f0312427c5e1fbd672206afea9ae2809ddc824", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "integration", "prezi"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/turn_source_content_into_campaign_storytelling`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `turn_source_content_into_campaign_storytelling_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
