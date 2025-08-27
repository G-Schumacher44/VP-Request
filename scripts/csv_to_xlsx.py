import os
import pandas as pd
import argparse

# --- Path Configuration ---
# Get the root directory of the repository
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def export_csv_folder_to_excel(input_folder_path, output_filepath):
    """
    Reads all CSV files from an input folder and saves them as sheets in a single Excel file.

    Args:
        input_folder_path (str): The absolute path to the folder containing CSV files.
        output_filepath (str): The absolute path for the output Excel file.
    """
    # Ensure the directory for the output file exists.
    output_dir = os.path.dirname(output_filepath)
    os.makedirs(output_dir, exist_ok=True)

    try:
        with pd.ExcelWriter(output_filepath) as writer:
            print(f"🔍 Reading CSVs from: {input_folder_path}")
            # Check if the input directory exists before trying to list its contents
            if not os.path.isdir(input_folder_path):
                print(f"⚠️  Warning: Input folder not found, skipping: {input_folder_path}")
                return

            for fname in os.listdir(input_folder_path):
                # Skip .DS_Store and non-CSV files
                if not fname.endswith(".csv") or fname.startswith("."):
                    continue

                fpath = os.path.join(input_folder_path, fname)
                # Use a clean sheet name (remove .csv, limit to 31 chars)
                sheet_name = os.path.splitext(fname)[0][:31]

                print(f"  - Processing '{fname}' into sheet '{sheet_name}'...")
                df = pd.read_csv(fpath)
                df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"✅ Successfully created Excel file: {output_filepath}")

    except Exception as e:
        print(f"❌ An error occurred while processing {input_folder_path}: {e}")

if __name__ == "__main__":
    def parse_args():
        parser = argparse.ArgumentParser(description="Export CSV folders from a story's output_data to Excel files.")
        parser.add_argument(
            "story_name",
            type=str,
            help="The name of the story directory to process (e.g., 'VP_Request')."
        )
        parser.add_argument(
            "--folder",
            type=str,
            default=None,
            help="Optional: A specific subfolder within the story's output_data to export (e.g., 'views'). If not provided, all subfolders will be processed."
        )
        return parser.parse_args()

    args = parse_args()
    story_name = args.story_name
    selected_folder = args.folder
    
    # Construct the base data directory path from the story name
    BASE_DATA_DIR = os.path.join(REPO_ROOT, story_name, "output_data")
    
    print("--- Starting Dynamic CSV to Excel Export ---")
    print(f"📂 Processing story: {story_name}")
    print(f"📂 Base data directory: {BASE_DATA_DIR}")

    if not os.path.isdir(BASE_DATA_DIR):
        print(f"❌ Error: Base data directory not found at '{BASE_DATA_DIR}'.")
        print("   Please ensure the directory exists and contains subfolders with CSV files.")
    else:
        folders_to_process = [selected_folder] if selected_folder else os.listdir(BASE_DATA_DIR)
        for item in folders_to_process:
            input_subdir_path = os.path.join(BASE_DATA_DIR, item)

            if os.path.isdir(input_subdir_path):
                output_filename = f"{item}_export.xlsx"
                output_filepath = os.path.join(BASE_DATA_DIR, output_filename)

                print(f"\n  -> Processing folder: '{item}' -> '{output_filename}'")
                export_csv_folder_to_excel(input_subdir_path, output_filepath)

    print("\n--- Export complete. ---")