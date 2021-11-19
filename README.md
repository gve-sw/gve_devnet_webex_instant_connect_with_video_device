# GVE Devnet Webex Instant Connect with Video Device
Prototype of how to include a Webex video device such as a Desk Pro as the only device for a health provider to connect to a Webex Instant Connect session. 


## Contacts
* Gerardo Chaves (gchaves@cisco.com)

## Solution Components
* Webex
*  Webex Instant Connect


## Prerequisites
Webex instant connect subscription:  https://instant.webex.com/  
NOTE: You will need to follow the process you will trigger by clicking on the "Activate Instant Connect" button on instant.webex.com using your 
organizations admin credentials to obtain the proper "Audience" string needed for the installation step below.  

## Installation/Configuration

  - Setup the following environmental variables in the .env file:  
        `IC_API_URL` is the URL for the Webex Instant Connect API (default value is https://mtg-broker-a.wbx2.com/api/v1/joseencrypt )   
        `IC_SPACE_API_URL` is the URL for the Webex Instant Connect space API (default value is https://mtg-broker-a.wbx2.com/api/v1/space )   
        `IC_AUDIENCE` is the "Audience" string provided to you when you register to use the Instant Connect Service  
        `IC_ACCESS_TOKEN` is a valid Webex Access token from the organization you register to use Instant Connect.  
        `IC_URL_DURATION` is the the expiration time given as the number of seconds from the Unix Epoch (1970-01-01T00:00:00Z UTC) on or after which the JWT will not be accepted for processing. If not specified will be set for 15 minutes later than the time when the request was made    
        `IC_BASE_SUBJECT`  A unique value in your organization which will be used to place hosts and guests into the same collaboration space. This claim may contain only letters, numbers, and hyphens  
        `IC_HOST_BASEURL` is the base URL to use with Instant Connect for the host without a need to log in.  Check the Instant Connect documentation for current values (default value is https://instant.webex.com/hc/v1/login?int=jose&v=1&data=)  
        `IC_AGENT_BASEURL` is the base URL to use with Instant Connect to force the host to log into Webex.  Check the Instant Connect documentation for current values (default value is https://instant.webex.com/hc/v1/login?&fli=true&int=jose&data=)  
        `IC_CLIENT_BASEURL` is the base URL to use with Instant Connect to use with the Guest without a need to log in. Check the Instant Connect documentation for current values (default value is https://instant.webex.com/hc/v1/talk?int=jose&data= )  
 
  - Install the required python libraries in your environment:  
``` pip install -r requirements.txt```  


## Usage

- Run app.py:  

```python app.py```  

- Browse to the URL where the flask aplication is running (i.e. http://127.0.0.1:5000/ )  
- (optional) Enter the name and Webex ID of the user that owns the personal device you want to add to the temporary space so they can dial in  
- You will be re-directed to a page that displays all the information you need to start the Instant Connect session, including the SIP URI for the Webex Device
 to dial into.  




# Screenshots




### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.