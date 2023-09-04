This is a basic implementation of a blockchain system using Python, including a FastAPI interface for interacting with the blockchain. The code demonstrates the fundamental components of a blockchain, such as creating blocks, mining blocks, and managing transactions. Below, you'll find an overview of the key components and how to use them.
Blockchain Class

The Blockchain class represents the core of the blockchain system. It includes the following functionalities:

    Initialization: Upon initialization, a genesis block is created, which serves as the initial block in the blockchain. The user_balances dictionary is used to track user account balances.

    Mining Blocks: The mine_block function allows miners to create new blocks by providing transaction data and a miner's address. Mining involves solving a proof-of-work puzzle, and the miner is rewarded with a transaction.

    Adding Transactions: Users can add transactions to the blockchain using the add_transaction method, provided they have a sufficient balance and valid addresses.

    Chain Validity Check: The check_chain_validity function checks the integrity of the blockchain by verifying the previous block's hash and the validity of each block's proof-of-work.

    Transaction Validation: The is_valid_transaction function checks the validity of a transaction, considering sender balance and other conditions.

    Address Validation: The is_valid_address function checks the validity of a blockchain address.

    Balance Checking: The get_balance function retrieves the balance of a given address.

Wallet Class

The Wallet class represents a user's wallet and includes the following features:

    Key Pair Generation: Public and private keys are generated for the wallet using RSA encryption.

    Address Generation: A unique address is generated for the wallet.

    Address Book: An address book allows users to store recipient addresses for easy reference.

    Transaction History: The wallet keeps track of transaction history.

FastAPI Integration

The code also integrates FastAPI to create a simple API for interacting with the blockchain:

    Mining Endpoint: You can mine a new block by making a POST request to /mine/ with the data and miner_address parameters.

    Blockchain Information Endpoint: You can retrieve the entire blockchain by making a GET request to /blockchain/.

    Last Block Endpoint: To fetch the last block in the blockchain, use the /lastblock/ endpoint.

    Mempool Endpoint: Get the current transactions in the mempool by making a GET request to /mempool/.

    Add Transaction Endpoint: Add a new transaction to the blockchain by making a POST request to /addtransaction/ with the sender, recipient, and amount parameters.
