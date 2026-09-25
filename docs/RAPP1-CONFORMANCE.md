# RAPP/1 conformance notes for RAR

RAR is checked against RAPP/1 by the reference conformance checker in
[kody-w/rapp-1](https://github.com/kody-w/rapp-1), `rapp_check.py`, at the
estate pin `591e014ad39e223b00ab343ae26e5d9a867ebeee`. This page records what
that checker needs from RAR and how to reproduce every claim with public tools
only.

## Run the checker

```bash
git clone https://github.com/kody-w/rapp-1
git -C rapp-1 checkout 591e014ad39e223b00ab343ae26e5d9a867ebeee
git clone https://github.com/kody-w/RAR
python3 -B rapp-1/rapp_check.py RAR --json    # "verdict": "COMPLIANT"
```

`-B` keeps Python from writing bytecode into either checkout. The checker
reports `DRIFT` for a violation *and* whenever it cannot finish looking, so both
sections below matter.

## The bounded scan

The checker walks the checkout with fixed bounds: it never enters `.git` or a
symlinked directory, stops after 10,000 directories, 100,000 entries or depth
32, and then reads every regular `*.json` file of at most 1 MiB, except
`rappid.json`, `rapp-frame-index.json`, files a frame index lists and numeric
`frames/<n>.json`, looking for RAPP/1 frames. It stops after 10,000 such files
or 64 MiB and reports `verification unavailable: bounded frame discovery JSON
budget exhausted`, which is a `DRIFT` verdict whatever the files contain. RAR
went over that bound, with more than 16,000 such files, over half of them loose
Rappterpedia stream deltas (16,166 and 8,930 at `db3fd2665`).

`scripts/check_rapp_scan_budget.py` restates those rules (it never imports
rapp-1) and fails at 90% of every bound, while the checker still has room.
Two workflows run it on the whole tree, and no other workflow does:

- **Test Suite** (`.github/workflows/test.yml`), job `rapp-scan-budget`, on
  every pull request to `main`, every push to `main` and every manual run. It
  is a job of its own that no other job needs, so a red budget never skips the
  rest of the suite.
- **Nightly Health Check** (`.github/workflows/nightly.yml`), step `RAPP/1
  bounded-scan budget`, daily at 06:00 UTC, because the commits that bots push
  to `main` never start the Test Suite. It runs last and even after an earlier
  step failed. A failure opens the nightly failure issue with the budget
  summary in it; a passing summary goes only to the job log, so it never
  crowds another step's failure out of the issue.

`tests/test_rapp_scan_budget.py` pins the script's rules on synthetic trees and
never reads RAR's own count. The workflows that run the unit tests as a gate
before they commit (agent approval in `approve-agent.yml` and
`approve-agent-batch.yml`, the estate rebuild in `aggregate.yml`, and
`release.yml`) are therefore never stopped by a growing tree, and RAR's front
door stays open.

```bash
python scripts/check_rapp_scan_budget.py          # summary, exit 1 near a bound
python scripts/check_rapp_scan_budget.py --json
RAPP1_CHECKOUT=../rapp-1 pytest tests/test_rapp_scan_budget.py   # also compares the rules with the checker's own
```

When the check trips, the checker can still finish: it gives up only at the
full bound, and the last 10% is the time to act. The failing job prints every
bound with its value and the largest discovery populations. Shrink the largest
bot-grown population through whatever owns it, keeping every record, the way
`dream_catcher.py` now folds the Rappterpedia stream deltas (below):

- change `scripts/build_scout_exports.py` for anything under `scout/`, and
  regenerate it;
- leave `state/receipts` to the owner. It is canonical notarized state: only
  the notarization tooling writes it (`scripts/apply_agent_mutation.py` for the
  Issue pipeline, `scripts/mint_maintainer_receipts.py` for maintainer
  migrations), and Notary Policy rejects any pull request that touches it.

Then confirm with the checker itself. Renaming files to a non-`.json`
extension, pushing them over 1 MiB or listing them in a frame index only hides
them from the checker.

## Rappterpedia delta bundles

Each Dream Catcher stream still writes a loose delta,
`rappterpedia/stream_deltas/frame-<N>-<stream>.json`. Once frame N has merged,
`merge` folds every loose delta at or below the merged frame into
`rappterpedia/stream_deltas/bundles/frames-<first>-<last>.json`, one file per
100 frames (a full window continues in `...-part2.json`, and so on). A bundle
holds each delta as its original JSON value, keyed by its original file name,
plus the SHA-256 of the original file bytes, and never exceeds 768 KiB, so the
checker still reads every bundle.

Nothing is lost: each original file's bytes are `json.dumps(delta, indent=2)`,
and a loose file is removed only after the bundle written to disk reproduces
those bytes and their SHA-256. A delta that cannot be reproduced byte for byte,
or that carries a top-level `spec`, stays loose, as do the five one-off
`frame-101-review-*` deltas named in `HELD_LOOSE` in `dream_catcher.py`: their
text quotes local tool output that folding would copy into a new file, so they
stay exactly as they are until their owner reviews them. To redact one, the
owner edits the file in place or deletes it, then drops its name from
`HELD_LOOSE`. An edited delta folds on the next merge if it is still in the
generator's format (`json.dumps(delta, indent=2)`, no trailing newline);
otherwise it just stays loose. Folding is idempotent, so any loose delta that
an older heartbeat committed to `main` folds on the next merge.

No writer overwrites a delta. `produce`, `cycle` and `refill` write
`frame-<N>-<stream>.json` only if no loose or bundled delta has that name, and
otherwise the next free `frame-<N>-<stream> 2.json`, `... 3.json` and so on (the
form the file-sync copies already have). The heartbeat's fleet workers produce
into an empty `delta-out/`, and its merge job copies their deltas in with
`collect`, which skips a delta already there byte for byte and gives a
differing delta of a taken name the next free name. So a delta committed before
its frame ran survives, and merges, beside the new one. `extract` never
overwrites a file either, and refuses to write into `stream_deltas/`.

A heartbeat run that is still in flight when another commit lands on `main`
does not land at all. Its jobs check out the commit the run started from, and
the merge job ends with a plain `git push`, which is then rejected as
non-fast-forward. That run's deltas never reach `main`, `tick_count` does not
advance, and the next run produces and merges the same frame again. This race
predates the bundles, and it loses nothing that reached `main`.

```bash
python rappterpedia/dream_catcher.py fold                 # fold merged loose deltas now
python rappterpedia/dream_catcher.py extract --out DIR    # write every bundled delta back out
python rappterpedia/dream_catcher.py collect --from DIR   # copy deltas in, never overwriting one
```

`tests/test_dream_catcher_bundles.py` proves the round trip on synthetic
deltas and proves that a merge reads bundled deltas exactly as it read loose
ones. On a full-history checkout it also re-reads from git every delta file
ever removed from `stream_deltas/`, and checks that its bundle reproduces those
exact bytes. The only exemption is a delta that `HELD_LOOSE` has named in any
committed revision of `dream_catcher.py`. A held delta is never folded, so
removing one can only be its owner redacting it, whether the name is dropped
before, with or after the removal.

## Stack eggs

`stacks/microsoft-365-team/microsoft-365-team.egg` and
`stacks/neighborhood-starter/neighborhood-starter.egg` are unsigned `rapp/1-egg`
organisms. Their §9 re-pack (commit `aa78b5a4e`) left the ZIP UTF-8 name flag
(general-purpose bit 11) clear in every local and central header, which §9
rejects. They were re-framed with rapp-1's own `rapp.pack_egg`, from each egg's
own manifest values and member bytes: the manifest is value-equal, every member
is byte-identical, the §9.1 egg address is unchanged, the length is unchanged,
and the only changed bytes are the flag fields (66 and 64 bytes, `0x00` to
`0x08`, two per entry). `pack.json` records the new sizes and SHA-256 values.

rapp-1's `egg_repack.py` was not used: it converts legacy eggs, and re-running
it on an egg that is already `rapp/1-egg` re-mints it. On these two it drops
`payload._migrated_from`, so the manifest and the address change.

To re-derive the committed bytes, run this from a RAR checkout with rapp-1 at
the pin cloned next to it:

```python
import io, json, subprocess, sys, zipfile

sys.dont_write_bytecode = True
sys.path.insert(0, "../rapp-1")
import rapp

for egg in ("stacks/microsoft-365-team/microsoft-365-team.egg",
            "stacks/neighborhood-starter/neighborhood-starter.egg"):
    before = subprocess.run(["git", "show", f"aa78b5a4e:{egg}"],
                            capture_output=True, check=True).stdout
    with zipfile.ZipFile(io.BytesIO(before)) as z:
        manifest = json.loads(z.read("manifest.json"))
        files = {name: z.read(name) for name in z.namelist()[1:]}
    rebuilt = rapp.pack_egg(manifest["variant"], manifest["rappid"], manifest["created_utc"],
                            files, manifest["payload"], manifest["sig"])
    committed = open(egg, "rb").read()
    assert rebuilt == committed
    assert rapp.egg_address(rapp.read_egg(committed)[0]) == rapp.egg_address(manifest)
    changed = [i for i in range(len(before)) if before[i] != committed[i]]
    assert len(before) == len(committed)
    assert all(before[i] == 0x00 and committed[i] == 0x08 for i in changed)
    print(egg, rapp.egg_address(manifest), len(changed), rapp.verify_egg(committed))
```

`tests/test_stack_eggs.py` keeps the receipts true and the framing intact
(`RAPP1_CHECKOUT=../rapp-1` adds the full `rapp.verify_egg`).
