<template>
  <section id="lawyers" class="section lawyers-section">
    <div class="container">
      <h2 class="section-title">Наши юристы</h2>
      
      <div v-if="loading" class="loading">Загрузка...</div>
      
      <div v-else class="lawyers-grid">
        <div v-for="lawyer in lawyers" :key="lawyer.id" class="lawyer-card">
          <div class="lawyer-image-wrapper">
            <img 
              v-if="lawyer.photo" 
              :src="lawyer.photo" 
              :alt="lawyer.full_name"
              class="lawyer-image"
            />
            <div v-else class="lawyer-image-placeholder">
              👤
            </div>
            
            <div class="lawyer-overlay">
              <div class="lawyer-bio">
                <p>{{ lawyer.bio }}</p>
                <p v-if="lawyer.experience_text" class="lawyer-experience">
                  ⭐ {{ lawyer.experience_text }}
                </p>
                <div v-if="lawyer.specialization && lawyer.specialization.length" class="lawyer-specialization">
                  <strong>Специализация:</strong>
                  <ul>
                    <li v-for="service in lawyer.specialization" :key="service.id">
                      {{ service.name }}
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          
          <div class="lawyer-info">
            <h3 class="lawyer-name">{{ lawyer.full_name }}</h3>
            <p class="lawyer-position">{{ lawyer.position }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { onMounted } from 'vue'
import { useLawyerStore } from '../stores/lawyer'
import { storeToRefs } from 'pinia'

export default {
  name: 'LawyersSection',
  setup() {
    const store = useLawyerStore()
    const { lawyers, loading } = storeToRefs(store)

    onMounted(() => {
      if (lawyers.value.length === 0) {
        store.fetchLawyers()
      }
    })

    return {
      lawyers,
      loading,
    }
  },
}
</script>

<style scoped>
.lawyers-section {
  background: var(--bg-light);
}

.lawyers-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

.lawyer-card {
  background: var(--white);
  border-radius: var(--radius-sm);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition-normal);
}

.lawyer-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-4px);
}

.lawyer-image-wrapper {
  position: relative;
  width: 100%;
  height: 350px;
  overflow: hidden;
}

.lawyer-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.lawyer-image-placeholder {
  width: 100%;
  height: 100%;
  background: var(--bg-light);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 100px;
}

.lawyer-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(74, 144, 226, 0.95);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: var(--transition-normal);
  padding: 20px;
}

.lawyer-card:hover .lawyer-overlay {
  opacity: 1;
}

.lawyer-bio {
  color: var(--white);
  text-align: center;
}

.lawyer-bio p {
  margin-bottom: 15px;
  line-height: 1.6;
}

.lawyer-experience {
  font-weight: 600;
}

.lawyer-specialization {
  margin-top: 15px;
  text-align: left;
}

.lawyer-specialization ul {
  margin-top: 10px;
  padding-left: 20px;
}

.lawyer-specialization li {
  list-style: disc;
  margin-bottom: 5px;
}

.lawyer-info {
  padding: 20px;
  text-align: center;
}

.lawyer-name {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 5px;
  color: var(--dark-color);
}

.lawyer-position {
  color: var(--text-light);
  font-size: 16px;
}

/* Responsive */
@media (max-width: 992px) {
  .lawyers-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .lawyers-grid {
    grid-template-columns: 1fr;
  }

  .lawyer-image-wrapper {
    height: 300px;
  }
}
</style>


