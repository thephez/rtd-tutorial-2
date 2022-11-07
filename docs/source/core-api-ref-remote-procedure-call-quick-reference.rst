`Addressindex RPCs <core-api-ref-remote-procedure-calls-address-index>`__
=========================================================================

These RPCs are all Dash-specific and not found in Bitcoin Core

-  `GetAddressBalance <core-api-ref-remote-procedure-calls-address-index#getaddressbalance>`__:
   returns the balance for address(es).
-  `GetAddressDeltas <core-api-ref-remote-procedure-calls-address-index#getaddressdeltas>`__:
   returns all changes for an address.
-  `GetAddressMempool <core-api-ref-remote-procedure-calls-address-index#getaddressmempool>`__:
   returns all mempool deltas for an address.
-  `GetAddressTxids <core-api-ref-remote-procedure-calls-address-index#getaddresstxids>`__:
   returns the txids for an address(es).
-  `GetAddressUtxos <core-api-ref-remote-procedure-calls-address-index#getaddressutxos>`__:
   returns all unspent outputs for an address.

`Block Chain RPCs <core-api-ref-remote-procedure-calls-blockchain>`__
=====================================================================

-  `GetBestBlockHash <core-api-ref-remote-procedure-calls-blockchain#getbestblockhash>`__:
   returns the header hash of the most recent block on the best block
   chain.
-  `GetBestChainLock <core-api-ref-remote-procedure-calls-blockchain#getbestchainlock>`__:
   returns the block hash of the best chainlock. *New in Dash Core
   0.15.0*
-  `GetBlock <core-api-ref-remote-procedure-calls-blockchain#getblock>`__:
   gets a block with a particular header hash from the local block
   database either as a JSON object or as a serialized block. *Updated
   in Dash Core 0.16.0*
-  `GetBlockChainInfo <core-api-ref-remote-procedure-calls-blockchain#getblockchaininfo>`__:
   provides information about the current state of the block chain.
   *Updated in Dash Core 0.16.0*
-  `GetBlockCount <core-api-ref-remote-procedure-calls-blockchain#getblockcount>`__:
   returns the number of blocks in the local best block chain.
-  `GetBlockFilter <core-api-ref-remote-procedure-calls-blockchain#getblockfilter>`__:
   retrieves a
   `BIP157 <https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki>`__
   content filter for a particular block. **New in Dash Core 18.0.0**
-  `GetBlockHash <core-api-ref-remote-procedure-calls-blockchain#getblockhash>`__:
   returns the header hash of a block at the given height in the local
   best block chain.
-  `GetBlockHashes <core-api-ref-remote-procedure-calls-blockchain#getblockhashes>`__:
   returns array of hashes of blocks within the timestamp range provided
   (requires ``timestampindex`` to be enabled). New in Dash Core 0.12.1
-  `GetBlockHeader <core-api-ref-remote-procedure-calls-blockchain#getblockheader>`__:
   gets a block header with a particular header hash from the local
   block database either as a JSON object or as a serialized block
   header. *Updated in Dash Core 0.16.0*
-  `GetBlockHeaders <core-api-ref-remote-procedure-calls-blockchain#getblockheaders>`__:
   returns an array of items with information about the requested number
   of blockheaders starting from the requested hash. New in Dash Core
   0.12.1
-  `GetBlockStats <core-api-ref-remote-procedure-calls-blockchain#getblockstats>`__:
   computes per block statistics for a given window. **Updated in Dash
   Core 18.0.0**
-  `GetChainTips <core-api-ref-remote-procedure-calls-blockchain#getchaintips>`__:
   returns information about the highest-height block (tip) of each
   local block chain. *Updated in Dash Core 0.12.3*
-  `GetChainTxStats <core-api-ref-remote-procedure-calls-blockchain#getchaintx-stats>`__:
   compute statistics about the total number and rate of transactions in
   the chain. **Updated in Dash Core 18.0.0**
-  `GetDifficulty <core-api-ref-remote-procedure-calls-blockchain#getdifficulty>`__:
   returns the proof-of-work difficulty as a multiple of the minimum
   difficulty.
-  `GetMemPoolAncestors <core-api-ref-remote-procedure-calls-blockchain#getmempoolancestors>`__:
   returns all in-mempool ancestors for a transaction in the mempool.
   **Updated in Dash Core 0.17.0**
-  `GetMemPoolDescendants <core-api-ref-remote-procedure-calls-blockchain#getmempooldescendants>`__:
   returns all in-mempool descendants for a transaction in the mempool.
   **Updated in Dash Core 0.17.0**
-  `GetMemPoolEntry <core-api-ref-remote-procedure-calls-blockchain#getmempoolentry>`__:
   returns mempool data for given transaction (must be in mempool).
   **Updated in Dash Core 0.17.0**
-  `GetMemPoolInfo <core-api-ref-remote-procedure-calls-blockchain#getmempoolinfo>`__:
   returns information about the node’s current transaction memory pool.
   *Updated in Dash Core 0.16.0*
-  `GetRawMemPool <core-api-ref-remote-procedure-calls-blockchain#getrawmempool>`__:
   returns all transaction identifiers (TXIDs) in the memory pool as a
   JSON array, or detailed information about each transaction in the
   memory pool as a JSON object. **Updated in Dash Core 0.17.0**
-  `GetMerkleBlocks <core-api-ref-remote-procedure-calls-blockchain#getmerkleblocks>`__:
   returns an array of hex-encoded merkleblocks for blocks starting from
   which match . *New in Dash Core 0.15.0*
-  `GetSpecialTxes <core-api-ref-remote-procedure-calls-blockchain#getspecialtxes>`__:
   returns an array of special transactions found in the specified block
   *New in Dash Core 0.13.1*
-  `GetSpentInfo <core-api-ref-remote-procedure-calls-blockchain#getspentinfo>`__:
   returns the txid and index where an output is spent (requires
   ``spentindex`` to be enabled). New in Dash Core 0.12.1
-  `GetTxOut <core-api-ref-remote-procedure-calls-blockchain#gettxout>`__:
   returns details about an unspent transaction output (UTXO). *Updated
   in Dash Core 0.15.0*
-  `GetTxOutProof <core-api-ref-remote-procedure-calls-blockchain#gettxoutproof>`__:
   returns a hex-encoded proof that one or more specified transactions
   were included in a block.
-  `GetTxOutSetInfo <core-api-ref-remote-procedure-calls-blockchain#gettxoutsetinfo>`__:
   returns statistics about the confirmed unspent transaction output
   (UTXO) set. Note that this call may take some time and that it only
   counts outputs from confirmed transactions—it does not count outputs
   from the memory pool. *Updated in Dash Core 0.15.0*
-  `PreciousBlock <core-api-ref-remote-procedure-calls-blockchain#preciousblock>`__:
   treats a block as if it were received before others with the same
   work. *New in Dash Core 0.12.3*
-  `PruneBlockChain <core-api-ref-remote-procedure-calls-blockchain#pruneblockchain>`__:
   prunes the blockchain up to a specified height or timestamp. *New in
   Dash Core 0.12.3*
-  `SaveMemPool <core-api-ref-remote-procedure-calls-blockchain#savemempool>`__:
   dumps the mempool to disk. *New in Dash Core 0.16.0*
-  `VerifyChain <core-api-ref-remote-procedure-calls-blockchain#verifychain>`__:
   verifies each entry in the local block chain database.
-  `VerifyTxOutProof <core-api-ref-remote-procedure-calls-blockchain#verifytxoutproof>`__:
   verifies that a proof points to one or more transactions in a block,
   returning the transactions the proof commits to and throwing an RPC
   error if the block is not in our best block chain.

`Control RPCs <core-api-ref-remote-procedure-calls-control>`__
==============================================================

-  `Debug <core-api-ref-remote-procedure-calls-control#debug>`__:
   changes the debug category from the console. **Updated in Dash Core
   18.0.0**
-  `GetMemoryInfo <core-api-ref-remote-procedure-calls-control#getmemoryinfo>`__:
   returns information about memory usage. *Updated in Dash Core 0.15.0*
-  `GetRPCInfo <core-api-ref-remote-procedure-calls-control#getrpcinfo>`__:
   returns details about the RPC server. **New in Dash Core 18.0.0**
-  `Help <core-api-ref-remote-procedure-calls-control#help>`__: lists
   all available public RPC commands, or gets help for the specified
   RPC. Commands which are unavailable will not be listed, such as
   wallet RPCs if wallet support is disabled. **Updated in Dash Core
   0.17.0**
-  `Logging <core-api-ref-remote-procedure-calls-control#logging>`__:
   gets and sets the logging configuration **Updated in Dash Core
   18.0.0**
-  `Stop <core-api-ref-remote-procedure-calls-control#stop>`__: safely
   shuts down the Dash Core server.
-  `Uptime <core-api-ref-remote-procedure-calls-control#uptime>`__:
   returns the total uptime of the server. *New in Dash Core 0.15.0*

`Dash RPCs <core-api-ref-remote-procedure-calls-dash>`__
========================================================

-  `GetGovernanceInfo <core-api-ref-remote-procedure-calls-dash#getgovernanceinfo>`__:
   returns an object containing governance parameters. *Updated in Dash
   Core 0.14.0*
-  `GetCoinJoinInfo <core-api-ref-remote-procedure-calls-dash#getcoinjoininfo>`__:
   returns an object containing an information about CoinJoin settings
   and state. *New in Dash Core 0.15.0*
-  `GetSuperblockBudget <core-api-ref-remote-procedure-calls-dash#getsuperblockbudget>`__:
   returns the absolute maximum sum of superblock payments allowed.
-  `GObject <core-api-ref-remote-procedure-calls-dash#gobject>`__:
   provides a set of commands for managing governance objects and
   displaying information about them. **Updated in Dash Core 0.17.0**
-  `Masternode <core-api-ref-remote-procedure-calls-dash#masternode>`__:
   provides a set of commands for managing masternodes and displaying
   information about them. **Updated in Dash Core 0.17.0**
-  `MasternodeList <core-api-ref-remote-procedure-calls-dash#masternodelist>`__:
   returns a list of masternodes in different modes. *Updated in Dash
   Core 0.14.0*
-  `MnSync <core-api-ref-remote-procedure-calls-dash#mnsync>`__: returns
   the sync status, updates to the next step or resets it entirely.
   *Updated in Dash Core 0.14.0*
-  `CoinJoin <core-api-ref-remote-procedure-calls-dash#coinjoin>`__:
   controls the CoinJoin process. *Updated in Dash Core 0.12.3*
-  `Spork <core-api-ref-remote-procedure-calls-dash#spork>`__: reads or
   updates spork settings on the network.
-  `VoteRaw <core-api-ref-remote-procedure-calls-dash#voteraw>`__:
   compiles and relays a governance vote with provided external
   signature instead of signing vote internally

`Evolution RPCs <core-api-ref-remote-procedure-calls-evo>`__
============================================================

-  `BLS <core-api-ref-remote-procedure-calls-evo#bls>`__: provides a set
   of commands to execute BLS-related actions. *Updated in Dash Core
   0.14.0*
-  `ProTx <core-api-ref-remote-procedure-calls-evo#protx>`__: provides a
   set of commands to execute ProTx related actions. **Updated in Dash
   Core 0.17.0**
-  `Quorum <core-api-ref-remote-procedure-calls-evo#quorum>`__: provides
   a set of commands for quorums (LLMQs). **Updated in Dash Core
   18.0.0**
-  `VerifyChainLock <core-api-ref-remote-procedure-calls-evo#verifychainlock>`__:
   tests if a quorum signature is valid for a ChainLock. **New in Dash
   Core 0.17.0**
-  `VerifyISLock <core-api-ref-remote-procedure-calls-evo#verifyislock>`__:
   tests if a quorum signature is valid for an InstantSend lock. **New
   in Dash Core 0.17.0**

`Generating RPCs <core-api-ref-remote-procedure-calls-generating>`__
====================================================================

-  `Generate <core-api-ref-remote-procedure-calls-generating#generate>`__:
   mines blocks immediately (before the RPC call returns). *Updated in
   Dash Core 0.12.3*
-  `GenerateToAddress <core-api-ref-remote-procedure-calls-generating#generatetoaddress>`__:
   mines blocks immediately to a specified address. *New in Dash Core
   0.12.3*

`Mining RPCs <core-api-ref-remote-procedure-calls-mining>`__
============================================================

-  `GetBlockTemplate <core-api-ref-remote-procedure-calls-mining#getblocktemplate>`__:
   gets a block template or proposal for use with mining software.
   **Updated in Dash Core 18.0.0**
-  `GetMiningInfo <core-api-ref-remote-procedure-calls-mining#getmininginfo>`__:
   returns various mining-related information. **Updated in Dash Core
   18.0.0**
-  `GetNetworkHashPS <core-api-ref-remote-procedure-calls-mining#getnetworkhashps>`__:
   returns the estimated network hashes per second based on the last n
   blocks.
-  `PrioritiseTransaction <core-api-ref-remote-procedure-calls-mining#prioritisetransaction>`__:
   adds virtual priority or fee to a transaction, allowing it to be
   accepted into blocks mined by this node (or miners which use this
   node) with a lower priority or fee. (It can also remove virtual
   priority or fee, requiring the transaction have a higher priority or
   fee to be accepted into a locally-mined block.) *Updated in Dash Core
   0.14.0*
-  `SubmitBlock <core-api-ref-remote-procedure-calls-mining#submitblock>`__:
   accepts a block, verifies it is a valid addition to the block chain,
   and broadcasts it to the network. Extra parameters are ignored by
   Dash Core but may be used by mining pools or other programs.
-  `SubmitHeader <core-api-ref-remote-procedure-calls-mining#submitheader>`__:
   decodes the given hex data as a header and submits it as a candidate
   chain tip if valid. **New in Dash Core 18.0.0**

`Network RPCs <core-api-ref-remote-procedure-calls-network>`__
==============================================================

-  `AddNode <core-api-ref-remote-procedure-calls-network#addnode>`__:
   attempts to add or remove a node from the addnode list, or to try a
   connection to a node once.
-  `ClearBanned <core-api-ref-remote-procedure-calls-network#clearbanned>`__:
   clears list of banned nodes.
-  `DisconnectNode <core-api-ref-remote-procedure-calls-network#disconnectnode>`__:
   immediately disconnects from a specified node. *Updated in Dash Core
   0.15.0*
-  `GetAddedNodeInfo <core-api-ref-remote-procedure-calls-network#getaddednodeinfo>`__:
   returns information about the given added node, or all added nodes
   (except onetry nodes). Only nodes which have been manually added
   using the ```addnode``
   RPC <core-api-ref-remote-procedure-calls-network#addnode>`__ will
   have their information displayed. *Updated in Dash Core 0.12.3*
-  `GetConnectionCount <core-api-ref-remote-procedure-calls-network#getconnectioncount>`__:
   returns the number of connections to other nodes.
-  `GetNetTotals <core-api-ref-remote-procedure-calls-network#getnettotals>`__:
   returns information about network traffic, including bytes in, bytes
   out, and the current time.
-  `GetNetworkInfo <core-api-ref-remote-procedure-calls-network#getnetworkinfo>`__:
   returns information about the node’s connection to the network.
   **Updated in Dash Core 18.0.0**
-  `GetNodeAddresses <core-api-ref-remote-procedure-calls-network#getnodeaddresses>`__:
   returns the known addresses which can potentially be used to find new
   nodes in the network. **New in Dash Core 18.0.0**
-  `GetPeerInfo <core-api-ref-remote-procedure-calls-network#getpeerinfo>`__:
   returns data about each connected network node. **Updated in Dash
   Core 18.0.0**
-  `ListBanned <core-api-ref-remote-procedure-calls-network#listbanned>`__:
   lists all banned IPs/Subnets.
-  `Ping <core-api-ref-remote-procedure-calls-network#ping>`__: sends a
   P2P ping message to all connected nodes to measure ping time. Results
   are provided by the ```getpeerinfo``
   RPC <core-api-ref-remote-procedure-calls-network#getpeerinfo>`__
   pingtime and pingwait fields as decimal seconds. The P2P ```ping``
   message <core-ref-p2p-network-control-messages#ping>`__ is handled in
   a queue with all other commands, so it measures processing backlog,
   not just network ping.
-  `SetBan <core-api-ref-remote-procedure-calls-network#setban>`__:
   attempts add or remove a IP/Subnet from the banned list.
-  `SetNetworkActive <core-api-ref-remote-procedure-calls-network#setnetworkactive>`__:
   disables/enables all P2P network activity.

`Raw Transaction RPCs <core-api-ref-remote-procedure-calls-raw-transactions>`__
===============================================================================

-  `CombinePSBT <core-api-ref-remote-procedure-calls-raw-transactions#combinepsbt>`__:
   combines multiple partially-signed Dash transactions into one
   transaction. **New in Dash Core 18.0.0**
-  `CombineRawTransaction <core-api-ref-remote-procedure-calls-raw-transactions#combinerawtransaction>`__:
   combine multiple partially signed transactions into one transaction.
   *New in Dash Core 0.15.0*
-  `ConvertToPSBT <core-api-ref-remote-procedure-calls-raw-transactions#converttopsbt>`__:
   converts a network serialized transaction to a PSBT. **New in Dash
   Core 18.0.0**
-  `CreatePSBT <core-api-ref-remote-procedure-calls-raw-transactions#createpsbt>`__:
   creates a transaction in the Partially Signed Transaction (PST)
   format. **New in Dash Core 18.0.0**
-  `CreateRawTransaction <core-api-ref-remote-procedure-calls-raw-transactions#createrawtransaction>`__:
   creates an unsigned serialized transaction that spends a previous
   output to a new output with a P2PKH or P2SH address. The transaction
   is not stored in the wallet or transmitted to the network. **Updated
   in Dash Core 0.17.0**
-  `DecodePSBT <core-api-ref-remote-procedure-calls-raw-transactions#decodepsbt>`__:
   returns a JSON object representing the serialized, base64-encoded
   partially signed Dash transaction. **New in Dash Core 18.0.0**
-  `DecodeRawTransaction <core-api-ref-remote-procedure-calls-raw-transactions#decoderawtransaction>`__:
   decodes a serialized transaction hex string into a JSON object
   describing the transaction. *Updated in Dash Core 0.13.0*
-  `DecodeScript <core-api-ref-remote-procedure-calls-raw-transactions#decodescript>`__:
   decodes a hex-encoded P2SH redeem script.
-  `FinalizePSBT <core-api-ref-remote-procedure-calls-raw-transactions#finalizepsbt>`__:
   finalizes the inputs of a PSBT. The PSBT produces a network
   serialized transaction if the transaction is fully signed. **New in
   Dash Core 18.0.0**
-  `FundRawTransaction <core-api-ref-remote-procedure-calls-raw-transactions#fundrawtransaction>`__:
   adds inputs to a transaction until it has enough in value to meet its
   out value. **Updated in Dash Core 0.17.0**
-  `GetRawTransaction <core-api-ref-remote-procedure-calls-raw-transactions#getrawtransaction>`__:
   gets a hex-encoded serialized transaction or a JSON object describing
   the transaction. By default, Dash Core only stores complete
   transaction data for UTXOs and your own transactions, so the RPC may
   fail on historic transactions unless you use the non-default
   ``txindex=1`` in your Dash Core startup settings. *Updated in Dash
   Core 0.16.0*
-  `JoinPSBTs <core-api-ref-remote-procedure-calls-raw-transactions#joinpsbts>`__:
   joins multiple distinct PSBTs with different inputs and outputs into
   one PSBT with inputs and outputs from all of the PSBTs.
-  `SendRawTransaction <core-api-ref-remote-procedure-calls-raw-transactions#sendrawtransaction>`__:
   validates a transaction and broadcasts it to the peer-to-peer
   network. *Updated in Dash Core 0.15.0*
-  `SignRawTransactionWithKey <core-api-ref-remote-procedure-calls-raw-transactions#signrawtransactionwithkey>`__:
   signs a transaction in the serialized transaction format using
   private keys provided in the call. **New in Dash Core 0.17.0**
-  `TestMempoolAccept <core-api-ref-remote-procedure-calls-raw-transactions#testmempoolaccept>`__:
   returns the results of mempool acceptance tests indicating if raw
   transaction (serialized, hex-encoded) would be accepted by mempool.
   **New in Dash Core 18.0.0**
-  `UTXOUpdatePSBT <core-api-ref-remote-procedure-calls-raw-transactions#testmempoolaccept>`__:
   updates a PSBT with UTXOs retrieved from the UTXO set or the mempool.
   **New in Dash Core 18.0.0**

`Utility RPCs <core-api-ref-remote-procedure-calls-util>`__
===========================================================

-  `CreateMultiSig <core-api-ref-remote-procedure-calls-util#createmultisig>`__:
   creates a P2SH multi-signature address. **Updated in Dash Core
   0.17.0**
-  `DeriveAddresses <core-api-ref-remote-procedure-calls-util#deriveaddresses>`__:
   derives one or more addresses corresponding to an output descriptor.
   **New in Dash Core 18.0.0**
-  `EstimateSmartFee <core-api-ref-remote-procedure-calls-util#estimatesmartfee>`__:
   estimates the transaction fee per kilobyte that needs to be paid for
   a transaction to begin confirmation within a certain number of blocks
   and returns the number of blocks for which the estimate is valid.
   *Updated in Dash Core 0.15.0*
-  `GetDescriptorInfo <core-api-ref-remote-procedure-calls-util#getdescriptorinfo>`__:
   analyses a descriptor. **New in Dash Core 18.0.0**
-  `SignMessageWithPrivKey <core-api-ref-remote-procedure-calls-util#signmessagewithprivkey>`__:
   signs a message with a given private key. *New in Dash Core 0.12.3*
-  `ValidateAddress <core-api-ref-remote-procedure-calls-util#validateaddress>`__:
   returns information about the given Dash address. **Updated in Dash
   Core 0.17.0**
-  `VerifyMessage <core-api-ref-remote-procedure-calls-util#verifymessage>`__:
   verifies a signed message.

`Wallet RPCs <core-api-ref-remote-procedure-calls-wallet>`__
============================================================

**Note:** the wallet RPCs are only available if Dash Core was built with
<>, which is the default.

-  `AbandonTransaction <core-api-ref-remote-procedure-calls-wallet#abandontransaction>`__:
   marks an in-wallet transaction and all its in-wallet descendants as
   abandoned. This allows their inputs to be respent.
-  `AbortRescan <core-api-ref-remote-procedure-calls-wallet#abortrescan>`__:
   stops current wallet rescan. *New in Dash Core 0.15.0*
-  `AddMultiSigAddress <core-api-ref-remote-procedure-calls-wallet#addmultisigaddress>`__:
   adds a P2SH multisig address to the wallet. **Updated in Dash Core
   0.17.0**
-  `BackupWallet <core-api-ref-remote-procedure-calls-wallet#backupwallet>`__:
   safely copies ``wallet.dat`` to the specified file, which can be a
   directory or a path with filename.
-  `CreateWallet <core-api-ref-remote-procedure-calls-wallet#createwallet>`__:
   creates and loads a new wallet. **Updated in Dash Core 18.0.0**
-  `DumpHDInfo <core-api-ref-remote-procedure-calls-wallet#dumphdinfo>`__:
   returns an object containing sensitive private info about this HD
   wallet New in Dash Core 0.12.2
-  `DumpPrivKey <core-api-ref-remote-procedure-calls-wallet#dumpprivkey>`__:
   returns the wallet-import-format (WIP) private key corresponding to
   an address. (But does not remove it from the wallet.)
-  `DumpWallet <core-api-ref-remote-procedure-calls-wallet#dumpwallet>`__:
   creates or overwrites a file with all wallet keys in a human-readable
   format. **Updated in Dash Core 0.17.0**
-  `EncryptWallet <core-api-ref-remote-procedure-calls-wallet#encryptwallet>`__:
   encrypts the wallet with a passphrase. This is only to enable
   encryption for the first time. After encryption is enabled, you will
   need to enter the passphrase to use private keys.
-  `GetAddressInfo <core-api-ref-remote-procedure-calls-wallet#getaddressinfo>`__:
   returns information about the given Dash address. **Updated in Dash
   Core 18.0.0**
-  `GetAddressesByLabel <core-api-ref-remote-procedure-calls-wallet#getaddressesbylabel>`__:
   returns a list of every address assigned to a particular label. **New
   in Dash Core 0.17.0**
-  `GetBalance <core-api-ref-remote-procedure-calls-wallet#getbalance>`__:
   gets the balance in decimal dash across all accounts or for a
   particular account. *Updated in Dash Core 0.13.0*
-  `GetNewAddress <core-api-ref-remote-procedure-calls-wallet#getnewaddress>`__:
   returns a new Dash address for receiving payments. If an account is
   specified, payments received with the address will be credited to
   that account. **Updated in Dash Core 0.17.0**
-  `GetRawChangeAddress <core-api-ref-remote-procedure-calls-wallet#getrawchangeaddress>`__:
   returns a new Dash address for receiving change. This is for use with
   raw transactions, not normal use.
-  `GetReceivedByAddress <core-api-ref-remote-procedure-calls-wallet#getreceivedbyaddress>`__:
   returns the total amount received by the specified address in
   transactions with the specified number of confirmations. It does not
   count coinbase transactions. *Updated in Dash Core 0.13.0*
-  `GetReceivedByLabel <core-api-ref-remote-procedure-calls-wallet#getreceivedbylabel>`__:
   returns the list of addresses assigned the specified label. **New in
   Dash Core 0.17.0**
-  `GetTransaction <core-api-ref-remote-procedure-calls-wallet#gettransaction>`__:
   gets detailed information about an in-wallet transaction. **Updated
   in Dash Core 0.17.0**
-  `GetUnconfirmedBalance <core-api-ref-remote-procedure-calls-wallet#getunconfirmedbalance>`__:
   returns the wallet’s total unconfirmed balance.
-  `GetWalletInfo <core-api-ref-remote-procedure-calls-wallet#getwalletinfo>`__:
   provides information about the wallet. *Updated in Dash Core 0.12.3*
-  `ImportAddress <core-api-ref-remote-procedure-calls-wallet#importaddress>`__:
   adds an address or pubkey script to the wallet without the associated
   private key, allowing you to watch for transactions affecting that
   address or pubkey script without being able to spend any of its
   outputs.
-  `ImportElectrumWallet <core-api-ref-remote-procedure-calls-wallet#importelectrumwallet>`__:
   imports keys from an Electrum wallet export file (.csv or .json) New
   in Dash Core 0.12.1
-  `ImportMulti <core-api-ref-remote-procedure-calls-wallet#importmulti>`__:
   imports addresses or scripts (with private keys, public keys, or P2SH
   redeem scripts) and optionally performs the minimum necessary rescan
   for all imports. *New in Dash Core 0.12.3*
-  `ImportPrivKey <core-api-ref-remote-procedure-calls-wallet#importprivkey>`__:
   adds a private key to your wallet. The key should be formatted in the
   wallet import format created by the ```dumpprivkey``
   RPC <core-api-ref-remote-procedure-calls-wallet#dumpprivkey>`__.
-  `ImportPrunedFunds <core-api-ref-remote-procedure-calls-wallet#importprunedfunds>`__:
   imports funds without the need of a rescan. Meant for use with pruned
   wallets. *New in Dash Core 0.12.3*
-  `ImportPubKey <core-api-ref-remote-procedure-calls-wallet#importpubkey>`__:
   imports a public key (in hex) that can be watched as if it were in
   your wallet but cannot be used to spend
-  `ImportWallet <core-api-ref-remote-procedure-calls-wallet#importwallet>`__:
   imports private keys from a file in wallet dump file format (see the
   ```dumpwallet``
   RPC <core-api-ref-remote-procedure-calls-wallet#dumpwallet>`__).
   These keys will be added to the keys currently in the wallet. This
   call may need to rescan all or parts of the block chain for
   transactions affecting the newly-added keys, which may take several
   minutes.
-  `KeyPoolRefill <core-api-ref-remote-procedure-calls-wallet#keypoolrefill>`__:
   fills the cache of unused pre-generated keys (the keypool).
-  `ListAddressBalances <core-api-ref-remote-procedure-calls-wallet#listaddressbalances>`__:
   lists addresses of this wallet and their balances *New in Dash Core
   0.12.3*
-  `ListAddressGroupings <core-api-ref-remote-procedure-calls-wallet#listaddressgroupings>`__:
   lists groups of addresses that may have had their common ownership
   made public by common use as inputs in the same transaction or from
   being used as change from a previous transaction. **Updated in Dash
   Core 0.17.0**
-  `ListLabels <core-api-ref-remote-procedure-calls-wallet#listlabels>`__:
   returns the list of all labels, or labels that are assigned to
   addresses with a specific purpose. **New in Dash Core 0.17.0**
-  `ListLockUnspent <core-api-ref-remote-procedure-calls-wallet#listlockunspent>`__:
   returns a list of temporarily unspendable (locked) outputs.
-  `ListReceivedByAddress <core-api-ref-remote-procedure-calls-wallet#listreceivedbyaddress>`__:
   lists the total number of dash received by each address. **Updated in
   Dash Core 0.17.0**
-  `ListReceivedByLabel <core-api-ref-remote-procedure-calls-wallet#listreceivedbylabel>`__:
   lists the total number of dash received by each label. **New in Dash
   Core 0.17.0**
-  `ListSinceBlock <core-api-ref-remote-procedure-calls-wallet#listsinceblock>`__:
   gets all transactions affecting the wallet which have occurred since
   a particular block, plus the header hash of a block at a particular
   depth. **Updated in Dash Core 0.17.0**
-  `ListTransactions <core-api-ref-remote-procedure-calls-wallet#listtransactions>`__:
   returns the most recent transactions that affect the wallet.
   **Updated in Dash Core 0.17.0**
-  `ListUnspent <core-api-ref-remote-procedure-calls-wallet#listunspent>`__:
   returns an array of unspent transaction outputs belonging to this
   wallet. **Updated in Dash Core 0.17.0**
-  `ListWalletDir <core-api-ref-remote-procedure-calls-wallet#listwalletdir>`__:
   returns a list of wallets in the wallet directory. **New in Dash Core
   18.0.0**
-  `ListWallets <core-api-ref-remote-procedure-calls-wallet#listwallets>`__:
   returns a list of currently loaded wallets. *New in Dash Core 0.15.0*
-  `LoadWallet <core-api-ref-remote-procedure-calls-wallet#loadwallet>`__:
   loads a wallet from a wallet file or directory. *New in Dash Core
   0.16.0*
-  `LockUnspent <core-api-ref-remote-procedure-calls-wallet#lockunspent>`__:
   temporarily locks or unlocks specified transaction outputs. A locked
   transaction output will not be chosen by automatic coin selection
   when spending dash. Locks are stored in memory only, so nodes start
   with zero locked outputs and the locked output list is always cleared
   when a node stops or fails.
-  `RemovePrunedFunds <core-api-ref-remote-procedure-calls-wallet#removeprunedfunds>`__:
   deletes the specified transaction from the wallet. Meant for use with
   pruned wallets and as a companion to importprunedfunds. *New in Dash
   Core 0.12.3*
-  `RescanBlockChain <core-api-ref-remote-procedure-calls-wallet#rescanblockchain>`__:
   rescans the local blockchain for wallet related transactions. *New in
   Dash Core 0.16.0*
-  `ScanTxOutset <core-api-ref-remote-procedure-calls-wallet#scantxoutset>`__:
   scans the unspent transaction output set for entries that match
   certain output descriptors. **New in Dash Core 18.0.0**
-  `SendMany <core-api-ref-remote-procedure-calls-wallet#sendmany>`__:
   creates and broadcasts a transaction which sends outputs to multiple
   addresses. **Updated in Dash Core 18.0.0**
-  `SendToAddress <core-api-ref-remote-procedure-calls-wallet#sendtoaddress>`__:
   spends an amount to a given address. *Updated in Dash Core 0.15.0*
-  `SetCoinJoinAmount <core-api-ref-remote-procedure-calls-wallet#setcoinjoinamount>`__:
   sets the amount of DASH to be processed *New in Dash Core 0.13.0*
-  `SetCoinJoinRounds <core-api-ref-remote-procedure-calls-wallet#setcoinjoinrounds>`__:
   sets the number of rounds to use *New in Dash Core 0.13.0*
-  `SetTxFee <core-api-ref-remote-procedure-calls-wallet#settxfee>`__:
   sets the transaction fee per kilobyte paid by transactions created by
   this wallet.
-  `SignMessage <core-api-ref-remote-procedure-calls-wallet#signmessage>`__:
   signs a message with the private key of an address.
-  `SignRawTransactionWithWallet <core-api-ref-remote-procedure-calls-wallet#signrawtransactionwithwallet>`__:
   signs a transaction in the serialized transaction format using
   private keys found in the wallet. **New in Dash Core 0.17.0**
-  `UnloadWallet <core-api-ref-remote-procedure-calls-wallet#unloadwallet>`__:
   unloads the wallet referenced by the request endpoint otherwise
   unloads the wallet specified in the argument. **New in Dash Core
   0.17.0**
-  `UpgradeToHD <core-api-ref-remote-procedure-calls-wallet#upgradetohd>`__:
   upgrades non-HD wallets to HD. **New in Dash Core 0.17.0**
-  `WalletCreateFundedPSBT <core-api-ref-remote-procedure-calls-wallet#walletcreatefundedpsbt>`__:
   creates and funds a transaction in the Partially Signed Transaction
   (PST) format. Inputs will be added if supplied inputs are not enough.
   **New in Dash Core 18.0.0**
-  `WalletLock <core-api-ref-remote-procedure-calls-wallet#walletlock>`__:
   removes the wallet encryption key from memory, locking the wallet.
   After calling this method, you will need to call ``walletpassphrase``
   again before being able to call any methods which require the wallet
   to be unlocked.
-  `WalletPassphrase <core-api-ref-remote-procedure-calls-wallet#walletpassphrase>`__:
   stores the wallet decryption key in memory for the indicated number
   of seconds. Issuing the ``walletpassphrase`` command while the wallet
   is already unlocked will set a new unlock time that overrides the old
   one.
-  `WalletPassphraseChange <core-api-ref-remote-procedure-calls-wallet#walletpassphrasechange>`__:
   changes the wallet passphrase from ‘old passphrase’ to ‘new
   passphrase’.
-  `WalletProcessPSBT <core-api-ref-remote-procedure-calls-wallet#walletprocesspsbt>`__:
   updates a PSBT with input information from a wallet and then allows
   the signing of inputs. **New in Dash Core 18.0.0**

`Wallet RPCs (Deprecated) <core-api-ref-remote-procedure-calls-wallet-deprecated>`__
====================================================================================

**Note:** the wallet RPCs are only available if Dash Core was built with
<>, which is the default.

-  `GetAccount <core-api-ref-remote-procedure-calls-wallet-deprecated#getaccount>`__:
   returns the name of the account associated with the given address.
   **Deprecated**
-  `GetAccountAddress <core-api-ref-remote-procedure-calls-wallet-deprecated#getaccountaddress>`__:
   returns the current Dash address for receiving payments to this
   account. If the account doesn’t exist, it creates both the account
   and a new address for receiving payment. Once a payment has been
   received to an address, future calls to this RPC for the same account
   will return a different address. **Deprecated**
-  `GetAddressesByAccount <core-api-ref-remote-procedure-calls-wallet-deprecated#getaddressesbyaccount>`__:
   returns a list of every address assigned to a particular account.
   **Deprecated**
-  `SetAccount <core-api-ref-remote-procedure-calls-wallet-deprecated#setaccount>`__:
   puts the specified address in the given account. **Deprecated**

`ZeroMQ (ZMQ) RPCs <core-api-ref-remote-procedure-calls-zmq>`__
===============================================================

-  `GetZmqNotifications <core-api-ref-remote-procedure-calls-zmq#getzmqnotifications>`__:
   returns information about the active ZeroMQ notifications. **Updated
   in Dash Core 18.0.0**

`Removed RPCs <core-api-ref-remote-procedure-calls-removed>`__
==============================================================

-  `EstimateFee <core-api-ref-remote-procedure-calls-removed#estimatefee>`__:
   **was removed in Dash Core 0.17.0.**
-  `GetPoolInfo <core-api-ref-remote-procedure-calls-removed#getpoolinfo>`__:
   returns an object containing pool related information. *Deprecated in
   0.15.0*
-  `GetReceivedByAccount <core-api-ref-remote-procedure-calls-removed#getreceivedbyaccount>`__:
   **was removed in Dash Core 18.0.0.**
-  `KeePass <core-api-ref-remote-procedure-calls-wallet#keepass>`__:
   **was removed in Dash Core 18.0.0.**
-  `ListAccounts <core-api-ref-remote-procedure-calls-removed#listaccounts>`__:
   **was removed in Dash Core 18.0.0.**
-  `ListReceivedByAccount <core-api-ref-remote-procedure-calls-removed#listreceivedbyaccount>`__:
   **was removed in Dash Core 18.0.0.**
-  `Move <core-api-ref-remote-procedure-calls-removed#move>`__: **was
   removed in Dash Core 18.0.0.**
-  `SendFrom <core-api-ref-remote-procedure-calls-removed#sendfrom>`__:
   **was removed in Dash Core 18.0.0.**
-  `SignRawTransaction <core-api-ref-remote-procedure-calls-removed#signrawtransaction>`__:
   **was removed in Dash Core 18.0.0.**
