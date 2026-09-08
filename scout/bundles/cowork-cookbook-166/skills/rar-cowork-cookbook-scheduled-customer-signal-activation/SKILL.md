---
name: "rar-cowork-cookbook-scheduled-customer-signal-activation"
description: "Runs a weekly sweep of customer calls, sales feedback email, Teams channels, support tickets, and market signals, returning a Word customer signal brief, a Teams summary post, and per-owner follow-up drafts held for revi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_customer_signal_activation", "rar_sha256": "4fa4dc3a0fa355dc0a27fb0fb88a37e85c8e4ac26885159e1f4c85e680bb89f5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
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
