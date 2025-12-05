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


#### Shipment Responses

| Property | 401 Status when API Key is missing or invalid | Response for invalid data | Label Request Response (raw) |
| :---- | :---- | :---- | :---- |
| **Cache-Control:**  | private | private | private |
| **Content-Length:**  | 338 | 40 | 397 |
| **Content-Type:**  | text/html or | application/json; charset=utf-8 | application/json; charset=utf-8 |
| **Server:**  | Microsoft-IIS/7.5 | Microsoft-IIS/7.5 | Microsoft-IIS/7.5 |
| **X-AspNet-Version:**  | 4.0.30319 | 4.0.30319 |  4.0.30319 |
| **X-Powered-By:**  | ASP.NET |  ASP.NET | ASP.NET |
| **Date** | Fri, 17 Aug 2012 18:24:43 GMT | Fri, 17 Aug 2012 18:19:23 GMT |  |
| **Message** | A valid API key needs to be included using the x-API-Key HTTP Header | "ER1016:Zip code is missing or invalid;" |

## Cancel Pickup

### Cancel Pickup Summary

| Method | POST |
| :---- | :---- |
| **URI** | http://{ServerName}/Shipment /{id}/CancelPickup |

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

### Tracking Data Elements-Schema Information

| Element | Null Allowed | Data Type | Description |
| :---- | :---: | :---- | :---- |
| merchantID | yes | String | Four-character NGSMerchantID, used to indicate which client brand the request is for. |
| qualifier | yes | String | Discriminator indicating the type of search to perform  String Values: Barcode – PRS or SL barcode. Reference Number – Return ID or client supplied Reference Number for deliveries. Order Number – RMA order number. This is not the same number as the ReturnID as there can be multiple ReturnIDs per Order Number. ItemID – A specific RMA item in an Order Number. NGSTrackingID \= Newgistics specific tracking number. |
| search Strings | yes | String (array) | Search value used to find matching labels |


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