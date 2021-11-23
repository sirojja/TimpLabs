3a - the program writes system information to a file and puts root rights on it. A non-privileged user can obtain this information by entering his private key into the secure program. Installation must be done with root privileges. The operating system is Linux.

3b - The php script parses the information from the browser request headers and saves it to a file on the server. To install, you need to do:
git clone https://github.com/matomo-org/device-detector
git clone https://github.com/mustangostang/spyc
