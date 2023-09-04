import blockchain as block_chain
import fastapi as   fast_api

blockchain = block_chain.Blockchain()
api = fast_api.FastAPI()



@api.post("/mine/")
def mine_block(data:str, miner_adres:str):
    if not blockchain.check_chain_validity():
        return fast_api.HTTPException(
            status_code=400, detail="the blockchain is not valid"
        )
    return blockchain.mine_block(data=data, miner_address=miner_adres)


@api.get("/blockchain/")
def fetch_blockchain():
    if not blockchain.check_chain_validity():
        return fast_api.HTTPException(
            status_code=400, detail="the blockchain is not valid"
        )
    return blockchain.chain




@api.get("/lastblock/")
def last_block():
    if not blockchain.check_chain_validity():
        return fast_api.HTTPException(status_code=400, detail="The blockchain is not valid")
        
    return blockchain.get_block_before()



@api.get("/mempool/")
def mempool_transaction():
    if not blockchain.check_chain_validity():
        return fast_api.HTTPException(status_code=400, detail="The blockchain is not valid")
        
    return blockchain.mempool()







@api.post("/addtransaction/")
def mine_block(self, sender: str, recipient: str, amount: float):
    if not blockchain.check_chain_validity():
        return fast_api.HTTPException(
            status_code=400, detail="the blockchain is not valid"
        )
    return blockchain.add_transaction(sender=sender,recipient=recipient,amount=amount)