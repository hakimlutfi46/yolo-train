import os

# Path ke folder dataset
dataset_path = r'D:\Kuliah\Semester_5\Project\yolo_train\datasets\valid\belum matang'

# Default label untuk stroberi matang dengan bounding box lebih besar
# Format: <class_id> <x_center> <y_center> <width> <height>
default_label = "0 0.5 0.5 0.9 0.9"  # Perbesar bounding box (ubah width dan height ke 0.6)

# Loop untuk membuat ulang file label .txt
for file_name in os.listdir(dataset_path):
    if file_name.endswith(('.jpg', '.jpeg', '.png')):  # Cek file gambar
        label_file_name = os.path.splitext(file_name)[0] + ".txt"  # Ganti ekstensi ke .txt
        label_file_path = os.path.join(dataset_path, label_file_name)

        # Buat atau timpa file label
        with open(label_file_path, 'w') as f:
            f.write(default_label)  # Tulis default label
        print(f"Label diperbarui untuk {file_name}: {label_file_name}")
