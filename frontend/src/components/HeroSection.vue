<template>
  <section class="hero-section">
        <swiper
          :modules="modules"
          :slides-per-view="1"
          :space-between="0"
          :loop="true"
          :autoplay="{ delay: 5000, disableOnInteraction: false }"
          :pagination="{ clickable: true }"
          :navigation="false"
          class="hero-swiper"
          ref="swiperRef"
        >
      <swiper-slide>
        <div class="hero-slide" :style="{ backgroundImage: `url(/images/Rectangle3.png)` }">
          <div class="hero-overlay"></div>
          <div class="container">
            <div class="hero-content">
              <h1 class="hero-title">Профессиональная юридическая помощь</h1>
              <p class="hero-subtitle">Более 15 лет успешной практики. Защитим ваши интересы в любой ситуации</p>
              <a href="#contact" class="btn btn-primary btn-lg">
                Записаться на консультацию
              </a>
            </div>
          </div>
        </div>
      </swiper-slide>
      
      <swiper-slide>
        <div class="hero-slide" :style="{ backgroundImage: `url(/images/Rectangle3.png)` }">
          <div class="hero-overlay"></div>
          <div class="container">
            <div class="hero-content">
              <h1 class="hero-title">Защита ваших прав - наша миссия</h1>
              <p class="hero-subtitle">Индивидуальный подход к каждому клиенту. Опытные юристы по всем отраслям права</p>
              <a href="#services" class="btn btn-primary btn-lg">
                Узнать больше
              </a>
            </div>
          </div>
        </div>
          </swiper-slide>
        </swiper>
        
        <!-- Custom Navigation -->
        <div class="custom-navigation">
          <button class="nav-arrow nav-prev" @click="prevSlide">‹</button>
          <span class="nav-slash">/</span>
          <button class="nav-arrow nav-next" @click="nextSlide">›</button>
        </div>
      </section>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Navigation, Pagination, Autoplay } from 'swiper/modules'
import { ref } from 'vue'

// Import Swiper styles
import 'swiper/css'
import 'swiper/css/navigation'
import 'swiper/css/pagination'

export default {
  name: 'HeroSection',
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    const swiperRef = ref(null)
    
    const prevSlide = () => {
      if (swiperRef.value && swiperRef.value.$el && swiperRef.value.$el.swiper) {
        swiperRef.value.$el.swiper.slidePrev()
      }
    }
    
    const nextSlide = () => {
      if (swiperRef.value && swiperRef.value.$el && swiperRef.value.$el.swiper) {
        swiperRef.value.$el.swiper.slideNext()
      }
    }
    
    return {
      modules: [Navigation, Pagination, Autoplay],
      swiperRef,
      prevSlide,
      nextSlide,
    }
  },
}
</script>

<style scoped>
.hero-section {
  position: relative;
  width: 100%;
  z-index: 999;
}

.hero-swiper {
  width: 100%;
  height: 820px;
}

.hero-slide {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  position: relative;
  display: flex;
  align-items: center;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1;
}

  .hero-content {
    position: relative;
    z-index: 2;
    color: var(--white);
    max-width: 700px;
    padding-top: 60px;
  }

.hero-title {
  font-size: 56px;
  font-weight: 800;
  margin-bottom: 20px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.hero-subtitle {
  font-size: 20px;
  margin-bottom: 30px;
  line-height: 1.6;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.btn-lg {
  padding: 16px 40px;
  font-size: 18px;
}

/* Swiper custom styles */
:deep(.swiper-button-next),
:deep(.swiper-button-prev) {
  color: #4F8FF0;
  background: transparent;
  border: none;
  width: 20px;
  height: 20px;
  border-radius: 0;
  top: auto !important;
  bottom: 20px !important;
  left: auto !important;
  right: calc((100% - 1200px) / 2 + 20px) !important;
}

:deep(.swiper-button-next::after),
:deep(.swiper-button-prev::after) {
  font-size: 12px;
}

:deep(.swiper-button-prev) {
  left: auto !important;
  right: calc((100% - 1200px) / 2 + 50px) !important;
}

/* Hide default navigation */
:deep(.swiper-button-next),
:deep(.swiper-button-prev) {
  display: none !important;
}

/* Custom Navigation */
.custom-navigation {
  position: absolute;
  bottom: 20px;
  right: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
  z-index: 10;
}

.nav-arrow {
  background: transparent;
  border: none;
  color: #FFFFFF;
  font-size: 36px;
  font-weight: 300;
  cursor: pointer;
  padding: 0;
  line-height: 1;
  transition: var(--transition-fast);
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 29px;
}

.nav-arrow:hover {
  color: #4F8FF0;
}

.nav-slash {
  color: #FFFFFF;
  font-size: 29px;
  font-weight: normal;
  line-height: 1;
}


/* Custom Pagination - Vertical Bars */
:deep(.swiper-pagination) {
  position: absolute;
  left: 20px !important;
  bottom: 20px !important;
  width: auto !important;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  gap: 8px;
}

/* Desktop positioning - align with container */
@media (min-width: 1201px) {
  :deep(.swiper-pagination) {
    left: calc((100% - 1200px) / 2 + 20px) !important;
  }

  .custom-navigation {
    right: calc((100% - 1200px) / 2 + 20px);
  }
}

:deep(.swiper-pagination-bullet) {
  width: 4px !important;
  height: 40px !important;
  background: rgba(255, 255, 255, 0.6) !important;
  border-radius: 0 !important;
  opacity: 1 !important;
  margin: 0 !important;
}

:deep(.swiper-pagination-bullet-active) {
  background: #4F8FF0 !important;
  height: 60px !important;
  opacity: 1 !important;
}

/* Tablet Styles (835px and below) */
@media (max-width: 835px) {
  .hero-swiper {
    height: 529px;
  }

  .hero-content {
    max-width: 100%;
    padding-top: 20px;
    padding-left: 15px;
    padding-right: 15px;
  }

  .hero-title {
    font-size: 36px;
    margin-bottom: 15px;
  }

  .hero-subtitle {
    font-size: 16px;
    margin-bottom: 25px;
  }

  .btn-lg {
    padding: 14px 30px;
    font-size: 16px;
  }

  /* Adjust pagination and navigation for tablet */
  :deep(.swiper-pagination) {
    left: 15px !important;
    bottom: 15px !important;
  }

  .custom-navigation {
    right: 15px;
    bottom: 15px;
  }

  .nav-arrow {
    font-size: 28px;
    width: 18px;
    height: 25px;
  }

  .nav-slash {
    font-size: 25px;
  }

  :deep(.swiper-pagination-bullet) {
    width: 3px !important;
    height: 30px !important;
  }

  :deep(.swiper-pagination-bullet-active) {
    height: 45px !important;
  }
}

/* Mobile Styles (390px and below) */
@media (max-width: 390px) {
  .hero-swiper {
    height: 486px;
  }

  .hero-content {
    max-width: 100%;
    padding-top: 20px;
    padding-left: 10px;
    padding-right: 10px;
  }

  .hero-title {
    font-size: 28px;
    margin-bottom: 12px;
  }

  .hero-subtitle {
    font-size: 14px;
    margin-bottom: 20px;
  }

  .btn-lg {
    padding: 12px 24px;
    font-size: 14px;
  }

  /* Hide pagination and navigation on mobile */
  :deep(.swiper-pagination) {
    display: none !important;
  }

  .custom-navigation {
    display: none !important;
  }
}
</style>


