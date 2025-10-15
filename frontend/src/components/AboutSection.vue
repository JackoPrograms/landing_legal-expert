<template>
  <section id="about" class="section about-section">
    <div class="container">
      <div class="about-content">
        <div class="about-text">
          <h2>О компании</h2>
          <h3 v-if="companyInfo">{{ companyInfo.company_name }}</h3>
          <p v-if="companyInfo" v-html="companyInfo.description"></p>
          <div class="about-buttons">
            <button class="btn btn-primary" @click="$emit('open-modal')">Записаться на консультацию</button>
            <a href="#services" class="btn btn-outline">Наши услуги</a>
          </div>
        </div>
        <div class="about-image">
          <img src="https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=600&h=400&fit=crop" alt="Юридические услуги" />
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
  name: 'AboutSection',
  emits: ['open-modal'],
  setup() {
    const store = useLawyerStore()
    const { companyInfo } = storeToRefs(store)

    onMounted(() => {
      if (!companyInfo.value) {
        store.fetchCompanyInfo()
      }
    })

    return {
      companyInfo,
    }
  },
}
</script>

<style scoped>
.about-section {
  background: var(--white);
}

.about-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.about-text h2 {
  font-size: 36px;
  color: var(--dark-color);
  margin-bottom: 10px;
}

.about-text h3 {
  font-size: 28px;
  color: var(--primary-color);
  margin-bottom: 20px;
}

.about-text p {
  color: var(--text-light);
  line-height: 1.8;
  margin-bottom: 30px;
}

.about-buttons {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.about-image img {
  width: 100%;
  height: auto;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
}

/* Responsive */
@media (max-width: 992px) {
  .about-content {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .about-text {
    text-align: center;
  }

  .about-buttons {
    justify-content: center;
  }
}

@media (max-width: 768px) {
  .about-text h2 {
    font-size: 28px;
  }

  .about-text h3 {
    font-size: 24px;
  }

  .about-buttons {
    flex-direction: column;
  }

  .about-buttons .btn {
    width: 100%;
  }
}
</style>


