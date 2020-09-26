# Transactions Parsers

# XML Name Spaces
XMLNS = {"poslog_ns": "http://www.nrf-arts.org/IXRetail/namespace/",
      "poslog_ns_ext": "http://schemas.vismaretail.com/poslog/"
}

# XML Parsing Functions
def retail_transaction_parser(transactionXMLElement):
    t = transactionXMLElement
    
    # Transaction Training Mode Flag
    try:
        trainingModeFlag = 0 + bool(t.attrib["TrainingModeFlag"])
    except KeyError as err:
        trainingModeFlag = 0
    
    # TransactionID
    transactionIDElement = t.find("poslog_ns:TransactionID", XMLNS)
    if (transactionIDElement is None):
        raise Exception ("Unable to find element: TransactionID.")    
    else:
        transactionID = transactionIDElement.text

    # UnitID
    unitIDElement = t.find(".//poslog_ns:UnitID", XMLNS)
    if (unitIDElement is None):
        raise Exception("Unable to find element: UnitID.")
    else:
        try:
            unitID = int(unitIDElement.text)
        except ValueError as err:
            raise err
    
    # WorkstationID
    workstationIDElement = t.find("poslog_ns:WorkstationID", XMLNS)
    if workstationIDElement is None:
        raise Exception("Unable to find element: WorkstationID.")
    else:
        try: 
            workstationID = int(workstationIDElement.text)
        except ValueError as err:
            raise err
        
    # SequenceID
    sequenceIDElement = t.find("poslog_ns:SequenceNumber", XMLNS)
    if sequenceIDElement is None:
        raise Exception("Unable to find element: SequenceNumber.")
    else:
        try:
            sequenceID = int(sequenceIDElement.text)
        except ValueError as err:
            raise err
    
    # Transaction StartDateTime
    startDTimeElement = t.find("poslog_ns:BeginDateTime", XMLNS)
    if startDTimeElement is None:
        raise Exception("Element not found: BeginDateTime")
    else:
        startDTime = startDTimeElement.text
        
    # Transaction EndDateTime
    endDTimeElement = t.find("poslog_ns:EndDateTime", XMLNS)
    if endDTimeElement is None:
        raise Exception("Element not found: EndDateTime")
    else:
        endDTime = endDTimeElement.text
    
    # Currency
    currencyCodeElement = t.find("poslog_ns:CurrencyCode", XMLNS)
    if currencyCodeElement is None:
        raise Exception("Unable to find element: CurrencyCode.")
    else:
        currency = currencyCodeElement.text
    
    # Quantity    
    quantityElement = t.find(".//poslog_ns:Quantity", XMLNS)
    if (quantityElement is None):
        raise Exception("Unable to find element: Quantity.")    
    else:
        try:
            quantity = float(quantityElement.text)
        except ValueError as err:
            raise err
        
    ### ExtendedAmount
    extendedAmountElement = t.find(".//poslog_ns:ExtendedAmount", XMLNS)
    if (extendedAmountElement is None):
        raise Exception("Unable to find Element:ExtendedAmount", XMLNS)
    else:
        try:
            extendedAmount = float(extendedAmountElement.text)
        except ValueError as err:
            raise err

    ### TransactionNetAmount
    transactionNetAmountElement = t.find(".//poslog_ns:Total[@TotalType='TransactionNetAmount']", XMLNS)
    try:
        transactionNetAmount = float(transactionNetAmountElement.text) 
    except:
        transactionNetAmount = None     
    
    transaction = {"TransactionID":transactionID,
                   "UnitID":unitID,
                   "WorkstationID":workstationID,
                   "SequenceNumber":sequenceID,
                   "BeginDateTime":startDTime,
                   "EndDateTime":endDTime,
                   "CurrencyCode":currency,
                   "TrainingModeFlag":trainingModeFlag,
                   "Quantity":quantity,
                   "ExtendedAmount":extendedAmount,
                   "TransactionNetAmount":transactionNetAmount
        }
    return transaction
    
