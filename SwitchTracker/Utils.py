import requests
serverchan = "https://sc.ftqq.com/SCU14945Tdf01b78094bd74ebcb24edb6cb89c53859f8236a06fa9.send?text="

def SendMsg(title, content):
	msg = ""
	msg += serverchan
	msg += str(title)
	msg += "&desp="
	msg += content
	print(msg)
	requests.get(msg)
	
if __name__ == '__main__':
    print("ok")