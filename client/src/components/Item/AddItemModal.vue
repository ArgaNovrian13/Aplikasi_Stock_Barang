<template>
  <div>
    <div class="modal-header">
      <h5 class="modal-title">Add New Item</h5>
      <button type="button" class="btn-close" @click="$emit('close')"></button>
    </div>
    <div class="modal-body">
      <form @submit.prevent="addItem">
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input
            v-model="name"
            type="text"
            class="form-control"
            id="name"
            required
          />
        </div>
        <div class="mb-3">
          <label for="quantity" class="form-label">Quantity</label>
          <input
            v-model="quantity"
            type="number"
            class="form-control"
            id="quantity"
            required
          />
        </div>
        <div class="mb-3">
          <label for="category" class="form-label">Category</label>
          <select
            v-model="category"
            class="form-control"
            id="category"
            required
          >
            <option value="electronics">Electronics</option>
            <option value="food">Food</option>
            <option value="office">Office Supplies</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="image" class="form-label">Image</label>
          <input
            type="file"
            @change="onFileChange"
            class="form-control"
            id="image"
          />
        </div>
        <button type="submit" class="btn btn-primary">Add Item</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import Swal from "sweetalert2";

const name = ref("");
const quantity = ref(0);
const category = ref("electronics"); // Default to "electronics"
const imageFile = ref(null);

const addItem = async () => {
  const formData = new FormData();
  formData.append("name", name.value);
  formData.append("quantity", quantity.value);
  formData.append("category", category.value); // Include category
  if (imageFile.value) {
    formData.append("image", imageFile.value);
  }

  try {
    await axios.post("/api/items", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    // Show success alert
    Swal.fire({
      title: "Success!",
      text: "Item has been added successfully.",
      icon: "success",
      confirmButtonText: "OK",
    }).then(() => {
      $emit("item-added");
      $emit("close");
    });
  } catch (error) {
    console.error("Failed to add item:", error);
    Swal.fire({
      title: "Error!",
      text: "Failed to add item. Please try again.",
      icon: "error",
      confirmButtonText: "OK",
    });
  }
};

const onFileChange = (event) => {
  imageFile.value = event.target.files[0];
};
</script>
