# ls-rescue
## Installation
This tool will be useful probably only for advanced linux users, so there is no package for it.
Maybe someday I'll create script that automates instalation, but for now:
1. Clone this repo: `git clone https://github.com/Q-back/ls-rescue/`
2. Add alias to your `.bashrc` or whatever your distro uses:
  * `nano ~/.bashrc`
  * add (e.g to the end of file) line: `alias ls-rescue="path/to/ls-rescue.py"`
3. Enjoy.
## Usage
* To diff two ls outputs from files
  * save your ls before and after your mistake to 2 separate files
  * run `ls-rescue -f ls1_file ls2_file`.
* To diff two ls outputs normally
  * run `ls-rescue`
  * input first ls output
  * input second ls output
  
  You'll see what changed.
