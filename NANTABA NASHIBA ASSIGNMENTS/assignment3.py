# Assignment 3 - World Cup 2026 Simulation

import random


def main():
	countries = [
		"Argentina",
		"Brazil",
		"France",
		"Spain",
		"Germany",
		"England",
		"USA",
		"Mexico",
	]

	# Randomly chooses the winner for this simulation
	winner = random.choice(countries)

	print("World Cup 2026 - Simple Simulation")
	print("Try to guess which country will win.")
	print("Commands: 'list' to show candidates, 'hint' for a hint, 'give up' to reveal, 'quit' to exit")

	attempts = 0

	# creates a lookup to match guesses case-insensitively while preserving display names
	lookup = {c.lower(): c for c in countries}

	while True:
		prompt = f"Round {attempts+1} - Your guess: "
		guess = input(prompt).strip()

		# demonstrate continue: skips empty inputs without counting them as attempts
		if not guess:
			print("Empty input — please type a country or command.")
			continue

		cmd = guess.lower()
		if cmd in ("quit", "exit"):
			print("Exiting simulation. Goodbye!")
			break

		if cmd == "list":
			print("Candidates:", ", ".join(countries))
			continue

		if cmd == "hint":
			# provides a small hint (first letter)
			print(f"Hint: the winner's name starts with '{winner[0]}'.")
			continue

		if cmd == "give up":
			print(f"You gave up. The winner is: {winner}")
			break

		# match user's guess case-insensitively against candidates
		key = guess.lower()
		if key not in lookup:
			print("That country is not in the candidate list. Type 'list' to see options.")
			continue
		candidate = lookup[key]
		# counts this as a valid attempt
		attempts += 1

		# demonstrate pass: placeholder for any future tie logic (no-op here)
		if attempts == 3:
			pass

		if candidate == winner:
			print(f"Correct! {winner} wins World Cup 2026!")
			print(f"You guessed it in {attempts} rounds.")
			break
		else:
			print(f"No — {candidate} didn't win this simulation. Try again or type 'give up'.")
			# continue to next round (explicit for clarity)
			continue


if __name__ == "__main__":
	main()

