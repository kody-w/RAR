---
name: "rar-cowork-cookbook-scheduled-brief-develop-project-approval-processes"
description: "Schedulable morning-brief email summarizing develop project approval processes for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_project_approval_processes", "rar_sha256": "f7212a4cdf82884a10199f586aa48d3109a8418525954ff8f953c68c19b83828", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_develop_project_approval_processes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-develop-project-approval-processes:a04e295bce868c8fe833a7f0e4fbc33e3451272a2aabfcc010aecd0bf8ee2c75", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_develop_project_approval_processes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_develop_project_approval_processes_agent.py` is
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

Develop project approval processes Scheduled Email Brief — Schedulable morning-brief email summarizing develop project approval processes for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-project-approval-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_project_approval_processes_agent.py` and embedded as the fenced Python below (sha256 f7212a4cdf82884a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_project_approval_processes_agent.py` first:

```bash
python3 scheduled_brief_develop_project_approval_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_project_approval_processes_agent.py   # or on stdin
python3 scheduled_brief_develop_project_approval_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project approval processes Scheduled Email Brief — Schedulable morning-brief email summarizing develop project approval processes for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-project-approval-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_project_approval_processes',
    "version": '2.0.0',
    "display_name": 'Develop project approval processes Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop project approval processes for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-project-approval-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-project-approval-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc2f2fc68f98a324',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-approval-processes'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-develop-project-approval-processes', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDevelopProjectApprovalProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopProjectApprovalProcesses'
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
    print(ScheduledBriefDevelopProjectApprovalProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aXOjWJPuX+F6PlT34LLEKvAbHXFBIAkkQAItSF0dLpbDJvZFgHr6v9+DJLuqpt+emZ6ZD5cK2yzn5J5PZkL9/mQ1dZCVT69PBrBSZG7FcRiAErFSF5lmbVae4Z/sbMMfxMnSugztps7K6un5yQWVU4Z5HWbpsN0JgNvElh0DJMnKNEz9z3YZAg8BiRXGSNUkiVWGV3gfccEFxFmO5GUWAadGrByeXax4uOGAqgIV4mUlUgcAKUGVZ2kVDmSzNgXlP+DuKvRT4CJ1hpRNiriQfI/A9S0A57h/gaKBzkryGFRPr7/+9vwUwvOn19+fnNiqqm+iApcf5BPuwqzvsnAPUdbvkkBqsZX6cFveQ0ul8DoHJRQvgbdcqN7j6qcKxN4z8q//em6t0q9+fv2SIo/jy9PwT4eiDhrVmVXVUHrHyi07jMO6f0G4uLX6CipbN2VaIRZSQUOn/st95zdK0Ga/DM9+ujN58UH905enDIpgDW748vTzYIcvT9As8PxloJL/9PNLnLWg/Onnb3Sqxr4ZHhKDUr+8Pa4fZOHCb0tD78b1F0j17nAbfHn6TrnhuMs96Al3Pr1EWZj+dCc8GBOkVuqAn37+K7LQG845Dqv6v0T31zvhAFgu1Okh+M/PNyP/hqAPhT5o/jXbHLr172gCl7+ze0Yehvor2jf7/zvScZjCuH63+D8l9882oL8gv/6lbv/RhmfE+/IkgDi8wOiA6fOK/P5mrMXpr5/cbzc//fYHJP2fkjGypnRuFN4SKw09UNVvb79+qm63P/3266cmh7EGrOStKeN/RvOf2fXG5wcLPlb99ONeyH+XnlOY/chHpCO/Z/n/Kf94QfZWHLrf7levyPf5MhwoMijxzvRugu9ypoKyfmfHn5/+gICRQm0a5/YYZvm//AuihE6ZVZlXI4aTNfWAO3WYgEH4bRBWyPaR1F+NpbRavSTuVwTeHdIdQoTVxDUyLwcUfCDeoEHmIV//r3OD2M/OA2JH1Ts0vd2w8+2BlG+PfW/vSPn2gZRfX5BtAAXJytAPU4ihOrdeI5YP0noQ4RYsEHs/XwYpoIThHYX0qTQgUAV5/QP5+vfZvt04vOT9oOiXFHrOCm+YDJI8KyHQQ0i2BiSz+xp8hngM0abM4ti2nDMy/Gryl8F6hwCkD5s6sP6ADjhNDZA4c6AqXggx/HmoAVl8gcg5WLo6h3GMuGEJ5crK/laooDdeB2Jfv361rSr4kt6hmkDuBaoawQUfAiOfP+cl8OLQD+ovKXCCDPn0+x+fkH9D/qNdN+IDjzWsIY/KBCWUDU1FYO42CVxWIUPgQGC6+fb3P+6uGaSDdQuBGRd6IbhthtS+Bcqgwd1f786COg8igvLB6Ue7IW0A7YKENbQWRIHq+Us6kMjg0rINK/BuxPvmu+nfvX/nM/iketgQ+skrs+S29hajgzOdrHRfEMlDPiwF1YV+rQePBllVw7DOQeqC1OnhTqv+5sI0q5EKZlbl9c9IU0FVB8pfbUh6ME4C4cuqvyLKdA0rYRa/F/FhEdydpeHg+Ef43m9DIuUnGGP8O4kXRIXxWSK5VVp5UFoVuK3zrHtEwAr4vh8St5AUtMjQAoDBR7ecv0We8J83IR+NAiLeephbv4B8afAxRiL//zQ8gzbcfK6Lc24rCoiobvXjPfSGjm2wxL3Jg63Gg80ADB/txztSvWP4lzQOobvK/h/3ld4t2u5r7rjYlFAYndNv9Ie8L290wxrGzBAEZTnEufUlfS8Wz9AN0GPVgHswtc93Xd4ZDk/fJQ1g/g7X3xoH5B6OQ5rAQEfyxo5DB/EAcG85UQflkHEPp8AAAkP2wRRxgh+0QiB1GByQPgKFCGEkQ+veTKfCzBmcdEuDj+Xh0I5BKdzGgdLC1AIvyGGIdOiBCrGhO9thDbTCpxspJAHQxlDEDwtXgZXfhRm66IeA1uCLLLFq8L0HHg9h1A5VCfL7SElI1XKtGtqyhU6AGdfdPfsh58NXUNhkSI/bph/d/dAV+b6q/WNISyjjtzoBG/9bKH8zDsTyMqlu8ARL9bmCiZ+Ajzi91/6Xe/m+9wcfsrz+aXT46e9NF7eCvPvRc69IUNd59Toa3Yvme818cbJkBGMkzEH1rX7eU/HzI/E+PxLv83viff5IvB843Q33ivw9aX8g8QjzVwR7Gb+Mh0er0AFDHD8OaJzpZ/74mRyefkl18M3rj9AYIBAmuN1/VKL3JbAc+SXwh8X3ylQNBa2FNfQGiLfK8hEZj7yBeJv6Qxmtsu/yedBp8PPdjR/ADR+lQ0lwhwbRB8MsFQ/iV+DpNW3i+PkptRLw35ihBqyGsQyNM0xi8Dnsv+oQ3K4+erHh4sep8pZxECrc7HVIPFgXYd/8jHy0wM/I+1ByG/vSBk5lvw7t98ASLoV/PtZ+jKw2eIJTYd3ngyL3SWvo+h7d+J+FGPLtES+DLO8JPHD8ExF44vug/DMR7XZixQ8UqWprqKawiD9y/z1ynxFoS5iTMM0gejZww5/ZQD4lKBpYv91B3W/2+6ZWdtflj5sZ6vu4+vvTO5oM5/dm4h5GA+3/fgs4GPm9dL8NrKwbwaFRu9n81gC/QX3DoUR/98gf+o23e5w+vUJwAs9Pg2XLEHb119v4/nSXDyr2rXWGFCDMfK6GlmME0wxSgo1APih1hhD5HYPhduje1g8nr3/db/+X8eLVGpMAZynbAQzNOIwHGIKwJt4YkJ7tEAQgSArDJ7iFW5btOc4YG1vAcce2xwCAOxMKijVwTayHWCNs8BJU6MMV/wtTwdOdIixBOEVDkt4Ex3CLdFyPwRmGtLAxxrIexdCWRTIugY1ZiyExhsIpliI9j/FYinCgehhrMwTcMtB7dKF3Md/eO/53v92B5A2CcRIOSkD1HcaZYKTLTizaAcTYJhyA4Zg7IcCYYgmPYQAJ939sffhucO3dEkOcwwYUtn+Xgc/vj1gYYpcm4coFWUnc/ZiO2L01wie2HqxQc4x23YgMGuqQqdp4vwZ7ptAUstnw6jwKqWWbm0fZOxt1YUnBuZnvHExYbwI009nzpU7cHJyXyj53osiH6+WrjLvpCfeItt3zyiI7m0VUFdLutDeZUpatnl96RBUqi3C7nM9NsceNehyetsU28gwZlwNqfzBGi0k5GVEzPU6NpF8ua4+ygvJaJPJyjLd4VS9H5CqWCGK0qYpAvOytcFccK6fQZNucuwWa8W7QsH04m5rHsOh3uyUbVzyaNHFZyrXGF+46jXvHm5xZ1aQkYoGOVHMm0DOS35/ks+sUHR6rF4MszMPIldxC0uVjjwVntsXZsR1rMEvlXmHysanEBcpwxioyz85041vyki4MQe7AeVZRjiVGUKSjF1obYj4zdT/gu/q0pM2+3mwlZ2fv9dilplJ5DuuJQDBOaWYUxi4r2vSMyMnjNOfwcyEvA+e6FU8k4VjHbbXfFNFh3/OnlJMO+4gSd5prEDN2n6U0RUymi2lTV7q94Xh3zkrFfm0x7Rrzk2S/t4U8JFa6oQlsLVYhtc93y85zy8NpDaJjEHTzJmw9c3EVg2q2MOwoLmdJuatKQ5+5ziE0XHlUneYYnTTuPj4u+2p9xbic32Wau53vap31NiCni5q1jNK8ahrPGev8ZFdob2HseNPQOJUt7OtRMfpe3+eJhXsHe1SrU7nYH8bKUs9TaubOS6lRrZwwZiK+X84DNZQ9ptL351VFLi9NftrtrzN02mhmWJzC3iE3Z3V0Xcwk6IGLy/XYXjse12sUs2gY2aqLWcC6HhzJFifOZSuVqsDTgYHvk84HiWAX+XQyv/0Ik1k+x1esT181qlkJJw27OlOSnVHogmXkyWEdH2Qyd7ALzh8rOhEI9Ohl6Wx8NAtbw5nNSdHrcAWmubpriqt6lVXRKQ8FJhWSdLVOU6eq1/xlpcnbSjmUbOvsF1VuU0Z+lgV1tzpMMi1xXUvA7DVDSwf+XFORpW4F81gehD23DLrZeTM6LnkpJZOTGLeB1HfV6SruNxtrtp0lYD5vnW1DTVaRsypQvi4L60zsDwCEynireap4jXpdHY92SeJVB6GcibU3yWflaK0ekqu2wZmzi9pruUGNpAQL7zAaMzTbytYCN0/rKliNYDqWfoebJK0bfEn212Ovu/YGIvhWOZK2z3Z1JDjc2lkvtvt0m5MLipjKEI+prMeka+qQuU0Huxa7sJO+IqttdSYc2dKihT7DRqy6l/faniRxfbUpybwwJl45OcSxx2KSkat6qe9LTp6PLFNimI2xBzWWLQXXQPWGppZLzCqSjTpSRP0YAp5FNyRDhZaph1kft7mMSjMcd6fOfl36wazYHX1sywQwMfX9PuabejylD6uG2zlnsqo6nORMLp2m1uzk4pom0rq+3FoTbu5bxFpT56c+jkl7a/TXfKw4XjBtZrUwyz1rpkzTEi3mkZljYcfmM60s5DG50EZb1PNPjcrxfWEvw/VUO6lXj1rvtonVncY2ub6y3AK3MS/MmMt046wn04N/JSo5lM69cVnN6QpN2XZddqJyYY1ZmVtRqwjoyUX7/Hyy9/Npe0GnUr3IpAXEYjm4MtJCkfW02+Qoe7jmNDsNEg7wEb9L+BNV54QgtYvdNNvMN7M5ttEj1o+3kbM5XM+2qc5s/6wZPYOvmtwCM27aiVW7FiV+F2Yn81BXrsQxgRnH5TJUj1prOPpmkzX2WsF3U+O8R1eXaappQNu7/rjSKz1TqpqQZTu18CN6OqW82UUaSaMjO8e99BqjnihCQFT4nCBM0tmjst5P3JmZXHGN71plUo6vqrZYd825URtwNJ3tdBFLSd15RMwkJoGzI/ViMtllYl7zhXNqpmpIXK+lgzXttp+NdMnfUPmiuihLsYhAme6MkxKMYEvi4GSyszW2HR82VkgDrqWik7venVRDkjW0W3ZzP6kiayR0My+nDK88UWkmRUVWhGqiFYsrhdLJqlAuaKiP3ZiKhJPNh1wzJeIRICphvE18H1MWgUkdowXY9mUUFSWIg0409VkpTYod62a1YGyZRN7w3cUfKbFD92iUqKgiumGLH3tKOPo921nthg8w0cOtEtqoIJbyxWcauzoYu+vF4jJD3qWBHpfApnUK0DhuECIhLqZj3LhUE9DhCr9K1uUGs5e9wmPzar2L99cDUe9GpEmKm2U7b+vkuKGxw+ooFty+nB0x/ARHfW6NYxFj5zp2sozeN/Le9dRGWoT+Xr0asIpcD+NZ5zCYfKqVBhQrunDygyJIJqeIvN0qxrQB4bnFgS3jI55z+WNuFVvVJ04udkbz6VXoQOKLhpTsZiILu9fKxkGMnV1JF7eawnVkqnPnxaWs52p83DC7yug3sSoKjdBsF9zF97qEjvfCRF5iSzSpL0G4XruqeAi7kvNwooozfWos3Oh8jBSZuJpnmil9Isv0MFDxvY4BKVhvC1jl15gaz+LVidxTKp/ZHWMaq1G6P+7Q4BqfNsTGphKiMbJZn419wRyb+nm/OIn+cWrk4bjxaDKjdyOdlwxez2Zowo4qY2zIGLbSuvxE0eeVPO2PF62Z82O82Vtx3kfLaLeRT/S6HqUl1YttonUrI5+pvmspO5fJTtfJahueMZpYHNCOPTWlVGNaibtV50TLvZC6k9KMfO2UhYLmN5rn0qK8GWdH6ShYx7nJE7Di9GvVB1I4NmxRcwXR0/vOS0+sHkWHw2ykKdu4Y7a7ZdvvSj1n9S6YHohdUWxLOt7yzMKqfEoogMHQ01M26pfm0hKoDY4JEX6pjmDjL/1R01B6pToi2CmrAmaFIZrdmphuVecQS6QGwmt2Tk6tEYfHmRLO54nkE7ykmqxhd/OtWp7y4sz1y0nDT1bJmeHdg7LrNCmmVm3LWZxM0ArsnEYz2dadhKHNIjurynkqA4sUunw6D5WwWCyLxTzuqcVhm8X1NRZmLnskQ1hByHrricfc4xxsTa/k7b44TPLeX3GyUhP78a7aL/Zz9CQKp1IpxdN5SaP4RYNVEfZAhdleN6gluIJN9WWL2ZyFOeZFXB3CyhYPm9i9HkGytJJltjaP6LUEe21krQhxO5GJYyldGgXdJ6fmkJln092JVNGmTSgRohU0Dt+Kobyb5NqSR6t4GSZSU/E7qXGC08INVplirzXY2hArw2Kpim18Mcdq2WtVGdsS8mSxOFDqVAzKPWU2heVv1L7AKjHtVUoO8o2qiqntH6TNhM4yzaSsVkrDTNeWMr86W7scs8s0FnZkZB98h6nzTaqdJmUumaWF+p6jB4LMlmlW5guu8M6CHJ8jw5ZDVekOzuiMucudnBOkm85lnw1zCZsuKFNLDkJyqNR4yYeZp+wYCQ85qtV3EL15oZtEczfdBK4SQcTjRugeLNYXP3Wbqxwbu0w8HcEUv2rBBg430dZOt9i2xGZnvN3olh7MUT4HEScS3Oa6xI7jWbwZp7bJ+YvaQSHqkLu5wG4tGuzb/b4vCeN4VgO/pjnGWq7klj9MLxrWt1N0c8216aWPrYU9qYBpzYUi4i2OY7nNkgUoqdE0Xo+5/aZczoRF6slFUUketF+5wYtIkRw5sKRxLWYZ1XhBupflenToUiPqFOesZbPu2KRRMUaVpdBZWoOXmTH3Df6EF7BTMOpgYhs7YtJdPNqXpSNTCPWxWlSzJkadrmPOEzMal0GOVtg6GLnGZX1I+ubaH7H1Lg0pMAnJS3DN8RMx5yMbx8mI0NJNObVSeyY3YzKOM+vIn6oRRJPthj9IuZtr0YGmZYHGt/t4oi7OsxwLyO2sVHpHSXnJ62zqYsmMlMKhroq3wBZ6OBYEs2Or8HITVjJAV87BWOGaud8fydG2wyydaz13UU+7hE3iteyW6rYdn5JRagOwEZxwHVWKm08AWqNN1fXagkhHo8neYziJivF56pQEukwxWtLoarJdUFjkTJasuHQzjdw74dzK6TU3tpbE1NSBkytbfGYpa3qxMiSJj84wDahNclxtov7aiqg+Oy5ylfJRjpQXzUGHczY+2hqT/HpJ9FBuljG0YWatYaduHqp410U7oqplItA05qrIp9iVkrnZut02nzO2FpOqeCkjjNit6AjnyUm0apNrWK7wSYCurnUdopuEmTMGqx6LjHe2rBAs2CW6dqaJpCsVdVYx0U3l8BDU9ZKhtHiURl7p4ZULJGoTC06yzvgEpuS4RQ9Yu1YNOGKjeWiuzLLeaUup2XBNs5QmGlbb6/4Yo3lc0Tbsx2zWoqKl6V2O4xElKI5IaXzqXhzmIEXrTtv1oibNVVyKxla963CpA5WHzyZ0yUuKALN3TZB2GNTTA0lXqXABvEZIjESOI6otFIg8VqcBdooqyYiz4QAsuxgbr1POWWKRTG4OkVhtS6qyY2IymrAKd615OhOqw3FDaOix2fYSyXHXXSsHXGWxCiNM/U2/yqymHa1xjqn3dSgyzuiwb5N6yvjx6IoTFnGa1KtK54jQVa9jv+qM7lzNUjy11VE0mc+DZTabTIAksQQ0A0CbDMNdQrtW8xHgp/jBya6OwF08wM0vCw7fqYIXLXwH88mrRNITatrCJh4cms7Ojxx5XPF1oTXnA0mwi7I0T+IEM/XrJR7XTlAWW3tHLvZEoy2KCYAm8zbSctUE9szbGBe76taSECpeT43Xsd6jWxKsDbBRYxPbq/QSyG29JQL+QnIYOgE+uggBW+MXsm3tiYeZ48htHHYE4UUZKQpKsAwdC72vXi+MnoGFObl4WDM7Ta8HbE5lEtNUljZy6VYj1mWNC6ORPJHQ+QZ2sO0cReMJ6UtzY90slx43H03hYF3Y6Sq+RPx1XFxwZexImDbKyqNXW6N57M99LtGsBI5oLNrEzmZse1TohAEJ3NwNcaIr0pkjXVR/LBfsFfqtvi647VixPZGbZ60mZvrJ2eHH5giC1SnqWTjCGhh7QdnZqqMI0gu7A8cIoeji6+ZYb/vJ1AxIZl0lddleLuRid9QMrnYkvXMs7qKQjiIVl45v9HQnaIKyOdFnUlRjnL6MpaVLZDmsvZOzQPa9oLNEVY0vzOgoZufqEm79CU5jl+vxQPfkNgeTJaA6d2yd1iRrbpNphs/665Lt+5CuO7Kws0u34ndw4qbSvF7UDZVpzrhnFoKvjjtlHo47IM7nZyvE+DBHmbbdU2PjhC3OW8XyqEtEK0qiKSAQ0BGO84ptKSAatZwUwnzSpxnHcb/88vT8dPuS/PSKjRl8/Pw0fFl4fB/4n71O9q9h/vagTUxI/Pnpf+9N5v2t4vvXxdvnAmC5rzfur/8TsX97fiqdEIp4fyVdxY3/eJ35797nfv77b50Hev398/nwobSr3z/H1JZ/e00ewsaiqsv+rcri5vaSHDqnqYb/YlO9C/t0UzzJ68cr6O8Uffp4v/5WZ8N6LxxWhenwDRC4oVWDx6X/+NTw/OT20NehU70RNPUGynwwwOPr1/D+d/j89fTH/wNGt+LuYSgAAA== -->
