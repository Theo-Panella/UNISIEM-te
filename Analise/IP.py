# --------------------------------------------------------------------------------------------------------------------
# Bloco de analise de IPs
# --------------------------------------------------------------------------------------------------------------------
import re
def analisa_ip(logs):
    #for result in logs:
        if re.search("Failed password for.*", logs):
            log_wrong_passwd_ip = re.search("Failed password for.* from (.*) port", logs)
            if log_wrong_passwd_ip:
                return log_wrong_passwd_ip.group(1)
        
        elif re.search("Connection closed by authenticating user.*", logs):
            log_connec_close = re.search(f"Connection closed by authenticating user.* (.*) port .*", logs)
            if log_connec_close:
                return log_connec_close.group(1)

        elif re.search("Invalid user.*", logs):
            log_invalid_user_ip = re.search("Invalid user.* from (.*) port", logs)
            if log_invalid_user_ip:
                return log_invalid_user_ip.group(1)

        elif re.search("Accepted password for.*", logs):
            log_successful_login_ip = re.search("Accepted password for.* from (.*) port", logs)
            if log_successful_login_ip:
                return log_successful_login_ip.group(1)