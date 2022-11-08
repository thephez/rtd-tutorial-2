Dash Core performs full <<glossary:masternode>> synchronization as required. There are several conditions that initiate a start/restart the sync process:

* Initial startup of Dash Core
* More than 60 minutes have passed since the last activation
* A failure occurred during the last sync attempt (after a 1 minute cooldown before sync restarts)
* Issuing a [`mnsync reset` RPC](core-api-ref-remote-procedure-calls-dash#mnsync) command

# Initial Masternode Sync

The deterministic masternode lists introduced by [DIP3](https://github.com/dashpay/dips/blob/master/dip-0003.md) eliminated several steps of the sync process related to the masternode list and masternode payments. Since that information is now available on-chain, P2P messages related to those steps were deprecated.

This diagram shows the order in which P2P messages are sent to perform masternode synchronization initially after startup.

![Masternode Sync (Initial)](https://dash-docs.github.io/img/dev/en-masternode-sync-initial-dip3.svg)

The following table details the data flow of P2P messages exchanged during initial masternode synchronization after the activation of [DIP3](https://github.com/dashpay/dips/blob/master/dip-0003.md) and <<glossary:Spork>> 15.

| **Syncing Node Message** | **Direction**  | **Masternode Response**   | **Description** |
| --- | :---: | --- | --- |
| **1. Sporks** |   |  |  |
| [`getsporks` message](core-ref-p2p-network-control-messages#getsporks)                            | → |                           | Syncing node requests sporks
|                                                | ← | [`spork` message](core-ref-p2p-network-control-messages#spork)(s)        |
| **2. Mempool** |   |  |  |
| [`mempool` message](core-ref-p2p-network-data-messages#mempool)                            | → |                           | Syncing node requests mempool entries
|                                                | ← | [`inv` message](core-ref-p2p-network-data-messages#inv)(s) | `inv` message(s) containing TXIDs of mempool transactions |
| **3. Governance** |   |  | See [Governance sync](#governance) |

*Masternode Sync Status*

There are several status values used to track masternode synchronization. They are used in both [`ssc` messages](core-ref-p2p-network-masternode-messages#ssc) and the [`mnsync` RPC](core-api-ref-remote-procedure-calls-dash#mnsync).

| **Value** | **Status**  | **Description** |
| --- | --- | --- |
| _-1_  | _`MASTERNODE_SYNC_FAILED` _     | **Removed in Dash Core 0.16.0**<br>Synchronization failed |
| _0_   | _`MASTERNODE_SYNC_INITIAL` _    | **Deprecated (merged with `MASTERNODE_SYNC_WAITING` in Dash Core 0.16.0)**<br>Synchronization just started, was reset recently, or is still in IBD |
| 1   | `MASTERNODE_SYNC_BLOCKCHAIN` (previously `MASTERNODE_SYNC_WAITING`)  | **Renamed in Dash Core 0.16.0**<br>Synchronization pending - waiting after initial to check for more headers/blocks.  |
| 4   | `MASTERNODE_SYNC_GOVERNANCE`  | Synchronizing governance objects  |
| 999 | `MASTERNODE_SYNC_FINISHED`    | Synchronization finished |

# Ongoing Masternode Sync

Once a masternode completes an initial full sync, continuing synchronization is maintained by the exchange of P2P messages with other <<glossary:nodes>>. This diagram shows an overview of the messages exchanged to keep governance objects synchronized between masternodes.

![Masternode Sync (Ongoing)](https://dash-docs.github.io/img/dev/en-masternode-sync-ongoing.svg)

**Governance**

After the initial governance synchronization, governance information is kept current by the [`govobj` messages](core-ref-p2p-network-governance-messages#govobj) and [`govobjvote` messages](core-ref-p2p-network-governance-messages#govobjvote) relayed on the <<glossary:network>>. Unsynchronized <<glossary:peers>> may send [`govsync` messages](core-ref-p2p-network-governance-messages#govsync) to request governance sync.

# Masternode Sync Schedule

The following tables detail the timing of various functions used to keep the masternodes in sync with each other. This information is derived from the scheduler section of `AppInitMain` in `src/init.cpp`.

| **Period (seconds)** | **Action** | **Description** |
| --- | --- | --- |
| 6   | MN Sync                   | Synchronizes sporks and governance objects (masternode-sync.cpp) |

The following actions only run when the masternode sync is past `MASTERNODE_SYNC_WAITING` status.

| **Period (seconds)** | **Action** | **Description** |
| --- | --- | --- |
| 60  | Process MN Connections    | Disconnects some masternodes (`masternodeman.cpp`) |
| 60  | InstantSend Check/Remove  | Remove expired/orphaned/invalid InstantSend candidates and votes (`instantx.cpp`) |
| 300 | Maintenance               | Check/remove/reprocess governance objects (`governance.cpp`) |