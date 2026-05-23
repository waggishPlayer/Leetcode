class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""
            
        have = 0
        need = len(set(t))
        left = 0
        right = 0
        store = {}
        
        for char in t:
            if char not in store:
                store[char] = 0
            store[char] += 1
            
        # 1. We need a dictionary to track our current window's characters
        window = {}
        
        # 2. Variables to store the BEST indices and the BEST length we've found
        res = [-1, -1] 
        res_len = float("infinity")

        while right < len(s):
            # --- EXPANDING THE WINDOW ---
            char = s[right]
            # Add the current character to our window dictionary
            if char not in window:
                window[char] = 0
            window[char] += 1

            # If the character is one we need, and we just reached the exact frequency we need
            if char in store and window[char] == store[char]:
                have += 1

            # --- SHRINKING THE WINDOW ---
            # As long as our window has all the characters we need, try to shrink it
            while have == need:
                # First, check if this is the smallest window we've seen so far
                current_window_size = (right - left) + 1
                if current_window_size < res_len:
                    # If it is, save the size and the indices!
                    res = [left, right]
                    res_len = current_window_size

                # Now, try shrinking by removing the left-most character
                left_char = s[left]
                window[left_char] -= 1

                # If removing that character dropped its count below what we need,
                # we no longer "have" all required characters.
                if left_char in store and window[left_char] < store[left_char]:
                    have -= 1

                # Move the left pointer forward
                left += 1

            # Move the right pointer forward to look for more characters
            right += 1

        # --- RETURNING THE RESULT ---
        # Unpack our saved best indices
        best_left, best_right = res
        
        # If res_len is still infinity, we never found a valid window
        if res_len != float("infinity"):
            # Slice the original string using our saved indices
            return s[best_left : best_right + 1]
        else:
            return ""