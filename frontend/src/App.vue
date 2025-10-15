<template>
  <div id="app">
    <AppHeader @open-modal="isModalOpen = true" />
    <router-view />
    <AppFooter @open-modal="isModalOpen = true" />
    <ContactModal :is-open="isModalOpen" @close="isModalOpen = false" />
  </div>
</template>

<script>
import { ref } from 'vue'
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
import ContactModal from './components/ContactModal.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter,
    ContactModal,
  },
  setup() {
    const isModalOpen = ref(false)

    return {
      isModalOpen,
    }
  },
}
</script>

<style>
/* Глобальные стили будут в assets/main.css */
</style>


