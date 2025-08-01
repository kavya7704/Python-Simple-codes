def minimize_badness(s):
    # Replace white houses with either 'R' or 'B' and calculate badness for each case
    def calculate_badness(string):
        badness = 0
        for i in range(1, len(string)):
            if string[i] != string[i - 1]:
                badness += 1
        return badness

    # Replace whites ('W') with 'R' in one scenario and 'B' in another
    scenario_red = s.replace('W', 'R')
    scenario_blue = s.replace('W', 'B')

    # Calculate badness for both scenarios
    badness_red = calculate_badness(scenario_red)
    badness_blue = calculate_badness(scenario_blue)

    # Return the minimum badness
    return min(badness_red, badness_blue)

# Example usage
input_string = "RRWBWBW"
result = minimize_badness(input_string)
print(result)  # Output: 1
