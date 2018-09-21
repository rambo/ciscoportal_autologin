# Autologin for Cisco captive portal

Due to JS bullshit in the portal needs to use real browser.

## Install dependencies

    sudo apt-get install python3-selenium chromium-chromedriver xvfb

## Usage

    xvfb-run `realpath selenium_login.py` "username" "password"

Run make a shell script wrapping that and run the script in interface post-up
and regularly from cron.
