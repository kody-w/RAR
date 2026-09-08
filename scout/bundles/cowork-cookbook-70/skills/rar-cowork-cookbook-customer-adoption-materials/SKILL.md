---
name: "rar-cowork-cookbook-customer-adoption-materials"
description: "Generates a Markdown learning curriculum for a named customer and product with three progressive paths (Beginner, Intermediate, Advanced), sequenced public-resource tables, persona application notes, and a rollout order."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_adoption_materials", "rar_sha256": "15d44695ee41d1433201801bcba8bad95f3e37f2181a766389ae958b6721d612", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/customer_adoption_materials`. The original RAPP
agent is preserved byte-for-byte in `customer_adoption_materials_agent.py` and in the RCI capsule.

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

Customer adoption materials — Generates a Markdown learning curriculum for a named customer and product with three progressive paths (Beginner, Intermediate, Advanced), sequenced public-resource tables, persona application notes, and a rollout order.

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
  Upstream entry : https://coworkcookbook.com/recipes/customer-adoption-materials
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
    "customer_name": {
      "description": "The customer or organization the curriculum is being built for.",
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
    "product_and_vendor": {
      "description": "The product the curriculum covers and its vendor, whose public sources are used.",
      "type": "string"
    },
    "program_type": {
      "description": "Whether this supports a champion program, power user program, or broader enablement rollout.",
      "type": "string"
    },
    "skill_gaps_priorities": {
      "description": "Known skill gaps, priorities, or use cases to emphasize across the levels.",
      "type": "string"
    },
    "user_base": {
      "description": "Who the learners are \u2014 roles, personas, size, and context of the audience.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_adoption_materials_agent.py` and embedded as the fenced Python below (sha256 15d44695ee41d143…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_adoption_materials_agent.py` first:

```bash
python3 customer_adoption_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_adoption_materials_agent.py   # or on stdin
python3 customer_adoption_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer adoption materials — Generates a Markdown learning curriculum for a named customer and product with three progressive paths (Beginner, Intermediate, Advanced), sequenced public-resource tables, persona application notes, and a rollout order.

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
  Upstream entry : https://coworkcookbook.com/recipes/customer-adoption-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/customer_adoption_materials',
    "version": '3.0.3',
    "display_name": 'Customer adoption materials',
    "description": 'Generates a Markdown learning curriculum for a named customer and product with three progressive paths (Beginner, Intermediate, Advanced), sequenced public-resource tables, persona application notes, and a rollout order.',
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
        "upstream_slug": 'customer-adoption-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/customer-adoption-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55d78296864b5bc9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/customer-adoption-materials', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', "Output matches: A full Markdown curriculum with three progressive learning paths (Beginner, Intermediate, Advanced) - each with sequenced resource tables, persona-tailored application notes, and a recommended rollout order for the customer's champion or power-user program."], 'confidence': 1.0, 'deliverable': "A full Markdown curriculum with three progressive learning paths (Beginner, Intermediate, Advanced) - each with sequenced resource tables, persona-tailored application notes, and a recommended rollout order for the customer's champion or power-user program.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_name': 'The customer or organization the curriculum is being built for.', 'product_and_vendor': 'The product the curriculum covers and its vendor, whose public sources are used.', 'program_type': 'Whether this supports a champion program, power user program, or broader enablement rollout.', 'skill_gaps_priorities': 'Known skill gaps, priorities, or use cases to emphasize across the levels.', 'user_base': 'Who the learners are — roles, personas, size, and context of the audience.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready. A full Markdown curriculum with three progressive learning paths (Beginner, Intermediate, Advanced) - each with sequenced resource tables, persona-tailored application notes, and a recommended rollout order for the customer's champion or power-user program.", 'expected_output': "A full Markdown curriculum with three progressive learning paths (Beginner, Intermediate, Advanced) - each with sequenced resource tables, persona-tailored application notes, and a recommended rollout order for the customer's champion or power-user program.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': "I need to build a role-relevant [Product] learning curriculum for [Customer Name] using publicly available resources that help users progress from foundational awareness to confident, practical use.\n\nBefore you start, ask me: who their user base is, whether this will be used in a champion or enablement program, and any known skill gaps or priorities.\n\nOnce I've answered, design three progressive learning paths using official [Product Vendor] sources only - no internal or tenant-specific content. Format the output in Markdown.\n\nFor each path:\n\nBeginner - foundational skills for users new to [Product]; focus on awareness, basic navigation, and first use cases\n\nIntermediate - practical, role-relevant application for users ready to build daily habits with [Product]\n\nAdvanced - deeper capability and workflow integration for power users and champions\n\nFor each level, produce a sequenced resource table with: title, source, link, estimated completion time (estimate and label clearly if not stated), 1-2 sentence summary, suggested audience, and prerequisites.\n\nWhere relevant, call out how [Customer Role/Persona] would apply each skill in practice - for example, preparing client proposals, summarizing documents, managing follow-ups, or building presentations.\n\nClose with a recommended rollout order and suggestions for how [Customer Name] could deploy this within a [Champion Program / Power User Program].\n\nUse only public, accessible resources from [Product Vendor] and reputable third-party training platforms.", 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': "A full Markdown curriculum with three progressive learning paths (Beginner, Intermediate, Advanced) - each with sequenced resource tables, persona-tailored application notes, and a recommended rollout order for the customer's champion or power-user program."}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a Markdown learning curriculum for a named customer and product with three progressive paths (Beginner, Intermediate, Advanced), sequenced public-resource tables, persona application notes, and a rollout order.', 'example_request': 'Build a Copilot learning curriculum for Contoso — beginner to advanced, for our champion program.', 'inputs': [{'description': 'The product the curriculum covers and its vendor, whose public sources are used.', 'name': 'product_and_vendor'}, {'description': 'The customer or organization the curriculum is being built for.', 'name': 'customer_name'}, {'description': 'Who the learners are — roles, personas, size, and context of the audience.', 'name': 'user_base'}, {'description': 'Whether this supports a champion program, power user program, or broader enablement rollout.', 'name': 'program_type'}, {'description': 'Known skill gaps, priorities, or use cases to emphasize across the levels.', 'name': 'skill_gaps_priorities'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a customer needs a role-relevant product training curriculum built from public vendor and reputable third-party resources for a champion or enablement program.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CustomerAdoptionMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CustomerAdoptionMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_name': {'description': 'The customer or organization the curriculum is being built for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'product_and_vendor': {'description': 'The product the curriculum covers and its vendor, whose public sources are used.', 'type': 'string'}, 'program_type': {'description': 'Whether this supports a champion program, power user program, or broader enablement rollout.', 'type': 'string'}, 'skill_gaps_priorities': {'description': 'Known skill gaps, priorities, or use cases to emphasize across the levels.', 'type': 'string'}, 'user_base': {'description': 'Who the learners are — roles, personas, size, and context of the audience.', 'type': 'string'}},
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
    print(CustomerAdoptionMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
