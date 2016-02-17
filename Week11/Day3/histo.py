
import matplotlib.pyplot as plt

results = ['Apache', 'Apache/2.2.3 (CentOS)', 'Apache', 
'Apache/2.4.6 (CentOS) PHP/5.4.16', 'Apache/2.2.29 (Unix) mod_ssl/2.2.29 OpenSSL/0.9.8e-fips-rhel5 mod_bwlimited/1.4', 
'Apache/2.2.15 (CentOS)', 'Apache/2.2.3 (CentOS)', 'Apache/2.4.6 (CentOS) PHP/5.4.16', 'Apache', 'Apache/2.2.15 (CentOS)', 
'Apache', 'Apache/2.4.6 (CentOS) PHP/5.4.16', 'Apache/2.2.3 (CentOS)', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.3 (CentOS)', 
'nginx/1.7.10', 'nginx/1.7.10', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 
'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)',
 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 'Apache/2.2.15 (CentOS)', 
 'Apache/2.2.15 (CentOS)']




def create_histogram(server_list):
	servers_dict = {'nginx':0, 'IIS':0, 'lighttpd':0, 'Apache':0}
	for server in server_list:
		for key in servers_dict:
			if key in server:
				servers_dict[key]+=1
	return servers_dict


def plot(h):
	keys = list(h.keys())
	values = list(h.values())
	
	X = list(range(len(keys))) 
	
	plt.bar(X, list(h.values()), align="center")
	plt.xticks(X, keys)
	
	plt.title(".bg servers")
	plt.xlabel("Server")
	plt.ylabel("Count")
	plt.savefig("histogram.png")	

dict_results = create_histogram(results)
plot(dict_results)




