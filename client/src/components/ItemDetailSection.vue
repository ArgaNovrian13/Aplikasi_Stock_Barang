<template>
  <div class="container mt-4">
    <div class="card mb-4">
      <div class="card-body">
        <h3 class="card-title mb-3">Item Detail</h3>
        <div class="row">
          <div class="col-md-6">
            <div v-if="item.image" class="mb-3">
              <img
                :src="`http://localhost:5000/api/uploads/${item.image}`"
                alt="Item Image"
                class="img-fluid rounded"
              />
            </div>
            <div v-if="!item.image" class="text-muted">No image available</div>
          </div>
          <div class="col-md-6">
            <p><strong>Name:</strong> {{ item.name }}</p>
            <p><strong>Quantity:</strong> {{ item.quantity }}</p>
          </div>
        </div>
        <button class="btn btn-secondary mt-3" @click="$emit('close')">
          Close
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  item: Object,
});
</script>

<style scoped>
.card {
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-title {
  font-size: 1.5rem;
  font-weight: 500;
}

.btn-secondary {
  background-color: #6c757d;
  border-color: #6c757d;
}

.btn-secondary:hover {
  background-color: #5a6268;
  border-color: #545b62;
}
</style>
