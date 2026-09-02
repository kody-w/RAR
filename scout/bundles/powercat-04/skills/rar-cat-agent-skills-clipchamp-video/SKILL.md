---
name: "rar-cat-agent-skills-clipchamp-video"
description: "Produce a polished, narrated demo video of a live web app or Copilot Studio agent \u2014 real screen-flow footage under an AI (Ava neural) voiceover \u2014 either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clipchamp_video", "rar_sha256": "2e87128dd2c080ab21531502b82cdfe9e1d8bb835a873d40d586a62fab55e4f8", "source_kind": "rar-agent", "source_commit": "657d2bb31e7d75b8fe4216443a5336cb035c07c9", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "clipchamp_video_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/clipchamp-video:af0ebc2dfd21bf917db4b54f5efca53e6a7608640487ed8e2059eabdd13eb8ec", "kind": "skill"}, "version": "2.0.0", "author": "Phi-Lay Nguyen", "tags": ["video", "demo", "narration", "playwright", "ffmpeg", "copilot_studio", "clipchamp", "tts"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/clipchamp_video`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `clipchamp_video_agent.py` is
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

Clipchamp Narrated Demo Video — Produce a polished, narrated demo video of a live web app or Copilot Studio agent — real screen-flow footage under an AI (Ava neural) voiceover — either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#clipchamp-video
  Upstream author: Phi-Lay Nguyen
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `clipchamp_video_agent.py` and embedded as the fenced Python below (sha256 2e87128dd2c080ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `clipchamp_video_agent.py` first:

```bash
python3 clipchamp_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 clipchamp_video_agent.py   # or on stdin
python3 clipchamp_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clipchamp Narrated Demo Video — Produce a polished, narrated demo video of a live web app or Copilot Studio agent — real screen-flow footage under an AI (Ava neural) voiceover — either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#clipchamp-video
  Upstream author: Phi-Lay Nguyen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/clipchamp_video',
    "version": '2.0.0',
    "display_name": 'Clipchamp Narrated Demo Video',
    "description": 'Produce a polished, narrated demo video of a live web app or Copilot Studio agent — real screen-flow footage under an AI (Ava neural) voiceover — either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project.',
    "author": 'Phi-Lay Nguyen',
    "tags": ['video', 'demo', 'narration', 'playwright', 'ffmpeg', 'copilot_studio', 'clipchamp', 'tts'],
    "category": 'creative',
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
        "upstream_slug": 'clipchamp-video',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#clipchamp-video',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'c2e348b1022ad7a1',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:produce'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ClipchampVideo(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ClipchampVideo'
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
    print(ClipchampVideo().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+15WZOjyJbmX6HjPmRWKzLELohrZTZCEhLaQICQRGVZJouz75uAmvrv40iKiMzbVbd7zOZxlGaRLMfP8p3VnT+ejLry0uLp9Uny/C9bo0P2bt2B5On5yQalVfhZ5afJ8LpI7doCiIFkaeSXHrCfkcQoCqMCNmKDOEUa3wYpkjqQJPIbgFyBiRhZhqQFMkszP0orRKlq208RwwVJhXytcRQjkQIYEQIlAZB8caL0ijhpWkEKpE5sUCBGgkwF5PO0MZAE1IUR/YI0qW+BtIEvHyyAX3nwzqmjqEM8YNgRKEvks+PEGXCREQJsF3ypqvKXQRejLEFsRlBrP0HgOmQW+ZnlGXF20/goQIpBKrD9yoB0SFakAbCqFwgJaCEZZP70+tvvz08+vH56/ePJiiBPCNE7I21AApJHRuLC51kHIR4QzUDhpEUMH9nAQR53n0sQOc/If/5neDUKt/zl9WuCPH5fn4Z/cn3Xs0qNcgDbMjLD9CO/6l6QaXQ1uhJiWNVFAtVGyqrwE/flvvKDU5ohvw7vPt+FvLig+vz1KYUqGIN/vz7doPn6VNTD9cvAJfv8ywt0Byg+//LBp6zNAYuBGdT65dvj/sEWEn6Q+s5N6q+Q6z2STPD16Qfjht9d78FOuPLpJUj95POdMQS9AYmRWODzL3/H1vKAFcJYrP5HfH+7Mx7CA9r0UPyX5xvIv8Mgub9+5/n3YjPo1v8bSyD5m7hn5AHU3/G+4f8vrCM/AeU74n/J7q8WjH5Ffvtb2/7dgmfE+fo0B0MOF0MCvCJ/fFOkxey3T/bHw0+//wlZ/7dslLQurBuHb7GR+A4oq2/ffvtU3h5/+v23T3UGYw0Y8be6iP6K51/hepPzE4IPqs8/r4Xyj0mYpNcEeY905I80+4/izxdEMyLf/nheviI/5svwGyGDEW9C7xD8kDMl1PUHHH95+hNWhARaU1u31zDL//EPZOdbRVqmDqx9VlpXCHRw5cdgUF71/BJRH0n9XdkI2+1LbH9H4NMh3WGJMOqoQpaF4UdvRWiwAFbY7//LMqovtzL6pQz9KCrH1lvx+Xarw99fENWDYtLCd/0EVlh5KkmPwgsF3EKhrOMvzSDjoxbKM2GoL2UdgX8i3/+F57fb8pesG3T8mkDQDegJG6lAnKWFUfiw+g61EzG7CnyBtRIWiiKNItOwQmT4U2cvg+EnDyQPOKyh0LbAqiuARKkF9XR8WF+foUfLNIJNpBpAupmI2H4BEUgLKCSxByBfB2bfv383jdL7mtyrLIHcm1Y5hgTvCiNfvmQFcCLf9aqvCbC8FPn0x5+fkP+N/LtVN+aDDAnW9xs8t161VsQ9AtOujiFZiQw+hzXl5pY//rzjPmiXwI4Ek8V3fHBbDLl9+Hiw4O6MN09AmwcVQfGQ9DNuyNWDuCB+BdGCCVw+f00GFunQ965+Cd5AvC++Q//m2rucwSflA0PoJ6dI4xvtLbwGZ1ppYb8ggoO8IwXNhX6tBo96aVnBiMwA7MmJ1cGVRvXhwgS29hImRel0z0hdQlMHzt9NyHoAJ4aVx6i+I7uZBJtYGsE/A0A38XB1mviD4x+xeX8MmRSfYIxxbyxekD0YOn5mFEbmFUYJbnSOcY+Ioa8/1kPmw6hwRYb2DAYf3dL1FnkfrX7/NrrMh9Hl1rDfpon/P+kMUE2XS3mxnKqLObLYq/LlHtdWmlSDRfepEY4g0IbinqQfY8lbBXur7V+TyIexUHT/vFM6t1C+09zrZV1AJeWpfOM/FJXixtevYEAOEVYUQxIZX5O3JvIMoYewlEM9hHUjHKpQ+i5wePumqQeLw3D/MVAg91gfchBmEZLVZuRbiAOAfUu4yiuGdH4ADqMTDJ6G+Wd5P1mFQO4w8iB/BCrhwzSBjeYG3R6mJRzC7jn2Tu4PY1p2jy0b+q4AL8hpSCOYCiVigiEgIA1E4dONFRIDiDFU8R3h0jOyuzJpEb4paDx88SP+j1cw9sA9at+zHfI0bKOCSF6hC2DYtXe/vmv58BRUNR4y77boZ2c/LEV+7HX/HDIeavjRX4wouoXUBzSwTRRxeat8sIGHJawpMXiED4yD20Twcm/q96nhXZdXZDZVkemNt3Lrdsjn+K2v3lrw8WefvCJeVWXl63j8TvbiwsypzRc/Hf+X1vmP9z735ZbZP3G8G/+K/Lw9+onkEYivCPaCvqDDqy1M2yHSHr9XmOGPVmAjn3+4fjjq5ohbmbnVOBgmQ0wOlec25cjgw5NQnTSGBW0AuINF/b1xvZHA7uUWwB2I742sHPrfFbbcG+9bI3r39iMToO2JO3TdMv0hQwdPDb67u+a9zsNXydBB7GEUdMGwLYoGc0vw9JrAuvT8lBgx+Kvt0FC7YQBCtIZdE0wFOEpVPrjdGbBcDpAN1z9vPMXbhREN2ZIONdQuhz74gO6mrl1AXYb0cmFvBMUzAlV0K+9mwXVIsWHMMMFQEGHTtgeVqy4bdLxvl4bR7X2u+68a3LIUlhc7fR2SFTZqOIM/I+/j9DPytsG57RGTGu7wfhtG+cFmSAr/e6d931eb4On3v1DjMdn/vRKPCvJ8HyHMoQMPJv6FTZBbAfIadnx70OfDwA+56V3Ynzc9q/ve9I+ntyIxXN/Hj3skwQV/NxEOJr518m8DH2OgvuXXzeLbKPvNgO4eOvYPr9xh/Ph2j8OnV1hQwPMTXAwTBM7n/W2n/XQXDrX+GIIhB1gavpTDBDKGaQc5wbkgGzQOYTb9IGB47Ns3+uHi9d9MzvfsfzUcFJgWbjs2jpkOi01skzQp0qGAYxkUAWhjQqMMTaIkMwE2A3CUYoFh2jZGAJMBFhRaQn/HxkPoGBsAhuq+o/jfTu9Pd3pY8HGKhgtwwEwwnLFt3EIZ1DBxjCIwCsVNBrdsB7AAsxnTZAjKYCaETaI2xdAGjTuGSVGAdJiB32OgvCvx7W14f8P8nuTfrDSO/UFFmprYuGkSGJjYE8pkHEDiGE2SBESAoC0TJSgLnVjs0/vSB+6DW+52DgEIZ0k4yTWDnD8efhyCiiYh5Yoshen9NxuPNB3HyaBteTahx2nAsQJeyand7typam0KsefPJadvCfO8dzd6ui571dxUsE5OZO/gzSRuNZo27FqNNOK8iyrzoo52S0FYBKG90qBnqqPa+suruT9GY17Uc43cXnA5OhYLizpqZFzb+WLLjMW9RKZoFgbZ6ZDmnbI92/npUDPpBRfs1Mx8FBcWCRbI60klG912oXntVvSxZST7Z1tLgDfrNsRmM9LzaNHxwQVTRnYYbx3dP7YHLQpP9ppJhfjSbDV8TQNlzxdxGqBUTG7OSul7ZYkmdJS36MisU1S6+HYYxnnBndVeuRSYpjNCpHTaydb0kxV6pnzSQXlk6sy6rMdpNdP1hkj5WZApazNXUk6MNiZ1tuQjfwVakkwwlrGTaNQ6UntpzhN2PBLbbVOqDLQxRcPzCduQXT335o67FXEhM6KzWB+TemGuNONcpRv6pM/zSl/FzP4gm8FBZPyDm4tivs/m1wnQTN1nMbXJ4ehO+oyRzi64iLpZy60TkT2ahnEdza4eq/HbSvCb0qzz2JdSVlv2GY6K41RsTtRxm4gkSvvkbhqjqiswBQuyoNSW0BcViTcCNyXXyz5trPA0IgCLNlyTCsxcXwk+4U5n9LVg2XkmstuccxrvaB7xg71TD1ieKG204wI5PPsxhZfeJuo3rLG5uFP0uBrPgoUSX/ZlaEyxwp6s0dBT4zg8qURDsTG777l11JFW6Ie71l17e707TaW4k2ZmhjqnUcwYHedz5W6SXTubHp/nZm2Vyz06mmtux7PnctSr0UhMSkHJop2b19zSCTHMLP2wpwxh5fhssZgFF5X0sLE51XR/Cc4T5hhZBEUU9u541YkM5xQc5w89umIwdreeTTZ5XglNz1CXHPfXKzo5hf54f9Fiq6T0KDrXltMe0WWyWuGsF9KN7Pj9kXYcZSGRzQmXcp9RR8u56S+ATI58GQuoaR6tD0Ab86Xno6K/99xR3FjjcKVexnzL892lc1NxFtSBsIXjRm61k3AzX+uGuc0PxlXSZhR6spPeiw9RhdVBFSrMpcZKjSMP+S5rvXQ5x8rFiNjwXRNp+LxsiDKbMYcx1U3Sqcm0V6yD0VcQHOrm67hKONUXBL3g9f04x05kuLU4Q24NcWcffNvy9zOXnUdBwuwY0u4qql+rpzXGgFrZYN6uYEt1YY6neBZgUrcr9gyqmrvstNIs6epeTwxhKNZE7efjEVCILFjIamRe2nnSq2lYYT4bJ37jT0Pda8iJwiyPrKAxpWrTNd2kMSVqUnkWFR/mdC0kwWWOcqdsFzVkKAuqwdf6tCw5+rLCg6UfjfLZSau0U8RboZHm82i8j5vlWJsXF7zbUGcn3KpbrF5GbnXulxw+T1LgHCMfFPRZK61aQ9f7kTwlwJ7UBEe0Jq1fyMpaysXRYcWUp6PsixOvOju6Lat9YIcBDk6u7CgGO/fUtXMUxVU534TKmRQxbJMEtUFhcTSXVX6aoCvNlpNFd0j888WiMtPaBqNzpeZETFC1dxbjxSQo1qUV9pd1NUv7jHSLI7aJtqPs2pj6fq6buKmCMgnmdFIrbMFQ7GbvXCfe+SRPiI1bqpmmClu7jjZsmcx4c7/0PaerVHylLnaCZhK+U/TnMexeTZ92sqiP+eOIdfsmvvqhlraLvJqedkS5uWAHhZWd6Gz2xzbSE+tSoBRdsAea2LmOYHJGm14Szl6O0M2U2oI8PW3lpq9np1HYhVYnhJFJ+lRfo443O4d6q42YRR6XDBEkI2WF+8RKFxlrzvnbhIwwC+OPJHsN1sKkYAvYIGbLEKbKlkj2no5tDrS3tZfXcHcu9csSCHOLXh3jYDGtKxzsjYtnN5KUoXa+9Vt1e+DOkeS6swlPXhfWziHaaJIrLKrBGWDRjEK57WnXzPeaFq8detFk03Q6iU9c2hCzpTidUvWhJGLsUomUiC2MUguKsyHYas4K+0oXduPYdTG6CzKZ8f2LO2t0abRSGHyJrg7X4uJaPK/w9loJR+mBuAaCaDd6DRWblk3ox8yoIfpmpzr+FLiqyMH2kHL7gCkP3EG8ioDxuubInfoRu822c9yhLcLUup0XNXgnCf6ZXKBr4LNbor7OI5dUME4OpmZ6WteedslaUmIFXfDbQD+Svge7UNOTXsIFaYjmG0lLtYOqr4NCr9o43wbG7HDk1S7PsGk3Mq1zN8JpKlWvSqbKHWwwV3J0lUGrnJLLJmxFi9953VITWlRW9K3C7HnM5MK4srEqvLQLuaPPs4xKOa41D1derJaHxX4NwmuQ8yG9tq0jrPmRSoeGcMLzy+ioq223Zo9rQJLyFt8t5LkYUcoO36BuQHp7lAK6MDkHu5NxZNjVxuWKzYhd6/ZMRjfzeFL5zJo0WN1bbo9FvJyU3dK1ZIItrtiG5xRKhdOPAR2ZrdYOl1Suuj/w274MO0bXmfhIZfXMCgyPZONmJcip5Svyph9ven4JPYtl02ZlLIpDnLMhfWRIs4pIFfgrXJqrHK9SecNnxWaHT1ImZGkBnxWH2Ra7OjAcuUVUJen2IPeGv+lCUkuudTaN90LV2ArRhOuNx16VcQazhpcSf3eIPEVZHCZdH+q72SxaCOL5us96BSW0TU2sutzMF/hmfBJXohMLOxnH3UshTYPmdNQqbuZhhT475Rv30p78MpISrtetjXkAKnMxdjUN6O4gHE+HkGm56UI9nop4thC2+gLn+gnZdToMxSW7WKYHRqb3R1/jitNBQj1FEAwWR4NxshTUjuNdc4WthdC3BDtcL5NAMkidsrzIW/oTEcMtT6w0U/PSqQR4/RxcDqdOw73YNIPGbSpYSpfxTBcJrb0W0yJfJLSyVmvsdCH5EKuBzc0td1UxSpqeaG2zdulxYlOtMaWsiDu3hD/uWx8Y08qqHNdSdcZo+YCGyR7zNCys1YUw+FDzI17Q7X6rykq7nmb9sSpROFTuOKvCQ1m6MB1KT6iRQM8Mq5+43ETE2Ylbe5OFYa38fI4tpB2wTZ5m9UprtLXobdeSm150bI97SW+r5zJLpQgF/Xk16hourbelNeGukm0s941pdpJC6TPMXMwve7w+9iNPNPYuRp77yzUl5/WpsxKJT6U55JQmY4zmy2VEFh7bFadmy3ahHse5zk9r2tAzlRL3zYlVk9RPsp6fRLZjmnE5XbtwWh4bU3Lems2i7RuVCLieQNc9YVRTy6wnNc5M0A3ONRHKu4RPhOdkt24T9wgqaTxGBYLm1Gqj1AUxGaUOOTmdKJvMV/nenqhwBopG+GK8mWiuXkh7SUGvkuL1Yblk6YV5cFx1nS7I1W5lLKnkpM0St9pEwSrlmVmmM2d5uSzJgDkdqcQdNjbEpQ6ituT5bDmJjDlq7bmRnbWlo9PAiibXBEaVtbJmbtzPnBHgRxsxBaqWL67NpG2uiXQNVuvRZKZX+/NWPLOkdyUS0+HJIGnYcrW9oJHb6p1g0KeM7ps57Hxdam5b27Pkld4KWuqstFrsK5sqzpQz7l1MiBJFtspj5C6K0gUqQYK+BKjlWOxO4/PlOai8rSBk5qwR+715Jspme6F3dF1e+CQaH46MLc8brc2IbnZBhQ2ztGu2W1t+OF5gyuVIuqRR6nD0rrr+NL1I5mqszvnItYTNcgSSibK/yqQkM3tjsdXUNREtp6CCJZHn/HNaKOu2x/n0kDiomm2ljSpaYMGgtoCTcj1bUhOtNR0sRW0pCWWZmlOHSqMKuZyzU10ASrsEl6W+PexH+8Bjd+XSDa+EYG38dizRS4MKxOVmPRltim5nnPuE7bN6XDfUJEzLViPKidwTx7KVvbKKpC4wa2YKV8i+t7cOhuMWda219VSfx+x1z4YEjQqXvG/kWBY5b1vpsYCL+5UTFKnFpmSnM1iBYmTCj9FzXi5p1DvPA2NfozF21ucm4dp+1elZ0TjLKJc7bN7sU2eL2kcX3Tf8Al8BfjO/bk1smRJWl1iGMN0VK1qqZhQrnrrT9TRebPzVusmjc5Vc2bmRnGcrsOBSGwPZUWpTfDy1MWNrY8U4GIuzERWdjsvdadWMSBIP8pO0UYgc0HzYY7RkVY1jCgrT6nYo8RdqQ3NJIxz2kjwZzUejTdovx1t6gRNu08iXcLYK5vvDWXY3FhoWx7PikBFpxamYk5et1vZ7fBE5/GgtXdvdlJmFgqSxDBCloE19ObAXYtVEGE+4upmfuVGzvzRR54vjvSGuixOnRrvDJL2c/BVHzsdwp3fIrBPYrXbSoS+vmKOaXHTFx6bhNGfVklWxLeyjUM4VYVI1FkVHAb5p5iUllXg2gQ2nFYUrOHKAPKx8Gp0DE70cZM3Jz9Z8mS0t8RKq/faam6YdS4cwu9pyh0a2lHLtvl71k2TTbsY9u0StYzQ6rkTTJdi0as3zNhOjEESTJPI6QhivYPFxVdU6r3YFIebbmFj4Re2P1zsulTIjC4osqRo+F00UJ1erKYe1MDtLTlnM4KpA2wfZVnUY+VjkzvbcqfWOcCtJ5i20NJoNQZ0bbwc3juOpE1ULcDCVA2z0v/769Px0+xD39MoSOPX8NBy0Po5L/83Rmtv72bfHOriMeH76f3cydD+lefs2cju4BIb9epP++rc6/f78VFg+lH8/eyuj2n2c/fzr0daXfzleG6i7+0fB4QtNW72dGleGezvte6MavrQ9DYfJxePY8nZI2V2L4dMkvLl/8xoOHu+f3L6Vt09uw4M3icOZaFUOyj6O6AfAhjP6pz//D9gso575JAAA -->
