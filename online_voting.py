# voters = {
#     "1001": "12345",
#     "1002": "abcd"
# }

# voter_id = input("Enter Voter ID: ")
# password = input("Enter Password: ")

# if voter_id in voters and voters[voter_id] == password:
#     print("Login successful!")
# else:
#     print("Invalid login")

'''voted = set()

voter_id = "1001"

if voter_id in voted:
    print("You have already voted!")
else:
    print("Vote submitted.")
    voted.add(voter_id)'''

# candidates = {
#     1: "Rahul (President)",
#     2: "Manoj (Secretary)",
#     3: "Iranna (Vice President)"
# }

# for cid, name in candidates.items():
#     print(cid, name)


# votes = {}

# candidate_choice = int(input("Choose candidate ID: "))
# votes[candidate_choice] = votes.get(candidate_choice, 0) + 1

# print("Vote saved!")


# Store the voters who already voted
voted_list = set()  

def cast_vote(voter_id):
    # Check if voter already voted
    if voter_id in voted_list:
        print("❌ You have already voted! Duplicate vote detected.")
    else:
        print("✔ Vote submitted successfully.")
        voted_list.add(voter_id)

# -------------------------------
# Testing the program
# -------------------------------

# First time voting
cast_vote("1001")  
# Output: ✔ Vote submitted successfully.

# Same voter tries again
cast_vote("1001")  
# Output: ❌ You have already voted! Duplicate vote detected.

# Another voter
cast_vote("1002")
# Output: ✔ Vote submitted successfully.
