from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pysimplesoap.server import SoapDispatcher
from NIH_caDSR_SOAP import settings
from forms_static import adrenal
from forms_static import demographic
from forms_static import FDA
from forms_static import HERF
from forms_static import NCI_Demographics
from pysimplesoap.simplexml import SimpleXMLElement

import os

def demo(request):
    return HttpResponse('NIH caDSR Web Services')

def wsdl(request):
    return HttpResponse('NIH caDSR WSDL')

def form_as_XML(request):
    formID = request.RetrieveFormRequest.workflow.formID
    if formID == 'Adrenal_xml':
      return SimpleXMLElement(adrenal)
    elif formID == 'Demog_xml':
      return SimpleXMLElement(demographic)
    elif formID == 'http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/form_package_identifier#4617751v1.0/1':
      return SimpleXMLElement(FDA)
    elif formID == 'http://nci.nih.gov/xml/owl/cadsr#form_package/99999/1.0':
      return SimpleXMLElement(HERF)
    elif formID == 'http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/form_package_identifier#2674812v4.0/1':
      return SimpleXMLElement(NCI_Demographics)
    else:
      return SimpleXMLElement('<xml>Error</xml>')

dispatcher = SoapDispatcher(
    'cadsr_soap_dispatcher',
    location = "https://localhost:8080/soap",
    action = "https://localhost:8080/soap",
    namespace = "http://nlm.nih.gov/sdc/form",
    prefix="ns0",
    ns = "urn:ihe:iti:rfd:2007")

# register func
dispatcher.register_function('soap', form_as_XML,
    returns={'FormResult': str},
    args={'formID': str})


#delete for csrf the POST for this view
@csrf_exempt
def dispatcher_handler(request):
    if request.method == "POST":
        response = HttpResponse(dispatcher.dispatch(request.body))
    else:
        response = HttpResponse(dispatcher.wsdl())
    response['Content-length'] = str(len(response.content))
    return response
