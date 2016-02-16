import requests
from bs4 import BeautifulSoup
import json

website_address = 'http://register.start.bg/'




def get_server_list(initial_path):
	r = requests.get(initial_path)
	soup = BeautifulSoup(r.content, 'html.parser')
	result_servers = {}
	all_links_from_website = soup.find_all('a')
	all_links_count = len(all_links_from_website)
	print(all_links_count)
	counter = 0
	for link in all_links_from_website:
		try:
			href = link.get('href')
			if href is not None:
				if href.startswith('link.php'):
						full_path = initial_path + href
				elif href.startswith('http'):
					full_path = href
				r_site = requests.get(full_path)
				server_name = r_site.headers["Server"]
				result_servers[full_path] = server_name
				print(full_path, server_name )
				counter += 1
				print(counter, "/", all_links_count)
		except (requests.exceptions.ConnectionError, KeyError, requests.exceptions.TooManyRedirects, requests.exceptions.ReadTimeout) as e:
			counter+=1
	with open('servers.txt', 'w') as outfile:
		json.dump(result_servers, outfile)
	print(result_servers)
	return result_servers




def create_histogram(server_list):
	servers_dict = {'nginx':0, 'IIS':0, 'lighttpd':0, 'Apache':0}
	for website in server_list:
		for key in servers_dict:
			if key in server_list[website]:
				servers_dict[key]+=1
	return servers_dict

results = get_server_list(website_address)
print(create_histogram(results))


