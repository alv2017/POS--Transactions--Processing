from datetime import datetime

class RetailTransaction:
    def __init__(self, transaction_id,
                 unit_id, 
                 workstation_id,
                 sequence_id,
                 start_dtime, 
                 end_dtime,
                 currency,
                 training_mode_flag,
                 quantity,
                 extended_amount,
                 transaction_net_amount
            ):
        
        self.id = self.set_transaction_id(transaction_id)
        self.unit_id = self.set_id(unit_id)
        self.workstation_id = self.set_id(workstation_id)
        self.sequence_id = self.set_id(sequence_id)
        self.start_dtime = self.set_datetime(start_dtime)
        self.end_dtime = self.set_datetime(end_dtime)
        self.currency = self.set_currency(currency)
        self.training_mode_flag = self.set_mode(training_mode_flag)
        
        self.quantity = self.set_amount(quantity)
        self.extended_amount = self.set_amount(extended_amount)
        self.transaction_net_amount = self.set_amount(transaction_net_amount)
    
    def set_transaction_id(self, id):
        try:
            int(id)
            return str(id)
        except ValueError as err:
            raise err
        
    def set_id(self, id):
        try:
            numeric_id = int(id)
            return numeric_id
        except ValueError as err:
            raise err
        
    def set_datetime(self, dt_string):
        try:
            dt = datetime.strptime(dt_string, "%Y-%m-%dT%H:%M:%S")
            return dt 
        except ValueError as err:
            raise err
        
    def set_currency(self, code):
        return code
    
    def set_amount(self, value):
        try:
            amount = float(value)
            return amount
        except (TypeError, ValueError):
            amount = None
    
    def set_mode(self, mode): 
        try:
            m = int(mode) 
            if (m in (0,1)):
                return m
            else:
                raise ValueError("ValueError: Mode can be equal to 0 or 1.")
        except ValueError as err:
            raise err
    
    def toDictionary(self):
        return {
            "TransactionID":self.id,
            "UnitID":self.unit_id,
            "WorkstationID":self.workstation_id,
            "SequenceNumber":self.sequence_id,
            "BeginDateTime":self.start_dtime,
            "EndDateTime":self.end_dtime,
            "CurrencyCode":self.currency,
            "TrainingModeFlag":self.training_mode_flag,  
            "Quantity":self.quantity,
            "ExtendedAmount":self.extended_amount,
            "TransactionNetAmount":self.transaction_net_amount          
        }  
        
    def __str__(self):
        s = ""
        for key,value in self.toDictionary().items():
            s = s + "\t{0}: {1}\n".format(key, value)
        return s
    
    @classmethod
    def create_from_dictionary(cls, transactionDictionary):
        transaction_id = transactionDictionary["TransactionID"]
        unit_id = transactionDictionary["UnitID"]
        workstation_id = transactionDictionary["WorkstationID"]
        sequence_id = transactionDictionary["SequenceNumber"]
        start_dtime = transactionDictionary["BeginDateTime"]
        end_dtime = transactionDictionary["EndDateTime"]
        currency = transactionDictionary["CurrencyCode"]
        training_mode_flag = transactionDictionary["TrainingModeFlag"]
        
        quantity = transactionDictionary["Quantity"]
        extended_amount = transactionDictionary["ExtendedAmount"]
        transaction_net_amount = transactionDictionary["TransactionNetAmount"]
        
        return cls(
                   transaction_id,
                   unit_id,
                   workstation_id,
                   sequence_id,
                   start_dtime,
                   end_dtime,
                   currency,
                   training_mode_flag,
                   
                   quantity,
                   extended_amount,
                   transaction_net_amount) 
        
