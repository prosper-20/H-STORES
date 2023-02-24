import requests


def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxa08ce2dc35284b29911386a445e26010.mailgun.org/messages",
		auth=("api", "3a24ab6591ce5540700f5e221a7df618-52d193a0-981d90ee"),
		data={"from": "Excited User <mailgun@sandboxa08ce2dc35284b29911386a445e26010.mailgun.org>",
			"to": ["edwardprosper001@gmail.com", "YOU@sandboxa08ce2dc35284b29911386a445e26010.mailgun.org"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})

# def send_simple_message():
#     return requests.post(
#         "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
#         auth=("api", "pubkey-022317934ae15342997baa3417eb6980"),
#         data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
#               "to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
#               "subject": "Hello",
#               "text": "Testing some Mailgun awesomness!"})




# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/sandboxa08ce2dc35284b29911386a445e26010.mailgun.org/messages",
# 		auth=("api", "3a24ab6591ce5540700f5e221a7df618-52d193a0-981d90ee"),
# 		data={"from": "Excited User <mailgun@sandboxa08ce2dc35284b29911386a445e26010.mailgun.org",
# 			"to": ["edwardprosper001@gmail.com", "YOU@sandboxa08ce2dc35284b29911386a445e26010.mailgun.org"],
# 			"subject": "Hello",
# 			"text": "Testing some Mailgun awesomness!"})