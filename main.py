introduction = print("Welcome to the script! I believe you're here to use the Eryn.IO API to check your Discord ID for any accounts used by RoVer and the Eryn.IO API.")
introduction2 = print("Let's get started, shall we?")

id = int(input("Please print your discord ID here:"))

request = requests.get(f'https://verify.eryn.io/api/user/{id}')

print("Here are the results!")
result = print(request.text)
