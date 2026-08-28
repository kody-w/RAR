---
name: "rar-cowork-cookbook-find-the-deals-that-need-my-help"
description: "Know where your attention moves the number this week - and understand why each deal is stuck, not just that it is"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_the_deals_that_need_my_help", "rar_sha256": "ec6d291a1f54411dbcf7f2999c1bb7b9c0b2a22302c45e3d7a938d626976e8ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/find_the_deals_that_need_my_help`. The original RAPP
agent is preserved byte-for-byte in `find_the_deals_that_need_my_help_agent.py` and in the RCI capsule.

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

Find the deals that need my help — Know where your attention moves the number this week - and understand why each deal is stuck, not just that it is

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/find-the-deals-that-need-my-help
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_the_deals_that_need_my_help_agent.py` and embedded as the fenced Python below (sha256 ec6d291a1f54411d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_the_deals_that_need_my_help_agent.py` first:

```bash
python3 find_the_deals_that_need_my_help_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 find_the_deals_that_need_my_help_agent.py   # or on stdin
python3 find_the_deals_that_need_my_help_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Find the deals that need my help — Know where your attention moves the number this week - and understand why each deal is stuck, not just that it is

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/find-the-deals-that-need-my-help
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/find_the_deals_that_need_my_help',
    "version": '2.0.0',
    "display_name": 'Find the deals that need my help',
    "description": 'Know where your attention moves the number this week - and understand why each deal is stuck, not just that it is',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'find-the-deals-that-need-my-help',
        "upstream_url": 'https://coworkcookbook.com/recipes/find-the-deals-that-need-my-help',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6aa29ccde9bda727',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/find-the-deals-that-need-my-help', 'uses_skills': {'custom': [], 'ootb': ['Deep Research'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class FindTheDealsThatNeedMyHelp(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FindTheDealsThatNeedMyHelp'
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
    print(FindTheDealsThatNeedMyHelp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
