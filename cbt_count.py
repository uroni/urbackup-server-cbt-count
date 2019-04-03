import csv
import urbackup_api
import time
import datetime

excel_output = True

def count_cbt_clients_server(serverurl, username, password):
	server = urbackup_api.urbackup_server(serverurl, username, password)
			
	clients = server.get_status()
	
	if clients==None:
		return None
	
	diff_time = 30*24*60*60 # 1 month
	ret = 0
	for client in clients:
		# Client was seen in the last month
		if client["lastseen"]!="-" and client["lastseen"] > time.time() - diff_time:
			if "-cbt" in client["client_version_string"]:
				lastseen_str = datetime.datetime.fromtimestamp(client["lastseen"]).strftime("%x %X")
				print("CBT client "+client["name"]+" last seen at "+lastseen_str+" version "+client["client_version_string"])
				ret+=1
				
	return ret

def count_cbt_clients():
	with open('servers.csv', newline='') as csvfile_in:
		with open('server_cbt_counts.csv', 'w', newline='') as csvfile_out:
			serverreader = csv.reader(csvfile_in, dialect='excel')
			serverwriter = csv.writer(csvfile_out, dialect='excel')
			if excel_output:
				serverwriter.writerow(["sep=,"])
			serverwriter.writerow(["Server URL", "CBT client count"])
			idx=0
			for row in serverreader:	
				if idx==0 and "sep=" in row[0]:
					continue
				if (idx==0 or idx==1) and row[0]=="Server URL":
					continue
					
				if len(row)<3:
					print("Row "+str(idx+1)+" doesn't have enough columns. ("+", ".join(row)+")")
					continue
			
				serverurl = row[0]
				username = row[1]
				password = row[2]
				
				num = count_cbt_clients_server(serverurl, username, password)
			
				if num==None:
					serverwriter.writerow([serverurl, "Getting CBT count failed"])
				else:
					serverwriter.writerow([serverurl, num])
					
				idx+=1


if __name__=="__main__":
	count_cbt_clients()