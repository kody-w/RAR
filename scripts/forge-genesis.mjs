#!/usr/bin/env node
// RAR Card Chain — Genesis Forge
// Builds the initial blockchain: genesis block + forge blocks for all cards
// Howard's Binder gets the 13 HOLO cards, Kody's Binder gets the rest
// Output: docs/api/v1/ — served via GitHub Pages as the public chain

import { createHash } from 'crypto';
import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

const sha256 = (data) => createHash('sha256').update(data).digest('hex');

// ── Binder Addresses ──
// Deterministic from identity. When Howard/Kody visit RAR, their Third Space
// keypair links to these genesis Binder addresses via a claim transaction.
const HOWARD_BINDER = sha256('rar-binder:howard-hoy').slice(0, 40);
const KODY_BINDER = sha256('rar-binder:kody-wildfeuer').slice(0, 40);
const AUTHORITY_BINDER = sha256('rar-authority:genesis').slice(0, 40);

// ── HOLO Card Slugs (Howard's 13) ──
const HOLO_SLUGS = [
  'borg', 'anvil', 'personafactory', 'tinyworld', 'bridge',
  'telegram', 'contextmemory', 'managememory', 'prompttovideo',
  'demovideo', 'experiment', 'hackernews', 'holonaming'
];

// ── HOLO Card Metadata (for richer chain records) ──
const HOLO_META = {
  borg:            { title: 'The Assimilator', rarity: 'mythic' },
  anvil:           { title: 'The Enforcer', rarity: 'mythic' },
  personafactory:  { title: 'The Shapeshifter', rarity: 'rare' },
  tinyworld:       { title: 'The Architect', rarity: 'mythic' },
  bridge:          { title: 'The Connector', rarity: 'rare' },
  telegram:        { title: 'The Signal', rarity: 'rare' },
  contextmemory:   { title: 'The Archivist', rarity: 'rare' },
  managememory:    { title: 'The Librarian', rarity: 'rare' },
  prompttovideo:   { title: 'The Director', rarity: 'mythic' },
  demovideo:       { title: 'The Presenter', rarity: 'rare' },
  experiment:      { title: 'The Alchemist', rarity: 'rare' },
  hackernews:      { title: 'The Herald', rarity: 'rare' },
  holonaming:      { title: 'The Admiral', rarity: 'mythic' }
};

// ── Compute block hash ──
function computeBlockHash(block) {
  const { hash, ...data } = block;
  return sha256(JSON.stringify(data));
}

// ── Build Chain ──
const blocks = [];
const cardIndex = {}; // mintId -> block
const BASE_TIME = new Date('2026-04-04T00:00:00.000Z').getTime();

// Block 0: Genesis
const genesis = {
  index: 0,
  timestamp: new Date(BASE_TIME).toISOString(),
  prevHash: '0'.repeat(64),
  type: 'genesis',
  data: {
    chain: 'RAR Card Chain',
    version: '1.0.0',
    protocol: 'rar-chain/1.0',
    authority: AUTHORITY_BINDER,
    totalSupply: null, // uncapped — new agents can always be forged
    message: 'The first bond. The oldest love in the world. — The Architect'
  }
};
genesis.hash = computeBlockHash(genesis);
blocks.push(genesis);

let prevHash = genesis.hash;

// Blocks 1-13: Howard's HOLO cards
for (let i = 0; i < HOLO_SLUGS.length; i++) {
  const slug = HOLO_SLUGS[i];
  const meta = HOLO_META[slug] || { title: '', rarity: 'rare' };
  const mintId = `HOLO-${slug}-0001`;

  const block = {
    index: blocks.length,
    timestamp: new Date(BASE_TIME + blocks.length * 1000).toISOString(),
    prevHash,
    type: 'forge',
    data: {
      mintId,
      agentSlug: slug,
      agentName: `@borg/${slug}`,
      setId: 'HOLO',
      title: meta.title,
      owner: HOWARD_BINDER,
      edition: 1,
      maxEdition: 1, // true 1-of-1
      rarity: meta.rarity,
      forgedBy: AUTHORITY_BINDER,
      cardHash: sha256(`${mintId}:${slug}:HOLO:${HOWARD_BINDER}`),
      provenance: [
        { action: 'forge', by: AUTHORITY_BINDER, to: HOWARD_BINDER, timestamp: new Date(BASE_TIME + blocks.length * 1000).toISOString() }
      ]
    }
  };
  block.hash = computeBlockHash(block);
  blocks.push(block);
  cardIndex[mintId] = block;
  prevHash = block.hash;
}

// Blocks 14+: All registry agents → Kody's Binder
const registry = JSON.parse(readFileSync(join(ROOT, 'registry.json'), 'utf8'));

// Rarity from quality tier
const tierToRarity = {
  official: 'rare',
  verified: 'uncommon',
  community: 'common',
  frontier: 'mythic'
};

for (const agent of registry.agents) {
  const agentSlug = agent.name.split('/')[1] || agent.name;

  // Skip HOLO cards — already forged to Howard
  if (HOLO_SLUGS.includes(agentSlug)) continue;

  const safeName = agent.name.replace(/[^a-z0-9-]/gi, '-');
  const mintId = `CORE-${safeName}-0001`;
  const rarity = tierToRarity[agent.quality_tier] || 'common';

  const block = {
    index: blocks.length,
    timestamp: new Date(BASE_TIME + blocks.length * 1000).toISOString(),
    prevHash,
    type: 'forge',
    data: {
      mintId,
      agentSlug,
      agentName: agent.name,
      setId: 'CORE',
      title: agent.display_name || agentSlug,
      owner: KODY_BINDER,
      edition: 1,
      maxEdition: null, // open edition for CORE set
      rarity,
      forgedBy: AUTHORITY_BINDER,
      category: agent.category,
      version: agent.version,
      cardHash: sha256(`${mintId}:${agent.name}:CORE:${KODY_BINDER}`),
      provenance: [
        { action: 'forge', by: AUTHORITY_BINDER, to: KODY_BINDER, timestamp: new Date(BASE_TIME + blocks.length * 1000).toISOString() }
      ]
    }
  };
  block.hash = computeBlockHash(block);
  blocks.push(block);
  cardIndex[mintId] = block;
  prevHash = block.hash;
}

// ── Write Chain Files ──
const apiDir = join(ROOT, 'docs', 'api', 'v1');
mkdirSync(join(apiDir, 'cards'), { recursive: true });
mkdirSync(join(apiDir, 'binders'), { recursive: true });

// Chain state (lightweight summary)
const chainState = {
  protocol: 'rar-chain/1.0',
  chainHead: prevHash,
  chainLength: blocks.length,
  totalForged: blocks.length - 1,
  genesisHash: genesis.hash,
  genesisTimestamp: genesis.timestamp,
  lastBlockTimestamp: blocks[blocks.length - 1].timestamp,
  authority: AUTHORITY_BINDER,
  binders: {
    [HOWARD_BINDER]: { alias: 'Howard Hoy', cards: 13, role: 'genesis-holder' },
    [KODY_BINDER]: { alias: 'Kody Wildfeuer', cards: blocks.length - 14, role: 'genesis-holder' }
  },
  verification: {
    method: 'sha256-hash-chain',
    description: 'Each block hash = SHA-256 of block contents. prevHash links to prior block. Replay from genesis to verify integrity.'
  }
};
writeFileSync(join(apiDir, 'chain-state.json'), JSON.stringify(chainState, null, 2));

// Full chain (all blocks)
writeFileSync(join(apiDir, 'chain.json'), JSON.stringify(blocks, null, 2));

// Individual card files (for direct lookup)
for (const block of blocks) {
  if (block.type !== 'forge') continue;
  writeFileSync(
    join(apiDir, 'cards', `${block.data.mintId}.json`),
    JSON.stringify(block, null, 2)
  );
}

// Binder files (wallet card listings)
const howardCards = blocks.filter(b => b.type === 'forge' && b.data.owner === HOWARD_BINDER);
const kodyCards = blocks.filter(b => b.type === 'forge' && b.data.owner === KODY_BINDER);

writeFileSync(join(apiDir, 'binders', `${HOWARD_BINDER}.json`), JSON.stringify({
  address: HOWARD_BINDER,
  alias: 'Howard Hoy',
  role: 'genesis-holder',
  forgedAt: genesis.timestamp,
  cards: howardCards.map(b => ({
    mintId: b.data.mintId,
    agentName: b.data.agentName,
    title: b.data.title,
    setId: b.data.setId,
    rarity: b.data.rarity,
    edition: `${b.data.edition}/${b.data.maxEdition || '∞'}`,
    blockIndex: b.index,
    blockHash: b.hash,
    cardHash: b.data.cardHash
  })),
  totalCards: howardCards.length
}, null, 2));

writeFileSync(join(apiDir, 'binders', `${KODY_BINDER}.json`), JSON.stringify({
  address: KODY_BINDER,
  alias: 'Kody Wildfeuer',
  role: 'genesis-holder',
  forgedAt: genesis.timestamp,
  cards: kodyCards.map(b => ({
    mintId: b.data.mintId,
    agentName: b.data.agentName,
    title: b.data.title,
    setId: b.data.setId,
    rarity: b.data.rarity,
    edition: `${b.data.edition}/${b.data.maxEdition || '∞'}`,
    blockIndex: b.index,
    blockHash: b.hash,
    cardHash: b.data.cardHash
  })),
  totalCards: kodyCards.length
}, null, 2));

// Verification helper — index of all card mint IDs for fast lookup
const cardLookup = {};
for (const block of blocks) {
  if (block.type !== 'forge') continue;
  cardLookup[block.data.mintId] = {
    blockIndex: block.index,
    blockHash: block.hash,
    owner: block.data.owner,
    cardHash: block.data.cardHash
  };
}
writeFileSync(join(apiDir, 'card-index.json'), JSON.stringify(cardLookup, null, 2));

console.log('');
console.log('═══════════════════════════════════════════');
console.log('  RAR CARD CHAIN — GENESIS FORGE COMPLETE');
console.log('═══════════════════════════════════════════');
console.log('');
console.log(`  Chain length:    ${blocks.length} blocks`);
console.log(`  Genesis hash:    ${genesis.hash.slice(0, 16)}...`);
console.log(`  Chain head:      ${prevHash.slice(0, 16)}...`);
console.log(`  Total forged:    ${blocks.length - 1} cards`);
console.log('');
console.log(`  Howard's Binder: ${HOWARD_BINDER}`);
console.log(`    → ${howardCards.length} HOLO cards (1-of-1 mythic/rare)`);
console.log('');
console.log(`  Kody's Binder:   ${KODY_BINDER}`);
console.log(`    → ${kodyCards.length} CORE cards`);
console.log('');
console.log(`  Output: docs/api/v1/`);
console.log('═══════════════════════════════════════════');
