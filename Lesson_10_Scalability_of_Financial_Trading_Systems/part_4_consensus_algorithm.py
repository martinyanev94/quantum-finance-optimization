class ConsensusAlgorithm:
    def __init__(self):
        self.leader = None

    def elect_leader(self, nodes):
        # Simple logic to elect a leader from the available nodes
        self.leader = nodes[0]  # Leadership assigned to the first node for simplicity
        print(f"Electing {self.leader} as the leader.")

    def replicate_transaction(self, transaction):
        print(f"Leader {self.leader} replicates transaction: {transaction}")

# Example usage
nodes = ["Node1", "Node2", "Node3"]
consensus = ConsensusAlgorithm()
consensus.elect_leader(nodes)
consensus.replicate_transaction("Trade Order: Buy 10 shares of AAPL")
