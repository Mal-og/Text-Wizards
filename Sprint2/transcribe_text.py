import os
import whisper

def transcribe_audio_files(folder_path):
    model = whisper.load_model("base")  
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if file_path.lower().endswith(('.mp3', '.wav', '.m4a', '.flac')):
            print(f"Processing: {filename}")
            
            result = model.transcribe(file_path)
            
            text = result['text']
            
            print(f"Transcription for {filename}:\n{text}\n")
            
            with open(f"{file_path}.txt", "w") as text_file:
                text_file.write(text)

if __name__ == "__main__":
    folder_path = ''  
    transcribe_audio_files(folder_path)
