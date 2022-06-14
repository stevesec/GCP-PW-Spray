# Google Cloud Platform (GCP) Password Spray

__My first commit__ 

![Go Easy on Me!](https://memegenerator.net/img/instances/84782628/go-easy-on-me.jpg)

GCP PW Spray is a __rude and crude__ password spraying tool using Selenium Webdriver and Undetected_Chromedriver. Currently, only Chrome browser is supported, due to limitations with Google accounts browser security.

GCP PW Spray is designed to run on Kali Linux. It will auto detect the file you give it with the -u flag with emails on new lines

## Linux

- Kali Linux
- Debian 7+
- [More to come]

### Setup:

1. chmod +x setup.sh
2. Run the setup.sh script as root.

### Usage:
```
python3 gcp_v2.py -f emails.txt -p 'Password'
```

### Further Tasks

- [ ] Add more support for various operating systems
- [ ] Add headless mode
- [ ] Add CAPTCHA response
- [ ] Add support for more passwords
- [ ] Add support for more Google login pages

## Inspiration:

- @knavesec [CredMaster](https://github.com/knavesec/CredMaster)
