# Day 1 - Pokémon TCG AI Battle Challenge

# Objective

The goal of Day 1 is to understand how the Pokémon Trading Card Game works before building an AI agent.

An AI cannot make good decisions unless it first understands the game rules and legal actions.

---

# 1. Game Rules

## What is Pokémon TCG?

Pokémon Trading Card Game (TCG) is a turn-based strategic card game played between two players.

Each player has:

- 60-card deck
- 1 Active Pokémon
- Up to 5 Benched Pokémon
- 6 Prize Cards

Players take turns until one player satisfies a win condition.

---

## Why do we need to learn the rules?

The AI should only perform legal actions.

Example:

Legal:
- Attach one Energy
- Play Trainer card
- Attack once

Illegal:
- Attach two Energies in one turn
- Attack without required Energy
- Attack twice in the same turn

Without understanding the rules, the AI cannot play correctly.

---

# 2. Turn Flow

Every turn follows the same sequence.

Start Turn

↓

Draw one card

↓

Attach one Energy (optional)

↓

Play Trainer cards

↓

Evolve Pokémon

↓

Use Abilities

↓

Retreat Active Pokémon (optional)

↓

Attack

↓

End Turn

---

## Why is Turn Flow important?

The AI must know which actions are available at each stage.

Example:

After attacking

↓

Turn immediately ends

↓

The AI cannot play another Trainer card.

Understanding the turn order prevents illegal moves.

---

# 3. Card Types

There are three major card types.

## Pokémon Cards

Purpose:
Used for battling.

Contain:

- HP
- Attacks
- Abilities
- Weakness
- Resistance
- Retreat Cost

Example:

Pikachu
Charizard
Bulbasaur

---

## Energy Cards

Purpose:

Provide energy required to perform attacks.

Without enough Energy

↓

Attack cannot be used.

Normally

Only one Energy card can be attached during a turn.

---

## Trainer Cards

Purpose:

Support the player.

Examples:

- Draw cards
- Heal Pokémon
- Search deck
- Switch Pokémon
- Remove special conditions

Trainer cards improve strategy but do not attack.

---

# 4. Energy System

Every attack has an Energy Cost.

Example:

Thunderbolt

Energy Required:

⚡ ⚡ ⚡

Meaning:

The Pokémon must have three Electric Energy attached before using the attack.

---

## Why is Energy important?

Energy controls the speed of the game.

The player must decide

Which Pokémon should receive Energy?

Since only one Energy can normally be attached each turn,

poor Energy management can lose the game.

---

# 5. Prize Cards

At the beginning of the game,

each player sets aside six Prize Cards.

Whenever an opponent's Pokémon is Knocked Out,

the player takes Prize Cards.

Usually

Regular Pokémon

↓

1 Prize Card

Powerful Pokémon

↓

2 or more Prize Cards

---

## Why are Prize Cards important?

Collecting all Prize Cards is the primary way to win.

The AI should therefore choose attacks that maximize Prize Card gain whenever possible.

---

# 6. Win Conditions

A player wins if:

1. Collect all Prize Cards.

2. Opponent has no Pokémon remaining.

3. Opponent cannot draw a card at the beginning of their turn (Deck Out).

---

## Why does the AI need this?

The AI should always know which winning condition is closest.

Sometimes attacking is not the best move.

Protecting a Pokémon or forcing a deck-out may lead to victory.

---

# 7. SDK (Software Development Kit)

## What is SDK?

The SDK is a collection of tools provided by the competition organizers.

It allows our Python program to communicate with the Pokémon Simulator.

Without the SDK,

our AI cannot interact with the game.

---

## SDK provides

- Battle APIs
- Search APIs
- Card information
- Game State access
- Simulator communication

---

# 8. Sample Agent

The competition provides a sample AI.

Purpose:

- Learn project structure
- Understand simulator usage
- Observe how an AI makes decisions
- Learn available APIs

The sample agent is not meant to be the strongest AI.

It is a learning reference.

---

# 9. Logs

Logs record everything happening during a match.

Example

Turn 1

↓

Draw Card

↓

Attach Energy

↓

Play Trainer

↓

Attack

↓

Damage

↓

Turn Ends

---

## Why are Logs useful?

Logs allow us to understand

State

↓

Action

↓

New State

They help debug the AI and understand why a decision was made.

---

# Competition Architecture

The competition consists of five major components.

Your AI Agent

↓

SDK (cg.api)

↓

Pokémon Simulator

↓

Game State

↓

Your AI Agent

The AI receives the current Game State,

chooses the best action,

sends it through the SDK,

the Simulator updates the game,

and returns a new Game State.

This loop continues until the match finishes.

---

# Day 1 Learning Outcome

After completing Day 1, I should be able to answer:

✔ How Pokémon TCG works.

✔ What happens during a turn.

✔ Different card types.

✔ How Energy works.

✔ How players win.

✔ What the SDK is.

✔ What the Sample Agent does.

✔ Why logs are important.

✔ Basic architecture of the competition.