---
name: "rar-cowork-cookbook-bulk-update-qualify-and-disqualify-leads"
description: "Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_qualify_and_disqualify_leads", "rar_sha256": "4d9d15123e39fadb893d5d9afbdc5afe51b3eae473117cf4117398b46327175f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_qualify_and_disqualify_leads`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_qualify_and_disqualify_leads_agent.py` and in the RCI capsule.

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

Qualify and disqualify leads Bulk Field Update — Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_qualify_and_disqualify_leads_agent.py` and embedded as the fenced Python below (sha256 4d9d15123e39fadb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_qualify_and_disqualify_leads_agent.py` first:

```bash
python3 bulk_update_qualify_and_disqualify_leads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_qualify_and_disqualify_leads_agent.py   # or on stdin
python3 bulk_update_qualify_and_disqualify_leads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Qualify and disqualify leads Bulk Field Update — Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_qualify_and_disqualify_leads',
    "version": '2.0.1',
    "display_name": 'Qualify and disqualify leads Bulk Field Update',
    "description": 'Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-qualify-and-disqualify-leads',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ac437cbee3509c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/qualify-and-disqualify-leads'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-qualify-and-disqualify-leads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateQualifyAndDisqualifyLeads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateQualifyAndDisqualifyLeads'
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
    print(BulkUpdateQualifyAndDisqualifyLeads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOi2LruX+Hk+VDdx6wUFERqx464yiCCyiSgdHVUM8+DzNC3//tdqJnVfXbvfXbfuBHXqkwFFu/8Ps+7MH99MZs6yMuXLy+Ka2bQzkySMHBLyMwciMy7vIzBWx5b4Aey86wuQ6up87J6eX1x3Mouw6IO8wzcvimKJHQryISsJokhL3QTB2oKx6xdyLTLvKqgW2MmoTfcZTth9X6YuKZTQaVr5yV498o8BSugMCuaGkrCqn6FurAOIKccPpdNBhWl24ZuB1mul5cuMCpNw/oN2OP2ZlokbvXy5aefX19C8Pnly68vdmJW4NTLFlil3s2RHno3mUN9GHGYbAAyEjPzweJiAEHJwHHhlkBLCk45rgc9j36o3MR7hf7rv+LOLP3qxy9fM+j5+voy/ZOBmXXgQnVuVrXrQLZZmFaYhPXwBm2Szhwmd+umzKZwVSCmmf/2uPO7pLyA/j5d++Gh5M136x++vuTABHOK+NeXH6G8BPpASMDnt0lK8cOPb0neueUPP36XUzVW5Nr1JAxY/fbtefwUCxZ+Xxp6d61/B1IfubXcry+/c256Peye/AR3vrxFeZj98BBclHnrZmZmuz/8+M/E2oFrx1NO/y25Pz0EByA3wKen4T++3oP8MzR7OvQh85+rLUBa/4onYPm7ulfoGah/Jvse//8mOgkz0AnvEf9TcX92w+zv0E//1Ld/dcMr5H19odwkbEF1WIn7Bfr1myLS5E+fnO8nP/38GxD9P4pR8qa07xK+pWYWem5Vf/v206fqfvrTzz99agpQa66ZfmvK5M9k/llc73r+EMHnqh/+eC/Qr2ZxlncZ9FHp0K958R/lb2+QBjrV+X6++gL9vl+m1wyanHhX+gjB73qmArb+Lo4/vvwGYCID3jT2/TLo8v/8T+gYTmiVezWk2DmAIJDgOkzdyfhzEFYQ+D/1NkAht6xCENjnOlD/U4Yni3MP+uV/2Xf0/Gw/0XM+weK3ByB+e6LON4CE374j4bc7Ev7yBp2B/LwM/TAzE0jeiOLXzPTdrJ50A/ir3LIFqGINtfsZ4NHn6QPAS+iXf1fFt7u0t2L45Y7F4QOtZHI/IVXVJO7b5K0euNnTNxsAstu7dgMUJbkNrPJCgLSvIApVnrQA6abIVHGYJADZAZQDinjgPIjel0nYL7/8YplV8DV7QOsSenBHNQcLPsyBPn8G7nlJ6Af118y1gxz69Otvn6D/Df2ru+7CJx0iQPpnboCFnCKcINBrTQqWgbSBRAPf77n59bdnkIGYDJAdyGToTeQ13QxqNXad94gr7ObzAlu9sw1glbysAV5DgHOgvQd92AuUTpcmRA/yqoYct3Azx83sAUg1gTsfkczyGqpAQVbe8Ao1lXvX+otVmncTU9D0Zv0LdCRFwB95An5NZt4XgZvzLATh/6iHx3kgpPxUQdt3EW/QaapOqDBLswhK86nDMx95AbzxfjsQbkKZ233NJr50p1DdW+URHrAIRMZ+pvTzlPM734LEVu+672vMieXOd7Yrv2bVsw3M0r3TOjBlgPwmdCZy+NuzpKogb8CEMMUPWDpJembBeWblXoPSvxoZJkqHmPug8WB26GuzgBEU+v88i0yGb3Y7md5tzjQF0aezfH0EdJqgpsA/hi4wD0DgvkfzfJ8R3hHmHWi/ZkkIqqMc/vZYeU/Dc80DvJoSRE3eyHf5oAZAQCe59xKdSq4s79H4mr0j+isIzR2+QJZAP4N6n8rsXeF09d3SADTtdPyd3Z/RmSIHyhAqGisBJeK5rmOZdgysKqc2e2YC1Ks7tVwXhHbwB68gIB2UBZAPASNC0DgA9e+hO+XATdBh9+h/LA+ntAArnMYG1oIR1X2DdNApU7VUIAFg8JnWgCh8uouCUhfEGJj4EeEqMIuHMdNU+zTQnHKRp1Nl/C4Dz4vfa/tuy2Q+kGqCOgKx7CbMddz+kdkPO5+5AsamUzfeb/pjup++Qr+nnr99ze42fsA8aPJkYu3fBQcCzZVW94qdMKoCOJO6zwIClXAn6LcHxz5I/MOWL/8wyv/w16b9O2uqf8zcFyio66L6Mp8/mO6d6N5AF8xBjYSFW91J7/Oj8z4/e+wzUPb5e8t9vrfcH+Q/wvUF+ms2/kHEs7i/QMgb/AZPlw6h7U7V+3yBkJCft9fP6HT1aya733P9LIgJZ5MBsOwH6bwvAczjl64/LX6QUDVxVwfo8o66IBtfs496eHYLAPXMnxizyn/XxXf2Bdl9JO+DHMClrAa6nWl2891pc5NM5lfuy5esSZLXl8xM3X97UzPRAKhbEJJpQwR6CAxEdejejz6Go+ngjzu6e3cBWHDyL1OTvULTIPsKfcykr9D7LuG++8oasE36aZqHJ5VgKXj7WPuxXbTcF7A5q4diMv+x9ZnGsOd4/I9GTL0FLLbdidrzj2adNP6DEPDB993yH4UI9w9m8kSMqjYnog7r9z6vgJ0OGHteIZBA0H+gpQBSgiD+iRqgp3RvDWBEZ3L3e/y+u5U/fPntHob6sX/89eUdOZ45eM6KYDlo0c/VxIlzUKxAITh+lBW49n89RT7lAMwD0wsQhDqEg2DIYukuCc90rDWxdDCHMD3LsTHTczHEWrqmi+JLBMFtDwW/l8TaQlfLBY7gmAfkPYr024PkgEgX9oAwZGE7y9UCw1ACwRcm4ZgobpoOvF7jMO45gBa+3xoDwHw6/HBwiubHQDsF5un3ry/WCgUrWbTabx4vck5o5mqBWqfempUrzz9n872VaVyJVrcUVp1+He/ME1/FC0xujrx6hE9cSXvUcKF2UX3t4L2X03ODI6KGzfhK5WagMPXIR1peEqluncyIdbA6+iRtzcudctPGKqhgKV6U+MJbGTyXXNfliTustbA8bVkPQ+Mq8SICIea0YqwyPYkDWT1HfL9ql4fwSC6E2mUXF4Q+MEVFtZq+W6QkAyeJmygHteZmnJn0jcwc6kLV1fBAKJpW26Ea1md+u7NwzbxUBJtjx/S8xo8Zt5oLbJ6OGHj3sIHT+soc45uWqJyO2Ve1qTuu3B4SOankAel3wk3LZnxLY+RtaZhs7BTn242jGLxcWc2JL243x5cC/aKZtGJfsGFs+GRMztvrbce6TEHazK7jVcNK3VTLw9PeNlX+BsOpGpy8a6YVaYPk9ckY97PFbl6hB3ulDql94XXUrE7VYeTjAjkwIG7G7nhY0WeOPFe+3cdKEWrNCc/d0xGPUCq+xu6wlc8Sd8EcY6QMGxVHQ6+z9cIcuNTx5yuFz11nx+h56tXRXq2oFZMa4ni+nDqPZQ90UDH6YEXbklrky2OmmGmzO2vcKfMsMtYFAEWxpZNrb7O21ZuEBJuMPhuDs1mUBpqs0HE0VoLrbAZ9eTwgo0LMiHkuX3GnYyqixfeEcSqrjMdFGE5k2l4gBZ3w5VX3cVHbuRctHY9am6C+65w0W+K1QAy5C1ExTLpX1ydWPF/SY8XN0SZMJN+fd/LVJFKB64YsXtMce6TrIBrYcYavWiblzkmZOKNg9wd0JJoAzGvX1R4+pIO9vsE3u+lv9izlPdOsqxjB3PMNjHu6nvsijG/KTvIGKetWzejiAca0jtnlqgjPU+EEz1qKXcn2leUWJVIdZ9tIMcBkHGbWts89URmbqsi1oSVxPR0UGh8qfGDdvdERodpS21tebTPZGuSFVhqkM54V7bqiokybScNsjLgzmTdBeTzr4dVET5fO2Aj17qqBLawc8tsZl8p7e28d+q23UQ+0LA3jyq3GoMuo0GhE7mQFDtuf1ugcJootzp0lQbnAFz8MzoS/4nQliw6wb8ErhZDj4yzNCFYUR03ASfd2FLuZvAszbkdE7TpDdiukypm9ksFXnbmWwzxZpAeklyNUJWnfudGIqeosS89pgc+r/SkzaXKjo6NNdGunvpSl3EfErBOut0MlKh2z3ImOZEhXhq934/wSnsi5ZHFUjMuVBM/ns/Kgbi+YK2RIGDFz65o7mTmMRb2zIi1rumRfitHCKOyyKzhMup1c7VBIJ+1iMFukW1hVp+UUeUDP/YrNeko9p2Jx0nsFu2zOc2Tf7gK+h8c1LlR87hOG2qLHaDiBPdmwcdqFiQGozojjaXAFxlLow8LRSx/WLZgIAiHW056zpcPlcjNoU5MTf6tzJ7JESOuicv0h5rBksWmoolj389NFNtUUN0KLnZX0zrxdDEEk3ItuUsdD1h2Hm7LLQtaLzIt2tjhcLmrTQPCuWW1Rfe3O1mLvmdRiKXWBulsJQ5zUB0vQIk1gez/bySVqHzcjKeXwhV407Mkdj+vcDqk+I+Rq5S98TJRV0evP1+BwxE9+xsIHISsX1jEX8ttYaDOz5OAapmBft7ensEPPFstcvdlplbDnTXCNFNTmBFJiuIFfUHFmaaKQdlE9U4PjkeaSHUPv9M2VYrh6LdOXw47pAMHw2obfOdytGY5wic54rEPxKOgphdH642qUDgKyxUXMtGfYevAR2BgFoZ0vVm5mrDEn47YcPSDhqZrhs5RRFNXOl1wkWqIUs35eCaI5z8blqvcPohWlIn6laXld6Md2Hq3L5S5GBMdbttVqXudsmKzVk0gdeGKmstvDhq9DOQYbeJEzC01SDLe8KLahkqvAwmdcwTOn9QqlubyWKbHTr311Q3g7LfZpThDchofja2MakSaJG1U9dynPmtIZ37vM0VQdFUtz6YKZ6S2mZrqWsYl+7ggx3RWBhdyyy4C3WKammHEilONeQ85ytKx00R7DYAngUtBXgikfsaTxGGqzXrpsv/bHiieJhM94YzkawUiZ+hXH2jzsy63SH+252wslwqRp3cyZUfMHb2FYXWcHZOwrcbLLI44NHbyNnPCwkNlg6GlOGgk0uUqxce1t+2h4Z5jcp3zVjCQe31Z9NAvFio75q5LtTiWFa5tCOrebFUxrQ1EJV1h293jXrjC1UgQ43WzHVbO/aG4UdaTCjUFYMjf0iDauqZKy1uZKGOwyfuOHA7LY9BtpRjn7W7YvNI1JQYHvFULSL7wj5YtZyVd0uqRb8rq25/SwDa4MTcw3s6s1uulJWcT7ULd222QtJdk66BfodqcUxhEnzygTtVaGxeaONxYwkcMcibuzQ2kv9hWHnE8ndb24MYftPF/V51iPBFz3Yb/eMOVSreAti1CBKrtg550HkrhyaE6U4yJgDDdMnZxPBKZuhX5jrlxGUle0YcXsiW50SvETPtRI+niKA2UnI2bCj/6+uOCKLwa9gHkz2JCMUSK1ApnjfrdciYvAGh12v1WJwqflbpqSAVaIBsJZroyd2LYM2MFt5zS83cOFwkhlSJXnfVs4tC3KJkanGYliC10sT4WaLOBZhbkjAwvBxa2zGlAYCXjb3zKX1r2E8V5KhXyz21GXYoVbt0aN1+yM3qdcJXWMTV35C46iwkptTLI7rA85IPpykV14bWWg1EgJMWf28q0YBBInaTCPIiTC32gcyUkhcCUeU5UMwVcafwpnRaRu4isl7PBYs01qj6Rdk+5X6jkOd40CumDLj7YmgfK9mbHCZFtyVHXB4M8HxpSpvE3Pbi7YziE5Lc94UZ46ct24PJys0W6+hdWWMRv/yh6oJnEy7dTzMhwUe0NiLijgiCg+nmnG0dmU7Og01rTz7aLq9SEYdnnGUUZEJYdlW4f8bDgb2Xa3u6CCcp6FnTqaibjy9pQcsVGFNuedrNm2rpQMlh0zVY+vi9miSmfKwiVnyaixUopRRI6tOc1AkeiGWRGL2td+XWjAp0Np5m6dJ4QUCgEaHQxBSJAMObOkME/OsHVuG7FRbxbBbDL/wlk0zKDZNdlx3b6mwv2SlPY03u4MVdBof6EGQT9Tui62G6ZCaXzLl8u81Js9fC57cxvlsKuat1a9iAI3nLbN/ByvL0tDQEuDzba3FTxsykvvrgpS3rK3KkVJZ7MefSbYHxdwdpAYV5kfoyxT18dKVXv4zCWMHo2Itd9f3E2F3C77PEy9kAPDZ2Z3cGUKuTx6xxhuZq2zN1hqE6DrHC1LQ1MahSOWaHrAVH8hesWikW4XDNknmIYkben7dX2IZDLE+O3AJGDADPR9im6L07JL/LWDyhGOrDx1X2yutofrF2SpDgeid+mhUI7kcd0WTCHIx3Z2uaW6G5XZ8kaNYLa/rSPyAIZTDJTXjGt3CD8WMzBHHMw8IusBhYt5HHEF3QhhFMMu02iyQWmH6rgdOicl4+F4LHYHOZyDyYrfWfv+lnFIYQgNRrR5zpdqn28OMHm5LQfPL4Woc9d1zMrtplH2zcaMhc5uxZohCWpzI+S+A2Af9WgXbot2tTO0/ALPt7SDIPFhvRaqVJE7MN9wVo5qjGUv4QC0oA+Mus1WYIpv9fpMNAuqK6OInKtUYdXnImuSJurdmY+y5aL26jl8y2qCI7x9NlfY7ejclpdmHgJ4AfvzwUGrhX7yjd0Ki5aMvD+fGpxYRLubNSqMeQq0zj3P5aQTWj51TvbsNCw2EbLIEL0/0TbVhU2wH/d86KqcuhOJ9srCoZlQ2Z4xjNpbdMeEHDeqre94yrJLMhuLZXLVCEUf2QUnLmUy4/ycqKhTa14sP/FKCgyG0W2s5mB+sH0eRmeCgSOSg7MXirCiWPeadj5f8Ets02t8VYu4KK41kcN3BDLCXov3O22h4qSKwkTPo8HaKnhxO8KOTXtMfWSRzuqLuXS1z1v/ePIGSwrtPXWOirHbmVdPcqW+Odv7KPXicT7mzcE5lsTI98bqsLEKLbYyGXa3AYXTi25boQi3PJgEJkfl7sqwx6g4drfZtuLX/nLEwMBukkS7gtFgdqm6JWtryL66doa7JNnedepaG5hZ1R6Xyo4sN3ow8+ORiD3L3foDbR22DmUTO3jbETS6OhEDwc4E0L9z4jrHA39MnWNN9HS1QZiYwrDZru9Ey/VSZ93Ti9NlufCZiFZqX18y6QnsoS8J3uyIy+mGLH3sCq/6JT3OZk7fLAfSkvb8mhGWbkBXveKF10Dd29fjuTLEnDCvF7CjJQwvPTQ3gfY3p1HnVrPsGlvXBIxEBYZGvld0bJAyqj1juGi5qUu6wGAKHc5rr+oNNF2yC8kTNp1WMlbnYw3DiF5YNJnXVmsirbAMl1jVh+MebQh4SDpbZrfbXYJg9MJZmdeDsKWqOrgdqNnyqtxuRCOBvT/GrBnuDOI6F0qntnJniSz2hRVyrbGMzvkNS21mWEhLHosvR9Y/3q65fMlgDyUG8TC/bBxCRwYYqZZ4sL9IxRDd1jQ9H/cbMFFQ1w52ZiJOG+W2Y4xhUc4vmJWKsssPhIwCQNApQ3Vq+tRVK++ieZhzhXEZ8ZZofpQw2DpczShEVv4JPbJd2e1ygbTbJtmUeGTRw5Hkt0TW9qHDnjUyygkWh0PV045EcbadLF7grI5KFBieiVjVqXK1LMU146v6WIp1s7IxhDDq+fHqi8Syn680CiA1flnvKrNto5uHAmJF0tx3loqlkHN/ySwBxWOIm+Gi57ftuup36xKnUjyqPYWgFDrCtkhA3vbbM4pouLkw5r3FdmZkyuiwK8ukbPthdljrXnAzt2ArJs3KEl3bDr6VWUfPlrjtRuF6UIgkastR57HMNQ5SWg5mAKa0mb1lJbyebTZmxF2VkeHGszFg3Yp2UrMsLRVugIfWCDTjMetEsHaTmOAmt84Za0WVdEd/LTJbW0VOLueuuzXovuNG62qBKaqNvcyHfMja22jKqbSzhSGUKHYorVqNRSXLS3NM0AQQ9hgWKHLC8LqivBbMNA05tolAztRSvV6L0wGZMwM7M3UHaSTs4lSYYtuUTffNuttfjNueOdvpHK62Uqu2qXuLPR29AJIsEl8UN07JdRaPMJh0Na38uNfJzOqj7WUp77OrHjgAeFhXzD0dK6PUQdTItcQLVTjncUXNEzmCdYyXNpuX15fp2fTzCfNf/kp5etr3/+yh4+P54Ps3T/fHy0DZl7uuL3/dtJ9fX0o7BIY9HrRWSeM/H0f+t8esn//d7y0mKcPjW9vpC7O+fn9AX5v+9IdIL2HmNFVdDt+qPGnuD3xfQUyr6e8hqm/PB9svdyfTor5f+3DqcboqXLv+VufAxfx+Lsym74FcJzQ/Dv3nI+jXF2cAeQvt6ttyhX0D0Di5/PwuBHi6eIPfkJff/g8YEVf09SUAAA== -->
