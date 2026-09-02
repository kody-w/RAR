---
name: "rar-cowork-cookbook-dashboard-conduct-exit-interviews"
description: "Produces a self-contained interactive HTML dashboard for conduct exit interviews - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_conduct_exit_interviews", "rar_sha256": "72280e6a8f6a9283acaef79b33def4e8033abf73e0fd89c7e298f687a608e377", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_conduct_exit_interviews_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-conduct-exit-interviews:cd484b15d46da971f1bbb79752bfde178341c84f95384e76a61453358015b73b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_conduct_exit_interviews`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_conduct_exit_interviews_agent.py` is
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

Conduct exit interviews Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for conduct exit interviews - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-conduct-exit-interviews
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_conduct_exit_interviews_agent.py` and embedded as the fenced Python below (sha256 72280e6a8f6a9283…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_conduct_exit_interviews_agent.py` first:

```bash
python3 dashboard_conduct_exit_interviews_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_conduct_exit_interviews_agent.py   # or on stdin
python3 dashboard_conduct_exit_interviews_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct exit interviews Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for conduct exit interviews - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-conduct-exit-interviews
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_conduct_exit_interviews',
    "version": '2.0.0',
    "display_name": 'Conduct exit interviews Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for conduct exit interviews - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-conduct-exit-interviews',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-conduct-exit-interviews',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3c5d872df35cbaa0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/conduct-exit-interviews'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-conduct-exit-interviews', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardConductExitInterviews(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConductExitInterviews'
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
    print(DashboardConductExitInterviews().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjxrrmX2HqfrB9VV2ITUCdcMQIhAAJIYSENrejO4FkEfsmBB7/90mkqur28fE9xxHzYdTRVQgy3+V596R+ewJNHWTl0+vTFoIUk0EchwEsMZC6mJi1WRmhX1lko/+Yk6V1GdpNnZXV0/OTCyunDPM6zFK03Sgzt3FghQGsgrH3aVgMwhS6WJjWsAROHV4hpuxWGuaCKrAzULqYl5UDVbSxxuAtrB9rryFsK+wTluUwrdAtJEyH2WXWVrB8xtIMm1ETBgMO4lZhKYQuYmJ3WB1AbNgKyxckHbyBJI9h9fT6y6/PTyG6fnr97cmJQYVuPc3eRRAf3CXEXP3gjbbHIPXRurxD6KToew5LJGyCbrnQw96+/Tho+oz9939HLSj96qfXzyn29vn8NPwzm/QuVp2BqkZSOiAHdhiHdfeCTeMWdBVWwrop0ztsCNzUf3ns/EYpy7Gfh2c/Ppi8+LD+8fMTwqYEA/Sfn37CEIqfn8pmuH4ZqOQ//vQSZwiIH3/6Rqdq7AtEOP98t8/Ll7fvb2TRwm9LQ+/O9WdE9WFkG35++k654fOQe9AT7Xx6uWRh+uODcF5mV5iC1IE//vRXZJ0AOlEcVvV/RPeXB+EAAhfp9Cb4T893kH/FRm8KfdD8a7Y5Muvf0QQtf2f3jL0B9Ve07/j/E+kYBUD1gfi/JPevNox+xn75S93+pw3PmPf5aQZjFGolsGP4iv32ZWtI4i8/uN9u/vDr74j0vyWzzZrSuVP4koA09GBVf/nyyw/V/fYPv/7yQ5MjX4Mg+dKU8b+i+a9wvfP5A4Jvq378417E30qjNGtT7MPTsd+y/H+Vv79gexCH7rf71Sv2fbwMnxE2KPHO9AHBdzFTIVm/w/Gnp99RhkiRNigTDI9RlP/Xf2Gr0CmzKvNqbOtkTY0hA9dhAgfhd0FYYbu3oP66Xaqa9pK4XzF0dwh3lCJAE9eYXIIwxlA8DBYfNMg87Ov/du5pFSXIR1rFP9Lhl7dU+GVIhV++pcKvL9guQHyzMvTDFMSYOTUMDPgwrQeOd9+omuTTdWB6T7h3KUxRHRJO1cTwH9jXf8vly53gS94NanxOkV0e6buGSZ6VoAzjDgNDnrK7Gn5C6RXlkjKLYxs4ETb8aPKXAZtDANM3xBxUUeANOk0NsThzkOReiFLyMzJ6lcWoHNQDjlUUxjHmhiUCKSu7e+lBWL8OxL5+/WojwT+nj0RMYY+SU+FowYfA2KdPeQm9OPSD+nMKnSDDfvjt9x+w/4P9T7vuxAceBioJd8CQM8fYYrvWMRSZTYKWDdUH2Ri4d8v99vvDEoN0KaqRKJ5CL4T3zYjaNzcYNHiY5902SOdBRFi+cfojblgbIFyw8F4Eq7p6/pwOJDK0tGzDCr6D+Nj8gP7d2A8+g02qNwyRnbwyS+5r7x44GNPJSvcFUz3sAymkLrJrPVg0yKoaOS0qty5MnaGSgvqbCdOsxioUN5XXPWNNhVQdKH+1EekBnAQlJ1B/xVaigepcFqMfA0B39mh3loaD4d+89XEbESl/QD4mvJN4wXSI0MRyUII8KEEF7+s88PAIVN/e9yPiANX8FhsqOhxsdI/ou+eJf9FJqP/cgHxUf+xzQ44JGvv/qnkZVJnKsinJ0500wyR9Z54efjeINcDw6NlQF3GX4R5E3zqL9yT0np4/p3GIbFV2/3is9O6u9ljzSHlNiWQwpyb2rnZ5pxvWyGEGDyjLwcnB5/S9DjwjnJC5qiGlobiOhiyRfTAcnr5LGiC0hu/fegLs4YtDjCAvx/LGjkMH8xAQ94Cog3IItze7IO+BQ+ih+HCCP2iFIerIMxB9DAkRIjdGteIOnY7CBvVRjxj4WB4OnVb+MLOLobiCL9hhcHPkqhVmQ9QuDWsQCj/cSWEJRBgjET8QrgKQP4QZmuI3AcFgiywBNfzeAm8PkcsOBQfx+4hHRBW4oEZYtsgIKNxuD8t+yPlmKyRsMsTGfdMfzf2mK/Z9wfrHEJNIxm81AfXxQ63/DhyUyMukuucmVIWjCkV9At8cCHnCvay/PCrzo/R/yPL6p0ngx783LNxrrfVHy71iQV3n1SuOP+rhezl8cbIERz4S5rD6Vho/vQXapyHQPn0LtD8QfuD0iv094f5A4s2rXzHiZfwyHh5poQMHt337ICzET8LpEz08/Zya8JuR3zxhSHcoBaOYfq8670tQ6fFL6A+LH1WoGopXi+rlPfndq8iHI7yFCcqtqT+UzCr7LnwHnQazPqz2kaTRo3RI/+7Q6vlwGIPiQfwKPr2mTRw/P6Uggf/J+DMkYuSrCI1hakJxg1qnOoT3bx9t1PDlj0PgPaJQKnCz1yGwUNFDLe8z9tG9PmPv88R9REsbNFD9MnTOA0u0FP36WPsxYdrwCU1wdZcPkj+GpKFhe2uk/yzEEE9I4nuCHcrFW4AOHP9EBF34Piz/TGR9vwDxW5aoajCUSpTk32K7QnK6qLN6xpDtUMyhMELZsUEb/swG8Slh0aDi7A7qfsPvm1rZQ5ff7zDUj0nzt6f3bDFcPzqFh98MU+h/3M4NmL6X4S8DZTDsvzddd4jvreoXpF44lNvvHvlD7/Dl4YdPryjXwOenAcgyRP13f5+snx7iID2+NbmIAsoan6qhfcBRGCFKqKjngw4RynjfMRhuh+59/XDx+ted8V+F/6vj0hxtE4xLT1zAs4RH2LbN8ixD2p4LCZajaMLhaI9nKI6G7ARMCJqhKIYbE4zNUjaSYrBkAt6kwInBBkj+D6D/frv+9CCA6gXJTBAFliS5MZwAzpsAnuQo4ADosbxNUQh8GnJjigK2x1Jw7Lkc77CQ5NFSjgWTMQcplh3ovfWLD6m+vPfm71Z5pAEkT5KEg8wkAA7nsATt8oiKA6mxTTmQIAl34MLwlMdxkEb7P7a+WWYw3EPxwWlRq4ialuvA57c3Sw+OOKHRSoWu1OnjI+L8HrAH1jYDmy8n8HQ+4qodWsXOhqxIHvhiXdHFSUpmZ62aZ1ZZSXq3kAjdMS/rscoeVrqoTASD3Hq2M9pO820qb7XAPgkRHTqk3VBa5DEMze4Fc571+p6JiCRR/HJ2XseSdyDmMwiOrqCkQcxork+VDM93N6a/WvS+pAyS7EZ4FUCivSwD+eCC+arO8wht38bdYrLGVzJ31OKjXqVepZOHQiqOssrZmmbVpQv0uXGQ41M2wker5niRvdPO1reh0Nn5vE6ITDOtWFEyXsnHE+faMyN4vTB4v5p4V4plNtwNnpjQkop9cJ3Ny73V9LVZnGp3U9G3vXG2FIMTrguAMg+oJCobLxMdjKgL30v59iYlqrqwNDLPnJk2Zpwq1RLyVBwW5Okg0FpxOC88M8jdbmlvz61kH7MaaQVuG9LcH2R+35gTXeh7qzJt/ljb2WGx5fr2UJjLfbiO8UjtmWYcCbHd+qe8n0x8qdvQHrMt5lJbkw4Bzk3jcr2glqUTJWNJAN7M222SnbF36CMbhx2R100V0WA7Lhi+c0rLqk9Xm0+C+qBTwnrp58SG0ltck/a32UmsK0IpDwqRxO5aIvbewbVocs/XjTDnC95Qt5VAwwXNLqygDNcrRqdu4+mkOSLkS0NPC4YZzxY7p70eDa1Mr7xoK6DZIDvQvLy/wJEa1jZ7c+a7kXLqQ3UV2RfzLF8qa8/kdXyyabiap7Grp5v4dLHnRz5Zl92ic5fHq7WaHBrreovNCSdpfLyzxXlgdPVtrVrOsaqsc5ESq8Nu5PDu0WFPZF5rPbnterFf41rFWucMqNHiuKl6UOeXSZzn5nbcTeJRunRDaFc0sSu3+NQ0ZOjdWjwUbhdmnwBRrXe4b1LrPMbxlTHuhci5mtAFLHVb6DW/pZuiivOjWfXTmAb1XtufxmtbguNUJsytcJEXzXZkwXpEjSdnGaWhbAtbccRry+MlmkG3Gs2iKt7KYNPthfiabpbmRNi6sq8RZpTtuJ2wINuEUVw1UM9kJe0vZmo5JOoAyn0CFWnsbPWYai+rWTnqLnEiX/od3Bo3Krqo8jhNL7Z8pNeEugkm24Vj9Md1UdB6FbHG7Nbot6VUsaKXe/hyslmvy5xeGNZIC7UZrPSjXFTXGyeqQinfdvamkC9lB1eaDIB+2yzHu6mQ5psKb5396jzKTUpIjEsNbvNTbG5FWjf41Ra6ot6Fp+nqOuE2OcGQ1+ygnJennTKzTHe3h3Bhdf18lMOoUSYFke+P7M6ZLkc3KQhmNONQl02cZptFfbzsNlPohsYS9OU5wzdxz3A+EQv7iZIS82oXa80ZnLfMRd3hpNSVy6syU9juDPeLhafOvdUu8s2FRThEraO5djeplTqJNm3OnMyrusnYOl7Jk47sq9ViHB5ZFfk46FBo78zgxNCHHHaTw8Lbl2fEodMqwhE183xBKWUyPq+ai0QZjMyseHNdZKiKURZT3VaMQJ5I15J2LK0c8WLhp+PNsT+Vh6vp9rMJM8InJ++yjhTGc3zGW8FcDxYCkMdufVqMlJufyjs13/VReGv3skPHDE3N7LVYyJIRbSc11RHcRiHdlF1XnjwDt+Lc5ZRk6xV9PVZgv8oOvT1Grny2ZVflmWkpbESlDbY2M43w9lwJAuPfjrMLKhVKrgjSRT35hEwxdtRM1G4rWCeRqZeLZiGdgDUz9/YpZdbLqg/abmOFOt2x7WZdnKUZCec8d+LZydjPpaQm+q0PRgcTUICk+f35UARjM4Gud6xv7pXliF2yEDR9e2iWFaqpaXzYnPAY7EG5SmlLsMZgnp6OLFe1YEp5ltO0lTEX5955jicefi1bqmduZ/fcpZE61zhU85VDmd5KW/Kn6UFQtomecfTmeAgEtWv223M0FpzF9aqSpWAdzVkrHjegmkCfZcKzvjo5SS4mV0/aWz6+dXXAL8aiB6B09dmzCLe7Q5hcbsTGEvVtakZjvhD5STQJWmXh9xbXxNu+n4VbdkXle1wc1XKYV9HUYGij8HOvvlVLpoqOcJ+vWDs8J6RbT66SMNnggeyftnN8kRXijFLpfiSZ9a08+9VsXkV62V+PF+4mjDlyzXZu1dYyZU/kfOIrzSbTq/NhsddILza8nevzamjmPDjTKd3Oc7Vz2V63ldtKj3sP9AXLjLPNBnd2nRdPw2k36cYnF8iVLjDc9ECa+hn0hi7N4brV+NzUxvFKFLZSkZ/JYnpV+cVMBPic0i0C19vNVtiJxHhnLaRYmEUSuKj7uRsEaDwgW//ixvXV7mjhMLdiYzENd318iLvC9ato4ZwhYwmgWC5sLuCmVNLv/X3dnmWNXAladTk4axk/WksgyuSiWgLc9BZij5+jenUyRjDIV5vRsqu3o3Fpj6v1EQ0QaLqXI8Bp60uxF3fQuTjgshXGdu2C1thxDefUiX6ziotdASofbyNeppNxsqzW0N87h2lCRVJ7PBlLvtSF4BClulSTM3iK6CYOW2G5OfW7bKJenIVQ6ORuXqyNhk3HwcSW9OlqlXqsrZC9gAOzVCznMu9v8vRw8bmCLZXZdtcX20kBCvGQ2t3Y8LxUY8nUHs0vQu8a1cYFSszb9MUn5ZhZsGSj10Q42bvHZc2vbdI+hHS6KzxAUoeald0c3qYhTXhGE2ZTk5TUuShcx0wJNCJSadk9edrcOceFPLoBIyJO135F5s2tbGVr00znen7r4qNG3dowDVf1aTO+LC9F008th50wRjRf8hOZWMq1yy03ZdHShKbvqz6lp3krT1WqP+BxITi6oK/rESEHtp9MzFXprJNErfzblRB02z84qu+Q8/PS1KJKFZZHXhAu1q2xSBeOooqaat2C17YpnszkdRrRGXWc10Dkc8cS4EStmSBdzmlxy6491GVp1i2kY3XbbU+ab+1NyVzN3dNtvNY0sDxFteZYqrYlSTVCneqUSIP1/LgkC9nRw1wHFr6YVJa4Ohz6irHClM3JqNw68bFr40Sq8Xy5wKtRukmL5W0OZorq1Yrhd9z1UG2Oq3NeHcjbMrkGuy5J0ATgCvqoNNSZQBlZQe52tbtTLbvaXRlLX49ZkvC6tuaWU/tWbrrdytyqZG6GzkrZNaLQRqG+YvNmKTRJqMfLLXnWwQlMG1DREiusULzrfBvZTGRevImU0oSxI11H2gZZVqlVM9e1DRlPtYVVryVuuj+nwmYKUnV08MnKb+hDYWtgXAtivEmApU92lmkxexvNUHsKH+mBtL4dLqtd1fCtJGiKqM40syWrbncktSo5OEtO6lVXbs7J+LaTvHUPezzcn6a7wghSe6ftKMXt4+MqEJQ+b4tcUqVpzi/jUx6bqesr1i1RFjVLKK28wtVTzzBKts785fTKswiHdemwu0Mg+Zu+zfnymIeoHV1Qy4YQjzwlHdjsiJKadNDD2GFob6YEuEaE2XxPkqJd9u5sN+XzdLzso4s1Rbmd2nX1/HzM/HZzFkh52p6UPFO5ozobidl1vfcPS9le3DKn2Oe10ZxvekmvC1GIZ8T4vFlS5AYNIaCfLs9RMG1y0wvCCTeb5YQsCtHGSq+qLpFpBSW+yLYbLmu1qkj2bDgyrp7DCLjIACr1rPle91SwysR44YzPEzQK0HsnWxpjeWosY6bSuOmaaHSIQ+pIXRV+khEKOykXdV/t10Tn1UBNG249W7Oz0dylYrYRwkbR0j5BVW/mkEcZ3qz11IGN22UBmUZRQvlONlkvyqqnxTLaUjLlUI5bTDm3IsymP6L2Q01O4eLo0GUgunMb12uRP23mmQaCJZcnHKVslLDg1HZ6cGeNShFGeqwuXsybe39HLK6sUyj6JWMzUccd4mQnI/zgV0bqxjZ0nflZNXKT8267fMuSeqUTzdo8j9Y47mWaF4lXsegtvHbwm8Rdc5Y6Gg4cNZGc5krD7NwdISahcm78jEsNs5jMZiXZ76QyPXQpIxKMMJ8SzKg/NbIzna/XlCaexi3uV8HFSThLcbyoH5UZlOH5qBV7rh8fp2RhN+n2knGo67MFIDLsLIOMc7yuoRMAYbuTqE2VVRk7usx0Hmhpy/jrcn48zPDRbhTSNqstxa5rNJLejGb2+ejygXdzUaNXXYAEdsZGorwomLCVrkz7HMwkL8maJD13LRF5bFwY/NlNVHxC4NRsHh7r+Z4XpGpKzKNZf+W1SwbJitVZJllU8vUIWrgy9/2UrPLk3NQlOzrOr7HiXtdTUSNxa01P7OZYwZqrU1IE4XTG98XIM/2UkrXcMU+sQ0dHa3s9aWM1ABe3u+GSnUvizG9vXLFze5ld7NiYcYrFmQKbWdZRx7WmBvQibugpyafptZ2FC+98jDVDbuhRO2NoWaxPNyjpeJtFzMgWaA4afntJDMqH+XQZUjp79Kb1pWsn6hRVzPnML0J+xSmhv5loJxCccK9azEFpR4sZPTp7JrBsaobbRCPXHmQn7Hlak6jcsmd2bDn9+nIDqhevKTu6UJ1FOmpJjCG950PNsGeubZYR37guXI2crSKt7QzujBnF33xWCYJyspoaix7MAuealcqVsBuuZApKacpKWKISFQcEcTnKbKY7JYo3BzUKbM03RJYdAiok9wEwtNQSrkI7kuBG9CfiHjUGCjRTJzV9c2NUJ3xJRLC2luvL2LtuzyZvEdQGFQ4j18frmvaVQLGp2o8UimjI0W2BUyFbXls4cQmC3jqczCEnZTvOBQFryjebPVd7eG6IUccdYbqf2U0h2cb1Cm46cTFsVUd9mpfheDe62TdLZyhnUbtbflSfZrc5FcgJGsbQIJCa1GnH2ETmXJY5f5MveVJel8VIYFucbvXpWIpozSK4vWHw4zKUL1abU0rmXFfjEUqJrEWFFCWwHTsqNE5T4y3Rt/pE0cvbdLc5KduDKlL7WaqlSmaSZ/FqkdGq3tj49bxF9ggUuppvDFEKLu5lcjSsDrYBZygCdyD0YQzw6V7gRLE0RaiVmzlzFRJzbo0smdeAfx4zhbBaXcWgCogVjGfbNZFqrW04LSUfxtBotHI1w6/0fMEJsQM4iWcP6cgUbRTr6zmOmmD24vnxedQT51FbSxtl1ZRRLcaXfUAWkwwn0NiCj5bzXrum8MJOU4VmOKHzk1tbr9NaCM9yhJoo0b1mnWTc5gFjxlEapiTkV4pGpZfmRM+uqcOmRrhqapoX8NmU0wsQRtPp9Oefn56f7u90n16J8WRMPj8N5/5vp/d/6+zX78P8yxspiiW456f/dweTj0PC9zd796N8CNzXO/fXvyHlr89PpRMiiR7HxVXc+G+Hkf90+Prp354ID9u7x1vp4RXkrX5/81ED/35iHaJtVV12X6osbu7n1Qjpphr+LqX68vba4OmuVpLf30G8c0TXQVjCL3U2nL+iq6fhj0aGl2rQDUH9/tV/O9tHOztkr9CpvlAT5gss80HNt/dLwxnt8ILp6ff/C0H/gfOBJwAA -->
