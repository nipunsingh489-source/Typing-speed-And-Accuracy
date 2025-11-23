import time

sample_text = "The journey of a thousand miles begins with one step."

print("\nType the following text:")
print(sample_text)
input("\nPress Enter when you are ready...")

start = time.time()
typed_text = input("\nStart typing:\n")
end = time.time()

# Time taken in minutes
time_taken = (end - start) / 60

# Count words
sample_words = sample_text.split()
typed_words = typed_text.split()

total_words = len(typed_words)

# Count correct words
correct = 0
for i in range(min(len(sample_words), len(typed_words))):
    if sample_words[i] == typed_words[i]:
        correct += 1

# Calculate Accuracy & WPM
wpm = total_words / time_taken
accuracy = (correct / len(sample_words)) * 100

print("\n--- Result ---")
print(f"Time Taken : {time_taken:.2f} minutes")
print(f" Speed: {wpm:.2f} WPM")
print(f"Accuracy: {accuracy:.2f}%")