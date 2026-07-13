"""Simple script to automatically parse docstrings from a js file and output to a Markdown file.

Please double check output results as there may be inaccuracies due to the nature of regex parsing. This script is not perfect and may not handle all edge cases.

Usage: `python generate.py <input_file> <output_file>`
"""

import re
import os
import argparse

EMPTY_LINE_REGEX = re.compile(r"^ \* (\s*)\n$")
DOCSTRING_REGEX = re.compile(r"^ \* ([^@].+)\n$")
PARAM_REGEX = re.compile(r"^ \* @param\s+{([^ ]+)}\s+([^ ]+) -?\s*(.+)\n$")
RETURN_REGEX = re.compile(r"^ \* @returns? {([^ ]+)} -?\s*(.+)\n$")
FUNC_DEF_REGEX = re.compile(r"^\s*function ([^\(]+\(.*\))\s*{")
CONSTANT_REGEX = re.compile(r"^const (.+) = (.+)\n$")

DOCSTRING_REPLACE = r"\1\n"
PARAM_REPLACE = r"- `\2` (\1) - \3\n"
RETURN_REPLACE = r"- (\1) - \2\n"
FUNC_DEF_REPLACE = r"#### \1\n"
CONSTANT_REPLACE = r"#### \1\n\n"


def make_toc_line(name, is_function=True):
    """Creates a table of contents line for a given function or constant

    Args:
        name (str): Name of the function
        is_function (bool): Whether the item is a function

    Returns:
        str: Table of contents line
    """
    link = name.lower().replace(" ", "-")
    link = re.sub(r"[^a-z0-9\-_]", "", link)

    if is_function:
        return f"- *function* [`{name}`](#{link})\n"
    else:
        return f"- *constant* [`{name}`](#{link})\n"


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
    toc = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            # If not inside a comment block just continue, unless comment block starts
            if not in_comment:
                if line.startswith("/**"):
                    print(f"Found comment block: {line.strip()}")
                    in_comment = True

                    # Clearn comment block in case
                    cur_comment.clear()
                continue

            # Inside comment, handle line or end comment
            else:
                # Get function name if comment block has ended
                if line.startswith("function"):
                    # Get function name
                    header_line = FUNC_DEF_REGEX.sub(FUNC_DEF_REPLACE, line)
                    name = FUNC_DEF_REGEX.match(line).group(1)
                    cur_comment.insert(0, header_line)
                    print(f"Comment block ended with func: {name}")

                    # Stop searching
                    in_comment = False

                    # Add comment block to documentation and clear current comment
                    newlines.extend(cur_comment)
                    newlines.append("\n")
                    cur_comment.clear()

                    # Add function to table of contents
                    toc.append(make_toc_line(name))
                    continue

                # Or get constant name
                elif line.startswith("const"):
                    header_line = CONSTANT_REGEX.sub(CONSTANT_REPLACE, line)
                    name = CONSTANT_REGEX.match(line).group(1)
                    cur_comment.insert(0, header_line)
                    print(f"Comment block ended with const: {name}")

                    # Not a function, stop searching
                    in_comment = False

                    # Add comment block to documentation and clear current comment
                    newlines.extend(cur_comment)
                    newlines.append("\n")
                    cur_comment.clear()

                    # Add constant to table of contents
                    toc.append(make_toc_line(name, is_function=False))
                    continue

                # Empty docstring line
                elif EMPTY_LINE_REGEX.fullmatch(line):
                    if in_param:
                        in_param = False
                    if in_return:
                        in_return = False
                    if cur_comment[-1] != "\n":
                        cur_comment.append("\n")

                # Regular docstring line
                elif DOCSTRING_REGEX.fullmatch(line):
                    if in_param:
                        in_param = False
                    if in_return:
                        in_return = False
                    newline = DOCSTRING_REGEX.sub(DOCSTRING_REPLACE, line)
                    cur_comment.append(newline)

                # Parameter line
                elif PARAM_REGEX.fullmatch(line):
                    if in_return:
                        in_return = False
                    if not in_param:
                        # Add paragraph break in case there isn't any
                        if cur_comment[-1] != "\n":
                            cur_comment.append("\n")
                        cur_comment.append("Params:\n\n")
                        in_param = True
                    newline = PARAM_REGEX.sub(PARAM_REPLACE, line)
                    cur_comment.append(newline)

                # Return line
                elif RETURN_REGEX.fullmatch(line):
                    if in_param:
                        cur_comment.append("\n")
                        in_param = False
                    if not in_return:
                        # Add paragraph break in case there isn't any
                        if cur_comment[-1] != "\n":
                            cur_comment.append("\n")
                        cur_comment.append("Returns:\n\n")
                        in_return = True
                    newline = RETURN_REGEX.sub(RETURN_REPLACE, line)
                    cur_comment.append(newline)

    # Make final content to write
    documentation = []

    # Add name of file as header
    file_name = os.path.basename(file_path)
    documentation.append(f"### {file_name}\n\n")

    # Add table of contents and parsed comments
    documentation.extend(toc)
    documentation.append("\n")
    documentation.extend(newlines)

    with open(output_file_path, "w", encoding="utf-8") as f:
        f.writelines(documentation)


def main():
    """Reads input and output files from command line args"""

    parser = argparse.ArgumentParser(
        description="Parse docstrings from a js file and output to a Markdown file."
    )
    parser.add_argument(
        "input_file", help="Path to input file with docstrings in JSDoc format."
    )
    parser.add_argument("output_file", help="Path to output Markdown file.")
    args = parser.parse_args()

    parse_docstring(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
