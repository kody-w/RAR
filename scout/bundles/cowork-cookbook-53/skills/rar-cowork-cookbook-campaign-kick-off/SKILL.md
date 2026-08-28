---
name: "rar-cowork-cookbook-campaign-kick-off"
description: "Stand up a new campaign with a working brief, prior campaign learnings baked in, the right stakeholders, and a kickoff already on the calendar."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/campaign_kick_off", "rar_sha256": "402bed53c415c523236e38953678ae94faf302ede36bef716f44dbd8d844511e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "fabric_iq"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_kick_off_agent.py` and embedded as the fenced Python below (sha256 402bed53c415c523…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_kick_off_agent.py` first:

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
    "version": '2.0.0',
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
