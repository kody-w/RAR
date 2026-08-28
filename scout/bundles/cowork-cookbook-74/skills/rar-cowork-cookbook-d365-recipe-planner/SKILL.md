---
name: "rar-cowork-cookbook-d365-recipe-planner"
description: "A guided planning skill that turns \"I want to automate something in Dynamics 365\" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_recipe_planner", "rar_sha256": "1c3b4425cfc86a5c3d5250975e457e3b2a96017af042f55656e0590b20e8d70f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_recipe_planner`. The original RAPP
agent is preserved byte-for-byte in `d365_recipe_planner_agent.py` and in the RCI capsule.

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

D365 Recipe Planner — A guided planning skill that turns "I want to automate something in Dynamics 365" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-recipe-planner
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
      "description": "The input to convert \u2014 path, URL or payload.",
      "type": "string"
    },
    "target_format": {
      "description": "Optional. The desired output format.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_recipe_planner_agent.py` and embedded as the fenced Python below (sha256 1c3b4425cfc86a5c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_recipe_planner_agent.py` first:

```bash
python3 d365_recipe_planner_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_recipe_planner_agent.py   # or on stdin
python3 d365_recipe_planner_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Recipe Planner — A guided planning skill that turns "I want to automate something in Dynamics 365" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-recipe-planner
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_recipe_planner',
    "version": '2.0.0',
    "display_name": 'D365 Recipe Planner',
    "description": 'A guided planning skill that turns "I want to automate something in Dynamics 365" into a runnable Copilot Cowork prompt, plus a predicted cost tier explaining what drives the estimate.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'administer_to_operate', 'beginner', 'read_only'],
    "category": 'general',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-recipe-planner',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-recipe-planner',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c36f119a3c6418a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': '2026-07-28', 'mutates_data': False, 'plugin': 'none', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-copilot-capabilities'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-recipe-planner', 'uses_skills': {'custom': ['d365-recipe-planner'], 'ootb': [], 'plugin': []}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 0.5, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class D365RecipePlanner(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365RecipePlanner'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The input to convert — path, URL or payload.', 'type': 'string'}, 'target_format': {'description': 'Optional. The desired output format.', 'type': 'string'}},
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
    print(D365RecipePlanner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6aZPiSJbtX+HFfMiqVmaAQGu2tdkAWpCQ0AZaqCjL0uJaQBtakERN/ffnAiKyarqq37TZ+zKkpYEk93vP3c51d8WvL27bxEX18vXFAG4+4d00TWJQTdw8mKyLrqjO8Ks4e/D/xC/ypkq8timq+uXzSwBqv0rKJilyOH05idokAMGkTN08T/JoUp+TNJ00sdtMmrbK68nbizDp3BxeFhOotsjcBkzqIgNNPI5P8gkz5G6W+PVkQeBvL/DOOHJStXnueimASMokLZp3YGVVZGXzGWpsazisrECQ+A2E4Bc1VJJAM0AP4SR3ON0IJKiSK6ghKDABdZOMCF6hKaB3szIF9cvXn37+/JLA3y9ff33xU7eGt14YiEYHflICdbQNVHAG/BHBR+UAvZfD6xJUYVFl8FYAwsnz6ocapOHnyd/+du7cKqp//PqWT56ft5fxn97mdyxN4dZ34G7pekmaNMPrZJl27lBPKvBwnjupofPz6PUx87ukopz8Y3z2w0PJawSaH95eCgjBHUPz9vLjpKigPuhF+Pt1lFL+8ONrWnSg+uHH73Lq1jsBvxmFQdSv357XT7Fw4PehSXjX+g8o9ZEEHnh7+Z1x4+eBe7QTznx5PRVJ/sNDMAzbFeRu7oMffvwrsX4M/HOa1M3/SO5PD8ExcANo0xP4j5/vTv55gjwN+pD512rH3P13LIHD39V9njwd9Vey7/7/b6LTJIfZ+O7xPxX3ZxOQf0x++kvb/tWEz5Pw7YUBKSyCaqyor5Nfvxkqu/7pU/D95qeff4Oi/59ijKKt/LuEb5mbJyGsp2/ffvpU329/+vmnT20Jcw242be2Sv9M5p/59a7nDx58jvrhj3Oh/kN+zosun3xk+uTXovw/1W+vE9NNk+D7/frr5Pf1Mn6QyWjEu9KHC35XMzXE+js//vjyGySFHFrT+vfHsMr/4z8mcuJXRV2EzcTwi7YZaQoyChjB7+OkniQPnqkA9GudjPz1GAfzf4zwiLgIJ7/8p39nsy/+k2anAaSbb9Wdb+4pAQnnl9fJHooqqiRKcjed6EtVfcvdCEAyhWog89WgukIC8YYGfIHU82X8MTLqL38i7dt94ms5/HKn+eTBQfpaGPmnblPwOtpgxSB/IvZhZwA98FsoMy18CCBMIFt+hrbVRXqF/DXa++D7IIHKYIcY7rKhT76Own755RfPreO3/EGYi8mjddRTOOADzuTLF2hJmCZR3LzlwI+Lyadff/s0+a/Jv5p1Fz7qUCFbPz0OEYqGspvACmozOAwGA4YP0sPd47/+9vTn2Fhgk4DxScLk2RZgBp5B8O5cY7P8MseJiQegU6FDs7Komnuzal4nQjj5wAuVjo9Gno7H7hOAEuQByP3h3gHf8g9P5rCB1TDN6nD4PGlrcNf6i1e5d4gZLGW3+WUir1XYFYp07JXVs0vAyUWeQPd/hP5xHwqpPtWT1buI18luzLlJ6VZuGVfuU0foPuICu8H79Ht7zUH3lo89D4yuuhfAwz1wEPSM/wzplzHmsLVmsNqD+l33fYw79q79vYdVb3n9TG63GkPhQ7KHSsfFwUj5f3+mVB0XbRrc/QeRjpKeUQieUbnn4Nh5J4/WO3n23slbO5+h2OR/73pjNGzJ8zrLL/csM2F3e915OHxcYI2BeazJ4CpgArPuUVzfVwbvvPJOr295msDsqYa/P0bew/Qc86CsFgKFlKHf5UN0EOco957CY0pW1Zj87lv+zuOfoXV30oJRhPUO62F04bvC8ek70hgW9ee7L957+j3kVTBWP0zTSdl6KUyhEIDAc/0zRFWNZfgMIsxnMJZkFyd+/AerJlA6TBsofwJBJLCwINffXbcrHuELYTS+D0/GlRJEEbQ+RAtXsOB1Yo0RgMGsYfnC5c44Bnrh013UZMyCAkL88HAdu+UDzBjrJ8C7pdAVze8D8Hz2PfXvUEb0UKgbuA10ZTeybwD6R2A/YD5DBbFmY7HeJ/0x2k9TJ7/vN39/y+8QPwgfckB6z9DvvpnA2svqO+mOFFZDGsrAM3/GrB+78uujsT469weWr/+00P/h39sL3Fvl4Y+B+zqJm6asv06nj/b23t1eIYFMH+2ovne6L4+LL8/e9AdRD898nfx7cP4g4pnGXyfo6+x1Nj6SEh+Mefr8QOvXX1bOF2x8+pbr4HtYn5wxMm46wNb60X7eh8AeFFUgGgc/2lE9drEONs47/0LHv+UfoX/WBaT3PBp7Z138rl7vfRgG8hGnjzYBH+UN1B2Ma7PovlVJR/g1ePmat2n6+QXyF/iLLcpI/zAhoQPGzQysDbi8gSR1v/pY6owXf9zI3asGlntQfB2L5/OdYD9PPlaYnyfva/77zilv4abnp3F1O6qEQ+HXx9iPXaIHXuDGqhnKEexjIzMuqp6L3X8GMRZNkpftHcl7CT7rrnQbyDkHXRo7WekOaeEGI5R/kt7A9g+ab+NOzP0THcr9h5s+ShQ+S0aehM1pVPuY9CdiodwKXNpx7Gj3d0d+t694GPXb3R/NY1v468s7NzyD8VwCwuGwCL/UY1OcwhyFCuH1I5vgs//J4vA5BfIXXKnAOai/8DBsjvuhTxEu7i8CfI7PaBIHGE6ChTd3aWKGkm44w+YhjhM4AWY4PfPmM0AF5CyE8h5p+G1s9skIY+66PuWTKBbQpEv4YDHzFj5A52hALsbJi5CiAAY98jH1DNnvadvDltFxH+vU0QdPE3998QgMjtxgtbB8fNZT2nSJheTtYg+piHDp51PBSw4XI2hqE82v6Mb2Pd51d4pyniMZxsdOImhnVPeEpXuwK+rQhdBXjkjn142wtA+HnpgH5/C2j0+ZtlSYmkwVmlpx2n5FKOnmdKN0c6isWN9eDyUs9iIOw2t5zIUGLXXFTAQBEFnXkAKqHFCuPa7z7ZDp1kqecvvMw7Y9GLZXpZFEq0NM1+TxSwsfzXIqa06XxXITsWDG6vElGfYDaogJedNck0zoAVvsCKFDPKcQ6eRal7HFi3bRCtrat4g+xo6ASOaHmXuTT40unCTc5JKiLKyhNByu2zHllG5vF6rJ8Yxqc+wqpRnRXLUpy7OIQG176xC7rrdQ4kFCXbwzxUY3OqkNtFINdoqV2s4sSfCNaxKuuz+qC3Zv9uUFGTLnIFvdsjcopaITylzujFJ0bMdLgJav+iwqtmzgZeBsBuItOkrh1hLRXKgXJ54Y+AOsVlfaW/6gNsdanA88bYrVzlm7arJY6+tjfRZuRJNeMqU/JOVxuEa8cubW3YWUqPMghsuDR9jxzV9hq8E6qnV0OMzWJkLutw7J220ouWuGrkRlm+pzBimdNsEPB5fD4nZQ0L7ozW2KOGSGqfGJS/YCbZ8HN+qrHSl2WblmjP0B2XS9FhSospzX3HyWDjukWRpnxd3zWqnfakc9XA8WEgr6aXHlkQSLgRWYHUETHSKgPu7VUknLmWTi4kW+ybh66MgNmqwTkz9Wg086Atn2TqFEdMutWZM4ZoooJ7uQqk3ubBfhoB/JUFK5MJd6S45VtRYsHjHjJOwqfI5EKVWHzoE6UUizMn2SLQdKUo6k4nDUEbH1Uz7H87iRrNtKPaOBTctrPGTsQ65sN2qP4PvSuC5jpffVrgvjJdZTF2vHCSCfYkCzZxQyzW1C7gLedMtF6R/4fRoGSav7811VFKQ7ALbO0fklQvcO6Yg3p6aL2Gf43V6+JoXvJep0EZ1q0hrYRZKc8eNso25Dv5v6WWYvuaKNK3lvrY/MulL4+VKMFslFIAR3J+RCRrL6LKlVli/0vQyr6Azr85jrqbJhb74ir2TH3lOZrXKN6nDzGz3QBUJN/QA5eb4v2Q3bXNpQpMsEPxGXo0YufWZnKu4Ol23acraEihFbfX+VSKzigE1d0B5UEM461rJ9LeBtzplprq42p6NlrbrmyM+YivcWVcbE6z4D8TVaoUcT69O6sA2uPYPUzg5cP+gSazWNraz4lVLreWaRtS9VM162wNUnlbMsFeTeqs7hdpZpXMmZ7urUokPbnPPKv6yoyjsaO3NzlGI0mqkJdhDWhHQwyAKEy2MMVvXWnSu2ibFhW4a922ZCsU8ASrXFWTuJfnU9a1eBMWUHUY0uVceN1haPD7e+q1wtNjViyyPZ3mJqWZwlEoCUKTpEsN/a6QHbL883DJgWD6dhlLumhsHLicHFqXDYXQLjvLHVmzBDGQzF+ZMzzVEnN9Y4v8qOpugCkfQlhbxIR/W42132oOa7jd5NL/SV6nFsU+6dzrlsNu4tMozzqsoP1mXLzR1muCwR0llE+Xar9wITV3bd8bobDfomjy9kwTqtFGn5gqrqZZ4fj12+WZ2veUWJGSAPu2NYUaUxOBjhLJMcUk4XCbwrqWqkyluhxZKeTxPC8w/RVvH1eGMl84uH7lT7eC4uDrMUTR5l8VO53HKDUNOag90q3y8NhhVm615MtVkZIu2tS6enUzW1WE5o5gfKUqT9XGYMUlGZkyfm2dBnQRB6KTUSLEFdN4Z2aIMDRkwJ1TAOx9IevOM0nxuyuNzs+Pg4tSlq6UuldL0qqqMtT4mn5hcKXE8dOd2eEHWzYW6ImU/jJeW069UpxvGgNbROEFZMY1zOW0+a6xfuqMs0f0mxoWhoQk+43twnQXlc9dfo7Duhap9mQK0ij95tcnore6ZlOINqXBPZMDXdcJlKN5dTNd4Z+hCqxinKjxY6gPSazfrW5I4DZkZ2oOa2BeYnFIE7tEp0stqio4WFnFH1jOlnU9WW22XlC361qLS4dFbxoqZsWq96A8wzcE16P6U7pso7hFyX8hl1OVLyZ4IOUzJcLd262ctgIMR+gfURGMiAwresWa6vctP3tz1IHcQue5XIJZYlVjehrqfcVkclh1gEAI21aH4UnahFaxJlLgc26bYii1KFM+c6fbk5JfnUWme3kjICQV1URLWtZyp17pk42rjXrKrJKEbT9SUfdlqx0DhxqR03IFpGrBpRWxEftqapH69Xps+2pwMNTNRKfJKreGcnTyGgpGNZeooh7LFpqHQ/PwuJR65XKaWhqRtnczJqWENkfdEztjJSLsRMRPxQW8zwaoavMaDIkj2Xr8fkcN2xi505mP2lJ0whOvZqf9kJm73i9rmvKosG3VziZmYpmza9gVxX9jPv4rnD9lD1Sxl3Lg3fhLiwxoy5uiTQzPBnBunsyEgjREsoCg2ANSGibrq9RUJj7w1MSUsFD5HZ0dCOxdKZEdNTp7nCjS6At9eHzlSz5dJL4jNKosjVzdm0MXWjpON9ny2Q4Dplg10bLKJ2YFthY81OQbwWCAbNJcPVERsMN5pcH1W6UYOTNHOU41xuEFQPh1yzBxFyhAmayxwT+DW7jhmLwHjc9sytouc1g2/O8tGNucI6EapVDd31svU9I2JOJqEwnn0umzKVlSukKL3b5WnpHPk4ivA1arbmjp2RwjpwSGON8bsTetOkhCskoqzX2FGYetAfvNyZl+pIpVrQHksjmXHp+pSrBEVwhbs+ag2/Hlb1ol6InrLb2kKF63LNcuGRlph5tDwS7VwWe/iA5nrNa1bYdcYNV/SkHW894e6K3XhCuWT9ummcjWxEyZl3iC193MobzAgOfqpvK70UeUaFMNtyHokoN9tuSroMlTpamTuNz/YX5swcslN+mMXNQY6EJAjZoJIX06o+7qipdPRwScajrVMtF455qm1uXTCeIm7mvKQq6JZtQicz9AwL3F1zQRxla9yKjeWXONvF1gLjNJHj0ExIrhWJnds+GHLEM+aBE3uHvSCkOWvS3XpotJRTvUN5sqSsdxWSPHeF1ixNEx+ucNiBJ5iKw0/Nvt7ViXtk8cswFInXnebTObsid5uAt/ow2megYwVdvLjJxqSj7YUvNEtaBzfVRSXEW++C5R5nIkHAiUjXfDHgcG0jWbiKKaqV9Sblz5at4Kfa2qFzUiKuUnuLrJqRg5BrCtpzpBJEU04teMU3z/k+FJ12u54naJEQGBAqhtWUvGHLI9t3RHRK1miKBccjSVNcuWfBGd0RuKmwOoHuBb8EN0IyzjShSBtbZ4GzwXZLrWxneOsL+oq/MvzmJvKYpEZCFHCLfbgwBkLZurd8sRF3a5lNlVWci+msJNtskIipxQ98SV8kUj9XhnhedtfTIRZB1ClrO9+AaSFj+b471h5mLzxHXm/XpyLMuSis7QwXCzwMWiFSb2vOQQ4R7VcdkwYmeskws7QALsHtGzTc6kq+s8pq0e3mG7Fu40GYrZyL6J8QqS/gmpJpCtl1EgIGaOG2GFl74aUcZrtAsK/JUuDh9gCbpfue6/FV1hTzJgYb7YrvsqwbcvfiViA5FdSBL6bANG9X5lxew3BxMMTaZ65Bm0qlbe/AJsKuyFDIUtmQ61saTzeGHBzkjRMRxJR3Q1cng1KB3T5b3VRtc14OpdfOWqWNg6EnZolb+dkiVGW5GUI83xIXMb9Ndzq7YzkFKKtT5nD6sQlRuuPmtpuGIn9IvSVDG3hHLZFqQ6m1E5Lh1pM39JK+zpf1fnYQ82GKiglB0rYyXOu5nDSyejvvmEHyV4CLUZFQVGmK4ACE1FJdp/w2pe0psrUxAgG3gETz200jQV3OKbE2kIPdXLwZtlb7MNCpVazpiA+m5z1SLDGC2TQWnlrxMu3mxXm/ySRifTDAoe3YzkqFadIr+wixiKPpKXt6gOv+2RRpeJ2cb1azNXrYb1caPcevihPgelwZe3ah1Zc6ypGI2MH2TC7aKJSSa+vdhj3CTGFnKziSFaQ5puP7W31tW+2KZVg6t/pytar2DaPcmnPogVU3yB7cLdA+zc/qm6ojysnxK2N6Syp0OrVUZXYUdowp7bPlMVmLJKXuSUzSr8oNTJ3BWdcH5croUVVqTVfHZn5sdxWJ2FxtboLrruDshij8vltQ0yXllb5aH9Dl0iZjs0aYOIw1e0utBYB3Qu4YmKvZtZ7QzjSr2haB1c/iEjsNY2SrXLYX+zJn2alsG/IgktvdMldjw5lpktvLqhLZrBEm4VlS+RbrOwafMakVWdeEQ7GDFYamRgF1Uxziy4bU1mZ8OXBnJm/cMKZOUcTFTbQ8WUqO5drZonPdoVmFowGVmdwigytl9kZSyq08rymsSXvqQFyr2lovWBvcrptc128ypnJF3B5uYSsIiHhyir0tuJuu6s5Wj7CEUu3Fhc8T/jFcscrWX6hOBrbbXR0ooA4LZarM5JIMOs4cZh6xgPUmAbC9NfSF82dcM5+dXOLmiAoMdeFnrUsnsEaEQtZwlBQx90RARvI6Z1TIF8p6u2jVvUsv5r0QLYc67GK0z0Vsrs1oVa+G/bZ2MzAj6tWekAImB8IK0+fIDdusbrQbXE8IoLGaIPEFAAiBZPMFIVsbsCCoZkvjmkItEGnGw81hEJ4Q1putC9sVPDYMja5BZRVsFJxmrl04xUzH6iSEqlp5EdzAqdZruF8tsC42y/PAiuQ86BvEoEqG9UzZEmaBjAa32O5CI0d2jLZbicoa3YUcc8OwbREXs7ayAiUmqNMtGLwFerzwpGgjpk6igaRJNL1iVWKzKvou1FzPOAjs7baxNxlTBPPj9tI2NwuvlKbZLZqyJRVCNtvLJuNLPkAXmU/vRXLNdARgsPLiUvx1iMsz4whsFW99ae+wx0UxFEM2PWSzdHeiMHlINIbB7WZ+MZhzQ4pW5KlUTCh1dwFNDvZSuFpIQ7eSiuvCyJmQF6tF7WcpsYh7ZqNINNpquB3UuAF8Wmb7ljoL9vEicHYAFzM+o13NawYu59Aic9W/lWmkqsugEjt3i8KW6LhewQjWOvdoe2kvdAFup/SgL6dbZHOGkcl2237frjgaL6UyUPWwP9BKd5GL5XL5j5fPL+OJ8vNc+F+9/R0P6/6/nRk+jvfeXwLdT4SBG3y96/r6L1H8/Pml8pMRw/30s07b6Hlw+N/OPr/8yeuCccLweG06vpHqm/dz8caNxr/meUnyoK2bavhWF2l7P3D9/OK19fhnBvX4lyg+/H65Q8/K5tv9FSK8LGBTHGW7QZbkyfha81tTfHuc9YJRAoiS96NXaOa3Ik/vhjzfNownpuPrhpff/i8xk3rwYCUAAA== -->
