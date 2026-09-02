---
name: "rar-cowork-cookbook-bulk-update-analyze-and-segment-goods-and-services"
description: "Applies a bulk field update across analyze and segment goods and services records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services", "rar_sha256": "e51c2dc320ca6713291445f61939927d97984eb587c5c0237d017e62312ff7a7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_analyze_and_segment_goods_and_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-analyze-and-segment-goods-and-services:8043db7b475ce9a79b982c3d7964de43be65515e38a6b2fecad4646ffd277e9b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_analyze_and_segment_goods_and_services_agent.py` is
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

Analyze and segment goods and services Bulk Field Update — Applies a bulk field update across analyze and segment goods and services records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-and-segment-goods-and-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_and_segment_goods_and_services_agent.py` and embedded as the fenced Python below (sha256 e51c2dc320ca6713…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_and_segment_goods_and_services_agent.py` first:

```bash
python3 bulk_update_analyze_and_segment_goods_and_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_and_segment_goods_and_services_agent.py   # or on stdin
python3 bulk_update_analyze_and_segment_goods_and_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and segment goods and services Bulk Field Update — Applies a bulk field update across analyze and segment goods and services records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-and-segment-goods-and-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services',
    "version": '2.0.0',
    "display_name": 'Analyze and segment goods and services Bulk Field Update',
    "description": 'Applies a bulk field update across analyze and segment goods and services records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-and-segment-goods-and-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-and-segment-goods-and-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d514fea47121dc5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/analyze-and-segment-goods-and-services'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-analyze-and-segment-goods-and-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeAndSegmentGoodsAndServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeAndSegmentGoodsAndServices'
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
    print(BulkUpdateAnalyzeAndSegmentGoodsAndServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166ZOjxpbvv8LUfLA96i52IerGjXhIbEIILWxC7htldhCr2JGf//eXSKru9th3Zhx3PjxVVAmSzLOf3zlJ1q8vdttERfXy9qL6dg4JdprGkV9Bdu5Bq6IvqgR8FYkDfiG3yJsqdtqmqOqXTy+eX7tVXDZxkYPlTFmmsV9DNuS0aQIFsZ96UFt6duNDtlsVNXiU2+l48++0az/M/LyBwqLw6udI1cUuoFD5blGBwaAqMvAEivOybaA0rptPUB83EeRV4+eqzaGy8rvY7yHHD4rKB+JlWdy8Asn8wc7K1K9f3n7+x6eXGFy/vP364qZ2DYZelkA+/S4Y8xCIyT31IY4wSXO/fcgCaKV2HoJF5QjMlIP70q8AtwwMeX4APe9+rP00+AT9x38kvV2F9U9vX3Lo+fnyMv0cgbhN5ENNYdeN70GuXdpOnMbN+AoxaW+Pk9pNW+WTAWtg5Tx8faz8Rqkoob9Pz358MHkN/ebHLy8FEMGefPDl5SeoqAA/YBpw/TpRKX/86TUter/68advdOrWufhuMxEDUr++P++fZMHEb1Pj4M7174Dqw9uO/+XlO+Wmz0PuSU+w8uX1UsT5jw/CZVV0fm7nrv/jT/+MrBv5bjL59n9E9+cH4ci3PaDTU/CfPt2N/A9o9lToK81/zrYEbv0rmoDpH+w+QU9D/TPad/v/J9JpnIPI/rD4n5L7swWzv0M//1Pd/qsFn6Dgywvrp3EHosNJ/Tfo13d1z61+/sH7NvjDP34DpP9bMmrRVu6dwntm53Hg1837+88/1PfhH/7x8w9tCWLNt7P3tkr/jOaf2fXO53cWfM768fdrAX89T/Kiz6GvkQ79WpT/Vv32Chl2Gnvfxus36Pt8mT4zaFLig+nDBN/lTA1k/c6OP738BuAiB9q07v0xyPJ//3doG0/4VQQNpLoFgCLg4CbO/El4LYprSHsm9S/qZi3Lr5n3CwRGp3QHEGG3aQMJlR2nAK+KyeOTBkUA/fJ/3Du+fnaf+ApPwPn+gMz3J1aCb+/9iZXvd6x8jjzw6ZdXSIuAIEUVhzFYAR2Z/R6ywwlZgQj3YKnb7HM3SQEkjB8odFytJwSq29T/G/TLX2f7fufwWo6Tol9y4DkbuNODGj8ri8qu4nSE7HspGBv/M0BjgDZVkaaO7SbQ9KctXyfrmZGfP23qAqD3B99tQblICxeoEsQAwT+BsKiLtAPIOVm6TuI0hbwYlAhQhMZ73QDeeJuI/fLLL45dR1/yB1Tj0KM61TCY8FVg6PNnUDWCNA6j5kvuu1EB/fDrbz9A/xf6r1bdiU889qCC3C0Iwj2FJHWnQCB328lMNTQFDgCmu29//e3hmkm6HJRTkHFxMJXHZnLXd4EyafDw14ezgM6TiH715PR7u0F9BOwCxQ2wFkCB+tOXfCJRgKlVH9f+hxEfix+m//D+g8/kk/ppQ+Cne5Wd5t5jdHLmVH1foXUAfbUUUBf4tZk8GhV1A8K69HPPz90RrLSbby7MiwaqQWbVwfgJamug6kT5FweQnoyTAfiym1+g7WoPKmGRgj+Tge7sweoijyfHP8P3MQyIVD+AGFt+kHiFFB9YEyrtyi6jyq79+7zAfkQEqIAf6wFxG8pBfzA1AP7ko3vO3yOP+Z+1IlOrAPH3VubRMUBfWgxBCej/m27nrowgHDmB0TgW4hTtaD0ib+rWJp6PBg90GhBY90ijb93HB1B9QPiXPI2Bt6rxb4+ZwT3YHnMesNhWIJKOzPFOf0r76k4XiAKtpxioqrtdvuQfteITMBJwWD3BHsjsZMKJ4ivD6emHpBFI3+n+W9/wtM5kMRDnUNk6aexCge9795RoompKuKdPQPz4U/KBDHGj32kFAeogNgB9CAgRg0AG9eRuOgUkDui1Htb/Oj2e3AKk8FoXSAsyy3+FzCnQgR9q4ADQUk1zgBV+uJOCMh/YGIj41cJ1ZJcPYaYO+imgPfmiyKYY+c4Dz4cgaKeiBPh9zUhA1QYRBWzZAyeAhBsenv0q59NXQNhsyo77ot+7+6kr9H1R+9uUlUDGb2UCNP1TP/CdcQCUV9kjUkGlTmqQ95n/DCAQCffS//qo3o/24Kssb3/YNvz413YW93qs/95zb1DUNGX9BsOPmvlRMl9BFsAgRuLSr+/l8/MjBz8/kw98e5+fyff5nnzPkUfy/Y7Tw3Bv0F+T9ncknmH+BqGvyCsyPZIBmymOnx9gnNXnpfWZmJ5+yY/+N68/Q2NCQIDKzvi1EH1MAdUorPxwmvwoTPVUz3pQQu94eC8sXyPjmTcAbvNwqqJ18V0+TzpNfn648Stug0f5VBG8qT8M/WkjlU7i1/7LW96m6aeX3M78v7yBmoAaRDIwzbQJA1kFmq8m9u93Xxux6eb3+8l7vgGg8Iq3Ke1AUQRN8yfoa//7CfrYkdx3fHkLtmQ/T733xBJMBV9f537drDr+C9gQNmM5qfHYZk0t37MV/6MQU7YBiYEi9STLR/pOHP9ABFyEoV/9kcjufmGnTwypG3sqpaCCPzO/BnJ6oBX7BAFHgowESQawswUL/sgG8Kn8awuKtzep+81+39QqHrr8djdD89ir/vrygSXT9aOTeAQRWPAv9H+TkT/q9vvEyp4I3ru0u83v3e870Dee6vN3j8Kp2Xh/ROnLG4Am/9PLZNkqBi397b5zf3nIBxT71jcDCgBkPtdTvwGDJAOUQBdQTkolACC/YzANx959/nTx9qfN9l9Di7cFQuCeQzkERbo+bVO0Qy8wF/coek54PoE7/pwkUdLHF/bcwQLftT1iTsyDwMMoyqcdINbk68x+igWjk5eAQl9d8b+wJXh5UAQFCCPngKRPoi7muTiGuPacQnGMRgmCDOYojdM0Rnk0RS8I3yEXlEu6CIZTHoJS/hzDUSwIKJua6D1b0IeY7x/t/offHjDy/mhIAEfMtt2FS6EEoG3PXR9HHNz1UQz1KNxHSBoPFgufAOu/Ln36bnLtwxJTnIN+Z9Jp4vPrMxam2J0TYKZI1Gvm8VnBtGHPMco5Rs6smvvW+QSvndyQ6hrFCrs/eUafC/OlxNw6r8gZ3kviXblJSrauQfsYC6FGcjm13NfNgtxS41pv+iTuTSw0GieXktt5QaU7enHehPGqN5MMmSGdWoc1Z1gNOhbV4G2sYV/kg4Xt0qOxv8JHe69sr5qr4r4qydKJgmnNG7LWL4drqHMW0vnyMBK3dXtZ6SU1mrAuc+VCXB4z1hAiIMQ1UsumNdaOqJJckg3i0TOkTlrhZoxyZ97OuI2EbW6ntuy3y2uwz9GZu7/RtAvPjZ0Io2QrU/EpvhWtUJdLNDVscluAbUG/Ko9VdTBqd0hLXplHySKVUp+UD3WKEop+JPS6SWB3WBs7Q0N4bn4lKuZqxOtOWw1W59nWhg9reljXali0q4smWSPSd/wSXcZRY5gCMibnihCujYxgg1hQpr/B0hPNJt1tjW/OS6tyhmxEQ3Z/HS9GbYRFqh/GrjjvEmnVy7eNtjE506r26sKs8j2zUeMRl/h0yaRwjI7majR6Jx9JZ0fWaKK5FAMniXFYzIxNc+QC2VdLi0Vld/SzEFf6QBBlLq55c3TYZcVi5Wmbq3bWCo4hKXlQrZLrDhSLxDZXi4BZuPr1gEZMzunLsV6LRo2otHcma3q/34VnqcqUOXn2fBoujhbl9XxN1zlDnxW5zjfUHkHSI+diaMmlm9JqqeXWO52bwb3WqbU4+QqpH+0hVFSunbm0kJwTYovf9C22a9dwn19iwjh0Idk0q15EulobBZG/XVfmoaRYKQ+orrxK6TnNvO7sLatb38RdNrJ+SYTrXK2p8tw7LdY7s5vGUphWI9hta/t20LJa5bTHWom2QZk1pzCEy+wUEr62JENJ6OqDz1f7hdiTo5LjBAxHIxv2nTFrSjEcrdzhTITXrNbjKdvWkDTdNmlxtpCdqZ4wPZsdzeNFkFp135+V/f6yiHl3NMeCCq/bua134jpw59RCrEzzvLE0QU+9cI4cV3jEu+x6x4XsruVYXRnWGSF66wszxA1nXhjtoIq3YHu7aqIYWztN2FKpKSzR2Vzr0SrFeSrMPB+RO7Ebdod25icKfslvF5yV0bWDxuqsiLbmjd43W1RrD3glawuzHRpyjHKfgg04nNloEJOc6uj7FS3NAzU78de2i+rVcdUKI2uj0uYGmuaVKuimvsQ9W2DYunD85Aynt7w8Nk3HuYHqoNb6Im24xRrE2jKPluEVORG7wCDiQMYXZ6aG514sBDDuEChjzE5si1rFEGDZRj5idT0/H2czb8MlK6E0zgtfljapz0t7mz/sUX+us2cdO2CeQ1PEFvWY22oU+FlKLlYmT7GqCpK5vfRrmD7uh/aa9BwsXOQbHRUlvyItut+fNuXINEWD1nZn+oG7IuKaGnvFPET0ydmcPS7bi5Z1IXlhoRmcSiLzzBBSzoAZfK4dVuSxTzHMvfKsfz4v5LC3tov9oOh2etzNnCy6lUPUVFK/E2cdW978hr9ZwtkoWW0Qo0srX6uGo6+I2Wzm7CLIwpk8M9ftXu4tUZkNzG2x3dH7VZLuWG/XdUYvkmEuHItw6y6d0SyoEwO3J8+69VZ4HXnu1C2XQmxzK7agOGQG83TMcTcCW7mBMQ5eJyXjzA5lRhL4us4P1AFRV0XMG7IfHWrdsmFLGvXbdsPHirwctoTE6HVRhTudrg+hZbk7odTcQekLztKLc7gsaz3Dh43oZsSBvSzCUl8SZyS7UmsAgSxR4Wxet+JWWhsnzqkOTLs5ic0sP1/KNtfNa7w5o+isM+UaVk7pzE246KaYa+zmXOjdpk4K0mi1LDD9iFGiY+H7aLfN92jK4Dwu1k7NHCJxPAYyQfiuLGkwTLTCJULyBcb4m9NwQOJtX+Gk5XI10x3SJNlVR1JKd9WKA4F5FS+b8LS4BdagjMa2CrdtxFu3xaHkhNW+usZqHl01EuHcmFlS5NVMTWZBX/r9ziKUfLlHzVXNrrKG211F9tRekPp2bsbAAzEbaAlho2Vu8ehlqJIrH6nHXulKf+7kuYxurePJ5M0dEY831kts8qZlMhbKZike2nHQFUrNye2ZWbbHs9B47lwDO41msbWCi1atz260tbRofXGkmddYpUvajZt1TuGrmBY7IkZIuumqvCyo1wHzCJHY4xbO5WG0r/l47UWVL2HcTtC3J/nGn3CPibVVJdd9S252bQ8XKsU2cSnJ8PnQo8bG5byDji+rw9VSdKveRRTizs2NfBDXK3apo4u4OKTuWkmuyYCGqEvr6n6oV2mqkWrRgARLhvU2antRX4nheeBVmttc6/qUp+TIqCxTOhW/vmH1tVcdV0XKxNDcY8Lmxebo9B49A+idnVUs2UaBs2PSrbYNwwbDalJQpaOyXBmOcOvOeZnb66u/IpQQk2LUnwVsgFlNheqNotdjyFMKXMzTQ6LkB1xg+tDbnivR8JCzDLPm+uiTcwA8hjL3uHIPYCpKz0EsGZVubAQpMC0G7C350JwLkpaKDdNkrE6kdiyu9LUiR75wNPxkxYbri8CaRNDcduVpgZz19Q1hqEMF48syXrnNGq+s3WpV3rS1UsUL6pRSld3frjayoEZrHwR+h9yCGV7wR+mabJYnThQyKsjUNQH81uq2n1+qszVrTVR1nMvtrNICe/VWGex09tkpdqlwWa+Gziy6DXNYKrzK1AqlMPugN+IkD2Ek4iLlIphVfF4u/e5CwAVCXjcgPbrhepnXNTOmRhYdSO5GCmbN2aV7ubZadHCpkewSfuPNuZNzkN0tAD21DfXiZJdDfkIELxTY9Wk4LRKbHRV+u1siQ36ImC1XB7W74jOiCAf4phtMIu82uilx7oikuoLE4hGWvHlMDkiro/hyrt7csFvnfbMJZty2pxVpsFDEObJrnysaitwQaptsJW3bBzuhGtfHJRdtT9k1BB3VZUnuZvtuzqolKl31XUqcZU/jyn7Y2gllCzcBPh9rLcw1eSF6R1xzt8dOy1EtWV6OiTp3T1IscWckNeVepG+xPSJGSGGBV2rmKrhSJbo+eKtd78PVBY23qLgfFsihIa9HNzKWfC4318JvipLWT4o8CMLM8+TCv853nAdv8iLLA1deXHV8US2DsFWvUitH9rDRT5G6CZ1VhCWxolAAjNnhvFF47uyqh2ZLruUIxD7os4qZPccrU5FGNOua+ZJLsXGNCjfiKHjXpiPYblyQEr631wa3xdeYlmo2L6uRktRZuQrCw+KCAkJymMgHX2QO6yLBFUE5HTRS18SUb5PBarlrQ8Zj3y6ic5nsjprI4YJNWcbuXFbWIditb+dwkeK9U162hMVpQnri3cpudWF56mBD8jeIyFDDDhsNexZKXCvP6gXtcnxDuvZa18rDQW+KVEo2FEMy3q6dCWvxAgvbYFdo1KrrhYGFB4PM0FmycPFWuXK35WXPEurVSY/8bZT02Q3hPYY+Wk2dGGZiGd4YB1J/1nqF9EvTk9BiIzmm7hrtdpdeZuo2S2xivtlpR8IkjTRR9Fnfi/ISszbauh/TojHX3HkAZa2+CFc3M9NkTuXYLA6vjSaEzO3AtnWw363qWRN7hJDMBj08Lo7GWkHm4V6Q+OtmAHU/jztUF25ly7OihW5nhbpvN6uKKuSSXQyeUqZpP5+2o9eVBHucNlw32Ky7HoSDsZI93pihiibOSrugAoWSTvIKxbfiCo9zS/RlOmBYb4ns8PR0dPDgGpxwDZ31NyzCW9wlUWfYdV4Y5PBZp2h8RUdnbIAvlaBbBtdo9UmqEYI3xjnoe+tZtkL2vbIM2f6Kn/Cjc+iKA+3vFKPRjizrrtNC3c73hRhx5NAtnGw5k4T2QF55w6y0WS0r2qJXOHHZjth+N5YuNiMxKdCNkqHVI+3oB7L2xIAZujkmt5zTus4qMD3MaOag00ujWSMO51WQnPxbs2y7oRf3JI7DFK8twvOYmmYHDxosauqJ7TwXPlS3oKixPkesnDiFWxHRC295ItpdiTEOmZcs7VsLAy52/iYcZmV35oujul2WR4Qilspuv95vLHxZc8OwH884iXSyspXp2wY7z2XGlYzEyY8HH47YfNOk3C3URbet8FTcuecMFBAlYTcysVwUiBxsyw09X7Nz+Iq3IinRy4CmeX1Fx0cJDtbBksQM9LQ+wdQiJmVrHjKXG7p0cHg9ywh2iWyxbAvPyatUSqMfLzxhRpoRnBunazCrA48YpdsuncNMbIZgh7cEfdyKoKgm3992mBVTSoViIX/h9CY0cT5TKgo7lVQn0CfliuIheUDmA87dvAV88bpki/UHnRC8llZHK17AHKquD0Rk5VYcHOfotgPNLTHAMugiFxJzCLKaHWhlEPBBVhcnFh9zBlbDQNxuC3KxYZn9slKliERYYtQWaI2eiRQXMQAKTG9UnNNnUivxeTAc9qdLP1f4ZJvzsL7E1spyHzodvCV1jlsS2lnc9Sq/m3srzSnnGttFfVXhCFa0FdDPyoJgMN0hP1K9DWOnYO8sQOhk687BlJqkrqqVDfmWpLHQUaiQYoVonZwJKlivYUxKu2jWhijm4Lt5LeC2tBrFHaKjXZjTl1AWL3klztl8gK1GcVrmssOuC2Uh4GK15y2f2jKkJfv1dYdVJmF6bNWczoaDUCoeVI15Xl6uuMgNIo83S7G4+St2a/fMRm5jh99rccciw7pgRzfYaIiXHtczjfD3jBg7UneNAmRXqze7CljZXy8LD5sx7n5Jk04ThHyExreqK65zD8Xp4CAf4x7GA5EuT/COwdu8b4dxtmo6OgqpoOOXrNprfmdHQ4Mt9+3+dKZPXX/CydNZ2ZzoHneHDPScI7861iHVR0eOIQn7SpeUsl80iaUcG2thsQZ64wmODPjZZt+jymK+QAIeX9DKjg6LuK0cQtmdDoZfli2pnOc1GrUVnNuJdKXNQpNoPGUiZEvtC0Yo5jqX0Mc6ZhV8Jx8uOm7SlZumJ3NGYXrn5J5Gm5vjPNoYmcfSyT6ZeT1D7MRhoaO0yu1B6crYhOGraOXL1YGXLmw28Iavz+jM05D5dlhmphYeMJNS2nSp+jSoY8HeDWHRPByDJvBDOVjiMuIu5Q7gpxN3zhafYztN9bRLEFE5CR/PyeyIOrNDKgYndltdlFU6nuPBxiUY3TD6HgV1rSxzujmzIIBId3kLxfO4FeBmqepCFpP8SrmUPtL1/ICqZ0wsctcJiNtlniitQyCZh4MUl0ZKuYQBzPh65TQEugkZ5uXTy/2I+eUNRRYI+ellOnN4nhz8a6+aw1tcvj9p49QckP7fe8v5eOP4ce54P0rwbe/tzv3tXxH7H59eKjcGIj5eV9dpGz5fdf6nd72f//ob6Yne+DhXn45Qh+bjoKaxw/sr9Dj32rqpxve6SNv7C3TgnLae/vemfn8ebLzcFc/K5v7sq6Lgbjpndu26eW+K9+eRSpxPB4O+Fz9mTLfh8wTi04s3AjfHbv2Oz8l3vyon3Z9HYtNr4elM7OW3/wfABFeRcigAAA== -->
