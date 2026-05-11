#!/usr/bin/env node
// RAR Card Chain — Genesis Forge
// Builds the initial blockchain: genesis block + forge blocks for all cards
// Howard's Identity gets the 13 HOLO cards, Kody's Identity gets the rest
// Output: docs/api/v1/ — served via GitHub Pages as the public chain

import { createHash } from 'crypto';
import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

const sha256 = (data) => createHash('sha256').update(data).digest('hex');

// ── Identity Addresses ──
// Deterministic from identity. When Howard/Kody visit RAR, their Third Space
// keypair links to these genesis Identity addresses via a claim transaction.
const HOWARD_IDENTITY = sha256('rar-identity:howard-hoy').slice(0, 40);
const KODY_IDENTITY = sha256('rar-identity:kody-wildfeuer').slice(0, 40);
const AUTHORITY_IDENTITY = sha256('rar-authority:genesis').slice(0, 40);

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
    authority: AUTHORITY_IDENTITY,
    architect: KODY_IDENTITY,
    consensus: { model: '3-of-5', threshold: 0.6 },
    totalSupply: null, // uncapped — new agents can always be forged
    message: 'The first bond. The oldest love in the world. — The Architect'
  }
};
genesis.hash = computeBlockHash(genesis);
blocks.push(genesis);

let prevHash = genesis.hash;

// Block 1: The First Card — forged before all others
const firstCard = {
  index: blocks.length,
  timestamp: new Date(BASE_TIME + blocks.length * 1000).toISOString(),
  prevHash,
  type: 'forge',
  data: {
    mintId: 'GENESIS-0000',
    agentSlug: 'architect',
    agentName: '@rar/architect',
    setId: 'GENESIS',
    title: 'The First Voice',
    owner: KODY_IDENTITY,
    edition: 1,
    maxEdition: 1,
    rarity: 'genesis',
    forgedBy: AUTHORITY_IDENTITY,
    cardHash: sha256(`GENESIS-0000:architect:GENESIS:${KODY_IDENTITY}`),
    flags: ['succession', 'transfer', 'rotation'],
    provenance: [
      { action: 'forge', by: AUTHORITY_IDENTITY, to: KODY_IDENTITY, timestamp: new Date(BASE_TIME + blocks.length * 1000).toISOString() }
    ]
  }
};
firstCard.hash = computeBlockHash(firstCard);
blocks.push(firstCard);
cardIndex['GENESIS-0000'] = firstCard;
prevHash = firstCard.hash;

// Blocks 2-14: Howard's HOLO cards
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
      owner: HOWARD_IDENTITY,
      edition: 1,
      maxEdition: 1, // true 1-of-1
      rarity: meta.rarity,
      forgedBy: AUTHORITY_IDENTITY,
      cardHash: sha256(`${mintId}:${slug}:HOLO:${HOWARD_IDENTITY}`),
      provenance: [
        { action: 'forge', by: AUTHORITY_IDENTITY, to: HOWARD_IDENTITY, timestamp: new Date(BASE_TIME + blocks.length * 1000).toISOString() }
      ]
    }
  };
  block.hash = computeBlockHash(block);
  blocks.push(block);
  cardIndex[mintId] = block;
  prevHash = block.hash;
}

// Blocks 14+: All registry agents → Kody's Identity
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
      owner: KODY_IDENTITY,
      edition: 1,
      maxEdition: null, // open edition for CORE set
      rarity,
      forgedBy: AUTHORITY_IDENTITY,
      category: agent.category,
      version: agent.version,
      cardHash: sha256(`${mintId}:${agent.name}:CORE:${KODY_IDENTITY}`),
      provenance: [
        { action: 'forge', by: AUTHORITY_IDENTITY, to: KODY_IDENTITY, timestamp: new Date(BASE_TIME + blocks.length * 1000).toISOString() }
      ]
    }
  };
  block.hash = computeBlockHash(block);
  blocks.push(block);
  cardIndex[mintId] = block;
  prevHash = block.hash;
}

// ── Fetch BTC price snapshot at forge time ──
let btcAtForge = 0;
try {
  const resp = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd');
  const data = await resp.json();
  btcAtForge = data.bitcoin.usd;
} catch(e) {
  try {
    const resp2 = await fetch('https://blockchain.info/ticker');
    const data2 = await resp2.json();
    btcAtForge = data2.USD.last;
  } catch(e2) { btcAtForge = 0; }
}

// ── Write Chain Files ──
const apiDir = join(ROOT, 'docs', 'api', 'v1');
mkdirSync(join(apiDir, 'cards'), { recursive: true });
mkdirSync(join(apiDir, 'identities'), { recursive: true });

// Chain state (lightweight summary)
const chainState = {
  protocol: 'rar-chain/1.0',
  chainHead: prevHash,
  chainLength: blocks.length,
  totalForged: blocks.length - 1,
  genesisHash: genesis.hash,
  genesisTimestamp: genesis.timestamp,
  lastBlockTimestamp: blocks[blocks.length - 1].timestamp,
  authority: AUTHORITY_IDENTITY,
  btcAtForge,
  consensus: {
    model: '3-of-5',
    threshold: 0.6,
  },
  identities: {
    [HOWARD_IDENTITY]: { alias: 'Howard Hoy', cards: 13, role: 'genesis-holder' },
    [KODY_IDENTITY]: { alias: 'Kody Wildfeuer', cards: blocks.length - 14, role: 'genesis-holder' }
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

// Identity files (wallet card listings)
const howardCards = blocks.filter(b => b.type === 'forge' && b.data.owner === HOWARD_IDENTITY);
const kodyCards = blocks.filter(b => b.type === 'forge' && b.data.owner === KODY_IDENTITY);

writeFileSync(join(apiDir, 'identities', `${HOWARD_IDENTITY}.json`), JSON.stringify({
  address: HOWARD_IDENTITY,
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

writeFileSync(join(apiDir, 'identities', `${KODY_IDENTITY}.json`), JSON.stringify({
  address: KODY_IDENTITY,
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
console.log(`  Howard's Identity: ${HOWARD_IDENTITY}`);
console.log(`    → ${howardCards.length} HOLO cards (1-of-1 mythic/rare)`);
console.log('');
console.log(`  Kody's Identity:   ${KODY_IDENTITY}`);
console.log(`    → ${kodyCards.length} CORE cards`);
console.log('');
console.log(`  Output: docs/api/v1/`);
console.log('═══════════════════════════════════════════');
