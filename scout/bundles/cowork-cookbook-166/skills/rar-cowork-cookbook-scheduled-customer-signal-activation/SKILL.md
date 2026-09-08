---
name: "rar-cowork-cookbook-scheduled-customer-signal-activation"
description: "Runs a weekly sweep of customer calls, sales feedback email, Teams channels, support tickets, and market signals, returning a Word customer signal brief, a Teams summary post, and per-owner follow-up drafts held for revi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_customer_signal_activation", "rar_sha256": "4fa4dc3a0fa355dc0a27fb0fb88a37e85c8e4ac26885159e1f4c85e680bb89f5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_customer_signal_activation`. The original RAPP
agent is preserved byte-for-byte in `scheduled_customer_signal_activation_agent.py` and in the RCI capsule.

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

Scheduled customer signal activation — Runs a weekly sweep of customer calls, sales feedback email, Teams channels, support tickets, and market signals, returning a Word customer signal brief, a Teams summary post, and per-owner follow-up drafts held for revi

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-customer-signal-activation
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "customer_calls_folder": {
      "description": "Folder holding customer call recordings and notes.",
      "type": "string"
    },
    "industry_segment": {
      "description": "Industry or segment used to pull market signals from research feeds.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "sales_feedback_tag": {
      "description": "Email tag identifying sales feedback messages.",
      "type": "string"
    },
    "support_ticket_folder": {
      "description": "Folder or queue of support tickets to mine for themes.",
      "type": "string"
    },
    "teams_channels": {
      "description": "Sales, Customer Success, and Marketing Teams channels to read and post to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_customer_signal_activation_agent.py` and embedded as the fenced Python below (sha256 4fa4dc3a0fa355dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_customer_signal_activation_agent.py` first:

```bash
python3 scheduled_customer_signal_activation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_customer_signal_activation_agent.py   # or on stdin
python3 scheduled_customer_signal_activation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scheduled customer signal activation — Runs a weekly sweep of customer calls, sales feedback email, Teams channels, support tickets, and market signals, returning a Word customer signal brief, a Teams summary post, and per-owner follow-up drafts held for revi

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-customer-signal-activation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_customer_signal_activation',
    "version": '3.0.3',
    "display_name": 'Scheduled customer signal activation',
    "description": 'Runs a weekly sweep of customer calls, sales feedback email, Teams channels, support tickets, and market signals, returning a Word customer signal brief, a Teams summary post, and per-owner follow-up drafts held for revi',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'scheduled-customer-signal-activation',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-customer-signal-activation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e592ecba5ff3930',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/analyze-marketing-trends'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-customer-signal-activation', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Scheduling', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Fabric IQ plugin enabled in your Cowork session', 'Output matches: Every Friday, a Word customer signal brief - themes, objections, message implications, recommended campaign adjustments, and owner follow-ups - grounded in customer voice and Fabric IQ campaign response data.'], 'confidence': 1.0, 'deliverable': 'Every Friday, a Word customer signal brief - themes, objections, message implications, recommended campaign adjustments, and owner follow-ups - grounded in customer voice and Fabric IQ campaign response data.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_calls_folder': 'Folder holding customer call recordings and notes.', 'industry_segment': 'Industry or segment used to pull market signals from research feeds.', 'sales_feedback_tag': 'Email tag identifying sales feedback messages.', 'support_ticket_folder': 'Folder or queue of support tickets to mine for themes.', 'teams_channels': 'Sales, Customer Success, and Marketing Teams channels to read and post to.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Run a weekly customer-signal sweep that feeds next week's messaging, content, and campaign moves - correlated against live campaign performance. Every Friday, a Word customer signal brief - themes, objections, message implications, recommended campaign adjustments, and owner follow-ups - grounded in customer voice and Fabric IQ campaign response data.", 'expected_output': 'Every Friday, a Word customer signal brief - themes, objections, message implications, recommended campaign adjustments, and owner follow-ups - grounded in customer voice and Fabric IQ campaign response data.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Fabric IQ plugin enabled in your Cowork session'], 'prompt': "Every Friday at 9 AM, run the customer signal sweep so we walk into Monday with next week's moves already informed by the last seven days of customer voice.\n\nMonitor:\n\nCustomer call recordings and notes in [Customer calls folder]\n\nSales feedback emails tagged [Sales feedback tag]\n\n[Sales channel] and [Customer Success channel] Teams discussions\n\nSupport themes from [Support ticket folder]\n\n[Industry/Segment] market signals from research feeds\n\nSynthesize:\n\nTop three themes of the week\n\nEmerging objections\n\nMessage implications\n\nRecommended campaign and content adjustments\n\nOwner-specific follow-ups across product marketing, content, sales enablement, and demand gen\n\nDeliver:\n\nWord customer signal brief\n\nSummary post for [Marketing channel] (Teams)\n\nTailored follow-up drafts queued for each owner", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Every Friday, a Word customer signal brief - themes, objections, message implications, recommended campaign adjustments, and owner follow-ups - grounded in customer voice and Fabric IQ campaign response data.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a weekly sweep of customer calls, sales feedback email, Teams channels, support tickets, and market signals, returning a Word customer signal brief, a Teams summary post, and per-owner follow-up drafts held for revi', 'example_request': 'Run the Friday customer signal sweep from our calls folder, sales feedback tag, and support tickets, and draft the brief.', 'inputs': [{'description': 'Folder holding customer call recordings and notes.', 'name': 'customer_calls_folder'}, {'description': 'Email tag identifying sales feedback messages.', 'name': 'sales_feedback_tag'}, {'description': 'Sales, Customer Success, and Marketing Teams channels to read and post to.', 'name': 'teams_channels'}, {'description': 'Folder or queue of support tickets to mine for themes.', 'name': 'support_ticket_folder'}, {'description': 'Industry or segment used to pull market signals from research feeds.', 'name': 'industry_segment'}], 'model': 'claude-opus-5', 'when_to_use': "Call each Friday (or on demand) to turn the last seven days of customer voice into next week's messaging, content, and campaign adjustments."}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledCustomerSignalActivation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledCustomerSignalActivation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_calls_folder': {'description': 'Folder holding customer call recordings and notes.', 'type': 'string'}, 'industry_segment': {'description': 'Industry or segment used to pull market signals from research feeds.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'sales_feedback_tag': {'description': 'Email tag identifying sales feedback messages.', 'type': 'string'}, 'support_ticket_folder': {'description': 'Folder or queue of support tickets to mine for themes.', 'type': 'string'}, 'teams_channels': {'description': 'Sales, Customer Success, and Marketing Teams channels to read and post to.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(ScheduledCustomerSignalActivation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
