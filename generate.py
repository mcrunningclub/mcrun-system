"""Simple script to automatically parse docstrings from a js file and output to a Markdown file.

Please double check output results as there may be inaccuracies due to the nature of regex parsing. This script is not perfect and may not handle all edge cases.

Usage: `python generate.py <input_file> <output_file>`
"""


import re
import argparse

EMPTY_LINE_REGEX = re.compile(r"^ \* (\s*)\n$")
DOCSTRING_REGEX = re.compile(r"^ \* ([^@].+\n)$")
PARAM_REGEX = re.compile(r"^ \* @param {(.+)}\s+(.+)\s+(.+\n)$")
RETURN_REGEX = re.compile(r"^ \* @return {(.+)}\s+(.+\n)$")
FUNC_DEF_REGEX = re.compile(r"^\s*function ([^\(]+\(.*\))\s*{")

def parse_docstring(file_path, output_file_path):
    """Iterates through file and parses docstrings

    Args:
        file_path (str): Path to input file with docstrings in JSDoc format
        output_file_path (str): Path to output file in markdown

    Returns:
        None
    """
    in_param = False
    in_return = False
    in_comment = False

    newlines = []
    cur_comment = []

    with open(file_path, "r") as f:
        for line in f:
            # If not inside a comment block just continue, unless comment block starts
            if not in_comment:
                if line.startswith("/**"):
                    in_comment = True
                else:
                    continue

            # If inside a comment block, handle comment line

            # Comment ends at start of function def
            if FUNC_DEF_REGEX.match(line):
                # Get function name
                cur_comment.insert(0, re.sub(FUNC_DEF_REGEX, r"#### \1\n", line))

                # Move out of comment block
                in_comment = False
                newlines.extend(cur_comment)
                newlines.append("\n")
                cur_comment.clear()
                continue

            # Regular docstring line
            if DOCSTRING_REGEX.fullmatch(line):
                if in_param:
                    in_param = False
                if in_return:
                    in_return = False
                newline = re.sub(DOCSTRING_REGEX, r"\1", line)
                cur_comment.append(newline)

            # Empty docstring line
            elif EMPTY_LINE_REGEX.fullmatch(line):
                if in_param:
                    in_param = False
                if in_return:
                    in_return = False
                cur_comment.append("\n")

            # Parameter line
            elif PARAM_REGEX.fullmatch(line):
                if in_return:
                    in_return = False
                if not in_param:
                    cur_comment.append("Params:\n\n")
                    in_param = True
                newline = re.sub(PARAM_REGEX, r"- `\2` (\1) - \3", line)
                cur_comment.append(newline)

            # Return line
            elif RETURN_REGEX.fullmatch(line):
                if in_param:
                    cur_comment.append("\n")
                    in_param = False
                if not in_return:
                    cur_comment.append("Returns:\n\n")
                    in_return = True
                newline = re.sub(RETURN_REGEX, r"- (\1) - \2", line)
                cur_comment.append(newline)

    with open(output_file_path, "w") as f:
        f.writelines(newlines)

def main():
    """Reads input and output files from command line args
    """
    
    parser = argparse.ArgumentParser(description="Parse docstrings from a js file and output to a Markdown file.")
    parser.add_argument("input_file", help="Path to input file with docstrings in JSDoc format.")
    parser.add_argument("output_file", help="Path to output Markdown file.")
    args = parser.parse_args()

    parse_docstring(args.input_file, args.output_file)

if __name__ == "__main__":
    main()