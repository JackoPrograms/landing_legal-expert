<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <!-- Company Info -->
        <div class="footer-col">
          <h3>{{ companyInfo?.company_name || 'ПРАВОЗАЩИТНИК' }}</h3>
          <p v-if="companyInfo?.slogan">{{ companyInfo.slogan }}</p>
          <div v-if="companyInfo" class="footer-social">
            <a v-if="companyInfo.vk_link" :href="companyInfo.vk_link" target="_blank" class="social-link">VK</a>
            <a v-if="companyInfo.telegram_link" :href="companyInfo.telegram_link" target="_blank" class="social-link">Telegram</a>
            <a v-if="companyInfo.whatsapp_link" :href="`https://wa.me/${companyInfo.whatsapp_link}`" target="_blank" class="social-link">WhatsApp</a>
          </div>
        </div>

        <!-- Services -->
        <div class="footer-col">
          <h4>Услуги</h4>
          <ul class="footer-links">
            <li v-for="service in services.slice(0, 6)" :key="service.id">
              <a :href="`#service-${service.slug}`">{{ service.name }}</a>
            </li>
          </ul>
        </div>

        <!-- Contacts -->
        <div class="footer-col">
          <h4>Контакты</h4>
          <ul v-if="companyInfo" class="footer-contacts">
            <li>
              <span>📞</span>
              <a :href="`tel:${companyInfo.phone}`">{{ companyInfo.phone }}</a>
            </li>
            <li>
              <span>✉️</span>
              <a :href="`mailto:${companyInfo.email}`">{{ companyInfo.email }}</a>
            </li>
            <li v-if="companyInfo.address">
              <span>📍</span>
              <span>{{ companyInfo.address }}</span>
            </li>
          </ul>
        </div>

        <!-- Lawyer Card -->
        <div class="footer-col">
          <h4>Записаться на консультацию</h4>
          <div v-if="mainLawyer" class="footer-lawyer-card">
            <img v-if="mainLawyer.photo" :src="mainLawyer.photo" :alt="mainLawyer.full_name" class="lawyer-photo" />
            <div class="lawyer-info">
              <p class="lawyer-name">{{ mainLawyer.full_name }}</p>
              <p class="lawyer-position">{{ mainLawyer.position }}</p>
            </div>
            <button class="btn btn-primary btn-block" @click="$emit('open-modal')">
              Записаться
            </button>
          </div>
        </div>
      </div>

      <!-- Copyright -->
      <div class="footer-bottom">
        <p>&copy; {{ currentYear }} {{ companyInfo?.company_name || 'ПРАВОЗАЩИТНИК' }}. Все права защищены.</p>
        <div class="footer-bottom-links">
          <a href="#">Политика конфиденциальности</a>
          <a href="#">Пользовательское соглашение</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import { computed, onMounted } from 'vue'
import { useLawyerStore } from '../stores/lawyer'
import { storeToRefs } from 'pinia'

export default {
  name: 'AppFooter',
  emits: ['open-modal'],
  setup() {
    const store = useLawyerStore()
    const { companyInfo, services, lawyers } = storeToRefs(store)

    const currentYear = new Date().getFullYear()

    const mainLawyer = computed(() => {
      return lawyers.value[0] || null
    })

    onMounted(() => {
      if (!companyInfo.value) {
        store.fetchCompanyInfo()
      }
      if (services.value.length === 0) {
        store.fetchServices()
      }
      if (lawyers.value.length === 0) {
        store.fetchLawyers()
      }
    })

    return {
      companyInfo,
      services,
      mainLawyer,
      currentYear,
    }
  },
}
</script>

<style scoped>
.footer {
  background: var(--dark-color);
  color: var(--white);
  padding: 60px 0 20px;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 40px;
  margin-bottom: 40px;
}

.footer-col h3 {
  color: var(--primary-color);
  font-size: 24px;
  margin-bottom: 15px;
}

.footer-col h4 {
  color: var(--white);
  font-size: 18px;
  margin-bottom: 20px;
}

.footer-col p {
  color: #ccc;
  line-height: 1.6;
}

.footer-social {
  display: flex;
  gap: 15px;
  margin-top: 15px;
}

.social-link {
  color: var(--white);
  background: rgba(255, 255, 255, 0.1);
  padding: 8px 15px;
  border-radius: var(--radius-sm);
  font-size: 14px;
}

.social-link:hover {
  background: var(--primary-color);
}

.footer-links {
  list-style: none;
}

.footer-links li {
  margin-bottom: 10px;
}

.footer-links a {
  color: #ccc;
}

.footer-links a:hover {
  color: var(--primary-color);
}

.footer-contacts {
  list-style: none;
}

.footer-contacts li {
  display: flex;
  gap: 10px;
  margin-bottom: 15px;
  align-items: flex-start;
}

.footer-contacts a {
  color: #ccc;
}

.footer-contacts a:hover {
  color: var(--primary-color);
}

.footer-lawyer-card {
  background: rgba(255, 255, 255, 0.05);
  padding: 20px;
  border-radius: var(--radius-sm);
  text-align: center;
}

.lawyer-photo {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  margin: 0 auto 15px;
}

.lawyer-name {
  font-weight: 600;
  margin-bottom: 5px;
}

.lawyer-position {
  font-size: 14px;
  color: #ccc;
  margin-bottom: 15px;
}

.btn-block {
  width: 100%;
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-bottom p {
  color: #ccc;
  margin: 0;
}

.footer-bottom-links {
  display: flex;
  gap: 20px;
}

.footer-bottom-links a {
  color: #ccc;
  font-size: 14px;
}

.footer-bottom-links a:hover {
  color: var(--primary-color);
}

/* Responsive */
@media (max-width: 992px) {
  .footer-content {
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
  }
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
  }

  .footer-bottom {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }

  .footer-bottom-links {
    flex-direction: column;
    gap: 10px;
  }
}
</style>


