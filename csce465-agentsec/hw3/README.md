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


OPENCLAW OPS

export TAMU_API_KEY="key"
node tamu-shim.mjs

openclaw onboard --non-interactive --accept-risk --auth-choice custom-api-key --custom-provider-id tamus --custom-compatibility openai --custom-base-url "http://127.0.0.1:8899/openai" --custom-api-key via-shim --custom-model-id "protected.gpt-4o" --skip-channels

openclaw config set models.providers.tamus.request.allowPrivateNetwork true
openclaw config set agents.defaults.timeoutSeconds 600
openclaw config set agents.defaults.memorySearch.enabled false

openclaw config validate
openclaw models set tamus/protected.gpt-4o
openclaw daemon install && openclaw daemon start




sudo useradd --system --create-home --shell /usr/sbin/nologin agentlab



sudo apparmor_parser -r -W policy/apparmor.profile
sudo aa-status | grep legacy_log_parser
sudo -u agentlab ./src/legacy_log_parser inbox/payload.bin
sudo dmesg | grep -i apparmor