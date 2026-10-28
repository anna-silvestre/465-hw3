run the following

sudo apt update
sudo apt install -y build-essential gdb binutils checksec apparmor-utils

and confirm with

gcc --version, gdb --version, checksec --version, and aa-status --version

use 

sudo mkdir -p /opt/agentsec
printf 'FAKE-COURSE-SECRET\n' | sudo tee /opt/agentsec/decoy.txt
sudo chmod 600 /opt/agentsec/decoy.txt

to create a decoy file in your root directory




gcc -O0 -g -fno-stack-protector -no-pie -Wl,-z,noexecstack -Wall -Wextra -o src/legacy_log_parser src/legacy_log_parser.c

checksec --file=./src/legacy_log_parser


TODO