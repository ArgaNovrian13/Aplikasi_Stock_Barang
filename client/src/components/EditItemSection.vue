<template>
  <div class="container mt-5">
    <h3 class="mb-4">Edit Item</h3>
    <form @submit.prevent="handleUpdate">
      <div class="mb-3">
        <label for="editName" class="form-label">Name:</label>
        <input
          v-model="item.name"
          id="editName"
          class="form-control"
          placeholder="Enter item name"
          required
        />
      </div>
      <div class="mb-3">
        <label for="editQuantity" class="form-label">Quantity:</label>
        <input
          v-model="item.quantity"
          id="editQuantity"
          type="number"
          class="form-control"
          placeholder="Enter quantity"
          required
        />
      </div>
      <div class="mb-3">
        <label for="editImage" class="form-label">Image:</label>
        <input
          type="file"
          id="editImage"
          class="form-control"
          @change="handleFileChange"
        />
        <!-- Tampilkan gambar yang sudah ada jika tersedia -->
        <div v-if="item.image && !newImageUrl" class="mt-2">
          <img
            :src="`http://localhost:5000/api/uploads/${item.image}`"
            alt="Current Image"
            class="img-thumbnail"
            style="max-width: 200px"
          />
        </div>
        <!-- Tampilkan preview gambar baru jika ada -->
        <div v-if="newImageUrl" class="mt-2">
          <img
            :src="newImageUrl"
            alt="New Image Preview"
            class="img-thumbnail"
            style="max-width: 200px"
          />
        </div>
      </div>
      <button type="submit" class="btn btn-success w-100">Save Changes</button>
      <button
        type="button"
        class="btn btn-secondary w-100 mt-2"
        @click="$emit('close')"
      >
        Cancel
      </button>
    </form>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, reactive, ref } from "vue";
import axios from "axios";
import Swal from "sweetalert2";

const props = defineProps({
  item: Object,
});

const emit = defineEmits(["close", "item-updated"]);

const item = reactive({ ...props.item });
const newImageFile = ref(null); // Untuk menyimpan file gambar baru
const newImageUrl = ref(null); // Untuk menyimpan URL preview gambar baru

// Tangani perubahan file gambar untuk preview
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    newImageFile.value = file;
    newImageUrl.value = URL.createObjectURL(file); // Buat URL objek untuk preview gambar // Debug log untuk memeriksa URL
  }
};

const handleUpdate = async () => {
  try {
    const formData = new FormData();
    formData.append("name", item.name);
    formData.append("quantity", item.quantity);
    if (newImageFile.value) {
      formData.append("image", newImageFile.value);
    }

    await axios.put(`/api/items/${item.id}`, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    // Tampilkan notifikasi SweetAlert
    Swal.fire({
      title: "Success!",
      text: "Item updated successfully.",
      icon: "success",
      confirmButtonText: "OK",
    }).then(() => {
      emit("item-updated"); // Beritahu komponen induk untuk menyegarkan data
      emit("close"); // Tutup modal
    });
  } catch (error) {
    console.error("Failed to update item:", error);
    Swal.fire({
      title: "Error!",
      text: "Failed to update item.",
      icon: "error",
      confirmButtonText: "OK",
    });
  } finally {
    // Hapus URL objek setelah digunakan untuk menghindari kebocoran memori
    if (newImageUrl.value) {
      URL.revokeObjectURL(newImageUrl.value);
    }
  }
};
</script>
