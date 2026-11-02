#include <tunables/global>

/home/anna_s/465-hw3/csce465-agentsec/hw3/src/legacy_log_parser {
    #include <abstractions/base>
    
    /home/anna_s/465-hw3/csce465-agentsec/hw3/inbox/* r,
    /home/anna_s/465-hw3/csce465-agentsec/hw3/markers/* rw,
    
    audit deny /opt/agentsec/decoy.txt rwklx,
    deny /bin/* x,
    deny /usr/bin/* x, 
}