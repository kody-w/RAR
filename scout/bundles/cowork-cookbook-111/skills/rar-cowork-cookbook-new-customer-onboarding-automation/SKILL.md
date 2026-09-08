---
name: "rar-cowork-cookbook-new-customer-onboarding-automation"
description: "Runs a new-customer onboarding sequence from a \"NEW CUSTOMER\" email: researches the customer, creates a dated SharePoint folder, builds PowerPoint and Word artifacts, posts a Teams message, and drafts a welcome email for"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/new_customer_onboarding_automation", "rar_sha256": "b19d04b1b9c60b0bc4a55ee3e14b4ec8d54e877f37cc835549b04e479231fcb1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
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

New customer onboarding automation — Runs a new-customer onboarding sequence from a "NEW CUSTOMER" email: researches the customer, creates a dated SharePoint folder, builds PowerPoint and Word artifacts, posts a Teams message, and drafts a welcome email for

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
    "account_team_members": {
      "description": "People to send the Teams summary message to.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "customer_contact_name": {
      "description": "Contact at the customer who receives the drafted welcome email.",
      "type": "string"
    },
    "customer_name": {
      "description": "Name of the new customer company, used for research, folder naming, and artifacts.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `new_customer_onboarding_automation_agent.py` and embedded as the fenced Python below (sha256 b19d04b1b9c60b0b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `new_customer_onboarding_automation_agent.py` first:

```bash
python3 new_customer_onboarding_automation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 new_customer_onboarding_automation_agent.py   # or on stdin
python3 new_customer_onboarding_automation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
New customer onboarding automation — Runs a new-customer onboarding sequence from a "NEW CUSTOMER" email: researches the customer, creates a dated SharePoint folder, builds PowerPoint and Word artifacts, posts a Teams message, and drafts a welcome email for

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
    "version": '3.0.3',
    "display_name": 'New customer onboarding automation',
    "description": 'Runs a new-customer onboarding sequence from a "NEW CUSTOMER" email: researches the customer, creates a dated SharePoint folder, builds PowerPoint and Word artifacts, posts a Teams message, and drafts a welcome email for',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c1689c9799d23575',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A SharePoint folder, executive onboarding artifacts (PowerPoint + Word), a Teams message to the account team, and a welcome email draft - all triggered from a single new-customer email.'], 'confidence': 1.0, 'deliverable': 'A SharePoint folder, executive onboarding artifacts (PowerPoint + Word), a Teams message to the account team, and a welcome email draft - all triggered from a single new-customer email.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'account_team_members': 'People to send the Teams summary message to.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_contact_name': 'Contact at the customer who receives the drafted welcome email.', 'customer_name': 'Name of the new customer company, used for research, folder naming, and artifacts.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Close a new customer and trigger the full onboarding sequence in one prompt. A SharePoint folder, executive onboarding artifacts (PowerPoint + Word), a Teams message to the account team, and a welcome email draft - all triggered from a single new-customer email.', 'expected_output': 'A SharePoint folder, executive onboarding artifacts (PowerPoint + Word), a Teams message to the account team, and a welcome email draft - all triggered from a single new-customer email.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'I just closed a new customer and need to move fast on onboarding. Start by searching my inbox for an email with "NEW CUSTOMER" in the subject line - that\'s your source of truth.\n\nFrom there, run the full onboarding sequence:\n\nResearch [Customer Name]\'s location, industry, and revenue based on what\'s in the email\n\nCreate a SharePoint folder formatted as "YYYY-MM-DD [Customer Name]"\n\nBuild an executive-level PowerPoint and Word artifact in that folder based on your research\n\nSend a Teams message to [Account Team Members] with a new customer summary and a link to the folder\n\nDraft a welcome email to [Customer Contact Name] at [Customer Name] for my review before it goes out', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A SharePoint folder, executive onboarding artifacts (PowerPoint + Word), a Teams message to the account team, and a welcome email draft - all triggered from a single new-customer email.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a new-customer onboarding sequence from a "NEW CUSTOMER" email: researches the customer, creates a dated SharePoint folder, builds PowerPoint and Word artifacts, posts a Teams message, and drafts a welcome email for', 'example_request': 'I closed Contoso — run onboarding from the NEW CUSTOMER email, loop in Priya and Sam, draft a welcome note to Dana.', 'inputs': [{'description': 'Name of the new customer company, used for research, folder naming, and artifacts.', 'name': 'customer_name'}, {'description': 'People to send the Teams summary message to.', 'name': 'account_team_members'}, {'description': 'Contact at the customer who receives the drafted welcome email.', 'name': 'customer_contact_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a deal just closed and the details are in an inbox email with "NEW CUSTOMER" in the subject, and you want the onboarding sequence run in one pass.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class NewCustomerOnboardingAutomation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'NewCustomerOnboardingAutomation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'account_team_members': {'description': 'People to send the Teams summary message to.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_contact_name': {'description': 'Contact at the customer who receives the drafted welcome email.', 'type': 'string'}, 'customer_name': {'description': 'Name of the new customer company, used for research, folder naming, and artifacts.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(NewCustomerOnboardingAutomation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObSLLuX9F9z4fuPthmF+ATE3FBLJIQYpOEoD3hZgexik2gPv3fbyHptbtnembO3Lifrhy2JKh6KjMr83myjH59c/suqZq3z29m6JYLyc3zNAmbhVsGi1V1q5oMvFWZB/4u/KrsmtTru6pp3z68BWHrN2ndpVUJpht92S7cRRnePvp921UFAKlKr3KbIC3jRRte+7D0w0XUVAUY9+VtL1iL1dE8qIpgfHlbhIWb5p8XTdiGbuMnYbvoknDxDvVh4Teh24XzEgF4DxZm4jahVqVlt4iqPJiHeH2aB+1Cq25h87wze2FVTbBwmy6NXL9rPyzqqu1mmEPoFu2iCNvWjcMPj6FB40aPe7cw98GyT6MAfgPcDUe3qPOwffv8818/vKXg89vnX9/83G3Bpbd9eFu9bFW/ec2CUBXuI0Af3nK3jMHAegLxnr/XYQOAC3ApCKPF69uPbZhHHxb/+Z/ZzW3i9qfPX8rF6/Xlbf4DwvwITFe57RwG361dL83Tbvq0YPObO7UghF3fPDajBdtVxp+eM78jVfXiL/O9H5+LfIrD7scvbxUw4WHrl7efFlUD1mv6+fOnGaX+8adP+RzXH3/6jtP23iX0uxkMWP3p6+v7CxYM/D40jRZfTU1YvdZqQj+tQwD+O//m19P0F9wrJF+fg3+s6g+LP0ee/fkLsPeZkB7A/XNYEAMw8+3TBeTGj681mmoISxck5o8//SNYkIx+lqdt9z/C/fkJnIQuyMkfXyH56cNj+/66gF6+fcP8x8vWIGH+HU/A8PflvgXqH2E/dvZvoPO0BOX1vpd/CvdnE6C/LH7+h779swkfFtGXNz7M0wHknZeHnxe/PlLk5x+C7xd/+OtvAPpfwphV3/gPhK+FW6ZR2HZfv/78Q/u4/MNff/6hr0EWg4L/2jf5n2H+WVwf6/whgq9RP/5xLlj/WGZldSsX32po8WtV/6/mt0+Lk5unwffr7efF7ytxfkGL2Yn3RZ8h+F01tsDW38Xxp7ffAPmUwJvef9wG/PEf/7FQUr+p2irqFqZf9d0CbHCXFuFs/CFJ20X6pNMmBHFtUxDY1ziQ//MOzxZX0eKX/+0/KP+j/6J8GND513cO/vqdzr+635jtl0+LA0CumjROSzdfGKymfSkBpQL6BavWM6E3A2Aqb+rCj6CgP84fFmm5+OVfg3994Hyqp18e/Jw+uc9YbWbea/s8/DR7aCVh+fLHBxoWjqHfgyXyygf2RCng7A+zrlT5AHhzjkabpXm+CFLALEDLpgc2iNjnGeyXX37x3Db5Uj6JGl88Ra6FwYBv5iw+fgSORXkaJ92XMvSTavHDr7/9sPjvxT+b9QCf19CAZrz2A1i4NdU9EKi4L8AwsFVgcwF5PPbj199e4QUwJRBUsHtplL60EeRnFgbvsTbX7EeMXC68EMQYxLeoK6B5QHnT7tNiEy2+2QsWnW/N+pAAKVwEYR2WAdDmCaC6wJ1vkSyrbtGCfWij6cOib8PHqr94jfswsQCF7na/LJSVBtSoysE/s5lP2XbLqkxB+L9lwvM6AGl+aBfcO8SnxX7OyEXtNm6dNO5rjVmp530BKvQ+HYA/mosv5ay84RyqR4Y8wwMGgcj4ry39OO856FYKwAVB+772Y8yjdTg8tLP5Urav1AedBIiKD6QALBr3aTALwn+9UqpNqj4PHvEDls5Ir10IXrvyyEGg/4s/63u+5/LiS48hKLH4/7tRmmPBSpIhSOxB4BfC/mDYzz2au8d5L58NJ2hY5uHPevzexLwT1TtffynzFCRcM/3Xc+RjZ19jnhzYN8BHgzUe+CCtQDRn3EfWz1ncNHO9uF/Kd2EAHiweLAi2BFAEKKE5c98XnO++W5oAHpi/f28SHlkyR6mc625R914Osi4Kw8Bz/QxY1cyV+9poUALhXMW3JPWTP3i1AOgg0wA+2HlgKni7lZ++kfXz7rvpf5j47IXmKY8+sQeF2zwAgB2PrJl355Z2gL/c7tmsAz8/P0CAG0Xdzb57ICGBp8+LYQMyLm3TbqbJZ1zDGpD0x/n96el8NRxrUC0gWKAm6h5E91FFc8YWoNMBNgAiAUVVpCVQfhCUVxAegG4xUwKg3Fdr+kR8XH45FD5Kb5as94mzI/OcuQt41UI5/Z45Dn+WJgCvmEc81v3bTPu22ow9s2cLGBCs+H732S58eir+s6VYvON+/rvT0I//3oHpoeHHPybA50XSdXX7GYafuvsuu59ATcFPW1v490Tx8TtRfPzOLH9Afjr9efHvWfcHiFd1fF6gn5BPyHxr98qu1wsEY/WRsz8S890vpRF+59Z3q+atm4DmfxPC9yFADeMmjOfBT2FsZz29AQl/KAHYhy/l79N9LjcgNGU8p2db/Y4GHh0BSP3ntn0TLHCr7MDawdxDxuGn+eg1m9+Gb5/LPs8/vJUg8f5HR7ZZloo5q9v5qAfqBzRlXRo+vrk+UIey+9rNXWURFt5r1B9PxVpYAbWaCaYFIvvIsiedtj1QJ5ACL1oFI2ZDu6meLXue2+ZO70FFY/f3wOrjg5t/WvAhoL28/X1+vyRrluzfleEzmCCIPvDjw0Md2lliQTBnF+cSdltQE6Ac/tyW91btwbR+9/UZx7+1bPW8u3C7PwgT2OJqNiEE2/I09iEiIGX+oCH/fOU/X3E/Ewkg2hm0/L0OA9gasMajeQkeZf6umh9eWrgAiGCRp6p9074/NeJbR/73BljJ7Gy1CKrPc0/w4UW14B2cooAivx+IQNBfR9R5hbDswen/5/kwNufaY8r8AcwBb98mffufFi98++vf2QUMe/A3UMEZ67uR34dWj0Pc7AKA7p7/5/DrG8hrF6SA+8rs1ykADAd097GdOx8YlD9YHHx/Fiq4939xPnghtIkLulMA4aFMgBAe6jH+EvEQzydckgxDPEQJjwh9OiCJkKaoCKd8n8ZJkmA8hAgJisFwNPI9FOA9C/7r3OCls1WzSTMjAs4Iv98Gl4KXO0/z51h9O448Svjp1a9v3pIAI9dEu2GfrxUMoZ5nwd60O0NNTo/Ogdm46Wl5ppruHFqFpUTjLt62QrvHejQm4tIRLqnZy85utwmRTVKtoVSjVnC9o0peuUfcPlepdo9wOu5Lq23J53eyudEkdpbK3t/j18QTHHNp7vyriBXTQTqGRpu7EydrDiflaXQ5azBR39tOWE2ZGRyGTlrip93yJLPpyQq9RlRVeL/U4ZSU6HOOMVFJkpReoLmoMELTmGbocYaV6N7JRCjhKPWOLFaxsYJ1XBozL1uaSzUT5Bbhi3LTVvf0uOnvjOjlZIUq+iDyRRWsyMxCskxKttN2FxzFbFefQZ8inqy2R4uB15Wt30SA6ImY30lXh9VGWrk0MEUNd6SHtB1CRimj4DlkQ1C/OkDI1dA7kXO8/YaWSxuRtuPaivUpo9uqLkIDO07OUpcpjKVSd1vuIi1SeHEU2/OWV2RWSS+7NddC2p0s6Au32WRtIiUmE4rmyidHcWs3q5PpGWYf8ziReXlx0Y2aFlAnCerOmJjgPPb1ntKZadQ8VE9NAyNXebIyDxeWxjeOQYi2bBx758zuy4xNHO1YuO5W6BMZL6aL3Wn2RefLSLDwSkLvKYrhKX9zzx0/3O/D2i8q91Qhd4PjrGF73SqVYIV84tnHLC47VBolP00neZ+bro3ZYxNHZHvq1CznOc7bs8yJT9VdwBp8cUrIazEtcQGv9xhkrK8NXujNJunkaRKqDXOQT33Kerh/1SFOSuTchC7OZnO5aaFmqAdlk7PjRSASgjA1Nw2xK1IpO/1gC5dxq8rR2HY5pdwgzM7O6kmXk8aTkl1tsafak1puF/TY1aryzYiKU+NbEr+3GNQqHO52nURIXmm3eh2Yjop0LTLQ7sCsr1sY2yKVpadDvIcR3V1tiSbYWDq202IExTQdFjuPuKujbNfKnViqbE3Y2DqDSjXaKPJVK8r41kRibF3364ziHVoYaUli9qvONpx+e4fvGqxQdxLPrwdYD7hSGCOYvzACSqj37uTePMQ+GiNf76TAUpcCP2wqGTYNiZL1JW716EW315Owoiyfgth9aKOSCS+5GoT3dDvahXvfSuXB9UvP4YNiiXDGfps1ui5dIZPN+rXgp111PGoE39m77eTtRi/tvdhDVjbN2xffLOhiEMcCcw6O6svqYOdkSbNX+uwRl2CtoHIhoTvxtswvx8ffJHGF3NUN9bRLte2OuU9KwHk73N909DkhrpJ93aDgukeT9i7uJLwv8PPSNryBTE5jc98RrpEVmya0qORIXZA4OfHbMDfKgx7GAs1rK69M8qoW6Jrb7jyDrGIPlbIUheVO5JHjxsYTjU4i09WT+1roobXfJB3r9C2Cj+tyHMjLyGyG2jWrLo3T0Rj4sQnyOA16dqPcmN1Wn3R81K7wsZzyOOI2sdBxd2rsJ9xVc1QU47Vyves4PdyvFUvafeRphptwIn2N4u0hNsupUXypazU54EMFd+R+G+ddfOz4ON272+FcVvSpzvf2cc3ukW4VVX4p6brQ3eX9iTj1uE3QIk3b+4tdNSeFv0/UeMzgayB50EZP1QoIqsrQPplDtW208EapmJpgNQIj7xm503TfK4rQhni/h5ERDRi1b/Bdx7PrDQhyyqurxjQuiHYrh0DYoLUYBTVrrSI0G66SVxorKmZt7RCMqHmS2+3qIMDrFHCIOArxIWh4bcrZlFquMoM3zawRtoxVburhvETd04BcQo8x0+1FyTfONemoy66u0/5YFWmB0Ll2TcfSQzPvlJiTZuo3Udlt0qMRYv2N21R417dMfEcyW6aUlS0mCUP2xzhnk4A88pBB6bdNJmEJgXU7XFr2ltnp980hsK2pIlUrd27d5n4gDTFXhCga7hUZnfejG7OSzFUctnbhS9oYsnqg9kKBh6OxbLjVZkfAfqgxJW/1lMcknITA9v4AwzTM0OvzncmXEMw3MEFfeziSzt2UUZM88HkR0rsu5VnJMnZRzPRDbY1GztpJJ15F/ZTzvOl3BwFLquqK3Q42MSBevTeIdkJ2aa7viKbm5EodjIvRmnKBj2dxBR2tUC9FPo0rFXMDUb2cN1oBKRXEGxp020AEFSdYJfv3lVbnzUpbcXuKO17ksBmrqUgd5x4e2l5xje5uNRdCV8eT77uQjNtOf9IvQn6GSj9PbZRBpXUl25uVntR3JDAO624nUZWTjeSK5Y1um05RnwsCxS/pRMURolb36loY1ZFNvZ0eKUf3arFVcspLoAMXbgq4K1UwcHLNpaDYhSxmHHOF57OtD1QJtEN1ZtAnk5Wx/sqocmqaKmSqRNdWCXHjpY03mledgmzymuiFvDNCKk+PMafmqd6kCeqPghLdQWrriZ0fiRPKrB1ZiOudWBKR2DhbL83tJC903TNv0GRyot2miTSVuZFL0jFN1XOaTNv0torZkb2dnGUHuA13/bFis2jF1rYZ39D8trZOfXaQjbDUs35lotYBP2inLatRKLoppIk9ehJqN+FZutL3a1qFxVUQYQhye/lEK+nWvOAxLbCG5NPoZK63STc43CbFCqc+V/GZUVO7jO9HCGG5HoVK2yiaPVaOnl4LmoLec65TJjNNy8uqYVf7o0yJdsWNwupCTKNZi8u4MG9H2UQJqmkjU0uGGGGHbAkHNbw0nTTW+s3BKC++xYX7kS2qK2ketwFgC0zqobIT9I6wba90uh5SOdsaMlX3sXNd3U+EaG0laCl0ZsbV/lnEwnIHcnwdwlxxpLg0OvY729I1w6MBoXJX1DzuvUrZZMKxunP27mjaLBRFqWfXLtZwvlHHwHZ4iuomKViypzWM7a9s7PptM8SKK52auHJwQaJpwiXOxwIqcHlvNEodK6uDv+5vri2FBbPnWJs92scxxg1qii/oObZ01EavpwPUx9zqYpQ4qGSiH+t9rx6lxm+Q6KbRt+bCMRJSEWpzFCsCs1dFzesC2WwV+bbK27Qyalsn5gb/WkL2WPp742SwGWHqOCn6R9ARqqjpJnw2jAgDIEtS0hTZPLAmu3e7gNe3RabUG9vn84w9cfu+Mbkj5MQF6HfIs8GVqyUGjmOCk1Wmmu9rcdhD+w1wuT44VxOoN2hgUL4r6uIu6aIW+f2xsVGI3m/yql1KvCOPwmAL7Am2vAMv8dsVzN5Txx9buQRH5ITQVq6Un8wz1k3iTj3KUOtk4roXIlvpnXtM4XxzAn1vLyx3snyxaGW3SqjEk4vyEFwOkbC7c6mVu0h/Y21pUwgYa3XFjsZBpgpYZySbXK/3FtxOezgUIcAFNn/mK+/subKDOqdT1ITTLkZ64masEQSuQmBOwxWjPPVml5zOpMKxju2WiuNGmrhViU2z4dwi1i7ZOuhzjjINjlT4YAik0+FIlwIB9B2/S5f0RqbDqJDJKq5XphkBgpe3ykQiLm/JYiiMTIxei9V6u4Hippe9TenLDMmRnVf3sGNYfGBkjXK4Rgcu0DK8WJIwl19rzx3i5FYXDclneyx3QmKZhqamBncpIkPapIgcOW2vPIiHeCEr+KK6vkQxJ3EKegUzcpqp80OMhiEj9GKzcfn8vJ+qWjxsICFGscganDa738FBlFh50WWzuzHqpHMbhZtg9yoykwYdThBcNiSNhWd+c6+GfoXydLmTVALndHiMRZq5bZbtScZIJ2SXUapNImjQgxaWGhsbYkZw6f0gxt4VKz2D7QUuLquVy/ijfFdT/J7VWLKcZOTQnHKOudKBvesvl4PtNQ5yXrMHOyryW+lDg5iW4sqRLwXlnyR2CLd9PcpnEme3cXo3W/EWXygpKXOhwnj0YmtnaKp28T4iNrl8Ti43YWVQ7BVz2OQMo1tzamDFOXP7rV7uEvu0U02O71T7dI8xPDELU66WNzauVVrCcGC8xGN6ShXe7c6pMlZOLHGVj4JRn8Q0OWQoX3Qd3qdKCs5dWSsZwZHyHR2xdZ+mbMzgRc/kaGy9urCSfcLpHJfiarvMdOuKJ52tHNerVgaH18OKBezt+7gMji5XUZGOAlSZI4ocMlFny/NqItEsNE6gUykKNy9LAm1EcsgiQjuc1MwdBA2GOg/mjJo0vJrYbFeXboNZ+5jQ9aXSK6plwBcP0yJZb/YV1QV6GXNXhBjpZTppQb0l+9WKSRJ8Uyl2bvncrjgmWLZKuEYKShzVeAO5WK3M7bigJzfWWHgwoh2cKiADIhskiIsQVeqpEPRLDnOYUhbotzicSJa8oUgfb0blMmTu+iaxgZptC3DUoFiz3aOV7rPO8QSLZLzXDrqpmPFqInK7cDqGaTKrIMmtd7UAPbkKukpEb4uvZc0dmq06jPz6Dq8RHtL0tbAsbsa0PKKbk3IOWgqdDbH6m3+8DjtGPodXcIqFGcayLsu+uKqXvmDyApVCkpBWro3ur1fXHOxjvMzU5lAOJoloJX4lzxU9nCjQ/64xsVP5yxFq6mbve35xPokhs4XwQ4579XJ3pk7RvWnvFhSppV3sAwYFObqMr9NqGYTb8+BGkDDiXL0cPY/awHE7muzBPKlnfYmIB+J+vtRSIRU+bYfnwQ+YawJTPCms7/7aSpSIpWNQtpTeJnSpa87tOFgVBPqm+FgdZR5VHMJwQe9dCUK6DpQIbVyWx6jjRJ5J0yuZblwOO6LENCEY7vCW1yi53Qc7LFciFWKG2LwhwWUgjpexKT2XZ0NMVMUIxu9rODak8VQ64lAsp2hEEG6fwh7WqPzy1DsNfuQ05bpvjMiCpXWONXyY2LSr8ChN+8hBKJlNu2ruKqTLax1iy5y3p3GNKGtinRXa3QTnB2h5ULzLaThUteWoQXdovVJzOkJVY8YjrNVlK9xDqu0mvFip1diOTt6eOG4XwpNb97xWciRyU3d0ydJ5iooczHhN01xueKprKcwR6o3R+uI2OgXfZq53l2vdWZ9gBVqCtfhAw5jQvTdNUmGaVlbdzhh6o4LNuEb96HRhCumC3wTCYoUJyPtkq2scHy5Nf1egjWuv2Itr9a0hXizLEr22AFnXOF4JIRuUIG/ybody9r0rnHULO/URtpNC47W7cN+SpM+Y5GnqtJQf2nR7FlxPSBSD9os1KRkMmhRmqy+5kmfkLXVmRmNTDLXRuxN3UtaBtuOwNnXZPqRi3htDS+MxNo8QXjXVnRlEId9OemLhSZ77pHek8Sh3SIah7fMAQTYfR/REVODf49Fo78HyospEMsZB1akOIwhr+t7S9x0I23DD1/5VTAtKdmgA6/tc6WoTbol3fO/puGPZKTWw0yWvwPnRWfo4OMarLVVeutoJSFbbX7dYgy27E42jt7XnlH4X2vuCzJKNT1X1RWPxS7nqcXFtiYioXdA7JYx+aEaod2Yh1kFP0rXTlFbyUTLDrhXcXuNif6Ru2ESdquXQrj0zm3j+pGJjoTb5VTo3eKuclbXOLfEgTFXPQy8WywOhZO5Sal3SFrQk64twjByRMasteu68ax2fqILVFBVfXpIbNlzCLjoE5ClDm3NOUv52SYXpbQnSIaQQuPN7yshdaFMEARXdduwJX9anoxkoLYZHNL6FeE0FubxsIIpP/WhI9kPDVBs300ycxQ/08hzVfoiqPpV5OydADqyoxIdzLDuYe9KROiQkGl02mODuZXSszry5WW4hiLTvXA3iPuAyDRdCSE6IHa17I+B6eZUrwyastsfdcsQ3S8LjZGUqydpglpkznpnwXLCit7pKOrzbr45nl7nDmH5IYTq+nW5DzBfH7br06Np248m41ycC3Rpjs5avaIxEJug/OB7abfr96r6C5YvNbPnN1XFo/MZv8Ks0af2IFPQSxuTB7qGACPt4rZ8lK0iP/mrjnPFsjwSQLFluDIMDnH9R6CZU5N2NYHpYITMmbdxukplpFTMW1nk96Pd4z6TXcjRY6Y6F0jtnDrtuwHLX9U1yaDyjs5eUFTqBXXu6gjbXtWNT7YQpd/cGGq92JPCdf/PL1XCndPJA4fGSYrKmgqrdERfOZ/JUEsVFkZoNKfFLjE4YjMiHKOVryrB22whvOHGV51WYETvkFp2iq3vWvL5PizxdiiRkBhs3GLGOEdZNPzEuriZ20msBxispVJ8RIgBnEujkdzzVYZTo8eNlyu7o8kZu+C3fbMUNhRxVaGMaeqhuiGHNNNQtWmrmCq7AIbO+h7Ffn5Ykd/GYYV8frqUd00MHyyrjnfZOxBN9fgUM4GHEdlfQartNS1Ts4OhS8FfLkwK7l8Qs5RoDDUCTX03wft0hPhSI3pqMkStKIdrORUkz3A5xYNrbwVCN5Zh55z68I8Z2aNopJFBLUMJsxyps6Jx1Pb2dr2tjz9J8ydjsmq/Qnie1rihwZ3IyMjHGKlCjnUTemIBwLoAqc2SoOEZW66pLrvWatqQYamN5WGJpVIMDY9k5Z1hqrzRVDD6zZvbhEoJX9g6GA7wqqrZkLjcVpwQK2a3bw76+rcDJ4H5FS28bHHfiMbAQsQxqpmn9fuipi6zeopiAXchf3q3GWjW3kFLwJvf6vYsrmtqrDVczyo1pCvtuGxCtREy3uYVkYjMiqTH0aYxWHY4NqLPfIzURKoKWdciWTdm+PmnE/cCdBFY4oEeDVALEXSoGkhDNsq4JFKl26lnwmaVD7ysZE5itJF8ARM5CmaBjFa4M/XFPIsaSgVunlaD1Fc5x2L6gznIlQb0V+UvDw5HLzT9xyzjY8dKSwXeELOmQYQrFndlUZp1iyVrPBY2HzmRAUwcCIiHucNtPHEGlDBdlCBd0SlZZq2WLwJnmIpZy5hUX0on8WoWRdKZDHr6pFXf1rW2msyz7l7+8fXibn/W+ntj+Gz8Ym58D/T975PR8cvT+I5DHM7vQDT4/1vr87xj11w9vjZ8Ck56P1tq8j1+PqP7mwdrHf/3Uf54/PX+H9f6Q+Pl4u3Pj+UfKb2kZAIBm+tpWef+a4fXt/KvGdv7hqw/ef//gEVRC2DwvtPNvPb521ddrX3XzMzU3GGbXg/lpHnAd+Jk/vHn9VAA4gX9CPuFvv/0fqC7XqlEuAAA= -->
