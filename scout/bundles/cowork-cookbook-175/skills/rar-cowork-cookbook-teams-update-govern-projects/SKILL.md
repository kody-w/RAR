---
name: "rar-cowork-cookbook-teams-update-govern-projects"
description: "Drafts a Teams channel post on govern projects status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_govern_projects", "rar_sha256": "5cd034c0c57251db5a51e5b75293befecbf47976fac6ae22523cda2b55b584c3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_govern_projects_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-govern-projects:694af9d6ace21e9b593c80008cc7641f22bbf1922f0544befb255f65424fe2e4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_govern_projects`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_govern_projects_agent.py` is
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

Govern projects Teams Channel Update — Drafts a Teams channel post on govern projects status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-govern-projects
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_govern_projects_agent.py` and embedded as the fenced Python below (sha256 5cd034c0c57251db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_govern_projects_agent.py` first:

```bash
python3 teams_update_govern_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_govern_projects_agent.py   # or on stdin
python3 teams_update_govern_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Govern projects Teams Channel Update — Drafts a Teams channel post on govern projects status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-govern-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_govern_projects',
    "version": '2.0.0',
    "display_name": 'Govern projects Teams Channel Update',
    "description": 'Drafts a Teams channel post on govern projects status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-govern-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-govern-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '827f16cbc42daa00',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/govern-projects'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-govern-projects', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateGovernProjects(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateGovernProjects'
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
    print(TeamsUpdateGovernProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716a5OjSLLlX2Hzfujuq6zkjVCOjdkiJCGQEEgCIdQ1ls0jeL8fEtDb/30DKTOrerp77ozZ2iqtMhFEeLgfdz/uEdSvT1bbBHn19Pp0BFaGCFaShAGoECtzET6/5VUM/+SxDf8hTp41VWi3TV7VT89PLqidKiyaMM/g9EVleU2NWIgGrLRGnMDKMpAgRV43SJ4hfn4FVYYUVR4BB46rG6tpa+QWNgFcCwmzBlSW04RXgHCuVdwveKtyES+vkLINnRiBa1s+eIErg85KiwTUT68//+P5KYTXT6+/PjmJVcNbT3cF9MK1GiDcV1XfF4UzEyvz4ZCih0Zn8HsBKrhACm+5wEPev/1Yg8R7Rv77v+ObVfn1T69fM+T98/Vp/Dm0GdIEAGlyq26AizhWYdlhEjb9C8IlN6uvkQo0bZWNeNRQ78x/ecz8JikvkL+Pz358LPLig+bHr085VMEaEf369BMCLf/6VLXj9csopfjxp5ckv4Hqx5++yalbezRuFAa1fnl7//4uFg78NjT07qv+HUp9+M4GX5++M278PPQe7YQzn16iPMx+fAiGrruCzMoc8ONPfyXWCYATJ2Hd/Ftyf34IDoDlQpveFf/p+Q7yP5DJu0GfMv962QK69T+xBA7/WO4ZeQfqr2Tf8f8n0UmYgfoT8T8V92cTJn9Hfv5L2/7VhGfE+/q0AAlMisqyE/CK/Pp2VJf8zz+4327+8I/foOj/UcwxbyvnLuEttbLQA3Xz9vbzD/X99g//+PmHtoCxBlPora2SP5P5Z7je1/kdgu+jfvz9XLi+nsVZfsuQz0hHfs2L/1X99oKcrCR0v92vX5Hv82X8TJDRiI9FHxB8lzM11PU7HH96+g2SQwataZ37Y5jl//VfiBw6VV7nXoMcnbxtEOjgJkzBqLwWhDWivSf1L8eNuN2+pO4vCLw7pjukCKtNGkSorDD5oLLRgtxDfvnfzp0tvzjvbIk2Iw29tXceenvQ39sH/f3ygmgBXDKvQj/MrAQ5cKqKQHbLmnGxe1jUbfrlOq4HdQkffHPgxZFr6jYBf0N++VcLvN1lvRT9qPzXDHrDgi5ykQakRV5ZVZj0iDWyk9034AvkU8ggVZ4ktgWJdvzVFi8jIkYAsnecHEjToANO2wAkyR2otBdCDn6Grq7zBNJ1M6JXx2GSIG5YQS3yqr/XEYjw6yjsl19+sa06+Jo96JdEHvWjRuGAT4WRL1+KCnhJ6AfN1ww4QY788OtvPyD/B/lXs+7CxzVUWAPuWMEQThDpqOwQmI9tCofVyBgMkGzu/vr1t4cTRu0yWPAgfKEXgvtkKO2b80cLHp75cAu0eVQRVO8r/R435BZAXJCwgWjBzK6fv2ajiBwOrW5hDT5AfEx+QP/h58c6o0/qdwyhn7wqT+9j73E3OtPJK/cFET3kEyloLvTrvf4GY8V1QQEyF2ROD2dazTcXZnmD1DBbaq9/RtoamjpK/sWGokdwUkhJVvMLIvMqrG55An+NAN2Xh7PzLBwd/x6oj9tQSPUDjLH5h4gXZAcgmkhhVVYRVFYN7uM86xERsKp9zIfCLSQDN2Qs4WD00T2P75En/FPD8Ggr+Pe24lHeka8tgeEU8v+t9xgV4wThsBQ4bblAljvtYD6iaOyNRqMe7RTsBO6T7ynxrTv4IJIPiv2aJSFEvur/9hjp3QPnMeZBW20Fo+LAHe7yxxSu7nLDBrp/9GdVjSFrfc0+uPwZogCtrUdaglkajzmffy44Pv3QNICpOH7/VteRR2SNEQ9jFilaOwkdxAPAvYd3E1Rj8rxjDmMBjIkEo90JfmcVAqVDP0P5I/ghBBzy/R26HUwC2As9IvpzeDh2S1ALt3WgtjBLwAtijEELA69GbABbnnEMROGHuygkBRBjqOInwnVgFQ9lxn71XUFr9EWejmHynQfeH8IAHIsGXO8zu6BUCwYVxPIGnQCTp3t49lPPd19BZdMx0u+Tfu/ud1uR74vO38YMgzp+I3fYYo/1+jtwIC1XMG5HmoCVNK5hDqfgPYBgJNxL88ujuj7K96cur39o0n/8z/r4e73Uf++5VyRomqJ+RdFHTfsoaS9OnqIwRsIC1I/y9uVRfb48MuzLR4b9TuYDolfkP9PrdyLeA/oVwV+wF2x8tA0dMEbs+wfCwH+Zm1+o8enX7AC++fc9CEbeglxq95/l42MIrCF+Bfxx8KOc1GMVusHCd2exezn4jIH3DBkZxh9rX51/l7mjTaNHHw77ZFv4KBt53B07tccGJhnVr8HTa9YmyfNTZqXgf9i4jGQKIxQCMW51INCw6WlCcP/22QCNX36/K7vnESQAN38d0wkWLtisPiOffecz8rETuO+rshZuhX4ee95xSTgU/vkc+7nls8ET3HY1fTEq/djejK3Wewv8RyXGLIIaO2AszflnWo4r/kEIvPB9UP1RiHK/sJJ3boAcPpY7WGXfM7qGerqwMXpGoNtgpsHkgZzYwgl/XAauUwFI7JBcR3O/4ffNrPxhy293GJrHHvHXpw+OGK8f1f4RMnDCv9WNjXB+VNG3Uag1Tr33THd07/3lG7QsHKvld4/8sfS/PaLv6RWSC3h+GjGEZSkJh/tO+OmhCTThW2cKJUCa+FKP1R+FyQMlwZpcjOrHkOK+W2C8Hbr38ePF65+3s3+R76/MjLK8mctYDiBwMLPpGemwGIaxjjNlKNwjCNv28BlBeBhNUTbwbIKmPYamCMoDBKCgAqP/UutdARQfkYeqf8L7H7XXT4+5sCwQNAMn046LkZSDOfSUoHHXpi0aB7Q9pYkZCZUBju1R09mUgaAzFiAImiAd1yJsmrZplnLIUd57k/dQ6O2jof7wxSPl3yBBpuGoLmFZDutMccqdTS3GASRmkw7ACdydkgCD8HgsCyg4/3Pquz9Gdz1sHqMU9newu7qO6/z67t8x8hgKjlxTtcg9Pjw6O1m2gdqHYDupkknXkcye1As9bq/4oq4Sfed2ji9Yu/XiuLkVZ1Py4mNTWlQkOVg+VeQd52En1DyTW3Xgae8gJwpRyy4mz6WLMq2n20GVsXq11+aMXdJ6arbhbjEpiu02rC6ivcGmZ7menaSKavQkLlhwVa9UmBWnLjyfy023kvUusXlaEHFKkCvDPRlnpSm3xr51V0yhh9bpmmxDSdJX3hCeLsfSKALtahW4E5aV7pRnHgNRPPHUoZ44mc1OQFjtzvAvumDPdnPYSJw5YZfVpsVLW8cvFnlK651p7AOTJg8y2hm+7bf26sRjKyGl8I1BsEBxNvGAX3guXzJlmxwLZcHSF/RypJkibqp805n1JpKb44bwZ0QdOFvaaKSK43Zb3VJSJ20dre0rbY0ZeUTjlbXzMCXG++KsWNKyPG0Wq6MBtIpnh0px+Y0Bzeok9XymJL6vzoq2IQSDysomRg1F9TdO35OdVO4qYVc49LC4bG7qjC1OZpLa2lJXNb1ds82S8mkcCg80rzL0pI9KUkysS3s0rXIxSw/pJjJ3DYbPK6NKz4G0WCeSWae9R6d7fH2oh7Kp5kc5mIBiSW3iedRKnLSJLNyfabPTlGYTQ21Zh9+mc+aC225DVjvn0NI9Y5IaBWqjF1en8HK9zBI5v0QKjMPDvOVXoi0IXpqsjHbQNRpQ60RLbvEqDebXCfR5v+odIbFxXIq2whpdYYd2xa4JRRy0uuv6taRoN712bkciVW+eap9P6K6zy5KPWm84bEGqBjPTEAkZOy63xdE9XQ46RleaDYrecqtYLyZJzdIOurCKSdCxrDxd3dD5fMJx1XnSLPXzglGHxZzxjtWUAZ5JrrAqKiFxzCr56hrdqgliXDwnFwyXpJVT6SUuthsxM9SFmddmF4mK5LSqUaNTbcOVdSIRXOFhy0LTRd1hVFZAgUGVpi3op8FnDgDLyxO3LFeTaCMUR5mqlktyOYihzqfM7aCzK2e+0eswTLcypQo359jQ5CaqF9UEuyYxEUUr5Sj1UR46IrMVloaCEpd2P4vYUBxsVSeIrSYwUXDN1vjuQlTkNp2tB9SeGYTisqtVQM4IbFMRJ1RKnHMbDuv+KlpaQy9xQyfLiHfD9c4xCvdkyanBo5P4oqbMJoymuA3oMwz6XI6PKL4clkqK62WEHVCb5gk11rCQqKtAtlEv3V6xY7mVze0W9/lJoRcNc7BsjK0m28bS/XS7KXHTM7SkqKddwS/z1b4zNkFboGKOnbd7sOkOMNkZf+8uBmpZb5pTXFc69CMHwGyudm2LzXMvOuwoP8f30YyJvaW63vjbZSE2s5b1JJOlg44/ZEEqoHO+b29Ys5W2J+l2y45bNsbaWxIVg6rsrEufrrSkKi+HM7NVlksf5VoLv/nNMpVpAt0aMcHsdMdj3P3FCt2huzaYdqBkqnW4ywlPD+tAzUEHt+s3jbA6gNnTadl68+jATqaEvGGxtXEF21u9cpyUDyM9bV3tkoeA4F2ghInaHuerOXbahsY5OjTlaung87oZVlW2WlPhBsPVDvccPiA5S+rtxFhnNJWSYrxxi3bWW0Vvq022WwpmKe1tfxHA34VsobpX2mpN1xfFOK6x4rjkxT6d8YPtNY0xFRcrDgs5VcqNk9DIke4nYUoEMB9vplHx7fwoptqwW8lEoR5aVzxHXUSuK4ePoyYJVumpoq2rMV1r69yWKRkVZFfCZyjYYtOdYcuEKF2EYx2UU5tkwWlDu6xNbgYC7G7iZi4yp2SxRulYty8toKbudp/r4nk2ne285NZPjoqasfqxSvz+skc3ll/ZCsuS5Eo0BWu+aI5svLEuw2YI4zI6hzSup05ueepMKQrJlamU4iVxdwBXbjHp6jKunLRYxlfPXOk+oxmHZrgQIR0zBV1VlrbXJ5scn/vJfMHu4r5yBh3SzCqipkyXLnuF79aCQfT2pSyjeYW6kS3ffH0aM2Jm5dUMrDi9C3CpOWKUMa0IjLm0otXi564UnYw9cVy9VWbJNjOMeJAxyjeu8qUe3H3eBWER4OramElGzEDSvboCyI7p1QvptrvI2rbJTU3MjpuVQORURq9AM1yjppVaEaykYu1dDmhY7/lzbdaqRHrxjbtoS6wobldf664mt5+fuK42gZDUJe/eBIMPAeNKBnY7djS2YNquVApT7PZuApmyc0zU5Jfp0TFnZ8fVBva8koP+ol2TNjDSQJxHyg1fLq9cf+N3VH4WLxKWWSyrxga6D7jS5XRiUoJCF2D03mRcvi6TfZRvpPW0YuN1ONsFsStehKsizweqpRVqC5kxlRPBQld1feT2l7XvHu1los8nCoHL+0l/bAx0XtmYqW5J/SCURmIuZgaeuqF4yO0YREtYbsCRPZ/2EwwwwYJZ4kEP242DOVMYORGv+kzXzfQscPshOK27VF8V6rHZavOt3GtpSAzzK4NvyiTcbHbqfL+a45fkSAbiWsOPp+s6GhprEsuxeFpyYbNDJ1TTcGR0jEzYfOxb0JeceQNn97KITUHCJfuE6YJJJvRmfUWzrMdjlDyvdkdNPfguwdczT/b8dJdVEolJjUuFDO6diwJTpgSoD04k4Wph2zVJ+KXc5P4h39BnUjO4XBTlpTOv5TU6FEJ/cqLBXPcizttWMKesiJHJqsYVy6ytfi4eKivRBydRWrmSBslT5D5cW82xEM8XrFR2tBsf+QQ0K5uewjp+kpKd0Jy3jUFVA7VI88V8uaXh9lafd7l/1GJXLhiJO89Vktd2jpKISwX4g854MsXt6ZpP99F6H/jZQdydZ8cpLWjbyi32IbgkbsOhSXec+E0m8Ga2tCbJxeG2e4k8tNs4tFcivWdjZ7MiqQwSULrXAj1QWcmv59ZJiJyO4BNeqbLDws6ElShPr+Fm4UTN2EPxrT+9xYVCnDQQYZ11W2EwekjT2FR9eE0vql4mdDqEwpDg5pT0NElb94Eukz0MLd7dTKne7gj7ZtzY4cpRAn89L42jNKuVXeea3e6AHyOmbSiMPutLQmaXCdj022mQupvUS+11p13rcOPTMBgDXJQ1/yC43F5Z1pq0Pm2HvdzEIqZ3u9n+GOx6LOMIZ9lGsNFnmEWgNPSVDKLF3r8NFeOQIcPEWRvFO0eoyoW4aUAyLcNiuQBlZHMSEwHYzh0X1kEkqNU+VtDNSrqh20uwZGecdDmIEhtuErXyHNa/XGPNxBfxqdksp/31tJC0Q10JKiSBpRqF6cR0OWahsaEpx1mpXbDDud0MZ7bYSlYkT9BD7dDKVSm17S00K09bzIfLSehXXK+r7ab01qaQBLubdKiu8XZuDrdojRYY8Audw0OUlK+RlGXZtLxJu6NhLg806JkbLOvtREtjcpIxGZkqebM/QEoXzpSQMDJ3Zm1jnp4ybVW0YYrNZjy27DZXWhyEZuHnOYZFWDOU3ibdbNeLXFhEt1V4CAaFu9RnPI0NP+WX9qW/eIYrEep0tlyc3KzhOMfnVsbEXS7bdEeQs5jTb2W5WqzPqDBUfQ4h44IoZHOWn/cp3vhBfgm3R1SRjWpbZWR3ouAWkZRJ1aLYfTStFKZpkiW333Ezby4R5NXBCdeK4yG4odaZjc5nH9gOw15m3bWbLKcSpNkp3P7stNZtp+MxRaG6tLPendCZMk0l0tHWTntWrzs3Mo3u2lJ0mcfigaDRMjxbnnF0XTRoMEtTzYISFvFRObU2wTBU1BE+fpju1ql97J1Q1E5D2Nyk22lgCdquQ8Pf7HxQ9+11Z/fXTrNcci/yWxv3yhl7pBtUuzqTEnae0B+z2l0EHQbYhYC2VE17bYfX0gLufQgyM+eGqbLMInL4M3cG0+scRENfqsP5TE6FBTE3goI0ULRcT5Q0qVHAdLPyjNOhafOThnckkNeXYLPINyqPp0m8yOZ79uof2m4yV9Kg35uUKlepe9KXLY+JrMPO1fhgzBkNUKqv8Ad0FXtrZXbFsJZwptPYnNtm60wdRogGpzztKukkU7iSJRJgpY40zvM1ZD4ZdhOL1pre8IjKm7l/mjq7ZMdN8pkPFKq3FpeugffE65wmCNwT17OrU4CkPu35WJvO+TUqTlqKO1GXupZ8FXYGsUYzIh570wQa756YCmVwNJuXwVYJ+4kfGtyx7ee06s0hnMQAA71Ic7fFmanJdzwn3CrNHwx8Nt32KBGBKhcCl/JKBSg53Z+6GdmnDiWVHKeSBtx3rXiPN9skX+53M17M9ONVGIhtB0Jlak1s67CUFw13U0nMDoOG1y/MNct8dj5hcta8+VF2y2X5srIOsgpuxWJJ0iR97LpkqKaBt+NueC5UtyQBq4vqlb6nriNsw3WLGbVm9pvbhVTNzDQoVYwibphfuCifZ25/MRVpHsj72ympJp6+xEmBEA8ayR4y/oAtWOF6azCTQFU3OIViymq2AtIk3cjyKm8m+ta+6ujlptGxf11fumCN7mrXV/GZ0GoGTcxycnoT9XJo1idfXngzQ22AwNf5XkbXjS/vQmaBTaCrZzN7WLWqe3aWS54y7cW1nLcHYk/MUjIwaBnDSW/qVocjvbi6dbmNnbNCrcE2oESWMbk58LBhv2NQtysiLvQ9rkPlKEetInbWFDuJ+WhaZMV8O4hskJkZyXNguavcSe/n18ptZtR5dt2Rhofj2HQ6TSv7ZnaiO71WM3yzTjibUKntvvNgKzjJqfNVFwKTdOe79XQWOp57ici0JrzTlF3NJk0vOuy1FuwWWrXANqKhxmtX1w+cAoSyZYRhjVZmudDtkyefSkgPU4y/hpNlxpopZ3FHfV1OJpssg7gc5C4fdHKd69ddPOksu8TIcHI+pEeWs+xDZUhBuL55mLzVFlzn35TY319ay5LXsrof6hvuafY8uRGobXnXs+bEhAnCmc7Vi6M4zT2HZpKI2FwX3c27NBoZ7NGbIt6APgfUfh0y2AJAIPaHk5pI7TzSF8pa2UtdRum7ptXW5R6jiZy2uHZG8M7F47F2ptZ8hqJ5oK4u5+V1jjqnAk1vuyrB1keU6GdD6Pl1j9JMo8rrQ72I0mRITslwCTsTK9Bkz+sqvr1EVZM1VzpXbIyg1mtujne1EtXz40pIS5ortwutIVF/i0tHGl/HmWN7ZRQyE8JOFaE7thoZhnpbUrMVygnSviV0b7PnuKfnp/vL16dXHKo+fX4az/XfT+f/3QNefwiLt3cp5BTHn5/+351DPs4EP97X3Y/qgeW+3ld//fcU/MfzU+WEUJnHcXCdtP77seM/nbB++VcnvuPM/vG+eHyd2DUfrzIay78fRoeZ29ZN1b/VedLej6IhtG09/j+R+u39ZcDT3Zi0GN8sfK/80+cR9luTj4O9cBxyf0+bAjd8DBm/+u/n9s9Pbg/dFDr1G8nQb6AqRjvfXxuNx7Hje6On3/4vp458++4mAAA= -->
