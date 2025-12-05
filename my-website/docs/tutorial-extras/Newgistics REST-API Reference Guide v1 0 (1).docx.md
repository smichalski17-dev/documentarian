---
title: "Newgistics REST API Reference Guide"
linkTitle: "Newgistics REST API Reference Guide"
description: >
  This is a guide to using the Newgistic REST API.
---

# Web Services REST-API Reference Guide

**20 August 2012**

**Version 2.0**


***Document Revision History***

| Version | Date | Significant Changes |
| :---: | :---- | :---- |
| 1.1 | 12/7/2011 | Added deliveries verbiage |
| 1.2 | 2/21/2012 | Updated TrackRequest method for Qualifiers strings and tracking statuses |
| 1.3 | 4/11/2012 | PRN change- Label URL is returned regardless of delivery method |
| 2.0 | 8/17/2012 | Web Services API – REst Revision |



## Audience, Scope, and Purpose 

This document provides the client with the details of REst API methods used by Newgistics to identify key transit events. Clients can use the API information to integrate tracking into their native systems seamlessly.

RESst calls can return data in either XML or JSON formats.  Both implementations are documented here.

## Web Services Overview 

### Description

The Newgistics Web Application Services API (Application Programming Interface) allows clients and partners to integrate Newgistics Forward and Reverse (SmartLabel) services into their own applications with a seamless look and feel for the user. 

Web Application Services are Internet-enabled APIs that allow clients’ current application to perform the following actions from an interface developed with technology such as C\# or Java: 

* Generate one or more new graphical return labels   
* Track existing delivery or return packages through the Newgistics handling process  
* Schedule a pickup with the US Postal Service for returns  
* Cancel a previously scheduled pickup with the US Postal Service for returns

#### Prerequisites

Before the client can make a Web Application Service call, the client’s user account must be configured in the Newgistics database. 

#### Result Formats

Results may be returned as either XML or JSON.

### REst API Method Summary

Some methods require {id} as part of the URL. This is derived from the shipmentId returned from the Create Shipment API. In all Methods the Server Name must be inserted.

| Method | URI | Method | Description |
| ----- | ----- | :---: | ----- |
| Create Shipment | http://{ServerName}/Shipment | POST | Duplicates the functionality of creating a SmartLabel return label while also scheduling a free carrier pickup through USPS. |
| Cancel Pickup | http://{ServerName}/Shipment /{id}/CancelPickup | POST | Provides a method for cancelling a previously scheduled pickup |
| Get Label Image | http://{ServerName}/Shipment /{id}/Label/Image | GET | Gets a label image for printing |
| Request Pickup (without Label Creation) | http://{ServerName}/Shipment /{id}/RequestPickup | POST | Provides a method for scheduling a returns pickup with USPS |
| Tracking | http://{ServerName}/Shipment /Tracking | POST | Provides an API for a web client to track one or more forward or reverse packages in the Newgistics network. |

## Header Information

One API key is assigned to each merchant.  This header is used for all API request types.

| Shipment Request Header |  |
| ----- | :---- |
| **User-Agent** | Fiddler |
| **Content-type** | application/json; charset=utf-8 |
| **x-API-Key** | 26e94273-d9c5-43f0-a6ca-036048251040 |

## Create Shipment

### Shipment Summary

| Method | POST |
| :---- | :---- |
| **URI** | http://{ServerName}/Shipment |

### Shipment Request XML/JSON 

| XML Request  | JSON Request |
| :---- | :---- |
| \<ShipmentRequestData xmlns="http://schemas.datacontract.org/2004/07/Newgistics.WebServices.ShipmentAPI"\>   \<Transporter\>     \<Carrier\>String content\</Carrier\>     \<ClassOfService\>String content\</ClassOfService\>     \<TransporterCode\>String content\</TransporterCode\>   \</Transporter\>   \<additionalData\>     \<NameValue\>       \<Name\>String content\</Name\>       \<Value\>String content\</Value\>     \</NameValue\>     \<NameValue\>       \<Name\>String content\</Name\>       \<Value\>String content\</Value\>     \</NameValue\>   \</additionalData\>   \<clientServiceFlag\>String content\</clientServiceFlag\>   \<consumer\>     \<Address\>       \<Address1\>String content\</Address1\>       \<Address2\>String content\</Address2\>       \<Address3\>String content\</Address3\>       \<City\>String content\</City\>       \<CountryCode\>String content\</CountryCode\>       \<Name\>String content\</Name\>       \<State\>String content\</State\>       \<Zip\>String content\</Zip\>     \</Address\>     \<DaytimePhoneNumber\>String content\</DaytimePhoneNumber\>     \<EmailOptInFlag\>String content\</EmailOptInFlag\>     \<EveningPhoneNumber\>String content\</EveningPhoneNumber\>     \<FaxNumber\>String content\</FaxNumber\>     \<FirstName\>String content\</FirstName\>     \<Honorific\>String content\</Honorific\>     \<LastName\>String content\</LastName\>     \<MiddleInitial\>String content\</MiddleInitial\>     \<PrimaryEmailAddress\>String content\</PrimaryEmailAddress\>     \<SecondaryEmailAddress\>String content\</SecondaryEmailAddress\>   \</consumer\>   \<deliveryMethod\>String content\</deliveryMethod\>   \<destination\>     \<Address1\>String content\</Address1\>     \<Address2\>String content\</Address2\>     \<Address3\>String content\</Address3\>     \<City\>String content\</City\>     \<CountryCode\>String content\</CountryCode\>     \<Name\>String content\</Name\>     \<State\>String content\</State\>     \<Zip\>String content\</Zip\>   \</destination\>   \<dispositionRuleSetId\>2147483647\</dispositionRuleSetId\>   \<labelCount\>2147483647\</labelCount\>   \<merchantID\>String content\</merchantID\> \<pickupRequest\>     \<packageCount\>2147483647\</packageCount\>     \<pickupAfter\>1999-05-31T11:20:00\</pickupAfter\>     \<pickupBefore\>1999-05-31T11:20:00\</pickupBefore\>     \<pickupDate\>1999-05-31T11:20:00\</pickupDate\>     \<remarks\>String content\</remarks\>     \<totalWeight\>12678967.543233\</totalWeight\>   \</pickupRequest\>   \<returnId\>String content\</returnId\>   \<userType\>String content\</userType\>  | The following is an example request Json body:  { 	"Transporter":{ 		"Carrier":"String content", 		"ClassOfService":"String content", 		"TransporterCode":"String content" 	}, 	"additionalData":\[{ 		"Name":"String content", 		"Value":"String content" 	}\], 	"clientServiceFlag":"String content", 	"consumer":{ 		"Address":{ 			"Address1":"String content", 			"Address2":"String content", 			"Address3":"String content", 			"City":"String content", 			"CountryCode":"String content", 			"Name":"String content", 			"State":"String content", 			"Zip":"String content" 		}, 		"DaytimePhoneNumber":"String content", 		"EmailOptInFlag":"String content", 		"EveningPhoneNumber":"String content", 		"FaxNumber":"String content", 		"FirstName":"String content", 		"Honorific":"String content", 		"LastName":"String content", 		"MiddleInitial":"String content", 		"PrimaryEmailAddress":"String content", 		"SecondaryEmailAddress":"String content" 	}, 	"deliveryMethod":"String content", 	"destination":{ 		"Address1":"String content", 		"Address2":"String content", 		"Address3":"String content", 		"City":"String content", 		"CountryCode":"String content", 		"Name":"String content", 		"State":"String content", 		"Zip":"String content" 	}, 	"dispositionRuleSetId":2147483647, 	"labelCount":2147483647, 	"merchantID":"String content", 	"pickupRequest":{ 		"packageCount":2147483647, 		"pickupAfter":"\\/Date(928167600000-0500)\\/", 		"pickupBefore":"\\/Date(928167600000-0500)\\/", 		"pickupDate":"\\/Date(928167600000-0500)\\/", 		"remarks":"String content", 		"totalWeight":12678967.543233 	}, 	"returnId":"String content", 	"userType":"String content" } The following is an example response Xml body:    |

### Shipment Data Elements-Schema Information

| Complex Type Name/Element |  | Element |  | Null Allowed | Data Type | Description |
| :---- | :---- | :---- | :---- | :---: | :---- | :---- |
| Transporter |  |  |  | yes | **tns** | **TransporterType** |
|  |  | Carrier |  | yes | string | Name of transporter. Defaults to client configured transporter carrier. |
|  |  | ClassOfService |  | yes | string | Class of service used for this transporter. Defaults to client configured transporter class of service.  |
|  |  | TransporterCode |  | yes  | string | Code for the class of service used for this transporter. Defaults to client configured transporter code. |
| additionalData |  |  |  | yes | **tns** | **ArrayofNameValue** |
|  |  | NameValue |  | yes | **tns** | **ArrayofNameValue** Names and values of any other client data fields to include in the SmartLabel barcode if appropriate. Additional data may be  added during implementation. |
|  |  |  | Value | yes | string | Value (Namespace Specific String) |
|  |  |  | Name | yes | string | Qualifier (Namespace Specific Qualifier) |
| clientServiceFlag |  |  |  | yes | string |  |
| Consumer |  |  |  | no  | string | Name of transporter. Defaults to client configured transporter carrier. |
|  |  | Address |  |  |  |  |
|  |  |  | Address 1 | no | string | Consumer’s address line 1  |
|  |  |  | Address 2 | yes | string | Consumer’s address line 2  |
|  |  |  | City | no | string | Consumer’s city  |
|  |  |  | Country Code | yes | string | Consumer’s 2 digit Country Code |
|  |  |  | Name | yes | string | Consumer’s Country Name |
|  |  |  | State | no | string | Consumer’s state code  |
|  |  |  | Zip | no | string | Consumer’s postal code  |
|  |  | DayTimePhoneNumber |  | yes | string | Consumer’s day time phone number |
|  |  | EmailOptInflag |  | no | string | Consumer’s email will be included |
|  |  | EveningPhoneNumber |  | no | string | Consumer’s day time phone number |
|  |  | FaxNumber |  | no | string | Consumer’s fax number |
|  |  | FirstName |  | no | string | The first name of the consumer |
|  |  | Honorific |  | no | string | Prefix or Suffix for consumer’s name  |
|  |  | LastName |  | no | string | The last name of the consumer |
|  |  | MiddleInitial |  | no | string | Consumer’s middle initial |
|  |  | PrimaryEmailAddress  |  | no | string | The primary email address of the consumer |
|  |  | SecondaryEmailAddress |  | no | string | The secondary email address of the consumer |
| DeliveryMethod |  |  |  | no | string | Label delivery method being requested. The delivery method defaults to self-service. If any other method is selected, the label images are not returned in the response.  String values: Email  Print and Mail  Self Service |
| destination |  |  |  | yes | **tns** | AddressData |
|  | Address1 |  |  | yes | string | Destination street address |
|  | Address2 |  |  | yes | string | Destination street address additional information |
|  | Address3 |  |  | yes | string | Destination street address additional information |
|  | City |  |  | yes | string | Destination City |
|  | CountryCode |  |  | yes | string | Destination Country 2-digit code |
|  | Name |  |  | yes | string | Destination country name |
|  | State |  |  | yes | string | Destination state |
|  | Zip |  |  | yes | string | Destination postal code |
| DispositionRuleSerId |  |  |  | yes | integer | DispositionRuleSet to use in determining the DispositionSort. If not provided, the Merchant default is used. |
| LabelCount |  |  |  | yes | integer | Number of labels being requested. The number must be between 0 and 9\. The count defaults to 1\.  Note: This will generate copies of the same label with the same return ID. For unique return IDs, multiple calls should be made with a label count of 1\. |
| MerchantId |  |  |  | no | string | Four-character NGSMerchantID, used to indicate which client brand the request is for. |
| pickupRequest |  |  |  | yes | **tns** | PickupRequestData |
|  |  | packageCount |  | yes | integer | Number of packages to be picked up dup |
|  |  | pickupAfter |  | yes | dateTime | The earliest time that packages can be picked up  Format: yyyy-mm-ddThh:mm:ss |
|  |  | pickupBefore |  | yes | dateTime | The latest time that packages can be picked up Format: yyyy-mm-ddThh:mm:ss |
|  |  | pickupDate |  | yes | dateTime | The date of package pick up Format: yyyy-mm-ddThh:mm:ss |
|  |  | remarks |  | yes | string | Additional pick up information (directions, gate codes, etc.) |
|  |  | totalWeight |  | yes | decimal | Weight of all packages being picked up |
| ReturnId |  |  |  | yes | string | ReturnID to use in the Label client data. If a ReturnID is not provided here, a merchant-specific progressive number is used.  |
| userType |  |  |  | yes | string | Client, customer or other end-user for which the labels are being generated. |

| Shipment Request Example |
| :---- |

{  
                "consumer":{  
                                "Address":{  
                                                "Address1":"2700",  
                                                "City":"Austin",  
                                                "CountryCode":"US",  
                                                "State":"TX",  
                                                "Zip":"78746"  
                                },  
                                "FirstName":"Test",  
                                "LastName":"User",  
                                "PrimaryEmailAddress":"[nobody@newgistics.com](mailto:nobody@newgistics.com)"  
                },  
                "deliveryMethod":"Email",  
                "dispositionRuleSetId":99,  
                "labelCount":1,  
                "merchantID":"NGST",  
                "returnId":"123456789A"  
}  
Delivery Unit","TransporterCode":"5"}}

### Shipment Response

| XML Request Response | JSON Request Response |
| :---- | :---- |
| \<ShipmentRequestResponse xmlns="http://schemas.datacontract.org/2004/07/Newgistics.WebServices.ShipmentAPI"\>   \<PrimaryBarcode\>String content\</PrimaryBarcode\>   \<ShipmentID\>String content\</ShipmentID\>   \<generalCharge\>     \<BaseRate\>12678967.543233\</BaseRate\>     \<CurrencyCode\>String content\</CurrencyCode\>     \<Discount\>12678967.543233\</Discount\>     \<Fees\>12678967.543233\</Fees\>     \<RateCategory\>String content\</RateCategory\>   \</generalCharge\>   \<labelURL\>String content\</labelURL\>   \<perPackageCharges\>     \<ReturnChargeType\>       \<BaseRate\>12678967.543233\</BaseRate\>       \<CurrencyCode\>String content\</CurrencyCode\>       \<Discount\>12678967.543233\</Discount\>       \<Fees\>12678967.543233\</Fees\>       \<RateCategory\>String content\</RateCategory\>     \</ReturnChargeType\>     \<ReturnChargeType\>       \<BaseRate\>12678967.543233\</BaseRate\>       \<CurrencyCode\>String content\</CurrencyCode\>       \<Discount\>12678967.543233\</Discount\>       \<Fees\>12678967.543233\</Fees\>       \<RateCategory\>String content\</RateCategory\>     \</ReturnChargeType\>   \</perPackageCharges\>   \<transporter\>     \<Carrier\>String content\</Carrier\>     \<ClassOfService\>String content\</ClassOfService\>     \<TransporterCode\>String content\</TransporterCode\>   \</transporter\> \</ShipmentRequestResponse\> | { 	"PrimaryBarcode":"String content", 	"ShipmentID":"String content", 	"generalCharge":{ 		"BaseRate":12678967.543233, 		"CurrencyCode":"String content", 		"Discount":12678967.543233, 		"Fees":12678967.543233, 		"RateCategory":"String content" 	}, 	"labelURL":"String content", 	"perPackageCharges":\[{ 		"BaseRate":12678967.543233, 		"CurrencyCode":"String content", 		"Discount":12678967.543233, 		"Fees":12678967.543233, 		"RateCategory":"String content" 	}\], 	"transporter":{ 		"Carrier":"String content", 		"ClassOfService":"String content", 		"TransporterCode":"String content" 	} }  |

   ### Shipment Response Data Elements-Schema Information

| Element |  | Properties |  | Null Allowed | Data Type | Description |
| :---- | :---- | :---- | :---- | :---: | :---: | :---- |
| primaryBarcode |  |  |  | yes | string | Primary barcode is the Smartlabel barcode provided by Newgistics |
| shipmentID |  |  |  | yes | string | This is the identifier the client uses in all methods ({id} in the URL).  It identifies the shipment/label. |
| generalCharge |  |  |  | yes | tns | **ReturnChargeType** Merchant-specified general charge for the return if the merchant defines a charge. |
|  |  | baseRate |  | no | decimal | The per package contracted rate  |
|  |  | currencyCode |  | yes | sting | Type of currency (i.e. USD) |
|  |  | discount |  | no | decimal | Amount of any contracted discount |
|  |  | fees |  | no | decimal | Amount of any additional fees |
|  |  | rateCategory |  | yes | string | Not applicable to REst APIs |
| labelURL |  |  |  | yes | string | Contains the URLs that can be referenced to load the label image from the Newgistics Shipment Manager web application |
| perPackageCharges |  |  |  | yes | tns | **ArrayOfReturnChargeType**  Merchant charge per package if the merchant defines a charge. |
|  | \*returnChargeType (multiple instances) |  |  | yes | tns | **ReturnChargeType** Merchant-specified general charge for the return if the merchant defines a charge. |
|  |  |  | baseRate | no | decimal | The per package contracted rate  |
|  |  |  | currencyCode | yes | sting | Type of currency (i.e. USD) |
|  |  |  | discount | no | decimal | Amount of any contracted discount |
|  |  |  | fees | no | decimal | Amount of any additional fees |
|  |  |  | rateCategory | yes | string |  |
| transporter |  |  |  | yes | string | **TransporterType** Carrier SCAC and carrier class-of-service for which the labels were generated. This is either as determined by the rules or as specified in the request. |
|  |  | Carrier |  | yes | string | Name of transporter. Defaults to client configured transporter carrier. |
|  |  | ClassOfServic |  | yes | string | Class of service used for this transporter. Defaults to client configured transporter class of service. |
|  |  | TransporterCode |  | yes | string | Code for the class of service used for this transporter. Defaults to client configured transporter code. |

| Shipment Response Example |
| :---- |
| {"PrimaryBarcode":"7051078799NGST01123456789AY","ShipmentID":"99387D55E973FBA71A5A60A8DF2A97151008F4C625BC80BF","generalCharge":null,"labelURL":"http:\\/\\/returnscenter.int.smartlabel.com\\/v3\\/PrintWebLabel.aspx?weblabelid=FA3F1D16CCBDA16C79B76F938278B08D094727EB0DF2FB80","perPackageCharges":null,"transporter":{"Carrier":"USPS","ClassOfService":"USPS Return Delivery Unit","TransporterCode":"5"}} |

      1. ### **Shipment Responses** {#shipment-responses}

| Property | 401 Status when API Key is missing or invalid | Response for invalid data | Label Request Response (raw) |
| :---- | :---- | :---- | :---- |
| **Cache-Control:**  | private | private | private |
| **Content-Length:**  | 338 | 40 | 397 |
| **Content-Type:**  | text/html or | application/json; charset=utf-8 | application/json; charset=utf-8 |
| **Server:**  | Microsoft-IIS/7.5 | Microsoft-IIS/7.5 | Microsoft-IIS/7.5 |
| **X-AspNet-Version:**  | 4.0.30319 | 4.0.30319 |  4.0.30319 |
| **X-Powered-By:**  | ASP.NET |  ASP.NET | ASP.NET |
| **Date** | Fri, 17 Aug 2012 18:24:43 GMT | Fri, 17 Aug 2012 18:19:23 GMT |  |
| **Message** | A valid API key needs to be included using the x-API-Key HTTP Header | "ER1016:Zip code is missing or invalid;" |  |
| **Html Sample** | \<html\>\<head\>\<title\>Request Error \- No API Key\</title\>\<style type="text/css"\>         body         {             font-family: Verdana;             font-size: large;         }     \</style\>\</head\>\<body\>\<h1\>         Request Error     \</h1\>\<p\>         A valid API key needs to be included using the x-API-Key HTTP Header     \</p\>\</body\>\</html\> |  | {"PrimaryBarcode":"7051078799NGST01123456789AY","ShipmentID":"99387D55E973FBA71A5A60A8DF2A97151008F4C625BC80BF","generalCharge":null,"labelURL":"http:\\/\\/returnscenter.int.smartlabel.com\\/v3\\/PrintWebLabel.aspx?weblabelid=FA3F1D16CCBDA16C79B76F938278B08D094727EB0DF2FB80","perPackageCharges":null,"transporter":{"Carrier":"USPS","ClassOfService":"USPS Return Delivery Unit","TransporterCode":"5"}} |

## Cancel Pickup

### Cancel Pickup Summary

| Method | POST |
| :---- | :---- |
| **URI** | http://{ServerName}/Shipment /{id}/CancelPickup |

### Cancel Pickup Request XML/JSON

| XML Request  | JSON Request |
| :---- | :---- |
| \<CancelPickupRequestData xmlns="http://schemas.datacontract.org/2004/07/Newgistics.WebServices.ShipmentAPI"\>   \<confirmationNumber\>String content\</confirmationNumber\>   \<merchantID\>String content\</merchantID\>   \<postalCode\>String content\</postalCode\>   \<remarks\>String content\</remarks\>   \<shipmentID\>String content\</shipmentID\>   \<userType\>String content\</userType\> \</CancelPickupRequestData\> | { 	"confirmationNumber":"String content", 	"merchnatID":"String content", 	"postalCode":"String content", 	"remarks":"String content", 	"shipmentID":"String content", 	"userType":"String content" } |

### Cancel Pickup Data Elements-Schema Information

| Element | Null Allowed | Data Type | Description |
| :---- | :---: | :---: | :---- |
| confirmationNumber | yes | string | Reference number confirming the cancellation |
| merchantID | yes | string | Four-character NGSMerchantID, used to indicate which client brand the request is for. |
| postalCode | yes | string | Zip code of the cancelled pickup |
| remarks | yes | string | Reason of cancellation |
| shipmentID | yes | string | This is the identifier the client uses in all methods ({id} in the URL).  It identifies the shipment/label. |
| userType | yes | string | Client, customer or other end-user for which the labels are being generated. |

### Cancel Pickup Response XML/JSON

| XML Request  | JSON Request |
| :---- | :---- |
| \<boolean xmlns="http://schemas.microsoft.com/2003/10/Serialization/"\>true\</boolean\> | true |

### Cancel Pickup Response Data Elements-Schema Information

| Element | Null Allowed | Data Type | Description |
| :---- | :---: | :---- | :---- |
| boolean | yes | boolean | The status of the cancellation request. True or error returned. |

## Get Label Image

### Create Label Summary

| Method | GET |
| :---- | :---- |
| **URI** | http://{ServerName}/Shipment /{id}/Label/Image |

### Get Label Request XML/JSON

| XML Request  | JSON Request |
| ----- | :---- |
| The Request body is empty |  |

### Get Label Response XML/JSON

| XML Request  | JSON Request |
| ----- | :---- |
| The Response body is a byte stream |  |

### Get Label Response Properties

## Request Pickup (without Label Creation

### Request Pickup Summary

| Method | POST |
| :---- | :---- |
| **URI** | http://{ServerName}/Shipment /{id}/RequestPickup |

### Request Pickup Request XML/JSON

| XML Request  | JSON Request |
| :---- | :---- |
| \<PickupRequestData xmlns="http://schemas.datacontract.org/2004/07/Newgistics.WebServices.ShipmentAPI"\>   \<packageCount\>2147483647\</packageCount\>   \<pickupAfter\>1999-05-31T11:20:00\</pickupAfter\>   \<pickupBefore\>1999-05-31T11:20:00\</pickupBefore\>   \<pickupDate\>1999-05-31T11:20:00\</pickupDate\>   \<remarks\>String content\</remarks\>   \<totalWeight\>12678967.543233\</totalWeight\> \</PickupRequestData\> | { 	"packageCount":2147483647, 	"pickupAfter":"\\/Date(928167600000-0500)\\/", 	"pickupBefore":"\\/Date(928167600000-0500)\\/", 	"pickupDate":"\\/Date(928167600000-0500)\\/", 	"remarks":"String content", 	"totalWeight":12678967.543233 } |

### Request Pickup Data Elements-Schema Information

| Element | Null Allowed | Data Type | Description |
| :---- | :---: | :---- | :---- |
| packageCount | yes | integer | Number of packages to be picked up dup |
| pickupAfter | yes | dateTime | The earliest time that packages can be picked up  Format: yyyy-mm-ddThh:mm:ss |
| pickupBefore | yes | dateTime | The latest time that packages can be picked up Format: yyyy-mm-ddThh:mm:ss |
| pickupDate | yes | dateTime | The date of package pick up Format: yyyy-mm-ddThh:mm:ss |
| remarks | yes | string | Additional pick up information (directions, gate codes, etc.) |
| totalWeight | yes | decimal | Weight of all packages being picked up |

### Request Pickup Response XML/JSON*

| XML Request  | JSON Request |
| :---- | :---- |
| \<PickupRequestResponse xmlns="http://schemas.datacontract.org/2004/07/Newgistics.WebServices.ShipmentAPI"\>   \<carrierConfirmationNumber\>String content\</carrierConfirmationNumber\>   \<confirmationNumber\>String content\</confirmationNumber\> \</PickupRequestResponse\> | { 	"carrierConfirmationNumber":"String content", 	"confirmationNumber":"String content" } |

### Request Pickup Data Elements-Schema Information

| Element | Null allowed | Data Type | Description |
| :---- | :---: | :---- | :---- |
| carrierConfirmationNumber | yes | string | The confirmation number of the pickup request provided by The carrier (USPS) |
| confirmationNumber | yes | String | The confirmation number of the pickup request provided by Newgistics |

### **Request Pickup Response Properties** {#request-pickup-response-properties}

## Tracking

### Tracking Summary

| Method | POST |
| :---- | :---- |
| **URI** | http://{ServerName}/Shipment /Tracking |

### Tracking Request XML/JSON

| XML Request  | JSON Request |
| :---- | :---- |
| \<TrackingRequestData xmlns="http://schemas.datacontract.org/2004/07/Newgistics.WebServices.ShipmentAPI"\>   \<merchantID\>String content\</merchantID\>   \<qualifier\>String content\</qualifier\>   \<searchStrings\>     \<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays"\>String content\</string\>     \<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays"\>String content\</string\>   \</searchStrings\> \</TrackingRequestData\> | { 	"merchantID":"String content", 	"qualifier":"String content", 	"searchStrings":\["String content"\] } |

### Tracking Data Elements-Schema Information

| Element | Null Allowed | Data Type | Description |
| :---- | :---: | :---- | :---- |
| merchantID | yes | String | Four-character NGSMerchantID, used to indicate which client brand the request is for. |
| qualifier | yes | String | Discriminator indicating the type of search to perform  String Values: Barcode – PRS or SL barcode. Reference Number – Return ID or client supplied Reference Number for deliveries. Order Number – RMA order number. This is not the same number as the ReturnID as there can be multiple ReturnIDs per Order Number. ItemID – A specific RMA item in an Order Number. NGSTrackingID \= Newgistics specific tracking number. |
| search Strings | yes | String (array) | Search value used to find matching labels |

| Tracking Request Example |
| :---- |

{  
                "merchantID":"NGST", "qualifier":"Barcode",  
                "searchStrings":\["123456789A","11223344A"\]  
}

### Tracking Response XML/JSON

| XML Request  | JSON Request |
| :---- | :---- |
| \<TrackingResultData xmlns="http://schemas.datacontract.org/2004/07/Newgistics.WebServices.ShipmentAPI"\>   \<Packages\>     \<PackageTrackingData\>       \<CarrierCode\>String content\</CarrierCode\>       \<CarrierCodeDescription\>String content\</CarrierCodeDescription\>       \<CarrierName\>String content\</CarrierName\>       \<CarrierService\>String content\</CarrierService\>       \<CarrierServiceCode\>String content\</CarrierServiceCode\>       \<CarrierServiceCodeDescription\>String content\</CarrierServiceCodeDescription\>       \<ErrorMessage\>String content\</ErrorMessage\>       \<EstimatedDeliveryDate\>1999-05-31T11:20:00\</EstimatedDeliveryDate\>       \<EstimatedDeliveryText\>String content\</EstimatedDeliveryText\>       \<FinalCarrier\>String content\</FinalCarrier\>       \<MerchantName\>String content\</MerchantName\>       \<PackageTrackingEvents\>         \<PackageTrackingEvent\>           \<CSREventMessage\>String content\</CSREventMessage\>           \<CarrierCode\>String content\</CarrierCode\>           \<CarrierDescription\>String content\</CarrierDescription\>           \<City\>String content\</City\>           \<ConsumerEventMessage\>String content\</ConsumerEventMessage\>           \<CreateDate\>1999-05-31T11:20:00\</CreateDate\>           \<Date\>1999-05-31T11:20:00\</Date\>           \<Description\>String content\</Description\>           \<EventCode\>String content\</EventCode\>           \<EventDescription\>String content\</EventDescription\>           \<FacilityID\>2147483647\</FacilityID\>           \<FacilityName\>String content\</FacilityName\>           \<PostalCode\>String content\</PostalCode\>           \<State\>String content\</State\>           \<Time\>1999-05-31T11:20:00\</Time\>           \<TrackingKey\>String content\</TrackingKey\>           \<UpdateDate\>1999-05-31T11:20:00\</UpdateDate\>         \</PackageTrackingEvent\>         \<PackageTrackingEvent\>           \<CSREventMessage\>String content\</CSREventMessage\>           \<CarrierCode\>String content\</CarrierCode\>           \<CarrierDescription\>String content\</CarrierDescription\>           \<City\>String content\</City\>           \<ConsumerEventMessage\>String content\</ConsumerEventMessage\>           \<CreateDate\>1999-05-31T11:20:00\</CreateDate\>           \<Date\>1999-05-31T11:20:00\</Date\>           \<Description\>String content\</Description\>           \<EventCode\>String content\</EventCode\>           \<EventDescription\>String content\</EventDescription\>           \<FacilityID\>2147483647\</FacilityID\>           \<FacilityName\>String content\</FacilityName\>           \<PostalCode\>String content\</PostalCode\>           \<State\>String content\</State\>           \<Time\>1999-05-31T11:20:00\</Time\>           \<TrackingKey\>String content\</TrackingKey\>           \<UpdateDate\>1999-05-31T11:20:00\</UpdateDate\>         \</PackageTrackingEvent\>       \</PackageTrackingEvents\>       \<ReferenceNumber\>String content\</ReferenceNumber\>       \<ShipToAddressLine1\>String content\</ShipToAddressLine1\>       \<ShipToAddressLine2\>String content\</ShipToAddressLine2\>       \<ShipToCity\>String content\</ShipToCity\>       \<ShipToName\>String content\</ShipToName\>       \<ShipToPostalCode\>String content\</ShipToPostalCode\>       \<ShipToState\>String content\</ShipToState\>       \<Signer\>String content\</Signer\>       \<Status\>String content\</Status\>       \<TrackingNumber\>String content\</TrackingNumber\>       \<UnitOfMeasure\>String content\</UnitOfMeasure\>       \<Weight\>12678967.543233\</Weight\>     \</PackageTrackingData\>     \<PackageTrackingData\>       \<CarrierCode\>String content\</CarrierCode\>       \<CarrierCodeDescription\>String content\</CarrierCodeDescription\>       \<CarrierName\>String content\</CarrierName\>       \<CarrierService\>String content\</CarrierService\>       \<CarrierServiceCode\>String content\</CarrierServiceCode\>       \<CarrierServiceCodeDescription\>String content\</CarrierServiceCodeDescription\>       \<ErrorMessage\>String content\</ErrorMessage\>       \<EstimatedDeliveryDate\>1999-05-31T11:20:00\</EstimatedDeliveryDate\>       \<EstimatedDeliveryText\>String content\</EstimatedDeliveryText\>       \<FinalCarrier\>String content\</FinalCarrier\>       \<MerchantName\>String content\</MerchantName\>       \<PackageTrackingEvents\>         \<PackageTrackingEvent\>           \<CSREventMessage\>String content\</CSREventMessage\>           \<CarrierCode\>String content\</CarrierCode\>           \<CarrierDescription\>String content\</CarrierDescription\>           \<City\>String content\</City\>           \<ConsumerEventMessage\>String content\</ConsumerEventMessage\>           \<CreateDate\>1999-05-31T11:20:00\</CreateDate\>           \<Date\>1999-05-31T11:20:00\</Date\>           \<Description\>String content\</Description\>           \<EventCode\>String content\</EventCode\>           \<EventDescription\>String content\</EventDescription\>           \<FacilityID\>2147483647\</FacilityID\>           \<FacilityName\>String content\</FacilityName\>           \<PostalCode\>String content\</PostalCode\>           \<State\>String content\</State\>           \<Time\>1999-05-31T11:20:00\</Time\>           \<TrackingKey\>String content\</TrackingKey\>           \<UpdateDate\>1999-05-31T11:20:00\</UpdateDate\>         \</PackageTrackingEvent\>         \<PackageTrackingEvent\>           \<CSREventMessage\>String content\</CSREventMessage\>           \<CarrierCode\>String content\</CarrierCode\>           \<CarrierDescription\>String content\</CarrierDescription\>           \<City\>String content\</City\>           \<ConsumerEventMessage\>String content\</ConsumerEventMessage\>           \<CreateDate\>1999-05-31T11:20:00\</CreateDate\>           \<Date\>1999-05-31T11:20:00\</Date\>           \<Description\>String content\</Description\>           \<EventCode\>String content\</EventCode\>           \<EventDescription\>String content\</EventDescription\>           \<FacilityID\>2147483647\</FacilityID\>           \<FacilityName\>String content\</FacilityName\>           \<PostalCode\>String content\</PostalCode\>           \<State\>String content\</State\>           \<Time\>1999-05-31T11:20:00\</Time\>           \<TrackingKey\>String content\</TrackingKey\>           \<UpdateDate\>1999-05-31T11:20:00\</UpdateDate\>         \</PackageTrackingEvent\>       \</PackageTrackingEvents\>       \<ReferenceNumber\>String content\</ReferenceNumber\>       \<ShipToAddressLine1\>String content\</ShipToAddressLine1\>       \<ShipToAddressLine2\>String content\</ShipToAddressLine2\>       \<ShipToCity\>String content\</ShipToCity\>       \<ShipToName\>String content\</ShipToName\>       \<ShipToPostalCode\>String content\</ShipToPostalCode\>       \<ShipToState\>String content\</ShipToState\>       \<Signer\>String content\</Signer\>       \<Status\>String content\</Status\>       \<TrackingNumber\>String content\</TrackingNumber\>       \<UnitOfMeasure\>String content\</UnitOfMeasure\>       \<Weight\>12678967.543233\</Weight\>     \</PackageTrackingData\>   \</Packages\> \</TrackingResultData\> | { 	"Packages":\[{ 		"CarrierCode":"String content", 		"CarrierCodeDescription":"String content", 		"CarrierName":"String content", 		"CarrierService":"String content", 		"CarrierServiceCode":"String content", 		"CarrierServiceCodeDescription":"String content", 		"ErrorMessage":"String content", 		"EstimatedDeliveryDate":"\\/Date(928167600000-0500)\\/", 		"EstimatedDeliveryText":"String content", 		"FinalCarrier":"String content", 		"MerchantName":"String content", 		"PackageTrackingEvents":\[{ 			"CSREventMessage":"String content", 			"CarrierCode":"String content", 			"CarrierDescription":"String content", 			"City":"String content", 			"ConsumerEventMessage":"String content", 			"CreateDate":"\\/Date(928167600000-0500)\\/", 			"Date":"\\/Date(928167600000-0500)\\/", 			"Description":"String content", 			"EventCode":"String content", 			"EventDescription":"String content", 			"FacilityID":2147483647, 			"FacilityName":"String content", 			"PostalCode":"String content", 			"State":"String content", 			"Time":"\\/Date(928167600000-0500)\\/", 			"TrackingKey":"String content", 			"UpdateDate":"\\/Date(928167600000-0500)\\/" 		}\], 		"ReferenceNumber":"String content", 		"ShipToAddressLine1":"String content", 		"ShipToAddressLine2":"String content", 		"ShipToCity":"String content", 		"ShipToName":"String content", 		"ShipToPostalCode":"String content", 		"ShipToState":"String content", 		"Signer":"String content", 		"Status":"String content", 		"TrackingNumber":"String content", 		"UnitOfMeasure":"String content", 		"Weight":12678967.543233 	}\] } |

### Tracking Data Elements-Schema Information

| Element | Properties  |  |  | Null allowed | Data Type | Description |
| :---- | ----- | :---- | :---- | :---: | :---- | :---- |
| **Packages** |  |  |  | yes | tns | **Array of Package Tracking Data** |
|  | **\*PackagetrackingData  (multiple instances)** |  |  | yes | tns | **Array of Package Tracking Data** |
|  |   | CarrierCode |  | yes | string | The carrier supplied code for the tracking event |
|  |  | CarrierCodeDescription |  | yes | string | The carrier supplied description for the tracking event |
|  |  | CarrierName |  | yes | string | The name of the merchant from whom the package originated |
|  |  | CarrierService |  | yes | string | The name of the service of the company carrying the package |
|  |  | CarrierServiceCodeDescription |  | yes | string | The Newgistics assigned identifier for the package service  |
|  |  | ErrorMessage |  | yes | string | A message indicating a transmission or data acquisition problem that interferes with the method |
|  |  | EstimatedDeliveryDate |  | yes | string | The calculated range of when a package will be delivered |
|  |  | EstimatedDeliveryText |  | yes | string | Comments/Text related to  the EDD |
|  |  | FinalCarrier |  | yes | string | The last carrier in the cycle; the one who delivers the package to its destination |
|  |  | MerchantName |  | yes | string | The name of the merchant from whom the package originated |
|  |  | \*PackageTrackingEvents  (multiple instances) |  | yes | **tns** | **ArrayOfPackageTrackingEvent** The scan events that the package has experienced |
|  |  |  | CSREventMessage | yes | string | The message that indicated the nature of the event |
|  |  |  | CarrierCode | yes | string | The carrier supplied code for the tracking event |
|  |  |  | CarrierDescription | yes | string | The carrier supplied description for the tracking event |
|  |  |  | City | yes | string | The city in which the event occurred |
|  |  |  | ConsumerEventMessage | yes |  | The event message sent to the consumer  |
|  |  |  | CreateDate | no | dateTime | The date the event message is created |
|  |  |  | Date | no | dateTime | The date that the event occurred |
|  |  |  | Description | yes | string |  |
|  |  |  | EventCode | yes | string | The event code for the tracking event. See the table below for possible values. |
|  |  |  | EventDescription | yes | string | The description of the tracking event |
|  |  |  | FacilityID | no | string | The Newgistics identifier for the facility at which the event occurred |
|  |  |  | FacilityName | yes | string | The name of the facility at which the event occurred |
|  |  |  | PostalCode | yes | string | The postal zip code in which the event occurred |
|  |  |  | State | yes | string | The state in which the event occurred |
|  |  |  | Time | no | dateTime | The time that the event occurred |
|  |  |  | TrackingKey | yes | string | For Internal use only; links events back to packages |
|  |  |  | UpdateDate | no | string | The date that the event occurred |
|  |  | ReferenceNumber |  | yes | string | The package reference number |
|  |  | ShipToAddressLine1 |  | yes | string | The street address of the customer receiving the package |
|  |  | ShipToAddressLine2 |  | yes | string | Additional address information about the customer receiving the package |
|  |  | ShipToCity |  | yes | string | The city of the customer receiving the package |
|  |  | ShipToName |  | yes | string | The name of the customer receiving the package |
|  |  | ShipToPostalCode |  | yes | string | The postal code of the customer receiving the package |
|  |  | ShipToState |  | yes | string | The state of the customer receiving the package |
|  |  | Signer |  | yes | string | The name of the person who signed for the package delivery in the case of Signature Confirmation. |
|  |  | Status |  | yes | string | The status of the package String Values: Exception NotFound Unknown Created Received InTransit Delivered Departed InUSPSNetwork |
|  |  | TrackingNumber |  | yes | string | The package tracking number |
|  |  | UnitOfMeasure |  | yes | string | The units of the weight measure (Default-lbs) |
|  |  | Weight |  | yes | decimal | The weight of the package |
|  |  |  |  |  |  |  |
| **Tracking Response Example** |  |  |  |  |  |  |

HTTP/1.1 200 OK  
Cache-Control: private  
Content-Length: 58303  
**Content-Type: application/json; charset=utf-8**  
Server: Microsoft-IIS/7.5  
X-AspNet-Version: 4.0.30319  
X-Powered-By: ASP.NET  
Date: Fri, 17 Aug 2012 19:08:17 GMT

{"Packages":\[{"CarrierCode":"NEWG","CarrierCodeDescription":"Newgistics, Inc.","CarrierName":"United States Postal Service","CarrierService":"USPS Return Delivery Unit","CarrierServiceCode":null,"CarrierServiceCodeDescription":null,"ErrorMessage":"","EstimatedDeliveryDate":null,"EstimatedDeliveryText":null,"FinalCarrier":null,"MerchantName":null,"PackageTrackingEvents":\[{"CSREventMessage":"Label created","CarrierCode":"LC","CarrierDescription":"Label Created","City":"","ConsumerEventMessage":"Label created","CreateDate":"\\/Date(1343702575000-0500)\\/","Date":"\\/Date(1343624400000-0500)\\/","Description":"Label Created","EventCode":"LC","EventDescription":"Label Created","FacilityID":114,"FacilityName":"","PostalCode":"","State":"","Time":"\\/Date(1345242660000-0500)\\/","TrackingKey":"163298425","UpdateDate":"\\/Date(1343702575000-0500)\\/"}\],"ReferenceNumber":"123456789A","ShipToAddressLine1":"2700 Via Fortuna","ShipToAddressLine2":"Suite 300","ShipToCity":"Austin","ShipToName":"Austin \- Newgistics Test 44","ShipToPostalCode":"78746","ShipToState":"TX","Signer":null,"Status":"Unknown","TrackingNumber":"123456789A","UnitOfMeasure":"pounds","Weight":null}\]}

