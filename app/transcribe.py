import subprocess
import os

def run_whisperx_cmd(audio_path):
    # Create the output directory if it doesn't exist
    output_dir = "transcricao"
    os.makedirs(output_dir, exist_ok=True)
    # Construct the command with the output directory
    command = f"whisperx {audio_path} --diarize --compute_type float32 --language Portuguese --output_dir {output_dir} --output_format txt"
    print(command)
    
    try:
        # Execute the command
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        return f"Error: Command failed with message: {e}"

    # Construct the path to the output file
    txt_file_path = os.path.join(output_dir, os.path.splitext(os.path.basename(audio_path))[0] + ".txt")
    
    # Check if the output file exists
    if os.path.exists(txt_file_path):
        # Read the content of the output file
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    else:
        return "Error: Transcription file not found."

    
    return content