# Entrypoint for the grader that writes a funny line to the specified output file.
# Entry validated: output is 1-200 chars, one funny line, deterministic.
import os
import pathlib

# Define the exact funny line required by the prompt.
LINE = "The password manager locked itself out of the vault and now refuses to speak to me until I provide three childhood memories."

def main():
    # Determine the output directory from the environment or default to 'out'.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    output_dir_path = pathlib.Path(out_dir)
    
    # Create the output directory if it does not exist.
    output_dir_path.mkdir(parents=True, exist_ok=True)
    
    # Build the target file path.
    output_file = output_dir_path / "entry.txt"
    
    # Prepare the content with a single trailing newline.
    content = LINE + "\n"
    
    # Validate the content according to the exact rule specified.
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")
    
    # Write the content to the file using UTF-8 encoding.
    output_file.write_text(content, encoding="utf-8")
    
    # Print the output path and the total character count.
    print(str(output_file))
    print(len(content))

if __name__ == "__main__":
    main()
