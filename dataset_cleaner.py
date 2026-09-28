# dataset_cleaner.py
# A simple utility to remove duplicate lines from a text dataset.

def clean_dataset(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Remove duplicates while preserving order
        seen = set()
        cleaned_lines = []
        for line in lines:
            if line.strip() and line not in seen:
                cleaned_lines.append(line)
                seen.add(line)
                
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(cleaned_lines)
            
        print(f"Success! Removed {len(lines) - len(cleaned_lines)} duplicate lines.")
        print(f"Saved to {output_file}")
        
    except FileNotFoundError:
        print("Error: Input file not found.")

if __name__ == "__main__":
    # Example usage
    clean_dataset("raw_data.txt", "cleaned_data.txt")
