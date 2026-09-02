---
name: "rar-cowork-cookbook-scheduled-brief-retire-assets"
description: "Schedulable morning-brief email summarizing retire assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_assets", "rar_sha256": "d296c6069831e230682319d338d77f7fd980667b39080fd9e3e48f75276633f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_retire_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-retire-assets:03124bc9d788206ab4f03622aee9dd7b2f21bf36c43e8d1d085dd6d86debdf0a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_retire_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_retire_assets_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Retire assets Scheduled Email Brief — Schedulable morning-brief email summarizing retire assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_retire_assets_agent.py` and embedded as the fenced Python below (sha256 d296c6069831e230…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_retire_assets_agent.py` first:

```bash
python3 scheduled_brief_retire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_retire_assets_agent.py   # or on stdin
python3 scheduled_brief_retire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire assets Scheduled Email Brief — Schedulable morning-brief email summarizing retire assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_retire_assets',
    "version": '2.0.0',
    "display_name": 'Retire assets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing retire assets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-retire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-retire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '66b914eec8041dc6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/retire-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-retire-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefRetireAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRetireAssets'
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
    print(ScheduledBriefRetireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6d3Pj1pLvV8Fq/xh7qRERiKRbrnogSIABAEEEJo9Lg5xzIuDn7/4OSEozs7bv3lu1VY9TGhFAn8796z4H+v3JaGo/K59en1THSCHeiOPAd0rISG2IzbqsjMCvLDLBD2RlaV0GZlNnZfX0/GQ7lVUGeR1k6bjc8h27iQ0zdqAkK9Mg9T6bZeC4kJMYQQxVTZIYZTCA+1Dp1EHpQEZVOXUFuVkJ1b4D7lZ5llbByCHrUqf8BwREBF7q2FCdQWWTQjbg1EOAvnOcKO5fgBbO1Ujy2KmeXn/97fkpAN+fXn9/smLA/JtWjj0fVVFucpmbWLA0NlIP0OQ98EAKrnOnBLok4JYN1H5c/VQ5sfsM/dd/RZ1RetXPr19S6PH58jT+U4Beo/p1ZlQ1UNUycsMM4qDuXyAm7oy+Gu1tyrSCDKgCDky9l/vKb5yyHPplfPbTXciL59Q/fXnKgArG6N4vTz+PRn95Aj4A319GLvlPP7/EWeeUP/38jU/VmKFj1SMzoPXL2+P6wRYQfiMN3JvUXwDXeyBN58vTd8aNn7veo51g5dNLmAXpT3fGeZm1TmqklvPTz3/HFrjeiuKgqv8lvr/eGfuOYQObHor//Hxz8m/Q5GHQB8+/F5uDsP47lgDyd3HP0MNRf8f75v//xjoOUqf68PhfsvurBZNfoF//1rZ/tuAZcr88LZw4aEF2gFp5hX5/U+Ul++sn+9vNT7/9AVj/j2zUrCmtG4e3xEgD16nqt7dfP1W3259++/VTk4Ncc4zkrSnjv+L5V369yfnBgw+qn35cC+TraZSCUoc+Mh36Pcv/o/zjBToYcWB/u1+9Qt/Xy/iZQKMR70LvLviuZiqg63d+/PnpD4AOKbCmsW6PQZX/539CYmCVWZW5NaRaWVOPIFMHiTMqr/lBBWmPov6qbteC8JLYXyFwdyx3ABFGE9cQX47oBuphjPhoQeZCX/+PdYPOz9YDOqfVOw693TDx7Y6Ab3cE/PoCaT6QmZWBF6RGDCmMLEOG56T1KO2WFwA+P7ejQKBMcAcchV2PYFMBtv+Avv5TCW83Zi95P6r/JQXPjOAGq06SZyWAZYCqxohPZl87nwGkAgwpszg2DSuCxv+a/GX0ydF30oenLNAtnKtjNbUDxZkFtHYDAMPPI4xncQvwcPRfFQVxDNlAEwt0jf7WVoCPX0dmX79+NY3K/5LeARiD7u2kmgKCD4Whz5/z0nHjwPPrL6lj+Rn06fc/PkH/F/pnq27MRxkysP/RXICGG3UnQaAimwSQVdCYDgBubhH7/Y97FEbtQOuBQB0FbuDcFgNu38I/WnAPzXtcgM2jik75kPSj36DOB36Bghp4C9R29fwlHVlkgLTsgsp5d+J98d3174G+yxljUj18COLklllyo71l3hhMKyvtF2jtQh+eAuaCuNZjRP2sqkGy5k5qO6nVg5VG/S2EaVZDFaiXyu2foaYCpo6cv5qA9eicBICSUX+FRFYG/S2L3/vwSARWZ2kwBv6RqffbgEn5CeTY/J3FCyQ5wJtQbpRG7pdG5dzoXOOeEaCvva8HzA0odTpo7OLOGKNbJd8yT/lhZPho69DyNlzcujv0pUFhZAb9f5lERh0ZnleWPKMtF9BS0pTzPaHGqWm07z5ogbHgIWas7I9R4R1V3vH2SxoHIAhl/487pXvLoTvNHcOaEiijMMqN/1jN5Y1vUINMGENblmP2Gl/Sd2B/Bs4FcahGjAIFG91teRc4Pn3X1AdVOV5/a/LQPcnG5AfpC+WNGQcW5DqOfcv02i/HOnr4H6SFM9YUSHzL/8EqCHAHIQf8IaBEADwOvHtznQTqYYzHLbk/yINxdAJa2I0FtAUF47xAxzF/QQQqyHTA/DPSAC98urGCEgf4GKj44eHKN/K7MuMk+1DQGGORJUbtfB+Bx0OQi2MHAfI+Cg1wNWyjBr7sQBBAHV3vkf3Q8xEroGwyJv1t0Y/hftgKfd+B/jEWG9DxG9CD4fuWtd+cAxC6TKob6IC2GlWgnBPnI0/vffrl3mrvvfxDl9c/je8//XsT/q156j9G7hXy6zqvXqfTe4N7728vVpZMQY4EuVN963X3qvt8r7HP9xr7gendR6/Qv6fYDyweGf0KIS/wCzw+EgLLGVP28QF+YD/Pz59n49MRR74F+JEFI4aBWjb7j1byTgL6iVc63kh8by3V2JE60ARviHZrDR9J8CgRAJipN/bBKvuudEebxpDeI/aBvOBROmK6Pc5tnjPuZ+JR/cp5ek2bOH5+So3E+Z/2MSOyghwFnhi3PqBewAxUB87t6mMeGi9+3LHdKglAgJ29jgUFuhiYXZ+hjzH0GXrfGNz2WWkDdka/jiPwKBKQgl8ftB/bQdN5Atuwus9Hre+7nXHyekzEf1ZirCOgseWMfTr7KMxR4p+YgC+e55R/ZrK7fTHiBzpUtTH2PtByHzX9npHPEIgbqDVQPgAVG7Dgz2KAnNIpGuBfezT3m/++mZXdbfnj5ob6vmX8/ekdJcbv99Z/z5mR9780m43+fO+pbyNX47Z2nKBu7r3Nm2/AtGDsnd898sZB4O2ef0+vAF+c56fRiWUAhujhtjV+uqsCbPg2qQIOACk+V+MsMAXlAziBDp2P+kcA5b4TMN4O7Bv9+OX178fbvyr5VxhD0Jlp0TZJUShMGObMhTECRQ3HoW2bNFEXRUwXI6wZ5lA2YsMUbtuETRG2Y9oubAANRgGJ8dBgioy+B7p/OPjfm7ef7otBb0BxYtztozRhETBBUxjioBhMUCiG0DaGUTZJuqRr0xRMEKSJ0TAFgysHc2aUS+IoSRAY5hIjv8fQd9fo7X3Afo/GvezfAEomwagvahgWZZHIzKZJg7AcDDYxy0FQxCYxB8ZpzKUoZwbWfyx9RGQM2N3oMVHBvAemrXaU8/sjwmPyETNAuZpVa+b+Yaf0wSAvgln7J7okbAZVpoamalstluQtDZr4wiyRhYzzdV1vGik7btjlht/nXsCtS/xop1a8wJl02CwwjAmYXI1nKXHaE9Sx74/edtYInovjM2GbFUF/kg8El20MAynKVaCYh5PDBdnpMDQ5O+WupX0wpvIQaii3zDNd3SG7U1MPon7FD7K0Qxscreg9PROabJEcay1AjZKSlGNeqsZmE5h6fZQVg6iwXDuXGh+YUaPs6Y1zlglJr11OznFRCEmaltNDfrXacpgpB2RCuTIuCRzOHnhzq+RHKeLRQTIPDZ3ONFPXky2eFl5O+gJdYOXxqm3JxOQWRX0xkSnJGo3kap0+sP5wKVA/MGUBJwZnm/jrc3vQ1N6RlLk1I/1jL8a7OC1qcyFqenk91vYx4danTVnDeJeeYb7VLLVs4pZojZYzYmGx65XELE6i16eTOZ5cz8QSbWIqVhKEZjbLdIs6aLxN+Ko2yzOBXglLged9q7oXxsuz4zw/+lYyERee2wpsMxiEG27kI9u2qbk/0zWRHyvXJ7bXpm+ux3xbddJgra55f12Tc6VKYIro6KIuN12Sl3iCqNoFm1yjbHY55jgvee2qk1f2NpLO+w0mX3oxkkqOTIgMGy5bx7U7QlcWwWEI0BXZ6umVL1MhD205Jzoz3SwOidlyPb50Zs1aqXVSnZn8qjki3KEZdATZH2v5mJyFg78K56uh5uJGUClu2YZmvKMu1MwhuGirkRznl+h5loZbR+uOhdWpKCav3Z3rk7gRJJh2WBn4kVcpUZbLWTVUXOatT2pCVuxydTqR0kkzwc9ZumjlIIjHVkerrNPdVg97cUXtZVHeXgZf4fIpteKRYSdP8WQaLHlPUekjiYWSHZMCvaUrLqkL6tx0ubI0QwNB60XkC0g4Qwt5LZ47KThp2lCeJoi2rkvB2i6ahdadLyqAJG3IV53FxYaS++Jhj6KL8rQUnDnTSx6qKpt9MkuCkxeYgQ0Ha09sclnRIxUptxlekDITGLsL309jLeHgSc4NfXid5a697HJ8nbKWis+SHAiuVWY9WbMNj5MJelBXmHpZTNgZix6JwtqZ2HnatfA8RqxIWBptX4pdm/NmcD22eBYQh2rmbuizTipwvYtFTZKPDOht2nku8idSE7HBOuwRmq8Td1Wl1QS/UPAmWC74vsoKh8hZ5dToBuWbFMYud1OVJFZLTEmigaIn6S4gkoKgqjxOBOpKX4idhITa1qXpbZdqUXQuJY+jStseg0kdil7SDhqeeARO+Nfz9ji3EoPzYFnO1rOCUtSiHuKOUFZksaIOp5OOrq8mTXfW4hIxqdTiS1ZdJ0RRrKyzthpUd3fWu2wzy071mqkuNrfwiBBvK0uiFoWUIFdG8ofmYhiNkM6Z4TpJDJS1JPza6DacRudiJRjadXo07QLJJvjknCSZE2WRYa6AE47hUsiuYo8KSRjIFoOf5loV0UGA2Szh0CsYF3PMnAZCJBcRyXBned4zc50q2FVTV3DOYIocqvuQPV+nUSFw3TaMaz45LwT7qM/ONkz63gaAba+nAxVaTJKKzaXXYkNOp6iYnFWOya7cpMG355Zepku+SPZ7asvE9J7Aqb3IbDgF5QLR9Dtmtlnr/jkUl+kE3lqxE60sfb1iOCufS0g2rFQvVS9GQ3uhecBgntnk9RYdmDo+U2VrcZeZGZYdxlxYNN/Tl4yz+Y62A6pahD2pdsVe2DVtUKHOacTeht0qs2XJG/kVmdJNFGVXvg35GFWQzW7OKfbO55I5Pb3MONMGaLOq1qxiBaEyid0VRmQH2TjNr9RkEKSVHC+orPAWR4TE84bfM2w5D3N1Au+MXNh2gSlpZW2RRlbHckzZzDEKdNifd6ypBtvW9TzYHeZTH1cXEmrq8k5zvCVDLg9wNB1ohp1Ys0WbiovTXut997A2PVj1iWZ+dW3i7FgLBDkyweHCYwPXzjBsN9B5gu3EYcGZjTYLrI2zoOh5dsllor0c8K531VVBlY46XAxeK8LrImSZJVMNKOgM3ErVUTTiF3hqx2LDJ+Ja3V4m+8l+IbWDSp4ODXsuE7We5wZt6/Vht+gV3+AJRdID/xoXO65X9s4M62JMxHiZXaKGG08olTpvARJLNpclXLXaw+2K0NPoxPqY4mpsMC+U6ALTiJjBy6iTFG5JI+alxv1mPrQyRh7qA7nPuovFOnpTqlxiLSUVXnMFbjTEbpX6ORvpAu5lyTzvvf26Cl1PUJayBxvbC7Hdm5e4brV+2UZLu0j3c7dNAuMk1Vd2s08Zfc1PmSxpo8kgO5KE1Bo8P6vsuZJadt9QSwWbDLP+oAiEuuG20WK3Y050ck68Cy24w3meqTGK0JxDVldFKywY0QYzU6wlnxbITtmJmH1ZbOcwewQB0BBkVTPyWnMOxqW5ii5MrEEHkVRT447SRLruJ9sN6fIFUx5sJLQJdqPFK5ppjittEc+2800WAb1SJDmYPO8hi/Pliu7TqT0QCi0Fx4jvFym988lqW7Fam+wsjRs6iblk842LDY6R+dg+qY/IgbPVPJo5k2nlcio97UTcjAx57ZORmhJU1HvNzoNxWErqGA4J3T1dakom6Us1t7QckWvz1OrkeSNlNFXthX5C8BQ/Z5f9Yc12ut7uBlM69FXsubPQunABv/Z9OfJtFxSgehp2B8lmkhmnZV0Q24nd4YVwZdlqbYRGmTWL/GQJPSnp3HZhrE/4Zmo4ZHycmyc31CtEKK4yo+sdL26wLUKX1II3WMMuDb8rrovDJiVXTH1ptmvRpbpyj7Okzyyartiwsh2pjG1VqIvM2ygX69qo881loh+jxfQUyyTLn400mmUYHALINZykjOIm2HTwELP9fEmd2thchhv13EjmshNjNuNynTgo80Fd22EBgnHcCHjA+wl1OCqLfp9PeFGUO36+uvI+jg5bF8aV44nZtRfYTji1mJQnYR0T2ziaBZS/A/0yAluP4XCeb33XWGCMW69kclulUsWYIEEoUTo3eZlvh3jIdR0lTLcwen82rIxdk+qzTD/PLhhVHEMjpq9xX23cucdPiZlxTrJ6eaI3CRPBJONZm1mr7ooT4Z2ErRLlWmmc0c1pB1DF7nxdcE7tSbe3dlb5E/iSnhmRmJynPuGYnnNpdmguEgeDLVe5BnirTJqUjce6jAlgOWekIgqFxSnfNuJVTxeUncDaFTT5eBmkvbC11ZomByaZKEJ42ClHuBKqItTZWOL6NpsIzMWa7HgBR2D2LMv9xut7OrN3AKSXtCnjpq7OZXEim62Fi5VMmOvustXlTRng8N67qN65OPUJRqvYOsmYvMb63KvsmRKSMOHuNzyDzKZuloWw3As14oh9vhVZkWo3B245q06uuFIFV0O0Epmf0EZRjoofg1nYDdfclDn4Z+0CNmBmRtXSlUFxgdDpXmkYSajLDOfjuoz1y34d2b4n8nPC2Mpcz0hqyxuIMT9nl+q08fvzJIFBW42PZUBkzKpjZLXrWyuZlpeoYVgwo+/17VGcnM5K5wvlUq1ZrBA3Q4dxhabAF9WPrS4Ui97AJ3ZoTVzpFJqZ2CTz3qENUGVUlQXZenmgNunJ5YbLBWM2shZk0+xEwdi5dzKqEM2FGl7pBi213m4KaoLMyT2OGRvsjDqrjlhsKmc5xYh03kkHHLfmFnoMvTNP0OGBU9Z7rO58mpf0KR9t4dUizJDkOsjeOVE2MwIH83Y9S8vcKerGmIqYFxzC9XDZgGnysuSm03a/qhImUYZ+W/QYgMKImSBYvJz7NeWQ66neKC4V9ieEduZrOJnUi95Cm7D2z9hkHrdifDy6fqWJq+1kSnh8d506HSVnfsdhzao7ZRPKHCgcpydXZrI+ZPwBaad4M/UuuCBjTeKayOBmidN55Sxdnjw5hueGrZxmTZNf1vH1iAk4V1atp00yq+LDFYyQm4xVZK9eiKksmrA486jN1ObhUyxOi2E3eJMjYR5A5732osqipV5hOz+iZYYtyssaX+3KHa7p7lZ01+qswJeHTbJyYQl3HWAKXy51tSWjtRvJFM03EzKs1sG1aQ+r/daNaVji3M1pg04GaX0pLGmdGhItH226nvGLtVK0Mcp1MGlFGuymGbrawm2Pm7Q5RcKh5sFWjKg0YnFR2S0prjSSEIbKwazpmr+wQrVrTyZ7FPdzlDOs5IK27cU+XeELQs3WQisMm9nCb/CGwzGWbM94s2bAQFAecH475SeOcNz5QsgFtr+hGVINEF/CSoEqaKbdV+xmp15ljDoFcRroMVGnac3NdyHr7CywE+gOSXNmUOo0786bfomhFq6SQ70TXcYxNl5p7NqAt2e6PpmYCkVNduxitybtOZEtiiMY2Cc912j9mljvu+NsSXoFS0vWKoj2RGkZQTetdku2PtTa0qSmnKso+hlbutcJtjj2DD2hl0F9TbCIvMxE3Rp2IXLMzrGECLEqBzpqrUtYdGY2jZRrcmGfQPulm4Vti76lrpa7U0UnDdtOBg6VQ+GIgkkilQKRK4iwn5L2jqYtYdHItGktdXZmCFpbHidK0xnzUo5VXIKRqYfZmXIGnesEHzqaLz140c6jydLZsx6xiOnVmXNU10oVT9nLlenyB9SxdWE39G6rbpRQH9DQviaOIlS26S9ldodNcmW/c0utolhsUsWg2fEHmCTLLo8JcVaJtIzMCCTsA24QqHVmtPWemOLVFttKakM2QRPSk76ZN/WVHs4rOaMnwWRqzXkZP8GbesoZk3TLRWzahyHDwWc2vRblRKuuU8TZRIc5HCqRe8K2B2duU9gstRcwzHRb3adPp6FtjR0bsOcaWx2tpjaoLU9GWFoMR55wJvti75SV18XaSuYXTKbA7n4N9pyz7UxcuMtkb1lozuc6Ty2a/YDYeUDXEqrB60lsRMqZKWSybhWc8PY7Sw6pXAiaTXkVsCRNGC702GaV72Pb0xKaP+z0E1Gh0SVSUq3KIganCpTio01/pGPzaMliRa94y3ZtwTVak5HJoZgLQUXmJ69tHXjF7zSVdnPCD5NDa5vRTpfNnZ6ma2xemV3DHlAimB+xvM0XC11ABCTN2hXdxL0s8pfzYuhWRG/zRX119IQPCKbnvByllt2BhlUOBvtuy3DJU0BuCDJxxRm+2mLX6+50cBxt2i0kH9uIezZiGOaXX56en24vZZ9eERgn4Oen8Yz/cVL/L5/1ekOQvz3YYCSCPz/97x1I3g8H39/e3Y7tHcN+vUl//Rc1/O35qbQCoM39aLiKG+9xAPnfDls//9PT33Fpf3+VPL5evNbvbzZqw7udTAep3VR12b9VWdzczqWBd5tq/COS6u3xauDpZk6S14+j4O/UB3cM63Ze/1Znb3ZQ5VnlPI1/6zG+OnPswKjfL73HSf7zk92DaAVW9YYR+JtT5qOxjzdJ4+ns+Crp6Y//B1jJ6BccJwAA -->
