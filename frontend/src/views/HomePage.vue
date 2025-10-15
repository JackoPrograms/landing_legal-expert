<template>
  <div class="home-page">
    <HeroSection @open-modal="$emit('open-modal')" />
    <ServicesSection />
    <AboutSection @open-modal="$emit('open-modal')" />
    <LawyersSection />
    <ReviewsSection />
    <ArticlesSection />
  </div>
</template>

<script>
import { onMounted } from 'vue'
import { useLawyerStore } from '../stores/lawyer'
import HeroSection from '../components/HeroSection.vue'
import ServicesSection from '../components/ServicesSection.vue'
import AboutSection from '../components/AboutSection.vue'
import LawyersSection from '../components/LawyersSection.vue'
import ReviewsSection from '../components/ReviewsSection.vue'
import ArticlesSection from '../components/ArticlesSection.vue'

export default {
  name: 'HomePage',
  components: {
    HeroSection,
    ServicesSection,
    AboutSection,
    LawyersSection,
    ReviewsSection,
    ArticlesSection,
  },
  emits: ['open-modal'],
  setup() {
    const store = useLawyerStore()

    onMounted(() => {
      // Загружаем все данные при монтировании страницы
      store.loadAllData()
    })

    return {}
  },
}
</script>

<style scoped>
.home-page {
  min-height: 100vh;
}
</style>


