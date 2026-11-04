---
name: "rar-cat-agent-skills-doc-format-converter"
description: "Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text \u2014 fully offline, using only the libraries already in the agent sandbox."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/doc_format_converter", "rar_sha256": "f4717f434448dedb4118c9bac67f91897994ccf3a9cee2ebed68021661ec4131", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Andreas Adner", "tags": ["documents", "conversion", "markdown", "pdf", "office", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/doc_format_converter`. The original RAPP
agent is preserved byte-for-byte in `doc_format_converter_agent.py` and in the RCI capsule.

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

Universal Document Converter — Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text — fully offline, using only the libraries already in the agent sandbox.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#doc-format-converter
  Upstream author: Andreas Adner
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `doc_format_converter_agent.py` and embedded as the fenced Python below (sha256 f4717f434448dedb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `doc_format_converter_agent.py` first:

```bash
python3 doc_format_converter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 doc_format_converter_agent.py   # or on stdin
python3 doc_format_converter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/doc_format_converter_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/doc_format_converter_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/doc_format_converter/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Universal Document Converter — Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text — fully offline, using only the libraries already in the agent sandbox.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#doc-format-converter
  Upstream author: Andreas Adner
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/doc_format_converter',
    "version": '3.0.2',
    "display_name": 'Universal Document Converter',
    "description": 'Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text — fully offline, using only the libraries already in the agent sandbox.',
    "author": 'Andreas Adner',
    "tags": ['documents', 'conversion', 'markdown', 'pdf', 'office', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'doc-format-converter',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#doc-format-converter',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd1c0d69a8989af49',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.375, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class DocFormatConverter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DocFormatConverter'
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
    print(DocFormatConverter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816a5Oj1rLlX9HU+eD2pbsAgQT0iRMxCIGQECCQEEJuh837/X7j8X+fjVRVbd9rn7kTMR9G3VGFYO/cmSszV+Zm128vZtsEefXy9YXOnMo16wXtZG718vnFcWu7CosmzDPwlMmzzq2ahZPbbepmTb2w3KZ33WwhmlXs5H32ecFfxOPnxWnLfV7oeeWAy7x3q1MeZs3nBTvYbgIz5+vCzJxF4w7N4lu7RFB84bVJMi5yz0vCzP28aOsw8xd5Bu41gbtIQqsyq9CtF2YC9HPGRZg9Hpg+UGNRA2lWPrwChd3BTIvErV++/vTz55cQXL98/e3FTswa3HrZ5jaXV6nZvFnysDExMx88K0aAQQa+F27lgUHgluN6i7dvn2o38T4v/uM/4t6s/PrHr9+yxdvn28v8T22fGjW5WTeus7DNwrTCJGzG1wWd9OZYLyq3aasM2LComwrY9/qc+V1SXiz+NT/79Fzk1XebT99ecqCCOXvg28uPi7wC61XtfP06Syk+/fiazAh/+vG7nLq1ItduZmFA69df3r6/iQUDvw8NvcUv5xPLvK1VuXZYuED4H+ybP0/V38S9QfLLc/CnvPi8+GvJsz3/Avo+o8gCcv9aLMAAzHx5jUCUfHpbo8o7NzMz2/3049+JtQPXjpOwbv5bcn96Cg5A+AC03iD58fPDfT8voDfbPmT+/bIFCJj/G0vA8PflPoD6O9kPz/4n0XNG1B++/EtxfzUB+tfip7+17d9N+Lzwvr1s3SQEGWJaift18dsjRH76wfl+84effwei/49iznlb2Q8Jv6RmFnpu3fzyy08/1I/bP/z80w9tAaLYNdNf2ir5K5l/hetjnT8h+Dbq05/ngvW1LM4ALS0+cmjxW178j+r318XVTELn+/366+KPmTh/oMVsxPuiTwj+kI010PUPOP748jvgmwxY09qPx4A//vGPhRjaVV7nXrM423nbLICDmzB1Z+UvQVgvwP+ZNSoX4FqHANi3cSD+Zw/PGufe4tf/aZvNlwfZfanjMElqGHDwL96Dy36x38ns19fFBQjLq9APMzNZqPTp9C17ciRYqKjc2q06QE7W2LhfwOwv88XMpb/+lbhfHjNfi/HXB12/Ua7K7Gdyq9vEfZ3N0APA/0+lbTNbuINrt0BokttAAy8EXPwZmFfnSQfIcTb5YcDCCQF9NHk1PmQDWL7Own799VfLrINv2ZONscWz/NQwGPChzuLLF2AKqBR+0HzLXDvIFz/89vsPi/+1+HezHsLnNU6gFryBDjQ8nGVpAZLoraDNHgQM8QD9t9/fAAViQDlcAFRCby5Cz5KUxa7zju6Zp78sV2tQDwGIANG0yKtmLmFh87rYe4sPfcGi86O5CAR5DUqpW7iZ42b2XOhMYM4Hklk+F7YmrL1xrofuY9VfQR18qJiCbDabXxcicwIlJ0/Aj1nNxyAwOc9CAP+H75/3gZDqh3qxeRfxupDmsFsUZmUWQWW+reGZT7+AUvM+HQg3F5nbf8vmiurOUD1y4AkPGASQsd9c+mX2+cLOU5DwTv2+9mOMORfGy6NAVt+y+i2+zWp2hQ34Hizqt6Ezs/4/30KqDvI2cR74AU1nSW9ecN688ohBLZt5qQbu3L61JouPCv/eYfz/3rzMdtC7ncru6Au7XbDSRTWe+IKEbOaRzy4NdBQLEGTPXPreZbwzyTuhfsue647/fI58eOVtzJOk2gqAqNLqQz4ICQDVLPcRsXMEVk+dv2XvzP0ZBMGDpoDTQHqD8J+j7n3B+em7pgHI4fn79yr+8HDlzNCBqFwUrZWAiPFc17FMOwZazci84wnC150zsA9CO/iTVQsgHUQJkA/wBaqCX332gE7KgZkAdq/K0+/Dw7nrAlo4rQ20DdzKfV3oIHHm4JkDALRO8xiAwg8PUYvUBRgDFT8QrgOzeCqTV/G7guabL/6I/9uj74H+0GRWHsg0HbMBSPYz2Tru8PTrh5ZvngKqpnNqPoPjT85+s3TxxwLzz2/ZQ8MPfgcZn8y1+Q/QgDCt0voRsDNh1YB0UvctfEAcPMrw67OSPkv1hy5fFwx9WdBPdnuUnMWn9L2YPeqe9meffF0ETVPUX2H4Y9irHzZBa72GOfxf6tc/QB5+eVacLx8V509inwh8XfxpT/KnEW/B+HWBviKvyPzoGNruHG1vn6+LNvvgi09/uH5z1sMZLsjz7EGEIFTmuKwD13m0F6r73ZtAmxzoOtMqyGtr/Kgx70NAofEr158HP2tOPZeqHlTHh2yA97fsw+Nv2QA4PPPnAlnnf8jSR7EF/nu656MWgEdZA9Z2Zq7z3Xm3k8zm1u7L1www0OeXzEzdv9vlzCQPAhEgNm+IQEqAPqYJ3cc3s3XCGbb5+s87PvlxYSZz1uRzwZwZ/YP3Hio7FdBnTjM/nHn98wKo6TfBw4p+TrW5K7CAVXUNeNeZ1W7GYtbzuQua+6aPpuq/avDIVkAzTv51TtrPi7kB/rz46GU/L953F4/tX9aCjdtPcx892wyGgl8fYz82tJb78vNfqPHWVv+9Em9M8vlhnGnNBWo28S9sAtIqt2xBRXRmfb4b+H3d/LnY7w89m+eW87eXd7J489JbEwiGg6z8Us81EQbRDhYE359xBp7999rDt0mA0UCrAmZ5OIESHo7hOE46gIhxFCVtCvDxmvAolKQIisJt28NMynbdpWu5zppEluh6jbo2jmIokPcM0V/mah/Oilg24qFrMBkwO2Utl9gaIV3Ewygg0ly72NJ1SARBrO9TY5CDb9Y9rZmh++hUH9H5NPK3F2uNg5E8Xu/p54eBoasJY0drCHiIR6gh8Eg/vTJ+TKiS0jgNJyXyST6xu7o9FGupXzJSz212DM3v+bMs5OtWCaBcpeJsTTg9vWEPl/i+FS6XSHZD+tJSnbUcCM/Dup0KiRDskQZMuhZOcYpmW4Guenqui9fdUZZYxhuvTn4mtV08cNe0HCSt7NddlJBCjY+KatvF6UJ4nBA3K72lWczrTu6ousdaWwrEbZ9cTONYo6bqqSx3SPZikB7ajX9M9VXR6Zweqe1BE+6RXhWGaeqscFXbIthi2pmB0O1BJnU6CuKW3CGSKBzkYSlGPeVk8fU+6igCs+0USnVYT5wLy7ccYZD0cOVOCSK2/KYkew1BSM+DK/UuXGOtHNiEiSOkHOlDexfMa3mA++aYGWFUXBJi8ERpI4yTyTcId53YwSzsDc8ukcvxFCF+lJ5V4UKNWS9M7Im8MmlwjT113FfEKQxPBjFEB0bAJ1U8umqyroooUHXhei8b0t3Ud2LjM+MBS+RJIp3ukFnL1b5RuNgjISOkzPCucvX6ljrE3ghW6dq8nQPnMPEBH+vYTgtvlOTHejLUlzze2mtsQse4hTSDuFLhsATL5Qqu5bpRymJ/68aa8SUpQdjd6X7YH4noiEebm3CjiCA/qmJUrAkZM2ohtLJ+j5xEfLI7JutzmKGPMOUnlibU5PJ6IPf4nVxuu5NWSqTeJmyRS8x6u78alnUft8oIoOOSa2FQxsqLOjzt8ipIlpatlOpgqOFeW/twZ3v1lrjgGzqnxEMGnWBq1bUUga1vfTAZI2tDYy1NdNEKcV1u8YmE4arCgwhCq/1gli0n7PMlFN988UAzd6+DsRS9hvYpqweuJcdIU8jpvi2LIT1b4ejecLtM76PtKSQbsuqm14oxWeqMIJb6OKqyfzmDXbJ4zJmdqxl9IlqHzYDTcqr7Sb5GuOPueuHq1FHzrpY7hsTXEOR2J7KEZGxaQYcVBUGed8J8TmSU61aRuZjRb1fbOvDRsjxsBF5ehRtpHaRkXNeD5F+0ZZagCLQ+S3iksDRZ9sJWo7mQ3+PFrqo3zEG9m4eEDOjSxBg+3MM3X+D945qJNnU0FlyzEUk61/OVm3RFqwgG4jn2fWWXiZ7sddVikp0ybUn4qKoCb5SJ1hy2QVqyFs1Sy4uQMne21ZIosBvPiPZc0p0vVs2E2LAaS260CKnekoa7TqdJx3snr1g0SbSg2UzFRS2RSyfopTJBl+lQpb7YRJSvKLS13FqjWctmYo/NYX49uazOS4sqbCyXuTFvmHHaCsVWZhkj0rWoC0t6rTWeHhHX5RRdFVsTfVOTg9V1xE4Iq5zrNYPYyCWa9Em0ZegyCCufazAq3tDrHAvAEL/KUeOudknuX6ENsuaYyLjgeQ+jeSEOdjboGC/GNWkEotqzuL0WqXTc7XjSWSIdwTIN39zo5oLSLq4iMiHsnUSJ9EQuMW/QeMFWu6AZeOHW0GeiL8qoivAT757EchtoALWmE+L8vBupCNrxBsT2rhHYeVn6wjTGvUBvpXOsRRPWRo6/ZndBgkRiOuoEbzDBqZRZrylz078laO5ou63lxuOVlrtrXQhBsaOWddyuOLZC/CYZqg20H04HBVKm9bAvbU0pt9w62dxNmRGNFmdyRtJJqMIO/SlwToOB8jJ8l1r2iGvba2TUfHnZ0a63nLwCEyKSt/r6lI/2UbZzPQsP0xYdqNskbO+rfeVN57ZwzhzIc+cOXRqi22V1lelIHFdlowuDy8FHBpdvq1wiWIPpdwDvWILLpW21wYSlSLGllG3HCRk6sFv9Lu8PY3SMBKpQtci5JrGuC+Vww8uDyYvd3r+arrK9oUeIkFYVdRXvPnEUr7ficK7RssVFQ9X8E3EoXQillICdaNE9KUGJdUGEn4vpugPoeNt6m2nGuD96643G3vJ1MvErodd3Uud7tRBEyGbZR6YSaEHHqSM1jlBt82e2pLEby2DRIBZ2wrNn1rhzZy5RTpvOzjaOgvkm4WhLx8Ui6Fo4Zcc32UBSkRvd8k03+N6Svg4JZqyHWIDjPsL6rk/TfZmSqKQl6z7FOrrmPeaIZivEkBNpEhzF0lYCwyGSPgb8HaTOIbgR03YMtEFExltjyILkDQoUdQTZelNNkiSUkDXstTiLJeZw3mrnPScrUGl2kCDe2mRL305siPoWcV6fh8FdZ1obN6h2LNOyyG+Hsyn42zOvXWh/H0w3+ehx6m6jHlNDjScuKC9WEhM4fCjNqLDDWNfMquhJqyrkOhpkWrpmqppx6T3y6YvMhhf/KE7KzUAchwdGHC/HgDnpSHmXNAchiXV1VeqSdt1xh9rdEsEu4tWCBUI2C1GBjkyitRqoUuI5xRpmp7YnG9qmTHq658dwnRhbYB45XkSaXHlIeDxtNHxrdput57N0wgSXSr2aKXKTG81U73F0o6xaQKisjZNUkC9hs6vV3EzOUwAUtVrmzuUUakA5tNtsFSYxMIg4QvUhPdAXsycn/H6MtWSb3Dp+tA1JyQ0Bzm9NG95rpIqdW6U7eBLi8h73twWt+/DhXqIe0vTNWqL3Q9dvDst9FHDeQRmFo0KaQixEDhOx2zMsTwhkpysL94h6dHpzfcNZx02ooHDYtsJ3uaCczz4rB7kZbuXkKHJxh9JJoFeiF+0SvO7t1Z7n9WDj7FhfQpjlslVzn9GXG3xdcOddv+O2nn0/K+O9PdRMZLrCSjqeI109j0insVc92zGMVK3OZ/WsZLLdM0J4NgqjlKI91heoXLO+Sy6XK13ZdBvWxvAxx2hMWed2fJX2phbv7pIAuI8/rA/MgEf6ZZM4OLNfpSURCSmJ3HB3s6JIqLQH1F6zDJ1KeYK4GoSGYe6O+8LRDTjaEAZyzSEx9u99smy3dXVRhHTbFHtfs8LCR4VVlnBcww5U0puMi0+MPVYaIphJLOqMVlJ+x50LcSNNCk/Em1ZuEb5axc5onNfsVLWxyjYTcQZMnJrnTXGPuMN6KwXCcelnmgDvSuV2nwxG1nnIsDs2ylg+bF19I6J9tjqaaC/cV07E4MMtbAymVpa1rhepz3KFaLIoRYtWIyGHVRHCrM8LpzWjQ0o0DTi57/Clv6ui/aaepFsvafu1Ju6CRmhSvTrdgmWpC6QkoU7klOjl7iWS0w8MOV0ksEdCq5jmDry9XXLSPi+jtY/6LYfRtJITeqge+ALtzCMDWHeCm5DxCfp4bhXrtleE1uhLVh+YItsiTJdG1dSvxyLexSzEmeV1o1RBUC0tMXTi+506X3E3rayLeYLkfJDNQ3e9u8WZTrB1uE9c3c11Qh+NdG8l6k6DygTbLRsszVF/Y+OC0QgKLrNHlNmuYcvZZM2mRYj8tm+xtC/lW8xzw01P74K9JmGOKXCT4HKFgBihi0tmXLaX0N5NOG+2+p6/q0PsrPGxQg/ctU4okSmtS9jlsWtcScuW3Wa67W/DTUZaJr/rUhUbpSnfKYFGDoFbIyx/lVe1pR0sMj8UmrTUt7yXjI3mO5wnb2G1v3H2RR/dQKsRXEb6GD+u64bq0TFpp4bGlpSa4AFZ2Rez3l8L1D7qhO01aDHdKwfPMmJl9kRN6b5zNpZYdstARSoscYfs+IrK0lySzv29pWiPwCGa7ndxoKOKXmxwcRnWMGjP7pwmWt415oRx02kQz8RuZLF5dt6dBPo0wkHXDqXIuIPZIthxABvJQDVpL9pQ2oqRa4pNKaKTaXPch9Yg5fTtZmP3hmiVymJJmc1NUYcie7WU9ySpYpWTqYecHpZXeCSde2SP2CXjWKdDOTU/I2SA5ylXDZotKhQkqVrnL/GWF++Ip9HeNkO2V4WgtkFIgSbvYPa7ZCtME00yHBuVAQSd8HzPw2mPcpVejYi4dohjYwjFWUYtApP7wWQrNUQwa22vfCzZ7a8H0Wt3CZetPSSebP10sHy3vROODQVH5IbBaAvVLaznZwP2ai7gZWS5tpiMJ1weU5AsTDStdMNOumew5mwstx5XlNRCZmhokBc2BQ+tzIhyZeR6hBoP6pd0kYEAQ5QkZ/Pat08dfOVvTncnFWRirTPSAVSOwr6ymA5suKrbVLeTZ55M+64ds+3Y1SpC1BXitWTJ66KZ0VtoqNcedOH7fCpciN16BntpD5dad8IDKPansgCBFPsnh1ZE0kgCz9u0wi4U3MsOh1erfJnQuLBihnGtge6ESf0LP2nL6ID1rdmig8A3BC1lFySxoNJh5dWYFxOkRQMFwzyrbE7GNve08B6aYlxcb+76xAO3UX3cy0w1ij0uHrhMRVL+ug28a3dI1Kt3zJHBQGAKp0CxrFZdbS0DH/Myo723dOpktrQLm1SF00nfitVa43cnto0V3Lmmu3ZdW4ThVQlhHSK3cQ0xbc48u7uulptEBd3fydJsx7gpNpSdCuQQElRMoQ179CqEKqKWMKyxSx3TlhwObU7mFrT+9ytWNLETEXozgoou00Mob4tuc6uoOvREod+OGLVFd9JyInhTZIQNueUJEc9UgxlSqePr892htCOEUFtJqlpyL+H+Lugu7WWwLayobl1WWmgjG6v1HZvKpk4QIz45w3mUCL1qNQgrTsZ5dAenhQ/SFN55jLzedo3iLnXRhmCZaRqYumExt+MvSWeaniIFVZSpEndizqJyU33B09LmisUtMVaTW1LBLirSVtKmnULpmec7IX4K2GgX91jMXxDNZ4htJ+YyLN+4Uyr4V5Ur00N80vSSowAnWrYZCMyYrYortd6JeOfxzGrc+PYZtEcbSjK5PURsRh6/oK0OJaxoeAadOw6Ml31CT+pUQitF1OEK1W5GKxMt2NCSpacR3KB37dFsJOdQNYwHlwh9t8y8OkjrobxAGkVwN69ojy5v+RzZj408XJZczBXRUsZ3UMmohHgy4NshVoksspkc9r1W6k+q2+zQq1fqxWkbVC0RHcnOFU8KqhIlguaXZXjYn9FrNa4s+64nkXxzUN6Mql2JwnHgaKtiYw7H7dq2h7t3MhzDROnxjphBZ9w2fTdCSGq6LuvxsX3EeOsal1Z3WeVMOaAbH7V4QYEjE7dWHb725bih7PrSKZ2IbKSjQt17Dz7zye1MTFmxwa4DYuo6Z1wzsl4rORwgfX3mxBiL7XNLYNzxhosZYuJjfRQijm/Rrak4SdYkXlUWSJjCKFltCHW4cNCOKmqowlf49lAd6R0oVxUv+oAcT+Z0nPar8qpSEAWvLSjKUWK9Uu9O6KxokAP+XufgJblM0KMWl5GYoRSTEAV2PHpoVGN3bZPDN+q2d4Sb3Y2ana38ney5mUy6sRC6e5GZXGbLadEpgPDroRsTyAQtxCTsfRwWuLRxwT6B6xSCXd7EjO3Gvh/hg9bU7KbIL4JhOzuw/cKXqy4LGD3Adjlta1u2OnqKEvZwyV/YTRZ5Mp5KYjI5yE5hBWxTw8vhYkWrQg10ZZjkfI1REO502v1SojFGgK0OrG4Lc4MP6M7WiB7kwhr0G1MF9mdaB+suIZOUg1IpyQA/ev11c57Y08rUzxRkjRSldeswDw1axg+mBPeGjEPqlnYOMo85eHszPQ3sI3i03acjDPm41XV30Py0kLevJ+tm3sxpahmi91Z1gx0xXCrcZesh2nQZTpjkE15o7Jd7zztu+B4bAZxEuvRauFAi1r7tk4a8r3qP5uQEycgTejsYe7qUupW0wy8W7bAkp2CKxjEdVFTJ8UKkVZ5i1TXfq4B3z3BiDzpy0XzrKqmEy7GQwggWaiU3jOHchnE7eMksoxtDkEQHDbfCWDM7CrJH3EYrW4ClXrOSLVKzboXZHZYgCTmye4loLkqDsQ3T+pZh74ALoFXKoxTsbi7DOqFRZ4BStodZ3Yqk0wrbppJHxCviGB/4XruK0nnMqFzjbxm8ufGMtc1Vyafpl88v8wnL2znJv/2bh/kN9f+zF+XPd9rvZ6GPAwrXdL4+1vr679X4+fNLZYdAiedb/zpp/bfX5f/5nf+XvzpRm6eMz78XmM9mh+b9rKgx/fmP5F4+jsPng5LHrPlIDXxJ307F53MUxwM/c88LgfJA4PPka1btffjXF+wVeV2+/P6/AdTiNtdMKAAA -->
