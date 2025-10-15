<template>
  <section id="reviews" class="section reviews-section">
    <div class="container">
      <h2 class="section-title">Отзывы клиентов</h2>
      
      <div v-if="loading" class="loading">Загрузка отзывов...</div>
      
      <swiper
        v-else-if="reviews.length"
        :modules="modules"
        :slides-per-view="1"
        :space-between="30"
        :loop="true"
        :autoplay="{ delay: 7000, disableOnInteraction: false }"
        :pagination="{ clickable: true }"
        :navigation="true"
        :breakpoints="{
          768: { slidesPerView: 2 },
          1024: { slidesPerView: 3 }
        }"
        class="reviews-swiper"
      >
        <swiper-slide v-for="review in reviews" :key="review.id">
          <div class="review-card card">
            <div class="review-header">
              <div class="review-avatar">
                <img v-if="review.photo" :src="review.photo" :alt="review.client_name" />
                <span v-else>👤</span>
              </div>
              <div class="review-client-info">
                <h4 class="client-name">{{ review.client_name }}</h4>
                <p v-if="review.client_company" class="client-company">{{ review.client_company }}</p>
                <p v-if="review.date" class="review-date">{{ review.date }}</p>
              </div>
            </div>
            <div class="review-text">
              <p>"{{ review.text }}"</p>
            </div>
            <div class="review-rating">
              ⭐⭐⭐⭐⭐
            </div>
          </div>
        </swiper-slide>
      </swiper>
      
      <div v-else class="no-reviews">
        <p>Отзывов пока нет</p>
      </div>
    </div>
  </section>
</template>

<script>
import { onMounted } from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Navigation, Pagination, Autoplay } from 'swiper/modules'
import { useLawyerStore } from '../stores/lawyer'
import { storeToRefs } from 'pinia'

import 'swiper/css'
import 'swiper/css/navigation'
import 'swiper/css/pagination'

export default {
  name: 'ReviewsSection',
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    const store = useLawyerStore()
    const { reviews, loading } = storeToRefs(store)

    onMounted(() => {
      if (reviews.value.length === 0) {
        store.fetchReviews()
      }
    })

    return {
      reviews,
      loading,
      modules: [Navigation, Pagination, Autoplay],
    }
  },
}
</script>

<style scoped>
.reviews-section {
  background: var(--white);
}

.reviews-swiper {
  padding: 20px 50px 60px;
}

.review-card {
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.review-header {
  display: flex;
  gap: 15px;
  align-items: center;
}

.review-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  overflow: hidden;
  background: var(--bg-light);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.review-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.review-avatar span {
  font-size: 32px;
}

.review-client-info {
  flex: 1;
}

.client-name {
  font-size: 18px;
  font-weight: 700;
  color: var(--dark-color);
  margin-bottom: 5px;
}

.client-company {
  color: var(--primary-color);
  font-size: 14px;
  margin-bottom: 3px;
}

.review-date {
  color: var(--text-light);
  font-size: 13px;
}

.review-text {
  flex: 1;
  color: var(--text-light);
  line-height: 1.6;
  font-style: italic;
}

.review-rating {
  font-size: 20px;
  color: #FFD700;
}

.no-reviews {
  text-align: center;
  padding: 40px;
  color: var(--text-light);
}

/* Swiper custom styles */
:deep(.swiper-button-next),
:deep(.swiper-button-prev) {
  color: var(--primary-color);
}

:deep(.swiper-pagination-bullet) {
  background: var(--text-light);
}

:deep(.swiper-pagination-bullet-active) {
  background: var(--primary-color);
}

/* Responsive */
@media (max-width: 768px) {
  .reviews-swiper {
    padding: 20px 40px 60px;
  }
  
  .review-card {
    padding: 25px;
  }
}

@media (max-width: 480px) {
  .reviews-swiper {
    padding: 20px 30px 60px;
  }
}
</style>


