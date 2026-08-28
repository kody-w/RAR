---
name: "rar-cat-agent-skills-sharepoint-list-insight-report-generator"
description: "Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_insight_report_generator", "rar_sha256": "1755e4d761977ef94e93304dc8d180edc0dc810f70e304a513ed4909b525f0d7", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Marco Rocca", "tags": ["sharepoint", "microsoft_365", "lists", "report", "html"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/sharepoint_list_insight_report_generator`. The original RAPP
agent is preserved byte-for-byte in `sharepoint_list_insight_report_generator_agent.py` and in the RCI capsule.

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

SharePoint List Insight Report Generator — Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-insight-report-generator
  Upstream author: Marco Rocca
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_list_insight_report_generator_agent.py` and embedded as the fenced Python below (sha256 1755e4d761977ef9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_list_insight_report_generator_agent.py` first:

```bash
python3 sharepoint_list_insight_report_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_list_insight_report_generator_agent.py   # or on stdin
python3 sharepoint_list_insight_report_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
SharePoint List Insight Report Generator — Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-insight-report-generator
  Upstream author: Marco Rocca
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/sharepoint_list_insight_report_generator',
    "version": '2.0.0',
    "display_name": 'SharePoint List Insight Report Generator',
    "description": 'Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items…',
    "author": 'Marco Rocca',
    "tags": ['sharepoint', 'microsoft_365', 'lists', 'report', 'html'],
    "category": 'integrations',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'sharepoint-list-insight-report-generator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#sharepoint-list-insight-report-generator',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '271bccfbe07e039e',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class SharepointListInsightReportGenerator(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SharepointListInsightReportGenerator'
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
    print(SharepointListInsightReportGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+16WZejSJbmX6G9HiKy5eFCIDavU+cMaEUSEgiEBOl5IliMfd9Rdv73NiS5R0R3Zk/VnHmYh8EfgsXs2l2/75opfn8y6spLi6fXJ8EorBQ5ppZlPD0/2aC0Cj+r/DSB39i6SmOj8i0jinrE9ksrbUBRIkZiI40R+bZRAfiEyJ5RADH1kwqJ/LJCWr/y/AR+sNIkAVYFbCRM0jYCtguQMq0LCzxDIUbUX+F8vyqRsipqq6oLcJMN5RrPiG+DpPIdHw4JQY+YdeknoITjk9J3vap8vo11QQKKhx522iZRatiGGQE4rIIfrMpvALJWhB1SgCwtqhdE8cDjHo6xohrajNh9YsS+hTh+BGdB0T/OtqB5w3IlnHITPaxbAug47/Z4e1nerEYyw/UTY/DfM2KDyvCh0XA1Ky2gWYUfRV8GJZHKK9La9ZA4tY0IydKszh722D4cPfgxCUukSpE0Awl0EYjLtxpDMRIGCXRGnMEVn15//e35yYf3T6+/P1mRUcJXT7dgZEMwdjAW/N1Zx5u9q7uvYNyfnyIjceHorId5kMDnDBROWsTwlQ0c5PH0uQSR84z8+7+HrVG45S+vbwnyuN6ehr9jPdgCXZAa5RBmy8gM04/8qn9B2Kg1+hIaD+OaDOGBQfYT9+U+87ukNEP+MXz7fF/kxQXV57cnaHdx8+Pb0y9IWsD1inq4fxmkZJ9/eYnSFhSff/kup6zNYHAdFAa1fvn6eH6IhQO/D/Wd26r/gFLvGW+Ct6cfjBuuu96DnXDm00sAPfr5LjgrYBkkRmKBz7/8lVjLA1Y4FMM/JffXu2APGDa06aH4L883J/+GjB4Gfcj862UzGNZ/xRI4/H25Z+ThqL+SffP/fxEdDSX54fE/FfdnE0b/QH79S9v+pwnPiPP2NAcRLMtiqLpX5PevsriY/frJ/v7y029/QNH/WzHyDYgGCV9jI/EdUFZfv/766Y5Pn3779ROsyaoARvy1LqI/k/lnfr2t85MHH6M+/zwXrn9KBlBMkI9MR35Ps38r/nhB1AFbv78vX5Ef62W4RshgxPuidxf8UDMl1PUHP/7y9AfEieQOssNnWOV/+xsi+FaRlqlTIbKV1hUCA1z5MRiUVzwfAm15q+0CDKDvD0h3Hwfzf4jwoHHqIN/+l2VUXwyIw9WXMoQIV47LDwj6OoT06wOxv95R96v7DkPf7mCcFv4AmhFyZEXxLbmJGhbPClCCooGwYvYV+AIB6ctwA7EZ+fbPLvH1Ju0l67/d0NW/w9Vxxg9QVdYReBnMPXsQZO/GWUaCgA5YNVwoSiHzDZwAIDhDZdIIskE1uOZm6AOr06K/yYbuex2Effv2zTRK7y25YyuO3Cm1HMMBH+ogX75A85xoUPoNcqSXIp9+/+MT8h/I/zTrJnxYQ4RY/wgO1HAjH/YILLY6hsNuBFlBJLkF5/c/Hk6GYqBLEBjKO6UOkweSAfa7x+U1+wUjSMQE0NPQy/HgSQjYkH1eEN5BPvR9sOcA6V4K6d4GkKMgWVs9lGpAcz48maQVUsKMLJ3+GalLcFv1m1kYNxVjWPVG9Q0RZiIkkDQa6K54EAqcnCZD4/GRD/f3UEjxqUS4dxEvyH5IT8i7hZF5hfFYwzHucYHE8T4dCjeQBLRvycCYYHDVrVbu7rklDGwA7iH9MsQcdi8xBAa7fF/7vdWwEeVGd8VbUj7qACbjjeWhKj3i1rAzguzw90dKlV5aR/bNf1DTQdIjCvYjKrcc/KGJGogbeTA3cqdu5IO7kaEPmEyR/9+c/b/XnA1xZFer42LFKos5stgrR+1uE3R2NeThve+G/RECi+yOJd97pnfEfSeetyTyYbEU/d/vI29Z+RjzERQbwubxJh+WBMyvQe6tYocKLIohQsZb8s5w0A7kBucwaSG8wfIf7Hhf8PmeFjdNPYhhw/P3bufdVdATsCqRrDajISoA2KZhhYPbBtR5pCcsXzAgUOv5lveTVQiUDqsEykfS5JZg0Om3EtinQ2q6iFOk8ffh/tBDQi3s2oLaeqAAL8gZAsdQPCVEK9gIDmOgFz7dRCExgD6GKn54GJJFdlcmLcJ3BY1HLH70/+PT90K/aTIoD2UaQ+a/Je2QvTbo7nH90PIRKahqPEDTbdLPwX5YivxIxH9/S24afnDeUM23vP3uGgQme3yv63vieWkMHunzXrEv947j3tJ86PKKzFgFYe/ofqNm5HP8Tvq3/uD0c0xeEa+qsvJ1PP4Y9uLCyqnNFz8d/zee/9t3Fv4yYMuXR/V/uVfwlw8W/mmpu1dekR92nj99f6TnKzJ5QV/Q4dPOt8CQf4/rFamTDwT9/MP9I3y38AD7GaL9QA1QmSFTSw/Yt8bsCL7H1/gJRM3+g3Xfh0DqdQvgDoPvLFwO5N3CfuEmG0bgLfnIgUd9QORJXHDDpB/q9tZ+DGh6j9E7O8JPSXUDcCjPBS/D1mwwtwRPr0kdRc9PEPzAP7+vG4gQJiv04bAphGUDe8LKB7cno7b9wZHD/c87/cPtxoiGykqHpmJgverdoTcjIEA2YChF1x+47xmBirsQVAe72qEch87JhHaWJexD7MGQqs8Gze/7vqEH/WhQ/7sGt4qGUGSnr0NhPyPDZuIZ+dgXDIh936kNkkFSw63qr8OeZLAZDoX/fIz9OMgwwdNvf6LGY4vy10o80OYO+oY5kPhg4p/YBKUVIK8hL9iDPt8N/L5uel/sj5ue1X2T/fvTO6A8ovRoqOFwWLlfyqFvGMP8hwvC53vmwW//5632QxAcDls8KGlCEQSY2hQ5YSgKOMwUMDiOTm2Ltic0CmwLhbcT1KFQAF8bxAQH9pRBGZPACAe1KSjvnshfhy7JH5SzIA2QOJxjOKSFGQaFTxycsgnacgANGGxi4CSK0uj3qSGs1IfFdwsHd350/beMvRv++5NJTuHI9bTk2fs1G48mxvhMBZ23HifoqNMdUooEH92hC0NdWhdLZvCoPcg9vcRWnXxIt1c+smRtGmypbIUvhc1s3c9FtHX4cGzhJR2JPWHzrsSKJ0GYyjauY01t4X3bzIVdoMlbEZBzqelgze2sc4FvzUKRk4NqLPdblcwvXKQb/n40bhaJpRoq8JvdfqPrlbffGPGeSaetKoTjRWBd5eNG2+KovDZOumAy+z4c6Zq/PoOc8k6+GRyYMxaHxUlWIytWI6EN7aTmRp0o91VpGPm04Dsfr9ki6zd7dUnGeSeFEyxNokzdW5jKUaiMnUjdPkwjPQgVh8jis6928SyWomXN94269mm6bJputlK164I4mcSVnG3KvuDwWL70GGr4k7OhHW3Nxp31iR8dSiaYFYfIykmFYxM88ghjskxVK7tGQtYcMnkpZafe36PYpko3+qYc9bzHKVFXe3lzXJqJ5QnLXZ7OckYM061BbTznPFnmqVSrLXrMDXw8om2Gs0SzJ5zkGmHgcr3SynXCOEkz3uWSQEXX2TlcnglU1iob45dLmt+opdyHQommmDNVU147EuqqP2NQmTK4AjLjp0qe+3qGb1Y8Te2vus94jrAvT0zQqlKy6jKu0XczFZiZXKXSzK35eZ9WQsc42ly65FNSq9dRcAhMyRxFU41bSjU9CdR9ym/YoG8iLyIkMgq3YF8IGZBnlh0WiRAxi8Iyq80UZfZrdyfqi/PIs6bT/DxPty7cn6XJolJDvTljm9T32faQR36/i47H8OKTUxRWatRvCS1HKXvBjtX1deGVy3NvcvzEo07aWfE2VRGFKAlwp1JCpkAF1JK30nXFxlsrn5/b4nTco4R4NWVg22w3QwWKuMo2SV0Cassl0jnASIuTe/Oir0TM0fXO25nYgg2KwqrcJcabjXoanWGpegK2qA8zMZDZKw2u5SlrO2JaFd1uoWq9LKCq0fRuko6ZNd6GHUyjbVuOxMDzM4NHV7muK/l04p+P/TUKzyroRoy+9RfLSGeDrb9ci2UsXrY8bO1qcjKHkTpLcRNKsGld1dOJh0U4ml5LWSFnEtla6cUw2nQiXkVlKRHGNphtVjtrdGpHGglSfZb1kAhOW0+W7fwgy8eZlTNGVEZWEF0rTyOEc6ZgtXzU+0bRc8WSdpMqWnUS5eVdl8TzSYofSIVdn6JLX9eHDW5tNkxXXGTgn8+AnGy03eEUwfxsz/Se4K2MLpfB6WxGmr/cd2tivko1FJ9tvXYT8oFPb4kpF8Qzw67XJ1XSLheU1Mn5uaHLfk7vKGK0pOmRT1tj3hrvVhtMc8ImKQjM9Y+yjvvjPLRHk/X1QkXUoSLGFDMfa8wk32fiLnA2Rx0vC87e1aauwVKbnJQz3Ngsle1Rc8ZOFIBwVpeNwq00YWRaWbXPMkpMPbmy9fhIA+lgGyvG3E0ONnMJ06JNw1b1j1t/fDBpzKBN5oIuddDNCMUKr1S7EXJ3gdNmu5ujokiq6EEltjENl0b34igjpiglt/L6WoyY0pf11Ygw7XbZ7LQla86YS93sx55SuEKbxADjZEaDWzxRUavSEnbHhcpPG1cvDgLVXZZ6FkWzjTe2Jf2CxVbbzcHGIa6+veet3VWeHGDf3sQkZ2U7DVthytjYkNerzbjqPOPOG1/cXpiTWMddHveTUs2xDUo1mJ/uhbFXZXhT7Te4vp3q+8P2LPvBMpf1U43Ngcu2xgawo9MutuOaHGdc113wsHd2h+W0mlhhQtZy0PSBSG9Xh7ORNrnAR1hDndflBuKOlEiGIO8m/NwGe+Ec2UpDjk6Yuuiks3iybaneovtqMT6dgJDnsVY54/1UTsr8FOD4Yh23ayrY4tXIo3l5FARadOGzvbqOaVokPN3HAClD3qqmdS9HfBU0K9a1ja7mvYmq6UrQsoxW4DbJ94eQMzb8WhR9c8JTpr4sF2Ukk8VCxr1TuR4x11TmtpxZns6ooXl24yz4CVPvZhMdHGbVZr5gj66A7XNYFSPsAnIv9PHLXhkrKT012s1kSdY+BOGZh2lbWTwvi2YX1sqa3VvXTWxStrBq6CT31fOWFbNR0Gpk3S/VfpZtWgxb72S04sXwdFywisc6Y+0Ccc81RC5b7Lx2a57RyUw1jXnFFgLJV36+DWDijoBSXGm6Hl9mXMvOhWNjLer2kGLuXvIWgqieaApdx0TL6GKBn/sDlTJ6QVfJ4rrCcE08t5VroNIyr83CdlNuXKCByXYxOw7EUqBz4uK3IjOrNaybL7TRrLPOJkHDUGhYmpNZr5Lu8VTikwPIhMvGqfztdn6kNkIWdBG22UUKvo+b7XYhuTS2KLEcW7OGpY7BduFtnc00mJyXfKdzwFxdOMU0yrOy25NYTukbLzAKZRYSB36LCek0jVfeZg4bgaNk49w22egCT4QdcZktav5iHSL6GPLRJiHEVLt2W3Whu2Hs8d1VzLVpx6DnXdiX8W4pbo1SdRdzSekXuceCE51btKj1xmK129k+tirPC8v3qMoL92EHGE7Wo8BaZRee0rIFz/So6qPXGGN4cGBFgsBOjmOd29NKQ/tVtMVT+aBTTL/Y8uMwlOu5H16P52Q7IaVNt6pyVN+Wel5XVkW2E4enan6n0bjEq2M/pc9plSpKE4SaGCyP7rafM4RGYitWOrKdj87aIJ6wChlfIlaiMzYS+KpZBI2zXZ1mcqqWBmh8LVMMf3Y8bA+st/J5O9C7NF8cOJ01V6zngCrDtqpdz5c2ftpkau3P8PqyEEMdnaRSMW4v9vmkOJyzW57kRXpSw97az/Gdc3BWBn+pF9Posr3uqp2uisuQa2Ytm3U+le6MeLsyG2kRx9fp9DDOy0OwoKfX9FJ0hccZ6AbPZ+x1Mc733pLal4ShjIOZIPU5nScHlJHZ5caJ2M2MruenttGmCrcQgtwurG5b5ekkr7SFI8yued5G1cKrpqLR17bauiomT9xA7raxOZsSJ8nCZ/NRF2a9uS7PXL9HJbfiF8pIl4TE5qNFCnfDI3paSVtXvh5pe+qU9DmMc0mkKE7l4xYVg7HEgxjDV/uNLTYwu87zXu3CpXYsrwroZW7PZbJVlSi3muwYu9h5eSm1Bz2hHeuw1wVtdMB4J6xdcq2AqQaUrBpNldTzVn1LkFx0nPf1Ou7SRDLPpkoGNrFsl/PrGasJKjBoAPRynjWwXTevxtqom1HaXKcWBbJ5oWHL0KRq0c/iYEWSa1zPUHLewoSsUEtprGy6kk6Tit/vYNMLlHGeiB0VWT25N4tDr567rSOv9W1QGPkmscUQy+Qr16A4kV3X6vLCxMV4k49GjdFJKw4rdqN87otRE87XHH0AwkKM2lAMeZTzaqqm1l0qUdpsdHFlyJnc8WyNkxngOCodj8dS4KTLoEw3res0pDcOKmJH4L4LrhPK0qS4TziPW2Ww3vbbrCNXYcelx+zSsPRil2eeQnNJ6XgsO3f6be+P3FUSHPHr7HAMyk0nBW0yl0/KaCcYCl7oKHExD0zUlct9tqMiY95ae3Cyq1ZzbBLug6k2WUWbcm3N3Pg6a0aGga/FVNznp/0umV8vgtJMz/OSsT3nFBf1+Mqh0tTEm3RWSsGUwYKoNGTJLIml6lwlRsc5ypvplkiYK9ghByWz1DCR8SdrgrSJ7EI446s74SMYYWuqRe6iKF2giFNZSQFqOZYtqMuCvASVu+N51Jw1h6tgXvCyuTqGQNZVukyisXSy7CPTqF2G96yG8lt6ZddM31t+O15M5PQ09aZGqYvppVpdYxaI5ppRAmzvWvxsNTJOYmi6iXUoiCyFrYSwtk7ahthxDXVasYLP8HGSSCfP12kJoCWtu+RoerlKi8r0zjT86J0zhjltestxPG8ZOhU7ueS6EBV1kBXomS8g3exNdmY0aBMcOb5cCWW/Tq1db3eH3AyI+fSwywp6C3XTGae6QP+fDxRJLS776xoviW5Dnyxd8R17eujry9xi0TA+JsEk1IwxR1wbD2ukio4YkxmlMwyDHNA1nCuBRbyvhGB+Rvl1M0/Q1WrieOVYX64iWrhyuVidhKnHlmuMNitlX5WQ+wlHX5oodbxoCQob+CS/sFx3MIucu+RXMJsLZMufkupgHi+pNznnwmzL0cFuOo89FFdmhjLlLFm3mVPBtLtta1pUeqQ6dj+rKazxwIbCxjnseMx9VRMMqTb4RB573YwdjYULj1eGR8xWjLbWG2x0BSusgn3gqRI2zVE95uLpQM3IWSgqa2zsUeOOOodwo2Kpje27jSPnbj9357Z1OrIHAH19vswTuIi2TrF8rAXH9mpjOi1LwThg27k0U9xKwTvHcXCs5lcHVyLP/UWiwEpn4gpfRs2ybC6wJ50fk717PfGX0dV3XXJhr935yOyXXHSIzLZs7fkBZ9X9pDFwTmeYqmaqTZeNL4sqkubtkg/qmOkTEhw0wzooLdkbeDHbjRdUwHXSsvDmYBdI+00w97rlCZwAsbIlYSp0XBIrroRh1L6OOCUd+VF6IBv2EhTCTsTiBpIah1O9frwc9IYA89GC3pfnTWXVKQUbL7UeJ9pOaEaHQrlyYOlaFp7rCV/GWnlmdg0RsttgJINRiI1s2K25BH4xXeHE7dYCYQJ0xfPbC7Xwi5LhU2fs8xGK9x0N1Z5MqcCmikN8Ok7UACSJWdCxq4zZo7LVpwK2cVn26flpOL98nEL+y7+7Dqc9/9cOne7nQ++/R9wOAIFhv97Wev3XVfvt+amw/EGx20lbGdXu4zjqv56zfflnT7oHMf39t83hd5Suej/FrQx3+A87PzgQDv04Zf+Kk8Tt5LesyuGo7iYV3nhVHA1qPs7EoXbYcCj+9Md/AkUMVf3CJQAA -->
