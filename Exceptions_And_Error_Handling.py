from flask import Flask
import pandas as pd

app = Flask(__name__)  

information=pd.read_csv("source.csv")

@app.route('/')
def getDistinctOrganizationNames():
    orgName=list(information["organizationName"])
    return orgName
    

@app.route('/getSmdNames')
def getSmdNames():
    smdName=list(information["smdName"])
    return smdName

@app.route('/searchStringInTitle')
def searchStringInTitle():
    Title=list(information["title"])
    return Title

@app.route('/findPercentOrgNamesPulses')
def findPercentOrgNamesPulses():
    pulses_research=0
    for i in information["organizationName"]:
        split_string=i.split(" ")
        if "Pulses" in split_string and "Research" in split_string:
            pulses_research+=1
            percentage="Percentage of Pulses and Research in organisation name : "+str((pulses_research/len(information["organizationName"]))*100)+" %"
    return percentage

@app.route('/findPercentOrgNamesPulsesAgainstResearch')
def findPercentOrgNamesPulsesAgainstResearch():
    pulses_research=0
    research=0
    for i in information["organizationName"]:
        split_string1=i.split(" ")
        if "Pulses" in split_string1 and "Research" in split_string1:
            pulses_research+=1
        if "Research" in split_string1:
            research+=1
            percentage="Percentage of Pulses Against Research in organisation name : "+str(pulses_research/research*100)+" %"
    return percentage

@app.route('/findPercentOrgNamesResearch')
def findPercentOrgNamesResearch():
    research=0
    for i in information["organizationName"]:
        split_string=i.split(" ")
        if "Research" in split_string:
            research+=1
            percentage="Percentage of Research in organisation name : "+str((research/len(information["organizationName"]))*100)+" %"
    return percentage
 
@app.errorhandler(Exception) 
def basic_error(e): 
    return "An error occurred: " + str(e) 
 
if __name__ == "__main__": 
    app.run()