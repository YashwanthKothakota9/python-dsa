# Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.

# Example 1:

# Input: "1+2*3"
# Output: 7, 9
# Explanation: 
#   1+(2*3) => 7
#   (1+2)*3 => 9
# Example 2:

# Input: "2*3-4-5"
# Output: 8, -12, 7, -7, -3 
# Explanation: 
#   2*(3-(4-5)) => 8
#   2*(3-4-5) => -12
#   2*3-(4-5) => 7
#   2*(3-4)-5 => -7
#   (2*3)-4-5 => -3
  
  
# This problem follows the Subsets pattern and can be mapped to Balanced Parentheses. We can follow a similar BFS approach.

# Let’s take Example-1 mentioned above to generate different ways to evaluate the expression.

# We can iterate through the expression character-by-character.
# we can break the expression into two halves whenever we get an operator (+, -, *).
# The two parts can be calculated by recursively calling the function.
# Once we have the evaluation results from the left and right halves, we can combine them to produce all results.

class Solution:
    def diffWaysToEvaluateExpression(self, input):
        result = []
        # base case: if the input string is a number, parse and add it to output.
        if '+' not in input and '-' not in input and '*' not in input:
            result.append(int(input))
        else:
            for i in range(0, len(input)):
                char = input [i]
                if not char.isdigit():
                    # break the equation here into two parts and make recursively calls
                    leftParts = self.diffWaysToEvaluateExpression(input[0:i])
                    rightParts = self.diffWaysToEvaluateExpression(input[i+1:])
                    for part1 in leftParts:
                        for part2 in rightParts:
                            if char == '+':
                                result.append(part1 + part2)
                            elif char == '-':
                                result.append(part1 - part2)
                            elif char == '*':
                                result.append(part1 * part2)
        return result

def main():
  sol = Solution()
  print("Expression evaluations: " +
        str(sol.diffWaysToEvaluateExpression("1+2*3")))

  print("Expression evaluations: " +
        str(sol.diffWaysToEvaluateExpression("2*3-4-5")))


main()

# Tc: O(N*2^N) Sc: O(2^N)


# ------------------------------------------------------------------

# Recursive with memoization

class Solution2:
  def diffWaysToEvaluateExpression(self, input):
    return self.diff_ways_to_evaluate_expression_rec({}, input)


  def diff_ways_to_evaluate_expression_rec(self, map, input):
    if input in map:
      return map[input]

    result = []
    # base case: if the input string is a number, parse and return it.
    if '+' not in input and '-' not in input and '*' not in input:
      result.append(int(input))
    else:
      for i in range(0, len(input)):
        char = input[i]
        if not char.isdigit():
          # break the equation here into two parts and make recursively calls
          leftParts = self.diff_ways_to_evaluate_expression_rec(
            map, input[0:i])
          rightParts = self.diff_ways_to_evaluate_expression_rec(
            map, input[i+1:])
          for part1 in leftParts:
            for part2 in rightParts:
              if char == '+':
                result.append(part1 + part2)
              elif char == '-':
                result.append(part1 - part2)
              elif char == '*':
                result.append(part1 * part2)

    map[input] = result
    return result


def main2():
  sol = Solution2()
  print("Expression evaluations: " +
        str(sol.diffWaysToEvaluateExpression("1+2*3")))

  print("Expression evaluations: " +
        str(sol.diffWaysToEvaluateExpression("2*3-4-5")))


main2()

# Time Complexity
# The time complexity of the given code is O(n*2^n), where (n) is the length of the input string. This complexity arises from:

# Recursive Calls: The function recursively splits the input string at each operator. For each operator, it recursively evaluates all possible left and right subexpressions. This results in exponential growth in the number of subproblems.

# Work per Subproblem: For each recursive call, the function performs O(n) work to split the string and process the results from the subexpressions.

# Space Complexity
# The space complexity is O(2^n*n), due to:

# Memoization Map: The map stores results for each unique subexpression, potentially resulting in 2^n different entries.

# Recursive Call Stack: The depth of the recursion tree can be (O(n)) in the worst case, where (n) is the length of the input string.