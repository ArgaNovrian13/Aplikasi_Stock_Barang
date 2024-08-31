<template>
  <div>
    <!-- Check if there are any items to display -->
    <div v-if="items.length === 0" class="text-center text-danger">
      <p>Item Not Found</p>
    </div>

    <!-- Display the list of items -->
    <div v-else>
      <div
        v-for="item in items"
        :key="item.id"
        class="card mb-3"
        :class="{ 'border-danger': item.quantity < 50 }"
      >
        <div class="row g-0">
          <div class="col-md-4">
            <img
              :src="`http://localhost:5000/api/uploads/${item.image}`"
              class="img-fluid rounded-start"
              alt="Item Image"
              v-if="item.image"
            />
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">{{ item.name }}</h5>
              <p class="card-text">Quantity: {{ item.quantity }}</p>
              <!-- Low stock warning -->
              <div v-if="item.quantity < 50" class="text-danger">
                <strong>Warning: Low Stock!</strong>
              </div>
              <button @click="$emit('view', item)" class="btn btn-info me-2">
                View
              </button>
              <button @click="$emit('edit', item)" class="btn btn-warning me-2">
                Edit
              </button>
              <button @click="$emit('delete', item.id)" class="btn btn-danger">
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  items: {
    type: Array,
    required: true,
  },
});
</script>
