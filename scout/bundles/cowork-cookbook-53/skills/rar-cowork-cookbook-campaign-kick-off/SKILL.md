---
name: "rar-cowork-cookbook-campaign-kick-off"
description: "Stand up a new campaign with a working brief, prior campaign learnings baked in, the right stakeholders, and a kickoff already on the calendar."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/campaign_kick_off", "rar_sha256": "402bed53c415c523236e38953678ae94faf302ede36bef716f44dbd8d844511e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "campaign_kick_off_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/campaign-kick-off:fd2033aafd68728d3f023b7621dfe71daf835877af1c2221a16281ad7e6b3c1d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/campaign_kick_off`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `campaign_kick_off_agent.py` is
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
