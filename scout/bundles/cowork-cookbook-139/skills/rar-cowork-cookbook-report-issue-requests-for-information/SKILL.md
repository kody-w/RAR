---
name: "rar-cowork-cookbook-report-issue-requests-for-information"
description: "Builds a structured summary report of issue requests for information activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_issue_requests_for_information", "rar_sha256": "0c27848498550aad395aa68fe53103c48a8b87b4c925f7641189692e07c9537b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_issue_requests_for_information_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-issue-requests-for-information:25e5f1f168a36af468dfd7d6c2a9142a547ea058747cbb0f2b2967aeb00588b4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_issue_requests_for_information`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_issue_requests_for_information_agent.py` is
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

Issue requests for information Summary Report — Builds a structured summary report of issue requests for information activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-issue-requests-for-information
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_issue_requests_for_information_agent.py` and embedded as the fenced Python below (sha256 0c27848498550aad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_issue_requests_for_information_agent.py` first:

```bash
python3 report_issue_requests_for_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_issue_requests_for_information_agent.py   # or on stdin
python3 report_issue_requests_for_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for information Summary Report — Builds a structured summary report of issue requests for information activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-issue-requests-for-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_issue_requests_for_information',
    "version": '2.0.0',
    "display_name": 'Issue requests for information Summary Report',
    "description": 'Builds a structured summary report of issue requests for information activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-issue-requests-for-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-issue-requests-for-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34399004cb5965ac',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-information'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-issue-requests-for-information', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportIssueRequestsForInformation(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIssueRequestsForInformation'
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
    print(ReportIssueRequestsForInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZOjxpruX2FqPrQ9VJfYEXXCEVcLYhUghFa3o5p9X8QmwOP/Pomkqu6esc8c37hx1dFaIPPNd33eJ5P6/cls6iAvn16ftq6ZQZyZJGHglpCZOdAiv+ZlDD7y2AL/ITvP6jK0mjovq6fnJ8et7DIs6jDPwPR5EyZOBZlQVZeNXTel60BVk6Zm2UOlW+RlDeUeFFZV44Lfl8at6gry8hIKM/CemqMYyLTrsA3rHrqGdQDVeW0m1TNUl27mgM9RJ6t0zdjJr1n1AlRwOzMtErd6ev31t+enEHx/ev39yU7MClx60m/LCuOS+mPFVV4K39YDEhIz88HQogdeGH8XbjneBpcc14Mev36q3MR7hv7jP+KrWfrVz69fMujx+vI0/tObDKoDF2hsVjUw3DYL0woTYMkLNEuuZl8Bm4FPsoeDwsx/uc/8JikvoF/Gez/dF3nx3fqnL085UOGm65ennyHgrS9PZTN+fxmlFD/9/JLkV7f86edvcqrGily7HoUBrV/eHr8fYsHAb0ND77bqL0DqPZiW++XpO+PG113v0U4w8+klysPsp7vgosxbNzMz2/3p578SaweuHSdhVf9Lcn+9Cw5c0wE2PRT/+fnm5N8g+GHQh8y/XrYAYf07loDh78s9Qw9H/ZXsm///m+gkzNzqw+N/Ku7PJsC/QL/+pW3/bMIz5H15WrpJ2ILssBL3Ffr9bauxi18/Od8ufvrtDyD6fxWzzZvSvkl4S80s9ECZvL39+qm6Xf7026+fmgLkmmumb02Z/JnMP/PrbZ0fPPgY9dOPc8H6uyzOQD1DH5kO/Z4X/1b+8QLtzSR0vl2vXqHv62V8wdBoxPuidxd8VzMV0PU7P/789AcAiewOUONtUOX//u/QOrTLvMq9GtraeVNDIMB1mLqj8kYQVpDxKOqvW0mQ5ZfU+Qpg7FbuACLMJqkhrjTDBAL1MEZ8tAAg3df/Y9/g87P9gM/JHQXfbhD49g6BbwBf3r6DwK8vkBGAtfMy9MPMTCB9pmmQ6btZPa56yw8Aq5/bcWGgVHgHHn0hjKBTNYn7D+jrv7TS203oS9GP5nzJQHxMEDQHqt0UzDbLMOkhc8Qrq6/dzwBpAaaUeZJYph1D41tTvIw+OgRu9vCcDTqI27l2U7tQkttAey8E6PwMgl/lSQvwcfRnFYdJAjlhCZyVg+4wwjrw+eso7OvXr5ZZBV+yOyDj0L3FVBMw4ENh6PPnonS9JPSD+kvm2kEOffr9j0/Qf0L/bNZN+LiGBrrDzWkgqRNI3KoKBCq0ScGwChrTA8DPLYK//3GPxqhdBnoiqKvQC93bZCDtWzqMFtxD9B4fYPOools+VvrRb9A1AH6Bwhp4C9R69fwlG0XkYGh5DSv33Yn3yXfXvwf8vs4Yk+rhQxAnr8zT29hbJo7BtPPSeYEED/rw1KMLjxEN8qoGyVuAtupmdg9mmvW3EGZ5DVUgRSqvf4aaCpg6Sv5qAdGjc1IAUmb9FVovNNDv8gS8jQ66LQ9m51k4Bv6RsffLQEj5CeTY/F3EC6S4wJtQYZZmEZRm5d7GeeY9I0Cfe58PhJtQ5l6hsbm7Y4xuyXvLPOGfk4ntg33caQD0pcEQlID+//OUUdUZx+ksNzPYJcQqhn6659VIqEYz7xxslDcudCuSbwziHWzeYfhLloQgFmX/j/tI75ZK9zHf2aTP9Jv8sajLuwE1SIgxwmU5JrH5JXvHe6DymNzVaBqo23hEgfxjwfHuu6YBKM7x97feD91zbTQaZDFUNFYS2pDnus4t4eugHMvp4XyQHe7oXpD/dvCDVRCQDiIA5ENAiRD4HPju5joFlAXgS/cc/xgejowKaOE0NtAW1I37Ah3GNAapWEGWC2jROAZ44dNNFJS6wMdAxQ8PV4FZ3JUZSe5DQfMRi+/9/7gFEnJsK2C1j2oDMk3HrIEnryAEoJi6e1w/tHxECqiajpl/m/RjsB+WQt+3pX+MFQc0/Ib6gJWPHf071wCYLtPqlmqg18YVqOnUfaQPyINb83659997g//Q5fV/8Pqf/h71v3XU3Y9xe4WCui6q18nk3vXem96Lnaeg8dlh4VaPBvj5Vluf32vrM9D583e19YPwu69eob+n4A8iHnn9CqEvyAsy3pJD2x0T9/EC/lh8np8+E+PdL5nufgs0WD4ftRr93wPM/egr70NAc/FL1x8H3/tMNbanK+iIN3i79YmPZHgUCkDPzB+bYpV/V8CjTWNo75H7gGFwKxsB3hlJne+Oe55kVL9yn16zJkmenzIzdf/Fvc6ItiBlgUPGXRIoHsCT6tC9/TIbJxy9Mn7/cWOn3r6YyVhf+dgzAXqGH3B6s8ApgXpjQfqgm7nlMwS09gEwjkZdx6IciYEFjATqpa4zWlH3xaj2fS808rIP0vY/NbjVNQAkJ38dyxu0VkCwn6EPrvwMve9ebnvCrAHbt19Hnj7aDIaCj4+xH/tWy3367U/UeND2v1bigTl3lDetsWeOJv6JTUDamOSgRzujPt8M/LZufl/sj5ue9X3j+fvTO6yM3++E4Z5cYMLfY3aj4e8d+e1+e9Rv5F83P9zY65sJkmDsvN/d8kca8XZP2KdXAEzu8xOYDPgPoOTDbb/9dFcJ2PKN944KmuXnamQSE1BvQBLo78VoRwzg8bsFxsuhcxs/fnn9C7L8v2DFK0a6pId6KDU1ccr0CGrqeA7tUDZmMiiBmSRBuyZCTmmCti0L8TALYyjadC0EXJxaBNCkAqmRmg9NJugYC2DDh8P/71j8010IaDEYSQEpiI3RU2JKMFOSREzTwRnSNKmp55I4iuA2MTWn1pS2CJvBSI+mCBSdMhSDuQhtMyROW6O8B4W8a/b2Ttffo3PHjTcAt2k46o2Zpj21aZRwGNqkbBdHLNx2UQx1aNxFSAb3plOXAPM/pj4iNAbwbvyYwIA9Au7Wjuv8/oj4mJQUAUbyRCXM7q/FhNmbE4y29ECGjwjcdRMiaOhDXnOxvJdjmyoDdYgX1jyzmrAS9tj8QMYAjRr12pj7OuPUYMnMMlrUPIUWpVBSEpGuZ0s5m21DuqLVoZq0bZJetqE0Tz0V3RUn5tDUR/XI4qswWEx6Oi52WGCF+b6vCxQW7cQ+H4h84nmB3ZoFmhlxFEhJk+0P6F5M+tO5RZB151G2Ffelt0XL2gr1xJF350QiG1LYr057zqOO+vac7qu0HJTrTg6IdZTAjBoxjOMNGDOvO7gta/gEd65c74RovypOhdTLhcnF7dYU68vljArnbZKpFyeDV3pgJ+ji2O+PPjpoMq8zZOipjkmZ0hlZZjrsVXhYLLADwyS7aghzoU5OJc/D1zg/uAQ+3+zRa0nBwanZpW0l5z19PCFYE5IJR4oZUpdlsgtCcrNO5hcLObG8u6I1u8CkZi+fDel8RGbxdh2dqdOmWJ1L9ExlW9LRiXlvzabnWZXn3KrEZtfUxdBrmwoBWZuVUijdro2E9NKpuetsD/pB5kmzZ8tTk4lhgSvDhp93k16Q2W3FYZg5Q8tVKyFpHdLzQynmGtMMZkZeqxUyjSWMnknFUmX7XXews9ky7dxz0+5hS97JZc5JUhe5Kna0Gnc1PaiYMzdV+nzVDsaCFrpmoDXRHhp+Hy1Rtmhwwd7TcVMW3SktdhKykSYpc0kX0ckgcnFi6YdzONeW8wHpyPTCtbDsb6pk0a6FA1efo9BDCpKjyjO+T8plww48U7lYDoBqv2+qhMg0eaGAiO7otSl0JHJxhpPISEKFRbuzwgqLfEodnO2ethGE1eH0mDiLUOVEeKnDbDSZ97JN7fVtRGyYyjZEaupquX29qkN95FonMmNWjBn6cCpPe7ncEqWCUanIS13FFfO407A4r+WzRmyvTLg7Luf5pp/FunzZdTthviiGglzETjAMF35z5lfEoQjWymZ34EuD1exZTq1nXL8UubhX2Iy1cRbPWYWVEyRsJEkMpWvVd1y5nppi3q8nxyrcX5voasKwvXNVhxA5VjsLCB9nfkgZUXzgNmzaiX5EROZgaWsYl44SZZwLW9vUzCHUBG4ZtFN6whE72+B5Nbue9vyxlCbxNeVRUp+fdqxGO664PmYVHTZc5fhzj+zk2f5UTig9gY/n3X5yMJdb29jMEWWbmtudiV/8xbTAkkPMHjWFPB12kYK2Szgq0N5Zty0S7uSTZ+QsJcGbOkLxrT8UxQHfM+XWXRz2q7LLz1x7octZjJ3ABccidXF/VFSyuODLbe3rzclYbGw4KvsM6yKtcNTcEPzC0Dqxxep8E5LMktj5fbTvcy8+bYVFUpkm7zgJK5ueuo6vecHm21oQWhtboIhTqCTGscgmouJ9N6sdl0yGMHQXy2q4wM6eVyQu2gyJpxckQzvnyHVay8RUJdXmklEOQV1Ihcs37eLkuQk3nLFzbZMlsRB0bDUcse0eQA4WOS7MX45+1uJtuKz4tuUD/ATLmyU3XAtx0DE8zpVlMz2LXUKVrUeKrIYGZ00MbSVV2rmx3PJ9xu/bdFOGpKqzrRbopzlwDKPH/BL3MgtTUv2KiudShtf+Dj5eFs1szXHbzYyaXVRAVyaz08VMKyY8q/v5THDjCqCAUvE5lshOkjKapgNIEehtGEqbdXQU0kV27HhuSoLkmCNht1CFsO/28+QQaQt/qqodaW9YnzlNp+RVscNc8YjzuhkINGnO6ZqiJpFVkZqBdm629HIistRmMqiFKKnbmjpdLx0iur0kLyO0ISt3ogqG5tluhw3zOevJyJRyPM87xr3rFbTQtG3bLYpwtblepLzb1667r7vtbJGcWEc6Y9HAtmG7WAyoJ9GG6nuCcTR15QzoUYzPRGd+ERJqeeHEeL/3YlTYIDThl/HJNItyl2szQYqu4UqzcgNZeId0nSsXY0kUc2Z/jo2T1uDr3AHAiu1sLeQPetJ1O8XhFti67wjYrmpbmEcOrGOkitm73Q5JjJVgGlaFiD5zoEh1AB1rhyW7+iwfkvxA43gwswTbWLgNI5LGxZ1ylHVN0FhpzFAQ3OtATFUPv5wuDH4uZL4mFdJYh0wmrXl4cSm4QFzt7QaJoq5DO6/fuKy5Ekt0MjjT9LSpyo2OWFKA5PbsImKa0kqus2OnrGfPTrPd/qjDNQWjl60u8EYYuVJaX5BTkVek4Z4jrfTjS+TPCMPGLNSNtM18Lfu+moklYD6uywkL/ZgfpdBOE2m2CXoFnlXsBl7uTvkQ2w21BQ7nU9nNF4s9iMW+laKLMa86q4mUw6qPZ5KcS0s9BfU+PZwvdl0s1Mtqp4s8l4iwSZvbLtsmZxY/WNvcRwKHsAd2YOTcmlqKeQpsN+4TVTuA7PDaeo2g9rWceQ3eZPk+dHB7eT0tFyJ+PeSWcV0L9JI18tVeW60mRp6KxHolSGW51nFzfh6Co9UXGy7Pkous5OvE3TnVKu5MfV3ujgvD7/RyB08XhTcj+NwWvHoTwI2YyB4WSMZSmyFwOsFt9gAXTJtW0fw6c7TzZr60tTSdwD2aOFRchrScrQp8Ws80b2BgDiNm3IrtEc4UMEajgpDQrxa/hwMShev2zMXNpI3ks5tthnM4TY8h4MZya8xmFXIVfH0tL48pVS02+9l6tV1UKKUMGoztppF84nthkM5mAFeHJanKCrVJUZVVio1rm3tNRrKltFfPFL+lCbw3j+nlupS252kp8oFKbfeSuT2cLDqLC1XcNqixSdStLVyUYLs++sLK7B3e2O+MXejadOlGu2Wkszay6eD0YG9qa7ebDFs+EZdNmOibGp9Li8aaMcJstUMsfskVQiLHKREPmasLgPhddttCli4A0w9HQzph8goLsW65UWUam8f2cD5Ey/zkG92KpuCFjLJiymsE6VtLDjnaq21dbOsdMuM2xKGzXYYz9DTa8AE/l686fjb4OA781ZEvdwmyAAxn0rvcYJ4RHJPzg6GafIvJgh1gy3NB8isR2yqzvcX5MbJgVkWdnpc24kxL+sochiM8W7MVfFT5OReK9bWcgya7yh2W6iNrvTpclM1wnBIbve72qoXNTi11ukiNsVO9fL1aJMxs3TIHZGYU6YrPp/D5ErLdKons3TVYOLsNjQ3hsJzpJSu0S9JG7MFZBp6En938EMCn6HheWhMJWZ+iuvW7I+yD/i9czCWawWksnmaHvJEAsOchfZjQe9nnLJZISaWwroF62Kx2Z3q+pXN9Y9K6lNrtlhXRdNDrCU7ovEjNMpAmq5YVc8LtWXE528DEhDIFz2fqYnLtOOE6ZUp6jkwxeb6fLgBbbqYIllAOL5wFvdkP9RmXB4c38+FkuIJqNGmOOGzQ7KT+0h4HxN/j+kXn4nRTrdNe2e80VihEvEK5EzlPh6A3nAWHIhlNSpHdFixRL0t4jtFo6mvrq+bhW5HeFIV4qfzAux635yrD1XabN6f2yulIqPj8cj/tQCXwRtfQm93VCVWF8jd94bd1SaTdAlaiWGPUNKkOtjXNttfLzg16VtdXSrdYEhPTblhZMPQKYwK3O0Uklyat5ra7EqNrriSN1uX93BKxGj0iadbk+7bUmWzZCpeERvED6HZRXTI9pbl5TQsDig5cJW0XBkbnK3PtFlS9QNOU5XXEpdfw3N1wZSIjHHbVVg2mZORwleUiHKgL4LQYK0+1AAE4hK8Djuaj3p9Muak8Yd3QPyKHkigo5sCtTjmz4JD5ZCci/OxIaZ1WMUc/PIJO7enyjqPkhq4mIszSAloEU7tLmoKQlEElr9qc4PtJy9PWxJ8H00QmfAOEfbIyeq/z0fUitjBqY7Sh6s9nE0B5SjNh+R3YQQb5QlHixLmaOo1OCAVdDop60XGsOaNXgDTKZb7qyAj2VywAAzQ05WWqdWc+6BrZUYYWl3oCk8rdype0ocw1p1vUi/3SjYIjIvcRz60RyT3zWzEhGcVbANaUZqLNrMWJq3QbGkbbHQ42y8qpOmGmh4f83HVqZi+tOl7j9GK5indp4+R+65xxbOL7drFCkMw7Lo0aPmpgBxAd7XI7kdMSJSdg69arB9FBJH4661n2iBFqhiMH3nMyEu6QKys7tYth60qIlEqa0mu09uY9ozj5pCCjTbNoWT5TeTplsmwqF4yfEv5ist62Wawb01NKZKyzwNUVSy90iugc1pjZYF85MWpO2FScrfaMhleWHx2CMjYbwb+kRuFz86bfkAtpOafn1lY0horv4owozxzesRqPbY6qtt3XfIkEuwAwRg8uvFaOq+kkVDVzwq5KTdG02CpqMaIOAuMHg7iJ+qNkayKAHQTjzWV3PLRkvTE8vqjI03UyCJRxyUQS9/Q2bitYJbfGeu9wTW87ibweiD5FMHJTh9PGCcKtoa9cDLlGLQuf6NwqT0qVOmhbBgl62RDBYCuYxa79a+eTdNfk9FTDCgObBNqyPLdqlm6JlUjRK2V2pZO8pnofQSZYT4PdVGRJKbOu6NjG6FN4RZeZlEcBxQslAgixduDd2WqOGJcJTNnHlqy2wmxd8qCkopBQDr3KB8QcE6u0uazxfMIqIYbDrDp15jY2nGF8lWITm5wiIV22OUk6K3zQkgEhQkBkm2tFHyoX2VWqV2ZzBbGsY58FDLMo2QQ5H02lm8KbNiTJ7kIbNQOHkwlfLHHRwzVn4Ew4LZfsZl52icHOUGKbo5bLILu2Dq8KVWCsqSbmhIJLwWilyWqyYZTZepEIGxSfwqrq+HnQLAtedeoEP+GhjU9DdIGdxJIB+50cM6+syUpHh9wIztIdiNmkhIM5v2qs3B+cIUREVFHaAy6c90rbMImMDWirluaZCrhDUPPMXthMmY1Aq3xP7NHOYhkisQZmmC26a7ABjHGLXOHBji6AMrqRWlAOd24NWbxqreSk2rY9C+55gdLDRABb7YTHsWsjLL0ZTmP7uRysefLot9gOoQ6qYTBe4My9tMgZK1b3uDXfgfYNmKDlXxYr3Azne7xoe3lu8lQx7dA6yxoxwtfU2VxeZywWU1rRJeTmdFkWVb6dZRaJz/CJLhwPurheFRPtsPJxxyPnA2fsLvhhwPH+uCPgJai3nAAkxJ/NZr/88vT8dHsc+/SKIgRGPT+NB/qPY/m/fV7rD2Hx9hCHUyT2/PT/7hDxfqD3/uDudkbums7rbfXXv6npb89PpR0Cre7HvFXS+I/Dw/92YPr5XzrJHUX094fL45PGrn5/vFGb/u20OcycpqrL/q3Kk+Yxw2qq8c9MqvEvkWzw+XQzLy3GQ/77qt9ON+v8rTBHB4fZ+OTMdUKzdh8//fJdB6cHcQvt6g24/s0ti9HMxwOk8Ux1fIL09Md/Ae5i43o0JwAA -->
