---
name: "rar-cowork-cookbook-demo-data-manage-the-initial-synchronization-of-data"
description: "Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data", "rar_sha256": "1349d033a2c40d5244f96acff2c53c3300d7035d255cfe3e6a9f25a495eba6c8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_the_initial_synchronization_of_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-the-initial-synchronization-of-data:b2b285491ed4361245369a798065600ddb1eea2d441f076e90e2f595eb3cfadf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_the_initial_synchronization_of_data_agent.py` is
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

Manage the initial synchronization of data Demo Data Generator — Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_the_initial_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 1349d033a2c40d52…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_the_initial_synchronization_of_data_agent.py` first:

```bash
python3 demo_data_manage_the_initial_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_the_initial_synchronization_of_data_agent.py   # or on stdin
python3 demo_data_manage_the_initial_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the initial synchronization of data Demo Data Generator — Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data',
    "version": '2.0.0',
    "display_name": 'Manage the initial synchronization of data Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-the-initial-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d3321d0db81c317',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-initial-synchronization-of-data'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-manage-the-initial-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataManageTheInitialSynchronizationOfData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageTheInitialSynchronizationOfData'
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
    print(DemoDataManageTheInitialSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejSJblX2G8P2RmE+Hsm9epcwbtCAQSICSRUceTHcS+iSUn//sYkjwisjKrp6uqP4zihDsCs2tvve8Z5r++WG0T5tXL24vmWRm0tpIkCr0KsjIXmuddXsXgVx7b4D/k5FlTRXbb5FX98unF9WqnioomyjMwfe1lXmU1Xn2f6lTe/Rr8SqK6iRzI9dIcfHXyyq0hP6+g1MqswIOa0IOiLGoiK4HqIXPCKs+i0ZpQodyHXKuxwHPIgmqAa+c91HiZlTV3iKaywNQsuC9ZREneQLUDHldRXr8CCb3eSovEq1/efv7bp5cIXL+8/friJFYNbr0sgEQLAL+7C6KHnvAQQ/u9FIo/DQJoiZUFYFoxAINl4HvhVUCIFNxyPR96fvux9hL/E/Sf/xl3VhXUP719yaDn58vL9E9ts7vOTW7VjQcsZRWWHSVRM7xCfNJZw2S0pq2yetIZ2DsLXh8zvyHlBfTX6dmPj0VeA6/58ctLXkwOABJ/efkJAtb58lK10/XrhFL8+NNrknde9eNP33Dq1r56TjOBAalf35/fn7Bg4LehkX9f9a8A9eF32/vy8p1y0+ch96QnmPnyes2j7McHcFHlt8ltjvfjT/8I1gk9J56C5b+F+/MDOPQsF+j0FPynT3cj/w2Cnwp9xfzHyxbArf+MJmD4x3KfoKeh/hH23f5/B51EGciLD4v/KdyfTYD/Cv38D3X7ryZ8gvwvINST6Aaiw068N+jXd22/nP/8g/vt5g9/+w1A/z9htLytnDvCO8jeyPfq5v395x/q++0f/vbzD20BYs2z0ve2Sv4M88/sel/ndxZ8jvrx93PB+scszvIO8MJHpEO/5sX/qn57hQxAM+63+/Ub9H2+TB8YmpT4WPRhgu9ypgayfmfHn15+A4SRAW1a5/4YZPl//Ae0i5wqr3O/gTQnbxsIOLiJUm8SXg+jGtKfSf2LJgqS9Jq6v0Dg7pTugCKsNmmgNaCsBAL5MHn8yXG//G/nzrSfnSfTIhNZvk/U9/5gyXcA8f5kyfe/Y8n33L8P/eUVAhz2JcurKIgywKYqv99DYDIgSyDEPVzqNv18m+QAMkYPHlLnwsRBdZt4f4F++VcWfr+v8VoMk7JfMuA9wMpggcZLi7wCZJwMkDWxmT003mfAyYBxqjxJbMuJoelHW7xOFjyFXva0qwNKkdd7Ttt4UJI7QBk/Ajz+CYRGnSe3qWoAleo4ShLIjUBVASVpuFcB4JG3CeyXX36xrTr8kj3omoAetapGwICvAkOfPxeV5ydREDZfMs8Jc+iHX3/7Afo/0H816w4+rbEHdeRuw6nKQVtNkSGQv20KhtXQFDyAnO7+/fW3h3Mm6UCVhEDWRX7k3ScDtG/BMmnw8NiHu4DOk4he9Vzp93aDuhDYBYoaYC3ABPWnL9kEkYOhVRfV3ocRH5Mfpv/w/2OdySf104bAT36Vp/ex9zidnDkV7FdI8KGvlgLqAr82k0fDvG5AaBde5nqZM4CZVvPNhdlUj0Go1P7wCWproOqE/Is9VW1gnBRQmNX8Au3me1AN8wT8mAx0Xx7MBnE2Of4ZwI/bAKT6AcTY7APiFZI9YE2osCqrCCurfjQUvvWICFAFP+YDcAvKvA6a2gBv8tE9iO+Rt/vvtyJT0wBNDQH0bHimQtviKEZC/991QJNq/HqtLte8vlxAS1lXL484nDq5ySyP5g/0Hg+wKam+9SMf1PVB6l+yJAK+q4a/PEb699B7jHkQZVuBuFJ59Y4/kUB1x40aEEBTRFTVFPTWl+yjenwCWgH31ZOqIM/jiTXyrwtOTz8kDUEyT9+/dRJPU06ag6iHitZOgJF9z3PvCdKE1ZR+T9+AaPImY4J8ccLfaQUBdBApAB8CQkQgrEGFuZtOBmk0mfaeE1+HR5NLgRRu6wBpQZ55r9BpCnsQujVke6DJmsYAK/xwh4JSD9gYiPjVwnVoFQ9hpu76KaA1+SJPQch874Hnw+AZWe63/ASo1hQZX7Juih7X6x+e/Srn01dA2HTKlfuk37v7qSv0fZn7y5SjQMZvZQNsCKYO4TvjgPir0keQg9od14AFUu8ZQCAS7s3A66OePxqGr7K8/WFL8eM/t+u4V+jj7z33BoVNU9RvCPKooh9F9NXJUwTESFR49b2gfp7s9fmRdJ+BqJ+fSff575Luc+5/fpj2u7UepnuD/jl5fwfxDPQ3CHtFX9HpkRSBXAX2eX6AeeafZ5fP5PT0S6Z63/z+DI6JEQFL28PXwvQxBFSnoPKCafCjUNVTfetASb3z473QfI2NZ+YA+s2CqarW+XcZPek0efrhyK88Dh5lU4Vwp54x8KbtVTKJX3svb1mbJJ9eMiv1/oVt1UTdIJqBcabNGcgs0JI1kXf/9rU9m778fr95zzlAFm7+NqUeKJOglf4Efe2KP0Ef+5T7TjBrwUbt56kjn5YEQ8Gvr2O/bmZt7wVsFJuhmBR5bL6mRvDZoP9RiCnjgMSONzUC+dcUnlb8Awi4CAKv+iOIcr+wkieP1I01FVdQ05/ZXwM5XdCefYKAK0FWPipHCyb8cRmwTuWVLSjn7qTuN/t9Uyt/6PLb3QzNYwf768sHn0zXj97iEUb33e2/0RNOZv6o5e/TYtYEee/c7la/d8XvQONoqtnfPQqmBuT9Eakvb4CgvE8vk20rsGo03vf0Lw8JgWrf+mmAAKjmcz31IAhINIAEOoNiUisGNPndAtPtyL2Pny7e/rQJ/2c5483GbZylSA7zXJKgMZykCJqzGI5FaYpGUde1Mc+zcJckMR9laI9DPdynOMqzCce3XB8INvk7tZ6CIdjkKaDSV3f8j2wWXh6YoBThFA1AMYLkXJQgLNwhUZfCSdLnaMvxfdyhCIcggOQMSlAuTlGO7xEebXE+TlnkJLhFO+yE92xNH4K+f2wDPnz3oJN3QMppNKmBW5bDOgxGuhwDEDwCBRbwMBxzGcJDKY7wWdYjwfyvU5/+m9z7sMUU7aArBT3hbVrn12c8TBFMk2DkhqwF/vGZI5xh0Thjq6ENV7R3Mc+IYEfHMoHJ1ZAVKkasB97M0VqS7ZXI8BtTuFqnUuwISVDEIsx5RN3Cg85sfGUxhyNKUre1w+POujV3xD4dpYSlxmYxOy47L0rG1hCjU9SGDoYV6SFlRlPGrLPE5fSADhfDjBL1dLz2xnpQPLT0MzHxkmrZFf4tKyj4cjMv592RWh+jK3I1aLMpVEVFq0LbWuauMsII9SyCoZNRuJxWhByxS+osmgbdR2J5PG3Lm7dr5iZ90eR61ZUXVFbpvU6x7G0sYP92TRCxpvybnZFyqN7qFWDyPMpDcagaLcGa8ynCmlJUZ5cBC2Ouw+D4ZBCXeepfrgvBTRjJ2WdLPRkLfVTVXblVSik5llJM3k6LAT1GJwkzjvk5ORzOW8vSF/t56RsafirnSwYzCsu4mpFF9W0lNvJNtcR9dmpyDDHwIxWh7t7YeNeNXi5N5uwcbEYqDPFCJc5hcAVNjrPWiY21v0orc4+NWbzcbl07jvAgEJmOHqzNYJBmxrPrs2mmKEqcqOW1zrjLllsNFZAqSplTra6yzKgP5W500Bnr+PUw74/2rFHSXLY4b3C25YUtCiPGVaRG1wdOxBRhqH1NTPSg0tbKMp3tpDI8LTNDgf2tcUVum3lEBV7qngjbpVFYwBzK3UkNt0sldylo3S6rkQE/7HricjrYc2Pd+2rq0LfKiOyrL/V8Ddtt3B2rub3cnrl6ZabSjpU3e32fKrWJkG2oDUbH9v3F4lJl2w1ZzK6kzW7ZFNdhM56ZFk7zBjNUA98XdXJbLHqalZb22hLmKzRX6F2dUiJgO5ormtlIN3KlxNGtNLIB21OnMS1G9rSxuOhM5ltaCuH1guVX61uzFTT3ukZIuRhL0/evN24jKNc5Z1A46y22V7dW7X4lFh5dKkOdqtIWs4qjSOVO7cr1ad2peH9dF62mHtVa3ceK1jj9eYiZoEyYCM02QudQCLtpvSWxDUQR7lwrD+3ghMzixfqoHjBRbVZkrDvXNjgER+IUSUYg5VttVZ+OmJmF/W6zvHrukI88jdQSBTZmZNSjx9g9XimaF6zY9w7uhj+YK5NttH4FF7JGCH58XtsUneKqZhFHe18w6H40ymJY3HgGaZDQo5VsjiUa6yjzJkn8wTyv6LLuY9FYw+vuajGixc2afb+IWslZOHhw7RKYJ/bOfqMbG7XgLJsT3J3MLU78VYyGWEsvm70a7MitmmilR8A3rUnq+MSEypa40PuVj4RDUYfB7ba+bKmS27XWaeRcC01v3EFDJbmURXHs2ACXDx1nW+ZRzH0rQcs1nbGSivWoXeJHYaHulys5b/3ZqtdXNQaaPft6nN/Go87qVdMOS/IKw9v4VKiJaSDokhZsQsxzFW+Rs6aygq7HbJz2Hh5ofUyipCzp9a7jGV3Uhaq9mHmp77IdTWFJKOQFbXhGudofdpQrKqyGxsY86jgSKa0asw62g+yumV4sGE1PvA3nxWi54Bd5Vw/kmN4Cz1bIm9V2Om71HpB/z3vDgs8498pxutBRLe4o13BEWTKOzdymMDkdO6TmycGdSb4TXsVLDh/ymbNfUylP+8Z6LtzgedCoR+GYmfhWYlgD3+mzGI2pJqFhb7YbRLy98LayKZ10ZNRenXtUGs+YQPOO69I/XMtktpCNaFfNeovc8sdGuMbGpZ0vjnJ+uuyvex4reD0pVRfLr7IaBJZ9WRY5pXbBRqBmmlDro7xSlpYlcGLf0cw1QWfaChsFGu2k1AgZINmFvprEKiXD1HV924gYEH+Un21nUjwakVzjJKJH1bZUDkxM3eQsPyyCo7XJruexg9nmotAtxYXuUlwKsN5zyP6qdog6W9+Q5uJLJGlwXL4PV4fDbXfbb91eW84Wws4V3TQcdcU8HY1DWbhS5h5MYTOHr0xrqrPVjY/ouZHt+3nQmQLV0kLp0OLeU+fbfnNNSws7SuhqxnPbS4gbF148JAfryMX9ypy3/LKrdjgqdqJAJHglI4ac7UPE9EP4kHYNvnOMI7bVdo7KWX2DkY2GkoGda1hqjgIIl4WKnRhP5nlYaMZ1eXNNW+1OyGau94Wc7lo1FXYoa9RXRCYip3RKtbyeOVzZqjK2D+p+Gzv0cdeVttg4os346tmTFLTvmJh0MkbqnBSj3Cg9G6piZARP8IfCCM5qzYirdWlug3A+d8gibm3dkJfLUpnvsUNJbCVYZ2fRVU2kklEZy1ha+CwrYasllU0WZnx4ZKhLnoRFlNZCfXUDiV/uA5IWV4Ooy6expLT1YXEqDxd0fjZMrBTwi9ya6Xbo9HwZ92wK+zZatNhwCqTI1xezhNRWhBeNBm6vayVXhFYwL+kpvI7JiHY7SdjAblNewvqQWBg8OxF1753LwrIKE7AjbhMGJoZi2KqtrIY8TTGnXWwycw6NNuj2Nk+2ZzIOaRctFPWQdMfkHG2xq6xbS9pfa4vEM9JIxVfbMdy4QRZLOzqxojwyXfXgnsxjQ2r8kTvG0sD67nlfbI6oaPHmdn9DLpsTSE9arTTUCVY6fuKl84zC2Fo5JWp2TOqzeryceU8LbYSi4Nr2tyMPF5tTISgUL8Aoowf6Ro92HO2fRVY1pRsT4PTZpHf47qbGdIY2DV5R8ckSL6owzNyKKaUZuiHn4TGw5UXv4FybaHt0jVgbbYnPTS0sSC2i/Q0GqzdCPW3NwOEJRV6iMKXlutK5CIWG0kmUtZmKnXmsE8mBSuKVyNEiNq4rdyh14PmoPVtJl2bk0unWvEAwBluym5U1t5xrEa4rck5u21hfVSF67DdxuoVNJT3OCjaa6ZdVXCzJJW3OSqTUPVBUXbtRXF5Ja4KXBoqStPN4XbAbVWOPpkVVtwDtY6yO2mhdHMdk18/Q/LxBKF5dhMo5bQLidLguI78VrttCUcLeZEx9SdVdmZbk5dSv5cOWxE1SD41h4S/Hqk6WRDEOsch3dF/YO2mJNcYtNbZGyQ2pnkrDyvSZk4bouD+3LHJObNoDTM9dHoPNhqQTuZljqnzA+4ppB2PbbvYLW7lR3lY9Aq7enDTLlarBXHtzFxGLCpd9z9vdZEI/LG51JHmUJqgpJuz0QLP8TlOsMQrdMYJJQtqoeRFV+SHZZiLlLMwuRPkmC1h6dy6WkX3ejTxR6biJ1QMSUHSZNVy9O56y3M7l2kv2ZZQI85N1s9gtybfUbhfwhKWyzUymFs0Qas5eQ0dVyQ5z76ha/jIqQFYTe2Fukyy+OzArex4qLIPxwxG1Re+K1bNsJITi1mwOioMiQrLYbukYd5d+Ft4MRLSGo0BtsKEpsq0xXDXqNNfjkT6Sa71lotgoN9eVsTHrhSckFznHziwR7ExanRHosD8cff7o+kxq9DFTjA3nLbVQ2s33cGsa1oosxJvllqtbA9gZDnPpLAqSMmoKiu63+RzxnXEXlQy6kvFaSSp+oWWc5lC5KCiSrBfUeVtUie4dep5Z8Gq96fOczYTlTETNyshXUZgOTnruE9rWGVwzynZRXnmb510RETlQ7pW+IrLDsSu0uRPNsr6m0cWS4k7LM3DQOUlldKhrT57tjrLEkp1Yl63n8u7SQBct6IG2sCOpbd24xs3H4ugCAv18WnF8MJ+VYVWaezytcvoKvMIpl0VXRMPKrWdsg1XjSGjIngyYg3uF6YqUHIazcarCGyJtO2WBMxc48+YG0y4ieCNmRot2juThG94VaHdeN6WrkBSe8Xl91lnLzdgON+HZYcm3hkeLFGMtWGlTZU3ZiFp+ucyWfWkmeriEhYWyRyR7tlf5fbWRg7IaHd8AVX3fLnI+llGjX+DYJrkFbnTG5NNuf4z9E7pT7I1KdDsbDiIi0Rj91MVyxiW25x5W5gWpVMcOdG7O4G6+xzxFo+CBRRDy4MfScifSBMJ2SI+iTc8Q5/0gcjd05ZvnMtdRG12vyi2mBBV73hzwwCElO1vOMfLab5HDRdNnAXviEiOUd9062ehZJNBH5+Adx3Zxka7xvjc3M+ImybLUECJM4QLvGERqZwfUk6LF+VQnx/F6zJymIhJFYc346AxKPC4kUiErVNL3WdmtDxJMW+dow6njwnH7GI36q7EiHMFfUTiG+cKZsh0Tj3eJN2+2+HW5wDLf9mbBwFsS7M4cWSFiVTrAeOU4jIWMpxt2QzxFWTrl3K60/WWWCkJ26zgJNILrgJEZLtvWIiBa1t3NLv3MBhtm3K4sGEl6m1IJe1zPDMYrN44jE3tiv6bPIzOTD/wKphIb1Nwzqa+6hh9WraNt8WWFaawmnHKiPd1witaCgNwJPoj95kDMJJvNJKzf72CN99c7bkey5YY/z66Hbcjgi3zQWakeTTJjrtVun/GOiF23pH4al9FYUVXGdKS8vu740Z3R+aI+XTRCgc+tPgikwHcnchYGte2m+CI8AIvtVuoFIai57BrNsERYRLwFsrix5xm1YqjKzVq47ZeSs20YRdOQFbHrg9oLNqZ/08wLKyWHbG5R7gbeOGGEYN3GIyxqY2aEHe7PfNhfG1LZ3gLJzzt3QXaYq8xu29FahM4tqDY3bmQcm+XMK3FE5wlfrweSpuWqcFGlrV0MiC3vXbbFrPi0zl3aXzkbDVvCAFVYdnbH5604u6nyomJgZhnxC7FHZkyOKFfQjfWsF56X6dk35kjOXM4ZdqI3J/awOFQNY11OC2YgbESTZrcVcfIJHyWys9x00lJYMA6L4MmBRRdecF5UGEPS6Y1IR5NF0a3MXOyWR1Iuqm6YV0vNSDN+wCFUduE6UeGqViDO6M1hQmFQXfJQRPyFlUGDxeE2jPfkJsdzf2eUNBUx8PwWwcuMvaSBNdeOm5KGxSyDSUPdq814IYTcuu1RuF/bJUpE8PGU0uy2dLFK3YZR1vmoIulXHg86Jc4PZmutlY2yP4z1gLm6HSYdDvZj/s3WXc1V9v2p4E+zYs1hRMtyhy2jbDr2uOrtI0HK53STHuQg0Npl0TVNoKfs2lgbBB0QMZXPMj3O465ny3VHbK9oThvMybnxNQMvyQGeFS6yN/kzgiihHtRZdJvtfaNE4kOKDfQ19Jmd5JK3zjD9mjv5taQuZ+NIU+OhuGAX59SKe+oYGHv4lB5phiIucLftYcXnnXxbO9KiYA6XVC3SWuUzm+bCDate/KOnqlSBrM5gVwEzvJ0p61FrOQLv5yBTvQjxiIRoO7Tkef6vL59e7kfLL28YytDUp5fpbOF5QvDvvlAOxqh4f6ITDIl+evmfe4/5eKf4ccZ4PzLwLPftvvrbvyf43z69VE40CXl/LV0nbfB8nfl3b3Q//ytvnifE4XGqPh2Z9s3HsUxjBfeX5VHmgoJcDe91nrT3V+XARW09/fVN/f48xHi5K58WjxORp7Lg2nJTsDxAr96b/P1xquC9TH8hM50Fem707WvwPHAAAAPwd+TU7wRNvXtVMRngeQY2vf+dDsFefvu/r0Ps24EoAAA= -->
