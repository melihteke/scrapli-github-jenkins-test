from scrapli.driver.core import IOSXEDriver

my_device = {
    "host": "192.168.178.1",
    "auth_username": "jenkins",
    "auth_password": "jenkins",
	"auth_secondary":"!mlh1985",
    "auth_strict_key": False,
    "transport": "paramiko"
}

with IOSXEDriver(**my_device) as conn:
    print(conn.get_prompt())
	
