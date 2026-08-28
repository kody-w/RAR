---
name: "rar-cowork-cookbook-campaign-kick-off"
description: "Stand up a new campaign with a working brief, prior campaign learnings baked in, the right stakeholders, and a kickoff already on the calendar."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/campaign_kick_off", "rar_sha256": "1a469eb7f0489ec10426703a471e94a6289a3aac5afc43f404fe259ca1b540d0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/campaign_kick_off`. The original RAPP
agent is preserved byte-for-byte in `campaign_kick_off_agent.py` and in the RCI capsule.

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

Campaign kick-off — Stand up a new campaign with a working brief, prior campaign learnings baked in, the right stakeholders, and a kickoff already on the calendar.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/campaign-kick-off
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_kick_off_agent.py` and embedded as the fenced Python below (sha256 1a469eb7f0489ec1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_kick_off_agent.py` first:

```bash
python3 campaign_kick_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 campaign_kick_off_agent.py   # or on stdin
python3 campaign_kick_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Campaign kick-off — Stand up a new campaign with a working brief, prior campaign learnings baked in, the right stakeholders, and a kickoff already on the calendar.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/campaign-kick-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/campaign_kick_off',
    "version": '2.0.1',
    "display_name": 'Campaign kick-off',
    "description": 'Stand up a new campaign with a working brief, prior campaign learnings baked in, the right stakeholders, and a kickoff already on the calendar.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'campaign-kick-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/campaign-kick-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bb969e010382f106',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/identify-campaign-audiences'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/campaign-kick-off', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Calendar Management', 'Scheduling', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class CampaignKickOff(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CampaignKickOff'
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
    print(CampaignKickOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
