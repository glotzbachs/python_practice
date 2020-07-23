#slice out username and domain from user's email address



#get user email

email = input('What is your email address?: ').strip()

#slice username

username = email[:email.index('@')]

#slice domain

domain = email[email.index('@')+1:-4]
              
#format

output = "Username: {}, Domain: {}".format(username,domain)

#display

print(output)
