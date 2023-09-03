import datetime as date
import hashlib as libhash
import json as ajson
import re
import uuid
import rsa

class Blockchain:



    def __init__(self):
        self.chain = list()
        self.current_transactions = list()
        genesis_block = self.generate_block(data="genesis block the begining of blockchain",proof=1,previous_hash=0,index=1)
        self.chain.append(genesis_block) 
        self.user_balances = {}




        
    def generate_block(self,data:str,proof:int,previous_hash:str,index:int)->dict:
        block = {
            "index": index,
            "timestamp": str(date.datetime.now()),
            "data": data,
            "proof":proof,
            "previous_hash":previous_hash,
         } 
        return block
    

    
    

    def get_block_before(self)-> dict:

        return self.chain[-1]

    



    def mine_block(self, data:str,miner_address:str)-> dict:
        previous_block = self.get_block_before()
        previous_proof =previous_block["proof"]
        index=len(self.chain)+1
        proof=self.proof_of_work(previous_proof=previous_proof,index=index,data=data)
        previous_hash=self.hash_block(block=previous_block)
        new_mine_block=self.generate_block(data=data,proof=proof,previous_hash=previous_hash,index=index)
        new_mine_block["transactions"] = self.current_transactions
         # Reward the miner with a transaction
        self.add_transaction(sender="0", recipient=miner_address, amount=1.0)
        self.current_transactions = []
        self.chain.append(new_mine_block)
        return new_mine_block






    def proof_of_work(self, previous_proof:str,index:int, data:str)->int:
        set_proof =1
        validate_proof = False

        while not validate_proof:
            print(set_proof)
            to_calculate =self.solve_mathematical_puzzle(new_proof=set_proof,previous_proof=previous_proof,index=index,data=data)
            value_of_hash=libhash.sha256(to_calculate).hexdigest()
            if value_of_hash[:3]=="000":
                validate_proof=True 
            else:
                set_proof= set_proof+1
        return set_proof


        
         
        
    def solve_mathematical_puzzle(self,new_proof:int, previous_proof:int, index:int,data :str)->bytes:
        mathetical_formular =str(new_proof**2 - previous_proof**2 +index) +data
        return mathetical_formular.encode()   
    




    def hash_block(self,block:dict)->str:
        block_to_be_encrypted=ajson.dumps(block,sort_keys=True).encode()
        return libhash.sha256(block_to_be_encrypted).hexdigest()
    



    

    def add_transaction(self, sender: str, recipient: str, amount: float):
      #exit  if self.is_valid_transaction(sender, recipient, amount):
            self.current_transactions.append({
                "sender": sender,
                "recipient": recipient,
                "amount": amount
            })






    def is_valid_transaction(self, sender: str, recipient: str, amount: float) -> bool:
      
        if not self.is_valid_address(sender) or not self.is_valid_address(recipient):
            return False

       
        sender_balance = self.get_balance(sender)
        if sender_balance < amount:
            return False

        if amount <= 0:
            return False

        return True
    





    def is_valid_address(self, address: str) -> bool:
     
        pattern = re.compile(r'^[a-zA-Z0-9]{32}$')  

        if not pattern.match(address):
            return False

        return True





    def get_balance(self, address: str) -> float:
        
        if address in self.user_balances:
            return self.user_balances[address]
        else:
            return 0.0  





    def check_chain_validity(self) -> bool:
        previous_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block["previous_hash"] != self.hash_block(previous_block):
                return False

            previous_proof = previous_block["proof"]
            index, data, proof = block["index"], block["data"], block["proof"]
            hash_operation = libhash.sha256(
                self._to_digest(
                    new_proof=proof,
                    previous_proof=previous_proof,
                    index=index,
                    data=data,
                )
            ).hexdigest()

            if hash_operation[:3] != "000":
                return False

            previous_block = block
            block_index += 1

        return True



class Wallet:
    def __init__(self):
        self.public_key, self.private_key = self.generate_keys()
        self.balance = 0
        self.transaction_history = []
        self.address_book = {}  # A dictionary to store recipient addresses

   



    def generate_keys(self):
        return rsa.newkeys(512)

    def get_address(self):
        return str(uuid.uuid4())





    def add_to_address_book(self, name, address):
        self.address_book[name] = address






    def get_address_from_book(self, name):
        return self.address_book.get(name)
    



    

    def is_valid_address(self, address):
        return len(address) == 36 and address[14] == '-'
    




    def add_transaction_to_history(self, transaction):
        self.transaction_history.append(transaction)






    def get_transaction_history(self):
        return self.transaction_history



    