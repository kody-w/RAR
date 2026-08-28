---
name: "rar-cowork-cookbook-build-an-account-research-brief"
description: "Walk into account planning already knowing the shape of the opportunity - pipeline, stakeholders, recent activity, and where the deal sits - without piecing it together from CRM tabs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_an_account_research_brief", "rar_sha256": "203f228ed329756df46b97b2041763fdb0b20a46ff362a905e37b8d4194bfd9e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_an_account_research_brief`. The original RAPP
agent is preserved byte-for-byte in `build_an_account_research_brief_agent.py` and in the RCI capsule.

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
