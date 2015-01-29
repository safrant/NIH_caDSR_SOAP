#!/bin/bash
#*****************************************************
# SyslogSender run script                    R Moulton
# Production
# This directory must be current to run
#*****************************************************
ROOT=/Users/safrant/NIH_caDSR_SOAP/NIH_caDSR_SOAP/caDSR_SOAP_agent/syslog-2.1/
CLASS=gov.nist.syslog.SyslogSender
CP=${ROOT}dist/SyslogCollector.jar:${ROOT}lib/*
java -cp $CP $CLASS &
