from clipsai import clip, transcribe

transcripiton = transcribe("doc_2024-01-06_18-36-52.mp4")
clips = clip(transcripiton)

print("StartTime: ", clips[0].start_time)
print("EndTime: ", clips[0].end_time)
