""" Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

# Import Section
from flask import Flask, render_template, request, url_for, redirect
from collections import defaultdict
import datetime
import requests, time
import json
from dotenv import load_dotenv
import os
from webexteamssdk import WebexTeamsAPI

# load all environment variables
load_dotenv()

# Global variables
app = Flask(__name__)

@app.route('/teleconsultCreate',methods = ['POST', 'GET'])
def teleconsultCreate():
    if request.method == 'POST':
        IC_API_URL = os.environ.get("IC_API_URL")
        IC_SPACE_API_URL = os.environ.get("IC_SPACE_API_URL")
        IC_AUDIENCE = os.environ.get("IC_AUDIENCE")
        IC_ACCESS_TOKEN = os.environ.get("IC_ACCESS_TOKEN")
        IC_URL_DURATION = os.environ.get("IC_URL_DURATION")
        IC_AGENT_BASEURL = os.environ.get("IC_AGENT_BASEURL")
        IC_CLIENT_BASEURL = os.environ.get("IC_CLIENT_BASEURL")
        IC_HOST_BASEURL = os.environ.get("IC_HOST_BASEURL")

        result = request.form
        resultDict=dict(request.form)
        print(result)
        print(resultDict)

        theWebexID=resultDict['WebexID']
        confirmedBaseSubject=resultDict['ICBaseSubject']

        url = IC_API_URL

        payload = json.dumps({
            "aud": IC_AUDIENCE,
            "jwt": {
                "sub": confirmedBaseSubject, #using same subject will return same consultation always!,
                "exp": int(time.time())  + int(IC_URL_DURATION)
            }
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ IC_ACCESS_TOKEN
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_dict = json.loads(response.text)

        print(response.text)
        theHost=response_dict['host'][0]
        theGuest=  response_dict['guest'][0]
        print(theHost)
        print(theGuest)

# now obtain the spaceID and token
        url = IC_SPACE_API_URL+"?int=jose&data="+theHost
        response = requests.request("GET", url, headers=headers, data=payload)
        response_dict = json.loads(response.text)
        print(response.text)
        theToken=response_dict['token']
        theSpaceID=response_dict['spaceId']
        print(f'access token: {theToken}')

        #obtain the space meeting URI
        api = WebexTeamsAPI(access_token=theToken)
        theResult = api.rooms.get_meeting_info(theSpaceID)
        print(f'Meetings info for the space: {theResult}')
        theSpaceSIP=theResult.sipAddress
        theMeetingNumber=theResult.meetingNumber

        #if webex ID to add was provided, add them to the space
        if theWebexID!='':
            theResult=api.memberships.create(theSpaceID,personEmail=theWebexID)
            print("Added to space: ",theResult)


        return render_template("result.html",
                               basehost=IC_HOST_BASEURL,
                               baseagent=IC_AGENT_BASEURL,
                               baseguest=IC_CLIENT_BASEURL,
                               host=theHost,
                               guest=theGuest,
                               spaceid=theSpaceID,
                               spaceURI=theSpaceSIP,
                               participant=theWebexID,
                               token=theToken)

##Routes
@app.route('/')
def index():
    IC_BASE_SUBJECT = os.environ.get("IC_BASE_SUBJECT")
    return render_template('consult.html',theBase=IC_BASE_SUBJECT)

if __name__ == "__main__":
    app.run(port=5000,debug=True)