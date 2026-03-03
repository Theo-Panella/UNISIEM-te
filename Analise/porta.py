# --------------------------------------------------------------------------------------------------------------------
# Bloco de analise de portas 
# --------------------------------------------------------------------------------------------------------------------
import re
def analisa_porta(logs):
    #for result in logs:
        if re.search("Failed password for.*", logs):
            log_wrong_passwd_port = re.search("Failed password for.* port (.*) ssh2", logs)
            if log_wrong_passwd_port:
                return log_wrong_passwd_port.group(1)
            
        elif re.search("Connection closed by authenticating user.*", logs):
            log_connec_close = re.search(f"Connection closed by authenticating user.* port (.*)", logs)
            if log_connec_close:
                return log_connec_close.group(1)

        elif re.search("Invalid user.*", logs):
            log_invalid_user_port = re.search("Invalid user.* port (.*)", logs)
            if log_invalid_user_port:
                return log_invalid_user_port.group(1) 

        elif re.search("Accepted password for.*", logs):
            log_successful_login_port = re.search("Accepted password for.* port (.*) ssh2", logs)
            if log_successful_login_port:
                return log_successful_login_port.group(1)