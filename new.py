# ------------------------------
# ONLINE VOTING SYSTEM (PYTHON)
# ------------------------------

# List of candidates (standing in the election)
candidates = ["Alice", "Bob", "Charlie"]

# Dictionary to store vote counts for each candidate
votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

# Set to store which voters have already voted (to avoid duplicate voting)
voted_voters = set()

# ------------------------------
# Function to show candidates
# ------------------------------
def show_candidates():
    print("\n--- Candidates List ---")
    for index, name in enumerate(candidates, start=1):
        print(f"{index}. {name}")

# ------------------------------
# Function to cast a vote
# ------------------------------
def cast_vote(voter_id):
    # Check if this voter has already voted
    if voter_id in voted_voters:
        print("⚠ You have already voted! Duplicate voting not allowed.")
        return

    # Show candidate options
    show_candidates()
    
    # Ask user to choose a candidate number
    try:
        choice = int(input("Enter candidate number you want to vote for: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    # Validate choice
    if 1 <= choice <= len(candidates):
        selected_candidate = candidates[choice - 1]
        # Add 1 vote to that candidate
        votes[selected_candidate] += 1
        # Mark this voter as voted
        voted_voters.add(voter_id)
        print(f"✅ Your vote for {selected_candidate} has been recorded successfully.")
    else:
        print("Invalid choice! Please select a valid candidate number.")

# ------------------------------
# Function to show voting results
# ------------------------------
def show_results():
    print("\n===== Voting Results =====")
    for candidate, count in votes.items():
        print(f"{candidate} : {count} votes")

    # Find winner (candidate with max votes)
    winner = max(votes, key=votes.get)
    print(f"\n🏆 Winner: {winner} with {votes[winner]} votes")

# ------------------------------
# Main program
# ------------------------------
def main():
    print("===== ONLINE VOTING SYSTEM =====")

    while True:
        print("\n1. Cast Vote")
        print("2. Show Results (Admin)")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            voter_id = input("Enter your Voter ID: ")
            cast_vote(voter_id)
        elif choice == "2":
            admin_password = input("Enter admin password: ")
            if admin_password == "admin123":
                show_results()
            else:
                print("❌ Wrong password! Access denied.")
        elif choice == "3":
            print("Thank you for using Online Voting System.")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
