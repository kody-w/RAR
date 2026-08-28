---
name: "rar-cowork-cookbook-adaptive-card-define-sales-teams"
description: "Produces a reusable Adaptive Card JSON snapshot of define sales teams status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_sales_teams", "rar_sha256": "e9d2fdee0e23f11ea0dd78755b00ee5483b764703d626c4656cfe141ad7ced94", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_sales_teams`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_sales_teams_agent.py` and in the RCI capsule.

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

Define sales teams Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define sales teams status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_sales_teams_agent.py` and embedded as the fenced Python below (sha256 e9d2fdee0e23f11e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_sales_teams_agent.py` first:

```bash
python3 adaptive_card_define_sales_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_sales_teams_agent.py   # or on stdin
python3 adaptive_card_define_sales_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales teams Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define sales teams status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_sales_teams',
    "version": '2.0.1',
    "display_name": 'Define sales teams Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define sales teams status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-sales-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27763364487f6cd0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-teams'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-define-sales-teams', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDefineSalesTeams(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineSalesTeams'
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
    print(AdaptiveCardDefineSalesTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abPiSJLtX2HufMisUebVLlC2ldlDgAAtSGgDVFmWpV1C+y5Rr/77CwH3ZuVU93S32Zg9cgGhCA/34+7HPUL8/mK1TZhXL19eVM/KZlsrSaLQq2ZW5s5WeZ9XMXjLYxv8mzl51lSR3TZ5Vb98enG92qmioonyDEyXq9xtHa+eWbPKa2vLTrzZ0rXA7c6brazKnXGqdJjVmVXUYd7Mcn/men6UebPaSsC0xrPSelY3VtPWMz+vZl5qe64bZcEsymauVYd2DqTUn8ANK0rAOxijTZNegS7eYKUFEPPy5ZdfP71E4PPLl99fnMSqwVcvb3pMaqzvi6rTmvfZYHJiZQEYVYwAiQxcF14FFEjBV0DD2fPqY+0l/qfZf/1X3FtVUP/05Ws2e76+vkx/lDabNaE3a3Krbjx35liFZUdJ1Iyvs2XSW2MNgGnaKpsgqgGQWfD6mPldUl7Mfp7ufXws8hp4zcevLzlQwZpg/vry02T115eqnT6/TlKKjz+9JnnvVR9/+i6nbu2r5zSTMKD167fn9VMsGPh9aOTfV/0ZSH041Pa+vvzJuOn10HuyE8x8eb3mUfbxIbio8s7LrMzxPv70j8Q6oefESVQ3/5LcXx6CQ89ygU1PxX/6dAf51xn0NOhd5j9etgBu/XcsAcPflvs0ewL1j2Tf8f9vohMQVvU74n9X3N+bAP08++Uf2vY/Tfg087++rL0ExHU1ZduX2e/fVHmz+uWD+/3LD7/+AUT/UzFq3lbOXcK31Moi36ubb99++VDfv/7w6y8f2gLEGkiXb22V/D2Zfw/X+zo/IPgc9fHHuWB9PYuzvM9m75E++z0v/qP643VmWEnkfv++/jL7c75ML2g2GfG26AOCP+VMDXT9E44/vfwB+CED1rTO/TbI8v/8z5kYOVVe534zU528bWbAwU2UepPyWhjVM/B3yu3KA7jW0cRtj3Eg/icPTxoDQvvt/zh3yvzsPCkTtp7M880B1PPtQXjf7oT37U54v73ONCA3r6Igyqxkpixl+WtmBV7WTGsWlVd7VQfYxB4b7zPgoc/Th4kRf/tnor/dpbwW4293Mo8e7KSs9hMz1W3ivU7WnUIve9riAP73Bs9pwQJJ7gBt/AhI+wSsrvMEsHgzIVHHUZLM3KgCZufVeJcN0PoyCfvtt99sQNRfsweV4rNHgahhMOBdndnnz8AsP4mCsPmaeU6Yzz78/seH2f+d/U+z7sKnNWRA6U9fAA3vNQXkVpuCYcBNwLGAOO6++P2PJ7hATAYqGvBc5EfeYzKIzdhz35BWd8vPGEnNbA8gDNBNi7xq7pWneZ3t/dm7vmDR6dbE4GFeN6CCFV7mepkzAqkWMOcdyQyUuBoEYO2Pn2Zt7d1X/c2urLuKKUhyq/ltJq5kUC/yBPw3qXkfBCbnWQTgf4+Dx/dASPWhnjFvIl5nhykaZ4VVWUVYWc81fOvhF1An3qYD4dYs8/qv2VQYvQmqe2o84AGDADLO06WfJ5+DSp8CHnDrt7XvY6ypqmn36lZ9zepn2FvV5AoHlAGwaNBG7lQM/vYMKVDp28S94wc0nSQ9veA+vXKPwfVf+wD10Qf82EB8bTEEJWb/HzuNSdvldqtstktts55tDppyeaA49UYT2o92ChT9u+R7xnxvBN5o5I1Nv2ZJBEKiGv/2GHnH/jnmwVBtBaBSlspdPnA8QHGSe4/LKc6qaopo62v2RtufACp3jgKuAUkMgnyKrbcFp7tvmobA0On6ewm/+xHABzwPYm9WtHYC4sL3PNe2nBhoVU259fQCCFJvgrYPIyf8waoZkA5iAcifASUikC2A2u/QHXJgJoDZr/L0+/BoaoyKh1PdGWg+vdfZCaTHFCI1yEnQ3UxjAAof7qJmqQcwBiq+I1yHVvFQZupXnwpaky/yFETtnz3wvPk9oO+6TOoDqYBSG4BlPxGs6w0Pz77r+fQVUDadUvA+6Ud3P22d/bm+/O1rdtfxndNBZif3mP0ODgjJCoTkRKUTMdWAXFLvGUAgEu5V+PVRSB+V+l2XL39p0j/+e338vTTqP3ruyyxsmqL+AsOPcvZWzV4BLcAgRqLCq98r2+ep/Hx+JNjne4J9vifYD3IfMH2Z/Xu6/SDiGdRfZugr8opMt4TI8aaofb4AFKvPzOUzMd39minedx8/A2Ei1WQEpfS9wrwNAWUmqLxgGvyoOPVUqHpQG+8UC7zwNXuPg2eWAAbPgqk81vmfsvdeaoFXH057rwTgVtaAtd2pMQu8acuSTOrX3suXrE2STy+ZlXr/fKsykT0IVIDFtL8BSQPanCby7lfvLc908ePm7J5OgAfc/MuUVZ9mU3v6afbeaX6avfX+981U1oLNzy9TlzstCYaCt/ex7zs/23sBe61mLCa9Hxuaqbl6Nr1/VWJKJqAxYO560uUtO6cV/yIEfAgCr/qrEOn+wUqeFAFYfCrHUfOW2DXQ0wXNDSDvbko4kEOAGlsw4a/LgHUqr2xB3XMnc7/j992s/GHLH3cYmseu8PeXN6p4+uDZAYLhICc/11Plg0GUggXB9SOewL1/uzd8zgfkBnoTIMCjXcx3PQ/xMNxHUc9CXHe+mJOkjSCeRxIL3J5TxBzBXQqjHIIiKcf3UAK13DkgVpoA8h5R+W0q79Gkk4f4Hk6jmOPiFEaSBI3OMYt2LWJuWS6yWMyR+bSi+31qDJjxaejDsAnF9zZ1AuRp7+8vNkWAkTui3i8frxVMGxaFC/YhtKGK8pf1lY6bgTfOV9vVNWfuKkiWkgg2dzRzflbU9bFV471q7cNo1fAy6vEXGVH9OoYGfF2vKpb3m1tNSiJGNJvFmuntZEHe2iCIVheZNatMbULTsuqS05zTmTVHq8SIaDQU69QlWnQ21QKCvCRb6GiBXCtGXiW8YdSmieUINUDn821xPhQei5sFnwrGfr0wbA4nG7VksVovtOwEbW6xXs61CxZvuWzLLakeg0VPT4W+zuK5lGns4Mo3lPRk5nK+oRAErQhdmLs8t7I6gyW4k+HaOlSUN5yvKvsSxZeT6Oq2vGA9djwbYTkIEVekkopmrYyLGjpU2YIV+1ynyjZRC2+3w4LaEHY8E9d2zg+2yAd1o8aDnkpkVjW2YKwZizTKs8GFnqlaVN9ehca9ahYlZOzey7r8qp35wiXzdM0PIoOI8SLz2Pku1eebUxkjSR0b7n6/MWHc6bllTznoiaM7xjse4wRvVcFaLatuXXG5z2Vh66wXpptg9llzTE5FdcKgzKhEciNKIbwOuSQzaqVc3ByE6R1/Ua6GzZxp2jQ+WDd3rLniUueVEWMq7KCSURadq1QmzwQARyljtvHB0XgjMW9OLxVk2RCENrcpEKVL9agw86YfXX4B743L3F3saroSOWq84Ob2jPmFOQS7y+noj0a0Xly2WRcbqFnf9Dnp7XeZZiDpKrloRLGHQVteD3YW5iRhO8P5KuPsWJ6ObZbuhbXfDoO80Z0sKi5klDS8d4QcKKxIMzqhJ/asEqeVSouwkPeiXbP7eH8eIyq+UQi5jyi3RVXLGauDZJ6pS4GxScvjgA3OxPJA8Boh7oijLMp8ooVHtpQXO5G8yR0ctnAAomykdRLNOg9BUpxoCAEbVKrkxwgzeW7t2XqK5k59lOp0OyjDcN1yrUqrXkPjCMaxrWkPx2PPFV7ccMPIZZIBM0MWHFJhb4+rBHRc7IkMjov18gB2ekWFXFfCoB4GiWJWjGZb+xJbFkGyPw3mzTh5603vjAcS5zNxXdG4nCT4NUpd3dzc8sgRRw5Tak1KdzmD531MjOJlUcupB4gvdhIa3d56ntjiZ4tyDBvP4VHUD0NJRqtD4iedePDqqrXZC3zK+Q1/DeEzGmuGrS0t5yZe0GqFYc31wugS7yUmHBH8WFGH3Wq7m/OsWpa52OwqLFH5XVs6YkIlp8yE7WF19PMGWaNwPmwuvgwPt0IsorbjLc6MQPKevFtj2ghWQW1x2TjsNmHNhS/ZgP9uQ8EVWulaqKDsbb6C0n1JW1x4FCLymPHMDZHl0gnOoqZStZIo7QpEmM+iibfX5VswIp5uRQpLH6Vx6SYKG52QLXnBshvkO+dLaMzHfnfSmJA4jAZ+Ka4MnjqjsgUSFXJLnbauQ6l9DCMo35X0OltTjpfsfJJc8aF2Wix8NDuBsnRo/VTRCixkrjEqm7ezKTp5sJ+LldiKXEOscxhlr2ckSmndPnVOa68xCjqgczipcjkqIWbAxN5Hue1lO7i2WVzk614Ss6OF4+JmzEohGYSqqLEal3l2Hy76U4kLy7PinIm260LpwsgSuVDj3frgy+faFK9sGV3F80LIuBpGVORoLsVjONc5YwwHjTwQxVqHUPPK986qXR3Z/bhHVpeNbbQxthAaa+OvtwtGPiUbfBuJaMQFBZ0rl1t7XfUXMSn2VSXvT80RqW5kOfR4pWXdEtug6838duThQ0hBLKClYpxHN/EoSG0XjZifsYtFJyBBDHHSsE19F75RBcdLqo0MrRs46jU4GrtzpdyWNNzsV11LktcQWi9Dz9e0gYZgebfWbnNypPwqRDKL2Rc+K6jLcex8g+nVfmVfYnN/wa6jkhr6Jj6XNBqn7tItTyEeWaqrnbh2GVmCrt8QVhVBSPE4VypchQ+MsZdjXDu1o7vEuywUEKnvsyKn+csYU4V4VXO5hEWc31Hl1ZNX9XWwLg3Tt9ucka5zSef6c3jdLCEGd9RjZkCDFZUgkY47TTQUsb1lRteuY8op1HSRspVgQhavmS2xYS7RIJoUjSTNjrRLh+u2BqaPRHwJqmrY3eqjjeJY5Wz9TJ8n+ihi7rU/5upBb9RrFNRn60zBMkSmREgoaagsMhsVhqBQi4hcbiIqjE+iIwutTlElR8AewRyXcFkzrNuZFxc9cPq67hWY3SSgDeH6ABogw0epytlgghism0N/aapmGxSOkoyBUVJI7vlbhFc1OR0jm094RQzGA7Vse0BkLFFkeSKiWTrS/v4IBbZRHpbmeFASw/KtaGOsncGOxGDjMZrsp3DiLVKzEptitQccGpj+xjTnhE279hAXp0FSotOF92MXptNLeuHctX8LOy0WwpjCmsEaoVQ36CJNq1NyWdMnFHOjWGnmkaWtLsfWU7Fr2fqR7OchzRO9qZ6gfONm9FaN8AiwlqicCa41j7FPDkvGFha5ejuagpPPczYa7MuG66PxqoJqrLhbzmhya60fyEwwV76bycUOQTjraF+kDqF2277qeamNyEE8y4zOpMEmwZ0DxUedu7JQ12BjVMC0cD6nIToR/D5b5hwfLS4esaexzh5EZbeXW5c2K0cS6SQjIdMVaHhrM+d8dLTyhM/1zU44LJk9Yi47ksSb/rTaMHF5PES55nlbLKoSU1jCyjZXhY2orFe+QmrOmaS1XNvqnNB4gU5Lpk4R43CWLt5li4RrvTRcZnAtsFfaeVoAOFc5QS4yjwzQySgqSpGGJK+gQEGWgbmGtvOkOV6qnIwlxOCUPU9yUN6zVYPqzDpLTcqUTs7SdFLmvGeyAg+0It5WUHEgAg5FW308yFLU4oE8kkV3PN+uy0VmqIvYtEyBDFElxIsQNC7ksU8cmkGJS7Md1ysuOjUHmetresUsIJnRykwvc5hSrrGLSaPMSJqkFPWONeMjHfPZgT/tqPXlSlz3xNzEZCruy1bEa6rTVoPh6ag656h40YmYrmLbtM6gG9WsfEdA/WNIbpichJgzWaKVOESSNDQtmx58ITU496LzkYVfd+j2QO0isUEICjd0VHf2c8iQlYaHSIJUzW7cr3zOMRxNP0d0pOchcyCuJ3adCBtKQVVIX5nm6sCKhq9sQolsr7HdbqQgXMGgHc8KFTORfIQDzCqzYpAkaa0ggr7BulWCKnq6lFmjOYrQEo2Tk3M7CCPCcvEB5lmu74Rzs6mPS+0oWUe9ptUy7SpZhXsSozXCiPSw3ddyH4m4oCqBRsjpbXOuumukek4/JwaRI6UYb0BjoWoeNDZkcdSYNoZ3h9An6Viiqm07IntHytiiYJYBK5OnKl2Wh0rfScxmJEmjNmTxclsUoZwt/EDw1gNFSAvb5FDKtyxd2ZStdPbHsucH9ezXwlHwz6hm0+vDKdoHtcAI1PpIb7s1FF+Xt+28IHX8yGBJT1P7G8xtHYQTdyxbIAuhxkBhq4+X3A+DPbK+ILp3q1cq64m3ElkOx5staQI1uIdqbTN79MzhylLKIQl0Pd6wdXY6Pr8sWZE/BudLbRO2BAc95SrhmmQBF6VX5VBQwI4bu1ZlXlTnUgG0wPZtldr5pouC3W3tNHsQAYswGJncFKJIPnVCpnYxw5CH9Y0qvRXrhyEgrDnY+lEQjcCtniJzzyjYjoFPVKuHFeNA256Sq1omE9zqQmJbLpxsqR2SCnQGbXcZBl3d6PNWQPOBSgKkwoKL52zrhWg6a3Eszvz5MHfc/YYGbKm0mkZm7ea4KLYmt9Dqq5N3cAOK66ZH9w4dld1hTh+SsKOquoL7kdjZvV/uxA5naJ6KqmVgaf5p2Er2TsEH0Yao6JZQ892pTw8Zndiee2TNC1xxlhbtHcWd99iSzs5BC9edLEObHbmq1mrbwfBGXtBrwfJo5Dbna5vepFhCJ5szDy3dbcRqwR5mSZTPZWl1Iu3lwbAXKw10E/lwgeyzaMV7VpLwzeq4GODjMdIWKX08L634CgkxLTNihWI86eyEwBbR9NwqkXcNeynHotLsy117Zue3LOPFrlQv25FN0Jr19QvXpccU3tY7hCrnIdxmftBtIYpizIGL6DaWg8Wcn3exALWt0iS1eVwpc2q1xSnRa+drpRex0wrdca1QXFGKY3N/Z5QS3bhk5VM4nO1AZ2wwLq1n9XLYxBpKQAnaS5XlpvTitsF2Z2Tb7K4bfRFscTZ1MwrLGtI9hfqBokEddHBKwXc3ZfQGCB+X9oXjxbWMe0VSM3s/Yv3quA/tTIxoeFyeJWVbjUZ78mkZiRimN5dzAcG9sF3pLemdy/TkovGSEs2BHIhYYlKVCrTz7SLdGKmPIDRbnT23GNbEelDrg80cFke048MdTjvyLrshuhJt54FsBEZwGzwc79DeU3bMZntA440OOgcCtKYDeiJQJoT9mkMNFRdB2CzQBWv2mSt3zNxpvAWd3XC1vG1sT2gyWVFvIiIaZQPpgtXpPZVrZBx0+8uir+DkxGBbClPyGOx92zT1W2YdZewoc11Q+fnoXvMeddtVx92sa+h1Qberd7e5Y4y0ecUdZJksQd1AKKqpQheRQIaNBV60STu/mCeTuZa4sRl2AmIxu3zurTRx2y/5c7M+b9qIdndupCzXyQWOroifcDykIa7MS8o6RlDtQPkQWzSHLmS77RKRSE+BdgGzaLc2LJ3ntgClFDdHb6eOWui53NxuPWVcb8cDtXLE7gwHpQWHKDsnyNw0UQV256DGszjY5Q81fkAkmPHhjI3wZT3HWuLq+moyjpsrx+LhKt0z1x41sjN+kYmKRbwrFS6HU1WlQrfnIYFQ/SGymJzjjl5VEV3X7QZl02yzg+94Q7kYb/MN2FxpnkAeLauCsbzFmk0q8UcGPhKNJK6t9ZJSQyYl8wvhEPRaugkGemi357WNNgVENwfsWoSQgF6i/rC/tRB9y0pFvvTQTsshwUq7Zes5nrnEVgxPqBnYNzKSTZi6afil5mlpuHUltdTWu7G2104qq1VRWYBb2KwltGtF7Fj8SscAA3rcQKuxTbwVBM81Jx8OQoJlJSJdTjTaHU3br8mT76z32wHuS0DrxR61nbTlZO54NTpMTRGIIs8Xoi/QhSQv/ZwLvOqWkMdLKRRsri4zmzgxO1jZn3VPcckC5k98jHediczXXNHZZ4Uiu3XpwktfEU7t3ljFy+Xy559fPr1MB9DPY+R/+eHwdLL3v3bA+DgLfHucdD9C9iz3y32tL/+6Sr9+eqmcCCj0OEStkzZ4Hjn+tyPUz//sIcQ0e3w8b52eeg3N22l7YwXTb4Veosxt66Yav9V50t4PcT+92G09/XKh/vY8rH65G5UW08n3D0Y8btSF5zTfmvxb2eaN9zL9umB6nOO5kfV+GTwPlj+9uCPwUOTU33CK/OZVxWTs89EGsBF7RV7Rlz/+H0NpFyGWJQAA -->
