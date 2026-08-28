---
name: "rar-cowork-cookbook-bulk-update-receive-service-requests"
description: "Applies a bulk field update across receive service requests records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_receive_service_requests", "rar_sha256": "ca6c0578cfb0cab88c5d907e7df1b7f4bdae096ba48d051c3af23f1805afd1e3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_receive_service_requests`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_receive_service_requests_agent.py` and in the RCI capsule.

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

Receive service requests Bulk Field Update — Applies a bulk field update across receive service requests records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-service-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_receive_service_requests_agent.py` and embedded as the fenced Python below (sha256 ca6c0578cfb0cab8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_receive_service_requests_agent.py` first:

```bash
python3 bulk_update_receive_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_receive_service_requests_agent.py   # or on stdin
python3 bulk_update_receive_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive service requests Bulk Field Update — Applies a bulk field update across receive service requests records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_receive_service_requests',
    "version": '2.0.0',
    "display_name": 'Receive service requests Bulk Field Update',
    "description": 'Applies a bulk field update across receive service requests records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-receive-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-receive-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5f6f147a39f422d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/receive-service-requests'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-receive-service-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateReceiveServiceRequests(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReceiveServiceRequests'
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
    print(BulkUpdateReceiveServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxpbvV2Fq/uj2qLpZhVDfcMRjk0ACgUCgxe1osySL2Dch5Ofv/hJJVW2Pr2euJybiqbuqgMw8+/mdk4l+fXG6Nirqly8vJnByZOmkaRyBGnFyH+GLvqgT+KdIXPiDeEXe1rHbtUXdvLy++KDx6rhs4yKHy9myTGPQIA7idmmCBDFIfaQrfacFiOPVRdMgNfBAfAFIA+pL7AF4X3Wgae8DRe03SFAXGeSMxHnZtUgaN+0r0sdthPj18KnucqSswSUGPeKCoKgBFCjL4vYzlAVcnaxMQfPy5aefX19ieP3y5dcXL3Ua+OiFgxJZd1GMhwjmQwLjKQAkkDp5CGeWA7RGDu9LUEMWGXzkgwB53n1sQBq8Iv/xH0nv1GHzw5evOfL8fH0Z/xlQxjYCSFs4TQt8xHNKx43TuB0+I2zaO8Ooa9vV+WinBhozDz8/Vn6nVJTIj+PYxweTzyFoP359KaAIzmjqry8/IEUN+UF7wOvPI5Xy4w+f06IH9ccfvtNpOvcMvHYkBqX+/O15/yQLJ36fGgd3rj9Cqg+nuuDry++UGz8PuUc94cqXz+cizj8+CJd1cQG5k3vg4w9/RdaLgJeMDv2X6P70IBwBx4c6PQX/4fVu5J+RyVOhd5p/zbaEbv07msDpb+xekaeh/or23f7/iXQa5zAF3iz+T8n9swWTH5Gf/lK3/2rBKxJ8fRFACkO6dtwUfEF+/WbqIv/TB//7ww8//wZJ/7dkzKKrvTuFb5mTxwFMjG/ffvrQ3B9/+PmnD10JYw042beuTv8ZzX9m1zufP1jwOevjH9dC/lae5EWfI++RjvxalP9W//YZsZ009r8/b74gv8+X8TNBRiXemD5M8LucaaCsv7PjDy+/QYzIoTaddx+GWf7v/46o8QhTRdAipldA/IEObuMMjMLvorhB4P8xtyEEgbqJoWGf82D8jx4eJS4C5Jf/491h85P3hE10xMNvDyT89oTAb08I/PYGgb98RnaQdlHHYZw7KWKwuv41d0KQtyNfiHvjCogo7tCCTxCLPo0XECiRX/4V8t/ulD6Xwy93YI8fKGXw8ohQTZeCz6OW+wjkT508iMLgCrwOMkkLD0oUxBBeX6H2TZFCDG9HizRJnKaIH0O2sCYMd9rQal9GYr/88ovrNNHX/AGpJPIoFg0KJ7yLg3z6BFUL0jiM2q858KIC+fDrbx+Q/4v8V6vuxEceOoT3p0+ghCtT2yAwx7oMToPugg6GAHL3ya+/PQ0MyeSwukEPxsFYrcbFMEYT4L9Z25TYT8SUfisxsJQUdQtxGoGFBpED5F1eyHQcGpE8KpoW8UEJch/k3gCpOlCdd0vmRYs0MBCbYHhFugbcuf7i1s5dxAwmu9P+gqi8DutGkcJfo5j3SXBxkcfQ/O+x8HgOidQfGoR7I/EZ2YxRiZRO7ZRR7Tx5BM7DL7BevC2HxB0kB/3XfCySYDTVPUUe5oGToGW8p0s/jT6/F1no2OaN932OM1a33b3K1V/z5hn+Tg3utRyKMiBhF/tjUfjHM6SaqOhgSzDaD0o6Unp6wX965R6Dxl/1CGMNRxb3ruJRypGvHYHhFPL/sfEYBWaXS0NcsjtRQMTNzjg+DDm2SqPBH90VrP8IXPdImu89wRuivAHr1zyNYVTUwz8eM+/mf855gFVXQ2sZrHGnD30PDTnSvYfmGGp1fbfE1/wNwV+hWe5wBb0D8xjG+RhebwzH0TdJI5is4/33av60zpjVMPyQsnNTGBoBAL7reAmUqh7T6+kFGKdgTLU+ir3oD1ohkDoMB0gfgULE0OoQ5e+m2xRQTZhZd+u/T49Ht0Ap/M6D0sJeFHxG9jBDxihpoANgozPOgVb4cCeFZADaGIr4buEmcsqHMGP7+hTQGX1RZGNU/M4Dz8HvMX2XZRQfUnVgDEFb9iPO+uD68Oy7nE9fQWGzMQvvi/7o7qeuyO9LzT++5ncZ36EdJnc6VunfGQeBSZU1dzQdsamB+JKBZwDBSLgX5M+Pmvoo2u+yfPlTz/7x77X19ypp/dFzX5CobcvmC4o+KttbYfsMswCFMRKXoLkXuU+PrPv0TLdPz3T79JZuf6D9MNUX5O/J9wcSz8D+guCfsc/YOKRAdmPkPj/QHPwn7viJGkdHbPnu52cwjNiaDrCqvheatymw2oQ1CMfJj8LTjPWqhyXyjrTQE1/z91h4ZgoE8jwcq2RT/C6D7xUXevbhuPeCAIfyFvL2xz4tBOMuJh3Fb8DLl7xL09eX3MnAv7Z7GXEfBiy0x7jtgckDO582Bve79y5ovPnjnu2eVhAP/OLLmF2vyNixviLvzecr8rYduO+x8g7uh34aG9+RJZwK/7zPfd8QuuAFbsHaoRxlf+xxxn7r2Qf/WYgxqaDEHhhrefGepSPHPxGBF2EI6j8T0e4XTvqEiqZ1xsoct28J3kA5fdjnvCLQezDxYC5BiOzggj+zgXzGiIUl0B/V/W6/72oVD11+u5uhfWwUf315g4ynD55NIZwOc/NTMxZBFEYqZAjvHzEFx/5H7eKTBgQ62KpAIp5De9h0xniBi3mOyzDe1J9jMzDzA9ydBZTrOwCb065DMT42xT3SCQgywBls6gQ+DkhI7xGd3x6VDZIkHMdjvBlO+fMZpA5IzCU9gBO4PyMBNp2TAcMACprofWkCUfKp7EO50ZLvnetolKfOv764NAVnSlQjs48Pj85thyYVdxO5k5oO2OY8T9pZgdF7m0wDW5P8YHWqTiuVdOj8SNfUUU5W62XGr45hvQ/nMGOEOZvPVnrnsygbm7ljzrpbs1mphBiKnrS6Kf6MEtZhzPfH/Tp1p0Zf1bHR+OuFVudmm5tx5dsgJoBzsjKqbpjEscwLSg7V7bxh8G29pk3ZkW4cNbXclFxEtbwXwWDEPWeuFscLX8sHNVJnQxWZZdvZsiuZUzHJrpLh26vLiif3MS6eFk4mrlfE+nboyl7lqkDP8Ymn3+ZzD6VxTULxabeW4kN8K7plYy+S8rTYd7u1pNQeW1kOjS1cST05xg4Up8vKPB06E1NWPhBsESwU5aSTqrnYpdacM7SqW/fr9BgrWN/sFXKf8dFR0T1TEYu1EjZYv1dbVblu/e2xcG07atVy6Uy4qjbnm8agNTyP29JGt3OFGTZDtluuYkXpeXfFqpN6vdlf93xsG8J6EiX0NlEEXJ2q5dE4xc1cuTqdx7DlWlG8ZG+JgkBkzq7fmxdBpQ/KidxkDMxBWZonQ7WEfOxKzqkgthUWtG4mYPhyWglUPz8li7AmhONpIzv4eprMdtb1enPKVVPPT/ASq0XqbPaHM3XI45TnW9mi4pNmhCzd5vGhrvVNXkynmLDyvf5y0JU6v8x5V3K6bZu1GLOsV62XlIfThEgq+RYT7TEsbHdJnJbnJrFxt9mt6ilQF/nZt0WzPe6OkYK2YaFGmzwq5vSpueKRjoqYY/O8gEowMogjlc/XYNdvE683iaUuB9rsYKOb67povFvn7rINWOotLjK72YJbRh6xz9OlfU7x+TnHI/hzPmv1ki5Kwj51itBq7ZoRRUakmCzHqMnVC0lC7nhcn3Brb7bckcwxoKZcIQb1AczR3d4N4iys3cWtuCi7HUjg1oJpeWWfDoNIDwk5KHv12G9iSxdWhcxwiVETJmFLRxEnt2Z6nApCfpiE5eR2W+34YxzWzcHi5autTASRvYQk34gzQ+W2OZWf2KiPmou4aridaiwERb/SN23Be5qRUUxCdAsMLA63c3AmznmTbNjpSt9qvIsLfVtE2wEVs6mS6PzpjDfMzg02ltts6AQNJEp0eK9xcewy0avFtZ6yaz3Vsx5bXw4puSqboKx4YShEdudiqworQlUzCPloG8etu8RkTK6vyo0UrqQNulZarlAT9xO/7BMzXbA3zF4CazLURhCd5odBbtDtbLVoZ9tmi6ETdK1Y3GHqaZQd3xaocyxaySFuZSoxU6wwcXmf2vmVaZLOpqxkHppDyxO2kPrklgdgI5DqYqbCOizTgMPnxhrGqXM4NEys99aNMetp66iGhDKFlewEwyzQ/kDKmLcOZJ7osL0GUHc1vZ4HLry4LH4y15nfpwCLj71/zbTEIPsNZq/zXXayHG9rJcK2nLPKglhaxmrgLR/PU7ZarLzzFbVwo8JlejpxFlq+XhBq1lE6jWpnfMZIq+i0MNNNwHLbjmqrCbUl6pODzXJ8O6941p+gM9niJp7caLFwq0I20s0wc2p3YwheIV2TbMnFoceIMW+G/SHpO2m+H9jKKOi9rFTCfs6lq8GPHQ/llzfeMQg3Wur59NiQIn1a+26eJWeK2LuVL4OSrWT2sOjMdM9vbLTATcv30UW8Ubj+SK1YK5VrSzP8zpo5jqUNK1Ptkz5NjtbxZHFeY2XkVTl7x+NBiK2wtFj5hGXVTN6Zlx1VS8K50SR2JdsH8VxrbOPYUgPy0znTcmtfxesTjk8aQmnQzSGdeIlY3NZ7mbi5+SSwVytjqL1MnTRzfuvxcU/NYZOgB/WabdxOO5I+F8ZKEjP7Q4yBAMXTybwNFlOKCVYkeg2BfOC2ZMc0Fbk6eqLKlkS5NJebZp44kc2VNtX4iyENlfNJr+hMLPeEUIfbPTTTes7tz+uhTsreSbqTIFEZ6wEzLNNkw8Hs7fcaf2SDIdL96Li9DeGkFPKdmS79oNC7uVoK5XC7XSmF1bpNlkqrkgQZ1d78OF9Yi/gQamJnszcXpgMxnRolRNrdZZY09s3AtiuU7Pud3NS8c/FPpZmAmeSd+nSR6N3JkWWz3zHHXIcQVPmeU7iHEtemhnpus0kjdfKxXIZiaXtNcq4jHO8319VMPt9mR3NZHMDEVGWgFttOzsQ2dzhRSsHhFNkDdPt1chUxNluIq7BeEhFauVahHMMd4BfcnpBUT940QXZ0rrHZh1e2mVmRSVfY2uTW0YpUbXdzUHOB7LHIoEums8wpFu2m4nJLFnzPCdTGjiMvTm1rX896JlJKbuGVOF+X073trDbZymmmXdnJA6czkuwTYJLNh2Ynlq7Jb4vNhTc7pd9NCGI2YOdVEmUep6TxCW1uFhnw0nLqZZQrXs02CK/tTD20dLXPqv1py8+zOeabhVm6iSuwx63Wafj5Ik9XLR1J1vri4RqsYslcq6ycpQ7bIblcxQg/Vy230886i120eLu+cDAezkS4v3FFaLYGF1XiUu4vglzlW46jl835Wod6NsuxaOKolXiitBq7odMwRMPcNZjpUjmH6y255YbpBaYpOE1S1YlbPVNTgUTR81wmUC5jt6Yv0Nv5wKGtR8ZhrOXBlMSX6bUYiH2Q223S4ZRKWBfYB+R92xJ17+1pWTRkmvPreT1jE1EWOCusN6DwsLZND/JAcEys7pb7AkQbrpNSGlVvTq4tm5CXKnJZzhqstKe5ox17xsBrflkd1rQb0taBZzqs5cx8Hy8mQ5Dl9NTiE3zq2MrGpJMbxgZHgRdnGNycKew1C7Ncpo+7xNQ6M6hkzpx5NrudTiuQmemZXR8sUzutDRf2MEKRZ7tJ1ZYdLe5vBMZU5s0LLzJUah1MRLWfb1bXI46R2/7oW/WcXimyqSXqaqdvfW2pXGWDEyP1kMECud+erTiuXJY40tICbvZUI7sJl2oanVzPVpPspvOMeNnOrqLvN0M21zyr20oKsVFO0TGRcTwzcQ+2ZA0FN1iLgzZPdNq6bnO6oyeDQG53jXQ5r2pJ7DZL1LuR/GI5tJaw92K8uhJEnE9Nz8ql48zAsS7rqoIyyCYL4uo0Hwgi2+mYLXr8bC1np846i2VkCjIlAqlYCpy0oHd0hBXCMCTeWnYIwMV23+Us6ck2359oHJe2qXPLa3+5I2J70SWnRs3lRJvNjaAPNsk09hvg7esCK9bNhU8x08p4fXHa9PKEnebiGlYWu9T24VqN0NNB0UrqtCnKc5EJa6WVYsNScdeVMq7F+d26ADHgV1ozI7eD1e+0yRltuPRGTdeXMt8uOeomd8Jaq8i9LWZSfLHRtTNY8jwn6E2dr/1BN0/7vV/uaIrST6ZMbQvNiT3DNmWX3Q+rTHAW/mRKCUuQWPM5yLGNEW7AZX5W6Ft1OhH0RTSsMuNEcGAyLJcj5ZLPy8Wlpss5HQ8zG2N6VukoQ08KtaQcxrBmWtLd0oVNm9pa4iEao6vlbr/yNgtpRTFrjyaGZbU7HndROPM4OTn6u2bpLiYqVlnqsD3b2k4xCd8/o4HB2ofytmUPBa/ZlxxwS19SZ5PbdiOn/Ik9U1G1dSOCmYhbBXNBgUu6EFTFRtpp6+USKoCbcbDDFjq5I/ULvaQ3a6PvL7pwRJ2w62qHY8XWuB4I0d+Yzu3iz+vJZeHZK/Lq+zWX+USJtTdKJ+lD6ElcMHVnfgUuuG8350DZzkil6Wl8Vh4Apt0uTe0PszUIm9kRxfHzKlyv9ykJN82OZ1aNL7UFoeacIzFLUibUtU+mtwxTSEs/2DfbTSbMac+Jh/iUGpI8kTlNRwWH1w2WzCWFqqr5MbBDrpI6rmCTzW0PIRCXsl7VroqTXRZ5tQv2t0ZzJdghqe7EicmInunLPsdzP3VBu12cjkFtMPttfkvJZrZ1a8bjbvN2PkG3cLfjrcxa2U3oKxq7A9y9+t5cnKGgWE2GHPRZmDebq6grPrejOhAVbE1ZZTjpWLDRaZ6MCzUALmE44k5hHcvXJuxudx6EIdv0Lqd6OybzJ74y3HY86g1tBuJ+Sdqn5RSzpAu1nXr1yVCpBUcq1Xxq3NLl0VbU84kd4gl3Wat78raKLyBn5xe6nUXa7rI9wPiw2cuxGwA5SD3wU98eFuj5sA7K3cIK1xNQyB56kggyPKrRkrnmwUE32pW6w4KoIMk1dmGoau6i+Pl2WRraCUtJTBww1iKOWk72Bynwu+nEwG7iwW1BR7DNMdSbNUap1zYAA6rPKbKatlbH6PIyBxqVuZfcc1smzDCev7C3liz2N9XKqawwYGFURLhloddEuriJAanojO/jyrbhOc286iRGispBrBQc6LrSCf6SZRgqOUt9rQJ20VKplPdCuLqg5ZDW54umX1jgcKFyVA5XIWOqlRpUGIMGwZVSy4wS8K0kN7jVzpvcI5Ntv11EmxDo3CKbbRgx0w0yQ20uQt1mZduA1OPDlaEnPDaNunUQb7qsHbQZPRPzzXUJw+UKPeXdNGHi9m6qknV6JmmL2co1jgHKn/A3PRB8l6uTeef7ntp5piRqbl3uAu4Au8DZLMrqGSOQq5szj46XsJZw9zbznIY5nWdbjE/Zlh6omTOv0xOmZYWP293O18Gsw51kvyy8abDwJBMXJ+cNJYt93YtFt2YDdSO4NOqKMSusr0yqG5kvnU/CmWLEmZgdAptHi8vRybGMlvbMVtjW7fxw3AuzgXQDwKDO9ISTgzzv1tNJZc5pBizBbEBb5zrbDtd0svY2h0PdoGdNdBdZ6cN9oj4s5x65JA8iMR38CwbQlYdipzM2PWBKiy6cyTlbJpw0nM/sAjvy+bWqiUtzQzVtE9oadjYSHe557EBoJwcqnAsYxvZrK5ofghtFzQg+Xjjt5eJRvmZPs2yW4Hl12y/pZHKotlp9dSI1J4HFS9tbMwlZ51xuzR2+HGSV9KiW3+x8l2iHve27s8vJhP7AdfxYShVsrU+YThwnuynJCiEVSNfdAZcNcthdVIlllQMvMgdYmm6atInXFVPOp6qTl9i04lT1wkdNSrjzNZ8APFd6V2V6Sdz3ftCe956CbvDakgUFFcXVrPTN5kYR3WHrQ1SN3Avdc3Y6ueKnSZ+KgaTo9XnDp7EdXR1URhcmZ6FTs9y1de63rpAvqSnDDWFu3GDmt1x8XGbZleX9Sw0h6LqI5sZpKVU5c2S6czud7kiVqXYaTYBcnPrulRLmZ3HrHCIzYVn2xx9fXl/GQ+nn0fLfenc8nvT9rx04Ps4G31413Y+VgeN/ufP68vfE+vn1pfZiKNTjcLVJu/B5DPmfjlY//SsvKUYKw+O17Phm7Nq+nca3Tjh+veglzv2uaevhW1Ok3f2A9xXasRm/6NB8ex5kv9yVy8r2PvauzEj7qUZbfHt+ReNl/C7C+MYHwA3yfc54Gz7PnF9f/AE6K/aabyQ9/QbqctT3+eZjPKYdX328/Pb/AK/YH9XIJQAA -->
