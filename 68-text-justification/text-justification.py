# Problem Summary:
# Inputs: array of strings words, and a width, maxWidth

# Task: Format the text such that each line has EXACTLY maxWidth characters
# fully (left/right) justified

# Complexities/Constraints: words are non-empty, each word length
# is at most 'maxWidth', pack words greedily per line

# Edge Cases: single word line, last line, line with one word, uneven
# space disttribution where left slots get more spaces (test-cases)

# Outputs: list of strings where each line is exactly maxWidth
# full justification except the last line which is left justified

# Naive/Non-Optimal Approach:
# Build each line greedily, then repeatedly cycle over gaps and add
# one space to each until the line reaches maxWidth
# O(total characters in line time gaps) per line => quadratic time
# in total characters => nested loops O(number of nests) => O(n^4)

# Approach:
# Greedy collect words that fit in a line
# for non last line, let g = # of gaps, spaces = maxWidth - sum(lengths)
# Use mod operator to mod spaces by gaps
# divmod => floored operation of divisor // dividend, remainder
# q, r = divmod(spaces, g)
# q = how many words can fit, remaining spaces
# leftmost r gaps get q + 1 spaces, the rest get q spaces
# for last line or line with one word, right pad spaces to reach maxWidth
# Time-Complexity: O(n), over total characters since each word
# is visited a constant number of times, n is len(words)
# Space-Complexity: O(n), for the output, O(1) extra space

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0

        # traverse words
        while i < len(words):
            # total letters length in the current line
            line_len = 0
            start = i

            # greedily take as many words as fit
            while i < len(words):
                word_len = len(words[i])
                # if we take k words, there are k - 1 gaps
                # future spaces count is (i - start)
                needed = line_len + word_len + (i - start)
                if needed > maxWidth:
                    break
                
                # add current word to line, increment to next word
                line_len += word_len
                i += 1

            last_line = (i == len(words))
            num_words = i - start
            if num_words == 1 or last_line:
                # left justified line or single word line
                # single spaces between words
                line = " ".join(words[start:i])
                spaces_to_pad = maxWidth - len(line)
                line = line + " " * spaces_to_pad
                res.append(line)
                continue

            # full justification with even distribution across gaps
            gaps = num_words - 1
            total_spaces = maxWidth - line_len
            # base spaces per gap, extra spaces
            # build the line by assigning base spaces to all gaps
            base, extra = divmod(total_spaces, gaps)

            # collect alternating words and spaces
            parts = []
            for k in range(num_words):
                # add the word
                parts.append(words[start + k])
                if k < gaps:
                    # determine how many spaces this gap should get
                    gap_spaces = 0
                    if k < extra:
                        gap_spaces = base + 1
                    else:
                        gap_spaces = base
                    parts.append(" " * gap_spaces)
            
            res.append("".join(parts))

        return res
