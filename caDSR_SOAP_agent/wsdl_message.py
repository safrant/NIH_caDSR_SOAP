from caDSR_SOAP_agent.local_settings import server_url

wsdl_xml = """
<definitions xmlns="http://schemas.xmlsoap.org/wsdl/" 
             xmlns:ihe="urn:ihe:iti:rfd:2007" 
             xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" 
             xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
             xmlns:wsaw="http://www.w3.org/2005/08/addressing" 
             name="FormManager" 
             targetNamespace="urn:ihe:iti:rfd:2007">

    <types>
        <xsd:schema elementFormDefault="qualified" 
                    targetNamespace="urn:ihe:iti:rfd:2007">
            <xsd:include schemaLocation="%s" />
        </xsd:schema>
    </types>
    <!--  Message definitions  -->
    <message name="RetrieveForm_Message">
        <documentation>Retrieve Form Request</documentation>
        <part name="body" element="ihe:RetrieveFormRequest"/>
    </message>
    <message name="RetrieveFormResponse_Message">
        <documentation>Retrieve Form Response</documentation>
        <part name="body" element="ihe:RetrieveFormResponse"/>
    </message>
    <message name="RetrieveClarification_Message">
        <documentation>
            Request clarification from the organization identified.
        </documentation>
        <part name="body" element="ihe:RetrieveClarificationRequest"/>
    </message>
    <message name="RetrieveClarificationResponse_Message">
        <documentation>
            Return clarifications and appropriate status message.
        </documentation>
        <part name="body" element="ihe:RetrieveClarificationResponse"/>
    </message>
    <!--  Operation/transaction declarations  -->
    <portType name="FormManager_PortType">
        <operation name="FormManager_RetrieveForm">
            <documentation>
                Corresponds to Transaction ITI-34 of the IHE Technical Framework
            </documentation>
            <input message="ihe:RetrieveForm_Message" 
                   wsaw:Action="urn:ihe:iti:2007:RetrieveForm"/>
            <output message="ihe:RetrieveFormResponse_Message" 
                    wsaw:Action="urn:ihe:iti:2007:RetrieveFormResponse"/>
        </operation>
        <operation name="FormManager_RetrieveClarifications">
            <documentation>
                Corresponds to Transaction ITI-XXX of the IHE Technical Framework
            </documentation>
            <input message="ihe:RetrieveClarification_Message" 
                   wsaw:Action="urn:ihe:iti:2007:RetrieveClarification"/>
            <output message="ihe:RetrieveClarificationResponse_Message" 
                    wsaw:Action="urn:ihe:iti:2007:RetrieveClarificationResponse"/>
        </operation>
    </portType>
    <!--  SOAP 1.2 Binding  -->
    <binding name="FormManager_Binding_Soap12" type="ihe:FormManager_PortType">
        <soap12:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
        <operation name="FormManager_RetrieveForm">
            <soap12:operation soapAction="urn:ihe:iti:2007:RetrieveForm"/>
            <input>
                <soap12:body use="literal"/>
            </input>
            <output>
                <soap12:body use="literal"/>
            </output>
        </operation>
        <operation name="FormManager_RetrieveClarifications">
            <soap12:operation soapAction="urn:ihe:iti:2007:RetrieveClarification"/>
            <input>
                <soap12:body use="literal"/>
            </input>
            <output>
                <soap12:body use="literal"/>
            </output>
        </operation>
    </binding>
    <!--  Service definition  -->
    <service name="FormManager_Service">
        <port binding="ihe:FormManager_Binding_Soap12" 
              name="FormManager_Port_Soap12">
            <soap12:address location="http://ushik-stg.dcgroupinc.com:80/FormManager_Service"/>
        </port>
    </service>
</definitions>
""" % (server_url)
