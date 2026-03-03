import re
from Analise.contexto import analisar_contexto

def analisa_user(logs):
    regex_failed = re.compile(r"Failed password for")
    regex_accepted = re.compile(r"Accepted password for")
    regex_invalid = re.compile(r"Invalid user|Failed password for invalid user")
    regex_closed = re.compile(r"Connection closed|Received disconnect")

    #for result in logs:
    if regex_failed:
        log_wrong_passwd = re.search("Failed password for (.*) from", logs)
        if log_wrong_passwd:
            return log_wrong_passwd.group(1)
        
    elif regex_accepted:
        log_connec_close = re.search(f"Connection closed by authenticating user (.*) .* port .*", logs)
        if log_connec_close:
            return log_connec_close.group(1)
        
    elif regex_invalid:
        log_invalid_user = re.search("Invalid user (.*) from", logs)
        #print("Failed login attempt for invalid user:", log_invalid_user)
        if log_invalid_user:
            return log_invalid_user.group(1)
        
    elif regex_closed:
        #print("Successful login for user:", re.search(f"Accepted password for (.*) from", result).group(1))
        return re.search(f"Accepted password for (.*) from", logs).group(1)