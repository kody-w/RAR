---
name: "rar-cowork-cookbook-bulk-update-define-banking-policies"
description: "Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_banking_policies", "rar_sha256": "f97bd4e13bf95ca1e4e567a815d33d585de97e35897afa25127c71b991303d38", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_banking_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-banking-policies:d5847401b4ce873eabf09928260116847abcb77264e3b3594aaa512a5fde8b08", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_banking_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_banking_policies_agent.py` is
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

Define banking policies Bulk Field Update — Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-banking-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_banking_policies_agent.py` and embedded as the fenced Python below (sha256 f97bd4e13bf95ca1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_banking_policies_agent.py` first:

```bash
python3 bulk_update_define_banking_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_banking_policies_agent.py   # or on stdin
python3 bulk_update_define_banking_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define banking policies Bulk Field Update — Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-banking-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_banking_policies',
    "version": '2.0.0',
    "display_name": 'Define banking policies Bulk Field Update',
    "description": 'Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-banking-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-banking-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6848bd3db14b5448',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-banking-policies'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-define-banking-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineBankingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineBankingPolicies'
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
    print(BulkUpdateDefineBankingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjVpPuX2FqPtgeVbfYEfXGG3FZxSaEBEKL21HNDmIViwR4/N/nIFVVt8f2zOsbN+Kqo6sEnJMn88nMJ/Mc6tcnp2vjsn56eTIDp4CWTpYlcVBDTuFDXHkr6xT8KlMX/Ie8smjrxO3asm6enp/8oPHqpGqTsgDTmarKkqCBHMjtshQKkyDzoa7ynTaAHK8umwbygzApAsh1ijQpIqgqs8SbptSBV9Z+A4V1mYOFoaSouhbKkqZ9hm5JG0N+PXyquwKq6uCaBDfIDcKyDoA+eZ60n4EqQe/kVRY0Ty8///L8lIDvTy+/PnmZ04BbTyxQaHfXhL9rwD4UMN7WB/Mzp4jAwGoAWBTgugpqsEIObgGdoberH5sgC5+h//iP9ObUUfPTy5cCevt8eZr+bYGKbRxAbek0beBDnlM5bpIl7fAZYrKbM0ymtl1dTCg1AMoi+vyY+U1SWUH/nJ79+FjkcxS0P355KoEKzgT0l6efoLIG6wE4wPfPk5Tqx58+Z+UtqH/86ZucpnPPgddOwoDWn1/frt/EgoHfhibhfdV/AqkPl7rBl6fvjJs+D70nO8HMp8/nMil+fAiu6vIaFE7hBT/+9FdivTjw0smf/5Lcnx+C48DxgU1viv/0fAf5F2j2ZtCHzL9etgJu/TuWgOHvyz1Db0D9lew7/v9NdAZiq/lA/E/F/dmE2T+hn//Stv9pwjMUfnnigyy5guhws+AF+vXVNATu5x/8bzd/+OU3IPp/FWOWXe3dJbzmTpGEQdO+vv78Q3O//cMvP//QVSDWAid/7ersz2T+Ga73dX6H4NuoH38/F6y/K9KivBXQR6RDv5bVv9W/fYZsJ0v8b/ebF+j7fJk+M2gy4n3RBwTf5UwDdP0Ox5+efgMUUQBrOu/+GGT5v/87tEomkirDFjK9EtAPcHCb5MGkvBUnDWS9JfVXU5U17XPuf4XA3SndAUU4XdZCy9pJMsBR5eTxyYIyhL7+H+9Oop+8NxKdT+z4+uDF1wchvr4R4us7IX79DFkxWLmskygpnAzaMoYBOVFQtNOa9+houvzTdVoWqJQ8aGfLyRPlNF0W/AP6+i+s83oX+bkaJlO+FMA3DhjmQ22QV2Xt1Ek2QM6d0Yc2+AQ4FvBJXWaZ63gpNP3oqs8TPvs4KN5Q8wB9B33gdYD1s9IDuocJ4OVn4PimzK6AGycsmzTJMshPAPGDWjLciw3A+2US9vXrV9dp4i/Fg4wx6FFkmjkY8KEw9OkTqAVhlkRx+6UIvLiEfvj1tx+g/4T+p1l34dMaBqgLd8hAQGeQYq51CGRnl4NhDTSFBqCeu/d+/e3hi0m7AlRFkFNJOJWsdvLPd6EwWfBw0Lt3gM2TikH9ttLvcYNuMcAFSlqAFsjz5vlLMYkowdD6ljTBO4iPyQ/o3939WGfySfOGIfDTvXZOY+9RODlzqqmfITmEPpAC5gK/tpNH47JpQeBWQeEHhTeAmU77zYVF2UINyJ0mHJ6hrgGmTpK/ukD0BE4OCMppv0IrzgC1rszAjwmg+/Jgdlkkk+Pf4vVxGwipfwAxxr6L+AzpAUATqpzaqeLaaYL7uNB5RASoce/zgXAHKkDVn8p6MPnontX3yOP/oqOYKj4k3luQR+GHvnQojODQ/78uZVKXWS63wpKxBB4SdGt7fMTW1FZNpj46MdAtQGDeI1G+dRDvZPNOw1+KLAH+qId/PEaG93B6jHlQW1eDWNky27v8KbHru1ygCiRPXq7rOxBfine+fwaoAJc0E3WB3E0nJig/FpyevmsagwSdrr/V/jd0pjwAkQxVnQtQg8Ig8O9B38b1lFJvTgAREkzpBXLAi39nFQSkA+8D+RBQIgGhCmrCHTodpMbkjjv6H8OTyS1AC7/zgLYgd4LP0H4KZeCHBjgAtEXTGIDCD3dRUB4AjIGKHwg3sVM9lJla3TcFnckXZT4FxXceeHsIwnIqLGC9j5wDUh0QQgDLG3ACSKn+4dkPPd98BZTNp/i/T/q9u99shb4vTP+Y8g7o+I35QXc+1fTvwAFkXefNnX9AtU0bkNl58BZAIBLu5fvzowI/SvyHLi9/6O9//HtbgHtN3f3ecy9Q3LZV8zKfP+ree9n7DLJgDmIkqYLmXgI/PZLu0yPbPr1l26f3bPud6AdSL9DfU+93It7i+gVCPsOf4emRlnjBFLhvH4AG94k9fsKnp1+KbfDNzW+xMJEaIFp3+Kgt70NAgYnqIJoGP2pNM5WoG6iKd4q714qPUHhLFMCgRTQVxqb8LoEnmybHPvz2QcXgUTGRvD81dVEw7XiySf0meHopuix7fiqcPPiXdjoT34JwBXBMOySQOqBLaqdH4OqjY5oufr+7uycVYAO/fJlyC9Q20N0+Qx+N6jP0vnW4b8eKDuydfp6a5GlJMBT8+hj7sXV0gyewW2uHalL9sR+aerO3nvmPSkwpBTT2gql6lx85Oq34ByHgSxQF9R+FrO9fnOyNKJrWmSoiKMRv6d0APX3QQj1DwHkg7UAmAYLswIQ/LgPWqYNLB2qwP5n7Db9vZpUPW367w9A+NpW/Pr0TxvT90RA8AgdM+Dt924Tqe719nWQ7k4R7d3UH+d6XvgIDk6mufvcompqE10coPr0AwgmenyYo6wQ02+N9H/30UAhY8q2jBRIAdXxqpj5hDjIJSALVu5qsAAr63y0w3U78+/jpy8uftsH/Cwe8+MQCp3AYcXEvWFBY4LghTNPoAiVhBCHBM8f1XIpCSTzAXIygccdxCAR1iNAPFi68AHpM3sydNz3myOQHYMEH2P833fnTQwQoHChBAhkhTbk+HiCYG9KE5yABHhAk5SwQwscwYALhBzQVYMSCppwQzEFQyqMQl6YRDMZ8bNLyvTl86PX63oi/e+bBBq+PRgKsiDqOtwAycB+IJL0Ag13MCxAU8QFIMEFj4WIBtPCfPqa+eWdy3sP0KXRBnwK6suu0zq9v3p7CkcTBSAlvZObx4ea07ZAo5W5jd1aTwfF0mMtuYStovXHVdStKXqiw+dm8CTmmigO7HrYS3G528Wy/sWtzGVmEUFCs0bQLYkUNclqhcLLYJ5F91QolHU8LKlvTi5MaJdzNWiOwkpqpN3S+dtx1uwyplZ1tkVfYPI8HNcUEH0sTc7Bns5l98E51oR4RVfAlPAJprg/U+ZZFdXpuBDEp0e1eE8szW8vWOm6o22XrVO16K7sHhxB2+ShtT3vlKvKHfY4IFevkO05GSWrXKbjBksfmIM68q9XOfKM3ipqm/TnPbCnkCBfK7qLi+2aoAN1qqb3nDmrmHpOszle+UBsLMVAG2+4GWFNok7d35lKjtivMc0TL3s3ZmCu7CyxneKfBUWNrhepHjc/yV+4Wd9z5yJVrZDS2HLxdpp3oiIh5tC7H/NpoJTwejvC+64i0OInhLBA72zmNSy3TNmtXYVaLepCPFjfszEQ+HWChMIXzcabk7MFDOFc8kocO9bYwOzTm4cREdSnUC3S5G1G0Yxceo7lXJW+GbXE0yCwhtcyMTxeZQoJB1LhZ7GdWQwrE2iA37DFHohy1Nnv92BEqAS82O5scHMXoXP1os/2shJtsc5MqvLCiwlx2ciqnx7Ves2R2OWNjtdbDFid2kqzDY4dRWn0oeq4u3Dbyr21602pFsfPT9TTLV6Vy3uOdvItBROHuUmpzWzS70T4TAS5lluguOeS4xYd+4W73bjIa7HbEByK5cuFautTCSr428n45t+MkvJXEVWe2o6gdj4vzwm39w4oSLgM9guKwPoqL0wzbWL2R2gIpjicV4ISqhwO6PtjoOrS7FVnX+baolAIPvQpRwuhYlLmU3gKL7c/EtgnUY2vNo+Gw7lN6vuTnHL5muRakLNX6Ke2gcttoy9gjtDWJFrGkEppumkoZNvJ4VdpbnPFL3fIaLuI2XCgYonpK22w7Z1cKPK/W661BDCS+9tqVag7LJlZcpQe79YI9MxLjxsulX+6F0mosPWLwLSolIsxUuZzEaVHSp8LM1pI8egHnHriLwdcEUve1fUXZWbyAw3LOimSIm4iBn4K49tIkzD1XTOcWZek7KtXJEZ4ti4XLeJcTEl3n80Ec6hOnrVstoxe2f3XJnYlf7QzWo81xJ6Oyu6/Yve+OkXkjk2GnU44gMzY+evRt4SOHut72iQRXY7vdK+WGWXpqcZHHobjYDj+T5hmeyDW2ODGtQerJ8oCNyMlJ1JA/Y06zP15HS8wiar/31+X8sMq4wOJ2STMzxDwbrlxaZFxZDK2vst2FUuq1ji68nOuiQ3qcleuQRXpThOHYkdzrjjPGnbUw3SqtVr1GL7hNap2dWzm/2aE8oupVZtFudtCD+VGp+sDsN6276Z3BccJU3MPrIx72SyXdHuAljKi5tbR3DrPZrazNhd6wGcp5JsHObH9TpzfHkN0RAJZtL8gRJWYXVi8uCpouO8q4YOuzOMLSKTuJZmxcI1/ryraclTu0VhyM4qQb3RkUj85BZPEzfHPzZlLhRtEQZPGq2O+deInfjLMirHj+RuEyLIhxaSiRp5N6xu54Uxqis32dMVVCrPuVYSDskdXXpB+lEp9fDzXproT9ZRjNw6KWFLiDV6uNl7DOcJM5TFwCRF3alLuOHJdiSsorJlbNzbbCdhF6OXn6cPCEE+dsjlylq7Jc3fqNOrpE1vA6asN4LHM7Jlp6ipMPAlyjs8t4wyj+fB32gs1K1LjRuCym2Cr3qLBCloD7cl93K32YG2M2mxuHYJP2oLb5bisRurpKawLLt/nVDOONOG5LJ0Tmq8wQExZFManR0u0mlkZkpktn1UiTZIvPkhrU5HXS8705V5fRLUOCmTamaSRyN5ncDa2UdjuykVXDTspgdWE9XqczAcnMpPc9ToSXZX4o190x3/pZYO1SfhPO0kiIuRWve8iFkaIVw+IWw3eMQt4MDtXVNWk5OMu2B+XSb+cn4tRXdiqvx+pMZSd2cNWko/ZWQKv9tahLPEoalWSZHiv32nFMEmxt+vqeWDr8isg6R42NEzzjYjkaVkpJp5dCPWHtKT7zFnqkCQFk/Jld9YI3C/tZjYj5We+KbLSZQUHd8dbdYj3NNnF66WzSGuZbEpeOKS2cKKRhuSt+gE2iYnrfEDYeDa80T42a80ClcjfwbWvkRscL1SES85a6qHClbCJ/xmnlbilp3rE/eoM1I+DS3t9UWdhzeV0o29jHV6IilgklXoiu9MPzUZBUkJ1bFTEzI9oQvB+psGAwN1S1SdUWT6eroQ3COl0q5vmg7s85Silqy0pW3sar3m4FO85XoWjk+eKsDxcTjnfb2TFaXZN9QzU+iV6Ow05TcsoMmYtfH+ercZeNOrVs95l80MaBdZNe7NeFTVzyHGyfjga9tEkvWZwK97ZnmNLSA5JOguOM8UfAU/lFsQzVlqr5Ni1Z1gnMLChtcSXatUIskpjQbiW8VG/KOpD9ZtnczKXQbmKet467OPX31abBOd6mkTWPelZ3mLfLHefBzJb0wxm+0nFlBlOBHuGyWugME3ba2BpSo1fWuqqt3lYimp7jc8unKOrUbxXYEHlMXqLIPJA4mfTbItyR++GsnU6zcL83qUM0nszZ0rqEHIo5V3prl+FWOOPicEXRhttsmJVocg1C0KOCorZ31o7SIPerE2AE0+EXa9RdjPrFxZ2BkZf1xsm6wcwOue8RKd9L+0Z2Kq+uOr7aetpAbVJR9R350Cs0GbrZRg0PSbVrkPpiGLctEa1k62pmRL3jlw7pMo1gFUl+MY39mues3X5zxIjLpdyIhShbqbk6kZ4skCe2nF+sQB58381WkjWWdYvzi87hYXEBmE5BdphwPgwyu65oU9LKXMtWxGYV6ZJIEarFRunqsIyTw2DFW2IlFXPCHqpWvey79EhI/rnJblvA9dSl7feuJ3hFnvE8LXQ9aNs8vxkl2rSReescLK7XT7Y9jIraHfLd4Ft789wcnIGi186NJw5+aLC2Q6mSMaq1JLT+HvPGgsWWXHYQ9psYIQkS5WrS9HaZdJz3SJoXJlmSZhEV4XBx6ATFcl5DfHjNUKScOt0pEU6tKcq40BWBwGeaQFpojJdLp4ePqjyQPmuehtuBQT3ZZ8YTiSDFrnH4otb3IZwoSpueSr3AoxXln8Kb4WfEsO0C2LyUQaM2VzWHuX3GWcpJN4U5U1GSumO8g7LcR+SKYU6WsnZWzrrMhihVVxgnt4fktKO3J/fQMS3CWVppJUGi642GbQbQB67RM930nYkTfFMVnsDKo9zlwgWpMyWxtBFTsTxjmeXcoqN8P8/2W+2yqA1jx/ahd8gvgqDuJNE1ZbNatjf9KFjaNUH746I/G8NlN7udBgaWDUe7gn0CjBU5HVfb/Cif8HBpW6tOCVYNpi0Q7nCT7GA0CTHLRLE4VsWwkXYLLZTIU26e/CHpiKVkHyKpOsyUZbjTV4oogU5WbQZ7yC/HYxnGkbbjZXgXWOnSFc0VfoGZfjOe1pbrwL5e0yGrCwKychheZzZku/BwdSyJMNybfBVHliwcBNvUvDVIqiTex569vlRHC3SiJe5uNzeUtlYXuCYTsP0h1z2NrUNr13grrIhvQbs9HDJaiLhl2de1auRVdcRmKIwd8qsmUHjR9REc4CDfSVYqCOY6k6K6qegGMQ4k2qHb66n0qRjb0Q491FdPOo2YPSO8NNzt/cYlyT66ilvNpLK+1df6br8u9rDGaREtzXg+cme2SuYE6op1ItUX5NImrrEib4kay2M5RIGwKZbzvsElPHVGPsNt22nDfr5AxpGBN5slUR9XlJqNLlIcM3q7T86gXaa2g6SfS7rk9LmLOLfCL87HAzV2Q3NdwnzTaHA5MxSrSihUb3SkW7PEbJjPw1ILU57bXQZ43izm/W5RXFzsYGzXc/TChU2FpUqpUKzb8wO22c20onQYdcaTR6OOpLM1i1r8wkvYhc72sXC7LTPJukYCjC+iRXX2ljdLEuZKERbmooFvV2xVn4qyYVsQnp0vstRMWO8v6M5asxt/IK/BziP6nDVHGd2symvkDmdBXwxHDWsjw521AW6lFCzOMdjeaKiWFu0iWUjFybW9OMTbISN3vS1z1+LCSQa6pVt8ycvb6+qEISPsmpZAS7ij00OrzdfqdT+njwuqT63cV0SaXbWMqOd8RS+WPYa5XZj6q15EqUPdRtpS5l2uXfMr94A113Ee6GTn2tqVH9gKO3egFhLYkgrlUwv2fzdACqTYjOJppgzCJu6jHmxbZnEG2LyX6KGfC5hvwhoTWWlj0fS6Z+BeTejDeRywCNtGhrZW5H6hjpLHuoESEwsG59z54FUOTo5n6ibl0ZFDOX2xwa9qYklkI/EjNQ959dQx9I4dNH2rha6C6YSwEtijdZSS29buwCZOOcM+cUU2xxClONs+tCN+XoSra0Svj25S4Fu3qr1zN+v67ehtdWq9CHxRWo3RPF8sCUvviCNNZ4bAqbQvdWIYeSN2w/Y3h1i7xeHAa4UQ93xOUil20+eL43qGny6zOXMePPR63Gu42tOmN8OWtbE8zmCdqTZa0HRr9OoQe5+vLpJvuylmYR3V7isxvkjrQ39g4W5rlGPAsSt1wapaElEgIPezK9rLETM0oWLBp2KLoxt8ZrBsr2QYsrmS7n55opUu7q8CA6tUaAdiNFu0KIb5BtrtfX8RA093YZVeg6sUF93iSu2bANaaU5iEvI2QFIaH8bI/XQ66D/OL6HrQ+xbp9c47uLR0HQ4YiE96bdMcFfb7a7mPK2a7KPEb6y+ZauFc6JpahQPoykSrleETj9CDeLhRYTZTjA2tMysuk0MbW9D6mo7KeF27FLKWrCw4VR2hn8gGibtynpEpe1nsS0uhsYyJ4RVllMyyJHdCSm+bhNextbY577A9XXtZdtjPKHR3dQvfovfqloxVO/d5OjfSmX9j8LXUL3YIbQr8IqVG9sZwyC02RKTkmjEej8klVK3AWlakv3YiiwfNl6v4+dyMKr49DYvliK30XmyWI12TIxtSHegjmdOBvLKGJ17sNMyRgeS7kFrxwRzD5eaKrmpjtix5nDrZO7eEU7PpeIk43MrNpZirNhe23nitjzsSk6RoDQv4mrigdLnaMjC8kxmrpZ3NeVamxkVjBhqeR64Ie2F32RFFu1GwfQ/jmVYHBhOmKlLVRVoxDPPPp+en+0vdpxcEJhHq+Wl6JfB2sP83T4WjMale34RhICien/7fHVc+jg7fX/zdj/kDx3+5r/7yt/T85fmp9hKg0+Moucm66O2Q8r8dy376F06LJwHD4+X09Jayb99fjbROdD/PTgq/a9p6eG3KrLufZgO8u2b6E5Xm9e21wtPdtLxq788+TJmOaO9n5a9t+fp4if40/Q3J9O4t8JPHiOkyejv/f37yB+C5xGteMZJ4DepqMvbtJdR0gju9hXr67b8AW4WHzX4nAAA= -->
