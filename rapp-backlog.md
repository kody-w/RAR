# rapp-backlog — RAR

Registry hygiene. Public repo: nothing here should reference private estate internals.

## The finding that opened this file

**An uncarded agent is a capability the registry owns and cannot find.**
`@kody-w/copilot_studio_parity_deploy` — 7,027 lines, self-contained, the piece that turns
any local RAPP agent.py into a provisioned, parity-tested Copilot Studio Draft — sat here
with **no card**. Two people went looking for exactly that capability on 2026-08-26 and both
built smaller, worse versions of things this registry already had, because search could not
see it. That is its own kind of drift, and the fix is a card, never a rewrite.

## Open

- [ ] **Audit every agent for a missing card.** One pass: any `*_agent.py` without a
      matching `*.card.json` is invisible to the index. Report the count before fixing it.

- [ ] **Cards should carry `companions`.** The Copilot Studio family (forge → parity-deploy
      → factory → provenance) only makes sense as a chain, and nothing in the registry says
      so. A card that names its companions turns four agents into one workflow.

- [ ] **`learn_new_agent` generates from scratch.** It should prefer **mutating a published
      template** over conjuring a new agent each time — inherit something verified and adapt
      it. Reference implementation:
      `kody-w/rappterbook-agent/blob/main/python/openrappter/agents/learn_new_agent.py`

- [ ] **No agent declares which spec revision it was written against.** When the protocol
      moves, nothing here can say what is stale. Cards could carry the anchor hash.

## Standing rules

- **Publish nothing with PII.** No personal names beyond authorship, no host names, no user
  paths, no customer content, no incident specifics. Audit on every version bump, not just
  the first publish.
- **Verify functionally before publishing, not just that it parses.** A leave-behind that
  fails on someone else's machine is worse than none.
- **`quality_tier` means something.** `official` is a claim about exercise, not intent.
