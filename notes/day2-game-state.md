# Day 2 Notes: Game State, SDK Setup, and Sample Agent

## 1. Game State Structure
In the Pokémon TCG AI Battle Challenge, the game state captures all information required for an agent to make a decision:
- **Active Pokémon**: The current Pokémon in battle, its HP, attached energy, status conditions.
- **Bench**: Up to 5 Pokémon waiting to enter battle.
- **Hand**: Cards available to play.
- **Deck**: Remaining library (hidden from agent, size is known).
- **Discard Pile**: Used cards.
- **Prize Cards**: Face-down cards taken upon knocking out opponent Pokémon (6 total).
- **Turn info**: Whose turn it is, phase, energy attachment status.

## 2. SDK Installation
Installed the Pokémon TCG simulator SDK:
```bash
pip install pokemon-tcg-simulator
```
*(Verify compatibility with environment requirements).*

## 3. Running the Sample Agent
Ran the baseline agent against a random opponent:
```bash
python -m pokemon_tcg.run_agent --agent sample_agent.py --opponent random
```

## 4. Log Observations
- Observed detailed step-by-step game actions in output logs.
- Turn decisions are logged including energy attachments, Trainer card activations, and attacks.
- Knockouts and prize card changes are logged.
