---
name: "rar-cowork-cookbook-build-an-account-research-brief"
description: "Walk into account planning already knowing the shape of the opportunity - pipeline, stakeholders, recent activity, and where the deal sits - without piecing it together from CRM tabs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_an_account_research_brief", "rar_sha256": "c036d4756a162d331d7970debcf65dbba22e12b18c2c2393f106adebf50deb24", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_an_account_research_brief_agent.py` and embedded as the fenced Python below (sha256 c036d4756a162d33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_an_account_research_brief_agent.py` first:

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
    "version": '2.0.1',
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
