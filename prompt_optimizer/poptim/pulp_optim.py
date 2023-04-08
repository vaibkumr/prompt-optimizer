from prompt_optimizer.poptim.base import PromptOptimize
from pulp import LpBinary, LpVariable, LpProblem, LpMinimize, lpSum

class PulpOptim(PromptOptimize):
    """This doesn't really reduce #tokens"""
    def __init__(self, aggression=0.4, verbose=False, metrics=[]):
        super().__init__(verbose, metrics)
        self.aggression = aggression #will reduce num tokens by aggression*100%

    
    def run(self, prompt): 
        tokens = prompt.split()
        target_length = int(len(tokens) * ( 1 - self.aggression ))
        
        x = LpVariable.dicts("x", range(len(tokens)), cat=LpBinary)

        # Define the objective function to minimize the number of deleted tokens
        model = LpProblem("Extractive Compression", LpMinimize)
        model += lpSum([1 - x[i] for i in range(len(tokens))])

        # Define the constraints to ensure that the compressed text has the target length
        model += lpSum([x[i] for i in range(len(tokens))]) == target_length

        # Define the constraints to ensure that the compressed text is a subsequence of the original text
        for i in range(len(tokens)):
            for j in range(i+1, len(tokens)):
                if tokens[i] == tokens[j]:
                    model += x[i] <= x[j]

        # Solve the optimization problem
        model.solve()

        # Extract the indices of the selected tokens
        selected_indices = [i for i in range(len(tokens)) if x[i].value() == 1]

        # Generate the compressed text
        opti_prompt = " ".join([tokens[i] for i in selected_indices])
        return opti_prompt