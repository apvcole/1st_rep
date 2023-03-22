import smtplib

# Collect name and email address from user
name = input("Enter your name: ")
email = input("Enter your email address: ")

# Compose email message
subject = "Thanks for submitting"
body = f"Thanks {name}, you are confirmed. We'll be in touch soon."

# Connect to email server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("calendar@amazingphotovideo.com", "Joey2022!") # replace with actual password

# Send email
message = f"Subject: {subject}\n\n{body}"
server.sendmail("team@amazingphotovideo.com", email, message)

# Close connection to server
server.quit()

print("Email sent!")
