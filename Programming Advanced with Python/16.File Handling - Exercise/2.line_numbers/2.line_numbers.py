from string import punctuation

with open('text.txt') as input_file, open('output.txt', 'w') as output_file:
    result = []
    for row, line in enumerate(input_file):
        letters_count = 0
        punc_count = 0
        for ch in line:
            if ch.isalpha():
                letters_count += 1
            elif ch in punctuation:
                punc_count += 1
        result.append(f"Line {row + 1}: {line[:-1]} ({letters_count})({punc_count})")
    output_file.write('\n'.join(result))

# {line.strip()}
# enumerate(input_file, start=1) remove +1 in line 13 {row}

# variant 2
# from string import punctuation
#
# result = []
#
# with open('text.txt') as input_file:
#     for row, line in enumerate(input_file):
#         letters_count = 0
#         punc_count = 0
#         for ch in line:
#             if ch.isalpha():
#                 letters_count += 1
#             elif ch in punctuation:
#                 punc_count += 1
#         result.append(f"Line {row + 1}: {line.strip()} ({letters_count})({punc_count})")
#
# with open('output.txt', 'w') as output_file:
#     output_file.write('\n'.join(result))
