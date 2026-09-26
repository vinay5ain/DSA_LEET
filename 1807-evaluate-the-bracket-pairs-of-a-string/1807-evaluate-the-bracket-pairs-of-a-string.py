class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Convert knowledge list to dictionary for O(1) lookup
        # Each sublist [key, value] becomes a key-value pair
        knowledge_dict = {key: value for key, value in knowledge}
      
        # Initialize pointer and get string length
        index = 0
        string_length = len(s)
      
        # Result list to build the final string efficiently
        result = []
      
        # Process each character in the string
        while index < string_length:
            if s[index] == '(':
                # Found opening bracket, find the corresponding closing bracket
                closing_bracket_index = s.find(')', index + 1)
              
                # Extract the key between brackets (excluding the brackets themselves)
                key = s[index + 1 : closing_bracket_index]
              
                # Look up the key in dictionary, use '?' if key not found
                replacement_value = knowledge_dict.get(key, '?')
                result.append(replacement_value)
              
                # Move pointer to the closing bracket position
                index = closing_bracket_index
            else:
                # Regular character, add it directly to result
                result.append(s[index])
          
            # Move to next character
            index += 1
      
        # Join all parts into final string
        return ''.join(result)
