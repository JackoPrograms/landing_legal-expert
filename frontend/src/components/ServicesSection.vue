<template>
  <section id="services" class="section services-section">
    <div class="container">
      <h2 class="section-title">Наши услуги</h2>
      
      <div v-if="loading" class="loading">Загрузка услуг...</div>
      
      <div v-else class="services-grid">
        <div v-for="service in services" :key="service.id" class="service-card card">
          <div class="service-icon">{{ service.icon }}</div>
          <h3 class="service-name">{{ service.name }}</h3>
          <p class="service-description">{{ service.short_description }}</p>
        </div>
      </div>

      <div class="services-footer">
        <button class="btn btn-outline">Все услуги</button>
      </div>
    </div>
  </section>
</template>

<script>
import { onMounted } from 'vue'
import { useLawyerStore } from '../stores/lawyer'
import { storeToRefs } from 'pinia'

export default {
  name: 'ServicesSection',
  setup() {
    const store = useLawyerStore()
    const { services, loading } = storeToRefs(store)

    onMounted(() => {
      if (services.value.length === 0) {
        store.fetchServices()
      }
    })

    return {
      services,
      loading,
    }
  },
}
</script>

<style scoped>
.services-section {
  background: var(--bg-light);
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
  margin-bottom: 40px;
}

.service-card {
  text-align: center;
  padding: 40px 30px;
  transition: var(--transition-normal);
}

.service-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-lg);
}

.service-icon {
  font-size: 64px;
  margin-bottom: 20px;
}

.service-name {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 15px;
  color: var(--dark-color);
}

.service-description {
  color: var(--text-light);
  line-height: 1.6;
}

.services-footer {
  text-align: center;
}

/* Responsive */
@media (max-width: 992px) {
  .services-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .services-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .service-card {
    padding: 30px 20px;
  }
}
</style>


