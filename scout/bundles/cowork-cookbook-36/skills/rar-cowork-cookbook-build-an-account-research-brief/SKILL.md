---
name: "rar-cowork-cookbook-build-an-account-research-brief"
description: "Walk into account planning already knowing the shape of the opportunity - pipeline, stakeholders, recent activity, and where the deal sits - without piecing it together from CRM tabs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_an_account_research_brief", "rar_sha256": "203f228ed329756df46b97b2041763fdb0b20a46ff362a905e37b8d4194bfd9e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "build_an_account_research_brief_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/build-an-account-research-brief:6df3cbfa42cda79d64e08dcc46fca5a99c8d0c7080191e63f5e53e19340f6bda", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/build_an_account_research_brief`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `build_an_account_research_brief_agent.py` is
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

Build an account research brief — Walk into account planning already knowing the shape of the opportunity - pipeline, stakeholders, recent activity, and where the deal sits - without piecing it together from CRM tabs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-an-account-research-brief
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_an_account_research_brief_agent.py` and embedded as the fenced Python below (sha256 203f228ed329756d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_an_account_research_brief_agent.py` first:

```bash
python3 build_an_account_research_brief_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_an_account_research_brief_agent.py   # or on stdin
python3 build_an_account_research_brief_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build an account research brief — Walk into account planning already knowing the shape of the opportunity - pipeline, stakeholders, recent activity, and where the deal sits - without piecing it together from CRM tabs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-an-account-research-brief
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_an_account_research_brief',
    "version": '2.0.0',
    "display_name": 'Build an account research brief',
    "description": 'Walk into account planning already knowing the shape of the opportunity - pipeline, stakeholders, recent activity, and where the deal sits - without piecing it together from CRM tabs.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'build-an-account-research-brief',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-an-account-research-brief',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '23c9fa073f79f483',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/build-an-account-research-brief', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.625, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'word:pipeline'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BuildAnAccountResearchBrief(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildAnAccountResearchBrief'
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
    print(BuildAnAccountResearchBrief().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
