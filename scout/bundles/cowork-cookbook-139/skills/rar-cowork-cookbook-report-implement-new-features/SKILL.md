---
name: "rar-cowork-cookbook-report-implement-new-features"
description: "Builds a structured summary report of implement new features activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_implement_new_features", "rar_sha256": "8ef2387926ab692670d2e286f1ed2c03e231b7b34153e17f172f1ede8cbe3e00", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_implement_new_features_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-implement-new-features:6025bb9c42b7673554163de662376614b7e09ef6ccd9a7ad0c875e5f12d88516", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_implement_new_features`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_implement_new_features_agent.py` is
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

Implement new features Summary Report — Builds a structured summary report of implement new features activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-implement-new-features
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_implement_new_features_agent.py` and embedded as the fenced Python below (sha256 8ef2387926ab6926…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_implement_new_features_agent.py` first:

```bash
python3 report_implement_new_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_implement_new_features_agent.py   # or on stdin
python3 report_implement_new_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement new features Summary Report — Builds a structured summary report of implement new features activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-implement-new-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_implement_new_features',
    "version": '2.0.0',
    "display_name": 'Implement new features Summary Report',
    "description": 'Builds a structured summary report of implement new features activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-implement-new-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-implement-new-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77ae80761843bc09',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/implement-new-features'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-implement-new-features', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportImplementNewFeatures(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportImplementNewFeatures'
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
    print(ReportImplementNewFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOjVpbvV+Hl/GG7lZViR8qOjngSSAghxC4QLkea5QoQq1iEwOPvPhcpM6s8Y/d0R7x4qigtcM9+zu+ce8nfnty2iYrq6fVJB26O8G6axhGoEDcPELboiiqBH0Xiwf+IX+RNFXttU1T10/NTAGq/issmLnJIvmzjNKgRF6mbqvWbtgIBUrdZ5lY9UoGyqBqkOCFxVqYgA3mD5KBDTsAdF0Iqv4mvcdMjXdxESFM0blo/I00F8gB+jrp4FXCToOjy+gWKBjd3ZFQ/vf78y/PTyPTp9bcnP3VreOlJu4sTPkTtQbd+FwRJUzcP4Zqyh2bn8HcJqlNRZfBSAE7I+68fa5CenpG//S3p3Cqsf3r9miPvr69P4z+tzZEmAlBVt26gpb5bul6cQhNekEXauX0NjYYi83ePxHn48qD8xqkokX+M9358CHkJQfPj16cCquCOPv369BNSVFBe1Y7fX0Yu5Y8/vaRFB6off/rGp269M/CbkRnU+uXt/fc7W7jw29L4dJf6D8j1ET0PfH36zrjx9dB7tBNSPr2cizj/8cG4rIoryN3cBz/+9Fds/Qj4SRrXzb/E9+cH4wi4AbTpXfGfnu9O/gWZvBv0yfOvxZYwrP+OJXD5h7hn5N1Rf8X77v//xjqNc5i2Hx7/U3Z/RjD5B/LzX9r2zwiekdPXJw6k8RVmh5eCV+S3N11ZsT//EHy7+MMvv0PW/ysbvWgr/87hLXPz+ATq5u3t5x/q++Uffvn5h7aEuQbc7K2t0j/j+Wd+vcv5gwffV/34R1oo38yTHBYy8pnpyG9F+X+q31+Qg5vGwbfr9Svyfb2MrwkyGvEh9OGC72qmhrp+58efnn6H6JA/EGm8Dav8P/4DkWK/Kuri1CC6X7QNAgPcxBkYlTeiuEaM96L+VReF3e4lC35F4NWx3CFEuG3aIHzlxikC62GM+GgBhLZf/69/x8sv/jteTh+w9/aJeW8Q894+MO/XF8SIoMyiisM4d1NEWygK4oYjNkJp97yA+PnlOgqEysQPwNFYYQSbuk3B35Ff/6mEtzuzl7If1f+aw3i4MEgB0oAMUrlVnPaIO+KT1zfgC4RUiCFVkaae6yfI+NaWL6NPrAjk757yYYsAN+C3DUDSwodan2IIw88w2HWRXiEejv6rkzhNkSCuoHMKCP8jfkMfv47Mfv31V8+to6/5A4AJ5NFD6ilc8Kkw8uVLWYFTGodR8zUHflQgP/z2+w/IfyL/jOrOfJShwDZwdxZM4hTZ6vIegRXZjg6qkTEdINzcI/bb748ojNrlsOnBOopPMbgTQ27fwj9a8AjNR1ygzaOKoHqX9Ee/IV0E/YLEDfQWrO36+Ws+sijg0qqLa/DhxAfxw/UfgX7IGWNSv/sQxulUFdl97T3zxmD6RRW8IMIJ+fTUe5sdIxoVdQOTtYT9E+R+Dynd5lsI86JBalgv9al/Rtoamjpy/tWDrEfnZBCU3OZXRGIV2N+KFL6NDrqLh9RFHo+Bf8/Ux2XIpPoB5tjyg8ULsgfQm0jpVm4ZVW4N7utO7iMjYF/7oIfM3fsw8JnE90q+Z57w59OC/j5WPPo88rXFUYxE/v8NIKNqC57XVvzCWHHIam9ox0cejRPSyPsxVI384DTxKIpvE8IHmHzA7Nc8jaHvq/7vj5Wne+o81nxni7bQ7vzHIq7ufOMGJsAY0aoak9b9mn/gOVR5TOZ6hCZYp8lY9cWnwPHuh6YRLMbx97fejjxyazQaZi1Stl4a+9BTILgneBNVY/m8Ox1mAxjdCvPdj/5gFQK5Q89D/ghUIoZpCX13d90elgGchx45/bk8HicmqEXQ+lBbWCfgBbHGtIWpVyMegGPPuAZ64Yc7KyQD0MdQxU8P15FbPpQZp9Z3Bd33WHzv//dbMAHHtgGlfVYX5OkGbgM92cEQwOK5PeL6qeV7pKCq2Zjpd6I/BvvdUuT7tvP3scKght/QHY7ZY8f+zjUQlqusvqca7KVJDWs4A+/pA/Pg3pxfHv310cA/dXn9H4P6j//eLH/vmOYf4/aKRE1T1q/T6aOrfTS1F7/IYGPz4xLU7w3uy2dNfYE19eWjpv7A9OGjV+TfU+wPLN7z+RXBXtAXdLy1i30wJuz7C/qB/bI8fiHHu19zDXwLMBRfZBBXRr/3EFs/+8fHEthEwgqE4+JHP6nHNtTBzneHsXs/+EyC9wKBKJmHY/Ori+8Kd7RpDOkjYp9wC2/lI5AH47AWgnETk47q1+DpNW/T9PkpdzPwv21eRjiFOQo9Me53YLXAwaeJwf2X2wbx6I7x+x+3ZvL9i5uOBVWMTRHCZPyJm3fVgwrqNVZgCNsVqJ4RqG4IkXC0phurcOz8HrSuhpAKglH9pi9HfR+bm3HQ+pzC/qcG90KGCBQUr2M9w94JJ+Zn5HP4fUY+tiP33V3ewv3Yz+PgPdoMl8KPz7WfO08PPP3yJ2q8z+F/rcQ7yDxg3fXGpjia+Cc2QW4VuLSwCQejPt8M/Ca3eAj7/a5n89hJ/vb0gSPj98dE8MgqSPCvjWyjwR+t9m3k6o6098Hqbv99DH1zYfDHlvrdrXCcD94eGfr0ChEIPD9BYjjYwNl6uO+Ynx6qQBu+DbCjYm71pR5HhCksMMgJNu5y1D+BOPidgPFyHNzXj19e/2Lq/QtQeKVRnPK8uU/iHkMzBEWRGE0EgKZxgqFpjPQYgM7Bifb9YO4yboD6M4YC1AnDg9mMwmioQQ1TIXPfNZhio++h7p8O/vfG8KcHMewdOEVD6hk44cSMmeO069HwnUEDHOAz+oSBAPdRAuAE5jEeQWIUATDmhDH4eAvMfA8QAL077n0WfGj09jF3f0TjAQxvEEezeNQXd11/5jMYGcwZl/YBgXqEDzAcCxjIkJoTp9kMkJD+k/Q9ImPAHkaPiQrHQDiEXUc5v71HeEw+moQrN2QtLB4vdjo/uIzFnG+RPa9ocJTO82R7c7EMxY3DurZnRgWq4zqpGZbg1O3muDol+vZyFKpkKHn7IG3ZTb9UMt2G5Qn4jbjPGNdZsZYR34ZtRvmTYJJvrq25WqmcRNmaW1pi3KzLxomrTHN4y1473sHVPUlb05Vg6OlkekrsmbvTXUtcr3dH9GAOxirbzPeynFG2HM1nrQEL4RrsEs3F0FZzMluqDpvirF706dJziuzI69Y1IfoAtxedvMkxut3VmJ97NT1d46Al1sNkRbaYHhtnRS+F+kKIDk8J+ECiRTq/iNbS6ct0T0fVXDREUqTFPHFL7gI5y8OcWLUmdVDcw5AIrcHejtfAPUrx/JCKErVjOYdHuxUvUjkcl4QUW5pED7eyTr/bk3hb7677TL5dmvnhJra0PmUp5XRZ3bL6KEZk0yWBvFjmKRgOkt8lSZlJFc0bJavWO35Q1vtkuB7026xtZl0kRLUZWehiaYOdLRfK1m590maOqk/JV7xOSNG+nWcXXSxAoPOaJcLq6deiJ1bbuNyvp8ZmeZv2wm6l1zzeu4tbtSbELsv0DG8sw66YAMfk4eaLZSmlTbY66LwvJGRSU9Zin+Fg2+aHibczhqrgRfF2BrJle+2Jmlky7i9dxaM6xTJYRri1A7PfmkO7s7Cojw/WIZMvmJZj2LGeUXaPquKUoqzt2uqyG3uYekvdifeyzxEXl5r7w5T15V1pSze2qQtrNU8h1KktiYPUPbQev0mUTPHM+f62E2p2qJ0zvge80mBHp7/einBj6yEThAnqVts8kjsHC3IDNjVJuvFTw8Xb5XLCrKYr9LQUJp0fEnJ6NLMpefI2CxpcNxzNSRIXUyaNOXXuzpOLD7N92HjssvZsR8Pt1WRL8dsIE4RMm3QBf/OECWvxtZ45p4YliThgr1vDUcMV6+2ZrTEUMggEig0Zua46c53sndhFDc5e7WRusQgXeHyRGElc7jZkRi2iLqqvK01dapLGrxNTwJz8vJQ2Gk7Okr5do2BtD3F2xmHjXmGbc6zGIOZLhVOwi4dK+oxNndqmgbtuEz9SDuh5JtjOdd1HuclOmSlp4U0o1A1+bQntAObXUt3BfLbViUYvXZRIfMKIa3JQljvOssxl1Th8KErH6yRxlAstJmfS8brilkqp6MyLOKSl/jwVWZWs+WDlOJW2CyZ2u1T12RT3uYtceVo9m043bGpwYgAq7TysmdxBpRXt3i4YgVm6ynaXBuw4oZ/bh+Mxn6v6mUhN91BgZpAoeTYcZRFfKtSCFJccqlwv2yM/mySYt96F0lKZmvHMtcqFqDApi+qmK2mTiT5bKc5usV54rqf517z3FPmYqauUObLVTsgDnHWaUrqp9HkFhOm1cIrLQcp91Ltpy9jhOfSqUrMs59cqcbH2LCll8XQzq9zcNI1rRiU+7R89Vy+JiKk6miMqrcaDzDmI7mQRmUF0OsyLtLZirCBchWztUzoZTjOBH4DI1ByHzpiZxBpmsvVo+qaTkx74jhhRxOXE3bbmwYgPOefWTiedMG0R77BzHhWrcJdQyu1Yn5acF+0FZohEJcWnMiE4MmivWg80JrW8iyNI9EI28qW+db21szsTJAva0h34dUZTkh+JaqdlhN3h7nG1x23HPF7c9XHJ7EVByBVB3LL1dV9rQS5Za7U7CJJ6dner5KA6WjGElcIZLbDQpbC3ZMXyOau7KNZkY+yKyd7J6ikf7L3bfgJyh55dB7wya63MidONMJOUF63psFtPG30fGqZtFL6BTqdSwrYyyZwbnF8eL+qOoVW6rnObGCZz6arkNRFviektBIK9VAl5VldekkjsZaEy5rVkM+q0OJl2eJGDYXPwSxXCXEzrpabw9aKn2UOk3PhQNQW6vWzFgC836cYWeBQd9EYNUM3cBKuL3Ki5uphIEJTxeHWIlp6h4ebkcl7P8TLdNUCJLkC+iLKF8U06sy90aury2YzNJrnKy2rb936fuUVUTSJq36YnnqNcL7zyyc50lFWk9/Z+p52KE1gsWm3RziJAD3rqz9H9kQgvMBrUSQijHaecSYoJbnGJpZcIbthNIpVuKO6R3Ukw6ETkyHTdp7qsbGx7Od0uSa0wsyvswIyz6iIHRLHQOjR/yFZqdqCacjPUEBbP1NkIp65J7v2qpeeOqNsF38QhELP9zvRvZI1rMwIcpKhmY32/MA5E4EQmvYu4xVngFpciq/xp5KyIOOmbQMDYaN+p82UQ4tbquuhaUSDXdAajdi4pfeP6lA7Uix8mTpCmIPLPfMNKN9eW9EUhK2KTZrM9NqtnpY5CrFI9sEp9lMyN5kLEHEvmydnhDosSb4bZsNfq23wHzvhZTXYpQ3fN9Rh3cC11yYQqXDP7aUGnarLJpSm/6MJA2la8Gc6vE6rjXJHVFuUJFSUDnLcqK9Lxej+Jp2Z9gMBty4BDh2WIrthhK7vbQOKzDk4kw8q0BEBxlwV91WWtX1k5Yx6VIJKp0wR1dNUp2CVKT4NO9dDzvIVwt+y6g5ItWJa8ymgBSDyW6KyJYzF1ym42V4iTMWfovCRv29UmVoMeOI1HnNRYriwPv+zl23B2jpPmgOXZjachUkq2QPPW1MsdxyrEw/osLKurRXsndBVySzOs9gHmk0Gd2kKPL2dxb0m1Okd3y/kmzZi94aY0jxYsibnnhOXSVKwkakktZytqKw4+OqdcY7fWhFk5VfXIUPXNLjj66faWHNCLuyr7oeQ0SdRif7morENMX9moSowhDzzLDf2FcM6izCHzM1eat7UyQyNKV+dlaZq7oNPDQe5gsJeHPR91t4u+1altUUoUkehKfsXPwkXTLxlXYCnaR0p8nRdtraJcPGkcZ4Pih+JGr4vVTDPA9cpODq3F42RQONwOiDjfWGi2wkwC7XMx6ZdE0bsonGwSkQSAA+7EqVZhT/qXsAk1B0wma4LYVtuUp1Q/qbJo5+QDIRzDFBhaSNspl7AH3tzJYW66zLLUcofjaeAreIdNulwWlPVsp+7zye58u1GFptC7g+Cv6D5y6kgr5v7ElI6+sb61xXq9UTYaawUTrtxE5OoSaQ15sWZzX6pWAWGjDrkVdb7D1qxvJpFJJPgQb3lftJSi3eh0STEOl9k7wp4UVjQ5nm1n5xEcujuemyaM7Ek4mdRCQXNlTmfJ9riwCllcykVekzhzxbYhL67InNqXWKfn1YK9SJPiMh/6Yn+o1gO/LeMVPZBHfHqZyefVfGEU3jG2Yx71Nw67gtAxNQFhLL0l4xnTLJbUiJrb+L5hatktj6s+2e3n1n6NUrLaa2epzMVBtpmAd4v50QCCYlwuHdasojYR2x7Oz2h4IPSLxifxyfazeH8wlU0XbIka41VqmQyZywUsP0VThhJjvypXZMNVkyXOHLJwldz6SYva+ITTjcN2PZ+Gl2RwtldPjrQTuIYSBDdvobUVdb42541xkxnVVINYluhQ7cuwai6kTE6zY6tjVjVFKzkLd6Y+aUNtSSrYkiMnrtyuLsJaq+TmAC7qmXKy6CqA2qwyRuPPdI0RXGeyPIP35TB3MF2YOgVgIkIO9HnDVO6mHPADzgScYlpBPbbzs7CG44yX2+RgnA+8V8T9PEu7YNNyXGgK6wvNkmQj7zovyL3JFbC3XaG3xllg9xd2YpC+q1L7mXo++RqlapPNjJubIF7mhVUx28s8aMQOloYVRlNzi24EG1duSj23rwvbXKQn6Wzy9K5l6qk44YJERLuZ3NGo7+95auPTmwU6709TInWm/aJx1XWtcgR1m8YlHC2IOANtSp8dbDga7dEQmJvF96W4JPlTfDsuONhwriYXypE3WXICWA44DXrFiNMFZ5ybrkv2kkJygkoXuWovjsl5sgtncuPAfeMhoXCb78yCdYaCVEDXo4U1iMKE2FODcRUl/WIcM3qVbpPNaYb1vu+bM7rYEHOFyVI1P3VXejKjORCtz5OTClY+s2OqWpy47Sbq+71wVHS/6PGAmmKEepQvfNflJ2OvBbJ8Ru1zgRE79ETSl7lxpW9z4rxeWIG8ZxZSs1jvM66czzYRQcB9TRLA/QLqbZrmzPDCtWIbmZM8m6ivBgH2dOsddleuX5bEud3mHkXwzEnYNosQDvhMQK+SYb2dbC+bMLpFN/mWTOIm1/zbxui76YoITqvNIj8ntTGfbMiCFi5bUMW2VYQX6Ngq2cpTNuo23QFlXRDAATuZLjyBB9uIpAeWujF6U8zASkJvAtzlVmsabpMNYyZ1wXImVBZwM5snatfYmKHGRPuETTdxS3a+sZOHUpLxDdteT4Yb0xPFKONyPl07wwrbe8MEN+w14cyC3srImMGDgmRE4GTLZl/u+9hLbwKDSecVK86bst2c1uaN6Air8xyZqWyb21VmdOMykjaJDk4F52jAznONIMlAzxtiAfKdc71ME/e435IVj1PFYVAtwlODituHCWW0NNa7VIXL2eDF4Y3L/foUwR1EZS6vS7jdASq26FRrfr0Au5Xx7UrlzfNkrcCtsMzHPMRahdhKl/biM6V9ZHPcojfyTOXUqplfjjLH9IN3amdz13Ewm0lm7YWaND1GzwB/VW3Xmp9NhRZM/jo7hzK9ayrS7uSJ5RJeg/cHVFHAKXP312t3mpLro9XtJjOmFSCgN74WL3ZAEo8hf2VNq7KzsE6nsrW+HmQ01hLFJhaYs4A7IzKccyi66EQzmtungSQpnI25o5z4FI7bwQZsxZbyHbqeRjZl6yetwU47XbgGebqIUIlRQm5CYCIrSYR92ybMZn/RLl4FsFbvq+oUMKLdnNtW9lyHjsRDFnDzTEkmQbcg5c2EPGBzfTWf5d5w6xYs1kXKGivYepgMx/hyEjlg8CUNofxqcLvuWm2DjNCv5SJw+jk9KNL2RtUbm3EOZ3Y6BACNF/1U01hAe2opTfZVim5MijhaDN0uDs6pDqxTvV1ubv1Ak4NaHtOj7/jQbCE8KBPzYjIuRXh6R91a+bTwiy0KO2jDqMdsWaa1vsg9mguJmXY8mZamUeV0ba86ErReQXFy43vXIwknS0xWQmXr1xzccBaLxeIfT89P9+eoT68YSpDE89N4Qv9+zv4vn8OGQ1y+vbMhaBJ7fvp/d1j4OLj7ePJ2P/MGbvB6l/76L2r4y/NT5cdQm8exbZ224fvh4H87CP3yT09mR9L+8fR3fDR4az6eSzRueD81jvOgrZuqf6uLtL2fGUPvtvX4dx/1+KdBPvx8upuTleMh/UMa/OIGWZzfHyu8NcXb4xAdPI1/mDE+8gJB/O1n+H6+/vwU9DBOsV+/ETT1BqpyNPP9CdB4Zjo+Anr6/b8AcmL6o74mAAA= -->
