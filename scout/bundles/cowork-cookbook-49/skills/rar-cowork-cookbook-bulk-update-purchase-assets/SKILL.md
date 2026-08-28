---
name: "rar-cowork-cookbook-bulk-update-purchase-assets"
description: "Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_purchase_assets", "rar_sha256": "f524cb2346478d42c95cf9fcb1412a05563cd596405a624b8b4792855dba7b31", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_purchase_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_purchase_assets_agent.py` and in the RCI capsule.

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

Purchase assets Bulk Field Update — Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-purchase-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_purchase_assets_agent.py` and embedded as the fenced Python below (sha256 f524cb2346478d42…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_purchase_assets_agent.py` first:

```bash
python3 bulk_update_purchase_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_purchase_assets_agent.py   # or on stdin
python3 bulk_update_purchase_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase assets Bulk Field Update — Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-purchase-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_purchase_assets',
    "version": '2.0.0',
    "display_name": 'Purchase assets Bulk Field Update',
    "description": 'Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-purchase-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-purchase-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc6286a232c60202',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/purchase-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-purchase-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdatePurchaseAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePurchaseAssets'
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
    print(BulkUpdatePurchaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZOjSNLmX2Hz/VDVL1mFOCVqbMwWCQS6QOIQR1dbFUdwiUscEqjf/u8bSMqs7umZ3hmztVUdKSDCw/1x98c9gvz1xe3auKxfvrxowC0Q0c2yJAY14hYBsiivZX2CP8qTB/8hflm0deJ1bVk3L68vAWj8OqnapCzgdK6qsgQ0iIt4XXZCwgRkAdJVgdsCxPXrsmmQqqv92G3gddOAtkFq4Jd10CBhXeZwQSQpqq5FsqRpX5Fr0sZIUA+f6q5AqhpcEnBFPBCWNYB65HnSfoYqgN7Nqww0L19+/uX1JYHfX778+uJncAGo0hwqYtw12D9X5u4Lw4mZW0RwRDVA4wt4XYEais7hrQCEyPPqYwOy8BX57/8+Xd06an768rVAnp+vL+MfFerWxgBpS7dpQYD4buV6SZa0w2eEy67uMNrYdnUxwtJA7Iro82PmD0llhfx9fPbxscjnCLQfv76UUAV3RPbry09IWcP1IA7w++dRSvXxp89ZeQX1x59+yGk6LwV+OwqDWn/+9rx+ioUDfwxNwvuqf4dSHz70wNeX3xk3fh56j3bCmS+f0zIpPj4EV3V5AYVb+ODjT/9KrB8D/zQ68t+S+/NDcAzcANr0VPyn1zvIvyDo06B3mf962Qq69T+xBA5/W+4VeQL1r2Tf8f8H0VlSwIh/Q/yfivtnE9C/Iz//S9v+asIrEn594UGWXGB0eBn4gvz6TdsLi58/BD9ufvjlNyj6/ypGK2FO3CV8y90iCUHTfvv284fmfvvDLz9/6CoYa8DNv3V19s9k/jNc7+v8AcHnqI9/nAvXN4pTUV4L5D3SkV/L6n/Vv31Gjm6WBD/uN1+Q3+fL+EGR0Yi3RR8Q/C5nGqjr73D86eU3yA0FtKbz749hlv/XfyG7ZGSlMmwRzS8h70AHt0kORuX1OGkQ+HfMbUg9oG4SCOxzHIz/0cOjxmWIfP/f/p0lP/lPlsRG+vv2IL5vb4z37cF43z8jOhRZ1kmUFG6GqNx+/7VwI1C043KQ5hpQXyCReEMLPkEK+jR+gbyIfP8Lqd/uAj5Xw/c7aycPTlIXq5GPmi4Dn0ebzBgUTwt8yLWgB34HZWelDxUJE0iir9DWpswukM9G+5tTkmVIkECWhoQ/3GVDjL6Mwr5//+65Tfy1eBAoiTwqQYPBAe/qIJ8+QYvCLIni9msB/LhEPvz62wfkf5C/mnUXPq6xh9Y9PQA1XGuKjMCM6nI4DDoHuhPSxd0Dv/72xBWKKWDpgv5KwrEUjZNhRJ5A8AayJnGfCJp5KySwYJR1C1kZgeUEWYXIu75w0fHRyNtx2bRIACpQBKDwByjVhea8I1mULdLAsGvC4RXpGnBf9btXu3cVc5jabvsd2S32sEqUGfxvVPM+CE4uiwTC/x4Cj/tQSP2hQeZvIj4j8hiDSOXWbhXX7nON0H34BVaHt+lQuIsU4Pq1GEshGKG6J8QDHjgIIuM/Xfpp9Pm9lELHNm9r38e4Yy3T7zWt/lo0z2B3a3Cv2FCVAYm6JBhLwN+eIdXEZQfr/Ygf1HSU9PRC8PTKPQb3/9AAjAUaWd47hUedRr52xASnkP//zcSoHieKqiByusAjgqyr9gO2sesZ4X00SrC2I3DeI0V+1Ps3tngjza9FlsAYqIe/PUbewX6OeRBRV0NsVE69y4eehrCNcu+BOAZWXd8B+Fq8sfMrRONORdAXMGthVI/B9Lbg+PRNUwhLPF7/qNRPdMYchsEGsfMyGAghAIHn+ieoVT0m0xN8GJVgTKxrnPjxH6xCoHTofCgfgUokEHXI4Hfo5BKaCfPojv778GR0C9Qi6HyoLWwrwWfEhPkwxkQDHQCbmHEMROHDXRSSA4gxVPEd4SZ2q4cyYyf6VNAdfVHmYzD8zgPPhz8i+K7LqD6U6sLQgVheRzINQP/w7LueT19BZfMx5+6T/ujup63I78vI374Wdx3f+RumcjZW4N+Bg8AUyps7d45M1EA2ycEzgGAk3Ivt50e9fBTkd12+/Kn9/vifdej3Cmj80XNfkLhtq+YLhj2q1lvR+gyzAIMxklSguRewT49k+/SWZZ8eWfYHkQ+EviD/mVp/EPGM5y8I/nnyeTI+2iY+GAP2+YEoLD7N7U/U+PRroYIf7n3GwEig2QAr5ns1eRsCS0pUg2gc/KguzViUrrAO3ukUOuBr8R4CzwSBxhbRWAqb8neJey+r0KEPf72zPnxUtHDtYGy9IjBuSLJR/Qa8fCm6LHt9Kdwc/PVGZCR1GJ8Qh3HnAnMFNjFtAu5X7w3NePHH3dY9i2D6B+WXMZlekbH5fEXe+8hX5K2zv2+Tig5ubX4ee9hxSTgU/ngf+76V88AL3EW1QzXq/NiujK3Ts6X9sxJjDkGNfTAW6vI9KccV/yQEfokiUP9ZiHL/4mZPZmhadyy7SfuWzw3UM4BNzCsCvQbzDKYOZMQOTvjzMnCdGpw7WN+C0dwf+P0wq3zY8tsdhvax5/v15Y0hnj549ndwOEzFT81Y4TAYoXBBeP2IJfjsP+n8nlMhncH2A84NaYLyPYKkGGo6CyjCZ2k/ZEPfwymccCc0zZB+QLMMNaFdhqC8mUdNWWJG05Cwpx6JQ3mPYPz2qF9QJOG6/syf4lTATl3GB+TEI32AE3gwJcGEZslwNgMUROZ96gly4dPGh00jgO9N6IjF09RfXzyGgiMlqllxj88CY4+uZ2KeGm/ROkP7nmQOJCizAKCLiFyhuGQG1orLeec2SZrVkZib9AnGercYrHazu/F7VWLnIZGx11szbU6qnynEbBf4guRq8s0hrDx0aHdT5um1Shi99dSNJrZHxzeswLLbIu+OFdh4q8o8CjWGYquG2lDVbjN0J1PmmVMb1O3A6JMsqpOYSY3EzPUNbme5nToLemK12nHYaq3arc0j0alZ2/YmAMlGNuVjHSSl4+bHxarPKaJbl/s5YTdW1vuXW0sH4eLUWTU6xUQqIc94pbisYUWZcyRanckhyQmt4RL4chV19GR+Yq9Tf9NLx/iMb9c3jdcTfGMSBFD8zem2NGLOWARHy60Ma00HO8hJPm4M5iyKrcyJrLXbYCaXQs8a1WplyMx5QnSHZDc74QHs8RSbNiP6eh2cM7pkTNrwip2AGi1HdyfuNlyWdKb0y00VLETdnUUCn5y8vQ5oIbcrr/UZE2Dlaragyfn6wh2ESS3inU+nTWsvUdSvnctCMmlu8AvWXtPLoTZOpNASrbM4puG1G5xOM9wzz57UfJPacjuZzFOzzq14zUuZbDf5ENL5AZ1ezDVuHqNavGJ7Y2EstYjGhWqXzrfuACr0zM6IQ1qQvhLLN47dUW2HTnEx35B+H+68aiabvEuvku7GTuXdtuNtPNkkRmeJp/OyVwu67YOqyVYzC8hUZMdms25UD2uj1S7eF3FmsDLqMFGICZNjtxQkZr666U3f36ZrRb8aCRtl7QpEqE92U8ZNrONxadlEobmzXShN12VKbrT1YjmrlI1XiNszKa4cTNxWKCOt8d7ptuQisDJKlMl1ygT79Wl29StLyQQjx6j9VuJQrNtMZw7aK9vYqI8KS9yODhga0yRE3YjBsTi4mrmhzepYqr4/oI0jJ0nPi7uIyq7XmdtjrRCta1prT+pe3q51fCNhSurP92HeubnQH9cwu2MjYiebadkees7pJX51Sxuz6ubdQaiWMh4llbtwEyP2lvnOdA6dXNKyc+uOS1uypp3Fr5R9LmD9jtr74Zyf7q9XVurYuVlMF8HpuhdQfKtv6PSwv/CsZzlneagu6g62E0f5miZl2Z5QieyXoWP5udmjxHllbbCYMfFGP7q61SiquKDPCbY+e/awyJR5CEp3nzPr4UyRMeO2u/Bc4Wew3fSiatlYXt2S/HJ0S3Zp4eEq9GYLcDLbFqxTnZ2iVWBn/vE6jY7bw3Y20I5jMGhfzfdolWW6SJ3K+lhhjdEFlBDFmx5sbVMxyEoRZ/6RiA05HOYck9KsVCxFTI+9A+MbpwMINvt+3eX85CbwU3p94AshxAz+suqFzarRJt2E2CmY59D9SuMue4+TwbDuAlhSCMIu9T7fnw7SSsazdZF2IMGjKDvu8gkuNBOz8s+FaBzIs6ksqEN+wqSZdcxrw7vkjKgEymnfVjv2Wgz06TCwKJ/xpmO4Qtrr2+nZiQo2zlm7JvbH9ZxHp9OZJGKlboe0fK2ENUssooPuHNW29uTVebuT8DKX1M4OGwndFNFZOjWKGKk1DjWYz6pV5sXcyu62M0u69YXPxcVOW2t6plk1PpMJ6SD05UVGQT94+5bnBdFd6WebW/JDNNEoHC2xs6jv+tbpAk06xdoi2TUHsHWqq4DrQcUlNreOUso+HjWXVyrTtk8Xuw8yD5Iqt02MhXya3RwNGKSwtFCRtGdBs9GVconOusTd4PDhGUyx+NY16c4+nRm9ZhlgTXu0myybw4HYZQ6Po5OQmpSzzaUAtOjeenTJ7deSNplwGBqIiSvjpLRtPSGJF5NOr4YjGg7Vfq9Xm0KfMKDYx9zM6ZKqqYfbxT/G18NZ6PrV+dBWRXPZbZLzDtSFoTlEXO5I4kxE+UTv+evOPLiJAzhqnjhH2aJlzV7PMUYTdFVtnKrMy800jpbB5LrE6ePk3NG9e7gN0fQ8r1ErHcqe3zosudhk9V7gSN5m/fZETgk9KNb41ug3ksCTwfbqLbLz1l6uJ4Xn0+fd1tTw6mzwQjq4mDiPbZWe1p6yC7aRt74sVsRhoFU7ivXtPMK1KVgP1c2MwtQKyFhRaN8RIlsR7L0mL6NNRwtr5Za2NRUm+sSU6tNVmGonnhTtaBYegD6N0zj2lO1A6Ety46jGgl3sxanNkUuL5/uYcjWtXBuct5tTsU7kZ3+1KX0O5uCxM02tEVZzzZrUE1PuDuU1Hbj1je9vxaHHPCYTnF1FHqxDrGuCol5sU1voiaPNF7Pj+tQ0sO4DIMEmotyWlsLNrfBYmOfUicQJvzp6/c7I8/Q0H0qMk5lONxxJEw8Jf1n4ndjofj6RrqWpLcGuX/g34XaxmcmEnyfi1deFfXOqj5faJlhxrrGTk3rOKpPD1NYp7EQ4KpQUXUX7ViSXA7lSVCs8xPLCu1baEV2tQBGIemSsy6VzpGJNuBh9xBd9Y9zsbujXKVesrykREbeq25zgpjIxuX3R70X1GJw0/rQhpdQ4onWSVTor7BJhQ4k3xiHRfgOIYgoiUtym0flw2/DLG9BLgrWDhYPLNsCqjXS5kBKhN1hnKbjGi23EEvNTYO2DKFEKZ4nj62yzxOFWKLy5lXzpp47GinznaDnmXbzl0Rb7ZcrN5YtJS6EgZstkw5kmStBJYW+6I9XwrODG6wY2dB6vbEhvmCqucXC06qAu/UoVN3517PO+M9dU5GmCrFXH07ZkjtZi1mE0pxVmsmQWgC40+jgv5Ilz3MqAsW+UoNv8QpjicM+14pqy1HUhUKrNnLd6iRT4NVCWgqCgzc3Y6DuqvIrxgd9qziHUVoE10zxc0uvar7rcc5ZOx2HZTQOnSyGKdiFos8ykV9yRV9y14wvgXBab5Ym/HNqQB7a/FgTquNLrhb3lDFld4DvnZhEnaVm0qZzmPM8v7NU5BbKrpjZ1xbhzCU76Jm1zwzqxqrhbrLfg1N12m/OshE2XB3MB2M0qbmm4r2PzXW8wUXOMo2qQGPXWH8M8NeVK6nZ9DAAbw764qQ4efmubSxira9WsetYyfTesK5VLw/XWSpoEpc9L1bnQ5nxmTmsuWXRGKpSqxq8oiRYpkZ9Ly0FnYrxcdMMJrJbt7KrF8rUrOMIXunTXsC7Dd0Tj1ESc9LR6TiY3f9a4J1cKsFNLXbqqpEpaKuZnxl9wNQk3GGWizqVzk1MCKOlTLgoRvdPkbq46PDbEmq9f8UaFDfvCNEwtFIbKYUhyvxI9RsiPB3o5MzSftrr4RDd5kPImpXPiFSbMujv5fJyoPqQBfN0wK0IXnCmq4ZPqQIRhBfvYM0m0q4w2Yo3Er1dAHNUohlsBbmriXNqkx0Nuzyuc7MOoCSg1neJMaGQRd+UwaXWpJ7vhxvbOiqi03WI3u1SOI6vLCwqYEwHSaUGe91RgJOdZuth2kg4TfYOuO+y2uZXKiVRrF0Zj2k8nWTCoEaduL9VqNjlWdWaAJD5Mea4U5wNlAD3i90vHv+AnWELywTe9IdOOLYvJMi7NcTW6cHM1NjKVXZT8hSNmlKhZfnieX7fTSHJw2NoXRNTPY+0IjNTWp2Z8mNjbberFoncsyclsvmAnrV6nuWLKOyAfCLOdseUQbVAc56Wb2e6WN6tVZKLuWwVd1bW9wTpWcTqrp9C1HF9ny0VxaS8VhS7PtSgwREZ2pLXGaxbtgjgsMGcyxfGBTR0Cx1IGbg7KypX8buNUuHtWJxMitM/Bsiyu2061HWNaTvM6IY+Hm3+VIQL1ND+sIlrbMZAYVansQ9TjUkorrf7WwZQgLwMaxRhzKXdLa1V713pW3M6KbK9ZnegvhLInVauQonLf8PLFJp1FEUapYU7T7tZgCsr7kUsLoXSiSSqoRVJkbhJHYWqIkZmDXZfM7nydYOcL1geYwsKqDBiVxYyWTkJvMMtFK4PSnydqmqz3yfWUU3UboB0nbi+MYGqbNchTVs1t/Hg4UFM/6guKny0Ww37wcDXgr3HYO1J/u3isvG0LhaBFxcS3hUIqXQQLdKa7w1FXZL2iNeuy2AXH7KreNoO+211Kz+xmwQrVaqvIAUkBZ7XHpzjPwgoKmwLYlLDXeEYWXrj00zC99SdXG47XDShy+bQ3A7j/350PKXBvlzpfTfeqIfNTt+2HoMZkF7NClmI1e1htumrFRqLHJeDG06Gl+y1NpFM6Wbst6PArZSdYiRFUCfEUcRZbz0gmUbZ1ys36doJLotFhZ8q4Tec7VVii28Lb25eciuW+tQehW8nidKEyDYidG+fvPWmmOyf/qgg8j+11VpWvanxZz1g/SRVrLqVmOPMVlY9UodOqCwX39FdZkazjjtJ4Jr9Zt2gvb/qMXdnXOA9wtCBZelesB/Mw+Cpa8sN1cmAvnbW7tQfjIEEsFt1ciqY7Qcgx9ZTvAz4G1mWd6aVXTEqqyy9lrQheYlGV53tu2qFdv775TkApAwiWkmJMrBvg/Tqv/ROYLk56LPtdeuEuO9SbUnptt34R3Go6Xk7jQ6/nDKNKlEISjRSCHW6FkXf1CRiaW2bbs6XPwBq8F22UkDlb24K2U4hCpAlYh0spWHonUic7rzUraWsoYZc0FxWHFUCmGumaXo1SSbQwlzmPrrxUFebZCtUlilTSvsz7GeD5Qd9czhmYRM2WZ6RgYYHVnFIJFO6zk45tCXKC74mOCILZZu+Vl8uKs2DduN4wQLKJuWc2k+2FIOMNMw1IZnpND2f5HHcMi8KQAzTB9Ke97LVoik15C1/uUJifcdtSWwxPDk20nJX0eXFezXUKP05DwsYwUri6qVv3kWxJOyvkjjOLKjCRjsRIyObM5ZL0PXaRDW3nKiKgWO5I4xmxmYZmPrMGanezIl135qqbEzt/Lh1u7YzjxHRuazq/vml0QkeMEORczcolv52I6JQwLlJhO7S3WTLRwoi6jr0VDFBs11eknj3hmCbwmDBN5/1hWcc82KYHeZ3ycb80UBsfdkxaXZ2c3+8KLmYruCfL5nqEJlmpMPvVus9a0Zoe8MLEkilOU+X2IkuKF4U7mBmtn2cMuUAt1MtTvDugVtDQhxz2HkZ/mTFVlx7UDUrvZq6vRco53LVyhbI3BaRmQVyp2TxP1iWZ1dtr1E+kA38ozSDsIj6kRU0p2XR609Gpr6sR5g89rcCgn6yrgSnSKMTmNaWIc0rZHDju5fVlPGN+nhT/O695xwO8/2fniI8jv7f3RPdDYuAGX+5rffm3tPnl9aX2E6jL44S0ybroeaj4D+ejn/7ixcI4cXi8Lx1fYvXt2wl660bjb/e8JEXQNW09fGvKrLsfzr5CsJrx9w2ab89D6Je7KXnV3p+9qw6vXP9+KvytLb8FSVOVzXgzKcaXMyBIHmPGy+h5Xvz6EgzQI4nffCMZ+huoq9HM59uK8ax1fF3x8tv/AWwXdwQ+JQAA -->
