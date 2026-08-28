---
name: "rar-cowork-cookbook-d365-prospect-to-quote"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Prospect to quote end-to-end process - covers 6 L2 areas and 22 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_prospect_to_quote", "rar_sha256": "91e83da851e5caa4ee2fb1f242e80696b4548a49693c2744b68a325567a04842", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_prospect_to_quote`. The original RAPP
agent is preserved byte-for-byte in `d365_prospect_to_quote_agent.py` and in the RCI capsule.

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

D365 Prospect to quote Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Prospect to quote end-to-end process - covers 6 L2 areas and 22 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-prospect-to-quote
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_prospect_to_quote_agent.py` and embedded as the fenced Python below (sha256 91e83da851e5caa4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_prospect_to_quote_agent.py` first:

```bash
python3 d365_prospect_to_quote_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_prospect_to_quote_agent.py   # or on stdin
python3 d365_prospect_to_quote_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Prospect to quote Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Prospect to quote end-to-end process - covers 6 L2 areas and 22 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-prospect-to-quote
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_prospect_to_quote',
    "version": '2.0.1',
    "display_name": 'D365 Prospect to quote Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Prospect to quote end-to-end process - covers 6 L2 areas and 22 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
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
        "upstream_slug": 'd365-prospect-to-quote',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-prospect-to-quote',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6bcc88d358dc10c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'prospect-to-quote/d365-prospect-to-quote', 'uses_skills': {'custom': ['d365-prospect-to-quote'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365ProspectToQuote(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProspectToQuote'
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
    print(D365ProspectToQuote().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9VaabObyHr+K+SkKuOJ7CN2hG/dqoCEkECIXUIaT9nsIPZNAibz39NIOsczmZnc3Kp8iWyXBHS//a7P83bjX17sro2K+uXzi+7bOcTbaRpHfg3ZuQcti1tRJ+CrSBzwD3KLvK1jp2uLunn5+OL5jVvHZRsXOZjOQKsht7PYbSCMJKB1nNu560P/BuldWaYDtIzsOIckO7dDP/PzFvL70q9bqHGL0vegtoDayIeUumhK322n66orWh/yc+9TW3wCX1BZF67fNNAnoMnVrxuIhHYoZNe+3dz1RVFoh72N8hsoqIvsLlWKXSC3CFqI7Zo4n2QoT1lLu7XTInwF9vi9nZWp37x8/unnjy8x+P3y+ZcXN7UbcOtlBax6084o1Ek3MCe18xA8LAfgxBxcA5OCos7ALc8PoOfVh8ZPg4/Qv/97crPrsPnx85ccen6+vEx/tC6/69kWdtMCZ7h2aTtxGrfDK8SkN3tooNpvuzoHdkINiEEevj5mfpdUlNDfp2cfHou8hn774csL8G1tTxH68vIjVNRgvbqbfr9OUsoPP76mxc2vP/z4XU7TOZcpAEAY0Pr16/P6KRYM/D40Du6r/h1IfeSC4395+Y1x0+eh92QnmPnyeini/MNDMIjT1b8nyYcf/0qsG/luksZN+7+S+9NDcOTbHrDpqfiPH+9O/hmaPQ16l/nXy5YgrP+MJWD423Ifoaej/kr23f//TXQ65eS7x/9U3J9NmP0d+ukvbfufJnyEgi8vKz+NQRXZTup/hn75qivc8qcfvO83f/j5VyD6H4rRi6527xK+ZnYeB37Tfv360w/N/fYPP//0Q1eCXPPt7GtXp38m88/8el/ndx58jvrw+7lgfTNP8uKWQ++ZDv1SlP9S//oKHew09r7fbz5Dv62X6TODJiPeFn244Dc10wBdf+PHH19+BbCQA2s69/4YVPm//utvwEV3i66FQIDbOPMn5Y0obiDwd6rt2p8gKwaOfY4D+T9FeNK4CKBv/+He0faT+0TbuQcAZyqSO+J8bYuvdzz89goZQFpRxyFA2BTSGEX5MmEqQFSwUln7jV9fAYY4Q+t/AujzafoBAej99ucCv97nvpbDtzuGxg8k0pbbCYWaLvVfJ0uOkZ8/9XYBTfi973ZAbFq4QIcgBqj5EVjYFOkVoNhkdZPEaQp5cQ3WKurhLht45vMk7Nu3b47dRF/yB2xi0INHmjkY8K4O9OkTMCZI4zBqv+S+GxXQD7/8+gP0n9D/NOsufFpDAaj99DvQUNDlPSCKsJuYB4QEBBGAxN3vv/z6dCkQkwPiA1GKg9h/TAZ5mPjem3/1DfMJJUjI8YFfgU+zsqhbgMVQ3L5C2wB61xcsOj2a0Doqmhby/BLwl5+7A5BqA3PePZkXgAFBsjXB8BHqGv++6jentu8qZqCg7fYbJC0VwA1FOrFi/eQKMLnIY+D+9+g/7gMh9Q8NxL6JeIX2U+ZBpV3bZVTbzzUC+xEXwAlv04FwG8r925d84r47Sd/L4OEeMAh4xn2G9NMUc0DDGah5r3lb+z7GnhjMuDNZ/SVvnikOWBp45c7bAxR2sTcB/9+eKdVERZd6d/8BTSdJzyh4z6jcc3Bi4D9pELhHH/GlQ2EEh/6ftyGTnQzPaxzPGNwK4vaGdnr4f2q+Jn0f/RpoDSCQhI9a+94uvIHNG+Z+ydMYJFM9/O0x8h6155gHjnU1sFpjtLt84Brg/0nuPaOnDK3rqRbsL/kbuH8ESXJHMhBUUP7Jw2lvC05P3zSNQI1P19+J/p4BtTd5CWQtVHZOCjIq8H3Psd0EaFVPVfmMJEhvf6rQWxS70e+sAsFoQRYB+RBQIgZ1Bgjg7rp9AcwEBXl3+fvweGqfgBZe5wJtQXfrv0JHUFhTcjWgmkEPNI0BXvjhLgrKfOBjoOK7h5vILh/KTA3xU0F7ikWRgXz/bQSeD7+Xwnv4gVTbA3H+kt8mQPb8/hHZdz2fsQLKZlPx3if9PtxPW6HfstDfvuR3Hd85AGBCOhH4b5wDgVrMHtk5QVoDYCnznwkEMuHO1a8Pun3w+bsun/+wC/jwz20U7gRq/j5yn6Gobcvm83z+IL03znsFgDIHORKXfnPnv09vdDXV3r0Qfyft4ZzP0D+n0e9EPFP5M4S8wq/w9GgXu/6Uq88PcMDyE3v6hE9Pv+Sa/z2yz/BPIAyQxRneGeltCKClsPbDafCDoZqJ2G6AS++QDHz/JX+P/rM2AOLn4USnTfGbmr1TM4jlI1TvzAEe5S1Y25uattCfdjHppH7jv3zOuzT9+AKw0P/L3cvECSArgQumnQ7w9QSFsX+/eu+Cpovfb/XutQOK3is+TyX0EZo61o/Qe/P5EXrbDty3VXkH9kM/TY3vtCQYCr7ex77vIx3/Bey62qGc1H3scaZ+69kH/1GJqXLekHhirmcpTiv+QQj4EYZ+/Uch8v2HnT7xoGntibXjdzZpgJ4e6IE+QiBgoLpAwQAc7MCEPy4D1qn9qgP06E3mfvffd7OKhy2/3t3QPjaKv7y84cIzBs+mEAwHBfipmQhyDpITLAiuH2kEnv0v28XnLIBfoHEB02jEX2CevSAQn3BtG/d9NHCQAMVRfwGTNOngBL6wcZqkMRelcNwhFzaGEgRJ2TC+wFEg75GCXyfujydNfDjwMRpBXaABGInTCIXatGfjlG178GJBwVTgAYj/PjUB4Pc072HO5Lv3znVyw9PKX14cEgcjN3izZR6f5Zw+2JS1c/rIokcyOBUXKU3PS7XWdT8VcTI5Wmf6NLadsHMMzom2TBvqNr4+ZVxzEvKDvTwpiR5Iydxw5yrLcIJoeEpx2cSm3jgtRtGk4i5oT2LiJexJ102OrbFSE9eDWB5F6zRDykNYIvSO087NgZ7NysxrxMDJeToponwf6Ocxj/3l/HTwEO6oOV5eZk3nXv0tYeHZflg2GbWuvIoTE2En2DHOtZpAyeLFWu0Q2xSjtd306Q5hPM2+2tur0cdXVnMlnOqLQUEXYTPX0Rjd7S1e38Apt4gOA17QlWNJuntyhFlnHsbeqDAGlvN8NlfGZubmTkMGDaVYzmJGr+jovOOIg1Uu0WtFmdXZOaQ6clhWe7XB1aNyNh1lsc3RSm099Xzdi8K+H9xrC9zai4YSlSi7zA8aEutykBM3Z+Esd+IWOR1PVqOpFnvWs0jp6dZfkpaaekYfZd5RrNyzXhFN6IwozRcIpuzpczG73Yog2hxYURMOZaZH3JmyXP1ktJEaX6x0YM9wuDVMf1ybXbauBpI6SMjlmoeaXLlJN/Carq4twiPG1dnGrZHQ25rkT4ORFiIlzI/LQHNjROSoXYPUSHQmiHq9TRVrzwSbTd+yznIfophh8mv76h85xPSPB/OEGnPvyG97nDxUvpaeVv1i1bdXFemV7cHRaP/ml6R4oW3jYlGyfGAHht477WwgEQJWKxKlThuH9nkNVufGcmgc6uieL/LORpZiy3UOH2VSvtBrGUHD0NrNl4uqabkbX0nWOZzzsAVyRD8XBF55mnVRRpvgVn0+Uvw6UlCpV3DTzcPyRMQpwvjqDNSbtcDOXVWIirFYGNK47EV4x1EmoXHGVu0uq7WQkCIyiubZPqdyIzaYfW7oWWYg/nJJN4Tfh7MlS4eEeJDY7TGd4cEqX5B+sJpTXCFfXHpDwljqJhWP7fb4UjTL80GpVQPPcTs9imsTlS/rFj7yN+2qXfgyM0bT34/pTRGyDjS+tnfTYhchjUuidk3krxxlfWIEFcvW9UESXL3FdyGjXqrdVkBNsznuUYkUVuyqPG+JaimrrWhF6lgs8MiIeokyYtU8svB8iyF9M1A3KgwXMbkVI/O8xkdPytzFMU+4xYjBIyKXMd5ft8MctfKoW4dprerBbXWjTvNURdUuZa4Dws+DSqxH7WjhOLs2jvFZa8vUOySlwpuXo4wFvm6WfIC7yN5MHFI/mnbAnMTYY/b0fhS3wkFVK99oid5aIiiqyhHNrRk/3kmnXQn8PNPbg9OlSW4c91hH10bMnA4H8QQv5Jkbp2uy8XYLhzyW3lIbVnN1pp33a1a7rUAI1yfbZ2la7VmKt6QrV6absLySZ0cmRV2KZh5rZnpsDpVSaNVpb4pFow8dclQIr7nAcLWtebdhkGQb7FEx252JS4tmEqpqbnLQNvL5eE77nSOb25WzJu1aFc5XwRyia7KY8epJWvsKidbSEd44yriF0xWO4MvLNchntlFp7pwZd7Vky1ta37ceIcMGafc+7JTRjEXcRZd5VBPAqs153moTYiDAnFnW9s1XxpsCEmJGBXaXi9L+tqXSkuKDvGRKLo/alKfFpb4K6bM5m53pCyfwZGxGUlAj5GKlIsqitmxEkc9DrbQbgVvvK1PFM6YjVOe8YOdMEs9nWjhcnV19SVgNj7lT4NRViZqw1w4jd+pXhR4r1TETEzamjf7sFJeLiTRjyIi6tdyDDCpMRbQ39LHjR9f1ElHt6lPHFatqfZLLG6F4SE/wvFsplT5uamLhWjU660RJ2wqyqCM90mHXBC4G8UpoxLEaBZQLU/miRhgxm3H4qjri1KWF10xRqRrG64GCILPmYFlkINxugWABlOi4AxuSfUa4gRgx2m25sZNoa6IjFmeszUfWkkjNLDh4lzGIFqRUzC5kuO3C9dlas7CvnMPZLIsQWjck1DMt+eKH3Mbh1lxC2qRGdGdCTdmde2zD3C4QsdSLWbmWh3wkt+NlqHnF2zcep/pXNLfKRMSbY+lkK/3GBRphwpkNEAdvrZPh5T4uUWjPs5a5ji2dymz3Jp+rU6/Tp35dxqOyOSGSL2c2eWXT8YZV++G42i35ZVCUgll2okpfPYe2HJGKuEj3Nhhqe8luuVqnjsUhO2J7oxokt8nWq/3ZIdqs2cGv1J2L+VVEVUa03azCOOPIskKypb3bNsQGbocYYW+sxuBVe7BEac0MmCS6KJLtOzI603VYnKVOqDZZLJXtcr218D3C8qfTShDpE5tdFyio6yV/XJulsDX26oB3lVEd4oggw81O3LEMYxhr7EpY9ZqkLNFmOnklqbxRiiXsajBK4/06GkmXtVfHC2cwHSUhm0ZN6O3o9IWekr23PWLNWY1Unaq2K6z06lPJ6SixKXqeGxvEZghZ9iwfB9+OWnCJUq03wlxLhBWeFdXlJM71VWauNjPuxu6kuchl6Do5qh6sk6c9HBtxfNxty3RnyqiwbhN9lQhtfnEAJKzk0lrAgq2ecdmCbWx2CwPj0iaNezmOtwNT35jSx1ZH++pQaoa4ulwZTb7CMOxCyFjdJBgpLOPm5OOhTx3bE7e9lFjntWV5kqU2zYmx9HYtBfjCX/EDWExucwB2ibyJ+5D1sNrDwtMtTOOC4Xl6397gcV1sxYWCh6RZ3QzBbC3GtJwbIZPH47npd9yKU8yaGstcRebSsMT6VOf2dqFxm01qZww+Q/bLg1hxFIIYnWzv4AO/s7zUXCDmkAUhOzKnWx7sFThSxbIQykHOYKMJ6yQnESZy0Sqzs9A/VkaBMAmpMkSzHMwLtk3izUGo5j0XJKWEtDbo3s4oZyWrmZUqlMQ3Z0noj9fOsOG1o4LOjACMMlyawollO0YpRFiGRHXqBI0rmnSJc4TZJRof6FvPyQZSxC/7lbO5XfQB3cY2qyiHPJLXIB1ZQ+5GKduLXtKb4p4XdmfUrZBqtzgttbJzS+IcY0seQ9PUQoMxNOAoYDx2lyhomi8IK7+gTJ9JIyrYmnY5zA/4YPho0YVkULhLtXFHW25IKVw6l54fk7E5GMH16AnNwu095ibPhm1Xptued8ywl/mgRFgG13u58MwrwtSGxseZYKhJK+33qAVygGaXdX/dt0riEIl2aclVTR83Btq6nB4VF9JyNpE3FKXOrJMqy5c+U3XGimH2ZRLs1kExl7nwIKSNLRWRvtUUkUd2lWZWa8dJkCU9EhmsnuKWV3Nfo8IzXwsXsfBh8lA49qE7nJceQrHmhfEMQiBNNODcxejX8/CQZSTTJVdeiJT9TvUx2fdGeGvK+boUWCZeK9GxzqRKqhse4bmB2Ndu7m/7nFjxlgLMAsHepVh7JpE94lx92wyzJe9vlL07q5I1esoILSvstvMEVLVnqnT04swlCpmtB4pJDAs0l1VY4dhOk26BrtEC7+Fpxl5iGPfTWSkSLLm8AC5U5TlzFJYbiWD9k7c6VxzTq6MjH3aU7u1r2uG3iCVgGiMWsyyhomPYuZsAQ8dQPCUR1/WMEzUkvF4RHs95hZwY2RGBZ0ljm7PmxOlz/CY2Inr09vOLg1B+BVrSjOjgtacfep3ZzteCU9ne/uIoh2xcrbwFSkuRb3ckxW7bW9m16FLuKdU2BrKa1z6117JgxI6DcO1WV7/rqNJyBZ8K8etsKGGqpqnlmEbz3OTo0DUMmXal0QgPGlW35sI+3Cxtzpa9iKAWmnbHLPJmvWOBbsTNV2w0RvODsRcPVa7xRj+/2Wa56FdNmOqJ5zvYzYmvpeOY2TxsVWtULKtjA4/Wdcyn4Jy8BuG82W/acIt5m4NXUTVnL+e+hx5SAr2dk4ufGSHG5C2PNZTq1Df30lMpPZuHyXy7Fs7qwT/TnRTgoMEbJAo0E0hg2VIOlygnlALJHvoVOkoCtu5hwb+ES1r22Z0tSPksUuB4uQmV+W0n2zeGlTPkEm3ts7JVRAZjG44dNkRDhC61HAydaodr58UhX3pEfoaRTYeHCFvfDhKOCNTO9ghtzJhWPJ43upCmi5VrYux15cc0VewGnDZu87l1VTHMPc84ky80H1tuhhHMrJPdte6kq84va1Y+zTVfpc9gdx+ezHATY3lgrYx2JoSI0lbYRoavC6ReBHPkcuk3QxiTB4FiJE3g6FExHFxkr/LYzU+Ds6xT9LrS4l1Vk33q5lLfBvKAt3RBlwQWHmSsisbNqh3psUfTxaw3TIYNstIacWk9I3pvFyq8kzMxPmhkPYu4HXfGdpv5ZQZzW1CkF0LKnWQPqy4mDISn9QAXNn10PUobPjptwrbYwjTF3k7CyF+r6pZSl1pWckZei3262NqnSNsjc06hcWmjmVrM0+GsYigOjnaOQxL1cNtu2ZOprmJh52VHNjJwb60gujRvUW7RHtsR3rlz6RoKIu+wV+k4jHa18WivCY+Ufh68BCZF9Jyzp5bbD51N9z11ETWZQwZSccXFZX29RnJbIYOLyV3Og8RcxcaKgoX6QvmnmwdagIM3W16F0aYj9xq2GzRwMjwjCmyDpg0jsgGcJpi9rqMzLGeihxw6w1N8WEZs2GVVYqTE236TGhWDhbd9RIVgxyb6Vx4wCXF1uJhZif186SXXLOEs4SYpJVd0g0OGRzrYrBrUJ24hFjH2LrherNXtejxSzszJR2fXDQRCIfPMWog3azN3iHkrzoiQp1VjfTWaAUF8wjosbu3SOBb0lrKukd3vEVsx9G4k50EYzG+65sUWPYCEbB19PZxOF2KNRctsy176w7HWMKsD1Yjvtfa0OK0O6Jhip3WwnvXKrd8zCz7Zbg7IwlEUOizi7rKfd+MadqxMtwK59TJHK1MYPWCjiWwSrWovOaPBshMkDF8MR67Qz13syJi8UdNkJPzuKpT2DMP8IaVOBK309m6TbfqLTG4w+ViuvQuLn/asayL7maAvTv6JOa6Yw63l12XDSA58NolDUDlmtL8scGmI1dWKOLQOLbC6BYQ2/IhJ+z5tNgbd2gMbUN1Bd5izxV9ZpfXKPAkydCAvUUBJOx/HcIEPGu/oNGKywiniYFIFnKhNh2zWOVyoVT4fDdFp3RG7nkwSA72tDHO4vK5QugA7DLgzN4zR0qgazIpEEZVt5cKLAdsMZ1Bx3KYw57F2jXvD9lewtWCx8nAiUq5kGObvLx9fptPl5xnxP3g/PJ3f/Z8dIz5O/N7eC92Ph33b+3xf6/M/UuTnjy+1GwM1HseiTdqFz+PE/3Yo+unP3yFMc4bH69XpVVXfvh2Wt3Y4/e+flzj3uqath69NkXb3w9iPL87zld3X56Hzy92ArGy/3l91g8uijfz6cfsPh7BxPr2B8b3Yfr8Mn8fDH1+85xvLr5Pdfl1OBj7fSwC70Ff4FXn59b8AUNNmaqolAAA= -->
