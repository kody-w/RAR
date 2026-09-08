---
name: "rar-cat-agent-skills-ai-demo-assistant"
description: "Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo \u2014 fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_demo_assistant", "rar_sha256": "0165c6ce3d00a88f977723874a6fb0151cd850b987b27b34359d4a8f111f09c2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Doak Moore", "tags": ["demo", "copilot", "microsoft_365", "sales_enablement", "content", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/ai_demo_assistant`. The original RAPP
agent is preserved byte-for-byte in `ai_demo_assistant_agent.py` and in the RCI capsule.

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

AI Demo Assistant — Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant
  Upstream author: Doak Moore
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_demo_assistant_agent.py` and embedded as the fenced Python below (sha256 0165c6ce3d00a88f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_demo_assistant_agent.py` first:

```bash
python3 ai_demo_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_demo_assistant_agent.py   # or on stdin
python3 ai_demo_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AI Demo Assistant — Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant
  Upstream author: Doak Moore
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/ai_demo_assistant',
    "version": '3.0.2',
    "display_name": 'AI Demo Assistant',
    "description": 'Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.',
    "author": 'Doak Moore',
    "tags": ['demo', 'copilot', 'microsoft_365', 'sales_enablement', 'content', 'productivity'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'ai-demo-assistant',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'c768346e949547d4',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AiDemoAssistant(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AiDemoAssistant'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(AiDemoAssistant().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+V6WbOb2LLmX+Hu82DXxd7Mg3yiIlpIoAGBJARCUK5wMYMYxQzV9d97IWlvu+6pOvd2RL+1/LCRyJUr88vML3OBf3+xmjrMy5cvL8vciiEpz0vv5dOL61VOGRV1lGfgltqUWQVZkNNUdZ56JZRZqfcJSqLMg3IfspsKXFXVJ8jKXKjwyirPrAqKsjoHi0rPcofPdf658jwXkiKnzKvcryGCpqBFXkRJXkOul+bQ1wZHMRLyI2fa1kogPS9d5JB3XnnIgTKE7x0vgbzeSovEA3KJV0FF0kyW+U2SAC1J1Hrl8DCjzNuoAoqiLABSVvYJ6qI6hPLiqT3PvM9OEjkxNBk2SQFz95m3LIGSuwrVs9LqFaDx3LJ6+fLLr59eInD98uX3FyexKvDTyzxaAvPnVRVVtZXVQB7sFoAbxQCgzcB3AImflyn4yfV86PntY+Ul/ifoP/8z7qwyqH768jWDnp+vL9M/pcmgOvSAWVZVA+gcq7DsKInq4RWaJ501VADb+hmaqi6BC6+Pld815QX083Tv42OT18CrP359yYEJ1gTD15efoLwE+5XNdP06aSk+/vSaTKB//Om7nqqxr55TT8qA1a/fnt+faoHgd9HIh76dDvziuVfpOVHhAeU/+Dd9HqY/1T0h+fYQ/pgXn6C/1jz58zOw95GfNtD712oBBmDly+sVJM7H5x4gIbzMyhzv409/p9YJPSdOQBz/R3p/eSgOQYIDtJ6Q/PTpHr5fIfjp27vOv992Ss//G0+A+Nt270D9ne57ZP+L6qlwq/dY/qW6v1oA/wz98re+/bsFnyD/68vyUZ2WnXhfoN/vKfLLB/f7jx9+/QOo/m/VnPKmdO4avqVWFvleVX/79suH6v7zh19/+dAUIItB5X5ryuSvdP4Vrvd9/oTgU+rjn9eC/bUszvIug95rCPo9L/6j/OMVOltJ5H7/vfoC/ViJ0weGJifeNn1A8EM1VsDWH3D86eUPQDYZ8Ka5M+LENf/4xw8MenLypoZAgOso9Sbj1TACtFvdWaP0AK5VBIB9yoH8nyI8WQw4+7f/5Vj1ZyvwsvpzFUdJUiFW9G3i4W/WG5P99gqpQFNeRkE0MaYyPxy+Zvc10y5F6VVe2QJmsofa+wwK+PN0AXgf+u1fdH27L3stht/u1Bo9qE1ZbCZaq5rEe50c0EMve5rrWBmges9pgMYkd8D2d8L/BByr8gQwdD05ezcdciNAHHX+ZH4AyJdJ2W+//WZbVfg1e/AwAT1aWoUAgXdzoM+fgR9+EgVh/TXznDCHPvz+xwfof0P/btVd+bTHATj4hBtYuD3tZQiUT5MCsakBAt623Dvcv//xRBOoyUAHBcGJ/Mh7LAbpF3vuG7Sn9fwzTtGQ7QFIAZxpkZf11J+i+hXa+NC7vWDT6dZE/2FeTV208DLXy5wBaLWAO+9IZqDHViDHKn/4BDWVd9/1N7u07iamoI6t+jdIWhxAs8mTqRGWz+YDFoMWCuB/D/zjd6Ck/FBB3JuKV0ieEg4qrNIqwtJ67uFbj7iAJvO2/D4UZF73NZsaqTdBdc/+BzxACCDjPEP6eYo55OQpKHW3etv7LmNNLVG9t8bya1Y9M9sqp1A4+X0MCJrInfj+n8+UqsK8Sdw7fsDSSdMzCu4zKvccnG+gqZ9D7w39bTD5/3oKuiOzWin8aq7yS4iXVcV4RMzJs3qK7GOQBNMJBNL2UZ3fJ5Y3Vnoj569ZEoH0K4d/PiTvcX7KPAivKQFOyly56wdJBvCe9N5rYMrpspyqx/qavXUBgDt0pzyQBoAwQEFNrrxtON19szQErDB9/z4R3HOmdCd/QZ5DRWMDSCAfIGJbAJo6nML3FhpQEPeAd2HkhH/yCgLaAfBAP8AVmAr+dNkdOjkHbgJw/TJPv4tH0wQHrHAbB1gbeqX3CumgFKd0rED9gzFskgEofLirglIPYAxMfEe4Cq3iYUxexm8GWs9Y/Ij/89b30rlbMhkPdFquVQMku4m7Xa9/xPXdymekgKnpVOz3RX8O9tNT6Mdm9c+v2d3C93YBOCSZ+vwP0ECgdtPqnmUTBVaAxlLvmT4gD+4t/fXRlR9t/92WL9BirkLzB1/e2xf0MX0rqnsP1f4cky9QWNdF9QVB3sVeA1AJjf0a5ci/9MJ/WNHnqRw/vzewP+l8uP8F+n5m+tPtZxp+gbBX9BWdbu0ix5vy7Pn5AjXZO/d8/OH6GaZ7GDz3E+DJiVRBkkwZWYWeex9SFO97HIEpeQoIdIJ3AJ34vV+9iYCmFZReMAk/+lc1tb0OdNq7boD01+w91s86AP0gC6ZmW+U/1Oe9cYPIPQLz3lfArawGe7sT7QTedGBKJncr7+VLBhjp08tElH95UJq6Bcg/ANd0oAKVAGizjrz7N6txowmz6frPx9H9k7ymYsnvzApo9p2m7/a6E31N1RVEU4MALO1lAeC9yYVuqrBpvLCBS1UFmrU72VwPxWTk4yA1jV7vc9m/WnAvUsAubv5lqtVPT2p9H4c/QW8HlPvxMWvA2e+XaRSffAai4M+77Ptp2/Zefv0LM56T+d8b8SSQR9+x7KnTTS7+hU9AW+ndGtBa3cme7w5+3zd/bPbH3c76cWr9/eWNI55Res6RQBwU4+dqaq4ISHWwIfj+SDJw738wYT5XABYDAw9YgmI05dCOR7goarGsP2MYBidYhrRo30YxCnNclkLtGcvYOGMTJEHNXNJifQzDfHTm4EDfIzm/TTNDNFlBzRhwa4b7JIajLjh/46TrsjRLOxSDo9bMtiibmln296UxqL6naw9XJtzeh917aj48/P3FpkkguSarzfzxWSDw2WJ0xlZCezbSnmFeZhsr1WjblfEb3umuLyucHOBHc1tXl7nAGIGjn2V1u6yXeGhIcwLfHNKVb0rwTKKVTVSKrjA/W/ZqHvDXZKRYZrY/+M7KOIer7cDyPHLehk6GpYU93DqtRYjhRoR26nSi6O3EpE1WK3O9vZo38bxyRWrR9OWig3W1OktxzefGKEt4KowVaJnkcBp8Kx83cKXlGXmunLRG0puwncFIkZBx6NCj1ijo9oaicbkuHLs6H4ZjCqvk+UIXo1g5cU77F0e7CV4h2nmhGefhVi6up6hWrLMei7yVwtrKLt3lkgpt41jspPG63ZlnYbw5ETF0cXuQCE0rxhwW6OP5aojNbjxgGD/fRERUUpK5Ol6Ww6h6bUZgI9vapoasq4bxWqTfb2u8SshrVwpWd70RorvCsKY/5USe9KWIb81BPO9pJYUTJXQE2+IF1eRuhbtKG/QqU0tcmyNcsMgbsZN2rUpRo7dJ7FVhlAvyyloib6wk1I3w5dUZ0VMdn7jQNyQc04p1wl7rzFBK1GktArvwDVM0s3i1vWx3gt2duk4F7LQ8iLBebUyjU8Ldwmo0i9jYzaDuMtNpsbHwXMS4brh4FeKjwWOAxdhK2rZV0yNUgBaXrcy0HC4mir6EC6OJqHNsCmTuYbuNXvBCv0s86yLPbXvN8EF1XnW2skHD8lzqaig72WF/i5MWYWyZ9lMzaJI40s8G527MLj1Gpz5xusY08xvtrPu2bldNQAbWykWZYl/77ZLZuxXOofAQBqN3NHEznGW0OSxsv2EWgmiqln7sSspJGWEVZnHeneFxqFRxFkrR0mersxBvC9ppOS3bHTK50ShVZC17n8Xp6oC0ZeimRoLroYm669G75tcD7+90yV2TzoCIm1odht2+Jed0ehD3zd7cEoVtCg01Hnp562dkXbEyXc6w3HfUdeccjMAjJRxxxS4vDgOSWsFwlflyeYQlnUK2Mt6zidYLRbtwjvl2MdLUWQrSBYaX2b6JjjZ+KgbLtCu3E1d97SYHi1yXInDcXWXuOuA8RFYqTTesm2NuA8KSxzIYMW+Ae2luhRVRFRwbYNQwxku16gYDZMKNHnk0yMIhTB1hvgkCVo/GkhGO107HunW936n9KufVMVZyU+BJrUeWh/1aa0/+vJdb5Uw0+3hdcH4SoH54pUSXEeV9reKHVIWzNNopXN3QocDEAi5hcyoi4hBh2OAStryiXkwj9C8zuz5lScruFULZxaYqGaVbNuE1xuY7e+t4+jwTBJZTikOxMi3NHtFwt+6JTeLnC3S5suDuEnhrXU8HtGaGDVm6PtyYG/5i1Cdxtmm4VZggcorIcJmdwtpjjS2aLZ39LjwNolErghdSMKcJBCKc9BBnrvPrDJ0j/K2zyQ0i+CVcRagWrdhy1nG73UKYGw2dGFU2eoe92Bw3GGNw5eYobtGbmVlF1Ov7azE/smrCnyiUTp1aLLqYM7oNKi72vkz1gyYzSXyR1XhmkkhtalZZMBRrtPIO9ICLXNRLuFOLDZwEpFRqvbiZsVvFrSMLTEa2cHNj6zgLOdRBVGbnZ3MEPaG8YSnNEs23VUTYZuAf552kz9RG8heUihPmSiZHY4PNWKR1D2uCbtpsJCndObRo4Hk5T7iKcho0LU2GEFmNLb/V8m0x148R7Fs4tzOvCjZs25kzV4ycwOYke833CaWH1W0zdsGtNCMyYi/utl1sz4ciV1R7fsrJXBA26fHSHdL+2ChDdNthGOkFGCqbOCKK9YraS8ZyG45rMsadM66RM23cSIy/c03mxIdbMjrq7HZtXBJLcmOsuunK7rizzhxxctfwFVWFYZHh9MGSF8fm0laa5Y0Cuz9pm/OJWhibOYo7bJSl+x0p1gjn0hp8SgUBUTckgxznq0XU74IEOxXzRGayxDXZqjOSdaNT/ACnI1ciWzxPzkHliqYCO6ZeWE2xG3ispsqqrzfIKtwpi62yhVMEMVVUmfcFLATHRpUKR79tuD2eE7bP0+hm1Y7ZXiuk+io3l8VSdRuc4klepWCeDJbRKu4U3K/T+EIYBrXayNbF4Dpb8szFhm1P9OosYLq1wDeLuDfry0jRTphS5H7N8u7MEtewZjb8lriqNKip46FzXEcINrOUJPgVrTkqriPR4nTIlZtq8UNxU5212586oTrOlHozN6u6zjWLl7HRazhDmdW50h8rQqQzbdyxnGBddgJW3JRTnC7SLF555SoN9zsR7q1CS3inoPqdbYkDkxmDtD2FJ6yM1TFt8NvISeTmmhYrrSGL43Ivbc7+cSVsF3gmn45n9MxuusYzevQwF8z1aRU1htXInIbiFbyklxLL5sO8r+eeSoe6dK75lcmXxQCz5NpfWeFqyTuhZl7tPV7dAkMU4P1FXGJjhTHLtEw5R9MdtcD1MT/Z0SkgNJQLzjvK3zWefD5VThG3ASEH6n4uYAyBau1Bs67CYMYz1N9J1zqSF2deoylhu3LnXWISinrjvACldlVxq+WqoDrM3mXwXOSr2YzHxhAfUqQ8afho76/okViturMdKFVbj6qwEbsqmgmZJvU1T/fZOZQuOCgI0R1sCilFg3aluUDGGUOm0Xq4gbQLI3kl4ht4BMR+PfQKd00Pyy1yMQirlpojdb7o60srOgS19C+L09pAB1OXhi3Bck3BxTf4zAdLY4FbkpNvUx1zQzo5xqAxl2yEJ+QpL/kFLB67UTe3tsVp49ESLupKpkjTxfydGnknU9vC87MR1EyNnbmNlO+LJXm0z0xSr0EzNK6yRGTY7nbabHlvHpviQKwqlFEx6soHV6fkB5HJbL08nL1g3rLi8WZ1aO2UNZ/qqOWHvrn1UEszbyQDcvyInY+Iv5jtQGPeV1kflPmczowjPiyWLX8TySYeIn3fUhev0vMVtlUT1iUvKHuJ09vpysy4yyYdL4SOHDfwrKjQHUyHByNsUE4tBVHsEkKSJWG3CpcdmlY4vQlu6VAvt1RhpbQ1rjxEjG8sZkkpy8PXsBZjqwypRUaau1kRrnqJcAwhKRNbwBdKiyVcLIR4abqWf8JszN/greW7REnNyhmlZwRld0g1OwSzk4UT7SWTdKPoNkzN75H0oGgaHcuDm5AkobAc1vHtaeYS7nbZemBOhY3ZoivLqFF2W0P2gxk138vnLoWNfg9shVO8P/onUM4rvxdvFc5ghsCFqpX7Z8490tGMXPIp0AnvyI506VbSlj5h4abMNMdS5djDJqYDD46qvt3H7HzEazBfH8/IvB7mY2CzGIPwl6GV27PEeiOOKDs31OFkf9nXjm1l7JWXECHrEEzIuH45Q5ljghwL5xiOxMob1mp0my/UsGJIZbW6DsJwLLTrcuEosC0Z6liqM6mUsz1O4YtAuzrDbHnJD3skwszyisOIaNWUckUWF4Hg6pMZXmDAhUKt79GDtfAIYqmcZgLog4eqZCqRRlMJbyVbWYaHBo/LXhwj+rZIWOcWRMtOLxAppInGY5zwvN8i2Khdlusrq18NBN9pfknT/cmne4RYGpHuctzIRXpwigaug5HFyZ3hTNbvVEmp16eZnM6rTVRUIsuASva9AZFnOVP09bFhW3GBrVVvaHqYGGLX2N6Ocx/epiMrArKPnDLehGXJX91QdPN1pbDwcg7cSJXBmfeBxM1x2chKetsvz4oazS48MztyWrXm1vtSRqywkzoNXRiwnaLGHl6peuptj7PW5Fiai0tDvPTrkBU3HoIFMw9QxRbjteYI81jcymsuSG70ldi2YSVz3REM3keC0vfLwTQwWQ6JgD1jJexq60tPXyTtgJDoYZMWFewxa9eZ11lPiI0d7VsTvyaA/GJrxRIxI26bsbuisLkS+TPlFvBiz8IXmuQS3L6s/fTqlloYcpkv82Cwihsixui+yRn2wIDzldsLKgOYte/VkSoPO7ssLcHBtxVOlPptNBR9NivOnu5ZhJtcMDKXjjSurnPriqJ0IA/suiu7VX6YYxfrooxO3/RkMB8qPy+wPiNRe2NyOycG3FBkJTiQ0obOVOcy5A+LPeFqpwpvr17toaDmaQtTUa7Nzq6v5InnH67jtcQL38GWTSJgGErhDHnTGYLJ5Vyk+doxGntvKbNu5fqoh1RM2d2ClhkuTp8dCquY5+T8fF2AWUCl48KCyRbRLqEhqPUGNZcYVqwvw7KsaEEt8WRkeA1NV2RJG6eEWxsulYAzBZhrYPPGYbx+M9PjUtHzI9ZW57qn+Xwt+nhyIdp8jEbW2bWbFddv2yhfo3KuXQllvfFDCSto8Xjsw1mwuGIEEjFgdgbZdDskea+bRZWjNTjiLEOqzw89JZxrcIidnVOcHPHThUZZp66Wx31yxiyZukoIcb6wvid6YFeBXV7a/VYiBH5zU/UVY9Hhsi+3G2N0d6jbJEtkLNqNCrusOu4pHkeZ5EzaYsB4+JVpWE8CZ9Z+mRBjrjaFvDkmYdZ7je2mY8JdZGpNX9yVWDOZwo4Mpey7Q4myUqH4G80xC4xjzIWpbgydC5xDiIo2GGbtTUE6ZeaROwfhazV2sZOur257XT0yJ6K3CUbZ+g65RJdFKUQEicxHVWOL+bm7Ie7G0/ASvrLcTgdHPKxcVEicnYQ166U8ZumD7am9iLSOlvjB4KvM1e5uN0f3GF4ulrjuoWXcEZp9YEXMXGd2G1kbAxnk+hwiyHq5MPmZEaFZc56PWWjzC1s3VSovdzemxdsuRPJ468KUdiEy1zs61+J2cq++m1UFwu53nJ2u7LRvLzp5zupwVPFLB+96s4z8ZBZdKFpSvY7hW2Qew4QiK9lqHZ6LRWg1VzXWYGx1mRVrupTpYYzYzf40s/P1hkbgxmkWJ2Q3W+7Y5IR3RzDYSWbYo5dTRlztNPT4rbV2rMDrj9KpqmfcYrcMc1c6rjx5gaENvS5TN5ACEMElhdQRTqzHKBXM67yiI8K70Fd8tr3uM11Fai5Yz/h9kq/B0dPs1Za7FUR5AKf5prRDC1kUTFOOZ+KC20zbSjKy1YRdY1yTEBywqXZHzHSks6JdMC+Dq0FcuYAJqTW7RGPWnxERyYx0QFkBXfeXs4dIxNydIbvzwgPnq2jc1W7hMgeQGC1HXgbCaZEArwlJQI6jfFhd9vYS96VOrY4sQohyaGjB7IAcKkSZScp+E7emYtMMFsAm7ZThgWRvlX48LjWG6K26S5v5sCWt4haI4tmf7c4inmDyRWnbfXk6Rp4cx4cdtajzpFigt1U9ICI4kccecTssrg2/QKx4dFlJroVGJijC56L5MKKxTLFm3TE7hdY8O8qJxa4wNizRbP2gLrbUmjzZxHALLV2kBXeBHekDBbJhbJES+LzIAlnkbuN1lnBXOI+Jm71bd9Ox0NwwjAsv1BtvCUrLXRMKVkmQ5Rc2uHUjP5/Pf/755dPL9Kz9+cT871+jT48r/589NX084Hx7GXZ/VO1Z7pf7Xl/+jQ2/fnopnQhY8Hj4WyVN8Hxw+l8f/X7+l/cpk/zwePk8vZbr67eXBbUVTP/R6mUSn56TP16Ogqv3FzffCJqalluJV30DNtuPt8h34fsbvpe7O+70JqqN6rudz1cywDziFX0FLv8fEJSSHvomAAA= -->
