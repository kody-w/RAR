---
name: "rar-cowork-cookbook-new-customer-onboarding-automation"
description: "Close a new customer and trigger the full onboarding sequence in one prompt."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/new_customer_onboarding_automation", "rar_sha256": "527ace04654f2b2778dbb8147853d3c79e0e9fcd031fc644dfd4db17d0c3e170", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/new_customer_onboarding_automation`. The original RAPP
agent is preserved byte-for-byte in `new_customer_onboarding_automation_agent.py` and in the RCI capsule.

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

New customer onboarding automation — Close a new customer and trigger the full onboarding sequence in one prompt.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/new-customer-onboarding-automation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `new_customer_onboarding_automation_agent.py` and embedded as the fenced Python below (sha256 527ace04654f2b27…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `new_customer_onboarding_automation_agent.py` first:

```bash
python3 new_customer_onboarding_automation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 new_customer_onboarding_automation_agent.py   # or on stdin
python3 new_customer_onboarding_automation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
New customer onboarding automation — Close a new customer and trigger the full onboarding sequence in one prompt.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/new-customer-onboarding-automation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/new_customer_onboarding_automation',
    "version": '2.0.0',
    "display_name": 'New customer onboarding automation',
    "description": 'Close a new customer and trigger the full onboarding sequence in one prompt.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'new-customer-onboarding-automation',
        "upstream_url": 'https://coworkcookbook.com/recipes/new-customer-onboarding-automation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '618b1e2db4f33a0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/new-customer-onboarding-automation', 'uses_skills': {'custom': [], 'ootb': ['Word', 'PowerPoint', 'Email', 'Communications', 'Enterprise Search'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['word:trigger'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class NewCustomerOnboardingAutomation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'NewCustomerOnboardingAutomation'
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
    print(NewCustomerOnboardingAutomation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
