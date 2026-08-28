---
name: "rar-cowork-cookbook-find-the-deals-that-need-my-help"
description: "Know where your attention moves the number this week - and understand why each deal is stuck, not just that it is"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_the_deals_that_need_my_help", "rar_sha256": "c5bfde1ed2d34e225df98a5c7b76d77100c276b55ed1bcb5295303cd53b35a97", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_the_deals_that_need_my_help_agent.py` and embedded as the fenced Python below (sha256 c5bfde1ed2d34e22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_the_deals_that_need_my_help_agent.py` first:

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
    "version": '2.0.1',
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
